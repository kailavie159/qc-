## Coincu Note: Mobile Navigation Cleanup

Ngày: 2026-05-15

### Kết luận

Menu `Mobile Navigation` hiện fail nặng và không nên sửa thủ công từng item.

Nên xem đây là một menu bị duplicate cấu trúc và nên rebuild từ đầu.

### Những vấn đề thấy trực tiếp

- menu có số lượng item rất lớn: `154`
- item `Coincu` bị lặp hàng loạt
- `News` bị lặp rất nhiều lần
- `Markets`, `Knowledge`, `Reviews`, `Recommended`, `PR` cũng bị lặp theo cụm
- submenu như:
  - `Bitcoin`
  - `Blockchain`
  - `Metaverse News`
  - `NFTs News`
  bị lặp lặp lại rất nhiều lần

Ngoài ra:

- `Recommended` vẫn chứa link `news.coincu.com/...`
- nhiều item cũ/rác đang bị nhân lên trên toàn menu

### Đánh giá

Đây không còn là lỗi item lẻ.

Đây là dấu hiệu của:

- duplicated menu structure
- menu corruption / copied blocks
- internal-link noise sitewide nếu menu này đang active

### Tác động SEO

Nếu menu mobile này đang được render trên live site, nó có thể:

- feed thêm rất nhiều internal links lặp
- feed thêm legacy URLs
- làm bẩn internal link graph
- làm nặng thêm vấn đề discovery/crawl noise

### Khuyến nghị

1. Không cleanup thủ công từng item

2. Bỏ dùng menu `Mobile Navigation` hiện tại

3. Dựng lại menu mobile mới từ đầu, thật gọn

### Cấu trúc menu mobile mới nên giữ

- Coincu / Home
- News
- Markets
- Knowledge
- Reviews
- Recommended (chỉ nếu đã dọn sạch link)
- PR

### Tuyệt đối không đưa sang menu mới

- link `news.coincu.com/...`
- item bị duplicate
- cụm link review/gambling cũ nếu chưa được review
- URL đang redirect nhiều tầng

### Khuyến nghị kỹ thuật thêm

Nếu theme hỗ trợ, nên:

- sync mobile menu từ phiên bản `Main Navigation` đã cleanup

để tránh maintain hai menu tách rời và tránh duplicate lỗi lần nữa.

### Kết luận ngắn

`Mobile Navigation` hiện tại nên được rebuild từ đầu.

Không nên cố sửa tay từng item.
