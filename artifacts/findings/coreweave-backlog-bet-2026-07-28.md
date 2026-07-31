# Finding — CoreWeave: the neocloud wager, IPO to now

**Thread:** coreweave-backlog-bet · **Crawled:** 2026-07-28 · **Bundle:**
`artifacts/bundles/coreweave-backlog-bet-2026-07-28/provenance.yaml`

Ben's brief: reconstruct the CoreWeave story from IPO (Mar 2025) to today —
backlog trajectory, customer concentration, the debt stack against the
AI-credit repricing, the failed Core Scientific deal and its aftermath,
Nvidia's actual stake, and the earnings calendar. Crawled via two sonnet
subagent WebFetch sweeps (Google News RSS + direct IR/SEC attempts); a
second pass went after specific gaps (Q2 earnings date, Nvidia stake %,
Microsoft concentration %, Core Scientific "plan B", Q1 net loss) and
closed four of five directly against CoreWeave's own SEC filings.

**Verdict up front:** CoreWeave is the neocloud wager in its purest form —
a **$99.4B backlog** built almost entirely on a handful of frontier-lab
contracts, financed by **debt priced at ~9.75%** and GPU-collateralized
structures, arriving into a market where the credit protecting that exact
trade (Nvidia CDS) **widened sharply the same week this crawl ran**
(2026-07-27). The Core Scientific deal — the plan to buy owned real estate
outright instead of leasing — **failed at the shareholder vote** in
October 2025, and the visible "plan B" is a scatter of smaller
international/leased deals with a **four-and-a-half-month gap** where no
new capacity announcement surfaced at all. Nvidia is simultaneously
CoreWeave's chip supplier, largest disclosed institutional shareholder
(~11%, an estimate), and the entity whose own credit risk is now the
market's live tell on whether the whole GPU-financing loop is cracking.

---

## 1. Backlog (RPO) trajectory

- **Q3 2025 (~Sep 2025):** backlog **doubled to $55.6B** (2025-11-11,
  Data Center Dynamics via RSS title — thin, single outlet).
- **Q4 2025 (Dec 2025 print, reported ~2026-03-06):** **$66.8B** — matches
  Ben's known reference point (Yahoo Finance via RSS; thin sourcing but
  corroborated by the brief's own figure — medium overall).
- **Q1 2026 (as of Mar 31 2026, reported 2026-05-06/08):** **$99.4B**
  (also reported rounded as "near $100B" / "$99B in contracts"), 3+
  converging outlets (grafa.com, TIKR.com, Yahoo Finance — one explicitly
  naming Nvidia, Meta, Microsoft, OpenAI as the backlog's contract
  counterparties). **Medium-high** confidence.
- **Most recent:** **no Q2 2026 figure exists yet.** CoreWeave has only
  announced the *date* it will report (see §7) — as of 2026-07-28 the
  $99.4B figure stands as the latest confirmed backlog. (gap — figure
  not yet available, not a sourcing failure.)

## 2. Customer concentration

- **OpenAI:** **$11.9B over 5 years**, announced **2025-03-10** — CNBC,
  Reuters, and a LinkedIn recap converge same-day; OpenAI also received
  **$350M in CoreWeave equity** as part of the deal (high confidence).
  **Expanded 2025-09-25** with an additional **$6.5B** (CNBC/WSJ/Reuters
  same-day; Reuters framed the quarter as CoreWeave's "diversification"
  push — high confidence). Cumulative OpenAI commitment reported as
  **~$22.4B** (Yahoo Finance + PYMNTS, 2025-09-25/26 — medium) though an
  outlier **$12B** figure also circulated (capacityglobal.com, 2025-10-09
  — thin); the two don't fully reconcile and likely reflect different
  partial-sum snapshots.
- **Meta:** **$21B** deal, announced **2026-04-09**, contract through
  **2032** — Bloomberg/CNBC/Reuters/Business Wire all same-day (high).
- **Anthropic:** a separate multi-year cloud deal, **2026-04-10** (single
  RSS mention — thin).
- **Jane Street:** **$6B**, **2026-04-15** (single RSS mention — thin).
- **IBM:** infrastructure/training partnership for IBM Granite models,
  **2025-01-15/16** (IBM Newsroom + StorageReview + Data Center
  Dynamics, 3 converging — medium on the fact, no dollar figure
  disclosed).
