---
wave: us-gov-pockets
kind: crawl-finding
date: 2026-07-28
bundle: artifacts/bundles/us-gov-pockets-2026-07-28/
method: >
  ROW 23 (US half) — four parallel research sweeps (CHIPS+DOE · DARPA+DoD AI
  · NIH+BARDA+WISeR · NSF+July sweep), each via WebFetch against Google News
  RSS / DuckDuckGo-Bing HTML / agency sites / SEC EDGAR / CRS, since the
  session's WebSearch budget was already exhausted (200/200) before any of
  the four sweeps ran a query — a recurring, cross-sweep constraint, not a
  one-off. Several primary docs (DARPA's FY26 Master Justification Book, a
  CRS BARDA report, ASPR's budget-in-brief) were located but returned as
  unparseable PDF byte-streams or 403/404'd — those gaps are flagged inline
  per pool rather than papered over. Confidence is per-pool, not uniform:
  CHIPS/NIH/NSF/WISeR rest on primary or multi-outlet-converged sources;
  BARDA and DoD AI's exact dollar figures are thin throughout.
---

# Finding — US federal AI-funding pockets: where's the money (2026-07-28)

**The throughline:** every pool in this crawl is running the SAME fight —
an executive branch trying to redirect or shrink appropriated science/health
money (NIH indirect-cost cap, NSF directorate clawbacks, BARDA mRNA
cancellations, mostly-zeroed CDAO line items) against a Congress that keeps
restoring it on paper — while a SEPARATE, much less contested track (CHIPS
equity stakes, DOE nuclear loans, the new Genesis Mission) is aggressively
standing up NEW AI-adjacent capital, mostly via loans/equity/OTA
mechanisms that dodge the standard appropriations fight entirely. The
"how free" axis is not one number per agency — it's two competing vectors
(statutory topline vs. administrative throttle) that this crawl had to
report separately.

---

## 1. CHIPS Act (Commerce) — `chips-act`

**Size:** $52.7B total appropriation ($39B manufacturing incentives + $11B
R&D/workforce) plus $75B in loan/guarantee AUTHORIZATION (not a direct
appropriation) — Wikipedia/CRS-derived, confirmed. As of Jan 2025: **19
companies funded, $30.7–30.9B in direct awards + $5.5B in loans** across 40
fab projects (marklapedus.substack.com aggregation — thin, not a primary
Commerce dataset, but the company table below is internally consistent):
Intel $7.86B · TSMC $6.6B · Micron $6.165B · Samsung $4.745B · GlobalFoundries
$1.5B · Texas Instruments $1.61B · SK hynix $458M · GlobalWafers $406M ·
Amkor $407M · smaller recipients ~$1.3B+. Disbursement is **milestone-gated
through 2028** — no clean current unobligated-balance figure exists
publicly (thin).

**How-free:** the defining 2025 event is the **grants-to-equity pivot**.
Commerce Secretary Lutnick pursued converting CHIPS grants into equity;
**Intel's conversion is the only CONFIRMED executed case** — 9.9% stake,
$8.9B ($5.7B remaining CHIPS grant + $3.2B Secure Enclave), 433.3M
non-voting shares, closed 2025-08-26 (see `artifacts/findings/intel-rescue-2026-07-28.md`
for the full deal mechanics — not re-derived here). Whether the same
mechanism was applied to **TSMC/Micron/Samsung** is a live SOURCE CONFLICT:
Trendforce (2025-08-21) reported Commerce eyeing stakes in all three;
Reuters (2025-08-21, same day) reported an administration official
explicitly denying it. A **separate ~$150M equity stake in an unnamed chip
startup** was reported (The Hill, 2025-12-02) — confirms the mechanism
extended past Intel at least once more, company not identified. The same
grants-to-equity logic was extended in **May 2026 to 9 quantum-computing
firms** ($2B in grants + equity, IBM ~half, Quantinuum/PsiQuantum/Atom
Computing ~$100M each) — a different program pool, same policy shape.
**Natcast** (the CHIPS R&D/NSTC operator) was targeted for closure with
most funding cut, layoffs starting Sept 2025 — a direct cut to the R&D
side. Trump has called CHIPS "horrible, horrible" but **no CHIPS-specific
rescission has been confirmed enacted** — rhetoric outrunning action so far.

**AI-relevance:** upstream, not AI-labeled — advanced logic (TSMC Arizona)
and HBM/memory (Micron, SK hynix) capacity that AI accelerators depend on,
but the awards themselves fund fabs, not AI programs per se.

**Confidence: medium.** Core appropriation figures and the Intel deal are
solid multi-outlet; the company award table and the TSMC/Micron equity
question are each flagged thin/contested above.

---

## 2. DOE — AI/datacenter power programs — `doe-ai-power`

**Size:** the Loan Programs Office's total authority is genuinely unclear
across sources ($400B vs. $289B vs. $290B Title 17 authority cited by
different aggregators — thin, no single primary reconciliation found).
What IS primary-sourced and concrete: **$17.5B in conditional nuclear
supply-chain loans** announced 2026-06-23 (DOE's own page,
energy.gov/articles/department-energy-announces-american-nuclear-supply-chain-loans)
via the new **Office of Energy Dominance Financing (EDF)** — funds up to 5
projects (10 Westinghouse AP1000 reactors, 11GW), each gated on **$1B
upfront private equity** before DOE releases funds. Plus: **$1B loan** to
restart Three Mile Island (Constellation, ~2025-11-18, 4-outlet
convergence) and a **$3B loan** to upgrade the Texas grid explicitly for
data-center power demand (Washington Examiner, 2026-07-08).

**Nuclear-for-AI (Prometheus / Genesis Mission):** figures here are
MESSY and need to be kept apart — DOE's own direct commitment (via Idaho
National Laboratory, Phase II) is **$60M over three years** (inl.gov). The
widely-headlined **"$200M"** figure (Bloomberg via aggregators,
2026-07-21: "Oklo, X-Energy in $200M push") is actually **industry
cost-share across ~32 partners** (X-energy, TerraPower, Oklo, Westinghouse,
GE Vernova, Aalo Atomics, HGP), NOT new federal money — treat the $200M as
industry-wide in-kind/capital, and $60M as the DOE line, when citing this.

