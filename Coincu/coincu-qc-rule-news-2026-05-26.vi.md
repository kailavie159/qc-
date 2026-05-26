## Coincu QC Rule: News

Ngày: `2026-05-26`

### Mục tiêu

Chỉ giữ bài `news` nếu bài đó:

- có fact đáng tin
- có giá trị thêm ngoài mức rewrite
- không kéo chất lượng section đi xuống

### 1. Fail cứng

Nếu dính `1` trong các lỗi dưới đây thì xem như fail ngay, không cần chấm tiếp:

- headline hoặc claim chính không được source chứng minh
- không có source rõ cho fact quan trọng nhất
- có số liệu nhưng không có `as of date`
- body diễn giải sai bản chất so với source gốc
- URL live / canonical / indexability có vấn đề
- raw format, citation bể, HTML bẩn nặng
- bài gần như chỉ paraphrase từ nguồn khác, không có value thêm

### 2. Cách chấm điểm

Chấm `5` mục, mỗi mục từ `0` đến `2`.

Tổng điểm tối đa: `10`

#### A. Source strength

- `0`: không có source, source yếu, hoặc source không chứng minh claim
- `1`: có source trung gian hoặc source gốc nhưng dùng chưa đủ
- `2`: có source gốc hoặc source mạnh, gắn đúng claim chính

#### B. Trust / verifiability

- `0`: claim khó kiểm, thiếu date, thiếu context
- `1`: kiểm được một phần
- `2`: claim chính, số liệu, mốc thời gian đều rõ

#### C. Added value beyond rewrite

- `0`: chỉ viết lại từ nguồn khác
- `1`: có thêm chút context nhưng còn mỏng
- `2`: có đối chiếu, delta, bối cảnh, implication, hoặc verification riêng

#### D. Clarity / user benefit

- `0`: đọc xong vẫn không rõ chuyện gì quan trọng
- `1`: hiểu chuyện xảy ra nhưng chưa hiểu vì sao nó đáng chú ý
- `2`: rõ `what happened`, `what changed`, `why it matters`

#### E. Editorial fit / restraint

- `0`: title overclaim, body filler, câu view
- `1`: hơi generic nhưng vẫn chấp nhận được
- `2`: title-body khớp, tone kỷ luật, không thổi phồng

### 3. Ngưỡng quyết định

- `0-4`: `Delete`
- `5-6`: `Improve mạnh`
- `7-8`: `Keep nếu cần`, hoặc `Improve nhẹ`
- `9-10`: `Keep`

### 4. Checklist QC từng bài

Trước khi pass bài `news`, phải trả lời được:

- claim chính là gì
- source gốc là gì
- số liệu tính tới ngày nào
- bài này thêm gì ngoài bài rewrite
- vì sao reader nên quan tâm
- nếu bỏ bài này đi, người đọc có mất thông tin giá trị gì không

Nếu trả lời yếu từ `2` câu trở lên, bài chưa đạt.

### 5. Khi nào nên xóa luôn

- tin đã cũ, không còn giá trị lưu trữ
- không traffic, không backlink, không topical value
- rewrite mỏng, không có original value
- bài rất ngắn chỉ để phủ topic
- có nhiều bài cùng một sự kiện và đây là bản yếu nhất

### 6. Khi nào nên giữ và sửa

- topic vẫn tốt
- URL vẫn hợp intent
- có tín hiệu như impressions hoặc backlinks
- source thực ra mạnh nhưng bài viết chưa tới
- chỉ cần thêm date, source, delta, context là cứu được

### 7. Mẫu cấu trúc bài news đạt chuẩn

Bài `news` tốt thường có:

- đoạn 1: fact chính + source + date
- đoạn 2: con số hoặc thay đổi chính
- đoạn 3: vì sao quan trọng
- đoạn 4: context ngắn hoặc correction cho chỗ dễ hiểu sai

### 8. Rule ngắn gọn để nhớ

`No source + no date + no added value = fail`
