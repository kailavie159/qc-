## Coincu Media Recovery Checklist

Date: 2026-05-15

Purpose:
- Track live recovery of the legacy media failure cluster
- Focus on the highest-risk folders: `wp-content/uploads/2022/08` to `2022/12`

### Current Read

- Recovery has started, but it is still partial
- `2022/07` sample recovery is mixed
- `2022/08` to `2022/12` still look broadly broken in live sampling

Sample status from live checks:

- `2022/07`: `2/3` sample images returned `200`, `1/3` returned `403`
- `2022/08`: `0/3` sample images returned `200`
- `2022/09`: `0/3` sample images returned `200`
- `2022/10`: `0/3` sample images returned `200`
- `2022/11`: `0/3` sample images returned `200`
- `2022/12`: `0/3` sample images returned `200`

### Pass Condition

- `coincu.com/wp-content/uploads/...` image URLs return `200` with an image content type
- `news.coincu.com/wp-content/uploads/...` legacy URLs, if still hit, should `301` to the new `coincu.com` image URL and the final destination should return `200`

### Priority Sample URLs To Recheck

#### 2022/08

- `https://coincu.com/wp-content/uploads/2022/08/og_image-1024x538.png`
- `https://coincu.com/wp-content/uploads/2022/08/image-978.png`
- `https://coincu.com/wp-content/uploads/2022/08/Binance-CEO-Meets-With-Ivorian-President-To-Discuss-Crypto.jpeg`

#### 2022/09

- `https://coincu.com/wp-content/uploads/2022/09/A%CC%89nh-chu%CC%A3p-Ma%CC%80n-hi%CC%80nh-2022-09-22-lu%CC%81c-07.57.04.png`
- `https://coincu.com/wp-content/uploads/2022/09/image-1683.png`
- `https://coincu.com/wp-content/uploads/2022/09/image-1794-1024x576.png`

#### 2022/10

- `https://coincu.com/wp-content/uploads/2022/10/Screen-Shot-2022-10-05-at-11.56.50-PM.png`
- `https://coincu.com/wp-content/uploads/2022/10/image-475.png`
- `https://coincu.com/wp-content/uploads/2022/10/image-476.png`

#### 2022/11

- `https://coincu.com/wp-content/uploads/2022/11/image-2126.png`
- `https://coincu.com/wp-content/uploads/2022/11/image-2127.png`
- `https://coincu.com/wp-content/uploads/2022/11/image-32-1024x500.png`

#### 2022/12

- `https://coincu.com/wp-content/uploads/2022/12/image-2316.png`
- `https://coincu.com/wp-content/uploads/2022/12/image-2318.png`
- `https://coincu.com/wp-content/uploads/2022/12/image-2320.png`

### Practical Next Step

- Wait for dev to finish the current media restore pass
- Recheck the sample URLs above first
- Only after those start returning `200` should we re-evaluate the broader image-indexing problem
