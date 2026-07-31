# Finding — Arm Royalty Regime — crawl 2026-07-28

**Verdict:** The ~$800B-gravity ISA chokepoint held through 2025-2026, but on
three fronts simultaneously: Arm **won the war, lost a battle** (Qualcomm
trial-court victory, appeal pending); it **stopped being a pure rentier**
(first-ever in-house chip, the "Arm AGI CPU," launched March 2026 with Meta
as customer); and the **design-around threat materialized in the open**
(Qualcomm bought a RISC-V chip company explicitly as an Arm hedge, mid-
litigation). SoftBank's 87.1% grip didn't loosen — if anything Arm shares
became SoftBank's preferred loan collateral for funding its OpenAI bets.

## 1. Qualcomm v. Arm — resolved at trial, appeal open

The Dec-2024 jury verdict (Qualcomm not liable on the Nuvia license breach,
deadlocked on the architecture-license claim) got a follow-on ruling:

- **2025-09-30/10-01** — A Delaware judge **rejected Arm's last remaining
  legal claim**, handing Qualcomm a complete trial-court win on the
  architecture-license question the jury had deadlocked on. Converged 4+
  outlets same news cycle: The Register, EE Times, Barron's ("Qualcomm
  Prevails Over Arm in Court. Next, an Appeal."), FoneArena. (high)
- **2025-10-02** — Reuters: **Arm plans to appeal** the final ruling.
  (high)
- **2025-10-03** — Data Center Dynamics confirms the Delaware ruling detail
  (Judge sides with Qualcomm and Nuvia). (high)
- **Open / not found:** no 2026 update located on the appeal's status
  (whether formally filed, to which court, any ruling). Treat as
  unresolved going into the next crawl. (thin — absence of coverage, not a
  negative finding)

Net effect: Qualcomm keeps its Nuvia-derived Oryon cores under its existing
architecture license — Arm did **not** get to force a re-license or block
Qualcomm's custom-core strategy. This is the backdrop against which
Qualcomm then bought a RISC-V company two months later (see §5).

## 2. Royalty-rate trajectory — v9/CSS driving growth, no v10 found

- **2025-07-31** — Q1 FY26: royalty revenue **+25% YoY**, Armv9 + CSS
  (Compute Subsystems) cited as the growth driver, revenue >$1B. EE
  Times, Investing.com. (medium)
- **2025-11-05** — Q2 FY26: revenue **>$1B for a third consecutive
  quarter**. Arm Newsroom (primary). (medium)
- **2026-02-04** — Q3 FY26: **fourth consecutive billion-dollar revenue
  quarter**. Arm Newsroom (primary). (medium)
- **2026-05-06** — Q4 + full FY2026 results: Arm's own newsroom, Business
  Wire, and Investing.com all report **"record-breaking" full-year
  results** same day — but the exact **$4.92B total revenue / $2.61B
  royalty revenue** figures (as given in the crawl brief) could **not be
  independently re-verified** this session — investors.arm.com and
  newsroom.arm.com direct fetches 404'd/stripped, so those two figures
  rest on the brief's framing plus directional corroboration from four
  straight >$1B quarters (~$4.9B annualized is consistent with the
  quarterly cadence). (medium on the trajectory, thin on the exact digits)
- **2026-06-02** — Arm's own $15B/yr chip-revenue target **"will arrive
  years early"** per company statement, reported by finance.biggo.com.
  (thin — single niche outlet, forward-looking, not an actual)
- **No v10 architecture found.** v9 + CSS remains the current royalty
  driver through FY2026; no v10 announcement surfaced in this crawl.
  (flagged gap)

## 3. SoftBank's 87.1% — collateral lever, not a sell-down

SoftBank did not reduce its Arm stake this window, but used it hard as
leverage:

- **2025-10-10** — Tom's Hardware: SoftBank **seeking a $5B loan using Arm
  shares as collateral** to fund an OpenAI investment. (medium)
- **2025-12-27** — mexc.co / Blockonomi: SoftBank's **$20B margin loan
  against Arm Holdings** faces a December deadline. **Outcome not found**
  — no resolution article located (extended? repaid? triggered a forced
  sale?). (medium sourcing, thin on resolution — flagged open)
- **2026-04-22/23** — SoftBank separately pursues (and by **2026-07-01**,
  per Reuters, **renews talks with added concessions for**) a **$10B loan
  collateralized by OpenAI shares** — a *different* collateral pool than
  Arm, but same playbook (lever the crown-jewel equity stakes to fund the
  OpenAI bridge). (high on the 07-01 Reuters item; medium on the April
  precursor)
- **2026-05-21** — TradingKey: Arm's market value **surpassed $300B**,
  making SoftBank's 87% stake the single biggest winner of the run-up.
  (medium)

