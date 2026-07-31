# Finding — Broadcom + Qualcomm — crawl 2026-07-28

*Crawl date: 2026-07-28. W4 backlog item: Broadcom's missing actor-doing
synthesis + the merge-vs-new decision on its rentier story (backlog.md W2
line 76); Qualcomm's missing actor-doing synthesis (backlog.md W2 line 74,
W4 line 104) and RISC-V corroboration, building on
`artifacts/findings/arm-royalty-regime-2026-07-28.md` §6 rather than
re-crawling the Ventana/Tenstorrent material from scratch.
Bundle: `artifacts/bundles/broadcom-qualcomm-2026-07-28/`.*

Method note: two sonnet subagents ran WebFetch sweeps in parallel (one per
actor) against Google News RSS search feeds plus direct outlet and
primary-source (company newsroom/IR) URLs, per the crawl skill's
WebSearch-exhaustion pre-flight. Most direct outlet fetches (Reuters,
Bloomberg, CNBC, The Register, Ars Technica, MacRumors, WSJ, TechCrunch)
403'd or 404'd — those citations rest on Google News RSS
title/source/date metadata, marked **medium** rather than **high** unless
independently corroborated by 3+ converging outlets on the same fact,
which several items below are. Company-primary sources (qualcomm.com,
OpenAI newsroom, stockanalysis.com financials) resolved cleanly and are
marked **high**. Nothing below is fabricated; gaps are marked **not
found** or **(thin)** rather than guessed.

---

## Broadcom — the toll collector, now with a fifth customer and an
## escalating second toll

**Verdict:** Broadcom's custom-ASIC co-design book widened again this
window — Meta extended through 2029, OpenAI's Jalapeño went from rumor to
unveiled product, and Apple joined as a **new** $30B/2031 customer — while
the VMware annuity, the *other* toll, went from "backlash" to active
litigation (Tesco: 40,000 servers, >£100M claim). Capex stayed
dep-only-thrust-confirmed (~$230M/quarter capex vs ~$2.15-2.2B/quarter
D&A, ~10-11%) — Broadcom collects, it doesn't build.

- **2025-12 → 2026-04 — Google TPU book widens.** A **$21B** Google TPU
  order was reported 2025-12-12 (analyticsindiamag.com, medium,
  RSS-metadata). On **2026-04-07/08**, four outlets (24/7 Wall St., Data
  Center Knowledge, IT Pro, and one more) converged same-week on
  **Anthropic signing a multi-gigawatt TPU deal with Google and
  Broadcom** as Claude demand picked up — Broadcom named as co-designer
  in the deal reporting, not just Google. (medium — RSS-metadata
  convergence, no full-text fetch succeeded)
- **2026-04-14/15 — Meta extended through 2029, and Hock Tan left Meta's
  board the same week.** Seven-plus outlets (CNBC, Reuters, qz.com,
  TechSpot, Anadolu Ajansı, The Fast Mode, Investing.com) converged on
  **Meta extending its custom-chip (MTIA) deal with Broadcom through
  2029**, framed as powering Meta's multi-gigawatt AI buildout. CNBC's
  framing paired the extension with **Broadcom CEO Hock Tan leaving
  Meta's board** — read as resolving what had been a conflict-of-interest
  optic while the two companies deepen the commercial relationship.
  (medium — the extension-to-2029 fact itself is high-confidence on
  breadth of convergence; the specific figures below are not)
  - Two dollar/scale figures circulated but rest on thin single-outlet
    sourcing, don't treat as confirmed: **"$35B"** extension value
    (tech-insider.org, thin) and **"1 gigawatt"** of committed custom
    chips (CNBC, medium but single-outlet on the number itself).
  - **2026-07-09** — Yahoo Finance (medium, RSS-metadata): Meta to start
    production of an **"Iris" AI chip** in September 2026 — plausibly a
    next-gen MTIA codename, but the Broadcom co-design link is **not
    independently confirmed** this session.
