---
thread: intel-rescue
title: "Intel Rescue"
lens: global-capital   # corrected 2026-08-02 — was `money`, stale since the 2026-07-30 rename
entities: [intel]
opened: 2026-07-28
crawled: 2026-07-28
---

# Intel Rescue — timeline

*Watch:* The subsidized-builder paradox: capex ~$12B/yr with thrust ≈ 0
(D&A caught up), building on OUTSIDE capital — the US 9.9% golden-share
(~$8.9B, warrant triggers only if foundry ownership drops below 51%),
Nvidia's $5B (plus real x86/RTX co-design), SoftBank's $2B — through 24k
layoffs and cancelled DE/PL fabs. Track: 18A/14A execution, foundry
customer wins (Microsoft, Tesla, Apple, Fortinet so far), whether the
state stake changes behavior, Ohio's fate. Backstory crawled 2026-07-28 —
see `artifacts/findings/intel-rescue-2026-07-28.md`.

## 2026-08-28 — Intel's 14A process posts its first real yield data point — defect density "best since the 22nm process," per the CFO

- **Intel's CFO said 14A defect-density improvement is the best the company has seen since its 22nm node, and that customers have shifted from "evaluating data" to "competing for capacity"** — filling a gap the thread has flagged since it opened ("no yield % anywhere"). Corroborated across Tech Times, finance.biggo.com, and igor'sLAB (which ran the actual defect-density curve against the 22nm comparison). Stock reaction was muted-to-negative on the same day (-2.9%) alongside a reported $2.1B foundry-unit loss, so this is a real signal inside continued financial pressure, not a turnaround headline. ([finance.biggo.com](https://finance.biggo.com/), [Tech Times](https://www.techtimes.com/)) ⟨daily 2026-08-31⟩

## 2026-08-11 — The offering upsizes to $20B on 5x institutional demand

- **Intel upsized the offering logged yesterday from $15B to $20 billion,
  pricing 210.5 million shares at $95 each after institutional demand
  topped $100 billion — roughly 5x oversubscribed — with underwriters
  holding a 30-day option on another 31.6 million shares.** Net proceeds
  land near $19.7B, still earmarked for "general corporate purposes"
  including foundry capex; the offering closed 08-12.
  ([Intel Newsroom](https://newsroom.intel.com/corporate/intel-announces-upsize-and-pricing-of-20-billion-common-stock-offering), [CNBC](https://www.cnbc.com/2026/08/10/intel-intc-stock-offering-ai.html)) ⟨daily 2026-08-11⟩

## 2026-08-10 — Intel raises $15B in fresh equity for the foundry buildout

- **Intel launched a $15 billion common-stock offering to fund its
  foundry buildout**, J.P. Morgan, Goldman Sachs, Morgan Stanley, and
  Citigroup as joint bookrunners, with a 30-day underwriter option for
  another $2.25B. A private capital raise stacked on top of the
  CHIPS-Act equity stake and the Nvidia/SoftBank investments this
  thread already tracks.
  ([Intel Newsroom](https://newsroom.intel.com/corporate/intel-announces-proposed-15-billion-common-stock-offering)) ⟨daily 2026-08-10⟩

## 2026-07-26 — The stake, marked to market: $8.9B → $36-42B

- **The government's Intel stake is now worth $36-42B**, up from the
  $8.9B paid — cited alongside a wider, uncoordinated federal equity
  portfolio: ~$26.7B across ~30 equity/quasi-equity deals scattered
  across Commerce (17), Defense (7), DFC (6), and Energy (2), with **no
  centralized oversight** (no TARP-style inspector general or GAO audit
  equivalent). Directly answers this thread's "does the state stake
  change behavior" watch: so far, no — it's accumulating with no visible
  governance layer.
  ([Fortune](https://fortune.com/2026/07/26/the-u-s-government-invested-27-billion-in-corporate-stakes-good-luck-finding-them/)) ⟨daily 2026-07-28⟩
- **⚠ Contradiction, unresolved — three figures, one stake:** Trump says
  the position "made about $70 billion in eight or nine months"; a
  separate Yahoo Finance/Treasury-sourced figure puts unrealized gains at
  "roughly $47.6 billion" (implying ~$56.5B current value); Fortune/
  TheNextWeb/Biggo separately size the whole position at $36-42B. None of
  the three reconcile with each other on the same $8.9B cost basis.
  Flagging, not resolving — worth a dedicated crawl if Ben wants the real
  number.
  ([Yahoo Finance](https://finance.yahoo.com/economy/policy/articles/trump-says-government-intel-stake-143115077.html)) ⟨daily 2026-07-28⟩

## 2026-07-23 — Q2 2026: the best quarter in ~15 years

- **Revenue $16.13B (+25% YoY, fastest growth in ~15 years), adjusted EPS
  $0.42 vs $0.21 expected** — AI-driven business (Foundry + AI-adjacent
  products) grew 70%+ YoY and now runs ~70% of revenue; gross margin
  41.8%, ~280bp above guidance. Stock fell 2.46% in the regular session to
  $100.10, then rose 3.44% after-hours as investors digested the beat.
  2026 capex guidance raised to $20B+.
  ([TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262050823-intel-earnings-report-q2-2026-intc-ai-data-center-intel-foundry-tradingkey)) ⟨daily 2026-07-28⟩
- **This is the first real revenue evidence behind the turnaround thesis**
  this thread tracks (18A/14A execution, foundry customer wins) — thrust
  was reading ≈0 in the crawl; today's print is the first print that
  argues otherwise, pending confirmation the AI-segment growth holds.

## ← Backstory

<!-- /crawl appends below; finding pointer goes in the heading line -->

### Backstory — the stake-value tangle, resolved 2026-07-28
Finding: `artifacts/findings/intel-stake-tangle-2026-07-28.md` · Bundle:
`artifacts/bundles/intel-stake-tangle-2026-07-28/provenance.yaml`

- **The three public figures are one position measured three ways** —
  fixed basis 433.3M sh @ $20.469 = $8.87B: **$36B** = April price ·
  **$42B** = July price (Fortune, the best current figure) · **~$56.5B**
  = the May-8 price peak ($129 intraday, Apple-deal day; a Kobeissi
  Letter number). **Trump's "$70B" gain is unsupported** — needs ~$182/sh
  stock-only (never traded), reachable only by counting the warrant's
  240.5M shares at full spot with the $20 strike and non-exercisability
  ignored, at pre-selloff prices. ⟨crawl 2026-07-28⟩
- **The filing-accurate number nobody uses: the government holds 290.3M
  shares today, not 433.3M** — 143M still escrowed against future Secure
  Enclave disbursements (Q2 FY26 10-Q). Literal current value **$25-28B**,
  gain ≈ $19-21B. Ownership diluted to **8.6%** (5.8% issued-only) by the
  SoftBank (Aug-25) and Nvidia (closed Dec-25) raises — the "9.9%" is a
  2025 headline. ⟨crawl 2026-07-28⟩
- **No SC 13D/13G was ever filed** for the position — 8-Ks and press
  releases only; unusual for a >5% holder, and the disclosure-side twin
  of Fortune's "in no budget document" finding. ⟨crawl 2026-07-28⟩

### Backstory — reconstructed 2026-07-28
Finding: `artifacts/findings/intel-rescue-2026-07-28.md` · Bundle:
`artifacts/bundles/intel-rescue-2026-07-28/provenance.yaml`

- **SoftBank stakes Intel first, $2B** — announced 2025-08-18/19 (SPA
  executed 08-28, closed 09-26), 86,956,522 shares at $23.00/share,
  widely read as Son personally backing CEO Lip-Bu Tan.
  ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/50863/000005086325000126/a08182025form8-kex991.htm)) ⟨crawl 2026-07-28⟩
- **The layoffs and the fab cuts land together** — 2025-07-24/25: ~24,000
  layoffs announced (target 75,000 "core employees"; Tan: "no more blank
  checks"), Magdeburg Germany fab cancelled outright, Poland assembly/test
  site scrapped, and New Albany, Ohio construction "further slowed" — all
  in the same Q2 2025 earnings-adjacent announcement wave.
  ([Google News RSS](https://news.google.com/rss/search?q=Intel+layoffs+24%2C000+2025)) ⟨crawl 2026-07-28⟩
- **US government takes a 9.9% stake, $8.9B, with a foundry-contingent
  warrant** — agreement 2025-08-22, closed 08-26: $5.695B in accelerated
  CHIPS Act funds + $3.175B Secure Enclave funds converted to 433.3M
  shares. A separate 240.5M-share warrant (strike $20, 5-year term) is
  exercisable only if Intel's foundry ownership drops below 51% — a
  poison pill against a foundry breakup, not a growth-funding mechanism.
  No board seat; Commerce votes with the Board except narrow carve-outs.
  ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/50863/000005086325000129/intc-20250822.htm)) ⟨crawl 2026-07-28⟩
- **Nvidia invests $5B and signs on to co-design chips** — SPA executed
  2025-09-15, announced 09-18, closed 12-26: 214,776,632 shares at
  $23.28/share. Real technical terms, not just equity: Intel builds
  Nvidia-custom x86 CPUs for Nvidia's AI infrastructure and x86 SoCs
  integrating Nvidia RTX GPU chiplets, connected via NVLink. Intel stock
  +22% same day, best single-day gain in ~38 years.
  ([Nvidia newsroom](https://nvidianews.nvidia.com/news/nvidia-and-intel-to-develop-ai-infrastructure-and-personal-computing-products)) ⟨crawl 2026-07-28⟩
- **Altera divestment closes, Abu Dhabi's MGX rides along** — Silver
  Lake's 51% purchase of Altera (announced 2025-04-14, $4.46B cash,
  ~$8.75-9B implied valuation) closes 2025-09-15; MGX reported to have
  contributed ~$3.3B of the purchase alongside Silver Lake (09-16/17).
  ([Google News RSS](https://news.google.com/rss/search?q=Intel+Altera+Silver+Lake+divestment+close)) ⟨crawl 2026-07-28⟩
- **Ohio goes quiet, then "on life support," then a denied buyout rumor**
  — by 2025-09-05/10 the New Albany site is described as "on life
  support" three years after groundbreaking, still unfinished, 5+ local
  leaders gone. Sentiment shifts by mid-2026 as Intel's stock rallies and
  the Apple foundry deal raises hopes of an anchor tenant; a 2026-07-21/22
  report that SK Hynix was in talks to buy the Ohio campus was denied by
  SK Hynix the same day, with Intel confirming 07-23 it's seeking *a*
  partner generally. Production timeline has slipped to a reported
  2030-2031 range.
  ([Google News RSS](https://news.google.com/rss/search?q=%22Intel%22+%22Ohio%22+%22SK+hynix%22+acquisition+talks)) ⟨crawl 2026-07-28⟩
- **18A stabilizes, 14A finds its first customer, Apple and Microsoft
  sign on** — 18A-P enters risk production 2026-06-16/17 (9% perf gain,
  40% lower thermal resistance vs base 18A); by 07-07 the node is
  reported "finally running smoothly." Foundry customer wins accumulate
  through the year: Microsoft's Maia 2 on 18A/18A-P (~Oct 2025), Tesla's
  $20B "Terafab" as first named 14A customer (2026-04-22/23), a
  preliminary Apple chip-making agreement on 18A-P (announced 05-08,
  Trump confirms 06-18), and Fortinet on Intel 4 (~07-27/28). No named
  18A/14A customer rejection surfaced in this crawl.
  ([Google News RSS](https://news.google.com/rss/search?q=Intel+18A+14A+process+node+2026)) ⟨crawl 2026-07-28⟩
- **CXMT passes Intel's market cap** — 2026-07-26/27: Chinese DRAM maker
  ChangXin Memory Technologies debuts on Shanghai's STAR Market, surges
  ~465-500%, briefly becomes China's most valuable A-share company;
  multiple outlets state this surpassed Intel's own market cap, which was
  already under pressure (reported ~$79B lost ahead of earnings 07-17,
  a further ~$90B "wipeout" 07-24). No exact side-by-side dollar figures
  found — the crossover is confirmed qualitatively, not numerically.
  ([Google News RSS](https://news.google.com/rss/search?q=CXMT+market+cap+Intel+surpass)) ⟨crawl 2026-07-28⟩