- **Nvidia as a CoreWeave customer:** a **$6.3B order** disclosed
  2025-09-15 (CNBC — medium).
- **Government/DoD:** no contract found — explicit gap.
- **Microsoft's share of revenue — the one gap worth flagging as a
  finding in itself.** CoreWeave's own **S-1** (filed 2025-03-03, SEC
  accession `0001769628-25-...` via EDGAR full text) states: *"We
  recognized an aggregate of approximately 77% of our revenue from our
  top two customers for the year ended December 31, 2024. None of our
  other customers represented 10% or more of our revenue."* Microsoft is
  named elsewhere as a customer but never tied to a specific percentage.
  CoreWeave's **Q1 2026 10-Q** (filed 2026-05-08, SEC accession
  `0001769628-26-000222`) goes further and **anonymizes all customers as
  "Customer A/B/C/D."** No 2025 or 2026 article was found stating a
  current or historical Microsoft-specific percentage despite 6+ RSS
  query variants. **This looks like a deliberate disclosure retreat —
  named concentration risk became anonymized labels as the customer base
  diversified (OpenAI, Meta, Anthropic, Jane Street) — which is itself
  the story, even without the missing number.** (gap, flagged rather than
  filled with a stale figure.)

## 3. The debt stack

| Instrument | Amount | Terms | Date | Confidence |
|---|---|---|---|---|
| Senior unsecured notes | $1.5B | Moody's B1 / CoreWeave corp. family Ba3 | 2025-05-19 | medium |
| Convertible + senior notes | $4B convertible + $1.75B senior | senior notes yield **9.75%** | 2026-04-14 | thin |
| Add-on senior notes | $1.0B | 9.750% due 2031, priced at 102% | 2026-04-21 | thin |
| Data-center SPV junk bond (GPU-collateralized, not corporate debt) | $900M | — | 2026-06-02 | thin |
| Sought loan facility | $8.5B | — | 2026-02-25 | thin |
| USD + EUR senior notes | $1.25B + €2B | first US AI issuer to sell euro junk bonds | ~2026-06-11 | medium |
| Aggregate debt (analyst estimate, not filed) | ~$25B | — | ~May 2026 | thin |

**Credit commentary:** "Moody's flags Oracle and CoreWeave as AI's weakest
credit link" (Bitget, 2026-07-25 — thin, single outlet, but directionally
consistent with §4). Total aggregate debt outstanding could not be
confirmed from a primary filing this crawl (EDGAR 10-Q text not
independently reconciled to a single total) — flagged gap.

## 4. The AI-credit repricing (macro context, same week as this crawl)

- "Nvidia's credit risk now exceeds Google's as CDS spreads widen to 69
  basis points" — Crypto Briefing, **2026-07-27** (thin, single outlet).
- "Concerns mount over Nvidia's revolving financing: CDS spreads surge to
  record highs, shares plunge 5%" — Futu, **2026-07-27** (converges with
  the above — medium).
- "Nvidia's debt protection costs surge on $750B AI infrastructure
  spending wave" — Crypto Briefing, 2026-07-27 (thin).
- "Bond market anxiety is growing over AI capex budgets" — CNBC,
  **2026-07-24** (medium, primary-tier outlet, title-level).
- "Tech credit risk rises as Oracle CDS hits cycle high, Nvidia spreads
  widen" — Seeking Alpha/MSN, 2026-07-20/21 (2 converging — medium).
- "Big Tech's $182 Billion AI Debt Spree" — Benzinga, 2026-07-16 (thin).

**Read:** 5+ independent outlets clustered **2026-07-16 through
2026-07-27** — the week immediately before this crawl — converge
directionally on AI-infrastructure credit anxiety and specifically Nvidia
CDS widening. No single primary CDS data source was fetched, so exact
basis-point figures stay thin, but the timing and direction are
well-corroborated (medium overall). This is the exact macro backdrop
CoreWeave's 9.75%-coupon, GPU-collateralized debt stack sits inside.

## 5. The failed $9B Core Scientific deal, and the capacity "plan B"

- **Deal announced 2025-07-07:** ~$9B all-stock acquisition of Core
  Scientific (bitcoin miner turned datacenter operator) — CNBC/Yahoo
  Finance same-day, WSJ had reported talks 2025-06-26 (high confidence).
