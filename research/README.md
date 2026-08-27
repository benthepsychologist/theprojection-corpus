# research/ — q1/q2/q3 real sourcing (build layer, not design)

This directory holds the first tranche of **real, cited data** for the
AI-buildout research program (kestrel's own q1–q4 namespace — not this
repo's `radar.md` Q1–Q7). The design is not here and is not repeated
here: it lives in `INBOX/`, and this directory follows it exactly.
**Read the design before touching this data:**

**`PRINCIPLES.md`** — durable schema-design principles distilled from
Ben's rulings (P-01, P-02, ...), separate from the frozen R-01–R-20
rulings register below: rulings are one-off decisions with their own
date/context, principles are the general rule a ruling revealed. Check
this file before designing any new schema field anywhere in `research/`.

1. `INBOX/2026-08-03-where-we-are.md` — orientation.
2. `INBOX/2026-08-03-q1-skeleton-v3.md` — q1's schema + rulings register
   (R-01–R-20, binding — do not relitigate here).
3. `INBOX/2026-08-03-q1-step0-audit.md` — the 56-record shelf audit this
   data's Tier-A tranche starts from.
4. `INBOX/sotg/` — the state-of-the-game sweeps confirming Epoch AI's
   dataset covers ~80% of q3's census for free, and that the JOINS these
   skeletons specify (who-pays-whom, owner/operator/propco/tenant) exist
   nowhere else as data.
5. `INBOX/2026-08-03-q2-skeleton-v3.md` — q2's design (not yet built on;
   this directory has no q2 content yet).

## Layout

- **`q1-flows/`** — the flow map (q1 skeleton sec 3): entity×activity
  `nodes.yaml`, money/capacity `edges.yaml` (each edge carrying at least
  one full observation per sec 4's schema — value, stage, basis, source,
  provenance_class, reliability, rationale), and `filters/` (named,
  versioned consolidation cuts per R-16 — the map itself stays
  classification-free).
