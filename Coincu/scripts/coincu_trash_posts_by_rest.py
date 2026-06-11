#!/usr/bin/env python3
import argparse
import base64
import csv
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def norm_url(url: str) -> str:
    return (url or "").strip().rstrip("/")


def slug_from_url(url: str) -> str:
    path = urlparse(url).path.strip("/")
    return path.split("/")[-1] if path else ""


def chunked(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def auth_header(user: str, app_password: str) -> str:
    raw = f"{user}:{app_password}".encode()
    return "Basic " + base64.b64encode(raw).decode()


def get_json(url: str, auth: str, timeout: int = 60):
    req = Request(url, headers={"Authorization": auth, "User-Agent": "Codex Coincu Cleanup"})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def delete_post(base_url: str, post_id: int, auth: str, timeout: int = 60):
    url = f"{base_url.rstrip('/')}/wp-json/wp/v2/posts/{post_id}"
    req = Request(
        url,
        headers={"Authorization": auth, "User-Agent": "Codex Coincu Cleanup"},
        method="DELETE",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body) if body else {}
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        payload = {}
        if body:
            try:
                payload = json.loads(body)
            except json.JSONDecodeError:
                payload = {"raw": body[:500]}
        return e.code, payload
    except URLError as e:
        return 0, {"error": str(e)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--site", required=True)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--lookup-size", type=int, default=100)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--sleep", type=float, default=0.05)
    args = parser.parse_args()

    user = os.environ.get("COINCU_WP_USER", "")
    app_password = os.environ.get("COINCU_WP_APP_PASSWORD", "")
    if not user or not app_password:
        print("Missing COINCU_WP_USER or COINCU_WP_APP_PASSWORD", file=sys.stderr)
        return 2

    auth = auth_header(user, app_password)
    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("Input file is empty", file=sys.stderr)
        return 2

    existing_urls = set()
    if output_path.exists():
        with output_path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                existing_urls.add(norm_url(row.get("url", "")))

    pending_rows = [row for row in rows if norm_url(row.get("url", "")) not in existing_urls]

    fieldnames = list(rows[0].keys()) + [
        "post_id",
        "wp_status_before",
        "publish_date_live",
        "delete_http_code",
        "delete_result",
        "delete_wp_status_after",
        "deleted_at_utc",
    ]

    write_header = not output_path.exists()
    with output_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()

        total = len(pending_rows)
        total_batches = (total + args.batch_size - 1) // args.batch_size if total else 0
        for idx, source_batch in enumerate(chunked(pending_rows, args.batch_size), start=1):
            print(f"Lookup batch {idx}/{total_batches}: {len(source_batch)} URLs", flush=True)
            batch_by_url = {norm_url(row["url"]): dict(row) for row in source_batch if row.get("url")}
            slugs = [slug_from_url(row["url"]) for row in source_batch if row.get("url")]
            slugs = [slug for slug in slugs if slug]
            lookup_rows = []
            for lookup_chunk in chunked(slugs, args.lookup_size):
                lookup_url = (
                    f"{args.site.rstrip('/')}/wp-json/wp/v2/posts"
                    f"?per_page={args.lookup_size}&_fields=id,slug,link,date,status&slug={','.join(lookup_chunk)}"
                )
                try:
                    data = get_json(lookup_url, auth)
                except Exception as e:  # noqa: BLE001
                    print(f"Lookup chunk failed in batch {idx}: {e}", file=sys.stderr, flush=True)
                    data = []
                for item in data:
                    url = norm_url(item.get("link", ""))
                    if url not in batch_by_url:
                        continue
                    src = dict(batch_by_url[url])
                    src["post_id"] = item.get("id", "")
                    src["wp_status_before"] = item.get("status", "")
                    src["publish_date_live"] = item.get("date", "")
                    lookup_rows.append(src)
                time.sleep(args.sleep)

            found_urls = {norm_url(row.get("url", "")) for row in lookup_rows}
            for url, src in batch_by_url.items():
                if url in found_urls:
                    continue
                src["post_id"] = ""
                src["wp_status_before"] = ""
                src["publish_date_live"] = ""
                lookup_rows.append(src)

            print(f"Deleting batch {idx}/{total_batches}: {len(lookup_rows)} rows", flush=True)
            immediate_results = []
            delete_rows = []
            for row in lookup_rows:
                post_id = row.get("post_id")
                result = dict(row)
                result["deleted_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                if not post_id:
                    result["delete_http_code"] = ""
                    result["delete_result"] = "missing_post_id"
                    result["delete_wp_status_after"] = ""
                    immediate_results.append(result)
                else:
                    delete_rows.append(result)

            for result in immediate_results:
                writer.writerow(result)
            f.flush()

            with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
                future_map = {
                    executor.submit(delete_post, args.site, int(row["post_id"]), auth): row
                    for row in delete_rows
                }
                for future in as_completed(future_map):
                    result = future_map[future]
                    try:
                        status_code, payload = future.result()
                    except Exception as e:  # noqa: BLE001
                        status_code, payload = 0, {"error": str(e)}
                    result["delete_http_code"] = status_code
                    if status_code in (200, 202):
                        result["delete_result"] = "trashed" if payload.get("deleted") else "ok"
                        after = payload.get("previous", {}).get("status") or payload.get("status") or ""
                        result["delete_wp_status_after"] = after
                    else:
                        result["delete_result"] = payload.get("code") or payload.get("message") or payload.get("error") or "error"
                        result["delete_wp_status_after"] = payload.get("data", {}).get("status", "")
                    writer.writerow(result)
                    f.flush()
                    time.sleep(args.sleep)
            print(f"Completed batch {idx}/{total_batches}", flush=True)

    print(f"Finished. Results: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
