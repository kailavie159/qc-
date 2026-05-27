## Coincu Dev Handoff: Dọn Sitemap Đang Chứa URL 404

Ngày: `2026-05-27`

### Kết luận ngắn

Recrawl mới cho thấy sitemap của Coincu không chỉ có vấn đề `301`.

Trong `sitemaps_all.csv` hiện có:

- `5,385` URL `404`

Điều này có nghĩa là sitemap vẫn đang emit một lượng lớn URL đã chết hoặc không còn hợp lệ.

Sitemap không được chứa URL `404`.

### Vì sao đây là lỗi cần sửa

Nếu sitemap chứa `404`, Google sẽ:

- crawl vào URL chết
- tốn crawl budget vô ích
- chậm hơn trong việc khám phá URL chuẩn
- giảm trust vào sitemap

### Phát hiện chính từ file `404`

File tham chiếu:

- `sitemaps_all_status_404.csv`

Tổng:

- `5,385` URL `404`

### Các nhóm lớn nhất

#### 1. Bucket `convert-crypto-to-fiat`

- `1,648` URL

Ví dụ:

- `https://coincu.com/convert-crypto-to-fiat/451-btc-to-chf`
- `https://coincu.com/convert-crypto-to-fiat/8341-btc-to-eur`

Diễn giải:

Đây nhiều khả năng là một tool/bucket generator đã chết nhưng vẫn bị sitemap emit.

#### 2. Bucket `currencies`

- `126` URL

Ví dụ:

- `https://coincu.com/currencies/eth-ethereum/`
- `https://coincu.com/currencies/cra-crabada/`

Diễn giải:

Đây là cụm detail/data pages không còn sống nhưng vẫn đang được đưa vào sitemap.

#### 3. Legacy content routes / content pages chết

Các nhóm:

- `/news` -> `100`
- `/markets` -> `55`
- `/analysis` -> `51`
- `/bitcoin` -> `14`
- `/press-release` -> `13`
- `/ethereum` -> `11`
- `/pr` -> `11`

Ví dụ:

- `https://coincu.com/news/toncoin-lands-on-robinhood-as-users-tvl/`
- `https://coincu.com/markets/goldman-sachs-fed-rate-cuts/`
- `https://coincu.com/analysis/coinmarketcap-terra-classic-upgrade-majorsurge/`

Diễn giải:

Đây cho thấy sitemap vẫn đang emit:

- route cũ
- hoặc các content URLs đã chết
- hoặc cả hai

#### 4. Bucket `market` / assets-like

- `/market` -> `31`

Ví dụ:

- `https://coincu.com/market/public/assets/images/chain-logo/XRP%20Ledger.png`

Diễn giải:

Đây là dấu hiệu sitemap đang lôi cả asset path hoặc path nội bộ của module market vào.

#### 5. Bucket `crypto-price-prediction`

- `25` URL

Ví dụ:

- `https://coincu.com/crypto-price-prediction/TON-toncoin`

Diễn giải:

Đây có thể là một bucket data/programmatic cũ đã chết.

#### 6. Taxonomy / author / language leftovers

- `/author` -> `17`
- `/vi` -> `9`
- `/uncategorized` -> `5`

Ví dụ:

- `https://coincu.com/author/Akinyemi%20Okedeji%20Amoo`
- `https://coincu.com/vi/currencies/egld-elrond-egld/`

Diễn giải:

Đây là các bucket phụ hoặc legacy branch không còn hợp lệ nhưng vẫn bị emit.

### Cách đọc đúng

`404 sitemap` hiện tại không phải một lỗi đơn lẻ.

Nó gồm ít nhất `4` lớp:

#### Lớp 1: tool / generator URLs đã chết

- `convert-crypto-to-fiat`

#### Lớp 2: data/detail buckets đã chết

- `currencies`
- `crypto-price-prediction`
- `market/public/assets/...`

#### Lớp 3: legacy content routes hoặc content pages đã chết

- `news`
- `analysis`
- `markets`
- `bitcoin`
- `ethereum`
- `pr`
- `press-release`

#### Lớp 4: taxonomy / author / language leftovers

- `author`
- `vi`
- `uncategorized`

### Cách sửa đúng

Không sửa bằng cách để Google tự bỏ qua.

Không sửa bằng cách chỉ redirect từng URL lẻ.

Phải sửa ở **nguồn sinh sitemap** và **bucket logic**.

### Việc dev cần làm

#### 1. Loại toàn bộ bucket `convert-crypto-to-fiat` khỏi sitemap nếu bucket này không còn sống

Nếu module/tool này đã retire hoặc không còn public:

- không emit bất kỳ URL nào của bucket này vào sitemap

#### 2. Rà các bucket data/programmatic đang chết

Review và loại khỏi sitemap nếu không còn dùng:

- `/currencies/`
- `/crypto-price-prediction/`
- `/market/public/assets/...`

Nếu các bucket này vẫn cần tồn tại, thì phải:

- khôi phục URL sống đúng
- hoặc chỉ emit các URL `200` final

#### 3. Với route content cũ, không emit URL chết

Review các nhóm:

- `/news/`
- `/analysis/`
- `/markets/`
- `/bitcoin/`
- `/ethereum/`
- `/pr/`
- `/press-release/`

Nếu đây là route cũ:

- sitemap phải emit final URL sống

Nếu bài đã chết:

- không được để URL đó ở sitemap nữa

#### 4. Rà taxonomy / author / language branches

Review các nhóm:

- `/author/`
- `/vi/`
- `/uncategorized/`

Bucket nào không còn chiến lược index:

- loại khỏi sitemap
- hoặc noindex + stop emitting

### Chỗ dev cần kiểm

- plugin sitemap đang dùng
- custom code / filters sinh URLs cho sitemap
- module market / tool pages / programmatic pages
- legacy route mappings
- bất kỳ branch nào còn emit URL chết theo template cũ

### Kết quả mong muốn

Sau fix:

- sitemap không còn URL `404`
- bucket tool/data đã retire không còn bị emit
- content routes cũ không còn xuất hiện nếu đích đã chết
- author/lang/taxonomy leftovers không còn tự động vào sitemap nếu không chủ đích index

### File tham chiếu

- `/home/thana2/coincu-2nd/sitemaps_all_status_404.csv`

### Kết luận ngắn

Coincu hiện có `5,385` URL `404` trong sitemap.

Đây không chỉ là vài bài chết lẻ.

Nó là lỗi ở tầng:

- bucket tools đã chết
- bucket data/programmatic đã chết
- legacy content routes
- taxonomy/author/lang leftovers

Sửa đúng là sửa ở nguồn sinh sitemap, không phải chỉ nhìn từng URL riêng lẻ.
