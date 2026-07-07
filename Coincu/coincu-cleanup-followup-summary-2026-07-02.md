# Coincu Cleanup Follow-up Summary

Date: `2026-07-02`

## 1. Former `draft_now` group current status

Source:
- `Coincu/coincu-pass1-draft-now-2026-06-16.csv`

Current status from WordPress REST `status=any`:
- total IDs: `24,095`
- `draft`: `1,273`
- `not_returned`: `22,822`
- `publish`: `0`

Logical buckets:
- `drafted`: `1,273`
- `not_public`: `22,822`
- `still_publish`: `0`

Key files:
- `Coincu/status-check-2026-07-02-final/coincu-draft-now-current-status-all-2026-07-02.csv`
- `Coincu/status-check-2026-07-02-final/coincu-draft-now-current-status-drafted-2026-07-02.csv`
- `Coincu/status-check-2026-07-02-final/coincu-draft-now-current-status-not-public-2026-07-02.csv`
- `Coincu/status-check-2026-07-02-final/coincu-draft-now-current-status-summary-2026-07-02.md`

## 2. Review recent `472` group

Source:
- `Coincu/coincu-pass1-review-recent-2026-06-16.csv`

Current status from WordPress REST `status=any`:
- total IDs: `472`
- `publish`: `88`
- `not_returned`: `384`

Next decision split:
- `draft_now`: `65`
- `manual_review`: `23`
- `already_not_public`: `384`

Top categories inside current `publish` review-recent set:
- `news`
- `ethereum`
- `markets`
- `bitcoin`
- `defi`
- `scam-alert`

Key files:
- `Coincu/review-recent-analysis-2026-07-02/coincu-review-recent-analysis-all-2026-07-02.csv`
- `Coincu/review-recent-analysis-2026-07-02/coincu-review-recent-draft_now-2026-07-02.csv`
- `Coincu/review-recent-analysis-2026-07-02/coincu-review-recent-manual_review-2026-07-02.csv`
- `Coincu/review-recent-analysis-2026-07-02/coincu-review-recent-analysis-summary-2026-07-02.md`

## 3. Practical next move

- Draft the `65` URLs in `review recent -> draft_now`
- Keep the `23` URLs in `manual_review` for a human pass
- Ignore the `384` already non-public URLs
