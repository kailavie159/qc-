## Coincu Handoff: Tách Internal `3xx/4xx` Thành `Editor Fix` Và `Dev Fix`

Ngày: `2026-05-28`

### Kết luận ngắn

Sau recrawl mới, lớp `internal 3xx/4xx` của Coincu là một lớp `mixed`.

Không phải toàn bộ đều cần dev, nhưng cũng không thể coi toàn bộ là lỗi editor/content.

Nên tách thành `2` nhóm:

- `Dev Fix`
- `Editor Fix`

### Bối cảnh từ recrawl mới

`response_codes.csv` summary cho thấy:

- `47,707` internal `3xx`
- `9,037` internal `4xx`

Trong `response_codes_all.csv`, các nhóm lớn nhất trong tập internal `3xx/4xx` là:

- `/wp-content` -> `32,055`
- `/convert-crypto-to-fiat` -> `1,649`
- `/news` -> `767`
- `/analysis` -> `637`
- `/markets` -> `369`
- `/currencies` -> `129`
- `/assets` -> `109`

### Nhóm chắc chắn là `Dev Fix`

#### 1. Toàn bộ `/c/...`

Đây là nhóm rõ nhất.

Các URL có inlinks rất cao:

- `https://coincu.com/c/casino-reviews/` -> `301`, `20,555` inlinks
- `https://coincu.com/c/pr/press-release/` -> `301`, `20,553` inlinks
- `https://coincu.com/c/news` -> `301`, `11,506` inlinks
- `https://coincu.com/c/analysis` -> `301`, `1,215` inlinks
- `https://coincu.com/c/uncategorized` -> `301`, `780` inlinks
- `https://coincu.com/c/bitcoin` -> `301`, `746` inlinks
- `https://coincu.com/c/markets` -> `301`, `735` inlinks
- `https://coincu.com/c/knowledge` -> `301`, `687` inlinks

Diễn giải:

Đây gần như chắc chắn là:

- source sitewide
- taxonomy/module/template cũ
- route generation cũ
- hoặc internal links được sinh tự động bởi code

Không hợp lý để sửa tay từng link.

#### 2. Bucket tools/data/modules

Các nhóm này cũng nghiêng mạnh về dev:

- `/wp-content`
- `/convert-crypto-to-fiat`
- `/currencies`
- `/assets`
- `/top-crypto-coins`

Đây không phải lỗi content editor thông thường.

Nhiều khả năng là:

- module
- generator
- bucket data/programmatic
- output của code/theme/plugin

### Nhóm `mixed`, có phần `Editor Fix`

Breakdown old-route URLs trong `response_codes_all.csv`:

- `/news 301` -> `667`
- `/analysis 301` -> `586`
- `/markets 301` -> `314`
- `/news 404` -> `100`
- `/markets 404` -> `55`
- `/analysis 404` -> `51`

Khi xem top URL theo số `inlinks`, phần lớn old-route article URLs chỉ có khoảng `8-16` inlinks mỗi URL, ví dụ:

- `https://coincu.com/analysis/ethereum-showing-strength-new-ath-run/` -> `301`, `16` inlinks
- `https://coincu.com/news/solana-dapp-revenue-exceeds-187m/` -> `301`, `11` inlinks
- `https://coincu.com/markets/bitwise-solana-etf-update/` -> `301`, `10` inlinks

Diễn giải:

Nhóm này có thể đến từ:

- body content cũ
- article blocks
- related content
- page builder sections
- đôi khi cũng có source template

Nên đây là nhóm `mixed`.

### Cách tách việc

#### `Dev Fix`

Dev nên xử các nhóm sau:

- toàn bộ `/c/...`
- `/wp-content`
- `/convert-crypto-to-fiat`
- `/currencies`
- `/assets`
- `/top-crypto-coins`
- bất kỳ internal links nào được sinh tự động bởi template/module/theme/plugin

#### `Editor Fix`

Editor hoặc content team có thể xử:

- old-route article links trong body:
  - `/news/{slug}`
  - `/analysis/{slug}`
  - `/markets/{slug}`
- article links đã `404`
- manual blocks / shortcode blocks / page builder content nếu sửa được trong WP

### Cách quyết định nhanh

Nếu một pattern có:

- hàng trăm hoặc hàng nghìn inlinks trên cùng một route pattern
- xuất hiện đồng loạt ở nhiều section

=> ưu tiên xếp vào `Dev Fix`

Nếu một URL chỉ có:

- vài inlinks
- xuất hiện trong bài viết, bài liên quan, block nội dung

=> có thể xếp vào `Editor Fix`

### Kết luận ngắn

Lớp internal `3xx/4xx` của Coincu nên tách như sau:

#### `Dev Fix`

- `/c/...`
- tools/data/programmatic buckets
- generated/template/module links

#### `Editor Fix`

- article old-route links trong content
- article links `404` rải rác
- manual blocks nếu sửa được trong WP

Đây là cách xử thực tế nhất để tránh:

- bắt editor sửa thứ mang tính sitewide
- hoặc bắt dev xử tay các link nội dung lẻ
