---
lens: global-capital
date: 2026-08-06
status: building
window_start: 2026-08-06T05:00:00-04:00
as_of: 2026-08-06T09:30:00-04:00
coverage: pending
---

# Global Capital — 2026-08-06

*Curated from a tier-2 hot-cluster deep sweep (agentic-interim; sources:
Investing.com, Daily Sabah, Bloomberg, Oilprice.com, Fortune, CBS News,
buffer/collect.py's google_news_rss + sec_edgar + fred pulls, direct
outlet fetches). Session WebSearch budget was shared across this run's
many concurrent agents and exhausted early; verification leaned on
WebFetch against primaries.*

## Today's throughline

The two ledger items this map had been counting down to both landed
today, and both resolved with more nuance than the headline number.
SoftBank's Q1 print showed net income down 18% YoY even as the
previously-stalled $10B OpenAI-collateral loan finally got signed — Arm's
own post-earnings slide is now visible directly on SoftBank's balance
sheet as a real, quantified NAV cut. SpaceX's insider lockup opened on
schedule, but the more consequential tranche stays locked because the
stock hasn't recovered to the price that would free it — a "ceiling on
what could sell," not evidence anyone actually has. Underneath both:
Brent whipsawed back up into the low-$80s on a still-unsigned Hormuz
deal, and this map's own coverage-critic catch from yesterday's finalize
— SpaceX's actual debut earnings, and the broader Microsoft/Meta-driven
tech rally — is worth re-reading alongside today's follow-through.

## Capital in my markets