- **2026-06-24 — OpenAI's Jalapeño inference chip unveiled.** OpenAI's
  own newsroom plus 7+ outlets (Tom's Hardware, CNBC, VentureBeat, qz.com,
  The Verge, Forbes, The Tribune) converged same-day on **OpenAI and
  Broadcom unveiling "Jalapeño,"** an LLM-inference-optimized custom
  chip, targeting **gigawatt-scale deployment starting 2026** per The
  Tribune (medium, single-outlet on that specific target). The Futurum
  Group (2026-06-26, medium) claimed a **9-month design-to-unveil
  cycle** — unverified against a primary source. **Not found:** any
  confirmed tape-out date, production-volume commitment, or reported
  delay — every source describes the unveiling event, not a
  manufacturing milestone. This resolves the crawl brief's open
  "Jalapeño status" question: **unveiled and public, not yet in
  production** as of this crawl.
- **2026-07-06 → 07-13 — NEW: Apple extends to 2031, ~$30B, ~15B chips.**
  Eight-plus outlets (Reuters, Bloomberg, MacRumors, The Register, Yahoo
  Finance, NBC News, The Globe and Mail, MSN) converged on **Apple and
  Broadcom extending their custom-silicon supply relationship through
  2031**, value **"over $30 billion,"** with a **"15 billion chips"**
  production figure from Tim Cook per The Globe and Mail (medium,
  single-outlet on the chip-count figure) and a domestic-manufacturing
  angle tied to Broadcom's **Fort Collins, Colorado** facility (thin,
  single outlet). This is **new** relative to the crawl brief's framing
  — a fifth major customer (after Google, Meta, OpenAI, and the
  established networking/RF relationship) confirmed just three weeks
  before this crawl. **Scope caveat:** no fetched source itemized
  whether this is RF/wireless chips (Apple's long-standing Broadcom
  relationship), AI-adjacent custom silicon, or both — treat "custom
  silicon" framing as the outlets' own language, not independently
  disaggregated here.
- **ByteDance — not corroborated for 2026.** The Reuters ByteDance-Broadcom
  scoop is from **2024-06-24** (background, outside this window). 2026
  ByteDance chip reporting (2026-02-10 Reuters: Samsung manufacturing
  talks; 2026-05-30 TweakTown: "in-house" framing) does **not** name
  Broadcom. **Flag: do not assert an active 2026 Broadcom-ByteDance
  relationship** — the crawl brief's premise here is unconfirmed, possibly
  stale from the 2024 story.
- **2026-04 → 07 — VMware: backlash became litigation.** The controversy
  the brief asked about ("pricing backlash?") escalated concretely:
  **2026-06-17/18** — six-plus outlets (Ars Technica, The Register,
  Crypto Briefing, TechRadar, Cyber Magazine, SDxCentral) converged on
  **Tesco moving 40,000 server workloads off VMware** and **suing
  Broadcom** (the underlying suit predates the window, filed
  2025-09-04 per TechRadar background) for **damages sought over £100M**
  per Crypto Briefing (medium, single-outlet on the exact figure).
  Independent of Tesco: 2026-04-09 Ars Technica reported "'negative'
  views of Broadcom driving thousands of VMware migrations" (a rival's
  claim, medium); coverage continued through **2026-07-23/25** (Mshale,
  medium) still framing Broadcom as facing "VMware backlash risk." This
  is now an active, litigated, and continuing story through the crawl
  date — not resolved, not cooling off.
- **Capex vs. depreciation — dep-only-thrust rule confirmed with fresh
  quarters.** stockanalysis.com quarterly cash-flow data (medium —
  third-party aggregator, primary 10-Q not directly fetched): Q3 FY25
  capex -$142M / D&A $2,202M; Q4 FY25 -$237M / $2,233M; Q1 FY26 -$250M /
  $2,153M; Q2 FY26 -$231M / $2,165M. TTM capex **-$860M** vs TTM D&A
  **$8,753M** — capex running **~10-11% of depreciation**, consistent
  with board.yaml's `axes_num.thrust: 0` dep-only framing (this is the
  underlying quarterly detail behind that annual call).
- **Next earnings — not found.** No source located an announced Q3
  FY2026 date. Historical cadence (Q2 FY26 reported 2026-06-03; Q4/FY25
  reported 2025-12-11) points to early **September 2026**, but this is
  inference, not a confirmed date — do not publish it as confirmed.

---

