# TSMC Capacity Race — the chokepoint's backstory (Jan-Jul 2026)

*Crawl date: 2026-07-28. Backward crawl answering: how did TSMC's 2026 sit
turn into a $60-64B capex year with a $265B US commitment, and is capacity
landing fast enough for the AI order book that's already booked years out?
Bundle: `artifacts/bundles/tsmc-capacity-race-2026-07-28/`.*

Method note: WebSearch was treated as exhausted (session-shared budget
spent by earlier same-day sweeps); three parallel sonnet subagents ran
WebFetch against Google News RSS search feeds, TSMC/NIST primary
documents, TrendForce (several direct full-body fetches succeeded — the
best-resolving outlet this session), and Wikipedia's TSMC article as a
dated-timeline spine. Most Google News RSS redirect links did not resolve
to article bodies via WebFetch (JS shell only) — where that happened, the
citation is the RSS feed item itself (title/source/date from feed
metadata), marked **medium** confidence rather than **high**. Nothing
below is fabricated; gaps are marked **(thin)** or **not found** rather
than guessed.

---

## 1. Capex trajectory — from $52-56B to $60-64B

TSMC's 2026 capex guidance climbed in one significant step this year, not
a gradual creep:

- **2026-01-20 (Q4 2025 earnings call)** — original 2026 guidance set at
  **$52-56B**, up from ~$40B actual 2025 capex; this is the first and only
  lower starting figure found — no earlier/smaller 2026 number turned up
  anywhere in this crawl. Reported same week by TrendForce, Yahoo Finance,
  Wccftech (RSS metadata, 5+ convergent outlets). (medium)
  - CEO C.C. Wei reportedly voiced open nervousness about overbuilding —
    Barchart headlined him "'I'm Also Very Nervous'" the same week — quote
    text itself not independently verified (headline/fragment only).
    (thin)
- **2026-04-16 (Q1 2026 earnings call)** — guidance held at $52-56B but
  pointed toward the **top of the range**; revenue growth guidance raised
  toward **30%+** for the year (Reuters, SCMP, Bits&Chips — RSS metadata,
  convergent). (medium)
- **2026-07-16 (Q2 2026 earnings call) — the big raise.** TrendForce
  (direct full-body fetch, high confidence): 2026 capex lifted **15% to
  $60-64B**; full-year revenue growth guidance raised to **"over 40%"**
  (from ~30%); Q3 2026 revenue guidance **$44.6-45.8B** (~37% YoY); Q3
  gross margin guidance **65-67%**, operating margin **56-58%**. Margin
  drags named explicitly: **N2 (2nm) ramp costing 3-4 points**, overseas
  fab expansion costing **2-3 points now, widening to 3-4 points**.
  Q2 net profit **+77% YoY to a record NT$706.6bn (~$22B)** (Wikipedia,
  convergent with the primary figures). (high)
  - Same call: CEO/Chairman C.C. Wei said AI demand would run **"through
    2030"** — three independent outlets (biggo.com ×2, The Loadstar,
    Nikkei Asia referenced) converge on "2030" specifically; exact
    verbatim quote not independently retrieved. (medium) *(Note: the
    thread's seeded watch line says "2029-2030" — this crawl found
    convergent sourcing for "through 2030," not a 2029 endpoint; treat
    "2030" as the better-sourced figure going forward.)*
  - Despite the beat-and-raise, **TSM shares fell ~5%** on margin-dilution
    and capex-spend concerns (3+ convergent outlet headlines). (medium)
- **Forward analyst chatter:** a pre-earnings estimate (2026-07-05,
  finance.biggo.com) had pegged **2027 capex at $78B** — this is an
  analyst forecast, not company guidance, flagged as such. (thin)

**Pricing power — the 2027 hike:**

