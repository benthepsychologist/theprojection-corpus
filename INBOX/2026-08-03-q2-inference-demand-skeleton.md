# q2 skeleton — "Who's buying inference? How much? And what are those committed capacity contracts worth?"

status:     DRAFT strawman for workshop — written to be argued with, same
            treatment as q1. Sibling of 2026-08-02-q1-skeleton-v2.md;
            routes to kestrel together with it once q1's two blockers
            (Ben's red-team edit, Ben's bar) clear and Ben has ruled on
            §10 below.
from:       theprojection-data workshop session with Ben, 2026-08-03
inherits:   the q1 rulings register in full (R-01 through R-15) and the ⚙
            convention — every tunable value below is a clearly-labelled
            starting point, never a fixed default, collected in the
            decision table rather than hidden in prose.

---

## 1. The question

> "Who's buying inference? How much? And what are those committed
> capacity contracts worth?"

Three asks, and they are three different measurement objects:

- **WHO** — buyer identity: a classification problem.
- **HOW MUCH** — realized revenue per period: a flow problem.
- **WORTH** — committed capacity contracts: a *forward-obligation
  valuation* problem, which is neither of the above.

Most press coverage smears these together ("OpenAI's $300B Oracle deal"
reads as revenue; it is an obligation of uncertain realization). Keeping
them separate is the whole design.

---

## 2. Where q2 sits on the q1 model — no new schema, one object promoted

**q2 is mostly a view of the map q1 already defines.** The q1 schema
deliberately carries revenue-type edges even though q1's scope is
spend-side (that was the ruling: scope stays q1, schema stays ready).
q2 turns them on.

**The consolidation frame does the heavy lifting.** Per the circularity
ruling — intra-system flows are transfers; only boundary crossings are
system totals — q2's revenue picture splits cleanly:

- **External revenue** — inference/capacity bought by parties *outside*
  the system (enterprises, consumers, governments). This is real system
  revenue, and it is the numerator against q1's build spend: together
  they produce the burn metric, "the system's earnings against the rest
  of the economy."
- **Intra-system revenue** — labs buying from hyperscalers, hyperscalers
  buying from neoclouds, everyone buying from Nvidia. Real contracts,
  real cash, and *transfers* at the system level. They appear on the map
  as edges; they never enter system-revenue totals.

**One formalization: the commitment object.** q1 already needed
commitments as things-that-amortize (its rule that Stargate's "up to
$500B over four years" enters flows only at the actually-deployed rate).
q2 promotes the commitment to a first-class object:

```
commitment := {parties, face_value, term, structure, disclosed_terms,
               termination/contingency clauses, funding_linkage
               (origination tags), amortized_to_date, observations[]}
```

One object class serves both questions — a supply-side build commitment
(Stargate) and a demand-side capacity contract (OpenAI→Azure) are the
same shape. `amortized_to_date` is the seam: it is exactly what q1's
deployed-rate rule consumes.

**Grounding — this gap is already on the record.** The July capex crawl's
own cross-cutting finding was that the payoff layer is the weakest thing
in this map: *"press-only backlogs; the $250B OpenAI→capex mapping
doesn't exist publicly."* q2 is that finding, worked as a question.

---

## 3. WHO — the buyer taxonomy (⚙ starting point, per the never-hardcode ruling)

Starting classes: **consumer subscriptions** · **enterprise** (coarse
sector split) · **government & defense** · **in-system AI companies**
(labs, neoclouds, hyperscalers buying from each other) ·
**resellers/aggregators** (API middlemen).

- **The load-bearing cut is not sector — it is boundary.** External vs
  intra-system is where the entire bull/bear argument lives, because
  today's headline "AI revenue" is dominated by in-system purchases.
- **Enterprise identity is mostly invisible** below the seller's segment
  line; the sector split will lean on surveys and procurement data —
  reliability-weighted estimates, which the evidence ruling makes
  first-class rather than second-class.
- **Government is the underrated seam.** US public procurement is a real
  disclosure regime — USAspending, SAM.gov, FedRAMP authorizations, DoD
  task orders — with named buyers and named amounts. Genuinely
  sourceable, mostly untouched by press, and a natural first build for
  the independent-measurement class the evidence model wants cultivated.

---

## 4. HOW MUCH — realized revenue, with its own four-stage ladder

q1 found that press collapses four stages of *spending* (guidance →
commitment → contract → delivered asset). Revenue has the same disease,
so it gets the same ladder:

**claimed run-rate → booked contract → recognized revenue → cash collected**

- A "$X ARR" leak is a stage-1 observation (provenance: company
  statement, usually un-audited), recorded as such and **never mixed into
  a period total**. A period's "how much" quotes recognized revenue where
  observable.
- **The inference-vs-training split, stated honestly:** almost nothing
  discloses it — contracts and segments cover *capacity*. Decision (a)
  below: measure strict-inference only, or measure AI-capacity
  consumption with an inference-share overlay estimated from token
  economics, traffic measurement, and subscriber math. The overlay is
  exactly the kind of crafted independent estimate the evidence ruling
  says can outweigh company guidance — recommend that path, labelled.
- Seeds already in this map's record (all subject to the
  audit-before-trust ruling): ChatGPT at ~1B weekly actives (single
  benchmark, flagged as such when recorded) on the consumer side;
  hyperscaler AI-segment disclosures (Azure growth prints, AWS revenue)
  as upper bounds that *contain* inference.

---

## 5. WORTH — the committed-capacity contract register

Face value is an observation. **Worth is face × realization, and
realization hangs on structure** — so v1 records, per contract:

