# research/ — q1/q2/q3 real sourcing (build layer, not design)

This directory holds the first tranche of **real, cited data** for the
AI-buildout research program (kestrel's own q1–q4 namespace — not this
repo's `radar.md` Q1–Q7). The design is not here and is not repeated
here: it lives in `INBOX/`, and this directory follows it exactly.
**Read the design before touching this data:**

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
