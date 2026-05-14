## Coincu Live Recheck - 2026-05-14

Summary:
- Do not start with article rewrites.
- Start with image delivery.

Live recheck on May 14, 2026 changed the earlier conclusion:
- `sitemap_index.xml` is currently reachable and points to `post`, `page`, `category`, `google-news`, and `local` sitemap groups.
- `/wp-content/` entries seen in sitemap exports are largely `image:image` references, so their presence alone is not the core issue.
- The largest live SEO issue is that many image URLs referenced through sitemap-related discovery do not return `200`.

Current counts from export analysis:
- `53,398` image URLs in sitemap-related exports are `non-200`
- `32,231` are old `news.coincu.com/...` media URLs returning `301`
- `21,166` are `coincu.com/wp-content/uploads/...` media URLs returning `403`

Representative live checks:
- `https://news.coincu.com/wp-content/uploads/2023/06/What-Is-A-Crypto-Airdrop-and-How-Does-It-Work.png` -> `301` -> final `200`
- `https://coincu.com/wp-content/uploads/2025/02/Kaito-Connect.avif` -> `200`
- `https://coincu.com/wp-content/uploads/2023/10/so5.pngon` -> `403`
- `https://coincu.com/wp-content/uploads/2022/08/image-459.png` -> `403`

Interpretation:
- The image-index loss is more likely tied to media delivery, redirect behavior, and blocked legacy uploads than to the main sitemap index endpoint itself.

First actions:
1. Check the layer blocking old and current uploads, most likely Cloudflare, WAF, hotlink, or media rules.
2. Make representative old and current upload image URLs return `200`, not `403`.
3. Gradually replace legacy `news.coincu.com/wp-content/uploads/` image references in old content with `coincu.com/wp-content/uploads/` where those references are still embedded.

Primary batch file:
- [coincu-batch1-broken-sitemap-images-2026-05-14.csv](/home/thana2/screaming-frow/Coincu/coincu-batch1-broken-sitemap-images-2026-05-14.csv:1)