- **SoftBank's Q1 FY26 print resolves both halves of yesterday's ledger
  entry, and the mechanism is now visible in the numbers.** Net income
  ¥347.3B, down 18% YoY, despite investment gains surging ~300% YoY to
  ¥1.86T — almost entirely ByteDance and Intel, not OpenAI, which booked
  no valuation gain this quarter. Shares fell 4.41% on the print,
  reversing yesterday's pre-print rally. **Arm's own post-earnings slide
  now shows up directly on SoftBank's balance sheet:** quarter-end NAV
  hit a record ¥72.3T, but a same-release pro-forma mark as of 08-05
  shows NAV down to ¥58.3T — a ¥14T (~19%) cut, driven specifically by
  Arm's own NAV contribution falling from ¥43.4T to ¥31.1T. **The
  previously-stalled $10B OpenAI-stake margin loan is now signed**
  (Goldman/JPMorgan/Mizuho/Apollo/SMBC, agreed 08-05, drawdown this
  month) — SoftBank's total OpenAI-linked commitments now exceed $60B.
  CFO Goto, pushing back on bubble framing: "There's clear demand and an
  overwhelming shortage of supply... I think we're in a very healthy
  state."
  ([Investing.com](https://in.investing.com/news/company-news/softbank-q1-fy2026-slides-record-nav-amid-massive-ai-bets-93CH-5538941), [Daily Sabah](https://www.dailysabah.com/business/tech/softbanks-q1-profit-falls-18-as-tech-investor-gains-on-intel-stake), [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-06/softbank-secures-10-billion-margin-loan-backed-by-openai-stake))
  <!-- k: t=softbank-all-in e=softbank,arm axis=capital-in-my-markets sev=major -->
- **SpaceX's insider lockup opens on schedule, but the bigger, more
  consequential tranche stays locked.** Up to 911.5M shares (~$101-116B)
  became eligible for sale today — the second trading day after the 08-04
  earnings print, as SpaceX's staggered nine-tranche unlock design
  intended. No confirmed evidence of actual selling turned up (no Form
  4s). A separate, larger 455.8M-share tranche stays fully locked because
  its release requires the stock above the $135 IPO price — SPCX closed
  $108.27 the day before, ~20% under issue. The headline eligible figure
  is a ceiling on what could sell, not evidence anyone has.
  ([Yahoo Finance/AP](https://finance.yahoo.com/markets/stocks/articles/spacex-insider-lockup-expires-freeing-115102691.html), [Motley Fool](https://www.fool.com/investing/2026/08/05/spacexs-lockup-expires-on-aug-6-heres-why-9115-mil/))
  <!-- k: t=spacexai-public-megacap e=spacex axis=capital-in-my-markets -->
- **Brent rebounds into the low-$80s as the Hormuz deal stays unsigned.**
  Readings cluster $80.80–83.64, up from the ~$78.4-78.7 close logged
  08-05, even as Iran's "agreed in principle" framing (world-news, below)
  stays short of a signed deal. Same anticipation trade wobbling in the
  other direction — nothing here confirms which way it ultimately
  breaks.
  ([Oilprice.com](https://oilprice.com/futures/brent/), [Fortune](https://fortune.com/article/price-of-oil-08-06-2026/))
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->

## Deals & filings

- **Two capital-markets infrastructure deals surfaced today, distinct
  from every AI-financing thread already tracked.** Intercontinental
  Exchange (ICE, NYSE's parent) agreed to acquire MarketAxess — the
  dominant electronic corporate-bond trading platform — for $167/share
  all-cash (~$5.7-6B, reported figures vary by equity-vs-enterprise
  value); MarketAxess stock surged ~29% on the news. Confirmed across
  multiple independent outlets (Reuters, Finextra, Yahoo Finance, Seeking
  Alpha), not a single-aggregator artifact. Separately, BlackRock is
  expanding tokenized money-market fund access into Europe, enabling
  24-hour settlement in pound/euro/dollar — a different mechanism from
  BlackRock's existing AI-infrastructure debt/equity coverage on this
  map, worth its own tag rather than folding into that thread.
  ([Reuters via aggregation](https://news.google.com/rss/search?q=ICE+MarketAxess+acquisition), [Finextra](https://www.finextra.com/pressarticle/ice-agrees-5-7-billion-marketaxess-acquisition), [fintech.global on BlackRock tokenization](https://news.google.com/rss/search?q=BlackRock+tokenized+money+market+Europe))
  <!-- k: e=blackrock axis=deals-and-filings -->

## 📊 Macro strip

- **Brent crude: $80.80–83.64/bbl**, rebounding off yesterday's ~7%
  two-session slide (see Capital in my markets above).
- No new FRED reading beyond yesterday's 10Y-2Y spread (0.45, 08-05),
  still feeding the standing `rate_regime` context.

## ⏳ Upcoming & expected

- ✅ **`softbank-q1-earnings` — hit.** See Capital in my markets above.
- ✅ **`spacex-insider-unlock` — hit** (mechanism confirmed; sale wave
  itself not yet evidenced). See Capital in my markets above.
- Next 7 days: `coreweave-q2-earnings` 08-11 · `iran-oman-hormuz-deal-
  signing` ~08-12.

## 🔄 Map changes

- `~ threads/softbank-all-in` — `last_seen` → 08-06, Q1 print logged.
- `~ threads/spacexai-public-megacap` — `last_seen` → 08-06, lockup
  opening logged.
- `~ threads/red-sea-oil-shock` — `last_seen` → 08-06, Brent rebound
  logged.
- `~ threads/ai-circular-financing-risk`, `nvidia-vendor-financing`,
  `coreweave-backlog-bet`, `oracle-stargate-bet` — ambient `last_seen`
  bump only, no real development.
- `~ upcoming/spacex-insider-unlock`, `~ upcoming/softbank-q1-earnings` —
  both flipped to `hit`.

## 🧵 Thread candidates

None occupying today's daily-slot count — the ICE/MarketAxess and
BlackRock-tokenization items above are real and now confirmed, but held
back from the 1-3 offered slots (used instead by the frontier-ai lens's
two stronger candidates); worth a `/steer` or a future daily's slot if
either keeps developing.

---
SoftBank's Q1 print resolved both halves of a ledger entry at once —
profit down 18%, but the stalled $10B OpenAI loan finally signed and
Arm's slide now visible as a real ¥14 trillion NAV cut. SpaceX's lockup
opened on schedule but the bigger tranche stays locked until the stock
recovers, and oil whipsawed back up on a Hormuz deal that's still just
"agreed in principle."
