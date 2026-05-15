## Coincu Handoff Tổng: Duplicate Route Discovery

Ngày: 2026-05-15

### Vấn đề chính

Coincu đang có hiện tượng Google phát hiện nhiều URL khác nhau cho cùng một bài viết, dù route chuẩn hiện tại nên là:

- `https://coincu.com/{post-name}/`

Các route phụ đang gây nhiễu gồm:

- `/news/{slug}/`
- `/analysis/{slug}/`
- `/blockchain/{slug}/`
- `/markets/{slug}/`
- `/blockchain-event/{slug}/`

Ngoài ra còn có query variants như:

- `?noamp=mobile`

Hệ quả:

- phình bucket `Crawled - currently not indexed`
- tăng crawl waste
- làm Google phải xử lý nhiều biến thể URL cho cùng một content

### Kết luận kỹ thuật đã chốt

#### 1. Canonical route của bài viết nên giữ nguyên là `/{post-name}/`

Cơ sở:

- WordPress permalink hiện tại đang là `/%postname%/`
- nhiều route phụ trên live đã `301` về root slug
- đổi sang `/{category}/{post-name}/` lúc này sẽ tạo thêm một migration URL rất lớn, không phù hợp trong bối cảnh site đang lỗi index/media

#### 2. Route phụ không nên là route chuẩn

Các route có prefix chỉ nên là route phụ, nếu còn tồn tại thì phải:

- `301` về `/{slug}/`

#### 3. Lỗi cốt lõi hiện tại không còn nằm ở permalink setting

Permalink setting đã đúng.

Phần cần fix là:

- nơi nào trong site vẫn tiếp tục render hoặc expose route phụ
- nơi nào vẫn sinh query variant `?noamp=mobile`

### Việc dev cần làm

#### Phase 1. Giữ nguyên route chuẩn

- Không đổi permalink post sang `/{category}/{post-name}/`
- Giữ canonical article URL là `/{post-name}/`

#### Phase 2. Đảm bảo route phụ luôn `301` về route chuẩn

Áp dụng cho:

- `/news/{slug}/`
- `/analysis/{slug}/`
- `/blockchain/{slug}/`
- `/markets/{slug}/`
- `/blockchain-event/{slug}/`

Ví dụ đã verify trên live:

- `/news/doj-epstein-documents-release/` -> `/doj-epstein-documents-release/`
- `/analysis/ada-breakdown-looms/` -> `/ada-breakdown-looms/`
- `/blockchain/agentlisa-funding-ai-security/` -> `/agentlisa-funding-ai-security/`
- `/markets/ethereum-treasury-plan-shelved/` -> `/ethereum-treasury-plan-shelved/`
- `/blockchain-event/digital-assets-forum/` -> `/digital-assets-forum/`

#### Phase 3. Cắt các internal source vẫn đang nhả route phụ

Đây là phần quan trọng nhất.

Cần kiểm tra và sửa:

- header/top-bar
- main menu/mobile menu
- sidebar nav/widget
- section templates: `news`, `analysis`, `blockchain`, `markets`, `blockchain-event`
- related posts
- home/category blocks
- old feeds
- sitemap output
- custom permalink/rewrite/plugin logic nếu có

Mục tiêu:

- internal links chỉ còn trỏ tới `/{slug}/`
- không còn render link bài kiểu `/news/{slug}/`, `/analysis/{slug}/`...

#### Phase 4. Cleanup `?noamp=mobile`

Đã verify live:

- batch cleanup hiện đã redirect đúng về clean URL không còn query

Nhóm URL mẫu:

- `https://coincu.com/analysis/bnb-smashes-905-ath/?noamp=mobile`
- `https://coincu.com/ethereum/ethereum-pectra-upgrade-eip-7702-live/?noamp=mobile`
- `https://coincu.com/news/circle-and-maple-partnership-expand-usdc/?noamp=mobile`
- `https://coincu.com/news/sec-delays-solana-etf-decision/?noamp=mobile`
- `https://coincu.com/sec-delays-solana-etf-decision/?noamp=mobile`

Việc dev vẫn cần đảm bảo:

- không còn source nội bộ nào sinh `?noamp=mobile`
- không còn module/feed nào append query này

### Checklist ngắn cho dev/WP

- Canonical article URL: chỉ `/{post-name}/`
- Route phụ có prefix: luôn `301` về `/{slug}/`
- Không đưa route phụ vào sitemap
- Không render route phụ trong menu, widget, blocks, related posts
- Không để query variants như `?noamp=mobile` tiếp tục bị discover

### Evidence / file tham chiếu

#### Tài liệu handoff

- `coincu-duplicate-route-discovery-handoff-2026-05-15.vi.md`
- `coincu-phase2-internal-link-sources-handoff-2026-05-15.vi.md`
- `coincu-noamp-mobile-cleanup-handoff-2026-05-15.vi.md`
- `coincu-crawled-not-indexed-action-plan-2026-05-15.md`

Link GitHub:

- https://github.com/kailavie159/qc-/blob/main/Coincu/coincu-duplicate-route-discovery-handoff-2026-05-15.vi.md
- https://github.com/kailavie159/qc-/blob/main/Coincu/coincu-phase2-internal-link-sources-handoff-2026-05-15.vi.md
- https://github.com/kailavie159/qc-/blob/main/Coincu/coincu-noamp-mobile-cleanup-handoff-2026-05-15.vi.md
- https://github.com/kailavie159/qc-/blob/main/Coincu/coincu-crawled-not-indexed-action-plan-2026-05-15.md

#### File dữ liệu local

- `/home/thana2/coincu/batch2_gsc_crawled_not_indexed_sample.csv`
- `/home/thana2/coincu/all_inlinks.csv`
- `/home/thana2/coincu/sitemaps_all.csv`
- `/home/thana2/coincu/batch3_gsc_redirect_sample.csv`
- `/home/thana2/coincu/batch3_gsc_5xx_sample.csv`

### Kết quả mong muốn sau khi fix

- Google chỉ còn discover một route bài viết chuẩn là `/{slug}/`
- route phụ không còn được feed từ nội bộ site
- query variants như `?noamp=mobile` không còn xuất hiện
- giảm dần bucket `Crawled - currently not indexed`
