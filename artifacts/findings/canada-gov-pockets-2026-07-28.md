---
wave: canada-gov-pockets
kind: crawl-finding
date: 2026-07-28
bundle: artifacts/bundles/canada-gov-pockets-2026-07-28/
method: >
  WebSearch treated as exhausted (session-shared budget). Four sonnet
  subagents ran WebFetch sweeps in parallel: (1) federal AI strategy +
  Strategic Innovation Fund, (2) CIFAR/Vector/Mila/Amii institute funding,
  (3) provincial pools (Ontario/Quebec/Alberta/BC) incl. health-system AI,
  (4) CIHR + the 2025/2026 federal budget. Sources: Google News RSS
  (news.google.com/rss/search), canada.ca/ised-isde.canada.ca,
  budget.canada.ca, cifar.ca/vectorinstitute.ai/mila.quebec/amii.ca,
  provincial gov sites, BetaKit (the strongest-resolving Canadian tech
  outlet this session). Several primary sites rejected the fetcher outright
  (cihr-irsc.gc.ca — persistent TLS handshake failure; GC InfoBase/Main
  Estimates — blocked). Google News RSS redirect links mostly did not
  resolve to article bodies (JS shell) — cited via feed metadata
  (title/outlet/date) where so, marked medium rather than high confidence.
  Nothing fabricated; explicit gaps marked (thin) or "not found."
---

# Canada government AI/health capital pockets (2026-07-28)

