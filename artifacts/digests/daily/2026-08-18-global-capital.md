---
lens: global-capital
date: 2026-08-18
status: building
window_start: 2026-08-18T05:00:00-04:00
as_of: 2026-08-18T15:15:00-04:00
coverage: pending
---

# Global Capital — 2026-08-18

*Curated agentic-interim, 05:00 ET through ~15:15 ET, extended through
the afternoon — still not a close (markets close 16:00 ET), so every
market level below carries its own as-of timestamp. Sources: today's full
collector run (18 sources, including `fred`, `sec_edgar` and
`treasury_tic`) plus live timestamped quotes (stockanalysis.com,
tradingeconomics.com) and direct primary-source verification of NVIDIA's
13F. The fresh 15:03 ET collector pass added little of its own — of 886
items only 13 were `global-capital`-tagged and none were market-moving;
this window's real update came from live verification.*

## Today's throughline

**The long end kept going and the market finally charged the AI complex
for it.** Monday's story was a bond market absorbing record supply while
crude sat still — a fiscal repricing that equities mostly shrugged at.
This morning the 30-year added two more basis points to **5.32%**, oil
went above $85, and the highest-duration equities in the index broke
together: **Nvidia −2.29%, AMD −5.2%, Micron −5.4%**, with Micron handing
back the $1,000 it crossed on Monday inside a single session. Nothing
company-specific happened to any of the three. That is the point — this
is the rate channel arriving in the AI trade, which is the mechanism
`ai-buildout-debt-risk` exists to watch and the first session where it is
legible without an accompanying story. **By the afternoon the story split
in two.** Yields eased slightly rather than extending further, but
memory/storage names kept falling hard — Micron −7.56%, Western Digital
−7.27%, SanDisk −9.80% — while Nvidia and AMD sat flat to their morning
levels. The co-movement that made the morning legible as a rate story
doesn't explain the afternoon; this reads more like `ai-memory-shortage`
reasserting itself (Xiaomi's margin hit below is the same shortage from
the demand side) than more duration repricing. Private AI-chip financing
didn't get the memo either way: Etched quadrupled its valuation to $21B
in seven weeks on the same day.

## Capital in my markets

- **The 30-year Treasury extended its 19-year high to 5.32% and semis
  broke together.** Live quotes at **10:09 ET**: **NVIDIA −2.29% at
  $219.79** (prior close $225.01) · **AMD −5.2% at $479.90** (prior close
  $506.00) · **Micron −5.4% at $957.00** (prior close $1,011.75).
  Nasdaq −1.2%, S&P 500 −0.46% at 7,709.14, Dow −0.3%. **The
  all-together-ness is the evidence**: an idiosyncratic story moves one
  name, a duration repricing moves all three, and this map has been
  burned twice this week by aggregators attaching a company narrative to
  a rate move. ⚠️ A Jefferies note recirculating this morning on AMD's
  Helios/ROCm taking Nvidia share is **UNVERIFIED and excluded** — the
  AMD event it describes was 07-22/23, its price targets conflict across
  sources, and AMD fell *harder* than Nvidia, which is the opposite of
  what that thesis predicts.
  ([Yahoo Finance live](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-august-18-dow-sp-500-nasdaq-080822735.html),
  [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-18-2026))
  <!-- k: t=ai-buildout-debt-risk,chip-hyperscaler-rotation e=nvidia,amd,micron axis=capital-in-my-markets sev=major interp=yes -->

