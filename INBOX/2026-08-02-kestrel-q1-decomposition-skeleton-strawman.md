# q1 decomposition skeleton — a strawman to attack before any figure gets sourced

from:      kestrel engine session, 2026-08-02 (design conversation with Ben)
date:      2026-08-02
kind:      request (strawman for workshopping — everything below is the
           agent's proposal unless marked as Ben's words)
touches:   the q1 research pass, and by extension attention/board.yaml,
           attention/capital-context.yaml, attention/threads.yaml once the
           reorganization begins. Nothing here is a code change.
done-when: Ben has ruled on the accounting identity, the six
           double-counting rules, the layer scope, and the evidence bar —
           and one adversarial pass has been run against the identity.
           Then, and only then, sourcing starts.
artifact:  /workspace/kestrel/ROADMAP/RESEARCH.md (the design of record —
           the 10-stage process, the claim substrate, the verification
           architecture) and /workspace/kestrel/ROADMAP/INVENTORY.md (what
           already exists across the fleet). Read as context, not as
           something to execute.

---

## 0. Why this is a strawman and not a plan

**Stage 1 of the process is designing the decomposition *before* sourcing
anything.** The recorded evidence for why: the manuscript project hardened
its outline before writing and its next act returned 14 findings against
the prior two acts' 22 and 21 — *"a ~33% reduction in v1-prose-review
surface area attributable to skeleton-hardening at the pre-prose stage."*

The format that works is a strawman with defensible positions, adversarially
reviewed — not a blank page. **So everything below is written to be
argued with.** Where a rule is arbitrary, it says so.

**One thing deliberately left blank: the bar.** What counts as an answer to
q1 is Ben's, in his words, and the system does not write it. That is the
first section of the finished skeleton and the last thing that should be
filled in from a template.

---

## 1. The question

> "what exactly are the hyperscalers spending all that money on"

and, from the same conversation:

> "what 750B a year BUYS from TSMC and samsung and intel to nvidia and
> broadcom to oracle and to the frontier labs and the hyperscalers… this is
> the largest mobilization of resources in human history, raw not
> necessarily percentage, and I want to understand it."

Reading that literally: **money enters at the top and buys things down the
stack.** The decomposition asks where it lands, by layer. That reading
drives everything in §3.

---

## 2. The aggregate is ambiguous, and the ambiguity is roughly 3× wide

This is the actual problem, and it is worth seeing concretely before
choosing a rule. All four figures below are already staged in `bizdev`:

| figure as reported | what it might mean |
| --- | --- |
| **Stargate: "up to $500B over four years"** | $125B/yr? $500B in the announcement year? Nothing until concrete is poured? |
| **Oracle–OpenAI: ">$300B over five years"** | additive to Stargate, or the same capacity counted again? |
| **Meta capex: $64–72B (2025)** | a *company* number that already contains foundry, memory, and networking spend |
| **Nvidia → OpenAI: up to $100B, progressive per GW** | investment, purchase, or the same dollar going in a circle? |

**Guidance, commitment, contract, and delivered asset are four different
things**, and press coverage uses them interchangeably. Sum them naively
and the residual is meaningless — which would make the whole scoreboard
meaningless, since the residual *is* the scoreboard.

---

## 3. Proposed accounting identity

**A ≡ Σ(Lᵢ) + R**

- **A** — total annual capital deployed by **final buyers** into AI
  buildout assets. Final buyers = hyperscalers · frontier labs ·
  neoclouds · sovereign vehicles.
- **Lᵢ** — the portion of A allocated to layer *i*, sourced.
- **R** — the residual. **R is the deliverable**, not an error term.

**The load-bearing choice: layers receive an *allocation of A*, not their
own revenue.** Meta's capex buys Nvidia systems containing TSMC wafers and
SK Hynix HBM. Summing Meta capex + Nvidia revenue + TSMC revenue
triple-counts the same dollar. Treating layers as allocations of a single
final-expenditure total makes the identity balance by construction, and
makes R meaningful.

**The alternative, named honestly:** a *value-added* decomposition (each
layer contributes margin plus its own inputs, GDP-style). Structurally
cleaner and much harder to source, because it needs per-layer margin data
that mostly isn't disclosed. **Recommend allocation for v1, value-added as
a later refinement** — but this is a real fork and worth ten minutes of
argument.

---

## 4. Six double-counting rules

Each maps to a figure already staged. Each is arguable.

**R1 — Count final expenditure, not transactions.**
A is what final buyers deploy. Supplier revenue is an *allocation* of A,
never an addition to it.

**R2 — A dollar is allocated once, to the layer that captures it as
margin.** TSMC's wafer margin → L07. The HBM inside → L08. Nvidia's markup
→ L10. **Nvidia's gross revenue is not L10's allocation** — most of it is
pass-through to layers below.
*Weakness: needs margin estimates, which for private and segment-level
numbers will often be Level 0 evidence (§5). Expect this rule to generate
the most residual.*

**R3 — Investment flows are Structure, not Flows.**
Nvidia's $100B into OpenAI is an equity fact. It enters A only when OpenAI
*spends* it on assets. **Counting both the investment and the resulting
purchase is precisely the circular-financing error** — and `bizdev` already
holds `ai-circular-financing-2025` as an anchor record for exactly this
debate.

