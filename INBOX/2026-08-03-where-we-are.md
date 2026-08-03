# Where we are — the research program + the site restructure (2026-08-03)

*A consolidation writeup, requested by Ben ("write up what we've got").
The thinking is done; this is the state of play before real sourcing
begins.*

## The four research questions (kestrel's namespace, NOT radar's Q1–Q7)

| # | question | design status | already-answered? |
| --- | --- | --- | --- |
| **q1** | Where is the money going? (buildout flows) | v3.2, color-clean | partially settled — build the joins |
| **q2** | Who's buying inference, how much, contracts worth? | v3.2, color-clean | partially settled — read demand, build contracts |
| **q3** | Where is ALL the capacity? (datacenter census) | strawman → to re-scope | leaning settled — Epoch IS ~80%; build the attribution layer |
| **q4** | How are these companies run on the inside? | registered, unstarted | not scoped yet |

q4 is new (Ben, 2026-08-03): the governance/management/internal-control
layer of the buildout firms. Registered on the site's research stub;
no skeleton yet.

## What's designed and review-clean

- **q1 v3.2** (`INBOX/2026-08-03-q1-skeleton-v3.md`) and **q2 v3.2**
  (`INBOX/2026-08-03-q2-skeleton-v3.md`) — the flow map and the inference-
  demand/contracts model. Both carry the full **rulings register
  R-01–R-20** in q1 §2; both passed the color-team cycle to **zero
  substantive residue** (INBOX/q1-color/, q2-color/ — 14 seat memos +
  round-2/round-3 passes).
- **The load-bearing rulings** (Ben's, verbatim in the register):
  R-16 boundaries are FILTERS over the flow map, not memberships ·
  R-17 no premature boundary rules, name the ambiguity · R-19 there is
  NO BAR and no done state, completion milestones (per-cut error bars
  <⚙10%) replace it · R-20 rendering bands are display heuristics, never
  reported metrics — reported confidence is the estimated error bar.

## What sourcing starts from (the audit + the market scan)

- **Step-0 shelf audit** (`INBOX/2026-08-03-q1-step0-audit.md`) — all 56
  staged buildout records graded against live sources: 16 verified, 12
  partial, 2 clerical mismatches, 23 bot-walled, 3 rotted, 0 fabricated,
  1 discard. Self-contained; no future bizdev read needed. Lesson: rot
  is fast (2-year-old primary URLs dead), the best-provenance sources
  are the least scrapable, and six citations carry figures their page
  never states (source-swaps queued).
- **State-of-the-game scan** (`INBOX/sotg/`) — three deep-research
  sweeps + verification. All three verdicts: the LAYERS are mature and
  mostly free/purchasable; the JOINS the skeletons specify exist NOWHERE
  as data. The design is not duplicative.
- **Epoch AI dataset** (`sources/external/epoch-datacenters/`, CC-BY,
  verified cell-by-cell, snapshotted as a diffable source) — 75 AI-player
  facilities, per-facility MW, energized-vs-planned, owner/user split
  with confidence tags. This IS ~80% of q3's census, free. The move:
  q3 becomes an **attribution layer over Epoch** (owner/operator/propco/
  tenant + control cuts Epoch doesn't model), not a from-scratch census.

## Open budget decisions flagged for Ben (not assumed)

- **SemiAnalysis** (institutional) — the paid ceiling for all three
  questions (5,000+ DCs with lease attribution, capex-by-category).
- **The Information Pro** — the only recognized-vs-run-rate revenue
  reporting, for q2.
- Free gets us far; these two are the completeness shortcuts.

## The site restructure (this session)

- **Front page → projects hub** — three cards (News · The Map ·
  Research), each with a line-art emblem in the house palette. The news
  feed stopped being the front page.
- **News → `/news/`** — the weekly dashboard, with the three lens beats
  now nested under it (`/news/ai/`, `/news/global-capital/`,
  `/news/mental-health/`). Adapter updated to write beats to
  `content/news/`.
- **Research → `/research/`** — a stub listing the four questions, no
  content loaded yet (Ben: "don't even load the research questions
  yet").
- Threads, entities, map, claims, metrics stayed put (shared news/map
  infrastructure) so all refs stay solid.

## The immediate next moves (when Ben calls them)

1. **Re-scope q3** from census to Epoch-attribution-layer (the sotg
   finding); optionally color it.
2. **Skeleton q4** (governance/management) as a strawman, its own color
   run.
3. **First real sourcing** — repoint/source-swap the audit's flagged
   records, ingest Epoch (normalize confidence tags → provenance,
   timelines → the delta WAL), begin q1's Tier-A flows.
4. The bundle (q1/q2 v3.2, method doc, run records) is already routed to
   kestrel's INBOX; the reply brief closes the original q1 strawman.
