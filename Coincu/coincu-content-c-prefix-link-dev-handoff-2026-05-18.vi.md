**Dev handoff: fix internal links `/c/...` trong post content**

File nguồn:
- [coincu-content-c-prefix-link-fix-candidates-2026-05-16.csv](/home/thana2/qc-coincu-only/Coincu/coincu-content-c-prefix-link-fix-candidates-2026-05-16.csv)

Mục tiêu:
- dọn các internal link đang trỏ vào URL redirect dạng `/c/...`
- thay bằng URL canonical sạch để giảm redirect hop trong internal linking

Phạm vi:
- chỉ sửa trong `post_content`
- chỉ áp dụng cho các `post_id` có trong CSV
- không replace mù toàn site

Rule replace:
- `https://coincu.com/c/news/` -> `https://coincu.com/news/`
- `https://coincu.com/c/knowledge/` -> `https://coincu.com/knowledge/`

Cách dùng CSV:
- `post_id`: ID bài cần sửa
- `find_url`: URL cũ
- `replace_url`: URL mới
- `match_count`: số lần xuất hiện dự kiến trong bài

Lưu ý:
- chỉ replace đúng full URL ở cột `find_url`
- không thay hàng loạt theo pattern `/c/` vì dễ đụng nhầm URL khác
- sau khi chạy xong, recrawl/check HTML sample để xác nhận không còn link `/c/news/` và `/c/knowledge/` trong body bài viết

Kỳ vọng:
- giảm internal links đang đi qua `301`
- làm sạch nguồn bơm link bẩn từ content, không chỉ từ menu/homepage blocks
