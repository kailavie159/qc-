## Coincu Handoff: Cleanup `?noamp=mobile`

Ngày: 2026-05-15

### Kết luận ngắn

`?noamp=mobile` đang làm phình thêm tập URL discoverable.

Đã test live và thấy:

- một số rule chỉ bỏ được prefix như `/news/` hoặc `/analysis/`
- nhưng vẫn giữ lại query `?noamp=mobile`
- riêng một số URL còn bị self-loop `301 -> chính nó`

Vì vậy, phần bỏ query `?noamp=mobile` **không nên xử tiếp bằng Rank Math**.

### Cách xử lý đúng

Xử ở layer server/code:

- nếu URL có `?noamp=mobile`
- thì `301` về đúng clean URL không query

Ví dụ:

- `/sec-delays-solana-etf-decision/?noamp=mobile` -> `/sec-delays-solana-etf-decision/`
- `/news/sec-delays-solana-etf-decision/?noamp=mobile` -> `/sec-delays-solana-etf-decision/`
- `/analysis/bnb-smashes-905-ath/?noamp=mobile` -> `/bnb-smashes-905-ath/`

### Việc cần làm

1. Remove các rule Rank Math vừa tạo cho nhóm `?noamp=mobile`
2. Thêm rule ở server/code để drop query `noamp=mobile`
3. Đảm bảo redirect đích cuối không còn query
4. Không để internal links hoặc module tiếp tục sinh `?noamp=mobile`

### Kết quả kỳ vọng

- URL có `?noamp=mobile` không còn được giữ lại sau redirect
- không còn loop
- giảm thêm URL variants trong nhóm `Crawled - currently not indexed`
