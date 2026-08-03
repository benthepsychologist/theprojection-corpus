# State of the game — q1/q2/q3: is any of this already answered?

run:      2026-08-03, on Ben's order ("look at what's already done and
          available… it might be a settled one I should be reading rather
          than researching"). Three deep-research agents, one per
          question, fetch-verified (the session's WebSearch budget was
          exhausted 200/200 before any of them started — flagged as
          tooling friction; they ran fetch-only, strong on verifying
          known names, weaker on discovering unknown ones).
verbatim: full agent reports in this dir — sotg-q1-flows.md,
          sotg-q2-demand.md, sotg-q3-datacenters.md.
epoch:    the Epoch dataset Ben pasted was independently pulled and
          verified cell-by-cell (log below); it is real and the
          single most important find of the exercise.

## The one-line answer, three times over

> **All three questions are "PARTIALLY SETTLED — read/buy the layers,
> build only the joins." The layers (chips, facilities, capex totals,
> enterprise adoption, usage) are mature, tracked, and mostly free or
> purchasable. The JOINS — who-pays-whom reconciled across layers,
> commitments-vs-delivered in dollars, circular-financing as a
> maintained graph, deduplicated obligation webs, the propco/tenant
> attribution stack — exist NOWHERE as data. The three skeletons
> specify exactly those joins. The design survived contact with the
> market: it is not duplicative.**

## The Epoch verification (Ben's paste, checked against the live CSVs)

Pulled `epoch.ai/data/data_centers/data_centers.csv` and the timelines
CSV directly. Confirmed: **75 sites** (not the 320 a naive line-count
suggests — embedded newlines), **12,048 MW**, **12,872,833 H100e**, **15
owners**; schema column-for-column as pasted; **owner/user split with
`#confident`/`#likely` inline tags** (64 confident, 9 likely); top-5
sites and MW exact (Colossus 2 946 · New Carlisle 910 · Fairwater
Atlanta 636 · Prometheus 631 · Abilene 421); **China = 3 rows**; **CC-BY**
confirmed. Timelines CSV is real (**433 quarterly records**, cost split
compute/construction/operating, water use) — but its filename is
`data_center_timelines.csv`, NOT the paste's `data_centers_timelines`
(which 404s). NOT verified (plausible, from hub docs not fetched): the
~27%-coverage figure, the 1.4×/1.5×/1.6× uncertainty bands, the GEM
gas-tracker sideways claim. One data fact worth Ben's eye: Colossus 2's
users read **"Anthropic #confident, Cursor"** — Anthropic on
SpaceXAI-owned capacity, if Epoch has it right.

## What already exists, by question — the READ/BUY layer

**Free and worth reading now (all three questions draw on Epoch):**
- **Epoch AI data hub** (CC-BY, CSV, updated within days) — AI Data
  Centers (75 facilities, satellite+permits, per-facility MW/H100e/capex
  + quarterly timelines), AI Chip Sales (spend by vendor), AI Chip
  Owners, AI Companies (revenue run-rates with credibility tags). This
  is the backbone for q1's chip slice AND q3's census AND q2's revenue
  reference — one free source, three questions.
- **Compute Atlas** (compute-atlas.com) — 786 US sites, 284 operators,
  2,813 cited sources, announced-vs-operating discipline (finds the
  ~17:1 pipeline:operating inflation). The transparency model to steal.
- **McKinsey "$7T race"** — the one free what-the-money-buys split
  (60% chips / 25% power / 15% construction) — q1's skeleton, pre-built.
- **Menlo State of GenAI** ($37B enterprise sizing), **Ramp AI Index**
  (transaction-based adoption + free API), **Census BTOS** (the only
  representative baseline), **Anthropic Economic Index**, **OpenRouter**
  — q2's demand side, largely solved and free.