- **2026-07-21** — TSMC in talks to raise **baseline prices 5-10%** on
  advanced nodes for 2027, with **AI-order/HPC surcharges up to 25%**
  (Bloomberg/Nikkei sourcing, Tom's Hardware). A company spokesperson
  reportedly confirmed the decision is **"not opportunistic"** and that
  **mature nodes are also covered**, not just leading-edge (Wccftech).
  TrendForce (2026-07-22) names **Apple and Nvidia specifically** as the
  customers "in focus" for HPC premiums. Digitimes frames the hike as
  handing **Intel Foundry** fresh pricing room competitively. One outlet
  ties the hike explicitly to **overseas (Arizona/Japan) cost dilution**.
  (medium, multi-outlet convergent on the headline figures; verbatim
  spokesperson quote not independently re-verified)
- **Not found:** any direct Nvidia/Apple/AMD statement reacting to the
  price hike — only editorial speculation that Apple "will feel it."
- **Not found:** an explicit dollar/percentage breakdown of how much of
  the $60-64B goes to advanced packaging (CoWoS) vs. wafer capacity.

---

## 2. The global buildout — Arizona, Japan, Germany, Taiwan

**Arizona — the big one.** TSMC's US commitment has now roughly doubled
in under three years: $65B (2024, CHIPS-era) → $165B (mid-2025) →
**$265B (2026-07-16)**, the last jump a fresh **+$100B** announced the
same day as the Q2 earnings call. NIST's own press release (direct
fetch, high confidence) quotes it as covering **"12 leading edge
semiconductor and packaging facilities"** in the US — but the NIST page
does not break out the fab-vs-packaging split or give a per-facility
timeline, and no other source in this crawl filled that gap. Reuters,
CNBC, AP, SCMP and others confirmed the headline figure same-day
(convergent, medium-high).

- Tom's Hardware headlines the add as **"at least four more 2nm fabs"**
  in Arizona; azcentral and AZ Family both independently report "four
  more" Arizona plants — but this is pre-July's more precise 12-facility
  US-wide framing, and the exact node assigned to each of the (up to)
  four new AZ fabs beyond Fab 2 was **not found**. (medium)
- **Fab 2 specifically** — TrendForce (2026-03-24, pre-dating the $100B
  add): targeted for **3nm mass production in 2H 2027**, with "four US
  fabs fully booked" already at that point. (medium)
- A. **A16** process was committed to Arizona back in 2024-11 (CHIPS
  finalization); a **packaging plant** in Arizona is separately targeted
  to open **by 2029** (Reuters, 2026-04-22). TSMC is also deploying an
  additional **$20B into its Arizona subsidiary** (2026-05-13). Apple
  was reported buying **100M+ chips from the Arizona fab** by end of
  2025 (2026-02-25). Local coverage flags **water and labor challenges**
  as live friction on the build (Taipei Times, 2026-05-12). (all medium)

**Japan — Kumamoto (JASM), a bumpier arc.** Fab 1 opened Feb 2024 and
moved to commercial production (12/22/28nm) by Dec 2024, swinging to
**profit in Q1 2026** (Taipei Times/Focus Taiwan, 2026-05-16/18). Fab 2
had a genuinely rocky year-plus: originally targeted 2027, reportedly
**delayed to 2029** amid weak auto demand (mid-2025), then **paused** in
Dec 2025 while TSMC weighed upgrading it from a mature node toward
N4/N5 or even 2nm. By **2026-02-06**, convergent reporting (Financial
Times, TrendForce direct-fetch, digitimes) settled on an **upgrade to
3nm** — TrendForce's own figure: Taiwan's Ministry of Economic Affairs
puts sub-5nm production at **~85% Taiwan / 15% US by 2030**, noting that
even factoring in Kumamoto Fab 2's 3nm, the overseas share moves "only
1-2 percentage points." Taiwan's government formally approved the 3nm
upgrade **2026-04-01** (Reuters/Taipei Times), with launch now targeted
for **2028**. No third JASM fab was found anywhere in this crawl — it's
Fab 1 (operating, profitable) plus Fab 2 (upgraded, 2028 target), full
stop. (medium-high, TrendForce items direct-fetched)

**Germany — ESMC Dresden, on a slower, steadier track.** JV with Bosch,
Infineon and NXP announced 2023-08 (TSMC €3.5B into a €10B+ factory,
German government €5B); groundbreaking 2024-08; still a **specialty
node** build (12/16/22/28nm), not leading-edge. TrendForce (2025-11-20)
had the fab entering structural build with **equipment move-in targeted
2H 2026**; Wikipedia gives a **2029** full-operational target and 40,000
12-inch-wafers/month eventual capacity. Infineon separately confirmed
plans to build RISC-V auto MCUs there, mass production **2028**. An
exact mid-2026 construction-completion percentage was **not found**.
(medium)

