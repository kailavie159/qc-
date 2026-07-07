# Coincu Crawled Not Indexed Recommended Actions

Date: `2026-07-07`

Source files:
- `Coincu Audit Final/coincu.com-Coverage-Drilldown-2026-07-07/Bảng.csv`
- `Coincu/crawled-not-indexed-sample-splits-2026-07-07/coincu-crawled-not-indexed-sample-backlink-summary-2026-07-07.md`

Important note:
- this is based on a `1000 URL` GSC sample, not the full `300,514` URL set
- actions below are pattern-level recommendations, not final per-URL decisions

## 1. `convert-fiat-to-fiat`

Sample size:
- `104`

Backlink risk in sample:
- backlinks: `0`
- ref domains: `0`

Recommended action:
- remove from sitemap completely
- remove internal links pointing into this cluster
- if these pages are not meant to rank, keep them out of index
- if they must stay live for users, use `noindex`
- if they are junk/empty/generated variants, return `410` or stop generating them

Priority:
- `P1`

Reason:
- biggest cluster in sample
- zero backlink protection
- safest cluster to clean aggressively

## 2. `parameter URLs`

Sample size:
- `32`

Backlink risk in sample:
- backlinks: `1`
- ref domains: `1`

Recommended action:
- enforce canonical to the clean URL
- stop linking to parameterized versions internally
- exclude parameterized variants from sitemap
- if possible, normalize internal links so only canonical URLs are emitted

Priority:
- `P1`

Reason:
- low backlink risk
- classic crawl waste
- usually fixable without content decisions

## 3. `news.coincu.com` duplicate host layer

Sample size:
- `21`

Backlink risk in sample:
- backlinks: `17`
- ref domains: `7`

Recommended action:
- do not block blindly
- build a host-consolidation rule:
  - if root-domain equivalent exists and is the intended canonical, `301` subdomain URL to root canonical
  - if subdomain version is canonical, then root duplicate must not remain indexable
- remove duplicate host versions from sitemap
- audit internal links so only one host is linked

Priority:
- `P1`

Reason:
- duplicate-host problem creates crawl waste and canonical confusion
- some URLs already have backlink value
- wrong move here can waste link equity

## 4. `numeric slug` URLs

Sample size:
- `86`

Backlink risk in sample:
- backlinks: `262`
- ref domains: `61`

Recommended action:
- do not mass `410`
- build a redirect/canonical map first
- for each numeric-slug URL:
  - if a clean canonical equivalent exists, `301` to that exact canonical
  - if no equivalent exists but URL still has backlinks, decide a nearest valid replacement manually
  - only use `410` where there is clearly no value and no backlink support
- remove numeric variants from sitemap
- stop generating or internally linking numeric variants

Priority:
- `P0`

Reason:
- this is the highest-risk cluster in the sample
- clear backlink footprint
- likely contributes both crawl waste and equity fragmentation

## 5. `duplicate slug across hosts`

Sample size:
- `40`

Backlink risk in sample:
- backlinks: `16`
- ref domains: `6`

Recommended action:
- treat as a canonical/host duplication issue, not a content-pruning issue
- pick one canonical location per slug
- `301` the non-canonical version where possible
- ensure sitemap and internal links only emit the canonical host/path

Priority:
- `P1`

Reason:
- smaller than numeric-slug cluster
- still carries real backlink and duplication risk

## 6. Practical execution order

### First

- `convert-fiat-to-fiat`
- `parameter URLs`

These are the safest fast wins.

### Second

- `news.coincu.com`
- `duplicate slug across hosts`

These need consolidation logic, not blind removal.

### Third

- `numeric slug`

This needs a redirect map before any destructive action.

## 7. What I would do next

1. Export the full sample URL list grouped by:
- `convert-fiat-to-fiat`
- parameterized URLs
- `news.coincu.com`
- numeric slugs

2. For numeric slugs and host-duplicates:
- map each URL to its best canonical target

3. For convert/parameter clusters:
- verify whether they are still in sitemap
- verify whether they are still internally linked

4. After rules are live:
- recrawl those clusters only
- then validate in GSC
