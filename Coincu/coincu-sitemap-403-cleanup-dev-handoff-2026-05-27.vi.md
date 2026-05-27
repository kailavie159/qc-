## Coincu Dev Handoff: Dọn Sitemap Đang Chứa URL 403

Ngày: `2026-05-27`

### Kết luận ngắn

Recrawl mới cho thấy sitemap của Coincu hiện có:

- `3,585` URL `403`

Khác với cụm `301` và `404`, cụm `403` này gần như không phân tán.

Nó tập trung gần như hoàn toàn vào:

- `wp-content/uploads/...`

### Phát hiện chính

File tham chiếu:

- `sitemaps_all_status_403.csv`

Tổng:

- `3,585` URL `403`

Phân cụm:

- `/wp-content` -> `3,584`
- preview URL lẻ -> `1`

Ví dụ:

- `https://coincu.com/wp-content/uploads/2022/12/Ban-sao-cua-BB-2022-12-26T054833.306.png`
- `https://coincu.com/wp-content/uploads/2022/12/image-1625.png`

Ví dụ preview URL:

- `https://coincu.com/206847-sam-bankman-fried-seeks-seal-caroline-ellisons/?preview_id=206847&preview_nonce=...&preview=true&_thumbnail_id=206853`

### Diễn giải đúng

Điều này cho thấy:

- sitemap đang emit rất nhiều media/uploads URLs
- nhưng server hiện đang trả `403` cho các URL đó

Nói ngắn:

`403 sitemap` hiện tại gần như là lỗi **media/uploads + preview URLs đang bị đưa nhầm vào sitemap**

Đây không phải vấn đề content/article riêng lẻ.

### Vì sao đây là lỗi cần sửa

Sitemap không được chứa URL `403`.

Nếu để nguyên:

- Google crawl vào các file bị deny
- tốn crawl budget
- giảm trust vào sitemap

### Cách sửa đúng

Không sửa bằng cách mở quyền truy cập hàng loạt cho toàn bộ các URL này.

Việc đúng cần làm là:

#### 1. Loại toàn bộ `wp-content/uploads/...` khỏi sitemap

Nếu đây là media/file URLs không chủ đích index:

- không emit vào sitemap

Nếu site có image sitemap riêng:

- chỉ emit các image URLs thực sự hợp lệ và public
- không emit các file đang trả `403`

#### 2. Loại preview URLs khỏi sitemap

Không được emit các URL kiểu:

- `?preview_id=...`
- `?preview=true`
- `?_thumbnail_id=...`

### Chỗ dev cần kiểm

- plugin sitemap đang dùng
- image/media sitemap configuration
- custom code/hooks có đang đưa `wp-content/uploads/...` vào sitemap không
- source nào đang emit preview URLs

### Kết quả mong muốn

Sau fix:

- sitemap không còn URL `403`
- không còn `wp-content/uploads/...` bị deny trong sitemap
- không còn preview URLs trong sitemap

### File tham chiếu

- `/home/thana2/coincu-2nd/sitemaps_all_status_403.csv`

### Kết luận ngắn

`403 sitemap` của Coincu là một case rất rõ:

- gần như toàn bộ đến từ `wp-content/uploads/...`
- cộng thêm `1` preview URL

Nên hướng xử đúng là:

- stop emitting media/uploads URLs bị deny
- stop emitting preview URLs

chứ không phải xử từng URL lẻ.