**Taiwan — still where the leading edge lives.** N2 (2nm) hit mass
production by end of 2025 (The Straits Times), with the Kaohsiung fab
reportedly reaching 2nm trial production ahead of schedule and **A14**
already under evaluation there (Oct 2025). TrendForce (2025-11-25 /
2026-02-23) reports TSMC accelerating domestic expansion further — up to
**10 fabs under construction or starting in 2026**, an **NT$900B**
investment tied to a reported 3-more-fab 2nm push. The roadmap update
(GIGAZINE, 2026-04-23) named **A12, A13, N2U** as upcoming nodes and
notably **postponed A16 (1.6nm) to 2027** from earlier late-2026
framing. Hsinchu's Baoshan site is confirmed (Space Daily, 2026-06-26)
as the current most-advanced-node home. Nvidia's Jensen Huang publicly
pushed back on a "40% of Taiwan capacity moving to America" framing
(2026-01-13/14), calling US fabs additive, not substitutive — explicitly
protecting the "silicon shield" framing. A Taiwan minister reportedly
said the **US is unlikely to match Taiwan's capacity** (Taipei Times,
2026-07-02) — full text of that claim did not resolve; worth a direct
follow-up fetch. (medium, several items direct-fetched via TrendForce)

**The split, as best sourced:** **~85% Taiwan / 15% US for sub-5nm by
2030** (Taiwan MOEA estimate via TrendForce) is the clearest hard number
found; a looser **~20% overseas share of total capacity (all nodes) by
2028** was referenced in the same piece but not independently sourced.
No single current-year (2026) overseas-percentage figure was found —
only forward estimates for 2028/2030.

---

## 3. The AI order book — booked years out, packaging is the pinch point

**CoWoS/advanced packaging remains the binding constraint**, not raw
wafer capacity, across this whole crawl:

- Nvidia alone reportedly had **over half of 2026-27 CoWoS capacity
  booked** as of Dec 2025 (Digitimes/Wccftech, convergent). Nvidia's
  Rubin Ultra is reported sticking to a dual-die design specifically
  *because of* TSMC packaging constraints (TrendForce, 2026-04-01).
  Broadcom flagged TSMC packaging capacity as a live supply constraint
  on its own earnings calls (Reuters/Astute, 2026-03-24/31).
  Digitimes/TrendForce put advanced-packaging output growing at a rough
  **80% CAGR**, with the CoWoS supply-demand gap reportedly narrowing
  from **20% to 10% by end-2026** (TrendForce headline figure, body not
  resolved). Dataconomy (2026-03-31): TSMC's advanced-chip capacity
  "booked out through 2028." (all medium — RSS/headline-level, several
  convergent)
- TSMC is adding dedicated packaging sites: **three new packaging fabs
  in Chiayi Science Park Phase II** confirmed by a Taiwan minister
  (2026-07-12/13), plus a **long-term Amkor partnership** to build out
  US advanced packaging (2026-06-16, expanded 2026-07-24 with a
  Nvidia-Amkor $1.5B piece). The Arizona packaging plant (targeted 2029,
  above) is the US anchor for this. (medium)

**Customer queue and the Apple-Nvidia handoff:** Nvidia is now widely
reported to have **overtaken Apple as TSMC's single biggest customer**
(Wccftech, 2026-02-27), with some reporting that Apple lost priority-
shipment status as a result (2026-01-20) — though a same-week counter-
report claims Apple still secured "historic" exclusive 2nm access for
the A20 Pro (contradiction flagged, not resolved; both RSS-title level,
thin-to-medium). What is better corroborated: N2's first customer list —
**Apple, AMD, Nvidia, MediaTek** (notably **not** Intel) — roughly 15
early customers, 10 of them HPC-class, confirmed across 3 outlets
(Sept 2025). Apple had earlier secured roughly **half of 2026 2nm
capacity** for the iPhone 18/A20 generation (MacRumors, Aug 2025). AMD's
MI400/Instinct MI455X and the Helios rack launched on **N2 (CDNA5)** at
Advancing AI 2026 (2026-07-22/23) — AMD's first AI-GPU generation on
TSMC's 2nm node. Steep 2nm pricing (reportedly **~$30K/wafer**) is cited
as a reason Nvidia/Apple might explore Samsung's GAA process as a
hedge (Wccftech, 2026-06-15) — worth watching as a competitive-pressure
signal, not a confirmed defection. (medium throughout)

