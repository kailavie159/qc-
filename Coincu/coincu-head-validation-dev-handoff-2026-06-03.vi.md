## Coincu Dev Handoff: Fix Lỗi HTML Sai Trong `<head>`

Ngày: `2026-06-03`

### Mục tiêu

Fix lỗi sitewide:

- `Validation: Invalid HTML Elements in Head`
- kéo theo khả năng phát sinh `Multiple <head>` trên một số URL

### Root cause đã xác nhận

Trên Coincu hiện có snippet:

- plugin: `HFCM by 99 Robots`
- snippet: `Top banner`

Snippet này đang inject HTML block kiểu:

```html
<div id="sevio-top-wrapper" ...>
  ...
</div>
```

vào bên trong `<head>`.

Đây là HTML không hợp lệ trong `<head>`.

### Vì sao phải fix

Khi `<head>` bị bẩn bởi `div` / HTML body-level:

- parser của browser và crawler có thể đọc metadata không ổn định
- canonical / meta robots / script / style có thể bị ảnh hưởng
- Screaming Frog báo lỗi diện rộng

### Việc dev cần làm

#### 1. Tìm snippet gây lỗi

Vào:

- `WP Admin`
- `HFCM by 99 Robots` / `Header Footer Code Manager`

Tìm snippet:

- `Top banner`

Hoặc snippet nào có comment tương tự:

- `HFCM by 99 Robots - Snippet # 1: Top banner`

#### 2. Kiểm tra vị trí inject hiện tại

Nếu snippet đang gắn vào:

- `Header`
- `Head`
- `Before </head>`

thì đó là sai với một block HTML banner.

#### 3. Chuyển phần HTML banner ra khỏi `<head>`

Nếu snippet chứa:

- `<div>`
- `<a>`
- `<img>`
- `<section>`
- ad wrapper / banner wrapper

thì phải chuyển phần này sang vị trí body-level:

- `After <body>`
- `Header`
- `Before content`
- hoặc render bằng theme / UX Block / template

#### 4. Chỉ giữ phần tử hợp lệ trong `<head>`

Trong `<head>` chỉ nên giữ:

- `title`
- `meta`
- `link`
- `style`
- `script`
- `base`
- `noscript`

Không để:

- `div`
- `p`
- `img`
- `a`
- `section`
- `article`

#### 5. Nếu snippet đang trộn cả JS/CSS và HTML

Tách thành 2 phần:

- `script` / `style` hợp lệ: có thể giữ trong `<head>` nếu thực sự cần
- HTML banner / wrapper: bắt buộc chuyển ra `body`

### Cách fix an toàn nhất

1. Disable tạm snippet `Top banner`
2. Purge cache
3. Check lại source HTML vài template chính
4. Nếu lỗi hết, dựng lại banner đúng vị trí trong `body`

### URL/template nên check sau fix

- `https://coincu.com/`
- `https://coincu.com/news/`
- `https://coincu.com/analysis/`
- `https://coincu.com/knowledge/`
- 1 bài post bất kỳ

### Acceptance criteria

Sau khi fix:

1. `view-source` không còn `<div` nằm bên trong `<head>`
2. Chỉ còn một `<head>` hợp lệ
3. `sitemap` và `page source` vẫn load bình thường
4. Recrawl lại thì:
   - `Invalid HTML Elements in Head` giảm mạnh hoặc về `0`
   - `Multiple <head>` nếu là side effect cũng giảm mạnh hoặc biến mất

### Kết luận ngắn

Đây là lỗi template/global, không phải lỗi từng bài.

Dev cần sửa ở nguồn inject snippet:

- đưa `Top banner` ra khỏi `<head>`
- chỉ để phần tử hợp lệ ở `<head>`