- **`q3-datacenter-census/`** — the attribution layer over Epoch AI's
  datacenter census (`sources/external/epoch-datacenters/`):
  `attribution.yaml` (owner/operator/propco/tenant/end-user per facility,
  the split Epoch's own schema does not carry) and `control-cuts.yaml`
  (the taxonomy those records use).

## What's actually in here as of this build (2026-08-10, two passes)

Coverage is asymptotic by design (R-19, no done state) — this is not a
complete pass at any point.

**First pass:** 17 q1 flow edges (mostly re-expressing the step-0 audit's
16 VERIFIED-LIVE records as proper flow edges, plus one high-confidence
PARTIAL and two genuinely new flows found and independently
fetch-verified — the Anthropic-xAI and Google-xAI Colossus capacity
leases, neither in the original 56-record shelf); 24 q1 nodes; one q1
consolidation filter (`cut:core-buildout` v1); and 28 q3 facility
attribution records (the top facilities by current MW in Epoch's census,
three of them real owner/operator/propco/tenant corrections to Epoch's
own single-field "Owner" tag — Abilene, Denton, Fairwater Atlanta — found
by tracing Epoch's own citations further).

**Second pass** (same day, Ben's rulings applied): introduced the
**round-node pattern** (Ruling 1) — a new node kind for financing EVENTS
with 2+ investors, replacing the first pass's `ext/investor-syndicate--*`
placeholder — plus a new `memberships.yaml` file for the `is_member_of`
edges it requires; **lowered the materiality floor** from ~$1B to ~$100M
with a signal-biased override (Ruling 2) and added 8 new financing rounds
under it, several well under $1B; and built out Tier-A coverage for six
previously-uncovered activities (power generation, grid interconnection,
semicap beyond TSMC, memory/HBM, advanced packaging, networking, and
datacenter construction as its own purchase category). Net: **edges.yaml
now carries 44 edges** (17 retrofitted/unchanged + 27 new), **nodes.yaml
143 nodes**, a new **memberships.yaml with 81 `is_member_of` edges**, and
`cut:core-buildout` is now **v2** with roughly triple the original
roster. Full build report (scoping estimate, threshold rationale, open
judgment calls) handed to Ben alongside this pass.

**Third pass** (2026-08-10, three more rulings applied plus a "continue
the build" instruction): **Ruling 4** — debt syndicates now get the SAME
round-node/`is_member_of` treatment as equity rounds when 2+ lenders are
named (reversing pass 2's judgment call to keep debt off the pattern).
The one existing debt edge (JPMorgan Chase's $2.3B Crusoe/Abilene
construction loan) was independently re-verified this pass and confirmed
to have exactly one lender — it correctly stays a plain edge, not a
retrofit. **Ruling 5** — the round-node schema's `lead` field (a single
nullable slot) couldn't represent a real co-lead (Cohere's 2025 round,
Radical Ventures + Inovia), so pass 2 had silently picked one and
demoted the other. Fixed: `lead` → `leads` (a list); both flagged
demotions (Cohere 2025, Together AI 2025 Series B) corrected to record
every named co-lead as `role: lead`. The general principle is now
recorded durably in **`research/PRINCIPLES.md`** (new file, P-01 — "a
schema field must match the real-world cardinality of what it
represents"), separate from the frozen R-01–R-20 register. **Ruling 6**
— light-touch reworded the Nvidia cross-membership note in
`cut-core-buildout.yaml` so it reads as documentation, not a pending
question. **Continue the build** — two previously-uncovered categories:
debt/project-finance structures beyond simple construction loans (bond
issuances, private-credit facilities, infrastructure-fund JVs,
sovereign-backed project finance — CoreWeave's Blackstone+Magnetar and
JPMorgan+MUFG co-led facilities, Meta's and Oracle's bond/preferred
issuances, the Meta/Blue Owl Hyperion JV, the pending Vantage/MUFG $22B
facility, and the Stargate LLC joint-venture structure), and
international (non-US) financing rounds filling the US-tracker bias gap
(DeepSeek — a confirmed **negative** finding, no external financing
through 2025 — Moonshot AI, Helsing, Synthesia, G42, and Humain's $3B
check into xAI's Series E). Net: **nodes.yaml now carries 180 nodes**
(+42), **edges.yaml 66 edges** (+22), **memberships.yaml 114
`is_member_of` edges** (+33), **26 round nodes total**, and
`cut:core-buildout` is now **v3**. Every new figure carries a real,
fetched citation; every referential edge/membership resolves to a real
node id (swept via `yaml.safe_load` + a full from/to/leads integrity
check after every write this pass).

**Fourth pass** (2026-08-27, an undocumented interim commit
`e58a324` on 2026-08-13 had already added five more financings —
Nvidia's $500B six-firm compute-financing-platform MOU, CoreWeave's
second Q2 debt facility, Intel's first capital node, Lambda's
leveraged loan, TSMC's capex approval, and Google's targeted bond —
before this pass's own starting point of 189 nodes/72 edges/114
memberships; this write-up covers only the new fourth-pass work).
Ten real, cited financings from the 2026-08-13 to 2026-08-27 window:
Nvidia's $105B residual-value guarantee backing OpenAI's 20-year Ohio
data-center leases (plus a separate $1.5B Nvidia cash investment in
the landlord, SB Energy) — both sourced directly from Nvidia's own SEC
8-K exhibit and newsroom release; Nvidia's $6B Poolside "Model Factory"
license plus a separate $1B Poolside equity investment; Broadcom's
reported (not yet closed) $70-100B SPV debt package for Anthropic's
chip capacity, with Apollo and Blackstone named as junior-tranche
capital — modeled with the Ruling-4 round-node/membership pattern,
total left `null` given genuine cross-source disagreement on the
actual figure; Anthropic's $45B/6-year, ~460MW Nscale compute lease
(West Virginia's Monarch campus, Nvidia Vera Rubin chips); Groq's
$350M Series A down-round ($3.5B valuation, down from $6.9B, led by
Disruptive with Nvidia participating) as it pivots to a neocloud;
Nvidia's $2B Lancium investment (~20% stake, tied to the same Abilene,
TX "Lancium Clean Campus" already referenced unlinked inside Crusoe's
2024 JV note) and its confirmed-but-undisclosed-amount minority stake
in Cloverleaf Infrastructure; Alibaba's $10.2B Hong Kong share
placement (100% earmarked for AI, alongside a 75% profit decline and a
$6.6B free-cash outflow the same quarter); nVent Electric's $1.75B
(+$550M earnout) acquisition of Maverick Power; Infineon's acquisition
of C2i Semiconductors (terms fully undisclosed — recorded
`coverage_state: unmeasured`); and two new debt edges off SoftBank's
existing capital node — a ¥1T (~$6.3B) retail bond pricing 09-04, and
a separate $10-20B wholesale bond still at the "considering options"
talks stage (`stage: guidance`), to refinance SoftBank's OpenAI bridge
loan. Net: **nodes.yaml now carries 204 nodes** (+15), **edges.yaml 86
edges** (+14), **memberships.yaml 118 `is_member_of` edges** (+4), two
new round nodes (Broadcom's SPV facility, Groq's Series A). Every new
figure carries a real, fetched citation; unmeasured/undisclosed terms
(C2i's deal terms; Cloverleaf's exact check size) are recorded as such
rather than estimated; every referential edge/membership/leads
reference resolves to a real node id (swept via `yaml.safe_load` + a
full from/to/leads/partners integrity check after every write this
pass — this sweep also surfaced two PRE-EXISTING, not-this-pass
`instantiated_by` references on `amazon/ai-compute-procurement` and
`talen-energy/capital` pointing at an edge id that doesn't exist in
`edges.yaml`; left alone as out of this pass's scope, flagged for a
future cleanup pass).

**Held for Ben this pass** (genuine schema judgment calls, applied
with the most defensible available choice and flagged inline in the
YAML at the exact spot, not resolved unilaterally): (1) whether a
Nvidia-style backstop/guarantee (the Ohio guarantee, and the earlier
compute-financing-platforms edge it was modeled after) deserves its
own edge `type` value the way `grant / subsidy` was added in pass
three, rather than reusing `type: equity` as a loose fit; (2) whether
`type: asset purchase` — originally scoped to EPC/construction
contracts — should extend to outright whole-company M&A (applied this
pass to nVent/Maverick Power and Infineon/C2i Semiconductors); (3)
which `destination_category` an IP/software license purchase (the
Poolside Model Factory license) belongs under, given none of the nine
existing values fit a non-physical asset — recorded `other/unallocated`
this pass; (4) whether `cut:core-buildout` (still v3, untouched this
pass per instructions) should be bumped to v4 to add several
plausible new members — Broadcom and Groq as AI chip lines, Nscale,
Lancium and Cloverleaf Infrastructure as datacenter builders/AI-power
projects, and arguably Poolside as a frontier lab — all of which sit
outside the filter entirely right now, neither `members` nor
`explicitly_outside`.

## Discipline (inherited from this repo's root CLAUDE.md, restated here
because this directory is new)

- **Never fabricate a figure or URL.** A number genuinely not disclosed
  anywhere is recorded as `unmeasured`, never estimated silently.
- **Every YAML file here is validated with `yaml.safe_load` on write** —
  an unvalidated LLM-edited YAML file is reverted, not shipped.
- **Import sources to verify and reconcile, never as truth to copy** —
  same rule this repo already applies to Epoch's dataset
  (`sources/external/epoch-datacenters/PROVENANCE.md`).
- **This is not attention/board.yaml.** Nothing here feeds `/publish` or
  the site automatically; it is a separate, standalone data layer for the
  research program. Do not wire it into the board/claims pipeline without
  a deliberate design decision — that integration question is open (see
  the build report handed to Ben alongside this directory).
