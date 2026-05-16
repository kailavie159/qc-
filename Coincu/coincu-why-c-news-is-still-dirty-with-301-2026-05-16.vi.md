## Vì sao `/c/news/` vẫn là vấn đề dù đã có `301`

Ngày: `2026-05-16`

### Kết luận ngắn

`https://coincu.com/c/news/` không lỗi theo nghĩa `dead URL`.

Nhưng nó vẫn là `URL bẩn` theo nghĩa:

- không phải canonical URL cuối
- vẫn đang được internal-link rất nhiều
- vẫn làm bot phải crawl qua một bước redirect không cần thiết

### URL đúng hiện tại là gì

Check live:

- `https://coincu.com/c/news/` -> `301`
- đích: `https://coincu.com/news/`
- `https://coincu.com/news/` -> `200`
- canonical HTML final của trang là `https://coincu.com/news/`

Vì vậy:

- `/c/news/` = redirect URL
- `/news/` = canonical URL

### Vì sao có `301` rồi mà vẫn chưa ổn

`301` chỉ là lớp `backward compatibility`.

Nó có tác dụng:

- cứu link cũ
- tránh 404
- chuyển user/bot sang URL mới

Nhưng `301` không có nghĩa là site nên tiếp tục internal-link đến URL đó.

Nếu chính website vẫn link tới `/c/news/`, bot sẽ phải:

1. crawl `/c/news/`
2. nhận `301`
3. rồi mới tới `/news/`

Đó là một bước crawl dư thừa.

### Bằng chứng local

Trong `internal_all.csv`, URL `https://coincu.com/c/news/` được ghi nhận là:

- `301`
- `Non-Indexable`
- `Redirected`
- `Redirect URL = https://coincu.com/news/`
- `Inlinks = 188863`
- `Unique Inlinks = 47948`

Điều này cho thấy đây không phải một redirect hiếm gặp.

Đây là redirect URL đang được internal-link trên diện rất rộng.

### Bằng chứng live HTML

Trên homepage live vẫn thấy nhiều chỗ đang render `/c/news/`, ví dụ:

- top menu `News`
- block `LIVE UPDATES`
- widget/menu phụ `nav_menu-3`
- mobile/off-canvas menu `News`

Trong khi footer `Product > News` lại đang dùng:

- `https://coincu.com/news/`

Nghĩa là site đang tồn tại song song:

- một số chỗ link đúng tới `/news/`
- một số chỗ vẫn link sai tới `/c/news/`

### Kết luận kỹ thuật đúng

`/c/news/` không phải lỗi do redirect hỏng.

Nó là lỗi kiểu:

- `redirecting internal URL`
- `internal-link inconsistency`
- `discovery/crawl inefficiency`

### Cách xử lý đúng

1. Giữ `301 /c/news/ -> /news/`
2. Đổi mọi internal links `/c/news/` thành `/news/`
3. Loại `/c/news/` khỏi nguồn sinh sitemap nếu còn
4. Recheck crawl để đảm bảo `/c/news/` không còn là URL được site nội bộ link tới

### Một câu ngắn để gửi dev

`301 chỉ để giữ backward compatibility; internal links phải trỏ thẳng tới /news/, không trỏ vào /c/news/.`
