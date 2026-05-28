## Coincu Dev Handoff: Dọn Sitemap Đang Chứa URL 500

Ngày: `2026-05-28`

### Kết luận ngắn

Recrawl mới cho thấy sitemap của Coincu hiện có:

- `139` URL `500`

Khác với các cụm `301`, `404`, `403`, cụm `500` này rất tập trung.

### Phát hiện chính

File tham chiếu:

- `sitemaps_all_status_500.csv`

Tổng:

- `139` URL `500`

Phân cụm:

- `/top-crypto-coins` -> `137`
- `/top-blockchain-ecosystems-tvl-defi` -> `1`
- `/top-cryptocurrencies-market-cap-ranking` -> `1`

Ví dụ:

- `https://coincu.com/top-crypto-coins/bnb-price-update`
- `https://coincu.com/top-crypto-coins/eth-price-update`
- `https://coincu.com/top-crypto-coins/arrr-price-update`
- `https://coincu.com/top-blockchain-ecosystems-tvl-defi`
- `https://coincu.com/top-cryptocurrencies-market-cap-ranking`

### Diễn giải đúng

Điều này cho thấy:

- sitemap đang emit một bucket programmatic/tool/content nào đó
- nhưng server hiện trả `500`

Nói ngắn:

`500 sitemap` hiện tại gần như là lỗi riêng của bucket:

- `/top-crypto-coins/...`

và thêm `2` URL đơn lẻ liên quan tới ranking/TVL pages.

### Vì sao đây là lỗi cần sửa

Sitemap không được chứa URL `500`.

Nếu để nguyên:

- Google crawl vào URL lỗi server
- tốn crawl budget
- giảm trust vào sitemap
- có thể làm Google chậm hơn trong việc xử lý sitemap sạch

### Cách sửa đúng

Có `2` hướng hợp lệ, dev cần chọn `1` hướng rõ ràng:

#### Hướng A: bucket này không còn dùng

Nếu `/top-crypto-coins/...` và các page liên quan không còn là phần public/site strategy:

- loại toàn bộ bucket này khỏi sitemap

#### Hướng B: bucket này vẫn cần tồn tại

Nếu bucket này vẫn là module/section cần giữ:

- sửa lỗi server để các URL trả `200`
- chỉ emit lại vào sitemap sau khi URL sống ổn định

### Việc dev cần làm

1. Kiểm bucket:

- `/top-crypto-coins/...`

2. Xác định:

- đây là module còn active
- hay là bucket cũ cần retire

3. Nếu retire:

- stop emitting URLs này vào sitemap

4. Nếu giữ:

- sửa lỗi `500`
- chỉ để lại các URL final `200` trong sitemap

5. Review thêm 2 URL lẻ:

- `/top-blockchain-ecosystems-tvl-defi`
- `/top-cryptocurrencies-market-cap-ranking`

### Chỗ dev cần kiểm

- code/module sinh bucket `top-crypto-coins`
- logic generating per-coin price update pages
- source data dependency hoặc template causing `500`
- sitemap source đang emit nhóm này

### Kết quả mong muốn

Sau fix:

- sitemap không còn URL `500`
- bucket `top-crypto-coins` hoặc được khôi phục `200`, hoặc bị loại khỏi sitemap hoàn toàn

### File tham chiếu

- `/home/thana2/coincu-2nd/sitemaps_all_status_500.csv`

### Kết luận ngắn

`500 sitemap` của Coincu là một case rất gọn:

- gần như toàn bộ nằm ở `/top-crypto-coins/...`

Nên đây nhiều khả năng là:

- một bucket/module lỗi server
- hoặc một bucket cũ chưa bị loại khỏi sitemap