**How-free:** posture is **expanding sharply** — the opposite trajectory
from CHIPS/NIH/NSF. Energy Secretary Chris Wright: nuclear "will get the
most Energy Department loans" (CNBC, 2025-11-10). Mechanism is loans, not
grants — repayment terms + private-equity-upfront conditions bound it, so
"free" here means "aggressively being deployed," not "unconstrained cash."
Much of the underlying Title 17 authority reportedly **expires 2026-09-30**
(thin, not primary-confirmed) — a near-term cliff worth watching. DOE also
opened **federal land at Idaho National Laboratory** for AI-datacenter
lease — a non-cash resource being deployed the same direction.

**AI-relevance:** the most directly AI-framed pool in this crawl —
Prometheus/Genesis Mission is explicitly pitched as speeding nuclear
deployment for AI power demand (Nvidia + AWS named partners); the $3B Texas
loan is explicitly datacenter-power-motivated.

**Confidence: medium-low.** The $17.5B program is primary-sourced; the LPO
topline and Prometheus dollar figures are aggregator-thin and partly
conflated in press coverage (corrected above).

---

## 3. DARPA — `darpa`

**Size:** FY2024 confirmed at **$4.122B** (Wikipedia, sourced to DARPA
budget docs). **FY2026 topline is a genuine three-way source conflict** —
$4.9B (LinkedIn post, unverifiable), $4.3B (cabrilloclub.com), $1.9B
(pertamapartners.com, likely a sub-account) — none primary, spread >2x,
**mark unresolved/thin**. One solid sub-line: Advanced Technology
Development FY26 request = **$1,733.5M** (HigherGov, tracker-sourced from
official DoD comptroller data — medium confidence). The FY26 primary
source (DARPA's Master Justification Book, comptroller.war.gov — note the
DoD comptroller domain has migrated to **war.gov**, consistent with the
department's 2025 "Department of War" rebrand) was located but returned as
an unparseable PDF byte-stream.

**How-free:** structurally NOT a balance-sheet pool — DARPA money is
RDT&E appropriation, obligated program-by-program via contracts/OTAs to
industry/academic performers, never held as a spendable balance. This
distinction matters for the axes recipe below (see §Board Structure).
FY2025 ran on continuing resolutions (CRS, thin on full text). One
unconfirmed (thin) signal of 2026 organizational restructuring inside
DARPA's technology offices (DefenseScoop, not independently verified).

**AI-relevance:** **AI Cyber Challenge (AIxCC)** — DARPA + Anthropic/
Google/Microsoft/OpenAI, autonomous vuln-finding AI, ~2023–2025 (dollar
figure and 2025 DEF CON results could not be freshly re-verified this
session, thin/unverified); **Air Combat Evolution (ACE)** — AI dogfighting,
demoed vs. a human F-16 pilot April 2024; **SemaFor/MediFor** —
deepfake/disinfo detection.

**Confidence: low-medium.** Mission/program facts are solid; the current
topline dollar figure is genuinely unresolved this session.

---

## 4. DoD AI — CDAO / DAWG (absorbed Replicator) — `dod-ai`

**Size:** CDAO's own itemized budget lines effectively **zero out for
FY2026** in official comptroller exhibits (HigherGov, aggregating primary
DoD data): MIP program element $70.78M(FY23)→$45.33M(FY24)→$0(FY25 enacted,
FY26 requested), Activities line similarly to $0, both annotated
"responsibilities transferring to Navy/DIA" with **no published
replacement line items** — the true CDAO FY26 number is opaque from public
exhibits alone, which is itself a finding (reduced budget transparency, not
necessarily reduced spend).

**Replicator was discontinued in late 2025 and absorbed into the new
Defense Autonomous Warfare Group (DAWG)** (Breaking Defense 2026-04-21;
meta-defense.fr 2026-05-25). DAWG's **FY26 baseline is $225.9M**, jumping
to a **FY27 request of $54.6B** ($1.0B base + $53.6B reconciliation
funding, per Pentagon comptroller Jules Hurst) — reported as a "24,070%
increase." Original Replicator funding (pre-DAWG, CRS IF12611 — thin,
snippet-only): a $300M FY23 reprogramming request, then $200M secured in
FY24 appropriations; original Aug-2025 deployment target was superseded by
the DAWG restructure.