**R4 — Commitments are not expenditure.**
Stargate's $500B/4yr and Oracle's $300B/5yr enter at the rate actually
deployed — sourced from filings or delivered capacity — not on
announcement. *This rule alone probably moves the aggregate by hundreds of
billions, which is why it goes first and gets attacked hardest.*

**R5 — Marks are never expenditure.**
Amazon's $53.4B non-operating gain on its Anthropic stake is not buildout
spend in any direction. Nor is Microsoft's ~$3.2B of the same.

**R6 — Non-cash consideration counts, at disclosed issue value.**
AMD's warrant for 160M shares against 6GW of purchases is real
consideration. It counts — at the value disclosed, not at a modelled value.

---

## 5. What "accounted for" means — the evidence bar

A four-level ladder, because "sourced" is currently doing too much work:

| level | what it is |
| --- | --- |
| **3** | Primary filing, figure bound to a captured excerpt with a hash |
| **2** | Company disclosure — IR deck, earnings call, press release — captured |
| **1** | Credible press citing a named source, captured |
| **0** | Estimate or inference; no single source states it |

**Proposed rule: a layer's allocation counts as *accounted for* only at
Level 2 or above.** Levels 0–1 are recorded as claims but count toward the
**residual**, not the accounted total.

That keeps R honest. It will also make R much larger than a press-based
tally would suggest, which is the point.

---

## 6. Layer scope for v1

Twenty layers are named in the design doc. **Recommendation: name all
twenty; source ten in v1; leave the rest named-but-empty** so they appear
in the gap map as *dark* rather than *absent* — the difference between "we
don't know" and "we didn't look."

| | layers |
| --- | --- |
| **Source in v1** | L03 power generation · L04 grid interconnection · L06 semicap · L07 foundries · L08 memory/HBM · L09 advanced packaging · L10 chip designers · L11 networking · L12 DC builders · L17 hyperscalers |
| **Named, dark in v1** | L01 minerals · L02 land · L05 water · L13 labor · L14 tax incentives · L15 capital sources · L16 model labs · L18 inference sellers · L19 downstream · L20 end-of-life |

**Bottom boundary (open question Q2):** recommend *bounded* — model
minerals only where a named constraint reaches the stack (copper for grid
works, transformer steel, gallium). Not ore markets, not Chinese refining
capacity. Preserves the constraint argument at a fraction of the surface.

**Period:** calendar **2025**, complete and disclosed. 2026 guidance
recorded separately and never mixed into A.

---

## 7. Known-dark register — written before sourcing, deliberately

Naming these in advance is what lets "we found nothing" be distinguished
from "we didn't look." Expect these to stay dark and say so up front:

- **L01 minerals · L02 land · L13 labor** — no disclosure regime exists.
- **L14 tax incentives** — disclosed unevenly, often county-level, rarely
  aggregated.
- **L19 downstream adoption / real inference revenue** — this is Ben's own
  q5, and the design doc already expects it to stay dark for a long time.
  *Naming it dark is more honest than quoting whatever revenue figure a lab
  last claimed.*
- **L20 end-of-life** — no secondary market to observe yet.

**Working hypothesis to test, not assert:** roughly half of A is
sourceable, and the unsourceable half concentrates at the two ends —
minerals and power at the bottom, real inference revenue at the top.

---

## 8. One boundary to set explicitly: L15 and CAPI

`capi` (Capital-as-Power Index) already holds **77 actors and 664 claims**,
grounded in Nitzan & Bichler, using the same claim shape (subject ×
dimension → value + confidence + sources + supersedes_ref). Its own
`AGENTS.md` names kestrel's design as the architecture any resurrection has
to fit inside, and **resurrection as a kestrel layer was decided
2026-07-28**.

**Recommendation: L15 (capital sources) is delegated to CAPI, not
duplicated here.** q1 consumes its claims; it does not re-derive who owns
what. Say so in the skeleton rather than leaving it to be discovered later.

---

## 9. The adversarial pass, before sourcing

One Red review of §3–§5 only. Fresh context. Two specific charges:

1. **Find a dollar these rules count twice.**
2. **Find a dollar these rules miss entirely.**

Bar: if it returns more than two substantive carries, the identity gets
revised before any sourcing begins. That is the whole point of doing this
first.

---

## 10. What already exists to source from

`bizdev/mh-tech-record` holds **56 staged records** on the buildout —
`new-citations-aifrontier-dd-compute-buildout.md` (36) and
`-dd-capital-megarounds.md` (20) — plus ~716 frontier-AI chronology
records, on a store of 3,240 citations and 5,611 captures.

⚠️ **All 56 are `track_b_check: pending`** — pointers, not verified
sources. So Stage 2 begins with a strong target list and a **capture
backlog**, not with sourced claims. Better than zero; worse than it looks.

---

## 11. What this document is not

It does not decide the bar (§0), does not touch any code, and does not
assume the claim substrate is settled — the substrate question is live and
routes through cloud-governor, not through this pass. **Stage 1 produces a
design document and a question object. It produces no claims**, which is
exactly why it can run now without waiting on anything.

Nothing was built, run, or committed for this. No file in this repo was
modified.
