## Coincu Checklist: Làm Gì Trước Next.js Và Làm Gì Sau Next.js

Ngày: 2026-05-15

Mục tiêu:

- tách rõ việc nào nên làm ngay trên site hiện tại
- việc nào nên đợi qua Next.js rồi làm sạch từ đầu

### 1. Nên làm ngay trên site hiện tại

Đây là những việc đang ảnh hưởng trực tiếp tới crawl/index hiện tại.

#### Media recovery

- hoàn tất restore media
- ưu tiên chốt nốt cụm `2022/12`
- tiếp tục verify sample image URLs trả `200 image/*`

Lý do:

- image `403` là lỗi nặng thật
- đang gây mất image index

#### Giữ và theo dõi batch `410` đã làm

- giữ nguyên các batch `410` đã có hiệu lực
- để Google recrawl và loại bớt URL rác

Lý do:

- đây là việc đã có tác dụng thực tế
- không nên bỏ giữa chừng

#### Giữ cleanup `?noamp=mobile`

- batch đã verify sạch `5/5`
- nếu còn source nào sinh query này thì chặn tiếp

Lý do:

- đây là một lớp URL variant đã được xử lý tốt

#### Gỡ redirect sai intent rõ ràng

- ưu tiên những redirect đang trỏ sai bài
- hoặc đang trỏ về homepage một cách yếu

Lý do:

- đây là lỗi hướng URL xấu và để lại tín hiệu internal không tốt

#### Nếu site cũ vẫn còn chạy thêm một thời gian

- bỏ link `news.coincu.com` khỏi các menu quan trọng
- bỏ link `#`
- bỏ các item demo/theme leftovers obvious

### 2. Không đáng tốn công sửa sâu trong WordPress nếu sắp migrate

Nếu migration Next.js đã gần, những việc sau nên chốt rule ngay bây giờ, nhưng triển khai sạch trong Next.js thì hợp lý hơn:

- rebuild toàn bộ:
  - `Main Navigation`
  - `Mobile Navigation`
  - `Top Bar Navigation`
  - `Footer Navigation`
  - `Footer Links`
- cleanup duplicate structure trong menu
- cleanup section blocks / related posts / homepage modules
- cleanup internal-link sources toàn site
- chốt route architecture cho bài viết
- chặn hẳn duplicate route discovery từ các route phụ

### 3. Cần chốt decision ngay trước khi migrate

Đây là các quyết định cần khóa sớm để dev build đúng trong Next.js.

#### Canonical post URL

- chỉ dùng `/{post-name}/`

#### Route phụ nếu còn tồn tại

- luôn `301` về `/{slug}/`

#### Không mang sang Next.js

- link `news.coincu.com`
- query `?noamp=mobile`
- menu duplicate
- link `#`
- theme/demo leftovers

#### Sitemap rules

- chỉ xuất canonical URLs
- không đưa login/query/legacy/redirecting URLs vào sitemap

#### Internal-link rules

- mọi article card
- related post
- section block
- menu item

đều phải link về `/{slug}/`

### 4. Nên làm sau khi qua Next.js

Đây là lúc làm sạch thật sự trong codebase mới:

- build lại navigation từ đầu
- build lại homepage blocks / section templates / related posts
- code redirect rules trong app/server
- code sitemap sạch
- code canonical sạch
- code bỏ query variants
- code image delivery / legacy image redirects nếu cần
- audit lại toàn site sau launch

### 5. Sau khi launch Next.js phải recheck ngay

- crawl toàn site
- sample duplicate routes
- sample old redirects
- sitemap output
- image URLs
- menus / homepage / related posts
- GSC coverage và image indexing

### 6. Kết luận ngắn

Nếu migration Next.js đã gần:

- sửa cái đang cháy trên site cũ
- không tốn công đại tu menu/template sâu trong WordPress
- mang phần cleanup lớn sang Next.js

Nếu migration còn xa:

- ngoài media + `410` + `?noamp=mobile`, có thể dọn thêm menu live