**How-free:** funding is being shifted OUT of standard RDT&E/procurement
lines and INTO **reconciliation funding** — per the Pentagon comptroller,
explicitly for obligation-timeline flexibility and the ability to move fast
on priority tech. DoD's total FY26 request is $961B, including $113B from
the 2025 reconciliation act (CBO, high confidence). This is a
"how-free-INCREASING" move: reconciliation dollars carry fewer of the
year-to-year appropriations constraints ordinary program budgets do.

**AI-relevance:** CDAO's live site (ai.mil, fetched directly) lists 2025-26
"Pace-Setting Projects" — **Swarm Forge, Agent Network, Ender's Foundry**
(warfighting), **Open Arsenal, Project Grant** (intelligence), **GenAI.mil,
Enterprise Agents** (enterprise). **GenAI.mil** gives DoD personnel
department-wide access to **Google Gemini and xAI Grok** at IL5+
classification — notably no OpenAI/Anthropic mentioned in what was
fetched. **Maven Smart System** remains CDAO's flagship operational
ISR-AI program.

**Confidence: medium** on program names/direction (ai.mil primary + dated
outlets); **low/thin** on precise current-year dollar figures — the CDAO
topline is genuinely unclear, and DAWG's FY26-vs-FY27 figures span
different fiscal years.

---

## 5. NIH — `nih`

**Size:** FY2024 actual **$48.857B**. The President's FY26 REQUEST proposed
a **~40% cut to $27.9B** — this was **REJECTED by Congress**: FY26 enacted
lands near flat-to-slightly-up across three converging sources — CRS
$47.493B, ACR $47.2B (+0.9% vs FY25), Senate Approps $48.7B discretionary
(+$415M). A **second cut attempt is already surfacing for FY27**: a
reported 20% cut proposal (Roll Call, 2026-03-27); Sen. Collins called it
"inexplicable" (2026-05-21).

**How-free — two separate mechanisms, opposite outcomes:**
(a) **Statutory: the indirect-cost 15% cap is DEAD.** Timeline: proposed
Feb 2025 → blocked by injunction Feb-Apr 2025 → permanently blocked Apr
2025 → **administration formally abandoned the fight, 2026-04-08** (STAT,
corroborated C&EN 2026-04-10). Researchers won this one outright.
(b) **Administrative: still throttled regardless.** Grant terminations cost
institutions **$3.8B** (Forbes, 2025-06-14 study); Funding Opportunity
Notices collapsed **787→84** (Forbes, 2026-03-29); NPR/NBC report ongoing
"new ways" to slow disbursement (2026-05-21, 2026-02-04) even after the
topline fight was won. **Net: the appropriated pool is intact, but
execution-level throttling is a live, separate constraint on how "free"
the money actually is in practice.**

