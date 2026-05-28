## Coincu Dev Handoff: Lỗi HTML Trong `<head>`

Ngày: `2026-05-28`

### Kết luận ngắn

Recrawl mới báo:

- `Validation: Invalid HTML Elements in Head` trên `43,312` URL (`98.92%`)
- `Validation: Multiple <head> Tags` trên `130` URL

Direct check trên live templates cho thấy lỗi chính đã xác nhận được là:

- một snippet `HFCM by 99 Robots - Snippet # 1: Top banner`
- đang inject HTML dạng `<div ...>` vào thẳng trong `<head>`

Đây là HTML không hợp lệ trong `<head>`.

### Vì sao đây là lỗi quan trọng

Theo Google/Screaming Frog, khi có invalid elements trong `<head>`, các thẻ quan trọng phía sau có thể bị parser hoặc Google bỏ qua/đọc không ổn định.

Điều này có thể ảnh hưởng:

- canonical
- meta robots
- structured data
- scripts/styles quan trọng
- metadata nói chung

### Phát hiện đã xác nhận

Đã kiểm live trên các URL:

- `https://coincu.com/`
- `https://coincu.com/news/`
- `https://coincu.com/analysis/`
- `https://coincu.com/knowledge/`

Tất cả các template trên đều có comment:

- `HFCM by 99 Robots - Snippet # 1: Top banner`

và ngay sau đó là HTML kiểu:

```html
<div id="sevio-top-wrapper" ...>
  <div class="sevioads" ...></div>
  <script ...></script>
</div>
```

đặt **bên trong `<head>`** trước thẻ `</head>`.

### Diễn giải đúng

Trong `<head>`, các thẻ hợp lệ chủ yếu là:

- `title`
- `meta`
- `link`
- `script`
- `style`
- `base`
- `noscript`
- `template`

`<div>` không phải phần tử hợp lệ trong `<head>`.

Vì vậy snippet hiện tại đang làm hỏng cấu trúc `<head>` trên diện rộng.

### Nhiều khả năng root cause nằm ở đâu

Rất có thể là một snippet/plugin đang được cấu hình sai vị trí inject:

- `HFCM by 99 Robots`
- snippet tên: `Top banner`

Thay vì render trong:

- `body open`
- `header`
- `before content`

nó đang được render vào:

- `head`

### Cách sửa đúng

#### 1. Không inject HTML block vào `<head>`

Snippet `Top banner` không được chứa:

- `<div>`
- ad wrapper HTML
- UI markup

trong `<head>`.

#### 2. Di chuyển snippet này ra khỏi `<head>`

Nên render tại một vị trí body-level, ví dụ:

- ngay sau `<body>`
- trong header
- trước main content

Nhưng không phải trong `<head>`.

#### 3. Nếu cần giữ preload / preconnect / script

Các phần như:

- `link rel="preconnect"`
- `dns-prefetch`
- `script`
- `style`

có thể ở lại trong `<head>` nếu hợp lệ.

Nhưng wrapper HTML:

- `<div id="sevio-top-wrapper">...`

phải chuyển ra `body`.

### Về issue `Multiple <head> Tags`

Direct check nhanh trên các template mẫu không xác nhận có nhiều thẻ `<head>` thật sự theo nghĩa literal sitewide.

Hiện mới xác nhận chắc chắn:

- lỗi `invalid elements in head` là có thật và sitewide

Issue `Multiple <head> Tags` có thể là:

- một subset template khác
- hoặc side effect parser do `<head>` bị làm bẩn

Khuyến nghị:

- fix `HFCM top banner in head` trước
- recrawl lại
- nếu `Multiple <head>` vẫn còn, review tiếp đúng các URL còn lại

### Việc dev cần làm

1. Tìm snippet/plugin:

- `HFCM by 99 Robots`
- snippet `Top banner`

2. Kiểm vị trí render hiện tại

3. Chuyển snippet khỏi `<head>`

4. Giữ lại trong `<head>` chỉ các phần tử hợp lệ

5. Sau deploy:

- purge cache
- recrawl vài template chính
- xác nhận `<head>` không còn chứa `<div>`

### Kết quả mong muốn

Sau fix:

- không còn `<div>` trong `<head>`
- issue `Invalid HTML Elements in Head` giảm mạnh hoặc hết
- nếu `Multiple <head>` là side effect, nhiều khả năng cũng biến mất hoặc giảm mạnh

### Kết luận ngắn

Lỗi `<head>` của Coincu hiện đã có root cause rõ:

- snippet `HFCM by 99 Robots - Top banner`
- đang inject banner HTML vào thẳng trong `<head>`

Đây là lỗi template/global và nên được dev sửa ở nguồn inject snippet.
