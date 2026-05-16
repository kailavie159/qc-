## Cơ sở chính thống của Google cho việc phải sửa internal links đang trỏ vào URL `301`

Ngày: `2026-05-16`

### Câu trả lời ngắn

Google không nói theo kiểu:

- `nhiều 301 sẽ bị phạt`

Nhưng Google nói rất rõ theo hướng:

- internal links nên trỏ tới `canonical URL`
- khi thay đổi URL thì phải cập nhật internal links sang URL mới
- duplicate/redirect URLs làm bot tốn thời gian crawl không cần thiết

Vì vậy, với case Coincu:

- `/c/news/` không phải canonical
- `/c/news/` đang `301` sang `/news/`
- nhưng site vẫn đang internal-link rất mạnh tới `/c/news/`

thì đây là một vấn đề kỹ thuật thật, không phải suy đoán.

### Nguồn chính thống từ Google

#### 1. Google Search Central: Canonicalization

Nguồn:

- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls

Ý chính Google nói:

- khi link trong nội bộ site, hãy link tới `canonical URL` thay vì `duplicate URL`
- redirects là tín hiệu mạnh để Google hiểu URL đích nên là canonical
- Google cũng nói tốt hơn là để bot dành thời gian crawl các trang mới/cập nhật, thay vì crawl các phiên bản duplicate

Ý nghĩa cho Coincu:

- `/c/news/` là duplicate/redirecting URL
- `/news/` mới là canonical URL
- nên internal links phải trỏ thẳng tới `/news/`

#### 2. Google Search Central: Site move / URL changes

Nguồn:

- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes

Ý chính Google nói:

- sau khi có mapping URL cũ -> URL mới, phải `update internal links`
- internal links trên site mới phải thay URL cũ bằng URL mới
- sitemap cũng phải chứa URL mới

Ý nghĩa cho Coincu:

- nếu `/c/news/` là URL cũ và `/news/` là URL cuối
- thì đúng theo khuyến nghị của Google, Coincu phải đổi internal links từ `/c/news/` sang `/news/`

#### 3. Google Search Central: Crawl budget

Nguồn:

- https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget

Ý chính Google nói:

- duplicate content / duplicate URLs làm crawl kém hiệu quả hơn
- mọi URL được Googlebot crawl đều tiêu tốn crawl budget
- nên nên giúp Google nhận diện và tránh phải crawl các bản duplicate không cần thiết

Ý nghĩa cho Coincu:

- mỗi lần bot đi vào `/c/news/`, nó lại phải qua thêm 1 bước redirect sang `/news/`
- nếu điều này lặp lại trên diện lớn thì đó là crawl inefficiency thật

### Case Coincu khớp với khuyến nghị của Google ở đâu

#### 1. Live check

Kiểm tra live ngày `2026-05-16`:

- `https://coincu.com/c/news/` -> `301`
- đích: `https://coincu.com/news/`
- `https://coincu.com/news/` -> `200`
- canonical HTML final = `https://coincu.com/news/`

=> `/news/` là canonical, `/c/news/` không phải canonical.

#### 2. Local crawl

Trong `internal_all.csv`, URL `https://coincu.com/c/news/` có:

- `301`
- `Non-Indexable`
- `Redirected`
- `Redirect URL = https://coincu.com/news/`
- `Inlinks = 188863`
- `Unique Inlinks = 47948`

Điều này chứng minh:

- đây không phải redirect nhỏ lẻ
- đây là redirect URL đang được internal-link ở quy mô lớn

#### 3. Live HTML vẫn đang render `/c/news/`

Trên homepage live vẫn thấy:

- top menu `News` dùng `/c/news/`
- block `LIVE UPDATES` dùng `/c/news/`
- widget/menu phụ dùng `/c/news/`
- mobile/off-canvas menu `News` dùng `/c/news/`

Trong khi footer `Product > News` lại dùng `/news/`.

=> internal linking hiện tại đang không nhất quán.

### Kết luận kỹ thuật đúng

Không nên diễn giải case này thành:

- `301 là xấu`

Diễn giải đúng là:

- `redirect URL đang bị internal-link rất mạnh`
- `internal links chưa trỏ thẳng vào canonical URL`
- `discovery và crawl path đang bẩn hơn mức cần thiết`

### Kết luận hành động

1. Giữ `301 /c/news/ -> /news/`
2. Đổi mọi internal links `/c/news/` thành `/news/`
3. Loại `/c/news/` khỏi nguồn sinh sitemap nếu còn
4. Recheck crawl để đảm bảo `/c/news/` không còn là internal destination lớn

### Một câu ngắn có thể dùng để gửi dev

`Google không cấm 301, nhưng Google khuyên internal links phải trỏ vào canonical URL cuối. Với Coincu, /c/news/ đang là 301 sang /news/ và vẫn có 188863 inlinks, nên cần đổi internal links sang /news/.`
