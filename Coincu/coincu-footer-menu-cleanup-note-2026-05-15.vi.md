## Coincu Note: Footer Menu Cleanup

Ngày: 2026-05-15

### Kết luận

Footer menu hiện đang bẩn và nên dọn.

Các dấu hiệu thấy trực tiếp trong WP menu:

- nhiều item demo/theme thừa:
  - `Purchase JNews`
  - `Intro Page`
  - `JNews Demos`
- nhiều item lặp lại rất nhiều lần
- có item `Contact Us` đang trỏ tới `#`

### Đánh giá

Đây không phải là bằng chứng chính của duplicate route article kiểu:

- `/news/{slug}/`
- `/analysis/{slug}/`

Nhưng đây là một vấn đề `site hygiene` rõ ràng vì:

- footer xuất hiện trên toàn site
- link rác bị lặp sitewide
- tạo internal link noise
- cho thấy theme/template cleanup chưa hoàn tất

### Việc nên làm

1. Xóa toàn bộ item demo/theme thừa:

- `Purchase JNews`
- `Intro Page`
- `JNews Demos`

2. Xóa các item `Contact Us` trỏ `#`

3. Dựng lại footer links tối thiểu, chỉ giữ các trang thật sự cần:

- About Us
- Contact Us
- Terms and Conditions
- Policy / Privacy
- Coincu Partners
- Verified Team
- Editorial standards / Disclosure pages nếu cần

### Kết luận ngắn

Footer menu này nên được dọn sạch.

Không phải vì nó là nguồn duplicate route lớn nhất, mà vì nó là:

- rác internal links lặp trên toàn site
- dấu hiệu leftover từ theme/demo
- một lớp technical hygiene nên sửa sớm
