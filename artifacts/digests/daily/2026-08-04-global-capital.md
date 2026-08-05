---
lens: global-capital
date: 2026-08-04
status: final
window_start: 2026-08-04T05:00:00-04:00
as_of: 2026-08-05T06:45:00-04:00
coverage: done
---

# Global Capital — 2026-08-04

*Curated from agentic-interim dispatch (reconstruction pass, run
2026-08-05): a full missed-day sweep. Sources: CNBC, NPR, Yahoo Finance,
Shacknews, TradingKey, Investing.com, CNN, TheStreet, Fortune, Benzinga,
24/7 Wall St, FX Leaders, Briefs.co, AI Weekly. Interpretation below read
against `capital-context.yaml` (asof 07-30). Status stays `building` —
this digest-day closed only ~1.5h before this pass ran; a coverage-critic
pass runs on the next `/daily`.*

## Today's throughline

Two of the night's four highest-profile earnings prints — SpaceX and
AMD — both beat cleanly and both sold off hard, and the shared mechanism
is the same one: investors are no longer rewarding AI-capex beats on
their own terms, they're pricing the capex itself as a cost, not a
promise. Underneath that, the broader market had its best two days in
months (fresh S&P and Dow records, Palantir's biggest single-day gain
since 2024), and Nvidia is reportedly negotiating up to $750B in new
AI-infrastructure financing — reviving the circular-financing scrutiny
this map has tracked since Oracle's credit story diverged from its
equity story in July.

## Markets — records, and the beat-then-sell-off pattern

