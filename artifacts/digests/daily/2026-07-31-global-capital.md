---
lens: global-capital
date: 2026-07-31
status: final
window_start: 2026-07-31T05:00:00-04:00
as_of: 2026-08-01T06:40:00-04:00   # extended 08-01: the 09:15 curation missed the whole session
coverage: done   # critic run 2026-08-02, two days late; appendix at foot
---

# Global Capital — 2026-07-31

*Curated from the 18-collector run (`collect.py`) plus 2 tier-2 cluster
research agents covering Grok/xAI/SpaceX/SoftBank and AI financing/
capital markets, each WebSearch/WebFetch-verified against primary
sources. FRED returned no new series values this window; no fresh macro
strip beyond what's already on file.*

## Today's throughline

A broad Tokyo AI/semiconductor rally (Nikkei 225 +4.37%) sent SoftBank to
the exchange's daily limit-up (+12-15%) and Arm +9% overnight — a
one-session snapback from Arm's own guidance-cut selloff two nights
earlier, and independent of SoftBank's own results, which turn out to be
due 08-06, not 07-30 as the ledger had it (a wrong date, corrected, not a
slip). Separately, Google became the third hyperscaler this week to
guarantee a third-party developer's bank debt rather than fund AI
buildout directly — backing Anthropic's own Texas data-center campus,
the same structure Meta/BlackRock and Nvidia/OpenAI used days earlier.
WSJ reported Tesla is weighing a sale of its China business ahead of a
possible Tesla-SpaceX merger; Musk denied it same day.

**Extended 08-01:** the session itself then closed higher — S&P +0.70%,
Nasdaq +1.00% — but the month is the number that matters. July finished
with the Nasdaq down 3.2% against a flat S&P, which is the AI complex
absorbing the month's damage almost by itself. Oil did break, and the
morning read that it "held its range" was overtaken: Iran's IRGC struck
two tankers in the Strait of Hormuz, taking Brent up about 1.1-1.2% and
turning the blockade from a threat into a strike on transiting vessels.
Two of the three FOMC hawks spent Friday publicly arguing their dissent.

## Capital in my markets — the Tokyo snapback