- **face + term** — the "$300B over five years" shape;
- **structure** — take-or-pay / committed minimum / usage-based with
  floor / best-efforts. These differ enormously in worth and are usually
  the undisclosed part;
- **termination & contingency clauses** — the restructured
  OpenAI–Microsoft arrangement is the canonical warning that terms move;
- **funding linkage, via q1's origination tags** — a commitment funded by
  the seller's own money going in a circle (Nvidia invests up to $100B in
  OpenAI progressive per gigawatt; OpenAI commits capacity spend back
  out) is worth less than face *as evidence of external demand*, and the
  register shows that linkage on the contract's face rather than leaving
  it to be rediscovered;
- **amortized to date** — how much has already converted to flows.

**Decision (c):** v1 stops at face + structure + linkage + flags.
Expected-realization modeling (discounting, probabilities) is a later
lens ⚙ — doing it now would manufacture precision the inputs don't have.

**Register seeds from this map's own record** (each needs the audit; the
one thing already known is that they exist):

| contract | face as recorded here |
| --- | --- |
| OpenAI → Microsoft/Azure | $250B commitment, reiterated on the 07-29 call (primary) |
| OpenAI → Oracle | ">$300B over five years" |
| OpenAI → Amazon | $50B investment + separate $100B/8yr compute, confirmed 02-27 |
| Stargate frame | "up to $500B over four years" |
| Anthropic → Amazon | $100B+/decade — *excluded* from AWS's stated $364B backlog when reported |
| Anthropic → Microsoft/Azure | $30B commitment |
| Anthropic → Google | TPU deal, unpriced — a register entry with face unknown, flagged |
| OpenAI ↔ AMD | 6GW purchases against 160M-share warrants (the non-cash-consideration rule applies: real edge, disclosed issue value) |
| CoreWeave backlog | conversion is literally the standing question on this map's CoreWeave thread |
| AWS backlog "$496B" | single-source, unverified — recorded as such 08-01; exactly what the audit step exists for |

---

## 6. The chain rule, extended to commitments

Backlogs chain exactly like flows. OpenAI commits to Microsoft; Microsoft
procures neocloud capacity to serve it; both obligations are real, both
sit in seller backlogs — and they are **hops of the same future dollar**.
Summing RPOs across the industry double-counts pass-through capacity,
which is the same error q1's first flow rule bans for spending (never sum
edges along a chain; totals only from boundary crossings and rollups).

So: **an "industry backlog" headline number is banned by construction.**
Commitment totals come only from (a) *boundary-committed* — external
buyers' commitments into the system — or (b) per-node registers.

---

## 7. The headline hypothesis — written before sourcing, to be graded

Per the coverage-hypotheses ruling (predictions get graded, never
exempted from looking):

> **Committed intra-system contract face value exceeds realized external
> inference revenue by roughly an order of magnitude.**

If sourcing confirms it, the buildout is overwhelmingly financing its own
demand signal. If sourcing refutes it, external demand is far more real
than the bear case allows. Either result is the finding of the year;
that is what makes it a good hypothesis.

Supporting predictions, also to be graded:

| buyer class | predicted sourceability | predicted best source class |
| --- | --- | --- |
| in-system contracts | high | company statements + filings |
| government | high | procurement records (independent, primary) |
| consumer | medium | subscriber counts × price cards; run-rate claims graded on the ladder |
| enterprise direct | low direct / medium via seller segments | segment disclosures + surveys |
| inference-vs-training split | low | estimate-driven by design (the overlay) |

---

## 8. v1 scope for q2 (⚙ tier cut, re-cuttable per pass)

- **Tier A:** build the contract register from the seed table (~10–12
  entries, each audited to its actual source before trust); realized-
  revenue observations for every seller that discloses anything
  (hyperscaler AI segments, labs' run-rate claims placed on the ladder,
  neocloud revenue); the **government procurement sweep** as the first
  purpose-built independent-measurement source.
- **Tier B probes:** enterprise adoption surveys · the token-economics
  estimation method (design it, grade its reliability ceiling before
  using its outputs) · app-store/subscriber data paths · the
  reseller/aggregator layer.
- **Activities note:** this activates the inference-selling and
  downstream-adoption activities that q1 held at probe level. (The
  original strawman guessed this question would be numbered q5; Ben
  numbered it q2, 2026-08-03 — the q1 doc's register is annotated.)

---

## 9. What q2 deliberately is not

- Not a re-derivation of q1 — same map, same evidence model, same
  consolidation rules; one object promoted.
- Not an expected-value model of contract worth in v1 (decision c).
- Not the bar — that is Ben's, in his words, same as q1.

---

## 10. Decision points for Ben

| # | decision | proposed starting position ⚙ |
| --- | --- | --- |
| a | **inference strictly, or AI-capacity with an inference-share overlay?** | the overlay: measure capacity consumption (what discloses), estimate the inference share by token economics/traffic/subscriber math, label the overlay as the estimate it is |
| b | **buyer taxonomy** | consumer · enterprise-by-sector · government · in-system · resellers — a starting list, per the never-hardcode ruling |
| c | **what "worth" means in v1** | face + structure + termination clauses + funding linkage + flags; expected-realization modeling deferred |
| d | **the revenue ladder** | claimed run-rate → booked → recognized → collected; period totals quote recognized only |
| e | **v1 register roster** | the ten seeds in §5, audited first |
| f | **routing** | ✅ ruled 2026-08-03 ("new document") — q2 stays this sibling file, routes to kestrel together with q1 v2 when its blockers clear |
| g | **the q2 bar** | yours, in your words — deliberately last, same as q1 |
