## Coincu QC Rule: Evergreen

Ngày: `2026-05-26`

### Mục tiêu

Chỉ giữ bài `evergreen` nếu nó là tài sản search lâu dài:

- intent rõ
- utility thật
- depth thật
- không phải filler dài

### 1. Fail cứng

Nếu dính `1` trong các lỗi dưới đây thì fail ngay:

- intent không rõ hoặc không ổn định theo thời gian
- nội dung mỏng, chủ yếu kéo dài bằng filler
- không có utility thật: không có framework, steps, examples, comparison
- chỉ định nghĩa lại thứ đã có sẵn khắp nơi
- title hứa nhiều nhưng body không giải quyết được
- topic không evergreen thật mà đang đóng vai evergreen
- YMYL nhưng trust yếu, source yếu, expertise yếu

### 2. Cách chấm điểm

Chấm `5` mục, mỗi mục từ `0` đến `2`.

Tổng điểm tối đa: `10`

#### A. Intent stability

- `0`: topic mơ hồ, lệch intent, không bền
- `1`: topic ổn nhưng chưa đóng đúng intent
- `2`: intent rõ và xứng đáng giữ lâu dài

#### B. Unique utility

- `0`: không có gì hơn top results phổ biến
- `1`: có ích nhưng còn generic
- `2`: có framework, checklist, examples, comparison, use cases rõ

#### C. Depth / completeness

- `0`: đọc xong vẫn phải search tiếp
- `1`: đủ mức cơ bản
- `2`: trả lời trọn intent, có edge cases hoặc pitfalls

#### D. Trust / expertise / experience fit

- `0`: claim yếu, expertise không rõ
- `1`: tạm ổn
- `2`: nguồn hợp lý, reasoning vững, thể hiện hiểu vấn đề

#### E. Structure / readability

- `0`: heading rỗng, flow rối, khó scan
- `1`: đọc được nhưng chưa sắc
- `2`: cấu trúc gọn, dễ scan, mỗi section có nhiệm vụ rõ

### 3. Ngưỡng quyết định

- `0-4`: `Delete`
- `5-6`: `Merge` hoặc `Improve mạnh`
- `7-8`: `Keep nếu strategic`, hoặc `Improve nhẹ`
- `9-10`: `Keep`

### 4. Checklist QC từng bài

Trước khi pass bài `evergreen`, phải trả lời được:

- user intent cụ thể là gì
- bài này giúp hơn các bài generic khác ở đâu
- có step-by-step, framework, examples, hoặc comparison không
- có source hoặc reasoning đủ trust không
- bài này còn giá trị sau `6-12` tháng không
- nếu gộp vào bài khác thì có tốt hơn không

Nếu không trả lời mạnh được ít nhất `4/6`, bài yếu.

### 5. Khi nào nên xóa luôn

- thin explainer
- keyword-led nhưng không utility-led
- cùng intent đã có bài khác mạnh hơn trên site
- không backlink, không traffic, không cluster value
- topic thực chất là news cũ kéo dài, không phải evergreen thật

### 6. Khi nào nên merge

- có `2-3` bài cùng intent nhỏ
- mỗi bài đều mỏng
- có thể gộp thành `1` bài pillar mạnh hơn

### 7. Khi nào nên giữ và nâng

- slug tốt
- intent tốt
- có cơ hội thành cluster hub
- chỉ thiếu ví dụ, source, structure, comparison

### 8. Mẫu cấu trúc bài evergreen đạt chuẩn

Bài `evergreen` tốt thường có:

- mở đầu trả lời thẳng intent
- section giải thích bản chất
- section framework hoặc steps
- section mistakes / pitfalls
- section examples hoặc comparison
- FAQ ngắn nếu thật sự cần

### 9. Rule ngắn gọn để nhớ

`No stable intent + no unique utility + no real depth = fail`
