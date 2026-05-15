## Coincu Checklist: Sitemap Hygiene

Ngày: 2026-05-15

### Mục tiêu

Làm sạch sitemap để nó chỉ còn chứa:

- URL chuẩn
- URL sống
- URL thực sự muốn Google index

### Quy tắc nền

Một URL chỉ nên ở sitemap nếu đồng thời thỏa cả 3 điều kiện:

1. trả `200`
2. là canonical URL
3. là trang thực sự muốn index

### 1. Bỏ toàn bộ login URLs khỏi sitemap

Từ local file `batch1_sitemap_login_sample.csv`, các URL kiểu sau phải ra khỏi sitemap:

- `https://coincu.com/coincu-login/`
- `https://coincu.com/coincu-login/?action=lostpassword`
- `https://coincu.com/coincu-login/?redirect_to=...`

Lý do:

- là `Non-Indexable`
- không có giá trị search
- chỉ làm bẩn discovery

### 2. Bỏ query variants khỏi sitemap

Ví dụ:

- `?noamp=mobile`
- login / redirect queries
- mọi URL có query nhưng không phải canonical thật

Ví dụ cần loại:

- `/sec-delays-solana-etf-decision/?noamp=mobile`
- `/news/sec-delays-solana-etf-decision/?noamp=mobile`

### 3. Bỏ URL legacy / domain cũ

Không để trong sitemap:

- URL `news.coincu.com/...`
- URL cũ chỉ tồn tại để redirect

### 4. Bỏ URL đang redirect

Từ local `sitemaps_all.csv`, nhiều URL hiện đang `301` nhưng vẫn xuất hiện.

Ví dụ:

- `https://coincu.com/221956-best-bitcoin-blackjack-casinos-in-2023/`
- `https://coincu.com/223491-best-tether-casino-sites-with-usdt-bonuses-2023/`
- `https://coincu.com/224023-top-5-crash-gambling-sites/`

Các URL này không nên nằm trong sitemap.

Nếu còn muốn index, chỉ để URL đích cuối cùng.

### 5. Bỏ URL `404 / 410 / 5xx`

Ví dụ local đã thấy:

- `https://coincu.com/158315-best-presale-cryptocurrencies-invest/` từng ra `404`

Nguyên tắc:

- `404`
- `410`
- `5xx`

không bao giờ nên nằm trong sitemap.

### 6. Bỏ duplicate article routes

Canonical bài viết hiện đã chốt là:

- `https://coincu.com/{slug}/`

Vì vậy sitemap không được chứa thêm:

- `/news/{slug}/`
- `/analysis/{slug}/`
- `/blockchain/{slug}/`
- `/markets/{slug}/`
- `/blockchain-event/{slug}/`

### 7. Chỉ giữ canonical post URLs

Giữ:

- `https://coincu.com/{post-name}/`

Không giữ các route phụ của cùng bài viết.

### 8. Category / hub pages

Các trang kiểu:

- `/c/news/`
- `/c/markets/`
- `/c/knowledge/`

có thể giữ nếu:

- đó là canonical archive pages
- và thực sự muốn index

### 9. Tag pages

Đối với tag URLs:

- nếu mỏng, không có giá trị, hoặc `noindex` thì bỏ khỏi sitemap
- chỉ giữ nếu là landing page thật sự muốn index

### 10. Image sitemap

`image:image` tự nó không sai.

Nhưng chỉ nên để image URLs nếu:

- ảnh đích trả `200`
- không còn `403`
- không còn `301` qua domain cũ

Nếu image URLs vẫn lỗi, không nên tiếp tục feed chúng trong image sitemap.

### 11. Ưu tiên dọn trước trên Coincu

1. `/coincu-login/` và mọi biến thể `redirect_to=`
2. mọi URL có `?noamp=mobile`
3. mọi URL trong sitemap hiện đang `301/404`
4. mọi article URL không phải canonical `/{slug}/`
5. broken image URLs trong image sitemap

### 12. Kết quả mong muốn

- sitemap chỉ còn URL sống và chuẩn
- giảm discovery noise
- giảm crawl waste
- hỗ trợ làm sạch bucket `Crawled - currently not indexed`