- **Opposition:** Core Scientific's largest shareholder, later identified
  as **Two Seas Capital**, said it would vote against as early as
  **2025-08-07** (Reuters), citing material undervaluation. **ISS**
  recommended against 2025-10-20; **Glass Lewis** joined 2025-10-21 (PR
  Newswire) — medium-high, converging across Reuters/PR Newswire/Yahoo
  Finance/a Jefferies note (2025-10-29).
- **Rejected 2025-10-30:** shareholders voted the deal down; Core
  Scientific announced termination the same day, confirmed by its own
  release plus Reuters, Bloomberg, WSJ, Investor's Business Daily (high
  confidence on the fact/date). **Exact vote tally not found** despite
  targeted searches — flagged gap. Reason cited was valuation/dilution
  concern from the activist holder and both proxy advisors, not
  explicitly named as "dilution" in any single source but the implied
  mechanism of an all-stock deal priced too low.
- **Plan B, reconstructed:** the deals genuinely *after* the 2025-10-30
  rejection are thinner and later than the brief implied:
  - **BCE (Western Canada)** data-center partnership, **2026-03-16**
    (Bloomberg).
  - **Conapto (Sweden)**, two-site deal, **2026-06-24** (Blockspace
    Media — thin, single outlet).
  - **EdgeConneX / Cedar Creek, TX** — **2026-07-27**, a $440M campus
    commitment inside a $2.2B Bastrop County project, corroborated by 3
    outlets (Data Center Dynamics, Business Journals, Community Impact —
    high).
  - **A separate 2GW Texas deal with Poolside (~$4B) was actually
    *terminated***, reported 2026-04-04/28 (MLQ.ai, tech-insider.org —
    thin) — CoreWeave *retreating* from a capacity commitment, the
    opposite of what "plan B" would predict.
  - **Gap within the gap:** no new-capacity announcement surfaced in the
    ~4.5 months immediately after the rejection (Nov 2025–Feb 2026);
    coverage in that window was dominated by shareholder-lawsuit /
    securities-litigation news (Pomerantz, GlobeNewswire investor
    notices), not new deals. The first confirmed post-rejection capacity
    move is the March 2026 BCE/Canada deal.

## 6. Nvidia's actual stake in CoreWeave (not Nebius's 9.3%)

- CoreWeave's own **10-Q and S-1 do not name a Nvidia ownership
  percentage.** No SC 13D/13G exists for Nvidia's CoreWeave position
  (confirmed via EDGAR full-text search, zero hits) — Nvidia discloses it
  via **13F-HR**, consistent with a passive/institutional-style stake
  rather than an activist one.
- **Nvidia's 13F-HR filed 2026-05-15** (EDGAR CIK 0001045810, accession
  `0001045810-26-000042`) is the underlying filing every outlet cites for
  a **~94.5% increase** in Nvidia's CoreWeave position that quarter.
- The **~11%** ownership figure circulating (IndexBox, 2026-05-19, and
  independently derived in similar form by TradingView/CryptoRank/
  foreignpolicyjournal.com/TipRanks, all 2026-05-16/19) is a **journalist
  calculation** (shares ÷ shares outstanding), not a number stated
  directly in the 13F — 13F filings disclose share count/dollar value,
  not percentage ownership. Treat **~11%** as medium confidence: the
  underlying filing is real and directly identified, but the percentage
  itself is a derived estimate, not a primary-source-stated figure.
- Earlier reference points along the way: Nvidia held **$900M** in
  CoreWeave stock per a March 2025 filing (CNBC, 2025-05-15 — medium);
  reframed as a **"$1.7B win"** by Barron's, 2025-05-19 (thin).
- **No explicit "vendor financing" or GPU-buyback language found** in any
  source — the reciprocal-capital loop (Nvidia invests equity, Nvidia
  sells CoreWeave GPUs, including a disclosed $6.3B order, §2) is
  structurally suggestive but not confirmed as a formally reciprocal
  arrangement. Flagged gap.

## 7. Q1 2026 earnings and next earnings date

- **Revenue:** **$2,078M ($2.08B)**, +112% YoY — confirmed directly from
  CoreWeave's own **10-Q** (SEC EDGAR, CIK 1769628, accession
  `0001769628-26-000222`, filed 2026-05-08) — high confidence.
