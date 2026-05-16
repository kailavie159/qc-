## Coincu Phase 2: Non-menu Internal Link Sources

Ngày: `2026-05-16`

### Mục tiêu

Xác định các nguồn internal link `ngoài menu` vẫn đang làm bẩn discovery/indexing, đặc biệt là các link kiểu:

- `https://coincu.com/news/{slug}/`
- `https://coincu.com/analysis/{slug}/`
- `https://coincu.com/markets/{slug}/`
- `https://coincu.com/blockchain/{slug}/`
- `https://coincu.com/blockchain-event/{slug}/`

### Nguồn dữ liệu đã dùng

- Crawl inlinks: `/home/thana2/coincu/all_inlinks.csv`
- Public content export: `/home/thana2/coincu-export-2026-05-14/wp_posts_public.csv`

### Kết quả chính

#### 1. Footer block đang là nguồn sitewide lớn nhất còn bơm route bẩn

Từ `all_inlinks.csv`, destination `https://coincu.com/news/` xuất hiện:

- tổng `46,554` inlinks
- `46,538` từ `Footer`
- `9` từ `Content`
- `3` từ `Header`
- `1` từ `Navigation`
- `1` từ `Head`
- `2` dòng position trống

Điều này cho thấy sau khi đã dọn menu, `Footer` vẫn là nguồn internal discovery bẩn lớn nhất còn lại.

Ví dụ source pages có footer link sang `https://coincu.com/news/`:

- `https://coincu.com/`
- `https://coincu.com/about-us/`
- `https://coincu.com/crypto-millionaire/`
- `https://coincu.com/crypto-glossary/`
- `https://coincu.com/upcoming-event/`
- `https://coincu.com/top-best-litecoin-casinos/`

#### 2. Không chỉ footer, nội dung bài viết cũng đang chèn rất nhiều prefixed URLs cũ

Từ `wp_posts_public.csv`, số `source posts/pages` có chứa ít nhất một prefixed route cũ trong `post_content` là:

- `6,474` bài/trang

Số lượng theo từng loại prefix:

- `news_post`: `3,332`
- `markets_post`: `2,382`
- `analysis_post`: `2,175`
- `blockchain_post`: `249`
- `blockchain_event_post`: `22`

Ví dụ literal links cũ còn nằm ngay trong body:

- `tradegenius-review-2026-hands-on-test`
- `the-open-network-review`
- `skyai-skyai-review-mcp-data-rail-thesis`
- `why-is-skyai-skyai-pumping-today`
- `bitcoin-steadies-as-boyaa-clears-100m-crypto-mandate`
- `the-ravedao-rave-case-file-will-another-hard-pump-happen`

Ví dụ URL cũ cụ thể còn được nhúng trong nội dung:

- `https://coincu.com/news/toncoin-lands-on-robinhood-as-users-tvl/`
- `https://coincu.com/news/bnb-chain-daily-transactions-record/`
- `https://coincu.com/analysis/10b-eth-shorts-at-risk-if-price-pumps-10/`
- `https://coincu.com/markets/fed-signals-two-rate-cuts-for-2025/`
- `https://coincu.com/blockchain/blackrock-leaders-tokenization-expansion/`
- `https://coincu.com/blockchain-event/ethdenver-2026/`

### Diễn giải đúng cho dev

`All Inlinks` không đủ để thấy toàn bộ literal href cũ trong nội dung, vì crawl có thể ghi nhận destination sau redirect/canonical processing.

Vì vậy:

- `all_inlinks.csv` rất tốt để thấy `sitewide sources` như footer/header/widget
- `wp_posts_public.csv` tốt hơn để thấy `literal old hrefs` đang nằm trong body content

Nói ngắn gọn: nếu chỉ nhìn crawl thì sẽ `under-count` nhiều link cũ trong bài viết.

### Những nguồn ngoài menu cần xử lý tiếp

#### Ưu tiên 1: Global footer block / footer template

Cần tìm và bỏ link `https://coincu.com/news/` khỏi footer sitewide.

Đây nhiều khả năng là:

- footer block
- footer widget
- footer template trong theme/builder
- reusable block hoặc UX block gắn toàn site

#### Ưu tiên 2: Content-level internal links trong bài viết

Đây là batch lớn nhất sau footer.

Cần xử lý các href cũ trong body:

- `/news/{slug}/` -> `/{slug}/`
- `/analysis/{slug}/` -> `/{slug}/`
- `/markets/{slug}/` -> `/{slug}/`
- `/blockchain/{slug}/` -> `/{slug}/`
- `/blockchain-event/{slug}/` -> `/{slug}/`

Khả năng cao cần:

- search/replace có kiểm soát trong DB
- hoặc export/import cleanup script
- hoặc batch editor theo prefix

#### Ưu tiên 3: Các content/page sources lẻ cần mở kiểm tay

Từ crawl non-footer sample, nên mở kiểm:

- `https://coincu.com/about-us/`
- `https://coincu.com/top-5-best-crypto-browsers/`
- `https://coincu.com/free-bitcoin-code/`
- `https://coincu.com/news/`
- `https://coincu.com/c/news/`
- `https://coincu.com/c/news`

Các page này có dấu hiệu còn block/content/link tự đẩy sang `/news/`.

### Những gì chưa thấy là nguồn lớn ở bước này

Trong pass hiện tại:

- chưa thấy `news.coincu.com` nổi lên như destination lớn trong `all_inlinks`
- chưa thấy `?noamp=mobile` nổi lên như destination lớn trong `all_inlinks`

Điều này phù hợp với việc `noamp` đã được fix redirect trước đó.

### Kết luận ngắn

Sau khi dọn menu, `Phase 2` ngoài menu đang còn 2 nguồn bẩn lớn:

1. `Footer sitewide` đang bơm `https://coincu.com/news/` trên diện rộng
2. `Post content` đang chứa hàng nghìn prefixed URLs cũ, tổng cộng ảnh hưởng ít nhất `6,474` source posts/pages

Muốn cleanup discovery tốt hơn thì không thể dừng ở menu và sitemap. Bắt buộc phải xử lý tiếp:

- footer/template blocks
- body content internal links theo prefix cũ
