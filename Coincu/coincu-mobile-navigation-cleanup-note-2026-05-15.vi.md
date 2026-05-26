## Coincu Note: Mobile Navigation Cleanup

Ngày: 2026-05-15  
Cập nhật brief triển khai: 2026-05-26

### Kết luận

Menu `Mobile Navigation` hiện tại không nên sửa tay từng item nữa.

Nên rebuild lại từ đầu, xóa toàn bộ duplicate, và chỉ giữ đúng một cấu trúc menu mobile gọn như dưới đây.

### Vấn đề hiện tại

- menu đang có quá nhiều item trùng
- các cụm `Coincu`, `News`, `Markets`, `Knowledge`, `Reviews`, `Recommended`, `PR` bị lặp
- nhiều submenu cũ bị nhân bản
- vẫn có legacy link kiểu `news.coincu.com/...`
- nếu menu này đang active, nó tạo internal-link noise trên toàn site

### Cách xử lý đề xuất cho dev

1. Không cleanup thủ công menu cũ `154` item
2. Tạo lại `Mobile Navigation` từ đầu
3. Mỗi item chỉ giữ đúng `1` bản
4. Nếu item đúng tên nhưng đang trỏ sai URL thì sửa URL, không cần tạo thêm item mới
5. Xóa toàn bộ item duplicate, legacy, hoặc ngoài cấu trúc chuẩn bên dưới

### Cấu trúc menu mobile chuẩn cần giữ

- `Coincu / Home` → `https://coincu.com/`
- `News` → `https://coincu.com/news/`
- `Markets` → `https://coincu.com/markets/`
- `Knowledge` → `https://coincu.com/knowledge/`
- `Reviews` → `https://coincu.com/crypto-reviews/`
- `Recommended` → `https://coincu.com/recommended/`
- `PR` → `https://coincu.com/pr/sponsored-articles-pr/`

### Submenu duy nhất cần giữ dưới `Recommended`

- `https://coincu.com/best-presale-cryptocurrencies/`
- `https://coincu.com/best-web3-cryptocurrencies/`
- `https://coincu.com/best-tether-casino-sites-with-usdt-bonuses/`
- `https://coincu.com/top-cryptocurrency-projects-2026/`
- `https://coincu.com/top-bitcoin-gambling-sites/`
- `https://coincu.com/top-bitcoin-casinos-sites/`
- `https://coincu.com/best-bitcoin-blackjack-casinos/`
- `https://coincu.com/top-5-best-p2p-crypto-exchanges/`

### Phải xóa khỏi menu mobile mới

- toàn bộ item duplicate
- toàn bộ link `news.coincu.com/...`
- toàn bộ category/subcategory cũ ngoài danh sách chuẩn ở trên
- các item cũ/rác bị nhân lên nhiều lần

### Ghi chú xác minh URL

Đã check live ngày `2026-05-26`:

- tất cả URL trong brief này đang trả về `200`
- không có URL nào trong danh sách chuẩn bị redirect sang đích khác

### Kết luận ngắn

`Mobile Navigation` nên rebuild từ đầu theo đúng danh sách URL chuẩn ở trên.

Không nên tiếp tục sửa tay menu cũ.