- **Broad market hit fresh records on AI-earnings confidence.** S&P 500
  closed +1.79% at 7,737 (first record in two months), Dow topped 54,000
  for the first time, Nasdaq +2.59% — a reversal of July's tech-led
  selloff on hopes AI capex is generating real returns.
  ([CNN](https://www.cnn.com/2026/08/04/investing/us-stock-market), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-4-2026))
  <!-- k: t=hyperscaler-capex-big-picture e= axis=markets-and-flows -->
- **Palantir jumped 29.7% on a Q2 blowout** — its largest single-day gain
  since 2024. Revenue $1.94B vs $1.80B expected, EPS $0.41 vs $0.35; US
  commercial revenue +149% YoY; FY26 guidance raised to $8.15-8.16B.
  CEO Karp called the results "otherworldly."
  ([CNBC](https://www.cnbc.com/2026/08/04/palantir-2q-earnings-ai-sovereign-tools.html))
  <!-- k: t=hyperscaler-capex-big-picture e= axis=markets-and-flows interp=yes -->
- **CoreWeave +20% on new government and international demand.** A
  Leidos partnership to supply AI cloud infrastructure to US
  defense/intelligence agencies, plus a first APAC expansion (three
  Indonesia data centers, 360MW) — sets up its 08-11 Q2 print.
  ([FX Leaders](https://www.fxleaders.com/news/2026/08/04/coreweave-crwv-stock-jumps-20-as-us-government-ai-deal-sparks-massive-rally/))
  <!-- k: t=coreweave-backlog-bet e=coreweave axis=markets-and-flows -->

## Two beats, two sell-offs — the AI-capex-as-cost pattern

- **SpaceX beat cleanly, and capex sank it anyway.** Revenue $7.8B (+92% YoY,
  beat ~$6.75-6.9B consensus); EPS -$0.09, far narrower than every
  tracked compiler's spread; adjusted EBITDA $3.5B (+191% YoY). Starlink
  led at $4.3B (the only profitable segment); the AI segment nearly
  tripled to $2.6B revenue but posted a $1.3B operating loss. Capex hit
  $18.4B, up 6x YoY, with $15.8B specifically AI-infrastructure — that
  number, not the beat, is what drove shares from +9.4% intraday to as
  much as -8.6% after-hours. Directly validates the "zero-AI-value"
  framing already on this thread (Morgan Stanley's 07-24 note).
  Management guided to a $100B annualized revenue run-rate by end of
  2026. [Ledger: `spacex-q2-earnings` hit, full detail in upcoming.yaml.]
  ([CNBC](https://www.cnbc.com/2026/08/04/spacex-spcx-earnings-live-updates-q2-2026.html), [NPR](https://www.npr.org/2026/08/04/nx-s1-5918536/spacex-first-earnings-report-since-ipo))
  <!-- k: t=spacexai-public-megacap e=spacex axis=markets-and-flows interp=yes sev=major -->
- **AMD beat and raised, fell 8-9% anyway** — the same pattern the same
  night, a different mechanism. Revenue $11.536B
  (record, +50% YoY) and Data Center $6.718B (+107% YoY) both cleared
  consensus; Q3 guide ~$13B. Coverage attributes the sell-off to
  stretched valuation (AMD trading above Nvidia's multiples) and flat
  56% margin guidance — Wall Street wanted a blowout Q3 forecast, not an
  in-line beat. [Ledger: `amd-q2-2026-earnings` hit, full detail in
  upcoming.yaml.]
  ([AMD IR](https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results), [Benzinga](https://www.benzinga.com/markets/tech/26/08/60936941/amd-earnings-stock-after-hours-wall-street-forecast))
  <!-- k: t=amd e=amd axis=markets-and-flows interp=yes -->

## The circular-financing question, revived at a bigger number

- **Nvidia in talks for up to $750B in AI deals** — $500B+ with SK
  Group, and up to $250B in lease guarantees to
  help OpenAI finance data-center compute. Terms still in flux; this is
  the same circular-financing mechanism already tracked on Oracle
  (Nvidia funding the buyers of its own chips), at a scale an order of
  magnitude larger than anything on this map so far.
  ([Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/nvidia-750-billion-deals-revive-102003935.html))
  <!-- k: t=nvidia-vendor-financing,ai-circular-financing-risk e=nvidia,openai axis=deals-and-filings interp=yes -->
- **Oracle's 5-year CDS remains near an 18-year/record high** (~2.03
  percentage points, up from 144bp at year-start) — unresolved into this
  window, the live proxy for AI-buildout credit risk this map has
  tracked since 07-17.
  <!-- k: t=ai-circular-financing-risk e=oracle axis=deals-and-filings -->
- **Goldman Sachs publicly warned Fed Chair Warsh's reduced-guidance
  approach could destabilize markets.** Warsh has stopped giving forward
  rate guidance and floated cutting policy meetings to six/year; Wall
  Street says the resulting communications void won't be tolerated the
  way pre-Warsh silence was.
  ([Fortune](https://fortune.com/2026/08/04/kevin-warsh-forward-guidance-goldman-sachs-wall-street-framework-inflation/))
  <!-- k: t= e= axis=deals-and-filings -->
- **Amazon priced a $25B, 8-tranche bond sale and says it's done issuing
  debt for 2026** — funding part of its $200B capex plan, part of a
  broader >$182B Big Tech AI-debt wave year-to-date.
  ([Briefs.co](https://www.briefs.co/news/amazon-to-issue-25b-in-bonds-halts-further-debt-issuance-for-2026/))
  <!-- k: t=aws-capex e=amazon-aws axis=deals-and-filings -->

## 📊 Macro strip

- Memory shortage thread intact, no relief: DRAM/NAND/HBM supply-demand
  gaps at worst since 2011; SK Hynix's CEO says the shortage could
  persist past 2030.
  <!-- k: t=ai-memory-shortage e=sk-hynix axis=macro-strip -->

## ⏳ Upcoming & expected

- ✅ **hit — `spacex-q2-earnings`**: beat cleanly, sold off on AI-capex
  shock. Full evidence in upcoming.yaml.
- ✅ **hit — `amd-q2-2026-earnings`**: beat and raised, sold off on
  valuation/margin concerns. Full evidence in upcoming.yaml.
- Next 7 days: `softbank-q1-earnings` and `spacex-insider-unlock` 08-06 ·
  `coreweave-q2-earnings` 08-11.

## 🔄 Map changes

- `~ threads/spacexai-public-megacap` — Q2 earnings resolved hit; capex
  shock detail added, `last_seen` → 08-04 (⟨daily 08-04⟩).
- `~ threads/amd` — Q2 earnings resolved hit (⟨daily 08-04⟩).
- `~ threads/nvidia-vendor-financing`, `~ threads/ai-circular-financing-risk`
  — Nvidia's reported $750B talks added (⟨daily 08-04⟩).
- `~ threads/coreweave-backlog-bet` — Leidos government deal + APAC
  expansion added (⟨daily 08-04⟩).
- `~ threads/aws-capex` — $25B bond sale added (⟨daily 08-04⟩).

## 🧵 Thread candidates

- **candidate:** **Palantir as a standalone thread.** Currently
  untracked on this map despite a +29.7% single-day move on real
  commercial-revenue growth (+149% YoY) — it keeps surfacing inside
  other hyperscaler-capex bullets without its own home. Palantir is not
  currently a watchlist entity either. Track it? (curator-noticed)

---
Two of the night's biggest earnings prints — SpaceX and AMD — both beat
cleanly and both sold off, because investors are pricing AI capex as a
cost rather than rewarding the beat around it; SpaceX's $15.8B
AI-infrastructure spend and AMD's flat margin guide were each what moved
the stock, not the top-line numbers. The broader market had its best
session in two months on the same AI-earnings confidence, Palantir
posted its biggest single-day gain since 2024, and Nvidia is reportedly
negotiating up to $750B in new financing deals that revive the
circular-financing question this map has been tracking since Oracle's
credit story diverged from its equity story in July.
