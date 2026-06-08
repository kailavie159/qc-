# Coincu Convert Cluster Dev Handoff

## Vấn đề

Cụm URL `Convert` của Coincu đang hỏng nhưng vẫn được internal link trên site.

URL gốc:
- `https://coincu.com/convert-crypto-to-fiat`

Các URL con:
- dạng `https://coincu.com/convert-crypto-to-fiat/...`

## Dữ liệu xác nhận

Nguồn dữ liệu:
- recrawl mới nhất: `/home/thana2/coincu-3rd/internal_all.csv`
- sitemap export: `/home/thana2/coincu-3rd/sitemaps_all.csv`
- full child URL export: `Coincu/coincu-convert-crypto-to-fiat-child-urls-2026-06-08.csv`

Tổng số URL con bị sinh ra:
- `9,920`

Trạng thái:
- `404`: `8,504`
- `0 / No Response`: `1,197`
- `403`: `219`

Ví dụ:
- `https://coincu.com/convert-crypto-to-fiat/6573-opn-to-cny`
- `https://coincu.com/convert-crypto-to-fiat/6961-opn-to-gbp`
- `https://coincu.com/convert-crypto-to-fiat/2173-eth-to-cny`

## Root cause hiện thấy từ crawl

1. URL `Convert` vẫn đang được internal link trên site.
2. Link này không chỉ ở menu; phần lớn dấu vết nằm trong `Content`, rất giống block/widget/reusable section.
3. Cụm route `/convert-crypto-to-fiat/` hiện không hoạt động ổn định nhưng vẫn sinh ra và bị crawl.

## Dev cần làm

### P1. Ngừng internal link tới cụm Convert

Tìm và gỡ tất cả internal links trỏ tới:
- `https://coincu.com/convert-crypto-to-fiat`
- các biến thể dưới `/convert-crypto-to-fiat/`

Ưu tiên kiểm tra:
- menu nếu còn item `Convert`
- UX Blocks / reusable blocks
- sidebar / related blocks / homepage blocks
- template bài viết / category template

Mục tiêu:
- không còn block/card/menu nào internal link sang cụm `Convert`

### P2. Quyết định giữ hay kill tính năng Convert

#### Nếu không còn dùng Convert
- retire toàn bộ route `/convert-crypto-to-fiat`
- trả `410` hoặc `301` theo phương án site chọn
- quan trọng: không để route tiếp tục bị internal link

#### Nếu vẫn muốn giữ Convert
- sửa route gốc `/convert-crypto-to-fiat` để trả `200`
- xử lý logic tạo URL con để không sinh ra hàng nghìn URL chết
- chỉ giữ các URL thực sự cần index nếu có

## Kỳ vọng sau fix

1. `https://coincu.com/convert-crypto-to-fiat` không còn `0 / No Response`
2. không còn internal link sitewide tới `Convert`
3. số URL lỗi dưới `/convert-crypto-to-fiat/` giảm mạnh ở crawl sau
4. cụm này không còn xuất hiện hàng loạt trong sitemap/crawl

## File tham chiếu

- Recrawl audit tổng:
  - `Coincu/coincu-3rd-recrawl-audit-2026-06-05.md`
- Full list child URLs:
  - `Coincu/coincu-convert-crypto-to-fiat-child-urls-2026-06-08.csv`