**Advanced-node share:** the ~90%+ figure carried on the board is an
**internal anchor, not independently re-verified this crawl** — the
closest fresh 2026 datapoint is Counterpoint's industry-wide claim that
advanced nodes (<7nm) will be **60% of all foundry shipments** in 2026
(not TSMC's share of that segment specifically). TSMC's overall foundry
share was independently corroborated at **70.2%** (Tom's Hardware,
citing Q2 2025 data). **Not found:** any 2026-dated source giving TSMC's
specific numeric share of the sub-7nm segment — treat the board's ~90%+
figure as carried-forward, not freshly confirmed. (medium/gap flagged)

---

## 4. China and geopolitical exposure

The China thread ran in two directions this year — both **US easing** and
**new friction**, plus a live "silicon shield" debate:

- **US tool-export policy loosened, twice.** A "fast-track"/VEU waiver
  letting TSMC ship US chipmaking tools into its Nanjing (China) fab was
  formally revoked in **Sept 2025** (broad 7+ outlet convergence, high
  confidence) — TSMC called it a "near-term operational risk" but said it
  retained "global advanced capacity for Chinese clients" outside Nanjing
  (TrendForce, Dec 2025). Then, **Jan 1-2, 2026**, the US restored
  continuity via a new **annual tool-import license** for TSMC's Nanjing
  fab (5 convergent outlets: Reuters, SCMP, Taiwan News, Tom's Hardware,
  Tech in Asia — high confidence), alongside similar approvals for
  Samsung and SK Hynix. TrendForce's 2025 full-year breakdown
  (2026-03-02) found **China (Nanjing) was TSMC's most profitable
  overseas unit** that year — ahead of a newly-profitable Arizona and a
  still-loss-making Japan.
- **New friction, mid-2026.** Taiwan itself began weighing **curbs on
  AI-chip exports to China** to align with US policy (Taipei Times/Yahoo
  Finance, 2026-06-09/10) — TSMC shares slipped on the news despite
  strong May sales growth, explicitly flagged as "China exposure and
  valuation in focus." US lawmakers separately pushed for tighter rules
  on TSMC supplying Chinese firms via overseas shell-company loopholes
  (2026-06-08/10). Then, in a notable reversal of direction, **China
  itself was reported weighing tighter controls that would ban local
  Chinese companies from using TSMC** (FT via Tech Times/Tom's Hardware,
  2026-07-21/22) — i.e., friction is no longer purely US-outbound.
  (medium throughout, several multi-outlet convergent)
- **Silicon-shield debate reopened.** Coverage around a Jan 2026
  US-Taiwan semiconductor deal explicitly reopened the "shield" framing —
  CNBC asked what the deal means for it, WSJ wrote TSMC "charting a
  future beyond Taiwan," and SCMP ran the pointed "Taiwan has just sold
  out TSMC and half its chips industry to the US" (all 2026-01-18,
  3-outlet convergent, medium). A recurring cross-outlet theme (MIT Tech
  Review, Lawfare, The Telegraph — thin, undated aggregation) argues the
  shield is structurally weakening *because of* the overseas buildout
  diluting Taiwan's unique leverage — set against Jensen Huang's public
  pushback (above) that overseas capacity is additive, not substitutive.
  Analyst pieces continue modeling the scale of a Taiwan-crisis shock
  (Bloomberg's "$10 Trillion Fight," Chatham House comparing it
  unfavorably to a Hormuz disruption) — none dated to a new 2026 event,
  more a standing background risk being repeatedly re-priced.

---

## What to watch

- **Q3 2026 earnings** — does the $60-64B hold, or does it climb again;
  does the margin dilution from N2 ramp + overseas expansion (3-4 points
  each, per TrendForce's Q2 breakdown) start biting harder as more
  overseas fabs go live.
- **The 2027 price hike finalizing** — 5-10% baseline / up to 25% AI
  surcharge is still "in talks" as of this crawl; watch for the actual
  contract terms and any customer (Nvidia/Apple/AMD) pushback once real.
- **Arizona's per-facility node assignments** — the 12-facility, $265B
  framing has no public fab-by-fab breakdown yet; this is the single
  best next-crawl target to sharpen the AZ picture.
- **Kumamoto Fab 2's 2028 target** — this project has already slipped
  and changed node once; worth checking whether the 3nm-by-2028 date
  holds.
- **The advanced-node share number** — the board's ~90%+ <7nm figure
  needs an independent 2026 source; this crawl could not find one.
- **China's reported ban-on-local-use idea (2026-07-21)** — thin, single
  cluster of reporting; confirm or drop on the next pass.
