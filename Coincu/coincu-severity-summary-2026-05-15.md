## Coincu Severity Summary - 2026-05-15

### Critical

- **Indexed pages collapsed sitewide**
  - Indexed pages fell from about `191,021` on `February 14, 2026` to about `69,597` on `March 11, 2026`.
  - They then fell again to about `17,951` on `April 19, 2026`, `13,179` on `April 28, 2026`, `8,437` on `May 2, 2026`, and `7,561` on `May 5-8, 2026`.
  - This is a full indexing incident, not a normal fluctuation.

- **`Crawled - currently not indexed` is extremely large**
  - Current count in local GSC export: `313,386`
  - This is the strongest direct sign that Google is seeing URLs but refusing to keep them indexed at scale.

- **Sitemap/discovery pollution is severe**
  - Local crawl found sitemap inclusion for bad URL classes such as `/wp-content/`, `/convert-crypto-to-fiat/`, `/wp-admin/`, and `/coincu-login/`.
  - Sitemap status mix also includes `301`, `403`, and `404`, which is highly damaging to clean indexation.

### High

- **Legacy media cluster is broken**
  - `21,166` image URLs in the broken-image batch return `403`.
  - `32,231` legacy image URLs return `301`.
  - `99.04%` of `403` image errors are concentrated in `2022/07` to `2022/12`.
  - `99.82%` of `301` legacy image redirects are concentrated in `2022/07` to `2023/06`.
  - This is a real media-layer problem, not just a content formatting problem.

- **Dead URL sets and wasteful crawl demand**
  - `404`: `8,531`
  - `Redirect`: `8,069`
  - `/convert-crypto-to-fiat/` is a large dead set and should not keep feeding crawl demand.

- **`Discovered - currently not indexed` remains large**
  - Current count in local export: `33,438`
  - This suggests Google is finding large numbers of low-priority or low-trust URLs that never earn indexing.

### Medium

- **Robots/search-result noise**
  - `Blocked by robots.txt`: `4,033`
  - Search-result URLs and utility pages still appear in the incident pattern and add noise.

- **5xx and redirect-error noise**
  - `5xx`: `219`
  - `Redirect error`: `413`
  - Smaller than the main collapse drivers, but still harmful when combined with the wider crawl/index mess.

- **Intentional noindex buckets still need discipline**
  - `Noindex`: `10,037`
  - Tag and archive policy may be intentional, but these buckets still need to stay out of the wrong discovery surfaces.

### Main Interpretation

- The site was already weakening in search performance in mid-`2025`.
- A major indexing collapse began on `February 14, 2026`.
- A second major collapse wave started in late `April 2026` and worsened again in early `May 2026`.
- The damage is not driven by one bug. It is a compound failure across index quality, sitemap hygiene, dead URL sets, and legacy media delivery.

### Practical Priority Order

1. Stop bad discovery inputs: sitemap, dead URL sets, and stale search surfaces.
2. Reduce waste and noise: `404`, redirects, duplicates, and thin discovery paths.
3. Fix legacy media delivery for the broken `2022/07` to `2022/12` cluster.
4. Continue content-side cleanup with `410` and delete batches for stale posts.
