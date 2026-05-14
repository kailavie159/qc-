## Coincu 403 Image Action Summary From Post Content - 2026-05-14

- Total `403` image URLs classified: `21,166`
- Published post/page rows scanned: `39,956`
- Published post/page rows containing `/wp-content/uploads/`: `35,425`
- `With source` in post content: `15,837`
- `No source` in post content: `5,329`
- `Attachment match`: `4`

### Action Counts

- `replace`: `15,837`
- `ignore_for_now`: `5,307`
- `remove`: `22`

### Priority Counts

- `P1`: `15,837`
- `P2`: `22`
- `P3`: `5,307`

### Rule Set Used

- `replace`: URL malformed in content, or content references a URL missing from attachments export
- `reupload`: content references a valid-looking image URL that exists in attachments export but returns 403
- `remove`: malformed URL with no current content source
- `ignore_for_now`: no current content source; likely legacy attachment/media-layer residue
