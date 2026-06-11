#!/usr/bin/env python3
import argparse
import base64
import csv
import json
import os
import sys
import time
from collections import OrderedDict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


USER_AGENT = "Codex Coincu Cleanup"


def norm_url(url: str) -> str:
    return (url or "").strip().rstrip("/")


def slug_from_url(url: str) -> str:
    path = urlparse(url).path.strip("/")
    return path.split("/")[-1] if path else ""


def auth_header(user: str, app_password: str) -> str:
    raw = f"{user}:{app_password}".encode()
    return "Basic " + base64.b64encode(raw).decode()


def get_json(url: str, auth: str, timeout: int = 60):
    req = Request(url, headers={"Authorization": auth, "User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def post_json(url: str, auth: str, payload: dict, timeout: int = 60):
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        url,
        data=body,
        headers={
            "Authorization": auth,
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, json.loads(raw) if raw else {}
    except HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        payload = {}
        if raw:
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {"raw": raw[:500]}
        return e.code, payload
    except URLError as e:
        return 0, {"error": str(e)}


def normalize_target_path(path: str) -> str:
    clean = path.strip()
    if not clean.startswith("/"):
        clean = "/" + clean
    if clean != "/" and not clean.endswith("/"):
        clean += "/"
    return clean


def map_old_url_to_new(old_url: str, site: str) -> str:
    parsed = urlparse(old_url)
    path = parsed.path or "/"
    if path in ("/c/market", "/c/market/"):
        new_path = "/markets/"
    elif path in ("/c/cmc", "/c/cmc/"):
        new_path = "/cmc/"
    elif path.startswith("/c/"):
        new_path = normalize_target_path(path[2:])
    else:
        return old_url
    return site.rstrip("/") + new_path


def build_candidates(detail_path: Path, site: str):
    grouped = OrderedDict()
    with detail_path.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            source_url = row.get("source_url", "").strip()
            old_url = row.get("destination_url", "").strip()
            if not source_url or not old_url:
                continue
            new_url = map_old_url_to_new(old_url, site)
            if norm_url(new_url) == norm_url(old_url):
                continue
            bucket = grouped.setdefault(
                source_url,
                {
                    "source_url": source_url,
                    "source_type": "",
                    "items": OrderedDict(),
                },
            )
            bucket["source_type"] = row.get("link_origin", "") or bucket["source_type"]
            bucket["items"].setdefault(old_url, new_url)
    return grouped


def lookup_source(site: str, auth: str, source_url: str, timeout: int = 60):
    slug = slug_from_url(source_url)
    if not slug:
        return None
    for source_type in ("posts", "pages"):
        lookup_url = (
            f"{site.rstrip('/')}/wp-json/wp/v2/{source_type}"
            f"?slug={slug}&context=edit&_fields=id,slug,link,status,type,content"
        )
        try:
            data = get_json(lookup_url, auth, timeout=timeout)
        except Exception:
            continue
        if not data:
            continue
        item = data[0]
        if norm_url(item.get("link", "")) != norm_url(source_url):
            continue
        return {
            "source_type": source_type,
            "source_id": item.get("id", ""),
            "source_post_status": item.get("status", ""),
            "link": item.get("link", ""),
            "raw": item.get("content", {}).get("raw", ""),
        }
    return None


def update_source(site: str, auth: str, source_type: str, source_id: int, raw_content: str, timeout: int = 60):
    url = f"{site.rstrip('/')}/wp-json/wp/v2/{source_type}/{source_id}"
    status_code, payload = post_json(url, auth, {"content": raw_content}, timeout=timeout)
    return status_code, payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-results", required=True)
    parser.add_argument("--output-details", required=True)
    parser.add_argument("--site", required=True)
    parser.add_argument("--max-updates", type=int, default=10)
    parser.add_argument("--scan-limit", type=int, default=1000)
    parser.add_argument("--sleep", type=float, default=0.2)
    args = parser.parse_args()

    user = os.environ.get("COINCU_WP_USER", "")
    app_password = os.environ.get("COINCU_WP_APP_PASSWORD", "")
    if not user or not app_password:
        print("Missing COINCU_WP_USER or COINCU_WP_APP_PASSWORD", file=sys.stderr)
        return 2

    auth = auth_header(user, app_password)
    input_path = Path(args.input)
    results_path = Path(args.output_results)
    details_path = Path(args.output_details)
    results_path.parent.mkdir(parents=True, exist_ok=True)
    details_path.parent.mkdir(parents=True, exist_ok=True)

    grouped = build_candidates(input_path, args.site)
    if not grouped:
        print("No candidate URLs found", file=sys.stderr)
        return 2

    result_fields = [
        "source_url",
        "source_type",
        "source_id",
        "source_post_status",
        "candidate_link_rows",
        "matched_link_rows",
        "replaced_occurrences",
        "updated_live",
        "result_status",
        "note",
    ]
    detail_fields = [
        "source_url",
        "source_type",
        "source_id",
        "old_link",
        "new_link",
        "old_count_found_in_raw",
        "status",
    ]

    updated_count = 0
    scanned_count = 0

    with results_path.open("w", newline="", encoding="utf-8") as results_file, details_path.open(
        "w", newline="", encoding="utf-8"
    ) as details_file:
        results_writer = csv.DictWriter(results_file, fieldnames=result_fields)
        details_writer = csv.DictWriter(details_file, fieldnames=detail_fields)
        results_writer.writeheader()
        details_writer.writeheader()

        for source_url, group in grouped.items():
            if scanned_count >= args.scan_limit or updated_count >= args.max_updates:
                break
            scanned_count += 1
            resolved = lookup_source(args.site, auth, source_url)
            if not resolved:
                results_writer.writerow(
                    {
                        "source_url": source_url,
                        "source_type": "",
                        "source_id": "",
                        "source_post_status": "",
                        "candidate_link_rows": len(group["items"]),
                        "matched_link_rows": 0,
                        "replaced_occurrences": 0,
                        "updated_live": "no",
                        "result_status": "missing_post_id",
                        "note": "Could not resolve source URL to posts/pages via REST",
                    }
                )
                results_file.flush()
                continue

            raw = resolved["raw"]
            replaced_content = raw
            matched_link_rows = 0
            replaced_occurrences = 0
            per_link_rows = []
            for old_link, new_link in group["items"].items():
                old_count = replaced_content.count(old_link)
                if old_count:
                    matched_link_rows += 1
                    replaced_occurrences += old_count
                    replaced_content = replaced_content.replace(old_link, new_link)
                    status = "replaced"
                else:
                    status = "no_match_in_raw"
                per_link_rows.append(
                    {
                        "source_url": source_url,
                        "source_type": resolved["source_type"],
                        "source_id": resolved["source_id"],
                        "old_link": old_link,
                        "new_link": new_link,
                        "old_count_found_in_raw": old_count,
                        "status": status,
                    }
                )

            if matched_link_rows == 0:
                results_writer.writerow(
                    {
                        "source_url": source_url,
                        "source_type": resolved["source_type"],
                        "source_id": resolved["source_id"],
                        "source_post_status": resolved["source_post_status"],
                        "candidate_link_rows": len(group["items"]),
                        "matched_link_rows": 0,
                        "replaced_occurrences": 0,
                        "updated_live": "no",
                        "result_status": "no_match_in_raw",
                        "note": "No candidate old URLs found in current raw content",
                    }
                )
                for row in per_link_rows:
                    details_writer.writerow(row)
                results_file.flush()
                details_file.flush()
                continue

            status_code, payload = update_source(
                args.site,
                auth,
                resolved["source_type"],
                int(resolved["source_id"]),
                replaced_content,
            )
            if status_code in (200, 201):
                updated_live = "yes"
                result_status = "ok"
                note = ""
                updated_count += 1
            else:
                updated_live = "no"
                result_status = payload.get("code") or payload.get("message") or payload.get("error") or "update_failed"
                note = str(payload)[:500]

            results_writer.writerow(
                {
                    "source_url": source_url,
                    "source_type": resolved["source_type"],
                    "source_id": resolved["source_id"],
                    "source_post_status": resolved["source_post_status"],
                    "candidate_link_rows": len(group["items"]),
                    "matched_link_rows": matched_link_rows,
                    "replaced_occurrences": replaced_occurrences,
                    "updated_live": updated_live,
                    "result_status": result_status,
                    "note": note,
                }
            )
            for row in per_link_rows:
                details_writer.writerow(row)
            results_file.flush()
            details_file.flush()
            time.sleep(args.sleep)

    print(f"Scanned sources: {scanned_count}")
    print(f"Updated sources: {updated_count}")
    print(f"Results: {results_path}")
    print(f"Details: {details_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
