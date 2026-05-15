## Coincu Note: Main Navigation Cleanup

Ngày: 2026-05-15

### Kết luận

Menu `Main Navigation` hiện không ổn và cần dọn.

### Những vấn đề thấy trực tiếp

#### 1. Cấu trúc menu bị nhân đôi

Các item top-level bị lặp:

- `Home`
- `News`
- `Markets`
- `Recommended`
- `PR`

Điều này cho thấy menu chính đang bị duplicate cấu trúc và không nên giữ nguyên.

#### 2. `Recommended` đang trỏ sang domain cũ `news.coincu.com`

Ví dụ:

- `https://news.coincu.com/158315-best-presale-cryptocurrencies-invest/`
- `https://news.coincu.com/159152-top-bitcoin-casinos-sites/`
- `https://news.coincu.com/158514-top-bitcoin-gambling-sites/`
- `https://news.coincu.com/166708-top-10-web3-coins-worth-investing-in-2023/`

Đây là không ổn vì:

- menu chính đang feed internal navigation sang domain cũ
- làm bẩn internal link graph
- có thể tiếp tục feed legacy URLs cho Google

#### 3. Nhiều link cũ/rác vẫn xuất hiện sitewide

Trong `Recommended` có nhiều bài rất cũ kiểu `2023`, gambling/review, ví dụ:

- `best-bitcoin-blackjack-casinos-in-2023`
- `best-tether-casino-sites-with-usdt-bonuses-2023`
- `top-5-best-anonymous-casinos-in-2023`
- `top-5-crash-gambling-sites-in-2023`

Nếu những link này nằm trong menu chính sitewide thì chất lượng internal navigation rất kém.

### Điều gì là tạm ổn

Các top-level item dạng `Category` như:

- `News`
- `Markets`
- `Knowledge`
- `PR`

về bản chất không sai.

Vấn đề nằm ở:

- bị lặp đôi
- và phần submenu/custom links bẩn

### Khuyến nghị

1. Xóa bản duplicate của các item top-level:

- `Home`
- `News`
- `Markets`
- `Recommended`
- `PR`

2. Trong `Recommended`, bỏ toàn bộ link `news.coincu.com/...`

3. Review mạnh tay các link `2023` gambling/review cũ

4. Giữ menu chính thật gọn, chỉ nên còn:

- Home
- News
- Markets
- Knowledge
- Reviews
- PR

5. Nếu vẫn muốn giữ `Recommended`:

- chỉ giữ link sạch trên `coincu.com`
- chỉ giữ trang còn sống và còn giá trị

### Kết luận ngắn

`Main Navigation` hiện fail về menu hygiene.

Không chỉ là duplicate route issue, mà là:

- menu bị duplicate
- internal links trỏ domain cũ
- nhiều link cũ/rác xuất hiện sitewide

Đây là một trong những khu vực nên dọn sớm.