- **By mid-afternoon the selloff had narrowed to memory/storage rather
  than staying broad across the three original names, and it deepened
  sharply there.** ~3:10 PM ET reads: **Micron −7.56% at $935.27**
  (from −5.4% at 10:09 ET) · **Western Digital −7.27% at $497.02** ·
  **SanDisk −9.80% at $1,611.81** — the whole memory/storage complex, not
  one name. Nvidia and AMD barely moved from their morning levels (NVDA
  −2.28%, AMD −5.09%, both flat to 10:09 ET). ⚠️ **The rate story that
  explained the morning's co-movement did not get worse into the
  afternoon** — 10-year at 4.71%, 30-year at 5.29% (tradingeconomics.com),
  both a hair *below* the 10:45 ET reads — so memory's continued fall
  while yields eased is a decoupling from this morning's throughline, not
  a clean extension of it. Worth holding as its own thing: this looks
  more like the memory-shortage/margin story `ai-memory-shortage` already
  tracks (see Xiaomi below) reasserting itself than more duration
  repricing.
  ([stockanalysis.com](https://stockanalysis.com/stocks/mu/))
  <!-- k: t=ai-memory-shortage e=micron axis=capital-in-my-markets -->

- **Asia and Europe both sold off overnight, and Europe is now on its
  sixth consecutive down session.** The **Nikkei 225 closed −1.62% at
  68,098.54** (−1,121.71 points), led down by paper and pulp, transport
  and communications. The **Hang Seng closed −0.6% at 25,852.92**, with
  the China Enterprises index −0.9% at 8,574.26 and, notably, **Hang Seng
  Tech +0.21%** — the one green print in the overnight. The **Stoxx
  Europe 600 was down ~0.2%** intraday, its **sixth straight loss** and
  its lowest since 08-03.
  <!-- k: t=ai-trade-bear-turn axis=capital-in-my-markets -->

- **ByteDance drew more than $30 billion of orders for a jumbo bank
  loan** — an order book that size, in a week when investors pulled 36%
  of their initial orders on US investment-grade issuance after pricing
  was squeezed, is a useful contrast: the demand is not gone, it is
  discriminating.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-18/bytedance-draws-over-30-billion-in-orders-for-jumbo-bank-loan))
  <!-- k: t=ai-buildout-debt-risk e=bytedance axis=capital-in-my-markets interp=yes -->

- **Xiaomi's profit fell on a worsening memory-chip crunch hitting
  smartphone demand** — the demand-destruction end of the memory shortage
  this map tracks from the supply side via `ai-memory-shortage`. Micron
  crossing $1,000 and Xiaomi's margin compression are the same shortage
  seen from opposite sides of the transaction.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-18/xiaomi-profit-dives-as-memory-crunch-hits-smartphone-demand))
  <!-- k: t=ai-memory-shortage e=micron axis=capital-in-my-markets interp=yes -->

## Deals & filings

- **Ant Group sold a 3% stake in Paytm for $309 million.**
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-18/ant-group-sells-3-paytm-stake-in-309-million-deal))
  <!-- k: axis=deals-and-filings -->

- **Baidu posted a fifth consecutive quarterly revenue decline**, with
  the AI gap against domestic rivals cited as the widening cause.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-18/baidu-posts-fifth-straight-revenue-drop-as-ai-lag-widens))
  <!-- k: t=china-stack-independence axis=deals-and-filings -->

