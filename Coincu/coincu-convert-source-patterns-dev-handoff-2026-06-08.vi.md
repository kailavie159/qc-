# Coincu Convert Source Patterns Dev Handoff

## Mục tiêu

Xác định đúng nguồn phát sinh broken internal links tới cụm:
- `https://coincu.com/convert-crypto-to-fiat`
- `https://coincu.com/convert-crypto-to-fiat/*`

Không nên xử lý bằng cách mở tay hàng chục nghìn bài trước. Cần sửa ở nguồn sinh link.

## Dữ liệu

Nguồn:
- `/home/thana2/coincu-3rd/all_inlinks.csv`
- `Coincu/coincu-convert-broken-internal-links-detail-2026-06-08.csv`
- `Coincu/coincu-convert-broken-internal-links-source-posts-2026-06-08.csv`

Số liệu:
- `33,150` broken-link rows
- `24,461` source URLs

## Nguồn phát sinh chính đã xác định

### 1. Template `/t/` (tag archive)

Xác nhận:
- `/t/...` là tag archive route thật
- REST check ví dụ:
  - `https://coincu.com/t/apple-store/`

Khối lượng:
- `11,881` source URLs thuộc nhóm `/t/`

Ý nghĩa:
- đây không phải từng bài riêng lẻ
- broken links ở nhóm này phải được sửa ở template/archive rendering, không phải editor mở từng URL

## 2. Block `conversions` trong cụm `/top-crypto-coins/*`

Khối lượng:
- `1,241` source URLs `top-crypto-coins/*`
- nhưng `9,928` broken-link rows vì mỗi URL thường sinh `8` link hỏng

Dấu vết kỹ thuật:
- tất cả đều nằm trong `Content`
- XPath lặp lại theo cùng một pattern:

```text
//body/div/div[@class='main']/div[@class='content']/div/div/div[1]/div[@class='conversions']/div[2]/div[1..8]/a
```

Ví dụ:
- `https://coincu.com/top-crypto-coins/opn-price-update`
- `https://coincu.com/top-crypto-coins/eth-price-update`
- `https://coincu.com/top-crypto-coins/bnb-price-update`
- `https://coincu.com/top-crypto-coins/btc-price-update`

Ý nghĩa:
- đây là block/module chung tên kiểu `conversions`
- không nên sửa tay từng page `top-crypto-coins/*`

## Dev cần làm

### P1. Sửa template/archive của `/t/`
- tìm nơi render internal links `Convert` trong template tag archive
- gỡ toàn bộ link cũ trỏ về:
  - `https://coincu.com/convert-crypto-to-fiat`
  - `https://coincu.com/convert-crypto-to-fiat/*`

### P2. Sửa block/module `conversions` của `top-crypto-coins`
- tìm component / template / partial đang render:
  - `div class="conversions"`
- gỡ hoặc thay toàn bộ link cũ `convert-crypto-to-fiat`
- nếu cần giữ tính năng, đổi sang URL chuẩn sống:
  - `https://coincu.com/instant-crypto-converter-real-time`

## Kỳ vọng sau fix

1. nhóm `/t/` không còn internal link sang route cũ `convert-crypto-to-fiat`
2. nhóm `/top-crypto-coins/*` không còn cụm `8` broken convert links trong block `conversions`
3. recrawl lại sẽ làm giảm mạnh:
  - `24,461` source URLs
  - `33,150` broken-link rows

## File tham chiếu

- Broken source posts:
  - `Coincu/coincu-convert-broken-internal-links-source-posts-2026-06-08.csv`
- Broken detail rows:
  - `Coincu/coincu-convert-broken-internal-links-detail-2026-06-08.csv`
- Convert child URLs:
  - `Coincu/coincu-convert-crypto-to-fiat-child-urls-2026-06-08.csv`
- Convert cluster handoff:
  - `Coincu/coincu-convert-cluster-dev-handoff-2026-06-08.vi.md`

