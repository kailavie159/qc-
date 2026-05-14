## Coincu Root Cause And Next Steps - 2026-05-14

Giờ cần làm 2 việc song song: **xác định nguyên nhân gốc** và **chốt hướng xử lý**.

### 1. Xác định nguyên nhân gốc

Mục tiêu là trả lời 3 câu:
- file có còn trên disk không
- nếu còn, quyền có sai không
- nếu file và quyền đều ổn, nginx/origin có đang chặn không

Checklist ngắn:

1. check file mẫu trong vùng chết:

```bash
ls -lah wp-content/uploads/2022/07/111-1*
ls -lah wp-content/uploads/2022/08/image-459*
ls -lah wp-content/uploads/2022/11/image-1066*
ls -lah wp-content/uploads/2022/12/Ban-sao-cua-BB-21-5*
```

2. check file đối chứng đang sống:

```bash
ls -lah wp-content/uploads/2022/01/image-37*
```

3. check quyền thư mục:

```bash
ls -ld wp-content/uploads/2022/01 wp-content/uploads/2022/07 wp-content/uploads/2022/08 wp-content/uploads/2022/11 wp-content/uploads/2022/12
```

4. nếu file tồn tại, check owner/mode:

```bash
stat wp-content/uploads/2022/01/image-37.png wp-content/uploads/2022/11/image-1066.png
```

### 2. Đọc kết quả để chốt nguyên nhân

- Nếu file `2022/07` đến `2022/12` không tồn tại:
  - nguyên nhân chính = **media legacy bị mất file**
- Nếu file tồn tại nhưng mode/owner sai:
  - nguyên nhân chính = **permission/ownership**
- Nếu file tồn tại, quyền giống file sống, nhưng web vẫn `403`:
  - nguyên nhân chính = **origin/nginx rule hoặc storage mapping**

### 3. Hướng xử lý theo từng nguyên nhân

- **File mất**
  - bài stale/date-bound: xóa bài
  - bài đáng giữ: thay ảnh mới hoặc re-upload ảnh cũ
  - không cố sửa rule nếu file gốc không còn

- **Permission lỗi**
  - sửa quyền thư mục/file cho cụm `2022/07` đến `2022/12`
  - test lại vài URL mẫu

- **nginx/origin rule lỗi**
  - tìm rule deny/try_files/path issue cho legacy uploads
  - ưu tiên so với `2022/01` đang sống để thấy khác biệt

### 4. Song song xử lý content

- `delete_now` batch: xóa trước
- `fix_keep`: bài có value thì sửa ảnh/reference
- các bài stale không signal: tiếp tục đẩy sang delete

### 5. Thứ tự nên làm ngay

1. xác minh file thật trên disk
2. xác minh permission
3. nếu file có đủ mà vẫn lỗi, mở nginx/origin config
4. sau đó mới quyết định:
   - `restore media`
   - `replace image`
   - `delete post`

Nói ngắn:
- bước quyết định bây giờ là **check file tồn tại + permission**
- chỉ sau bước đó mới chốt được nguyên nhân gốc thật sự
