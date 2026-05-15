## Coincu Handoff: Phase 2 - Check Internal Link Sources

Ngày: 2026-05-15

### Mục tiêu

Sau khi đã chốt:

- canonical post route là `/{post-name}/`
- nhiều route phụ đã `301` về root slug

thì bước tiếp theo là tìm xem **nguồn internal nào vẫn đang tiếp tục nhả ra route phụ** hoặc query variants.

Nếu không xử lớp này, Google vẫn tiếp tục crawl URL bẩn dù redirect đã tồn tại.

### Những gì crawl data đang gợi ý

Từ `all_inlinks.csv`, các khu vực lặp lại nhiều nhất trong HTML path và link position hiện nằm ở:

- `Header`
- `Navigation`
- `Content`
- `Aside`

Các dấu hiệu cần ưu tiên kiểm tra:

- `top-bar`
- `main-menu`
- `nav_menu-3`
- các block/sidebar kiểu `media_image-5`
- các block content section trên các trang section như `/news/`, `/analysis/`, `/blockchain/`, `/markets/`, `/blockchain-event/`

Điều này cho thấy nguồn phát sinh URL không chỉ nằm trong bài viết, mà nhiều khả năng nằm ở:

- menu dùng chung
- sidebar/menu widget
- section templates
- block/module kéo bài theo category

### Cần kiểm tra theo thứ tự này

#### 1. Header / Top Bar Menu

Kiểm tra:

- menu chính
- top bar menu
- mobile menu

Mục tiêu:

- không render link bài kiểu `/news/{slug}/`, `/analysis/{slug}/`, `/blockchain/{slug}/`
- nếu là link bài viết thì chỉ render `/{slug}/`

#### 2. Sidebar Navigation / Widget Menus

Kiểm tra:

- `nav_menu-3`
- sidebar navigation
- widget menu

Mục tiêu:

- không để link bài viết route phụ xuất hiện trong nav/sidebar

#### 3. Section Archive Templates

Kiểm tra các section:

- `/news/`
- `/analysis/`
- `/blockchain/`
- `/markets/`
- `/blockchain-event/`

Mục tiêu:

- các bài trong listing phải link về `/{slug}/`
- không link sang `/news/{slug}/`, `/analysis/{slug}/`, `/blockchain/{slug}/`...

#### 4. Home / Category Blocks / Related Posts

Kiểm tra:

- home blocks
- category blocks
- related posts
- content modules kéo bài tự động

Mục tiêu:

- mọi link bài đều dùng clean root slug

#### 5. Query Variant Sources

Kiểm tra riêng các chỗ có thể còn sinh:

- `?noamp=mobile`

Mục tiêu:

- không còn internal link nào append `?noamp=mobile`
- không còn module/feed cũ sinh query này

### Checklist ngắn cho dev/WP

- Header/top-bar menu: chỉ output clean article URLs
- Main menu/mobile menu: chỉ output clean article URLs
- Sidebar/nav widgets: chỉ output clean article URLs
- Section templates: không output route bài có prefix
- Related posts/home blocks: không output route bài có prefix
- Không sinh `?noamp=mobile` ở internal links

### Kết quả mong muốn sau Phase 2

- internal links chỉ còn trỏ tới `/{slug}/`
- route phụ chỉ còn tồn tại như URL bị gọi trực tiếp và trả `301`
- Google không còn được feed thêm duplicate article routes từ nội bộ site