- **ai-circular-economy.com** — a sourced hobbyist deal map; the closest
  thing alive to a circularity tracker (maps flows, doesn't reconcile).
- **LBNL / IEA / ERCOT queue / EU EED + German RZReg** — the aggregate
  power envelopes and the regulatory quasi-census seam for Europe.

**Paid, the "complete" versions:**
- **SemiAnalysis** — the recurring paid answer to nearly the whole
  stack: Datacenter Industry Model (5,000+ DCs, satellite+permits+FOIA,
  the ONLY systematic **lease-vs-self-build attribution**), Accelerator
  model, AI Cloud TCO, capex-by-category. Institutional pricing,
  undisclosed. Named in ALL THREE reports as the paid ceiling.
- **The Information Pro** — the only place recognized-vs-run-rate revenue
  is reported from primary leaks; maintains AI Data Center + AI Chip
  databases. q2's revenue truth layer.
- **Baxtel** (cheapest paid CSV, 8,000+ sites w/ current+planned MW),
  **DC Byte / DataCenterHawk** (brokerage-grade colo).

## What NOBODY publishes — the joins the skeletons specify

Verbatim-convergent across the three reports:

| gap (nobody covers) | the skeleton that builds it |
| --- | --- |
| an integrated who-pays-whom flow map across layers | **q1** — the flow map itself |
| commitments-vs-delivered reconciled in DOLLARS (MW↔$ is always a derived bridge, never measured) | **q1** — the four-stage ladder + the flow/stock join |
| a maintained circular-financing GRAPH (amounts, dates, instrument types) — exists only as prose (Zitron, Kedrosky) or one hobbyist map | **q1** — origination tags + the financing edges |
| deduplicated obligation web (the same OpenAI dollar sits in Oracle's, Microsoft's, AND CoreWeave's RPO; nobody nets it) | **q2** — the chain rule + serves_ref/part_of_ref |
| external-vs-circular revenue split | **q2** — the boundary cuts + burn metric |
| ANY empirical inference-vs-training split (fungible sites; nobody measures it publicly) | **q2** — the revenue-space overlay (explicitly the hardest, ⚙-gated) |
| the propco/developer/GPU-owner/tenant attribution stack; dedicated-lease share inside colo | **q3** — owner≠operator first-class + control cuts |
| energized-vs-announced discipline outside the US | **q3** — the physical status ladder + the ex-CN/RU hypothesis |

## The verdict per question

- **q1 (flows) — PARTIALLY SETTLED, build the joins.** Every layer is
  tracked (Epoch chips, Dell'Oro equipment, Synergy totals, SemiAnalysis
  the stack, McKinsey the split). No one publishes the reconciled
  who-pays-whom Sankey, the dollar-denominated commitments-vs-delivered
  ledger, or the circular-financing dataset. Those are q1's design.
- **q2 (demand/contracts) — PARTIALLY SETTLED, read demand, build
  contracts.** Adoption/usage is genuinely well-covered and free — don't
  rebuild it. The deduplicated obligation web, external-vs-circular
  split, and inference-vs-training decomposition are open; q2 builds
  them.
- **q3 (census) — PARTIALLY SETTLED, LEANING SETTLED.** This is the one
  that shifts. **Epoch already IS ~80% of Ben's census, free** (75
  AI-player sites, per-facility MW, energized-vs-planned, satellite-
  verified) and **SemiAnalysis sells the complete attributed version.**
  Ben's bet (ex-CN/RU sourceable) is confirmed correct — but the move is
  **assemble-and-attribute on top of Epoch + Compute Atlas + Baxtel-class
  data, NOT re-census from scratch.** The genuinely open part is the
  attribution graph (owner/operator/propco/tenant), which is also
  exactly what q3's facility object + control cuts specify.

## Recommendation

1. **q3 changes shape: from "census" to "attribution layer over Epoch."**
   Adopt Epoch's AI Data Centers as the spine (it is already a
   `diffable` source in this repo's own taxonomy, and its `#confident`/
   `#likely` tags map onto our reliability model, its timelines give
   thrust-as-derivative, its uncertainty bands ARE the R-20 error-bar
   reporting style). Re-scope the q3 skeleton so v1 is "ingest Epoch +
   Compute Atlas, add the owner/operator/propco/tenant attribution and
   the control cuts Epoch doesn't model" — not a from-scratch census.
   The ex-CN/RU census is a solved import; the four-layer attribution is
   the original work.
2. **q1 and q2 stand as designed** — the joins they specify are exactly
   the confirmed gaps. Fold the free layers in as sources (Epoch chip
   sales for q1's chip edges; Ramp/Menlo/BTOS for q2's demand side;
   ai-circular-economy.com as a starting deal roster to verify, never
   copy). A **SemiAnalysis / The Information Pro subscription is a real
   budget decision** for the paid ceiling — Ben's call, flagged not
   assumed.
3. **The step-0 audit's lesson holds:** import these as sources to
   verify, capture forever, and reconcile — never as truth to copy. The
   value we add is the joins nobody else publishes, not the layers
   everybody already sells.

## Tooling friction (flagged per standing rule)
All three agents hit an already-exhausted WebSearch budget (200/200,
session-wide) and ran fetch-only. It worked for verifying known
vendors; it under-samples unknown newsletters/datasets and the
fetch-blocked majors (Bloomberg, FT, IEA, Business Insider, DCD). The
read-first lists are solid; the gap analysis could miss an obscure
existing tracker. A re-run with search budget would tighten the "nobody
covers it" claims — but three independent agents converging on the same
gaps is itself strong signal.