- **Etched's valuation quadrupled in seven weeks: a $700M round at $21B,
  led by Jane Street, the same day public memory/semis names took their
  worst hit of the week.** Path: $5B (Dec-25) → $10.3B Series C (Jul-26)
  → $21B (today). Etched builds AI-inference-specific hardware — a
  low-voltage "prefill" chip plus shared cluster-scale memory — pitched
  against Nvidia on cost/speed for inference rather than training. Other
  investors: Kleiner Perkins, Sequoia, a16z, Peter Thiel, Tiger Global,
  Blackstone. Jane Street is already a watchlist entity (added 08-14 for
  its CoreWeave role); Etched has no entity slug on this map yet. Worth
  holding against the memory selloff above: private AI-chip financing
  didn't blink on the same day public AI-adjacent names had their worst
  session of the week.
  ([TechCrunch](https://techcrunch.com/2026/08/18/etcheds-valuation-doubles-to-21b-in-a-month/))
  <!-- k: t=ai-buildout-debt-risk e=jane-street axis=deals-and-filings -->

- **No new SEC filing of consequence in-window.** Today's `sec_edgar`
  pull is 479 filings and its shape is the 08-14 13F deadline's wake —
  135 N-PX, 95 13F-HR, 14 13F-HR/A, 62 424B2 — with 19 8-Ks, none from
  the capex or frontier-lab complex. NVIDIA's most recent 8-K remains
  the 08-17 Ohio guarantee (accession 0001045810-26-000069). **No public
  Anthropic S-1 or S-1/A has appeared** — the June 1 submission remains
  confidential, which matters because the fall IPO timeline now has a
  $65B run-rate attached to it and no public document.
  <!-- k: t=frontier-lab-ipos,anthropic-ipo-timing e=anthropic axis=deals-and-filings -->

## 📊 Macro strip

*All intraday unless marked; ~10:00–10:45 ET morning reads, with a
~3:10 PM ET afternoon update on yields and the index levels below. Market
close (16:00 ET) had not happened as of this pass — a close-vs-intraday
delta should be re-pulled on the next run rather than assumed from these
reads.*

- **30-year Treasury: 5.32%** morning → **5.29%** ~3:10 PM ET
  (tradingeconomics.com) — a slight afternoon ease rather than a further
  extension; ⚠️ unverified against a primary source, so treat as directional
  not exact. Still a third consecutive session at/near 19-year highs.
- **10-year: 4.72–4.73%** morning → **4.71%** afternoon — flat to
  slightly eased, same caveat as above.
- **2-year: 4.18%** (08-18) — flat on Monday's ~4.17%. The steepener
  holds.
- **S&P 500: 7,709.14 (−0.46%)** at 10:45 ET → **7,696.64 (−0.63%)**
  ~3:10 PM ET — deepened. **Nasdaq** −1.2% → **−1.33%** (26,290.51) —
  deepened. **Dow** −0.3% → **−0.15%** (53,380.49) — **recovered**, less
  negative than the morning read.
- **10Y–2Y spread: 0.53** (FRED `T10Y2Y`, 08-17) — the bear steepener
  with a number on it, from this map's own collector.
- **VIX: 15.19** (FRED `VIXCLS`, 08-17 close) — **+6.6%** on Friday's
  14.25. ✅ **Retires the stale-VIX flag** carried since 08-14;
  independently confirmed by this map's FRED collector and a vendor's
  4:36pm ET snapshot, which agree exactly.
- **Brent: $90.97/bbl** (08-18, +0.11%) · **WTI ~$84–85** — crude has now
  moved *up* through $85 after sitting still through Monday's escalation,
  which is the change from yesterday's reading.
- **Gold: ~$4,429/oz** (08-18) — holding above $4,400 for a second
  session on fading Fed-hike odds.
- **DXY: ~99.40** (08-18) — lowest since June 2026, weakening a third
  straight session.
- **US equities:** S&P 500 7,709.14 (−0.46%) · Nasdaq −1.2% · Dow −0.3%
  (all 10:09 ET).

⚠️ **One number deliberately not carried:** "Eurozone 10-year yields above
3.2%, a 15-year high," cited in coverage as the driver of the Stoxx
decline, traces only to a search-engine summary rather than a fetched
primary article. It is plausible and it is not in this strip until it is
sourced.

## 🕰 Caught late — NVIDIA's 13F, filed 08-14, read today

**Nvidia's disclosed public-equity book is $63.4 billion, and this map
had no figure for it at all.** The 13F-HR was filed **2026-08-14 at
16:19:53 ET**, period ending 06-30. Full treatment, table and all, is in
the 08-17 finalize; the three points that change the reading, restated
because they invert the obvious headline:

- **Only about $26B of the quarter's $50B growth is buying.** The rest is
  mark-to-market. **Intel's share count is identical across both quarters
  — 214,776,632** — so its $7.93B → $29.99B move involved no purchase at
  all. Any account describing "Nvidia's Intel stake growing" is describing
  Intel's share price.
- **SpaceX at $20.98B is the second-largest position and was entirely
  absent from this map's stake ladder** — 122,764,805 shares, an implied
  ~$170.86 at 06-30, against a $135 IPO price and a stock that traded
  below issue in early August before recovering. The mark has since been
  given back.
- **CoreWeave is the one position Nvidia actually added to** — 24.3M to
  47.2M shares, **+94%** — and it is the smallest headline in the filing.

⚠️ Secondary reporting puts Intel at ~$22B after Intel's own 08-12
offering diluted it; that is reported, not filed, and this map carries the
06-30 filing figure as primary. **Naver does not appear in the 13F** — a
13F covers 13(f) securities only, so the ladder's prose and the filing's
holdings are overlapping sets, not the same set. Absence is not disposal.

## ⏳ Upcoming & expected

**One hit.** `ping-an-h1-2026-interim-results` (due 08-18) → **HIT**, on
its due date, and the disclosure this entry was explicitly holding for
exists. Ping An Good Doctor (1833.HK) reported H1 2026: revenue **RMB
2.484bn**, net profit attributable **RMB 219mn (+63.5% YoY)**, adjusted
net profit RMB 227mn (+37.7%), B-end corporate health-management revenue
**RMB 714mn (+65.1%)** and now 28.7% of total. **AI contributed ~4.6% of
gross profit** — a rare hard number for AI's P&L contribution rather than
a narrative — alongside 9.7M+ cumulative AI-doctor users and AI-medical-pay
coverage at 149,000 of 245,000 partner pharmacies.
⚠️ **Trap logged, and it is a nasty one:** English-language wire mirrors
(PRNewswire, Barchart) served **2026-dated URLs and headlines** whose body
was the **August 19 2025** H1-2025 release, prior-year numbers and all
(RMB2.5bn revenue / RMB134mn profit, dateline "HONG KONG, Aug. 19,
2025"). The genuine 2026 figures were reachable only through primary
Chinese-language financial press.

**New entry logged.** `ping-an-group-h1-2026-interim-results` (due
**08-20**) — the parent (HK:2318 / SH:601318) reports separately, now
pinned by the company's own voluntary HKEX/SSE announcement filed 08-13.
This closes a gap the subsidiary entry had carried since 08-04, when the
group-level date could not be independently confirmed. Watch for a
group-level AI-contribution figure to set beside the subsidiary's 4.6%.

**Nearest pending:** `iran-oman-hormuz-deal-signing` (**08-19**, in
drafting, not signed — see the world-news digest),
`xai-mn-preliminary-injunction` (**08-19**, confirmed on),
`apple-cxmt-senate-deadline` (08-21).

## 🔄 Map changes

**A standing watch item is ready for a decision rather than a seventh
flag.** The FT Unhedged yen/BOJ theme was logged 08-14 as five runs in
two weeks and 08-17 as a sixth, with the promotion bar set at "a
discrete, named, live mechanism rather than analyst commentary on
direction." Monday's **"Broken FIMA"** — arguing Treasury Secretary
Bessent's push to expand the Fed's FIMA repo facility as a yen-defence
backstop is structurally weak — names the facility, the official and the
policy ask. **It clears the bar.** Promote it to a thread or drop it on
the next `/week`; do not flag it a seventh time.

**`meta-capex`'s capex basis is corrected** — the $76B TTM figure this map
carried is retired in favour of Meta's own guidance, **$130–145B for
FY2026**, per exhibit 99.1 to its 07-29 8-K. The thread's watch field had
flagged this for resolution "at earnings 07-29"; earnings happened and
the flag sat for three weeks until the cold rotation found it. New and
larger: reporting dated 08-17 puts Meta's **off-balance-sheet AI
obligations at ~$420B** against $83.7B of reported on-balance-sheet debt,
with five hyperscalers together at a cited **~$1.65T**.

## 🧵 Thread candidates

- **NEW — off-balance-sheet AI obligations as a disclosed-versus-real
  gap.** Meta reports $83.7B of debt and carries a reported ~$420B of
  lease, chip-purchase and cloud commitments outside it; the five-company
  aggregate is put at ~$1.65T; EY flagged Meta's Beignet structure as a
  critical audit matter in February. This map has `ai-buildout-debt-risk`
  for the credit-market channel and `where-the-capex-lands` for the
  physical destination, but nothing on the **accounting boundary** — which
  is where a credit event would actually surface first. Track it?
  (curator-noticed)
- **Dropping without a third offer:** payments/fintech rolling up the AI
  model-access layer. ⚠️ Noted rather than dropped silently, because the
  underlying event — **Stripe/OpenRouter, >$7B** — went uncovered as news
  on both 08-16 and 08-17 while sitting in the candidate slot. **A
  candidate is not coverage**, and this map made one decision where it
  needed two.

---
The 30-year went to 5.32% and the AI complex finally paid for it —
Nvidia, AMD and Micron down together, Micron surrendering its $1,000
milestone in a single session, with no company-specific news behind any
of it. By the afternoon the story split: yields eased slightly while
Micron, Western Digital and SanDisk kept falling hard, a memory-specific
move rather than more rate repricing, even as Etched quadrupled its
valuation to $21B in seven weeks in the private market the same day. Asia
and Europe sold off overnight and Europe is on its sixth straight down
day, while ByteDance pulled more than $30bn of orders for a jumbo loan,
which is what discriminating rather than absent demand looks like.
Nvidia's 13F, filed four days ago and read today, shows a $63.4bn equity
book — but Intel's share count did not move at all, so half the growth is
price, and the only position Nvidia genuinely doubled down on was
CoreWeave. Ping An put a number on AI's contribution to gross profit:
4.6%.