- **SoftBank shares hit the exchange's daily limit-up (+12-15%, to
  ~5,322 yen) and Arm rose 9% overnight**, part of a broad Tokyo
  AI/semiconductor rally (Nikkei 225 +4.37%, Advantest and Tokyo
  Electron also limit-up) triggered by strong US tech earnings —
  reversing, for one session, the "rotation away from chips" framing
  that closed out 07-29's Arm earnings coverage, and happening
  independent of SoftBank's own still-unreported results.
  ([Bloomberg Japan](https://www.bloomberg.com/jp/news/articles/2026-07-31/TJ0K57KJH6V400), [Nikkei](https://www.nikkei.com/article/DGXZQOFL3119J0R30C26A7000000/))
  <!-- k: t=softbank-all-in,arm-royalty-regime,chip-hyperscaler-rotation e=softbank,arm axis=capital-in-my-markets -->
- **SoftBank's Q1 FY26 earnings date was wrong, not slipped** —
  SoftBank's own IR page shows the briefing scheduled for **2026-08-06**
  (3:30pm JST disclosure, 4:30pm briefing); all Q1 materials still show
  placeholders. The prior 07-30 date traced to a single uncorroborated
  secondary source.
  ([SoftBank Group IR](https://group.softbank/en/event/earnings_2026q1))
  <!-- k: t=softbank-all-in e=softbank axis=capital-in-my-markets -->
- **Brent held its range, ~$90-92/bbl through this morning** — essentially
  continuing 07-30's noisy-but-elevated level, no fresh break in either
  direction; the market hasn't repriced off the new Saudi maritime
  alliance yet (see World News), consistent with how fresh that
  announcement still is.
  ([Fortune](https://fortune.com/article/price-of-oil-07-31-2026/))
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->

## Deals & financing

- **Google guarantees a $15B bank loan backing Anthropic's Texas
  data-center buildout** — a Morgan Stanley-led consortium ($14B bridge
  loan + revolving credit) lending to Nexus Data Centers for a Hubbard,
  TX campus (1.6GW dedicated gas plant, four leases for Anthropic);
  Google takes ~20% project equity for the guarantee, not yet an
  official Google/Anthropic announcement. Third instance this week of a
  hyperscaler guaranteeing a third-party developer's debt rather than
  funding buildout directly — see the interpretation below.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-30/banks-line-up-15-billion-of-debt-for-anthropic-with-google-aid))
  <!-- k: t=google-capex,ai-power-buildout,where-the-capex-lands e=google,anthropic axis=deals-and-financing interp=yes -->
- **WSJ: Tesla weighing a sale/spinoff of its China business ahead of a
  possible Tesla-SpaceX merger — Musk denies it.** Tesla executives were
  reportedly told to prepare options (spinoff/sale/closure) for
  Gigafactory Shanghai; Musk called it "fake news... never even come up
  in a discussion ever" same day, though he's separately declined to
  rule out a Tesla-SpaceX merger this month. Reported-but-denied, not
  confirmed — a new structural narrative for `spacexai-public-megacap`
  regardless of which way it resolves.
  ([Bloomberg pickup of WSJ](https://www.bloomberg.com/news/articles/2026-07-31/tesla-weighs-china-unit-sale-ahead-of-spacex-deal-wsj-says))
  <!-- k: t=spacexai-public-megacap e=tesla,spacex axis=deals-and-financing -->
- **CoreWeave and Qualcomm: nothing new on the tracked threads today** —
  checked directly; every headline in today's sweep either restates an
  already-logged 07-29/07-30 fact (the $2.6B loan's repricing to 5.5pp
  over benchmark, 96-97 cents on the dollar) or is routine
  insider-selling/analyst chatter.
  <!-- k: t=coreweave-backlog-bet,qualcomm-dragonfly e= axis=deals-and-financing -->

## The Friday close and the July month-end   <!-- added 08-01 -->

*This digest was originally curated at 09:15 ET — fifteen minutes before
the opening bell. Everything below was missing from it.*

- **US indices closed higher on Friday: S&P 500 7,489.72 (+0.70%), Nasdaq
  25,373.85 (+1.00%), Dow 52,485.03 (+0.53%)** — but the AI/semi complex
  was mixed rather than uniformly bid, and single-name earnings moved the
  tape more than chips did: Amazon +15.3% on the AWS beat, Apple -7.4% on
  weak Services and China guidance.
  ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-friday-july-31-dow-sp-500-nasdaq-081227738.html))
  <!-- k: t=chip-hyperscaler-rotation,ai-trade-bear-turn e=amazon-aws,apple axis=capital-in-my-markets -->
- **July finished with the AI trade carrying the month's damage: Nasdaq
  -3.2%, S&P 500 roughly flat at -0.1%, Dow +0.32% (a fourth straight
  monthly gain)** — a month whose mid-July chip selloff a strong Friday
  only partly repaired. The spread between a flat S&P and a -3.2% Nasdaq
  is the cleanest single number on what July actually did to the AI
  complex. Deltas computed from index levels directly, then
  cross-checked against independently stated monthly percentages.
  <!-- k: t=ai-trade-bear-turn,chip-hyperscaler-rotation e= axis=capital-in-my-markets sev=major -->
- **Micron fell 4.3-6.0% on Friday**, tied to forced-liquidation selling
  out of the Situational Awareness unwind (see 07-30) and Michael Burry
  adding to a short. ⚠ Friday closes for Nvidia, AMD and TSMC could not
  be verified — repeated searches returned only 07-28/07-29 figures for
  those names, so they are deliberately not stated here rather than
  approximated.
  ([Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60845173/why-is-micron-stock-falling-on-friday))
  <!-- k: t=ai-memory-shortage,ai-trade-bear-turn e=micron axis=capital-in-my-markets -->
- **The 10-year Treasury yield hit 4.73%, its highest since January 2025.**
  ⚠ The 30-year is the weaker number: the Fed's own H.15 series only runs
  through Thursday 07-30 at 5.21%, and the 5.28% Friday close is
  secondary-sourced only — consistent with the arithmetic but not
  primary-confirmed, so treat it as moderate confidence. The 10-year
  figure is the better-corroborated of the two.
  ([Fed H.15](https://www.federalreserve.gov/releases/h15/))
  <!-- k: t= e= axis=capital-in-my-markets -->
- **Brent closed around $88-90/bbl, up roughly 1.1-1.2%** — the move
  driven by Iran's Strait of Hormuz tanker strikes (below), not by the
  Saudi maritime coalition. ⚠ Sources spread across the range ($90.12 in
  two recaps against ~$88 in a direct fetch), so it is reported as a
  range rather than a false single print.
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->

## Deals & financing — the Friday session   <!-- added 08-01 -->

- **Iran's IRGC struck two tankers in the Strait of Hormuz on Friday
  morning**, saying it disabled vessels transiting under unauthorised
  routes with US military escort — the day's actual oil catalyst, and the
  first time the blockade has produced a direct strike on transiting
  tankers rather than a threat. Corroborated by Iran's own Tasnim agency
  and CNBC's oil desk.
  ([Washington Times](https://www.washingtontimes.com/news/2026/jul/31/irgc-says-struck-two-tankers-strait-hormuz-escorted-us-military/))
  <!-- k: t=red-sea-oil-shock,iran-conflict-widening e= axis=capital-in-my-markets -->
- **MediaTek's board approved a $5B discretionary financing budget for AI
  data-center ASICs**, disclosed on its Friday earnings call — CEO Rick
  Tsai sized the custom-AI-chip market at $80B by 2027 (up from a prior
  $70-80B range) and targeted 15-20% share, against smartphone chip
  revenue down 20% in Q2. Another entrant paying to get into the
  custom-silicon toll layer.
  ([The Star](https://www.thestar.com.my/tech/tech-news/2026/07/31/mediatek-plans-5-billion-financing-for-ai-data-center-chips))
  <!-- k: t=custom-asic-tolls,ai-compute-spend e= axis=deals-and-financing -->
- **Two of the three FOMC hawks publicly defended their dissent** —
  Cleveland's Beth Hammack and Minneapolis's Neel Kashkari each argued on
  Friday for hiking now rather than waiting, extending Tuesday's 9-3 hold
  rather than restating it. The dissenting bloc is arguing its case in
  public, which is the thing to watch before September.
  ([CNBC](https://www.cnbc.com/2026/07/31/fed-officials-who-voted-to-hike-rates-say-action-is-needed-now-against-inflation.html))
  <!-- k: t= e= axis=capital-in-my-markets -->

<!-- DAY-ASSIGNMENT NOTE ⟨08-01⟩: the Google/Anthropic $15B guarantee
     above is dated 2026-07-30 at source and belongs to digest-day 07-30,
     not 07-31. It was filed here because the 07-31 morning run swept
     overnight news and attributed it to the current day rather than
     bucketing by the 5am ET boundary. Left in place (one canonical copy,
     and the render layer dedupes by URL); recorded in 07-30's coverage
     appendix and in coverage-log.md. Same applies to Apple's Q3 print,
     carried here via Tim Cook's memory-pricing remark — it was an
     after-close 07-30 release. -->

## ⏳ Upcoming & expected

- ✅ **hit — `altman-washington-briefing`**: full detail on Frontier AI.
- 🚧 **corrected, not a flip — `softbank-q1-earnings`**: due date moves
  07-30 → 08-06 (was wrong, not a slip).
- 39 expectations on the ledger, 14 hit.

## 🔄 Map changes

- `~ upcoming/softbank-q1-earnings` — due-date corrected 07-30 → 08-06
  (⟨daily 07-31⟩).
- `~ threads/softbank-all-in`, `~ threads/arm-royalty-regime`,
  `~ threads/google-capex`, `~ threads/spacexai-public-megacap` —
  timeline blocks added (⟨daily 07-31⟩).
- `+ artifacts/digests/daily/2026-07-31-global-capital.interp.yaml` —
  first interpretation of the day, on the Google/Anthropic financing
  guarantee (mechanism: off-balance-sheet hyperscaler credit guarantees
  as a response to the elevated long-rate environment).

## 🧵 Thread candidates

- None new today — the CoreWeave/Qualcomm cluster returned nothing
  digest-worthy, and the day's one adjacent financing story (Nscale's
  $1.65B Anyscale acquisition) predates this window's cutoff and doesn't
  map to a tracked thread; not offered.

---
A Tokyo AI-chip rally opened the day with SoftBank limit-up and Arm +9%,
and the US session closed higher too — but July as a whole ended with the
Nasdaq down 3.2% against a flat S&P, the AI complex carrying the month's
losses on its own. Oil finally broke on a real event: Iran struck two
tankers in the Strait of Hormuz, lifting Brent about 1.1%. Two of the
three Fed hawks spent Friday publicly making the case for hiking now.

## Appendix — Coverage check vs. benchmarks

*Run 2026-08-02 (two days late). Benchmarks: Axios Pro Rata (issue
confirmed, partial body), FT Unhedged (headline/byline only — paywalled),
Bloomberg Technology (search-snippet only — CAPTCHA blocked full text),
Money Stuff (fully inaccessible; Bloomberg paywall plus CAPTCHA defeated
every attempt). Two of four benchmarks were therefore only partially
readable, and this appendix says so rather than implying a clean sweep.*

**They led with → we missed:**
- **Alimentation Couche-Tard agreed to buy Poland's Żabka Group for
  ~$8.7B** — Axios Pro Rata's actual lead story for the day, also carried
  by Bloomberg and Reuters. Żabka runs 13,000+ stores across Poland and
  Romania; the deal follows Seven & i walking away from its own Żabka
  talks, with SoftBank, PayPay and Sumitomo Mitsui separately agreeing to
  put ~¥100B each into Seven & i in the same window. A clean, confirmed
  miss — an $8.7B acquisition absent from deals-and-filings entirely.
  ([Axios](https://www.axios.com/2026/07/31/alimentation-couche-tard-zabka))
- **FT Unhedged ran two consecutive issues centred on the Fed chair, whom
  it names as Kevin Warsh** — "What Warsh is (probably) up to" (07-31) and
  "Warsh spooks long bonds" (08-01), on pro-volatility positioning and its
  yield-curve effects. ⚠️ **This map has never named the Fed chair
  anywhere** — not in `attention/`, not in any digest — despite carrying
  detailed FOMC dissent coverage (Hammack, Kashkari, Logan). That is a
  structural gap, not a missed story, and it is under direct verification
  as of this writing.
- **Bloomberg Technology: "Corporate America Cracks Down on AI Spending
  After Rushing to Powerful Tools"** — an enterprise AI-spending-pullback
  trend piece with no counterpart here. Moderate significance; possibly a
  benchmark analysis angle rather than a hard news miss.

**Both covered (loosely):** AI and hyperscaler capex holding up against
market scepticism — Bloomberg Tech framed it as "$2T commitments," we came
at it through the Amazon and Apple earnings moves.

**We had → they didn't:** Google's $15B loan guarantee for Anthropic's
Texas buildout (Nexus Data Centers) · Tesla weighing a China-business sale
ahead of a possible Tesla-SpaceX merger (Musk denied) · the IRGC's Hormuz
tanker strikes correctly identified as Friday's actual oil catalyst ·
MediaTek's $5B AI-ASIC financing budget · the July month-end math,
computed and cross-checked directly.

**Map adds:** none auto-applied. The Couche-Tard deal is real but is
general retail M&A, outside this lens's AI-capital focus — a process note,
not a thread. **The Fed-chair naming gap is the one genuinely structural
item** and is being resolved separately.