**AI-relevance:** **Bridge2AI** ($130M, NIH Common Fund, now Stage 2 —
shifted to AI health-tool safety frameworks, thin single-source figure);
**AIM-AHEAD** (health-equity AI consortium, 10,230+ members active through
2026, coordinating-center predecessor awards ~$50-100M, current total
unconfirmed — thin); a $12.5M/5yr AI-on-biobank Alzheimer's grant (thin,
illustrative not comprehensive).

**Confidence: medium-high** on budget totals (multiple independent
official/authoritative sources converge); **thin** on AI-specific program
dollar figures.

---

## 6. BARDA — `barda`

**Size: thin/unconfirmed.** Official budget pages (phe.gov, aspr.gov)
were unreachable this session (DNS failure/403/404). Only a non-appropriated
advocacy ASK surfaced: Alliance for Biosecurity requested $1.4B Advanced
R&D + $300M for the Emerging Infectious Diseases program, FY26 (outlet/URL
not captured — thin). **This is a genuine research gap** — a follow-up
pass against ASPR's own FY26 budget-in-brief (a 7.4MB PDF was located but
not text-extracted; saved at the scratch path noted by the research agent)
would likely close it quickly.

**How-free:** the concrete, well-sourced event is the **mRNA vaccine
contract cancellation** — **~$500M across 22 projects**, cancelled by
RFK Jr.'s HHS 2025-08-05/06 (5 independent outlets: HHS.gov, NYT, BBC,
BioSpace, Forbes — all converge on the figure and date). **Partially
reversed**: House appropriators put mRNA funding back into the FY26
spending bill over HHS's objection (STAT, 2025-09-10) — same
executive-cuts-vs-congressional-restoration pattern as NIH/NSF.

**AI-relevance:** a BARDA RFI on AI-enabled discovery of broad-spectrum
filovirus therapeutics (thin, single-source, no dollar figure, date
unconfirmed).

**Confidence: thin overall.** The mRNA-cancellation story is reliable;
everything else on BARDA needs a follow-up pass with a working budget-doc
fetch.

---

## 7. NSF — `nsf`

**Size:** FY2024 $9.06B, FY2025 $8.826B enacted (nsf.gov, primary). FY2026:
Trump requested cuts up to **60%** overall / **75%** to Chemistry
specifically — **Congress rejected the deep-cut request but voted for
"substantial decreases"** relative to FY24/25 (Nature 2026-04-30,
Science|AAAS 2026-01-05, AIP FYI 2026-01-09) — **no single clean FY26
enacted total was recoverable this session** (CRS report R48489 almost
certainly has it, blocked by a 403 — thin).

**How-free:** a striking internal-vs-external split. **Statutory
guardrail** in the FY26 bill caps any directorate cut at 5% vs. FY24 —
but internal NSF memos (obtained by *Science*, 2026-06-23) show **Math &
Physical Sciences down 30%/$260M and Biology down $200M** — the guardrail
is being breached administratively. **Grant-making has slowed ~50%**
despite only a 3% topline cut — money is being held back, not formally
zeroed. Mechanism: the new **X-Labs initiative — $1.5B via Other
Transaction Authority** (bypasses standard peer review), announced
2026-05-14, funding 10-year "generational breakthrough" teams in quantum/
AI/sensing. The **National Science Board was reportedly eliminated**
(thin, single-source). NSF is currently run by an acting Chief of Staff
("performing the duties of the Director"), not a confirmed Director
(nsf.gov, 2026-07-22).

**AI-relevance — the big one, NSF's Genesis Mission contributions
(all 2026-07-22, all primary nsf.gov, high confidence):**
- **NAIRR (National AI Research Resource)** — still a PILOT, not
  permanent. 820+ research projects, 82 classroom awards, 23
  infrastructure/data-demo projects, all 50 states + DC + PR.
- **$400M over 4 years** for 20 Programmable Cloud Lab test-bed nodes.
- **$83M** Integrated Data Systems and Services (FabAID, National Data
  Platform, iDLab, BRIDGE, National Science Data Fabric, MESA) —
  explicitly complements NAIRR.
- **Up to $100M** — "Unlocking Dataset Value for AI-Enabled Scientific
  Discovery," $2-5M awards, making existing datasets AI-ready.
- A national network of **20 AI-enabled autonomous laboratories** with
  the Astera Institute.

**Confidence: medium** on core budget; **high** on the Genesis Mission
contributions (primary-sourced, same-day multi-release).

---