## Qualcomm — the RISC-V hedge cooled, but a much bigger datacenter bet
## just launched in its place

**Verdict:** The crawl brief's premise (corroborate an $8-10B Tenstorrent
close) did **not** hold up — talks were real (mid-June, high-confidence
convergence) but the CEO denied them by month-end and no closing followed.
What actually happened instead, same week, was bigger: a June 24 Investor
Day launched **Dragonfly**, Qualcomm's own datacenter CPU+accelerator
line, with **Meta and Microsoft as named launch customers** and a
**$15B-by-2029 datacenter revenue target** — a direct entry into territory
Arm (AGI CPU), Broadcom (co-designed accelerators), and Nvidia currently
occupy. Alphawave closed cleanly in December with no regulatory drama.
Qualcomm reports **earnings tomorrow, 2026-07-29** (confirmed, 4
converging outlets) — arriving one day after this crawl.

- **2025-12-18 — Alphawave closed clean.** Qualcomm's own newsroom
  (high) plus Business Wire, Investing.com, and IT Pro confirm the
  **$2.4B / $2.48-per-share** acquisition **completed**, with the UK
  High Court sanctioning the scheme of arrangement 2025-12-22. A
  targeted search for a UK national-security or China SAMR holdup
  narrative returned **nothing** — treat the deal as closed without a
  reported regulatory obstacle, contrary to the crawl brief's implied
  "close status" uncertainty.
- **Ventana integration — thin, and possibly superseded by "Dragonfly"
  branding.** Beyond the 2025-12-10 acquisition (prior crawl baseline),
  the only 2026 signal found is **2026-02-24** Wells Fargo raising its
  Qualcomm price target to $150, citing the Ventana + Alphawave AI
  acquisitions as basis (TradingView/Seeking Alpha, medium). **No 2026
  reporting on Veyron V2 silicon shipments or roadmap changes was
  found.** Notably, the June 24 "Dragonfly" datacenter roadmap
  announcement (below) does **not** name "Veyron" in any fetched
  coverage — **flagged open gap, not confirmed either way**: whether
  Dragonfly supersedes, absorbs, or runs parallel to the RISC-V Veyron
  line is unresolved and worth a direct question on the next pass.
- **2026-06-15 → 06-30 — Tenstorrent: talked about, not closed.** Reuters
  + The Information + Yahoo Finance converged 2026-06-15 (high) on
  **Qualcomm in talks to acquire Tenstorrent for up to $10B**. By
  **2026-06-29**, GuruFocus reported **Tenstorrent's CEO denying the
  talks** (medium, single-outlet), and 2026-06-30 TradingView headlined
  "Qualcomm's Tenstorrent Deal Looks Less Likely." **No confirmed close,
  no July update found.** The crawl brief's ask to "corroborate the
  $8-10B" is answered: the figure and the talks are real and
  well-sourced, but the deal itself did not close and looks to have
  stalled or fallen through.
