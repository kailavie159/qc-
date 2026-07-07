# Coincu Cleanup Final Rollup

Date: `2026-07-02`

## Scope

This rollup closes the workflow around:

- `coincu-pass1-draft-now-2026-06-16.csv`
- `coincu-pass1-review-recent-2026-06-16.csv`

## 1. Former `draft_now` bucket

Source size:
- `24,095` URLs

Current WordPress status via REST `status=any`:
- `draft`: `1,273`
- `not_returned`: `22,822`
- `publish`: `0`

Meaning:
- the `1,273` URLs that were still public were drafted successfully
- the remaining `22,822` are already non-public from the point of view of the current REST check
- there are now `0` public URLs left in this bucket

Key files:
- `Coincu/status-check-2026-07-02-final/coincu-draft-now-current-status-all-2026-07-02.csv`
- `Coincu/status-check-2026-07-02-final/coincu-draft-now-current-status-summary-2026-07-02.md`

## 2. `review recent` bucket

Source size:
- `472` URLs

Initial live-state split:
- `384` already non-public
- `88` still public

Decision split on the `88` public URLs:
- `65` moved into `draft_now`
- `23` moved into `manual_review`

Execution:
- `65 / 65` drafted successfully
- `23 / 23` drafted successfully
- public recheck after both runs: `0` still publish

Key files:
- `Coincu/review-recent-analysis-2026-07-02/coincu-review-recent-analysis-summary-2026-07-02.md`
- `Coincu/review-recent-draft-live-2026-07-02/coincu-review-recent-draft-summary-2026-07-02.md`
- `Coincu/review-recent-manual-draft-live-2026-07-02/coincu-review-recent-manual-draft-summary-2026-07-02.md`

## 3. Final operational status

From the buckets handled in this workflow:

- old `draft_now`: no URLs left public
- `review recent`: no URLs left public

Operationally, this means the cleanup action set for these two buckets is complete.

## 4. What remains outside this rollup

This file does not claim that all Coincu indexation or quality issues are solved sitewide.

It only closes the two specific triage buckets above.

Remaining SEO work, if needed, should move to:

- recrawl validation
- sitemap/indexation verification
- internal link cleanup follow-up
- route/template issues outside the post-status cleanup flow