## Cross-cutting: Genesis Mission (2026-07-22) — NOT its own pool

The single biggest live item this crawl surfaced. An "all-of-government"
AI-for-science initiative, **>$5B committed**, DOE-led, spanning NSF (data
infrastructure, above), NIH/HHS ("Bio Genesis Mission" — chronic disease),
DoD (aerospace/sensor data), NASA, and the national labs (Sandia assigned
6 mission areas, Los Alamos 7 — Business Journals, 2026-07-27). Focus:
chronic disease, nuclear/grid, cancer, quantum, climate, materials/
semiconductors. Google pledged $40M in AI resources; a US-Japan $1B/5yr
co-investment was announced same week (both thin, single-source —
GovCon Wire). **The primary whitehouse.gov document was not locatable**
(guessed URL 404'd) — everything here is agency-press-release + 3
independent-outlet triangulation, not primary-document-verified. **This is
an OVERLAY across multiple pools, not a pool itself** — model it as a
thread, not a node (see below).

## Context, not a funding pool: WISeR (CMS)

Confirmed directly from CMS's own page: **"Wasteful and Inappropriate
Service Reduction (WISeR) Model,"** Section 1115A authority, an AI+human
prior-authorization pilot across 6 states (NJ/OH/OK/TX/AZ/WA), 6
performance years 2026-2031, vendors paid a % of averted "wasteful" care.
Live controversy: EFF + medical-society lawsuits (Mar-Apr 2026), a
Democratic Senate resolution to overturn it **blocked by Republicans
2026-07-16/17**, and multi-outlet reporting of care delays/denials across
the pilot states. No program-scale dollar figure found. Health-side
context for the ai/mental-health lenses, not a capital pool for this row.

---

## Per-pool summary table

| Pool | Size (best figure) | How-free | AI-direction | Conf |
|---|---|---|---|---|
| CHIPS Act | $52.7B appropriated ($39B mfg+$11B R&D); ~$30.7-30.9B awarded + $5.5B loans to date | Milestone-gated to 2028; grants→equity pivot (Intel confirmed 9.9%/$8.9B; others contested); Natcast cut | Upstream fab capacity (logic/HBM), not itself AI-labeled | medium |
| DOE AI-power | LPO authority ~$290B (thin); concrete: $17.5B nuclear loans + $1B TMI + $3B Texas grid | Loans not grants; expanding sharply; ~2026-09-30 authority-cliff (thin) | Directly AI-framed (Prometheus/Genesis nuclear-for-AI; Texas loan explicit) | medium-low |
| DARPA | $4.122B (FY24 confirmed); FY26 contested 2-2.5x spread | Not a balance pool — RDT&E flow-through, contract-by-contract | AIxCC, ACE, SemaFor/MediFor | low-medium |
| DoD AI (CDAO/DAWG) | CDAO lines ~$0 FY26 (opaque); DAWG $225.9M FY26 → $54.6B FY27 request | Shifting into reconciliation funding (fewer constraints); Replicator absorbed into DAWG | GenAI.mil (Gemini/Grok), Maven, Swarm Forge | low on $, medium on direction |
| NIH | $48.857B (FY24); ~$47.2-48.9B FY26 enacted (Congress rejected 40% cut) | Statutory fight WON (15% indirect cap dead, 2026-04-08); admin still throttles via FOA collapse (787→84) + terminations ($3.8B) | Bridge2AI $130M, AIM-AHEAD, Genesis Mission (Bio) | medium-high |
| BARDA | Unconfirmed (thin) | mRNA cuts ~$500M/22 projects (Aug 2025), partly restored by House (Sep 2025) | AI-filovirus RFI (thin, no $) | thin |
| NSF | $8.826B (FY25 enacted); FY26 total unclear (Congress rejected 60% cut, voted "substantial decreases") | 5%-cap statutory guardrail breached internally (MPS -30%); grants ~50% slower; $1.5B X-Labs OTA bypass | NAIRR (pilot, 820+ projects) + $583M+ in named Genesis Mission lines | medium (high on Genesis lines) |

---

## Proposed board structure

**New G1 pocket: `gov-pool`**, `member_of: [finance]` — sits alongside
`capital`/`insurance` in the finance sector (fits the existing gloss "the
capital pools — asset managers, sovereign funds, insurers"; federal
funding/loan agencies are the state's version of the same thing, and the
CHIPS equity pivot literally converts them into shareholders). Keep
`state-organ` separate and unchanged — it's for pure regulators (FDA,
CAISI) with no capital axis, a different kind of actor than a pool that
commands and deploys dollars.