- **2026-06-24 — What happened instead: Dragonfly + Modular, same
  Investor Day.** Qualcomm's own newsroom (high, primary) unveiled a
  **"comprehensive data center roadmap"**: the **Dragonfly C1000 CPU**
  (250+ cores, up to 5GHz, deployment starting 2028) and **Dragonfly
  AI300** accelerator, plus a new **HBC** (memory-bandwidth) architecture
  — reported in product detail by StorageReview.com (medium-high) and
  corroborated across Forbes/CNBC/Reuters. Targets: **$15B datacenter
  revenue by 2029**, **$40B total non-handset revenue by 2029** (roughly
  double prior guidance) — Reuters, CNBC, and Benzinga converge (high),
  with **CNBC reporting the stock popped 15%** on the news. Named
  customers announced same day: **Meta** (multi-generation CPU supply
  agreement, primary source, deployment starting 2028), **Microsoft**
  (early HBC deployment, single-outlet Invezz, medium), and **ByteDance**
  (China-specific AI-chip production agreement, "China-compliant export
  variants" per Tom's Hardware, medium). Same day, Qualcomm also
  announced acquiring **Modular** (AI-inference software, **$3.9B**
  stock deal) — explicitly framed by WSJ/Bloomberg as a counter to
  Nvidia's CUDA software moat. Futurum Group (2026-06-29, medium)
  explicitly frames the whole day as a **"re-entry"** into the
  datacenter-CPU market Qualcomm exited after Centriq (~2018) — directly
  answering the crawl brief's "datacenter-CPU return" question, and at
  materially larger scale than the brief's framing implied.
- **Edge-AI / Snapdragon — steady, not the story this window.** Mobile:
  Snapdragon 8 Elite Gen 6 leak-tier coverage points to a **September
  2026** launch (medium, unconfirmed). PC: Snapdragon X2 Plus/Elite
  launched January 2026 (The Register, high); **no 2026-dated
  market-share figure was found** — only stale 2024/2025 numbers exist,
  so current PC share is genuinely unknown from this sweep. Automotive
  (Digital Chassis) had the most concrete 2026 motion: Toyota RAV4 (Jan,
  primary), a VW letter-of-intent (Jan, primary + Automotive News),
  Tata manufacturing partnership (Feb), Bosch ADAS expansion (April,
  primary), and a Stellantis expansion (May, primary) that **popped the
  stock 12%** per TradingView.
- **Arm relationship post-trial — quieter than expected, one new
  wrinkle.** **2026-02-17** — Yahoo Finance (medium, single-outlet):
  Qualcomm withdrawing a separate **UK lawsuit** over royalties,
  presumably mooted by the Delaware win. **2026-05-15/18** — four
  outlets (Reuters, Straits Times, Electronics Weekly, biggo.com,
  medium-high) reported **Arm facing an FTC antitrust probe** — not
  explicitly tied to Qualcomm as complainant in what was fetched, but
  consistent with the same licensing-restriction dispute pattern. **No
  appeal-status confirmation or reconciliation found** — this remains an
  open gap shared with the arm-royalty-regime finding (its own open
  question #1).
- **Capex/depreciation and cash — Q2 FY26 detail, ahead of tomorrow's
  print.** stockanalysis.com (medium): Q2 FY26 (period ended 2026-03-29)
  capex **-$533M** vs D&A **$413M** — capex *exceeds* depreciation this
  quarter (unlike Broadcom's pattern), consistent with the existing
  `artifacts/bundles/qualcomm-node/provenance.yaml` bundle's TTM figures
  (capex $1.78B, FCF $12.5B, cash+STI $9.8B) — no update needed there,
  this sweep corroborates rather than revises it.
- **Next earnings — confirmed 2026-07-29.** Four converging outlets
  (Stock Titan, AlphaStreet, Barchart, Yahoo Finance) — Qualcomm's fiscal
  Q3 FY2026 report lands **the day after this crawl**.

---

## Cross-actor read

Both companies are mid-motion on the *same* axis right now — who collects
rent on custom AI silicon — but from opposite starting points. Broadcom
keeps widening an **outsourced-design** book (5 hyperscaler/major
customers now, each on a multi-year extension) while its VMware toll
turns openly adversarial. Qualcomm just announced it wants to **build its
own competing datacenter line** (Dragonfly) rather than only license
(Arm) or hedge (RISC-V/Ventana) — with Meta as a customer of *both*
companies simultaneously (MTIA-via-Broadcom for accelerators, Dragonfly
CPUs directly from Qualcomm), which is itself a small data point on how
hyperscalers are multi-sourcing every layer of the stack rather than
picking one silicon partner.

## Open questions for the next crawl

1. Does Dragonfly supersede, absorb, or run parallel to Ventana's Veyron
   RISC-V line? (Broadcom-adjacent question, actually Qualcomm)
2. Broadcom Q3 FY2026 earnings date — not found this session, check
   investors.broadcom.com directly.
3. Jalapeño — first tape-out/production milestone, once one is reported.
4. Whether the Apple $30B/2031 deal is RF-only, AI-silicon-inclusive, or
   both — no source disaggregated this.
5. Whether ByteDance's 2026 in-house-chip reporting (Samsung-manufacturing
   angle) has any live Broadcom co-design component, or whether that
   relationship lapsed after the 2024 scoop.
6. Qualcomm's Q3 FY2026 print (2026-07-29, tomorrow) — first live test of
   whether Dragonfly's $15B/2029 target moves guidance at all this early.
