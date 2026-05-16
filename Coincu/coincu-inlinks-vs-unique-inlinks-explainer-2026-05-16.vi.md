## Giải thích `Inlinks` và `Unique Inlinks` cho case `/c/news/`

Ngày: `2026-05-16`

### Số liệu đang thấy

Trong `internal_all.csv`, URL:

- `https://coincu.com/c/news/`

được ghi nhận:

- `Inlinks = 188863`
- `Unique Inlinks = 47948`

### `Inlinks` là gì

`Inlinks` là tổng số internal links trỏ vào một URL trong crawl.

Nó cộng tất cả các link nhìn thấy, kể cả:

- cùng một link lặp lại trên nhiều trang
- cùng một link lặp lại ở nhiều vị trí khác nhau
- các block/sitewide elements render lặp lại toàn site

Nói ngắn:

- `Inlinks` = tổng lượng link đổ vào URL đó

### `Unique Inlinks` là gì

`Unique Inlinks` là số internal link source duy nhất trỏ vào URL đó.

Nó loại bớt phần lặp thô hơn so với `Inlinks`, nên thường dùng để hiểu:

- URL này đang được bao nhiêu source instances khác nhau link tới

Nói ngắn:

- `Unique Inlinks` = số nguồn link duy nhất đang trỏ vào URL đó

### Hiểu hai số này trong case `/c/news/`

Với `/c/news/`:

- `188863` cho thấy đây không phải vài link lẻ
- `47948` cho thấy số nguồn link duy nhất cũng cực lớn

Điều đó nghĩa là:

- `/c/news/` đang được internal-link trên diện rất rộng
- đây là một pattern lặp đi lặp lại toàn site
- nhiều khả năng đến từ menu, widget, homepage blocks, reusable elements hoặc template outputs

### Vì sao đây là vấn đề

`/c/news/` không phải canonical URL cuối.

Live check cho thấy:

- `/c/news/` -> `301`
- đích là `/news/`

Tức là website đang làm bot đi theo đường:

1. vào `/c/news/`
2. nhận `301`
3. mới tới `/news/`

Nếu chỉ có vài link như vậy thì không đáng kể.

Nhưng khi:

- `Inlinks = 188863`
- `Unique Inlinks = 47948`

thì đây là lỗi ở quy mô lớn.

### Ý nghĩa SEO kỹ thuật

Con số này cho thấy `/c/news/` không phải:

- redirect cũ ít người dùng
- URL phụ vô hại

Mà là:

- `redirecting internal URL` đang được site bơm link rất mạnh

Hệ quả:

- crawl path không sạch
- discovery không nhất quán
- bot phải qua bước redirect không cần thiết
- dữ liệu crawl/internal linking bị bẩn

### Cách hiểu thực dụng

Không cần tranh luận `/c/news/` có truy cập được hay không.

Điểm chính là:

- nó truy cập được vì có `301`
- nhưng chính site vẫn đang link nội bộ tới một URL `301`

Đó mới là vấn đề.

### Kết luận ngắn

`Inlinks` và `Unique Inlinks` cao cho `/c/news/` chứng minh rằng:

- đây không phải redirect nhỏ lẻ
- đây là redirect URL đang được internal-link trên quy mô lớn
- vì vậy cần đổi internal links sang `/news/`, không tiếp tục link tới `/c/news/`
