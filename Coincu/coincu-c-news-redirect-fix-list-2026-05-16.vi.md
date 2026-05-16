## Coincu `/c/news/` Redirect Fix List

Ngày check live: `2026-05-16`

### Kết luận

- `https://coincu.com/c/news/` đang là `301`
- đích là `https://coincu.com/news/`
- `https://coincu.com/news/` là URL `200` canonical hiện tại

Vì vậy:

- `giữ redirect 301`
- `sửa tất cả internal links đang trỏ tới /c/news/`

### Rule sửa

- trước: `https://coincu.com/c/news/`
- sau: `https://coincu.com/news/`

Nếu có phân trang:

- trước: `https://coincu.com/c/news/page/2/`
- sau: `https://coincu.com/news/page/2/`

### List chỗ cần sửa đã thấy trên HTML live homepage

#### 1. Top menu `News`

- hiện tại đang dùng: `href="/c/news/"`
- cần đổi thành: `href="/news/"`

#### 2. Block `LIVE UPDATES`

- hiện tại đang dùng: `href="/c/news/"`
- cần đổi thành: `href="/news/"`

#### 3. Widget/menu phụ homepage `nav_menu-3`

- hiện tại đang dùng: `href="/c/news/"`
- cần đổi thành: `href="/news/"`

#### 4. Mobile/off-canvas menu `News`

- hiện tại đang dùng: `href="/c/news/"`
- cần đổi thành: `href="/news/"`

### Chỗ không cần sửa theo case này

Footer `Product > News` hiện đang là:

- `https://coincu.com/news/`

Chỗ này đang đúng với canonical hiện tại, nên `không cần đổi sang /c/news/`.

### Bằng chứng kỹ thuật

#### Live

- `curl -I https://coincu.com/c/news/` -> `301`
- `Location: https://coincu.com/news/`
- HTML final của `/c/news/` có:
  - canonical: `https://coincu.com/news/`
  - `og:url`: `https://coincu.com/news/`

#### Local crawl

Trong `internal_all.csv`, URL `https://coincu.com/c/news/` được ghi nhận là:

- `301`
- `Non-Indexable`
- `Redirected`
- `Redirect URL = https://coincu.com/news/`
- `Inlinks = 188863`
- `Unique Inlinks = 47948`

Trong `sitemaps_all.csv` còn thấy:

- `https://coincu.com/c/news/`
- `https://coincu.com/c/news/page/2/`

đều đang là `301`.

### Cách làm đúng

1. Đổi các internal links `/c/news/` -> `/news/`
2. Giữ redirect `301 /c/news/ -> /news/`
3. Loại `/c/news/` khỏi nguồn sinh sitemap nếu còn
4. Purge cache
5. Recheck HTML live để confirm không còn `href="/c/news/"`