**Each pool as an `agency`-kind node**, `parent: united-states` (L2),
`pocket: gov-pool`:

| slug | name | axes_num draft (weight / thrust / gravity, $B) |
|---|---|---|
| `chips-act` | CHIPS Act (Commerce) | weight ≈52.7 (appropriated) · thrust TBD (milestone pace unclear) · gravity TBD |
| `doe-ai-power` | DOE AI/datacenter power programs | weight TBD (authority figure unreconciled) · thrust ≈21.5 (2025-26 committed: 17.5+1+3) · gravity TBD |
| `darpa` | DARPA | weight ≈4.1 (FY24, not a real "pool" — RDT&E flow) · thrust ≈ weight (contract-by-contract, no balance) · gravity TBD |
| `dod-ai` | DoD AI (CDAO/DAWG) | weight TBD (CDAO opaque) · thrust ≈54.6 (DAWG FY27 request) · gravity TBD |
| `nih` | NIH | weight ≈47.5 (FY26 enacted) · thrust ≈ weight (annual granting agency) · gravity TBD (academic-biomedical ecosystem, large, unsized) |
| `barda` | BARDA | insufficient data — omit numeric axes_num until a follow-up pass |
| `nsf` | NSF | weight ≈8.8 (FY25 enacted, FY26 unclear) · thrust ≈1.5 (X-Labs, best-known new-obligation vehicle) · gravity TBD |

Every TBD above is a genuine gap (not a placeholder to silently fill in
later) — most of these agencies don't cleanly separate "available capital"
from "annual granting," which is a different shape than a corp's
capex-vs-cash distinction; the weight/thrust recipe may need a per-kind
variant for `agency` nodes the way ROADMAP #24 already flags for
states/persons. **`gravity` (dependent economy) is unsourced across the
board this pass — needs a dedicated crawl** (e.g. NIH's academic-research
ecosystem, CHIPS's leveraged private co-investment, DOE's grid/utility
dependents).

**Genesis Mission**: do NOT model as a node — it's a cross-agency
initiative that wraps NSF/DOE/NIH/DoD's existing pools, not a capital pool
of its own. Model as a thread (below) that cross-references the affected
pool nodes.

---

## Thread candidates

1. **Genesis Mission** (kind: story) — the >$5B all-of-government AI
   science initiative (DOE-led, NSF/NIH/DoD/NASA/national-labs), announced
   2026-07-22, still missing a primary whitehouse.gov source as of this
   crawl. Very fresh, very likely to generate near-term follow-on
   announcements (agency-specific dollar breakdowns, the primary EO/
   memo text, international partner terms).
2. **CHIPS equity pivot** (kind: story) — the government-as-shareholder
   mechanism, Intel confirmed, TSMC/Micron/Samsung contested/denied,
   extended to 9 quantum-computing firms in May 2026. Links to the
   existing `intel-rescue` thread but is broader than one company — a
   policy-level story about appropriated grants becoming equity stakes.
3. **DoD AI consolidation (CDAO→DAWG)** (kind: story) — CDAO's budget
   lines zeroing out, Replicator discontinued and absorbed into the new
   Defense Autonomous Warfare Group, funding routed through reconciliation
   ($54.6B FY27 request) instead of ordinary appropriations — a real
   restructuring of how DoD funds AI/autonomy, worth tracking as its own
   throughline distinct from Genesis Mission.

## Dated expectations (for the ledger, not yet written)

- **2026-09-30** — federal fiscal year-end / FY2027 appropriations
  deadline (government-wide CR-or-shutdown pressure point; also the
  reported, unconfirmed DOE Title 17 loan-authority expiration — same
  date, worth checking if that's coincidence or the actual sunset date).
- **~2026-Q3/Q4** — FY2027 NIH cut proposal (reported 20%, Roll Call
  2026-03-27) moving through markups; watch for a repeat of the FY26
  Congress-rejects-the-cut pattern.
- **Ongoing, no fixed date** — WISeR litigation (EFF suit filed
  2026-03-25, medical-society suits from 2026-04-17) — a ruling would be
  a real event; Senate already blocked the legislative overturn attempt
  2026-07-16/17, so the courts are now the live track.
- **Watch for** — a primary whitehouse.gov Genesis Mission document (not
  yet located as of 2026-07-28); agency-by-agency dollar breakdowns beyond
  what NSF/NIH/DOE have already announced.
