## Coincu Note: Footer Navigation Cleanup

Ngày: 2026-05-15

### Kết luận

Menu `Footer Navigation` hiện không ổn và nên được dọn mạnh hoặc dựng lại từ đầu.

### Những vấn đề thấy trực tiếp

- menu có số lượng item quá lớn: `218`
- nhiều item bị lặp rất nhiều lần:
  - `Live Prices`
  - `Trending`
  - `Binance`
  - `NFT`
  - `Solana`
  - `Polygon`
  - `Coinbase`
  - `CryptoLinks`
- có item trỏ homepage nhưng label không khớp:
  - `Live Prices` -> `https://coincu.com/`
- có custom path cần review:
  - `https://coincu.com/bestCrypto/trending/`
- có external link không cần thiết trong footer nav:
  - `http://lux.world/`
- có item URL rỗng:
  - `CryptoLinks`

### Điều gì là ổn

Các tag URL như:

- `https://coincu.com/t/nft/`
- `https://coincu.com/t/binance/`
- `https://coincu.com/t/polygon/`
- `https://coincu.com/t/metaverse/`

về cấu trúc thì không sai, vì `t` là tag base.

Tuy nhiên, việc đưa quá nhiều tag links lặp lại vào footer vẫn là internal-link noise.

### Đánh giá SEO

Đây không phải nguồn chính của duplicate route article kiểu:

- `/news/{slug}/`
- `/analysis/{slug}/`

Nhưng đây là vấn đề `sitewide internal link hygiene` rõ ràng vì:

- footer xuất hiện trên toàn site
- link rác/lặp bị nhân lên trên rất nhiều trang
- làm bẩn internal link graph
- làm nặng thêm crawl noise

### Khuyến nghị

Không nên sửa từng item lẻ.

Nên:

1. xóa hoặc dọn mạnh menu `Footer Navigation` hiện tại
2. dựng lại menu mới, rất gọn

### Chỉ nên giữ các link thật sự cần trong footer nav

- About Us
- Contact Us
- Terms and Conditions
- Privacy / Policy
- Coincu Partners
- Verified Team
- Editorial / Disclosure pages nếu cần

Nếu muốn giữ tag/hub links:

- chỉ giữ một số ít trang chiến lược
- không để hàng loạt tag links lặp sitewide

### Kết luận ngắn

`Footer Navigation` hiện tại nên được rebuild từ đầu.

Lý do không phải vì duplicate route bài viết, mà vì:

- menu bẩn
- nhiều link lặp
- nhiều item không có giá trị
- tạo internal-link noise trên toàn site
