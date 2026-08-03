# q3 skeleton — "Where is ALL the capacity?" The global datacenter census

status:     DRAFT strawman for workshop, registered 2026-08-03 on Ben's
            words: *"I want to know where every existing datacenter in
            the world is owned by any top 10 inference player. Call that
            q3 maybe? Where is ALL the capacity. Outside of China and
            Russia, I bet it's possible to source every datacenter on
            earth."* Written to be argued with; a color run awaits Ben's
            go once workshopped.
inherits:   the full rulings register (q1 v3.2 §2, R-01–R-20) and the ⚙
            convention. Nothing here re-litigates a ruling.
foundation: q1 v3.2 (the flow map — q3 is the STOCK its flows build) and
            q2 v3.2 (capacity contracts — served FROM the facilities q3
            censuses).

---

## 1. The question

Where is every datacenter operated by, owned by, or dedicated to the top
inference players — and how much capacity does each represent? Not the
money (q1), not the contracts (q2): the **physical stock**. A census,
with receipts, of the machines' actual homes.

## 2. How q3 sits on the model — a stock register joined to the flows

q1 maps **flows** (money moving); q2 registers **forward obligations**
(commitments). q3 adds the third object class: the **facility** — the
physical asset the flows build and the contracts are served from. One
new object, additive fields only (the R-13 pattern, third instance):

```
facility := {id, location (geo + jurisdiction),
             operator (entity — who runs the compute),
             owner (entity — who owns the shell/land; opco/propco and
                    leaseback structures make owner ≠ operator routine),
             tenancy: owned | leased-dedicated | colo-shared,
             status: announced | permitted | under-construction |
                     energized | expanded | decommissioned,
             capacity: typed value + UNIT (MW IT load · MW campus ·
                       GW announced · chip count where known) — never
                       unit-blind,
             power: source + PPA/utility references where known,
             commitment_refs: [q2 commitments served from here],
             observations[] — the one evidence model, unchanged}
```

- **The status ladder is the four-stage money ladder, physical flavor**
  — announced (guidance) → permitted (commitment) → under-construction
  (contract) → energized (delivered). Same discipline: an announced
  gigawatt is not an energized megawatt, and totals never mix stages.
- **Capacity is a typed value with a mandatory unit.** "5GW campus" is
  an announced-stage upper bound; "300MW IT load energized" is a
  delivered-stage point. The unit-blind "GW" headline is this domain's
  version of the four-stage collapse.
- **Owner ≠ operator is first-class**, because the market made it so:
  propco/leaseback structures, REIT landlords, and dedicated-lease
  arrangements mean "owned by a top-10 player" is genuinely three
  different questions (owns · leases-dedicated · rents shared racks).
  Per R-16/R-17, "the top 10's capacity" is computed under **control
  cuts** (⚙): `cut:operated` · `cut:owned` · `cut:dedicated`
  (owned + leased-dedicated) — named on every total, never one rule.

**Joins:** a facility's build is where q1 `asset purchase` edges land
(gross build materializes here — a cross-question reconciliation:
Σ facility build-cost estimates vs. q1's operator-frontier build, per
entity); q2 capacity commitments carry `commitment_refs` to the
facilities that serve them, when known.

## 3. The roster — "top 10 inference players" is a filter, not a fact

Per R-16, the roster is ⚙ data: a named, versioned list. Starting
proposal: OpenAI · Anthropic · Google · Microsoft · Amazon · Meta · xAI
· Oracle · CoreWeave · Nvidia (as operator of its own research/DGX
capacity) — with the census schema indifferent to the list: adding an
11th player is a filter edit, not a redesign. "Inference player" is
deliberately loose at the edges (Oracle serves inference it doesn't
originate); the roster is a scope choice, revisable per pass.

## 4. Why Ben's bet is probably right — the sourcing regime

This is the **independent-measurement class's home turf** — the class
the evidence model was rebuilt to make first-class (R-05), and the one
q1's round-1 review found structurally starved. Datacenters are the
least hideable objects in the entire program:

- **They pull permits** — construction, environmental, water. Public.
- **They join interconnection queues** — ERCOT/PJM/MISO et al. filings
  with MW figures. Public, recurring, already named in q1's collector
  plans.
- **They show up from the sky** — satellite construction progress is a
  proven method in this field.
- **Their landlords disclose** — Digital Realty, Equinix and peers are
  public REITs with 10-K property schedules; colo and leaseback deals
  surface in filings.
- **Their power is contracted** — PPAs, utility rate cases, grid
  studies.
- **Local press covers them** — sitings are jobs-and-tax-break stories.
- **Aggregators exist** — commercial/community datacenter maps provide
  starting rosters to verify, not truth to copy.

The census is therefore mostly a **triangulation build**: aggregator
roster → per-facility verification against permits/queues/filings →
capacity typed by stage and unit. The capture discipline applies from
observation one (the step-0 audit just demonstrated rot eating 2-year-old
primary URLs).

## 5. Coverage hypotheses — including the headline bet, pre-registered

Per R-09/R-19, predictions written before sourcing, graded after:

| region/class | predicted sourceability |
| --- | --- |
| US/EU/UK/CA/AU facilities of roster players | **high** — Ben's bet: near-complete census possible |
| Gulf states (UAE/KSA sovereign builds) | medium — announcements loud, ground truth thinner |
| rest-of-world ex-CN/RU | medium-high |
| China | low — predicted-dark, still probed (R-06: darkness is an outcome, not an exclusion) |
| Russia | low — same treatment |
| owner/propco structures behind operated facilities | medium — REIT filings help, private leasebacks hide |
| energized MW (vs announced GW) | medium — the stage that matters most is the least announced |

**The headline hypothesis:** *outside China and Russia, ≥95% of
roster-player facilities (by count and by energized MW) can be sourced
to at least one independent-measurement observation.* If it grades true,
the census is a solvable problem; where it fails, the failure map is
itself the finding.

## 6. Milestones (R-19 — waypoints, never finish lines)

- Census v1: every roster player's facility list under `cut:operated`,
  each facility carrying stage + typed capacity + ≥1 observation.
- Error bars on each player's total energized MW < ⚙10%.
- The ex-CN/RU hypothesis graded.
- Cross-question reconciliation running: facility build-cost vs q1
  flows, per entity.

## 7. Decision points for Ben ⚙

| # | decision | proposed starting position |
| --- | --- | --- |
| a | the roster | the ten in §3, as a named versioned filter |
| b | capacity unit conventions | MW IT load as the canonical energized unit; campus/announced figures kept as typed upper bounds, never summed with energized |
| c | control cuts | `cut:operated` primary for v1; `cut:owned` and `cut:dedicated` computed where ownership data lands |
| d | China/Russia treatment | predicted-dark with probes, never excluded by rule |
| e | color run | q3 gets the standard treatment (Green ∥ Red → Blue → White) once this strawman is workshopped |
