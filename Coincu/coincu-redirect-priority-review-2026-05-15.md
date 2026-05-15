## Coincu Redirect Priority Review

Date: 2026-05-15

Scope:
- Quick triage based on the Rank Math redirect list pasted from the live site UI
- This is a priority review, not a full export-driven audit
- Goal: identify redirects that are safe to keep, redirects that need manual review, and redirects that should be removed or replaced first

### Keep

These look like normal slug consolidation or AMP normalization where source and destination intent still match.

- `/347436-12345-xrp-price-may-never-hit-10-say-analysts-as-a-new-008-payfi-token-is-already-capturing-ripple-market-share/` -> `/347436-xrp-price-may-never-hit-10-say-analysts-as-a-new-008-payfi-token-is-already-capturing-ripple-market-share/`
- `/343729-pi-coin-price-forecast-will-this-mobile-mined-penny-token-break-into-the-top-50/` -> `/343729-pi-coin-price-forecast-will-this-mobile-mined-penny-token-break-into-the-top-40/`
- `/340302-joby-stock-surges-29-after-toyotas-250m-air-taxi-investment/` -> `/340302-joby-stock-surges-nearly-30-after-toyotas-250m-air-taxi-investment/`
- `/337875-binance-alpha/` -> `/337875-what-is-binance-alpha-how-to-join-and-get-a-huge-airdrop/`
- `/338371-market-overview-may-12-may-18-bitcoin-soars-to-105k-on-heavy-accumulation-by-giants/` -> `/338371-bitcoin-soars-to-105k-on-heavy-accumulation-by-giants/`
- `/337786-short-term-price-predictions-pi-xrp-btc-16-may-2025/` -> `/337786-short-term-price-predictions-pi-xrp-btc-15-may-2025/`
- `/337654-short-term-price-prediction-5-15-eth-people-ondo/` -> `/337654-short-term-price-prediction-eth-people-ondo/`
- `/333834-sui-ecosystem-tokens/` -> `/333834-top-sui-ecosystem-tokens-to-watch-in-2025/`
- `/332434-travis-kelce-net-worth-2/` -> `/332434-travis-kelce-net-worth/`
- `/328219-ethereums-burn-rate-drops-to-record-low/` -> `/328219-ethereums-burn-rate-drops-to-historic-low/`
- `/324426-taylor-swift-net-worth-2025/` -> `/324426-taylor-swift-net-worth/`
- `/321908-chartup-launches-solana-volume-bot-to-boost-token-visibility-2/` -> `/321908-chartup-launches-solana-volume-bot-to-boost-token-visibility/`
- `/321236-arweave-computing-platform-officially-launched-after-long-testing-period/` -> `/321236-arweave-computing-platform-officially-launched/`
- `/305264-jd-vance-net-worth-rises-with-power-influence/` -> `/305264-jd-vance-net-worth/`
- `/305306-ftx-repayments-will-start-in-next-2-weeks-after-long-wait/` -> `/305306-ftx-repayments-will-start-in-next-2-weeks/`
- `/304990-400-million-xrp-unlocked-ripples-strategic-power-boost-for-future-use/` -> `/304990-400-million-xrp-unlocked-ripples-for-future-use/`
- `/304110-bitcoin-price-lost-100000-mark-again-as-fomc-approaches/` -> `/304110-bitcoin-price-lost-100000-mark-again/`
- `/market/amp/` -> `/markets/amp/`
- `/market/` -> `/markets/`
- `/302096-missed-the-snek-bonanza-btfd-coin-is-the-next-top-meme-coin-to-invest-2/` -> `/302096-missed-the-snek-bonanza-btfd-coin-is-the-next-top-meme-coin-to-invest/`
- `/299459-pudgy-penguins-review-exploring-the-coolest-nft/` -> `/299459-pudgy-penguins-update-exploring-the-coolest-nft/`
- `/295615-this-is-why-acx-token-up-150-today-december-6/` -> `/295615-why-acx-token-is-up-150-today-december-6/`
- `/294247-ton-teleport-btc-white-paper-released-mainnet-expected-to-launch-in-2025/` -> `/294247-ton-teleport-btc-white-paper-released/`
- `/293585-💥-100x-potential-unlocked-discover-this-cheap-altcoin-with-massive-bullish-momentum/` -> `/293585-100x-potential-unlocked-discover-this-cheap-altcoin-with-massive-bullish-momentum/`
- `/286170-telegram-mini-apps/` -> `/286170-telegram-mini-apps-transform-user-experience/`
- `/290648-jpmorgan-launches-instant-eur-usd-blockchain-conversion/` -> `/290648-jpmorgan-launches-instant-eur-usd-conversion/`
- `/241855-hasbulla-net-worth/amp/` -> `/241855-hasbulla-net-worth/`