**Raspberry Pi — likely resolves the FY26 20-F "subsequent event" flag,
not fully confirmed:** on **2026-04-23**, an Arm subsidiary **invested
£50M into a £60M Raspberry Pi share placing** — a follow-on top-up of a
stake Arm has held since Nov 2023 (it was also a 2024 Raspberry Pi IPO
investor), not a new acquisition or a lawsuit. Two outlets (businesscloud
.co.uk, London South East) converge on date and amount. (medium) The
timing — about two weeks before the **2026-05-06** FY2026 results date —
fits an unresolved-subsequent-event disclosure, but this crawl could
**not directly confirm** that this transaction is the specific item the
20-F flagged. Treat the link as **inferred, not confirmed** — worth a
direct 20-F pull on the next crawl pass.

## 4. Moving up-stack — Arm's first-ever in-house chip

- **2025-02-14** — TechPowerUp: earliest reporting that Arm would develop
  **in-house server CPUs with Meta as first customer**. (medium, RSS
  metadata only, but consistent with what followed)
- **2025-07-30** — Arm shares fell ~8% after-hours (~13% next morning) on
  a soft Q2 profit forecast, alongside signaling it would invest profits
  into **developing its own chips** — the market's first real look at the
  strategy shift. Reuters, corroborated by Economic Times/Investopedia.
  (high)
- **2025-10-06** — Arm Newsroom: company framing of the CSS/CSA
  (Compute Subsystem Architecture) chiplet push — "democratizing custom
  AI silicon." (medium, primary but promotional)
- **2025-11-18** — Arm Newsroom: **Microsoft's Azure Cobalt 200** datacenter
  CPU confirmed built on **Neoverse CSS V3**. (medium)
- **2026-03-24** — Arm unveils the **"Arm AGI CPU"** — its **first
  in-house-designed chip in a 35-year history**: a 136-core Neoverse-based
  CPU targeting AI-inference workloads in datacenters, development begun
  2023. Launch customer **Meta**; other named partners **OpenAI,
  Cerebras, Cloudflare**. Converges CNBC, TechCrunch (fetched full text),
  The Information, and Arm's own newsroom. (high)
