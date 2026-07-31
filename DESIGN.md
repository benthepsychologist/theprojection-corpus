# DESIGN.md — the board's node+claim graph, and Global Capital's interpretive layer

*The schema shapes and plans behind two systems: `attention/board.yaml`'s
node+claim graph (Part 1), and the former money lens's reframe into an
interpretive "Global Capital" layer (Part 2, specced AND built 2026-07-30,
same day). Hand-maintained; as of 2026-07-30.*

## Part 1 — the board

> **One line:** the board is a **file-based node+edge graph** (YAML → JSON →
> static site, **no database**). Every actor is a **node**; every metric we
> assert is a **claim** with cited **sources** and a clickable page. The
> convention is borrowed from the `lifeos-registry` / CAPI (`power_assessment`)
> knowledge-graph model — we took the field shapes, not the DB.

---

## 1. Nodes

Everything on the board is a node. Two **orthogonal** descriptors + edges.

- **`kind`** — *what it is:* `person` · `house` (≥2 people acting as one) ·
  `corp` · `state` · `agency` (gov sub-body) · `group` (a pocket/sector —
  aggregates members, no agency of its own).
- **`level`** — *where it sits:* `L1` (nothing over it) · `L2`+ (has a
  `parent`). **Assigned, seeded rough, refined** — not a formula. `kind ⊥
  level`: a person may be L1 (Musk) or L2++ (most people); a corp may be an
  L1 independent or an L2 subsidiary.
- **Group tiers:** `G1` (pocket — a cohort of actors) · `G2` (sector — a
  cohort of pockets). Loose hint, not a strict ladder.

**Edges** (kestrel keeps structural edges inline on the node; semantic ones
are the claim/thread links):

| edge | meaning | on |
| --- | --- | --- |
| `parent` | containment → makes it L2+ | the child node |
| `held_by` | a person/house controls an org | the org |
| `depends_on` / `liege` | reliance, **not** containment (stays L1) | the dependent |
| `pocket` / `member_of` | membership in a group | the actor / the group |

Actors are mostly a clean containment **tree**; groups are a messy
many-to-many **graph** (`Finance ⊃ {capital, insurance}`, but hyperscalers
are not in Finance).

`kind`/`level` are **derived as a default seed** in `tools/publish_projection.py`
(`build_board`) from `rank`/`parent`, overridable per-node.

---

## 2. The axes (the differentiators)

The feudal rank ladder was dropped 2026-07-25; the model went **four measured
axes** 2026-07-27, each deliberately adopting an established formalization
(prior-art research absorbed that day — every axis page cites its lineage at
`/metric/` on the site):

- **commanded_capital** (weight, $ stock) — $ the actor **directs**: owned +
  fiduciary + undrawn. *(Renamed from `capitalization` 2026-07-27 — done, not
  pending.)* Adopted: latent power (Mearsheimer) · PE committed-vs-called.
- **thrust** ($/yr flow) — capital committed in the last 12mo to **new**
  positions. Corps: capex − D&A + M&A + stakes + capitalized bets; labs:
  commitment run-rate; funds: net *new-position* deployment (never inflows).
  Buybacks+dividends tracked separately as **capital returned** — a signed
  negative channel, never netted in. Adopted: reinvestment rate (Damodaran),
  extended · commitment (Ghemawat).
- **gravity** ($/yr flow) — the third-party economy that **breaks if the
  actor stops**. Method is **structural, attributable** (never gross
  ecosystem headlines): substitutability × forward-linkage, granularity
  cross-check. Adopted: G-SIB substitutability (Basel) · upstreamness ·
  Gabaix granularity. *(Supersedes the earlier "stored gross, deflation
  deferred" position — un-deferred 2026-07-27.)*
- **optionality** (band) — how **free** the commanded capital is: `free` ·
  `mixed` · `constrained` · `locked`. **Measured encumbrance, NEVER derived
  as thrust÷weight** (Dixit–Pindyck: commitment destroys option value — the
  ratio is a category error). Adopted: net-resources correction (Beckley).

Numeric values live in `axes_num: {weight, thrust, gravity}` ($B) alongside
the prose axis strings — **53 of 92 orgs** carry them (a 21-actor pilot on
2026-07-27, full corps rollout 2026-07-28); the
site's `/map/` plate renders from them as the **POWER view** (Ben,
2026-07-27): optionality columns (free→locked) × log-weight height,
**size = gravity**, **fill = burn (thrust÷weight) as heat**, neon sector rings. *(v1 —
thrust × gravity with size = weight — was retired same day: gross-AUM area
domination misranked the finance actors. The reach=spend diagonal view is
queued to live on the circular-financing thread pages.)*