### Review

These may be acceptable, but the destination should be checked against live content and intent before leaving them alone.

- `/333339-suiplay/` -> `/333339-how-suiplay0x1-differs-from-existing-gaming-handheld/`
  Reason: probably related, but the source is very broad while the destination is a narrower explanatory title.

- `/326334-world-liberty-financial-reportedly-considering-partnership-with-binance-cz-denies/` -> `/326334-world-liberty-financial-partnership-with-binance/`
  Reason: likely the same story, but the destination may soften or remove important context.

- `/312285-kentucky-bitcoin-bill-eyes-750b-crypto-market/...` -> `/312285-kentucky-bitcoin-bill-pushes-5-bn-state-fund/`
  Reason: the numbers and framing look materially different. Check whether the source was just a bad slug version or a different article.

- `/291588-bitcoin-etf-volumes-hit-6-9-billion-milestone/` -> `/291588-bitcoin-etf-volumes-hit-8-01-billion-milestone/`
  Reason: same theme, but the quantity changed. Fine if it is a corrected version of the same article, weak if not.

- `/221956-best-bitcoin-blackjack-casinos-in-2023/` -> `/221956-best-bitcoin-blackjack-casinos/`
  Reason: probably fine as evergreen cleanup, but confirm the destination is actually the updated canonical page.

### Remove Or Replace First

These are the ones to fix first because the redirect intent is clearly weak or broken.

- `/321632-best-cryptos-for-passive-income-a-deep-dive-into-qubetics-xrp-and-algorand-2/` -> `/321632-chartup-launches-solana-volume-bot-to-boost-token-visibility/`
  Why: completely different topic. This is a bad redirect and should not stay live.
  Action: remove this rule. If no true replacement exists, return `410` instead.

- `/314166-maximal-extractable-value-mev-battle-heats-up/` -> `/314166-bnb-chain-plans-to-tackle-mev-issues-after-vote/`
  Why: related ecosystem area, but still not the same article intent.
  Action: replace only if there is a true MEV-focused equivalent. Otherwise `410`.

- `/currencies/bux-buxcoin/fullChart/` -> `/`
  Why: utility/market-data path to homepage is usually a poor redirect target.
  Action: if the currency page or chart alternative still exists, point there. Otherwise consider `410`.

- `/terms-and-conditions/info@coincu.com...` -> `/`
  Why: malformed legal/contact URL should not sink to homepage.
  Action: if this came from a broken internal link, fix the source link and remove the redirect. Use `410` if the path itself is junk.

- `/vi/currencies/qbit-project-quantum/ ...` -> `/`
  Why: a currency/entity URL should not collapse to homepage unless the whole section was intentionally removed and no better replacement exists.
  Action: if there is no real replacement, prefer `410` over homepage.

- `/vi/currencies/qbit-project-quantum/` -> `/91006-viabtc-launches-event/`
  Why: completely different entity and content type.
  Action: remove this redirect. If there is no true replacement URL, use `410`.

### Operating Notes

- Do not mass-delete the current redirect set. Remove or replace only the obviously bad rules first.
- Home page redirects should be used sparingly. For junk URLs, `410` is often cleaner than forcing a weak homepage destination.
- If you can export the full Rank Math redirect list later, a full review should also check:
  - duplicate rules
  - redirect chains
  - rules matching query variants or malformed paths
  - redirects pointing to URLs that now `410` or `404`
