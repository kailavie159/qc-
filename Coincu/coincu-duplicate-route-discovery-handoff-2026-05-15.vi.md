## Coincu Handoff: Duplicate Route Discovery

Ngày: 2026-05-15

Vấn đề:
- Coincu hiện vẫn đang tạo hoặc làm lộ nhiều route URL khác nhau cho cùng một bài viết
- Đây là một trong các nguyên nhân góp phần làm phình nhóm `Crawled - currently not indexed`
- Kiểm tra live cho thấy một phần route phụ đã `301`, nhưng Google vẫn đang phát hiện quá nhiều URL thay thế

### Cách xử lý Duplicate Route Discovery

Duplicate Route Discovery nên được xử lý theo 4 lớp, theo đúng thứ tự sau:

#### 1. Chốt 1 route chuẩn duy nhất

Nên giữ:

- `https://coincu.com/{slug}/`

Không giữ song song các route bài viết như:

- `/news/{slug}/`
- `/analysis/{slug}/`
- `/blockchain/{slug}/`
- `/markets/{slug}/`
- `/blockchain-event/{slug}/`

#### 2. 301 toàn bộ route phụ về route chuẩn

Ví dụ:

- `/news/doj-epstein-documents-release/` -> `/doj-epstein-documents-release/`
- `/analysis/ada-breakdown-looms/` -> `/ada-breakdown-looms/`
- `/blockchain/agentlisa-funding-ai-security/` -> `/agentlisa-funding-ai-security/`

Việc này trên live đã có một phần. Bước tiếp theo không chỉ là thêm redirect, mà là dọn toàn bộ nguồn đang tiếp tục sinh ra các route phụ đó.

#### 3. Cắt mọi nguồn đang tiếp tục “nhả” route phụ

Đây là lớp quan trọng nhất.

Cần kiểm tra và sửa:

- sitemap
- breadcrumbs
- category modules
- related posts
- home/category blocks
- old feeds
- internal links trong bài
- mọi custom permalink/plugin logic vẫn đang in ra `/news/{slug}/`, `/analysis/{slug}/` hoặc các route có prefix tương tự

Nếu không cắt các nguồn này, Google vẫn sẽ tiếp tục crawl route phụ dù chúng đã `301`.

#### 4. Recheck bằng mẫu thật

Sau khi dọn xong:

- crawl lại site
- xác nhận internal link chỉ còn trỏ tới `/{slug}/`
- xác nhận route phụ khi gọi trực tiếp vẫn `301`
- xác nhận sitemap chỉ chứa `/{slug}/`

### Checklist ngắn cho dev/WP

- Canonical article URL: chỉ dùng `/{slug}/`
- Route phụ của bài viết: luôn `301` về `/{slug}/`
- Không đưa route phụ vào sitemap
- Không render route phụ trong internal links, modules hoặc widgets
- Không để query variants như `?noamp=mobile` tiếp tục bị discover

### Các ví dụ đã verify trên live

- `/news/doj-epstein-documents-release/` -> `/doj-epstein-documents-release/`
- `/analysis/ada-breakdown-looms/` -> `/ada-breakdown-looms/`
- `/blockchain/agentlisa-funding-ai-security/` -> `/agentlisa-funding-ai-security/`
- `/markets/ethereum-treasury-plan-shelved/` -> `/ethereum-treasury-plan-shelved/`
- `/blockchain-event/digital-assets-forum/` -> `/digital-assets-forum/`
- `/news/sec-delays-solana-etf-decision/?noamp=mobile` -> `/sec-delays-solana-etf-decision/?noamp=mobile`

### Kết quả kỳ vọng

- giảm số lượng URL bài viết thay thế mà Google phát hiện
- giảm crawl waste do route trùng
- làm sạch sitemap và internal link graph
- tăng khả năng các canonical article URLs thật sự được index