*Backward crawl of Canadian public capital pools relevant to AI +
health/mental-health — the Canada half of ROADMAP row 23 ("Government
funding pockets"). Companion to a US-federal-pools crawl (separate). Bundle:
`artifacts/bundles/canada-gov-pockets-2026-07-28/`.*

**The throughline:** Canada has committed real money to AI
infrastructure — federally `$2B`+ (Dec 2024 sovereign-compute strategy,
possibly another `$2B`+ under the Carney government's June-2026 "AI for
All" strategy, overlap with the 2024 figure unresolved) plus `$925.6M`
newly appropriated in the Nov-2025 federal budget — and provincially,
Alberta (`$50M`/5yr) and Quebec (`$36M` via Mila) have made their own
moves. Almost none of this money has an explicit health angle, and where
AI has actually reached the public health system this year the two
clearest signals are a **success** (Amii's Alberta Health Innovation Lab,
`$10M`) and a **failure** (Ontario's auditor general finding that
government-approved AI medical scribes hallucinate). Mental health
specifically got the opposite of a funding story: the Nov-2025 federal
budget's own coverage flagged **no new money for mental health or
substance-use programs**, even as AI infrastructure lines grew.

---

## 1. Federal AI strategy / Sovereign Compute Strategy

- **`$2B CAD`** Sovereign AI Compute Strategy, announced 2024-12-05:
  `$1B` public supercomputing infra ($200M augmenting existing
  NRC/institute/Digital-Research-Alliance facilities + `$800M` for a new
  large sovereign supercomputer), `$700M` for commercial AI data centres
  (delivered via SIF's "AI Compute Challenge"), `$300M` "AI Compute Access
  Fund" for SMB compute access (opened 2025-03).
  (https://betakit.com/federal-government-outlines-2-billion-in-ai-compute-spending-commitment/, 2024-12-05)
- **AI Compute Access Fund disbursement**: `$66M` of `$300M` paid out to 44
  SMB recipients as of 2026-05-12 — subsidy model (50-67 cents per compute
  dollar), fund described as **oversubscribed**; **`$234M` still
  uncommitted**.
  (https://betakit.com/feds-announce-66-million-for-44-businesses-through-ai-compute-access-fund/, 2026-05-12)
- **Cohere deal**: up to `$240M CAD` toward Cohere's `$725M` compute
  buildout (with CoreWeave/Nvidia) — the first investment under the
  Sovereign Compute Strategy, structure (grant/loan/equity) unspecified.
  (https://betakit.com/cohere-secures-federal-backing-to-build-multibillion-dollar-canadian-ai-data-centre/, 2024-12-06)
- **"AI for All" strategy**: Carney government launched a new national AI
  strategy 2026-06-04 promising "over `$2B`" more, targeting 250,000 jobs
  by 2031, plus a new investment/startup fund taking equity stakes in AI
  firms. **(thin — could not confirm whether this is incremental to or
  restates the 2024 `$2B`)**.
  (Google News RSS — CBC/Globe and Mail, 2026-06-01/04)
- **CAISI** (Canadian AI Safety Institute) is referenced in federal
  strategy material but no budget figure located. **(thin, unconfirmed
  size)**. (https://ised-isde.canada.ca/site/artificial-intelligence-strategy/en, fetched 2026-07-28)
- **How-free:** mixed — the SMB-facing `$300M` fund shows real disbursement
  velocity (~22% spent) but most of it remains uncommitted; the two large
  tranches (`$1B` supercomputing, `$700M` data centres) are committed on
  paper but slow to land (partner selection was still pending at
  announcement).
- **AI/health direction:** industrial/compute-infrastructure only.
  Healthcare appears solely as one of several eligible *sectors* for
  Compute Access Fund recipients (energy, manufacturing, agriculture,
  healthcare/life sciences) — no named health recipient, no dedicated
  health line.

## 2. Strategic Innovation Fund (SIF)

- Launched 2017, initial `$1.26B` envelope over 5yr; government claims
  (as of 2025-03) 750+ SMBs supported, `$1.7B`+ investment drawn, 1,200+
  jobs added.
  (https://betakit.com/canada-invests-36-6-million-in-strategic-innovation-fund-technology-networks/, 2025-03-18)
- **`$700M`** of the `$2B` Sovereign Compute Strategy runs through SIF's
  "AI Compute Challenge" as contributions to companies/consortiums/academic
  partnerships (repayable and non-repayable, mix unspecified).
  (BetaKit, 2024-12-05)
- **`$36.6M`** spread across 5 SIF-backed technology networks (clean
  resources, agri-food automation/AI, food innovation, natural products,
  mining) — only the agri-food network is explicitly AI-focused.
  (https://betakit.com/canada-invests-36-6-million-in-strategic-innovation-fund-technology-networks/, 2025-03-18)
- **Rebrand signal (thin, structurally important):** the current
  `ised-isde.canada.ca/site/strategic-innovation-fund/en` page describes a
  **"Strategic Response Fund (SRF)"** that "builds on the success of the
  former Strategic Innovation Fund," with the AI Compute Challenge as one
  of three SRF priorities (alongside tariff response, general innovation).
  Exact transition date and current total SRF envelope not found this
  pass. (fetched 2026-07-28)
- **How-free:** mixed; historically slow to disburse (a 2020-era
  assessment found only `$313M` paid out in the first three fiscal years —
  dated context, not current-state).
- **AI/health direction:** none — purely industrial/sector-diversified, no
  health stream identified.

## 3. CIFAR / national AI institutes (Vector, Mila, Amii)

- **CIFAR / Pan-Canadian AI Strategy** base envelope: **`$441.6M`**
  (Budget 2021, running 2021-22 through 2030-31) — CIFAR's own Talent &
  Research (AI Chairs) slice is `$208M` of that. ISED's strategy page
  (last modified 2026-06-04) still reflects the Budget-2021 figures, no
  further full-strategy renewal found.
  (https://ised-isde.canada.ca/site/artificial-intelligence-strategy/en, fetched 2026-07-28)
- **`$24M`** new federal top-up to the CIFAR AI Chairs program, announced
  2026-05-21 — reporting diverges on scope (BetaKit/PR Newswire: "20 new
  appointees"; Amii's own site: funds "42 CIFAR AI Chair positions across
  Canada" total). Unresolved discrepancy.
  (BetaKit/PR Newswire, 2026-05-21; amii.ca/latest-from-amii, 2026-05-22)
- **Vector Institute** (Ontario): no new public-funding figure found for
  2025-26 beyond its CIFAR-Chairs share. BMO renewed a 5-year partnership
  (2026-05-28) — amount unconfirmed. 100 scholarships to Ontario grad
  students (2026-05-12); Helmholtz Munich MOU (2026-06-11); IPON IP-
  protection partnership (2026-01-07) — none are funding grants.
  **AI/health: none found — the clearest gap of the three institutes.**
- **Mila** (Quebec): Quebec government **`$36M`** to "sustain Mila's AI
  research," part of Quebec's 5-year innovation strategy
  (https://betakit.com/, 2026-02-27). Globe and Mail separately reported
  "Ottawa plans major investment" in Mila — figure unconfirmed, paywalled
  (2026-02-19, thin). Mila is also raising its **own `$100M` fund** for AI
  startups (a venture vehicle, not core research funding; Globe and Mail,
  2026-01-21). **AI/health signal:** Mila + ROOST **suicide-prevention
  guardrail pilot** for AI chatbots — genuine mental-health-adjacent
  research, no funding amount disclosed (mila.quebec/en/news, 2026-07-08,
  thin on $).
- **Amii** (Alberta): Alberta government **`$50M` over 5yr**, spread
  across five provincial ministries (Digital Journal/BetaKit, 2026-07-09).
  **AI/health — strongest signal in the whole institute set:** Alberta +
  Amii **Health Innovation Lab, ~`$10M`**, explicitly building
  AI-enabled healthcare solutions integrated into the provincial health
  system (Calgary.Tech/BetaKit, 2026-05-20/21; confirmed on
  amii.ca/latest-from-amii, 2026-05-20).
- **How-free (all four):** federal CIFAR money is government-restricted,
  multi-year, pillar-tied ("locked"); provincial top-ups (Quebec/Alberta)
  are multi-year grants tied to strategy/ministry mandates ("locked-to-
  mixed"); corporate partnerships (Vector/BMO, Anthropic credits to
  Mila/Amii) are project-tied, smaller, and not government capital at all.

## 4. Provincial pools (Ontario, Quebec, Alberta, BC)

**Ontario**
- **`$4B` "Protect Ontario" investment fund** — announced in the 2026
  provincial budget for AI and other high-growth sectors; province
  searching for an external private-sector manager (direct-investment
  vehicle, not a grant program).
  (The Logic, 2026-03-27; Bloomberg, 2026-03-26)
- Health-system AI item is a **critical audit finding, not a funding
  win**: Ontario's auditor general found most Ontario-approved AI medical
  scribes/note-taking tools used in doctor visits **hallucinated**,
  generating factual errors during testing.
  (CBC, 2026-05-13; The Trillium, 2026-05-12)
- Oracle cloud + AI note-taking reportedly cut Ontario hospital EHR wait
  times 71% — vendor-reported, no dollar figure (Stock Titan, 2026-02-09,
  thin).
- No mental-health-specific AI funding or pilot found.

**Quebec**
- `$36M` to Mila (see above; BetaKit, 2026-02-27).
- **Santé Québec** (provincial health authority) plans a 2026 AI pilot
  focused on clinical-documentation ("notes médicales") — clearest signal
  of AI entering Quebec's public health system directly; no dollar figure
  or mental-health angle found. (La Presse, 2025-08-11, thin)
- Montreal General Hospital hand-hygiene AI alert system — live in-hospital
  deployment, no funding figure, no MH angle. (La Presse, 2026-04-29, thin)
- No dedicated province-wide Quebec AI fund distinct from the Mila
  commitment found.

**Alberta**
- No dedicated Alberta AI strategy fund with a clear size found beyond the
  Amii `$50M`/5yr above. An "updated tech strategy" + new equity-investment
  authority for backing Alberta tech companies announced 2026-04-22/23,
  no dollar figure disclosed (thin).
- Regulatory levy on large-scale AI data centres (a cost imposed, not
  capital deployed) — Calgary Herald, 2025-08-28.
- `$800M CAD` Alberta cancer-care investment with Siemens Healthineers +
  Alberta Cancer Foundation, explicitly including AI-enabled diagnostics —
  strongest Alberta health+AI dollar figure found, but pre-dates the
  preferred 2026 window and is cancer-specific, not mental health.
  (Siemens Healthineers, 2025-03-21)
- AI-scribe pilot in Alberta Health Services emergency departments
  (U of Alberta-led), expanded to three EDs — no funding figure, no MH
  angle. (U of A, 2026-03-02)
- No mental-health-specific AI funding found.

**British Columbia**
- No dedicated BC AI strategy or capital pool found. BC has a Minister of
  State for AI and New Technologies (Rick Glumac, appointed 2025-07) — a
  governance role, not a funding vehicle. (BetaKit, 2025-07-18)
- Adjacent, not AI-specific: InBC/SFU `$20M` strategic investment fund
  (2026-05-12); UVic clean-tech/quantum `$1.9M` fund (2026-02-19).
- **Nothing findable inside BC's public health system** — no hospital,
  health-authority, or mental-health AI item surfaced despite targeted
  searches. BC is explicitly the weakest of the four provinces on both
  counts.

## 5. CIHR + the 2025/2026 federal budget

- **CIHR overall budget:** ~`$1.3B CAD` (FY2023-24 expenses figure,
  Wikipedia infobox — **thin, not a primary CIHR/Treasury Board number**;
  CIHR's own domain returned a persistent TLS error on every fetch this
  session, and GC InfoBase/Main Estimates rejected the fetcher outright).
- **No dedicated CIHR AI-in-health-research funding stream found** —
  multiple targeted searches (CIHR release archive, INMHA institute)
  turned up nothing current (2025-2026); the one AI-competition item found
  was from 2020 and excluded as stale.
- **No mental-health/digital-MH-specific CIHR AI program found** — only
  individual investigator grants surfaced (a CHEO eating-disorder program
  grant, 2026-02; a Sunnybrook ~`$7M` general CIHR award, 2025-08), none
  AI-specific.
- Budget 2025 softened the tri-council (CIHR/NSERC/SSHRC) savings target
  from 15% to 2% — an `$83M`/yr reduction in planned cuts, i.e. an
  overall increase vs. Budget 2024, but ordinary council operations, not
  a new AI or MH line. (Evidence for Democracy analysis, thin/secondary)
- **2025 federal budget (tabled 2025-11-04, Carney govt):**
  - **`$925.6M`** over 5yr (starting 2025-26) for sovereign public AI
    infrastructure — of which `$800M` is *reallocated* from existing
    fiscal-framework funds, not fully new money. AI-infrastructure only,
    no health angle. (https://budget.canada.ca/2025/report-rapport/chap1-en.html)
  - `$25M`/6yr + `$4.5M` ongoing for an AI & Technology Measurement
    Program (StatCan) — not health-related. (same source)
  - `$656.9M`/5yr (ISED) for dual-use tech commercialization spanning
    AI/aerospace/biodefence/life sciences — defence-adjacent, not
    health/MH-specific. (https://budget.canada.ca/2025/report-rapport/chap4-en.html)
  - `$2.3B`/5yr quantum/advanced-tech R&D + `$334.3M` quantum-anchoring —
    no health tie.
  - **Mental health / substance use: no new money.** Multiple outlets
    reported the budget provided **no new funding for mental-health or
    substance-use programs**, and that bilateral MH/substance-use funding
    agreements with the provinces lapse in 2027 with no replacement
    signaled. (The Hill Times, 2025-11-04/10/17, thin — headlines
    confirmed via RSS, full bodies not retrievable this session)
  - Post-budget implementation: "Canada opens applications to build a
    public AI supercomputer" (BetaKit, 2026-04-16); "Feds and TELUS
    advance work to build sovereign AI infrastructure" (ReNew Canada,
    2026-05-13) — the `$925.6M` line moving into execution in 2026.

---

## Per-pool summary table

| pocket | pool | size | how-free | AI/health direction | confidence |
|---|---|---|---|---|---|
| gov-canada | Sovereign Compute Strategy | `$2B` (2024) + possible `$2B`+ more ("AI for All", 2026, overlap unclear) | mixed — `$234M`/`$300M` SMB fund uncommitted; big tranches slow | industrial only; health = eligible sector, no recipient | med |
| gov-canada | SIF / Strategic Response Fund | `$1.26B` base, rebrand-in-progress, current total unclear | mixed — contributions, slow historical disbursement | industrial, no health stream | thin-med |
| gov-canada | CIFAR / Pan-Canadian AI Strategy | `$441.6M` (2021-2030) + `$24M` top-up (2026) | locked — govt-restricted, pillar-tied | general research; no dedicated health envelope | high (base), med (renewal) |
| gov-canada | Vector Institute | no new public $ found 2025-26 | mixed — corporate-partnership-tied | none found | thin |
| gov-canada | Mila | `$36M` (Quebec, 2026) + own `$100M` venture fund | mixed — provincial grant + venture vehicle | MH-adjacent: suicide-prevention guardrail pilot (no $) | med/thin |
| gov-canada | Amii | `$50M`/5yr (Alberta) + `$10M` Health Innovation Lab | locked — provincial, multi-ministry | **strongest health signal** — AI-enabled healthcare buildout | med-high |
| gov-canada | Ontario "Protect Ontario" | `$4B` (2026 budget) | free-ish — direct-investment vehicle | health item = audit failure (hallucinating AI scribes), not funding | med |
| gov-canada | Quebec (Santé Québec pilot) | no $ figure | thin | clearest in-hospital AI deployment signal, no MH angle | thin |
| gov-canada | Alberta (provincial, ex-Amii) | no dedicated fund found; `$800M` cancer+AI (2025, adjacent) | thin | AI scribe pilot in AHS EDs, no $, no MH | thin |
| gov-canada | BC | nothing dedicated found | n/a | nothing found — weakest province | thin |
| gov-canada | CIHR | ~`$1.3B`/yr (thin, FY23-24) | n/a | no AI-in-health stream, no MH-AI stream found | thin |
| gov-canada | 2025 federal budget (AI lines) | `$925.6M` + `$656.9M` + `$2.3B` (various AI/tech, 5yr) | committed but `$800M` of the `$925.6M` is reallocated, not new | AI-infra only; **explicit zero new MH/substance-use money** | med |

## Proposed board structure

- New **`gov-canada` pocket** (parallel to the existing `state-organ`
  pocket already declared in `attention/board.yaml` pockets list but not
  yet populated) — sibling to a future `gov-us` pocket for the US-federal
  half of row 23. Both would sit under a new G2 sector, e.g. `government`
  (member_of nothing, or member_of a future `power`/`infra` cross-link —
  needs Ben's call since these pools fund *other* pockets rather than
  compete with them).
- Candidate `kind: agency` node slugs (not full states — these are
  sub-national/programmatic pools, closer to the `state-organ` rank stub
  than a full `state`):
  - `canada-sovereign-compute` (federal AI compute strategy, incl. AI
    Compute Access Fund + Cohere deal)
  - `canada-sif` (Strategic Innovation Fund / Strategic Response Fund)
  - `cifar` (Pan-Canadian AI Strategy + AI Chairs)
  - `vector-institute`, `mila`, `amii` (already candidate `kind: agency`,
    `parent: cifar` for the funding relationship, `sphere: uk`→n/a, use
    `on`/`fr`/`ab` provincial hints if the sphere enum grows)
  - `ontario-protect-fund`, `quebec-innovation` (Mila is the Quebec proxy
    today — a separate provincial-strategy node may be premature until a
    dedicated Quebec fund beyond Mila surfaces), `alberta-ai-strategy`,
    `cihr`
- **`axes_num` recipe for state/agency pools** (distinct from the
  `weight/thrust/gravity` corporate recipe already piloted):
  - `weight` = total committed/appropriated envelope size (not
    market-cap-like; a program budget), in $B CAD converted or noted.
  - `thrust` = annual disbursement/appropriation *rate* actually landing
    (not the headline multi-year total) — e.g. Compute Access Fund's
    `$66M` disbursed over ~14 months ≈ `$0.06B`/mo run-rate, not the
    `$300M` sticker.
  - `gravity` = size of the third-party ecosystem the pool anchors (e.g.
    number/scale of AI companies, institutes, hospitals dependent on the
    pool) — mostly not estimable yet at this crawl depth; leave
    `est-uncited`/thin rather than fabricate.
  - `optionality`: government pools generally read **locked** (mandate-
    restricted, multi-year, tied to specific pillars/ministries) except
    where structured as a flexible direct-investment vehicle (Ontario's
    `$4B` fund, still seeking a manager, reads closer to **mixed**).

## Thread candidates (1-3)

1. **Ontario AI scribes hallucinate** (health/MH-adjacent) — the
   auditor general's finding that government-approved AI medical
   transcription tools generate factual errors in doctor visits is the
   single clearest health-system-AI story of this crawl, and it's a
   *risk* story, not a funding win — directly relevant to a clinician
   tracking AI/MH quality and safety. (CBC 2026-05-13, The Trillium
   2026-05-12)
2. **Amii's Alberta Health Innovation Lab** (`$10M`) — the strongest
   *positive* government-funded AI-in-health signal found anywhere in
   Canada this pass; worth tracking what it actually ships. (BetaKit/
   Calgary.Tech, 2026-05-20/21)
3. **Budget 2025's AI-vs-mental-health gap** — Canada appropriated
   `$925.6M`+ for AI infrastructure in the same budget that multiple
   outlets reported delivered **zero new money** for mental-health/
   substance-use programs, with bilateral MH funding agreements set to
   lapse in 2027 unreplaced — a directly on-lens "where the priorities
   are" story. (The Hill Times, 2025-11-04/10/17)

## Dated expectations

- **AI Compute Access Fund** — `$234M` of `$300M` still uncommitted as of
  2026-05-12; watch for the next disbursement-round announcement.
- **"AI for All" strategy** (announced 2026-06-04) — watch for the new
  investment/startup fund's actual structure/launch, and whether its
  claimed `$2B`+ is confirmed as incremental to the 2024 Sovereign
  Compute Strategy or a restatement of it.
- **SIF → Strategic Response Fund** — watch for an official rebrand date
  and a confirmed total SRF envelope (not found this pass).
- **Santé Québec AI pilot** (clinical documentation, flagged for 2026) —
  watch for results/expansion and whether a dollar figure surfaces.
- **Bilateral federal-provincial mental-health/substance-use funding
  agreements** — lapse in 2027 with no replacement signaled as of the
  Nov-2025 budget; watch the 2026 fall fiscal update / next budget for
  whether this gets addressed.
- **CIFAR AI Chairs scope discrepancy** ("20 new appointees" vs "42
  positions across Canada") — unresolved; watch for CIFAR's own
  authoritative count.
