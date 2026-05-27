## Coincu Dev Handoff: Dọn Sitemap Đang Chứa URL 301

Ngày: `2026-05-27`

### Kết luận ngắn

Sitemap hiện tại của Coincu đang bẩn nặng.

Từ recrawl mới:

- tổng URL trong `sitemaps_all.csv`: `101,066`
- chỉ `20,967` URL là `200` indexable
- có:
  - `47,520` URL `301`
  - `5,385` URL `404`
  - `3,585` URL `403`
  - `139` URL `500`

Vấn đề chính: sitemap đang feed rất nhiều URL không phải đích cuối.

### Vì sao đây là lỗi cần sửa

Sitemap chỉ nên chứa:

- URL `200`
- indexable
- canonical/final URL

Không nên chứa:

- URL redirect `301`
- URL lỗi `404/403/500`
- attachment/preview URLs
- legacy subdomain URLs

Nếu để nguyên, Google sẽ:

- tốn crawl vào URL cũ
- đi qua redirect không cần thiết
- giảm trust vào sitemap
- làm yếu discovery của URL chuẩn

### Phát hiện chính từ file `301`

Từ `47,520` URL `301` trong sitemap:

#### 1. Legacy media từ `news.coincu.com/wp-content/...`

- `28,471` URL

File:

- `sitemaps_all_status_301_wp_content_legacy.csv`

Ví dụ:

- `https://news.coincu.com/wp-content/uploads/2023/01/image-506-1024x451.png`

#### 2. Toàn bộ legacy subdomain `news.coincu.com`

- `33,973` URL

File:

- `sitemaps_all_status_301_news_subdomain.csv`

Điều này cho thấy sitemap vẫn đang emit URL từ subdomain cũ.

#### 3. Sau khi loại toàn bộ `news.coincu.com`, vẫn còn `13,547` URL `301` trên domain chính

File:

- `sitemaps_all_status_301_remaining_excluding_all_news_subdomain.csv`

Các nhóm lớn nhất còn lại:

- `/news` -> `667`
- `/analysis` -> `586`
- `/markets` -> `314`
- `/bitcoin` -> `85`
- `/ethereum` -> `67`
- `/blockchain` -> `57`
- `/pr` -> `55`
- `attachment/preview query` -> `28`
- `/press-release` -> `24`
- `/author` -> `22`
- `/uncategorized` -> `21`
- `/scam-alert` -> `19`
- `/knowledge` -> `15`

### Diễn giải đúng

Hiện có `2` lớp lỗi sitemap:

#### Lớp 1: legacy subdomain/media

- `news.coincu.com/...`
- `news.coincu.com/wp-content/...`

#### Lớp 2: legacy content routes trên `coincu.com`

- `/news/{slug}/`
- `/analysis/{slug}/`
- `/markets/{slug}/`
- `/bitcoin/{slug}/`
- `/ethereum/{slug}/`
- `/blockchain/{slug}/`
- `/pr/{slug}/`

Ngoài ra còn có:

- `?attachment_id=...`
- `?preview=true`
- author/category/uncategorized/query rác

### Cách sửa đúng

Không sửa bằng cách thêm redirect mới.

Không sửa từng URL tay.

Phải sửa ở **nguồn sinh sitemap**.

### Việc dev cần làm

#### 1. Loại toàn bộ `news.coincu.com` khỏi sitemap

Sitemap không được emit bất kỳ URL nào thuộc:

- `https://news.coincu.com/...`

Đặc biệt:

- `https://news.coincu.com/wp-content/...`

Nếu đây là image/media legacy thì phải loại khỏi sitemap hoàn toàn.

#### 2. Loại attachment / preview URLs khỏi sitemap

Không được xuất các URL kiểu:

- `?attachment_id=...`
- `?preview=true`
- `?_thumbnail_id=...`

Attachment redirect có thể vẫn giữ để xử lý request ngoài đời, nhưng attachment URLs không được có mặt trong sitemap.

#### 3. Với content routes cũ, sitemap phải xuất final URL

Ví dụ:

- không xuất `/news/{slug}/`
- không xuất `/analysis/{slug}/`
- không xuất `/markets/{slug}/`

Mà phải xuất:

- `/{slug}/`

Tương tự với các nhóm:

- `/bitcoin/`
- `/ethereum/`
- `/blockchain/`
- `/pr/`
- `/press-release/`

Nếu route cũ vẫn cần redirect để đón traffic, vẫn giữ redirect.

Nhưng sitemap chỉ được chứa URL đích cuối.

#### 4. Rà bucket author/category/archive

Review lại các nhóm:

- `/author/`
- `/category/`
- `/uncategorized/`

Bucket nào không chủ đích index thì:

- noindex
- và loại khỏi sitemap

### Chỗ cần kiểm trong code / plugin

Dev cần kiểm:

- plugin sitemap đang dùng
- filters/hooks đang sinh sitemap URLs
- bất kỳ custom rewrite/permalink logic nào
- chỗ nào còn hardcode hoặc còn data từ `news.coincu.com`
- chỗ nào còn emit route cũ `/news/`, `/analysis/`, `/markets/`

### Kết quả mong muốn

Sau fix:

- sitemap chỉ còn URL `200`
- sitemap chỉ còn URL indexable
- sitemap chỉ còn canonical/final URLs
- không còn:
  - `news.coincu.com`
  - `wp-content` legacy
  - `attachment`
  - `preview`
  - route content cũ dạng prefix redirect

### File tham chiếu

- `/home/thana2/coincu-2nd/sitemaps_all_status_301.csv`
- `/home/thana2/coincu-2nd/sitemaps_all_status_301_wp_content_legacy.csv`
- `/home/thana2/coincu-2nd/sitemaps_all_status_301_news_subdomain.csv`
- `/home/thana2/coincu-2nd/sitemaps_all_status_301_attachment_like.csv`
- `/home/thana2/coincu-2nd/sitemaps_all_status_301_preview_like.csv`
- `/home/thana2/coincu-2nd/sitemaps_all_status_301_remaining_excluding_all_news_subdomain.csv`

### Kết luận ngắn

Coincu không chỉ có vài URL redirect trong sitemap.

Hiện sitemap đang phát ra một lượng lớn:

- legacy subdomain URLs
- legacy media URLs
- legacy content routes
- attachment/preview URLs

Đây là lỗi ở tầng nguồn sinh sitemap và cần sửa tại nguồn đó.