- **Net loss: $740M** for the three months ended 2026-03-31, per the same
  10-Q — up from a **$315M** net loss on **$982M** revenue in Q1 2025 (the
  loss more than doubled YoY even as revenue guidance disappointed and
  the stock fell **10%** on the print, CNBC, 2026-05-07). High confidence
  (primary source, corroborated independently by 24/7 Wall St.,
  2026-05-29).
- **CapEx guidance:** figures cluster **$30–34B** for full-year 2026
  across several outlets reporting at different points as guidance was
  revised upward through the year (tech-insider.org $30B, 2026-04-01;
  TechStock² $34B, 2026-07-20) — medium on the general range, thin on any
  single precise number.
- **Next earnings date: Tuesday, 2026-08-11, 5:00 PM ET** — a Business
  Wire release ("CoreWeave Announces Date of Second Quarter 2026
  Financial Results and Conference Call," 2026-07-27) republished
  verbatim by stocktitan.net, independently corroborated by Benzinga's
  CRWV earnings page (which also lists consensus estimates: EPS −$1.27,
  revenue $2.56B). Medium confidence — two independent sources, one
  quoting the release directly, but not fetched from CoreWeave's own IR
  page (DNS/404 issues persisted all session).

## 8. IPO context

- **IPO date: 2025-03-28**, priced at **$40/share**, initial valuation
  **~$23B** (CNBC — "biggest U.S. tech IPO since 2021," high confidence,
  multiple converging outlets across the whole timeline).
- Performance arc (RSS-title level, individually thin-to-medium but a
  coherent converging shape): shares rose past IPO price within days
  (2025-04-01, Reuters); up **250%** since IPO by June 2025 (Yahoo
  Finance); wiped out **33% in two days** 2025-08-15 (TradingView); up
  **322%** since IPO by October 2025 (24/7 Wall St.); WSJ ran "Staggering
  Fall From Market Grace Highlights AI Bubble Fears," 2025-12-15; founders
  reported to have "dumped $2.3B in stock since IPO," 2026-06-09 (Crain
  Currency).
- **Current state (as of 2026-07-28):** trading around **$71/share**,
  market cap **"slipped under $50B"** — a cluster of converging RSS
  titles 2026-07-13 through 2026-07-28, including CFO share-sale
  disclosures on 2026-07-22 and 2026-07-28 (Globe and Mail) — medium
  confidence (no single primary stock-quote fetch, but a consistent
  dated cluster).

---

## Gaps to flag explicitly (nothing fabricated)

- No Q2 2026 backlog/earnings figures yet — not reported as of
  2026-07-28; call is scheduled 2026-08-11.
- Microsoft's specific % share of CoreWeave revenue — never found for any
  year; CoreWeave's own disclosure moved from a named-but-unattributed
  "77% from top two customers" (S-1, FY2024) to fully anonymized
  "Customer A–D" labels (Q1 2026 10-Q). The disclosure shift itself is
  the finding.
- Exact Core Scientific shareholder vote tally/percentage — not found.
- The ~11% Nvidia stake figure is a derived/journalist estimate from a
  real 13F filing, not a primary-source-stated percentage.
- No formal "vendor financing"/GPU-buyback arrangement between Nvidia and
  CoreWeave confirmed, despite the structural suggestiveness of the
  equity-stake-plus-$6.3B-order pattern.
- A ~4.5-month dead zone (Nov 2025–Feb 2026) with no visible new-capacity
  deal after the Core Scientific rejection — plausibly explained by
  shareholder-litigation distraction, but not confirmed either way.
- Total aggregate CoreWeave debt outstanding not reconciled to one
  filed figure this crawl.
- Government/DoD contracts: none found.

**Method note:** direct fetches of CoreWeave's own IR site
(`ir.coreweave.com`), Reuters, CNBC, and several SEC full-text document
bodies were frequently blocked (403/DNS failure/404) this session;
figures rated below "high" above are RSS-title-derived rather than
confirmed against full article/filing text. Three items — Q1 revenue,
Q1 net loss, and the S-1's 77%-top-two-customers disclosure — were
confirmed by directly fetching CoreWeave's own SEC filings (10-Q and
S-1) and are the crawl's strongest-sourced claims.
