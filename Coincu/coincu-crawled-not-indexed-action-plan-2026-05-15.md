## Coincu Crawled - Currently Not Indexed Action Plan

Date: 2026-05-15

Primary GSC count:
- `313,386` URLs in `Crawled - currently not indexed`

This bucket should not be treated as one problem. On Coincu it is a mix of:
- duplicate route discovery
- query variant discovery
- real canonical URLs that are still weak or oversupplied

### What The Sample Shows

From the local sample file `batch2_gsc_crawled_not_indexed_sample.csv`, the clearest repeated pattern is:

- root article URL plus one prefixed route URL for the same slug

Examples:

- `/doj-epstein-documents-release/`
- `/news/doj-epstein-documents-release/`

- `/ada-breakdown-looms/`
- `/analysis/ada-breakdown-looms/`

- `/agentlisa-funding-ai-security/`
- `/blockchain/agentlisa-funding-ai-security/`

- `/digital-assets-forum/`
- `/blockchain-event/digital-assets-forum/`

- `/ethereum-treasury-plan-shelved/`
- `/markets/ethereum-treasury-plan-shelved/`

- `/sec-delays-solana-etf-decision/?noamp=mobile`
- `/news/sec-delays-solana-etf-decision/?noamp=mobile`

### Important Finding

The secondary prefixed routes in the sample are already returning `301` to the root slug in live checks.

Examples verified live:

- `/news/doj-epstein-documents-release/` -> `/doj-epstein-documents-release/`
- `/analysis/ada-breakdown-looms/` -> `/ada-breakdown-looms/`
- `/blockchain/agentlisa-funding-ai-security/` -> `/agentlisa-funding-ai-security/`
- `/markets/ethereum-treasury-plan-shelved/` -> `/ethereum-treasury-plan-shelved/`
- `/blockchain-event/digital-assets-forum/` -> `/digital-assets-forum/`

This means:
- route normalization is at least partially in place
- but Google is still discovering and crawling too many alternate paths
- and many root canonical URLs are still failing to earn indexation

So the `313k` problem is not just “missing redirects”.

### Real Diagnosis

There are three sub-problems:

#### 1. Duplicate Route Discovery

Google is still finding alternate route forms such as:

- `/news/slug/`
- `/analysis/slug/`
- `/blockchain/slug/`
- `/markets/slug/`
- `/blockchain-event/slug/`
- likely other section prefixes

Even if those now `301`, they still waste crawl if they remain linked internally, emitted in feeds, or historically present in sitemap/history.

#### 2. Query Variant Discovery

Sample includes URLs like:

- `/sec-delays-solana-etf-decision/?noamp=mobile`

These are low-value duplicates and should not remain discoverable.

#### 3. Canonical URLs Still Not Strong Enough

The root article URLs themselves also appear in the `Crawled - currently not indexed` sample.

That means even after normalization, many canonical URLs still have one or more of these problems:

- too much news volume relative to crawl/index capacity
- near-duplicate headlines/topics
- weak distinctiveness
- quality/trust drag from broader site issues such as broken media and indexing noise

### Action Plan

#### Phase 1: Reduce Discovery Noise

Goal:
- stop feeding Google unnecessary alternate URLs

Actions:

- Keep root slug as the canonical article route
- Ensure all section-prefixed article variants `301` to the root slug
- Remove section-prefixed article URLs from sitemap inputs completely
- Remove login/query/utility variants from sitemap inputs
- Remove `?noamp=mobile` and similar query variants from any internal links

Target route rule:

- `/news/{slug}/` -> `/{slug}/`
- `/analysis/{slug}/` -> `/{slug}/`
- `/blockchain/{slug}/` -> `/{slug}/`
- `/markets/{slug}/` -> `/{slug}/`
- `/blockchain-event/{slug}/` -> `/{slug}/`

#### Phase 2: Check Internal Link Sources

Goal:
- stop regenerating the same bad alternate URLs

Actions:

- audit breadcrumbs, category modules, widgets, and related-post blocks that may still output prefixed paths
- audit any custom post-type or permalink logic that may emit both root and section-prefixed article URLs
- check feeds, API outputs, and old sitemap plugins for stale prefixed URLs

#### Phase 3: Triage Canonical URLs Themselves

Goal:
- reduce the number of weak root URLs that Google crawls but declines to index

Actions:

- segment root canonical article URLs into:
  - keep and improve
  - merge/redirect
  - delete/410
- prioritize URLs with:
  - backlinks
  - impressions
  - strong evergreen potential
- deprioritize thin short-term news items with no links and no traction

### Practical Interpretation

Do not assume:
- “313k crawled not indexed” means Google just needs more time

Do assume:
- Coincu is producing more article-like URLs than Google currently wants to keep indexed
- route cleanup helps, but it will not solve the full bucket by itself
- the bucket will only fall meaningfully when both discovery noise and low-value content volume are reduced

### Priority Order

1. finish media recovery enough to reduce sitewide quality drag
2. clean sitemap/discovery sources for alternate routes and query variants
3. then batch-triage weak root canonical articles

### Sample Route Pairs To Reuse For Validation

- `/news/doj-epstein-documents-release/` -> `/doj-epstein-documents-release/`
- `/analysis/ada-breakdown-looms/` -> `/ada-breakdown-looms/`
- `/blockchain/agentlisa-funding-ai-security/` -> `/agentlisa-funding-ai-security/`
- `/markets/ethereum-treasury-plan-shelved/` -> `/ethereum-treasury-plan-shelved/`
- `/blockchain-event/digital-assets-forum/` -> `/digital-assets-forum/`
- `/news/sec-delays-solana-etf-decision/?noamp=mobile` -> `/sec-delays-solana-etf-decision/`

### Bottom Line

The fastest wrong move would be to treat the whole `313k` bucket as an indexing-request problem.

The right move is:
- reduce alternate URL discovery
- keep one article route only
- then cut or improve weak canonical articles at scale
