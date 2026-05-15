## Coincu Checklist: Lam Gi Truoc Next.js Va Lam Gi Sau Next.js

Ngay: 2026-05-15

Muc tieu:

- tach ro viec nao nen lam ngay tren site hien tai
- viec nao nen doi qua Next.js roi lam sach tu dau

### 1. Nen lam ngay tren site hien tai

Day la nhung viec dang anh huong truc tiep toi crawl/index hien tai.

#### Media recovery

- hoan tat restore media
- uu tien chot not cum `2022/12`
- tiep tuc verify sample image URLs tra `200 image/*`

Ly do:

- image `403` la loi nang that
- dang gay mat image index

#### Giu va theo doi batch `410` da lam

- giu nguyen cac batch `410` da co hieu luc
- de Google recrawl va loai bot URL rac

Ly do:

- day la viec da co tac dung thuc te
- khong nen bo giua chung

#### Giu cleanup `?noamp=mobile`

- batch da verify sach `5/5`
- neu con source nao sinh query nay thi chan tiep

Ly do:

- day la mot lop URL variant da duoc xu ly tot

#### Go redirect sai intent ro rang

- uu tien nhung redirect dang tro sai bai
- hoac dang tro ve homepage mot cach yeu

Ly do:

- day la loi huong URL xau va de lai tin hieu internal khong tot

#### Neu site cu van con chay them mot thoi gian

- bo link `news.coincu.com` khoi cac menu quan trong
- bo link `#`
- bo item demo/theme leftovers obvious

### 2. Khong dang ton cong sua sau trong WordPress neu sap migrate

Neu migration Next.js da gan, nhung viec sau nen chot rule ngay bay gio, nhung trien khai sach trong Next.js thi hop ly hon:

- rebuild toan bo:
  - `Main Navigation`
  - `Mobile Navigation`
  - `Top Bar Navigation`
  - `Footer Navigation`
  - `Footer Links`
- cleanup duplicate structure trong menu
- cleanup section blocks / related posts / homepage modules
- cleanup internal-link sources toan site
- chot route architecture cho bai viet
- chan han duplicate route discovery tu cac route phu

### 3. Can chot decision ngay truoc khi migrate

Day la cac quyet dinh can khoa som de dev build dung trong Next.js.

#### Canonical post URL

- chi dung `/{post-name}/`

#### Route phu neu con ton tai

- luon `301` ve `/{slug}/`

#### Khong mang sang Next.js

- link `news.coincu.com`
- query `?noamp=mobile`
- menu duplicate
- link `#`
- theme/demo leftovers

#### Sitemap rules

- chi xuat canonical URLs
- khong dua login/query/legacy/redirecting URLs vao sitemap

#### Internal-link rules

- moi article card
- related post
- section block
- menu item

deu phai link ve `/{slug}/`

### 4. Nen lam sau khi qua Next.js

Day la luc lam sach that su trong codebase moi:

- build lai navigation tu dau
- build lai homepage blocks / section templates / related posts
- code redirect rules trong app/server
- code sitemap sach
- code canonical sach
- code bo query variants
- code image delivery / legacy image redirects neu can
- audit lai toan site sau launch

### 5. Sau khi launch Next.js phai recheck ngay

- crawl toan site
- sample duplicate routes
- sample old redirects
- sitemap output
- image URLs
- menus / homepage / related posts
- GSC coverage va image indexing

### 6. Ket luan ngan

Neu migration Next.js da gan:

- sua cai dang chay tren site cu
- khong ton cong dai tu menu/template sau trong WordPress
- mang phan cleanup lon sang Next.js

Neu migration con xa:

- ngoai media + `410` + `?noamp=mobile`, co the don them menu live
