## Coincu Duplicate Route Discovery Handoff

Date: 2026-05-15

Problem:
- Coincu is still generating or exposing multiple URL routes for what appears to be the same article slug
- This contributes to the large `Crawled - currently not indexed` bucket
- Live checks show some secondary routes already `301`, but Google is still discovering too many alternate URLs

### How To Fix Duplicate Route Discovery

Duplicate Route Discovery should be handled in 4 layers, in this order:

#### 1. Lock One Canonical Route Only

Keep:

- `https://coincu.com/{slug}/`

Do not keep parallel article routes such as:

- `/news/{slug}/`
- `/analysis/{slug}/`
- `/blockchain/{slug}/`
- `/markets/{slug}/`
- `/blockchain-event/{slug}/`

#### 2. 301 All Secondary Routes To The Canonical Route

Examples:

- `/news/doj-epstein-documents-release/` -> `/doj-epstein-documents-release/`
- `/analysis/ada-breakdown-looms/` -> `/ada-breakdown-looms/`
- `/blockchain/agentlisa-funding-ai-security/` -> `/agentlisa-funding-ai-security/`

This is already partly true on the live site. The next step is not just adding more redirects. The next step is cleaning the sources that continue to emit those secondary routes.

#### 3. Cut Every Source That Still Emits Secondary Routes

This is the most important layer.

Check and fix:

- sitemap output
- breadcrumbs
- category modules
- related posts
- home/category blocks
- old feeds
- internal links inside articles
- any custom permalink/plugin logic still printing `/news/{slug}/`, `/analysis/{slug}/`, or similar prefixed routes

If those sources are not cleaned, Google will keep crawling the secondary routes even if they already `301`.

#### 4. Recheck With Real Samples

After cleanup:

- crawl the site again
- confirm internal links only point to `/{slug}/`
- confirm secondary routes still `301` when hit directly
- confirm sitemap only contains `/{slug}/`

### Practical Dev/WP Checklist

- Canonical article URL: only `/{slug}/`
- Secondary article routes: always `301` to `/{slug}/`
- Do not include secondary routes in sitemap
- Do not render secondary routes in internal links, modules, or widgets
- Do not leave query variants such as `?noamp=mobile` discoverable

### Live Examples Verified

- `/news/doj-epstein-documents-release/` -> `/doj-epstein-documents-release/`
- `/analysis/ada-breakdown-looms/` -> `/ada-breakdown-looms/`
- `/blockchain/agentlisa-funding-ai-security/` -> `/agentlisa-funding-ai-security/`
- `/markets/ethereum-treasury-plan-shelved/` -> `/ethereum-treasury-plan-shelved/`
- `/blockchain-event/digital-assets-forum/` -> `/digital-assets-forum/`
- `/news/sec-delays-solana-etf-decision/?noamp=mobile` -> `/sec-delays-solana-etf-decision/?noamp=mobile`

### Expected Outcome

- fewer alternate article URLs discovered by Google
- less crawl waste on duplicate routes
- cleaner sitemap and internal-link graph
- better chance for canonical article URLs to get indexed