- **2026-03-25** — Follow-on trade-press analysis: The Next Platform
  ("Arm Comes Full Circle"), ServeTheHome ("Arm AGI CPU Launched
  Establishing Arm as a Silicon Provider"). (medium)
- **Not confirmed:** deal economics (pricing/royalty treatment) of the
  Meta AGI-CPU arrangement — no source disclosed terms. (flagged gap)

This is the structural pivot underneath the "royalty regime" framing:
Arm is no longer purely a licensor collecting rent on others' silicon: it
now competes with some of its own licensees (Qualcomm, Nvidia's Grace
customers) as a chip vendor.

## 5. Datacenter share — real growth, competing figures don't reconcile

- **2025-09-11** — The Register: Arm's **server-CPU revenue share doubled
  YoY, ~15% → 25%**, driven by Nvidia Grace + custom cloud silicon — but
  **short of the 50%-by-end-2025 target** Arm's own infrastructure
  leadership had set. (medium)
- **2026-02-18** — Tom's Hardware/MarketWatch: Meta to deploy **standalone
  Nvidia Grace CPUs** in production, up to 2x perf/watt on some workloads
  — framed as an "Intel killer." (medium)
- **2026-04-24** — Meta signs a **multiyear, multibillion-dollar AWS deal
  for Graviton5** (Arm-based) chips. Outlets disagree on scale — Amazon's
  own release says "tens of millions of Graviton cores," Reuters/CNBC/
  Bloomberg say "hundreds of thousands" of chips over 3+ years. Flagging
  the discrepancy rather than picking one. Converges 5+ outlets on the
  deal itself. (high on the deal; medium on the scale figure)
- **2026-06-22** — Tom's Hardware, citing IDC: **non-x86 platforms = 47.9%
  ($58.7B) of $122.6B** in Q1 2026 global server revenue; accelerated
  (GPU/ASIC) servers >70% of total revenue. **Caution: "non-x86" is not
  the same scope as "Arm"** — this figure includes non-Arm accelerators
  and shouldn't be read as an Arm-specific share number. (medium)
- **2026-06-25** — Nikkei Asia: an **unnamed Arm executive** claims Arm now
  has **>50% share of hyperscale/"top AI" datacenters** — no methodology,
  no named source, a company talking its own book. (thin)

**Do not average the 25% / 45-48% / 50%+ figures** — they use different
scopes (server-CPU unit share vs. server revenue vs. non-x86 vs.
hyperscaler-only) from different dates. Directionally: real, fast,
unambiguous growth through the window; precisely how big remains
genuinely unsettled and partly self-reported.

## 6. RISC-V — the design-around threat went from theoretical to funded

- **2025-12-10** — **Qualcomm acquired Ventana Micro Systems**, a RISC-V
  datacenter-CPU design firm (Veyron V2: up to 32 RISC-V cores, custom
  matrix-math AI accelerators, silicon expected early 2026). Qualcomm
  explicitly framed running **Arm and RISC-V cores in parallel** as a
  hedge **given its ongoing litigation with Arm** (quote from EVP Durga
  Malladi). Terms undisclosed. Primary source (qualcomm.com press
  release) + The Register, CRN, Data Center Dynamics, Tom's Hardware.
  (high)
- **2025-12-22** — Yahoo Finance: **Arm's stock dipped** on the Ventana
  news — read as the market pricing in a competitive threat. (thin,
  RSS metadata only, magnitude unconfirmed)
- **2026-06-16 → 06-24** — Reports (Tech Times, The Register) that
  **Qualcomm is in advanced talks to acquire Tenstorrent** (RISC-V AI-chip
  startup led by Jim Keller) for **$8-10B**, ~3x its prior valuation —
  would give Qualcomm a "full AI silicon stack." **Not confirmed
  closed** — described as ongoing talks; Tenstorrent also reportedly
  exploring other funding. (medium — multiple outlets converge on the
  figure, deal status explicitly a rumor)
- **2026-03-25/27** — **Alibaba DAMO Academy unveiled the XuanTie C950**,
  billed as the most powerful RISC-V processor yet, optimized to run
  China's top AI models — explicit China chip-self-sufficiency framing
  (not explicitly tied to US export controls in the sources fetched).
  The Register, South China Morning Post. (medium)
- **2026-01-15** — SCMP: **SpacemiT** (China) to launch a server-class
  RISC-V processor after a capital injection. (thin)
- **2025-07-21** — TechPowerUp: **Nvidia ported CUDA to RISC-V** — notable
  as a hedge signal even from one of Arm's own big (Grace) customers.
  (thin)
- **2026-01-06** — Digitimes: "Qualcomm, Google bet big on RISC-V for AI
  dominance" — **could not independently confirm** Google's specific
  RISC-V commitments beyond this single headline. (thin, flagged)

The throughline: RISC-V went from a background academic/embedded
alternative to a **funded, named competitive program inside Arm's own
largest litigation adversary**, timed within months of losing that
litigation to Arm.

## 7. FY2026 numbers and the stock narrative into July 2026

Four consecutive >$1B quarters (Jul-25, Nov-25, Feb-26, and the May-06-26
"record-breaking" FY2026 close) support the brief's ~$4.92B revenue /
$2.61B royalty framing directionally; exact digit verification is a gap
for the next crawl (primary IR fetches 404'd this session).

Stock/valuation narrative turned volatile and bifurcated into summer 2026:

- **2026-06-05** — TIKR: ARM **up 240% in 2026** YTD per one source, but
  Street mean target sits **38% below** the then-current price — an
  outsized figure, single-outlet, flagged as unusually large and worth
  re-checking rather than repeating uncritically. (thin-medium)
- **2026-06-24** — Bernstein raises price target. **2026-07-14** — an
  unnamed analyst downgrade reported. **2026-07-16** — Benzinga: "Wall
  Street Sounds Alarm on Stretched Valuation." (thin-medium, pattern
  across many single-outlet headlines)
- **2026-07-18** — simplywall.st: ARM down **17.4%**, tied explicitly to a
  **global AI-chip pullback + China export concerns**. (medium)
- **2026-07-27** — 24/7 Wall St.: ARM has fallen **28% in the past
  month** heading into **2026-07-29 earnings** (Arm's Q1 FY2027 report —
  two days after this crawl). (medium)

**Forward marker:** Arm reports **Q1 FY2027 earnings 2026-07-29** — the
next real test of whether the royalty trajectory (§2) and the AGI-CPU
pivot (§4) are showing up in guidance. Logged to `attention/upcoming.yaml`.

## Sourcing note

Two sonnet subagents ran WebFetch sweeps in parallel (legal/royalty/
SoftBank/financials; up-stack/datacenter/RISC-V/stock) against Google News
RSS search feeds plus direct outlet and Arm-primary-source URLs, per the
skill's WebSearch-exhaustion pre-flight. Google News redirect links mostly
did not resolve to full article text via WebFetch this session (same
pattern as the 2026-07-27 google-capex bundle) — where that happened, the
citation is the RSS feed item itself (title/source/date), marked medium
rather than high. The second subagent additionally used
`html.duckduckgo.com/html/` search-snippet lookups (not the session
WebSearch tool) to recover real outlet URLs behind Google News redirects,
then fetched several directly (TechCrunch and qualcomm.com succeeded in
full; CNBC 403'd; Reuters/The Register mostly blocked or 404'd on direct
fetch). No URL or figure was fabricated; multiple items are explicitly
flagged thin, unconfirmed, or contradictory rather than reconciled by
guesswork.

**Open questions for the next crawl:** (1) Arm's appeal status in the
Qualcomm case; (2) exact FY2026 $4.92B/$2.61B digit confirmation via a
primary filing; (3) direct 20-F confirmation that the Raspberry Pi £50M
top-up is the flagged subsequent event; (4) resolution of SoftBank's
Dec-2025 $20B Arm-collateral loan deadline; (5) whether the
Qualcomm-Tenstorrent RISC-V deal closes; (6) a methodologically clean,
single-scope Arm datacenter-share number.