**Capital is a flow, not a pile** — the per-node bundles break it into
**in · out · available · operating · deployed**.

---

## 3. Claims + sources (the receipt layer)

**Discipline (`CLAUDE.md`):** every cap/opt/gravity + posture value carries a
cited source; the value is the summary, the **claim page is the receipt**,
and it must be clickable.

- **Source data** lives in per-node bundles:
  `artifacts/bundles/<node>-node/provenance.yaml`, shape:
  ```
  posture:  {value, basis, sources[]}
  capital:  {available|operating|deployed|in|out: {value, sources[]}}
  optionality: {value, sources[]}
  gravity:  {value, sources[]}
  ```
  each source = `{figure, label, url, as_of, confidence}` (→ PKG `source`
  shape: `title`/`locators[]`/`reliability_tier`/`published_at`).

- **A claim** = `subject(node) × dimension → value`. Built by
  `build_claims()` into `data/claims.json`:
  ```
  {id: "<node>--<dimension>", subject, dimension, label, value,
   basis, confidence, as_of, sources[]}
  ```
  `id` is a stable **permalink** (`/claim/<node>--<dimension>/`).

- **Aggregate claims** — group nodes (pockets G1, sectors G2) get claims
  **derived from members**: posture = *modal + spread*; other dims link to
  the member claims. An aggregate claim's `members[]` are its evidence; its
  page is a pile of links to the member claims. (This is how "why are
  frontier labs hedging?" resolves.)

- **Adopted from `lifeos-registry`/CAPI, deliberately:** the
  `power_assessment` claim shape (subject × dimension → value +
  confidence + as_of + sources + **`supersedes_ref`**), the `source`
  citation shape, and `origin`+`review_status` provenance. **Skipped:** the
  BigQuery/WAL/registry-daemon machinery, the full lifeos-registry kind
  ontology (100+ kinds), deep inheritance. File-based only.

- **Pending:** `supersedes_ref` (claim-as-micro-thread history) is
  designed-in but not yet implemented or rendered; a claim's related
  **threads** are derived rough (the subject's threads) and will be
  relevance-filtered later.

---

## 4. The pipeline

```
attention/board.yaml            hand-maintained nodes + groups + edges
artifacts/bundles/*-node/       per-node sourced metrics (the claim data)
       │  tools/publish_projection.py
       ▼
data/board.json   (nodes + groups, derived kind/level)
data/claims.json  (node claims + group aggregates)
content/map/*     (a page per node + group)   content/claim/*  (a page per claim)
       │  Hugo (theprojection)
       ▼
/map/            the PLATE (power view: optionality cols × weight, size=gravity, heat=burn thrust÷weight) → sectors → tiles
/map/<node>/     the actor: node-line (kind·level·pocket·POSTURE) + "The metrics"
/claim/<id>/     the receipt above the fold (value·confidence·citations) · the working below
/metric/<slug>/  methodology per metric — definition · recipe · prior art (hand-authored, site repo)
```

`/publish --push` regenerates all three JSON/stub sets, pushes the site, and
fires the Cloudflare deploy hook. Template/CSS changes need the hook fired by
hand.

---

## 5. Pockets / sectors (current)

- **Sectors (G2):** `finance` (capital + insurance) · `power` (hyperscaler +
  frontier-lab) · `infra` (foundry + chips) · `care` (health).
- **Pockets (G1):** hyperscaler · frontier-lab · foundry · chips · capital ·
  insurance · health · **gov-pool** (state capital — rendered on a SEPARATE
  state map, never the corp plate; Ben 2026-07-28).

---

## 6. Open / parked

- **`axes_num` beyond the corps** — the 21-actor pilot became a full corps
  rollout 2026-07-28 (**53 of 92 orgs carry `axes_num`**); what remains is
  states/persons, which want different recipes per kind.
- **`asml` not on the board** — high-gravity gap (sole EUV supplier); needs a
  `/steer add actor`. **`apple`/`coreweave` unpocketed** — neutral ring on
  the plate until assigned.
- **`pocket`/`member_of` as first-class predicates** — currently a denormalized
  string; promote if the graph earns it.
- **Aggregate claims** — posture is modal; capital/gravity aggregates are
  link-rollups (no numeric sum of freeform strings yet).
- **Parked cohorts:** gov-funding pockets (US/Canada — a state-capital layer);
  the Evidence-Gap MH evaluators/enforcers (their source moved to the
  `the-evidence-gap-src` project).
- **Data flags to sanity-check:** a few person net-worths (e.g. Larry Page)
  read high; several execs are operating-capital-only (no personal fortune).
- **`silk-road`** (route-layer stub) still seeds as `corp` — pending retirement.

---

## Part 2 — Global Capital (specced 2026-07-30, BUILT same day)

> **One line:** the `money` lens becomes **Global Capital** — an
> *interpretive* lens, not just an aggregating one. Every relevant item can
> carry a generated, confidence-tagged **interpretation** (mechanism ·
> branching scenarios · a link to a full reasoning receipt), read against a
> **standing capital-context artifact** refreshed from real macro data, not
> invented fresh each day. Same "summary on the surface, receipt behind a
> click" convention as Part 1's claims — a different subject, the same shape
> of honesty.

**Origin** (Ben, 2026-07-30): *"'finance' is boring, 'Global Capital' is
interesting to me... it's not just aggregating news items, it's reviewing
them through this lens and offering possible interpretations about how this
might change the global picture. Or regional picture."* Two changes bundled
together, and they're separable: a **scope** widening (rates, war, risk
reassessment become capital-flow *drivers*, not separate topics) and an
**editorial-mode** change (interpretation, not just aggregation).

### 7. The rename — BUILT 2026-07-30

**Full rename, up and down the beat** (Ben's call, not cosmetic-only). The
slug landed as **`global-capital`**, not the originally-proposed `capital`
(Ben: "Global-Capital" when confirming the open decisions) — everywhere
`money` appeared: `attention/watchlist.yaml`'s lens block,
`attention/threads.yaml` (13 threads), `sources/benchmarks.yaml`,
`sources/{sources,feeds}.yaml`, `tools/readouts.py`'s
`LENS_LABEL`/`LENS_SLUGS`/`LENS_BEATS`, `tools/{render_read,
publish_projection,collect}.py`'s lens constants, every collector that
emitted `lens="money"` (`fred.py`, `sec_edgar.py`'s payer-org map,
`lda.py`/`fec.py`'s CLI defaults), `templates/read-shell.html`'s filter
chips, `templates/daily-digest.md`, and theprojection's `hugo.yaml` nav +
`/beat/money/` → `/beat/global-capital/` + `main.css`'s `--lens-money` →
`--lens-global-capital`. Digests dated **before** the rename keep their
historical `-money.md` filename and `lens: money` frontmatter — not
rewritten, only the going-forward convention changed (the current week's
07-27 through 07-30 files were renamed, since they were still live in the
render window; older archive was left alone). `read-shell.html` keeps a
`money`→`global-capital` alias in its lens filter so archived items stay
findable under the new chip.

### 8. The interpretation shape — BUILT 2026-07-30

`tools/readouts.py`: `normalize_interpretation()` + `validate_interpretation()`,
constants `MECHANISM_MIN/MAX`, `CONTEXT_NOTE_MIN/MAX`,
`SCENARIO_DIRECTION_MIN/MAX`, `SCENARIO_WHY_MIN/MAX`, `SCENARIOS_MIN/MAX
= 2/4`, `CONFIDENCE_LEVELS`. Attached to a digest item, alongside its
existing sourced bullet — **not replacing it**:

```yaml
interpretation:
  mechanism: "one sentence naming the transmission channel"
  confidence: speculative | plausible | well-supported
  scenarios:
    - direction: "..."
      why: "..."
      precedent: "..."       # a specific historical instance, or absent
    - direction: "..."        # a second, genuinely different path — the
      why: "..."              # fuzziness Ben asked for: real branches, not
                               # one hedge-everything paragraph
  context_note: "how this interacts with the standing capital-context snapshot"
```

**The reasoning template** (Ben, 2026-07-30 research pass — this is the
pattern real capital-flow analysis actually uses, e.g. BIS's Quarterly
Review and IMF's GFSR, not house style invented here):

1. Name the event.
2. Name the **transmission mechanism** explicitly — rate differential → carry
   trade; risk event → flight-to-safety **or** flight-*from*-carry (not the
   same thing); sovereign-bank linkage; leverage/margin amplification.
3. Trace the flow direction — from what, to what, via which instrument.
4. Classify **push vs. pull** (source-country-driven vs. destination-
   country-driven — the standard Calvo/Reinhart framing).
5. State the regional/second-order consequence — who's exposed, and why.

**The guardrail** (Ben: *"shouldn't invent interpretation on thin evidence or
should at least flag itself"*): `confidence` is not decorative — it is
**enforced like `readouts.py`'s existing shape validators**. Concrete
operationalization landed on: `mechanism` is required unconditionally (a
sentence, 30-200 chars); above `confidence: speculative`, at least one
`scenario` must carry a real, non-empty `precedent` or the whole
interpretation is rejected — this is the checkable form of "must name a
real mechanism or a real precedent," since the mechanism field is already
mandatory regardless of confidence level. Duplicate scenario directions
are also rejected (real branches, not restated hedges). A generation that
can't ground either gets rejected, the same way a summary missing a
required field gets rejected today. **Trigger is per-item** (Proposal-2
Option A) — attached where a real mechanism is identifiable, never forced
onto every bullet to pad a thin day. This is a new (sixth) duty in
`/daily`'s curation rubric for this lens specifically (`.claude/skills/
daily/SKILL.md` step 4), not a rewrite of the shared five.

**Storage, resolved:** a sidecar per Global-Capital digest,
`artifacts/digests/daily/<date>-global-capital.interp.yaml`, keyed by
`slugify()` of the bullet's own bold lead phrase (a dedicated key
namespace, decoupled from the item's own `id` field, which is
URL-based when a source link exists). The bullet's `<!-- k: ... -->`
annotation carries `interp=yes` to mark it. `tools/render_read.py`'s
`parse_digest()` loads the sidecar (Global Capital scope only), attaches
`interpretation` + a computed `interpretation_id` to the matching item —
computed once, in Python, so the Hugo template never re-derives it and
risks drift from the page it actually generates.

### 9. Visual identity — interpretation vs. fact — BUILT 2026-07-30

Must be unmistakable at a glance that this is generated reasoning, not a
sourced fact — same discipline as "a metric with no visible source is a
bug" (`CLAUDE.md`), inverted: *an interpretation that reads as a fact is a
bug.* **Color chosen** (Ben: "look at it and make a call"): a muted
indigo-violet, `--interp:#5A4B8C` / `--interp-tint:#EEEAF7` — outside the
palette's existing blue (AI)/amber (Global Capital lens itself)/red
(mental-health)/plum (`--power`, board sector)/teal (`--care`) hues
entirely, in the same desaturated register as the rest, and clear of
`#E01279`'s reservation. A labeled band (`.interp-band` on the site,
matching the mono-caps kicker convention already used for
`BREAKING`/`NEWS`/`SUMMARY`) rendered directly under the bullet it
belongs to, never in place of it.

### 10. The receipt page — BUILT 2026-07-30

Same move as a `/claim/<id>/` page: a compact teaser on the surface
(`→ what this could mean`), the full reasoning one click away.

- **Pre-generated and cached at curation time** (Ben's call) — same
  cost/validation model as the rest of the readouts pipeline (a sonnet
  agent writes it, a validator checks it, `--apply` stores it), rather than
  generated live on click. theprojection is a static Hugo site; there is no
  live-generation plumbing today, and building one wasn't the ask.
- **Contents:** the named mechanism, confidence, each scenario with its
  precedent, the context note, and linked threads — matches the built
  page exactly (`layouts/interpretation/single.html`).
- **Route, confirmed:** `/interpretation/<slug>/`, parallel to `/claim/`
  and `/metric/` — `<slug>` is `<day>--<slugify(item title)>`, computed
  once in `render_read.py` and carried through to
  `tools/publish_projection.py`'s `data/interpretations.json` + one
  content stub per interpretation, same pattern as `/claim/<id>/`.
  Verified end-to-end with a real local Hugo build (0.111.3), not just
  component-level checks.

### 11. The standing capital-context artifact — BUILT 2026-07-30

**A macro-wide sibling to `attention/actor-doing.yaml`** (which holds a
per-actor "what are they doing now" synthesis) — but for the whole global
capital system rather than one actor. Daily interpretation **reads** this
snapshot to answer "how does this news item interact with the current
picture," rather than reasoning from nothing each time.

- **Cadence, confirmed: weekly, `/week`-adjacent** (Ben: "weekly yes
  week-adjacent sounds good") — `.claude/skills/week/SKILL.md` step 4b
  re-runs the 5 data-stack collectors and re-writes each `readings.*`
  entry; `/daily` never touches this file.
- **Read-only from `/daily`'s curation step**, confirmed — same "who
  writes what" discipline that keeps `threads.yaml`/`upcoming.yaml`
  main-session-only.
- **File + shape, confirmed:** `attention/capital-context.yaml` —
  `{asof, framing: {emphasis[], deprioritize[], notes}, readings:
  {<name>: {value, basis, sources[{figure,label,url,as_of}], as_of}}}`.
  First real snapshot has 5 readings (`rate_regime`, `cross_border_credit`,
  `external_position`, `fund_flows`, `conflict_risk_premium`), each
  sourced from the data stack in §12 plus the FOMC decision, GDP/PCE
  print, and the Iran conflict's Treasury sanctions action.
- **`/steer` support, confirmed** (Ben: "manual steer allowed to adjust
  the parameters by which the global context is built or framed") —
  touches `framing` ONLY, never a `readings.*.value` directly (a wrong
  reading is a collector bug, not a `/steer` edit). New verbs in
  `.claude/skills/steer/SKILL.md`: `/steer capital-context emphasize
  <thing>` · `deprioritize <thing>` · `note: <instruction>`.

### 12. The data stack behind it — WIRED 2026-07-30

Researched 2026-07-30 (two passes — conflict-detection sources and
capital-market-pricing sources), **all 5 built as real collectors the
same day** (`collectors/{treasury_tic,bis_stats,imf_data,epfr_flows,
fund_flow_reports}.py`), each independently live-verified against real
endpoints, not simulated:

| tier | source | tracks | lag | access | built |
| --- | --- | --- | --- | --- | --- |
| spine | **Treasury TIC** | foreign holdings of US securities | ~2mo | ✅ free, direct download | ✅ real data — Treasury's own TIC Table 5 pull, no key; 20 items/180d, matches known figures ($9,371.1B total, 2026-05) |
| spine | **BIS locational banking stats** + **Quarterly Review** | cross-border bank credit; the Review's own prose is the best model for §8's template | ~6wk | ✅ free, bulk + full-text PDF | ✅ real data — BIS SDMX 2.1 API (`BIS_LBS_DISS` dataflow) + sitemap-discovered Quarterly Review chapter pages; $45.97T cross-border claims (2025-Q4) matches BIS's own published number |
| spine | **IMF GFSR** + **BOP/IIP** | financial-stability narrative; cross-border transactions/positions | semi-annual / quarterly (~3mo) | ✅ free | ✅ real data — BOP/IIP via IMF's new `api.imf.org` SDMX endpoint (the documented `dataservices.imf.org` host is dead, DNS NXDOMAIN); GFSR itself pivoted to Crossref's DOI API since imf.org 403s everything including `robots.txt` |
| corroboration | **EPFR "Global Navigator"** newsletter | fund-flow trends, analyst-written | weekly | ✅ free, opt-in | ✅ real data — `epfr.com` redirects to `isimarkets.com` (EPFR's parent), which publishes it as full open articles, no login; 4 items/60d with real $ figures |
| corroboration | **Morningstar / ETF.com** fund-flow reports | US/ETF-only proxy for EPFR's paid data | — | ✅ free | ⛔ honest 0 — both sources are real and public in principle but bot-walled from this environment (Cloudflare JS challenge on etf.com incl. its own robots.txt; AWS WAF challenge on morningstar.com); the collector detects the specific challenge fingerprint rather than mis-parsing a block page as "no results" |
| not realistic | IIF Capital Flows Tracker, raw EPFR/Lipper, full sovereign-CDS history | the best single sources, if paid | — | ⛔ member/subscriber-gated | not attempted — gated as expected |

Also researched, adjacent to this but really World News's territory (see
ROADMAP §World News, built 2026-07-30): GDELT's Events table
(`GoldsteinScale`, `NumMentions`/`NumSources`), UCDP, ACLED, Lloyd's JWC
Listed Areas, the Baltic Exchange BDTI/BCTI. Where conflict *itself* gets
detected (World News) is a separate mechanism from where its
*capital-flow consequence* gets interpreted (this Part 2) — the same event
can and should feed both.

### 13. Pipeline — BUILT 2026-07-30 (as it actually shipped)

```
attention/capital-context.yaml    standing snapshot — refreshed /week-adjacent
       │  (5 collectors re-run in .claude/skills/week/SKILL.md step 4b)
       ▼
artifacts/digests/daily/<date>-global-capital.md    curation reads the
       │  + <date>-global-capital.interp.yaml         snapshot, writes
       │    (sidecar, keyed by slugify(bold lead phrase))  interpretation
       │  tools/readouts.py: validate_interpretation()   per item
       ▼
tools/render_read.py: parse_digest() loads the sidecar (global-capital
       │  scope only), attaches `interpretation` + `interpretation_id`
       ▼
data/payload.json items[].interpretation   → the internal read's inline band
data/interpretations.json                  → one entry per interpretation
content/interpretation/<id>.md             → one stub per entry
       │  Hugo (theprojection), layouts/interpretation/single.html
       ▼
/beat/global-capital/   the lens front — inline .interp-band under each
                        item that carries one (layouts/beat/single.html)
/interpretation/<id>/   the receipt: mechanism · confidence · scenarios ·
                        precedent · context_note · linked threads
```

Differs from the original proposal in two small ways, both simplifications
found while building: interpretations live in a **sidecar file**, not
folded into `readouts.json` (a cleaner separation — `readouts.json` stays
scope-keyed/fingerprint-cached, interpretation is per-item and generated
fresh each curation pass); and the receipt-page id is `<day>--<slugified
title>`, computed once in Python and reused everywhere, rather than a
separate id scheme per surface.

### 14. Open / parked (Global Capital) — resolved 2026-07-30

All six items below were open as of the original spec; all six are now
decided and built:

- ~~Exact lens slug~~ → **`global-capital`**.
- ~~Interpretation band's accent color~~ → **`#5A4B8C` / `#EEEAF7` tint**.
- ~~Receipt page route~~ → **`/interpretation/<day>--<slug>/`**.
- ~~`capital-context.yaml`'s refresh cadence and exact schema~~ →
  **weekly, `/week`-adjacent; schema in §11**.
- ~~Whether the standing context artifact ever takes a manual `/steer`-style
  edit~~ → **yes, but `framing` only, never a reading's `value` directly**.
- ~~Data-source wiring~~ → **all 5 built same day, 4 return real data, 1
  (fund-flow reports) an honest, evidenced 0 — see §12**.

**Genuinely still open, found while building, not part of the original
six:** the first `capital-context.yaml` snapshot was hand-assembled from
the collectors' verified test-run output, not yet through a real `/week`
run end-to-end — the next `/week` is the first live test of step 4b's
refresh discipline itself. "World News" / Big World News remains a
related but separate system (mechanical, not interpretive) — tracked in
ROADMAP.md, not part of this design.
