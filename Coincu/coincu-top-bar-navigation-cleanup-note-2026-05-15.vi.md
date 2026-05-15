## Coincu Note: Top Bar Navigation Cleanup

Ngày: 2026-05-15

### Kết luận

Menu `Top Bar Navigation` hiện không ổn và nên được rebuild hoặc bỏ hẳn.

### Những vấn đề thấy trực tiếp

- `About` đang trỏ tới `#`
- item `Coincu` bị lặp rất nhiều lần
- menu có dấu hiệu duplicated block, không phải menu được maintain sạch

### Đánh giá

Đây không phải nguồn chính của duplicate route article kiểu:

- `/news/{slug}/`
- `/analysis/{slug}/`

Nhưng đây vẫn là `sitewide internal-link noise` vì top bar xuất hiện lặp trên rất nhiều trang.

### Khuyến nghị

1. Xóa toàn bộ item `About -> #`

2. Xóa các item `Coincu` lặp

3. Rebuild top bar thật gọn, chỉ giữ nếu thật sự cần

### Chỉ nên giữ nếu còn dùng

- About Us
- Contact Us
- Coincu Partners
- Verified Team
- Terms / Policy

### Nếu top bar không thực sự cần

- bỏ hẳn sẽ tốt hơn giữ một menu rác

### Kết luận ngắn

`Top Bar Navigation` hiện fail về menu hygiene.

Nên rebuild hoặc remove, không nên sửa lẻ từng item.
