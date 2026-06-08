# Coincu 3rd Recrawl Audit

Source folder:
- `/home/thana2/coincu-3rd`

Key crawl counts:
- `internal_all.csv`: `98,374`
- `sitemaps_all.csv`: `65,571`
- `redirect_chains.csv`: `855`

## Main findings

### 1. Broken sitewide menu link causing `500`
- URL: `https://coincu.com/top-blockchain-ecosystems-tvl-defi`
- Crawl status: `500`
- Unique inlinks: `24,486`
- Source pattern: linked sitewide from `Header`, `Navigation`, and `main-menu`
- Anchor: `TVL Ranking`

Impact:
- High crawl waste
- Repeated internal link to server error page

### 2. Broken convert cluster is still linked sitewide
- Main route: `https://coincu.com/convert-crypto-to-fiat`
- Crawl status: `0` / `Connection Refused`
- Child routes under `/convert-crypto-to-fiat/*`: mostly `404`

Counts:
- `404` under `convert-crypto-to-fiat`: `8,504`
- `403` under `convert-crypto-to-fiat`: `219`
- `0` under `convert-crypto-to-fiat`: `1,199`

Source pattern:
- Sitewide content/widget block with anchor `Convert`

Impact:
- Major crawl waste
- Large volume of dead utility URLs being re-linked internally

### 3. Broken/forbidden article URLs are still pushed by content widgets
- Example URL: `https://coincu.com/bitcoin-breaks-above-64000/`
- Crawl status: `403`
- Unique inlinks: `16,397`

Source pattern:
- Repeated in article body widgets
- `popular-posts`
- inline text blocks

Impact:
- High internal link pressure to forbidden content

### 4. Broken author links remain inside content
Examples:
- `https://coincu.com/author/Victor` `404`, unique inlinks `697`
- `https://coincu.com/author/Akinyemi%20Okedeji%20Amoo` `404`, unique inlinks `264`
- `https://coincu.com/author/Liam%20Zhang` `404`, unique inlinks `134`
- `https://coincu.com/author/Yuna%20Kim` `404`, unique inlinks `86`

Source pattern:
- Content links inside pages, especially `/t/` pages and old content blocks

Impact:
- Internal links to dead author archives

### 5. Old `/c/` routes still heavily linked internally
Examples:
- `/c/casino-reviews/` -> `301`, unique inlinks `11,252`
- `/c/pr/press-release/` -> `301`, unique inlinks `11,251`
- `/c/news` -> `301`, unique inlinks `6,378`
- `/c/news/`, `/c/markets/`, `/c/knowledge/` -> `301`, each `1,262`

Impact:
- Avoidable internal redirects remain widespread

### 6. Tag and currency route layer is still unhealthy
Counts:
- `403` under `/t/`: `2,279`
- `404` under `/currencies/`: `61`
- `403` under `/currencies/`: `9`

Impact:
- Archive/utility route system is broken or intentionally blocked but still linked

### 7. External `302` redirect loops concentrate in `top-crypto-coins`
Redirect chains:
- Total rows: `855`
- Main final domains:
  - `www.kucoin.com`: `450`
  - `www.bybitglobal.com`: `260`

Source pattern:
- `top-crypto-coins`: `589`

Impact:
- Low-quality crawl churn from affiliate / exchange links

### 8. Current `404` count is not mainly from the latest trash batch
From `internal_all.csv`:
- Total `404`: `10,625`
- Matching URLs from the `9,414` newly trashed batch: only `238`

Meaning:
- Most current `404` URLs come from other broken route systems, not from the latest planned deletion

## Priority order

### P1
1. Fix or remove the sitewide `TVL Ranking` link that returns `500`
2. Disable or fix the `Convert` widget / route cluster
3. Stop content widgets from linking to `403` article URLs like `bitcoin-breaks-above-64000`

### P2
4. Fix broken author links or restore the intended author archive routes
5. Replace internal `/c/` links with final canonical routes
6. Decide whether `/t/` and `/currencies/` should be live, noindex, or unlinked

### P3
7. Clean the `top-crypto-coins` exchange link / `302` loop cluster
8. Revisit media `403` / `wp-content` layer separately

