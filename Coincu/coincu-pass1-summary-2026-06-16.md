# Coincu Pass 1 Summary

Date: `2026-06-16`

Logic used in this version:
- inventory: live published posts fetched from WP REST
- signal join: by slug, not exact URL, because Coincu has route/permalink drift
- keep: slug has backlinks or appears in GSC top pages export with clicks/impressions
- review: no backlink, no GSC signal, published in last 30 days
- draft_now: no backlink, no GSC signal, older than 30 days

- total published posts in REST inventory: `27693`
- keep: `3126`
- review recent: `472`
- draft_now: `24095`
- keep with backlink signal: `3083`
- keep with GSC 3m signal: `86`
