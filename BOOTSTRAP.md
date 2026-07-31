# BOOTSTRAP — standing kestrel up with zero bizdev coupling

*Reframed 2026-07-20 (Ben): **kestrel owes bizdev nothing.** The earlier
migration plan (move files, leave pointers, retire old paths, keep a
promotion pipeline into `citations.json`) is superseded. bizdev is a
**read-only quarry**: copy what's useful once, then it's kestrel's; we may
or may not refer to bizdev again later. Nothing kestrel does waits on, cleans
up, or writes back to bizdev.*

*Revised same day after a deep review (adversarial pass + reference-implementation
extraction — see `REBUILD-NOTES.md`). Key corrections: the zero-dependency rule
is scoped precisely; the judgment layer (curate + coverage critic) is now
specified, not hand-waved; every item has a done-when.*

**Scope of "zero dependency" (precise):** zero *bizdev code/runtime coupling* —
never import, call, or write to anything in bizdev after seeding. It does NOT
forbid: one-time seed copies (below), one-time reads of other knowledge for
seeding (internal research docs in the pm hub, CAPI canon in cloud-governor),
or shared workstation infra (`authctl`/`gorch` for Drive delivery — they're
platform, not bizdev).

**Health-check context (STATUS.md, 2026-07-20):** the bizdev digest operation
has been dormant since 2026-06-27/28 — no live system to coordinate with.
Launch fresh from here. **Runner decision: kestrel runs in this container**
(egress verified live 2026-07-20; authctl creds present). The reference's
cloud routine died on blocked egress — do not re-create a cloud runner
without first proving egress + creds there.

## Seeding (copy once — then the kestrel copy is the only copy that matters)

- [x] **Attention map — copied 2026-07-20** (`951ee87`): three files
      populated (ai + mental-health verbatim incl. critic auto-adds; Q1–Q6).
      ✅ **Re-triage answered 2026-07-22:** Ben resolved `gpt-5.6-release`
      and promoted all 6 candidates to open threads; 3 critic-adds applied
      by the first coverage pass the same day. Map was 16 threads then
      (**65 now**, 8 of them `kind: meta`), each with `entities:` +
      `weight:` (thread-centric reframe
      Phase 0 — ROADMAP §Delivery).
- [x] **Money lens — scoped + drafted 2026-07-20** (`f4d310a`): Ben's scope =
      capital-in-my-markets + macro backdrop + wealth/power (not trading
      signal); Q7 live in radar.md; `lenses.money` seeded (12 orgs → **15
      now**, 6 themes, draft). ⏳ Open with Ben: entity tuning + the
      CAPI-style people cohort.
- [x] **Feed set — done 2026-07-28** (finding: `/workspace/bizdev` DOES NOT
      EXIST in this container — the seed copy was impossible; feeds.yaml
      built FRESH, every URL live-probed, dead feeds kept w/ reasons; 28
      live: ai 16 · money 7 · mh 5; Cloudflare-challenge feeds caught by
      GET-probe — HEAD lies). Done-when met: loads clean + audit table
      (`python3 -m collectors.rss --audit-only`).
- [ ] **Prompts & thresholds** — copy-once seeds, same status as the
      attention map: the reference curate/coverage prompt rules and tuned
      constants (5am-ET boundary, 10am-ET coverage hour, pacing values) are
      distilled in `REBUILD-NOTES.md`. Start from them; diverge freely.
- [ ] **Keys & identities** — kestrel's own `.env` (+ `.env.example`):
      existing (OpenAlex — effectively required, CourtListener, DATA_GOV,
      LDA, OpenSecrets) **plus tier-2 signups by track**: FRED (money),
      LegiScan + Congress.gov + Regulations.gov + GovInfo (legal/leg),
      Semantic Scholar + GitHub (ai). Mint a kestrel `mailto` (never reuse
      the reference's). *Done when: every wired-or-next collector has its
      credential present or explicitly marked keyless.*
- [x] **Source knowledge — MOOT 2026-07-28**: /workspace/bizdev does not
      exist here; REBUILD-NOTES already distills what mattered. sources/sources.yaml
      notes now maintained from live evidence (e.g. the CourtListener
      quota finding).

## Building (fresh code — reference is reading, never imports)

*This is the collector + digest pipeline checklist. The **board / node +
claim graph** (`attention/board.yaml` → theprojection `/map/` + `/claim/`
pages) is a separate track — its schema shapes and state live in
[`DESIGN.md`](DESIGN.md), [`ROADMAP.md`](ROADMAP.md) rows 13–25, and
[`STATUS.md`](STATUS.md), not on this list.*

- [x] **Read renderer — built early, 2026-07-22** (reframe Phase 0):
      `tools/render_read.py`, the first judgment-free tool — deterministic
      page assembly from attention/ + tagged digests + timelines into
      `templates/read-shell.html`; byte-equivalent regeneration verified.
      Not on the original list; recorded here so the tools ledger stays
      honest. (Container note: needs the `tzdata` pip wheel — no system tz
      database; bake into env setup with the collectors.)

- [x] **Collectors — built 2026-07-28** (5-agent wave, P1+P2): **TWELVE
      live modules** — google_news_rss · rss · gdelt · sec_edgar ·
      federal_register · openalex · clinicaltrials · fred, plus the
      same-day tier-2 wave semantic_scholar · github · lda · fec — stdlib,
      live-proven; registry auto-imports; + tools/collect.py runner,
      tools/probe.py (7/7 UP verified), tools/pdf_text.py. CourtListener
      wired for TARGETED use only (quota — see sources/sources.yaml). The
      original "8 proven sources" target is met and passed; only LegiScan
      still awaits a key.
- [ ] **CourtListener decision** — test real search endpoints with the token;
      keep, degrade, or drop. *Done when: sources/sources.yaml status flips from
      `at-risk` to `wired` or `retired`, with the reason.*
- [ ] **Curation (the judgment layer — specified, not vibes)** — a
      `tools/curate` step: headless model call, **no web access**, works
      only from buffered files; per-lens rubric seeded from the reference
      rules (watchlist-entity priority, signal-over-noise, source-class
      trims, de-dupe vs. prior digest, carry threads on empty input,
      throughline + axis sections + 3-line summary); output rendered
      against a **fixed template** in `templates/` (not match-by-example).
      *Done when: given a real collected day, it emits all three lens
      digests conforming to the template, and a re-run is stable.*
- [ ] **Coverage critic (the recall guarantee)** — headless model call WITH
      web search, at finalize + weekly; **baseline = named benchmark
      publications per lens**: ai seeds from the reference set (Rundown AI,
      TLDR AI, The Neuron, AI Daily Brief; weekly + Import AI, Last Week in
      AI); ⛔ **mh + money benchmark sets are a Ben call** (reference had
      none for mh — a known gap, not a convention to keep). Misses append
      the coverage appendix, log to `coverage-log.md`, and auto-grow
      watchlist/threads for **all lenses** — with the YAML
      safe_load-or-git-revert guardrail. *Done when: one real finalized day
      produces the appendix, the log entry, and a guardrail-protected
      auto-grow.*
- [ ] **Digest state machine** — frontmatter states
      (`building | final` · `coverage: na | pending | done`), 5am-ET
      DST-aware day boundary (zoneinfo), freeze-then-critique ordering,
      finalize re-collects the precise final window. *Done when: a
      building→final→coverage cycle runs across two consecutive days.*
- [x] **Backward crawl — done 2026-07-22** — per-thread, on-demand: crawl
      the external SoT backwards, emit a finding + bundle. Six `/crawl`
      backfills shipped 2026-07-22 with provenance bundles
      (`artifacts/bundles/`: gov-review, state-bans, china-stack,
      containment, kaiser, cxmt) — done-when met. GDELT past ~3 months
      routes through its BigQuery public dataset — ✅ **gcloud auth completed
      by Ben 2026-07-20, dry-run verified from this container** (a personal
      Google account and GCP project); full-depth crawls are unblocked.
      (The interim path is agentic web sweeps; the automated collector code
      is still open under Collectors.)
- [x] **Weekly synthesis + near-miss audit — done 2026-07-27** (first
      fixed-week `/week`, run late for wk 07-20): 3 weekly digests written
      against the radar questions with near-miss audits fed by the week's
      coverage-log — done-when met. (Interim agentic mode; the automated
      weekly tooling still rides Collectors above.)
- [x] **Steering-loop surfaces** (AGENTS.md §steering loop, Ben 2026-07-20) —
      the daily template carries a **map deltas** section (added/dropped/why,
      with provenance tags) and a **thread candidates** section (1–3 "track
      this?" offers); the weekly template carries the **decay review** (prune
      candidates by aging `last_seen`). Map edits happen only through the
      loop. *Templates + command skills shipped 2026-07-20 (`9d0b72f`) —
      done when: one daily ships with deltas + candidates and one weekly
      ships with a decay review Ben has answered. **Done-when met
      2026-07-27:** the daily half landed 07-20 (briefing #0), and the
      first `/week`'s decay review was answered by Ben same-read (5
      verdicts applied: Jalapeño folded, apple-gemini kept+crawled,
      lab-IPO meta opened, gap-day rule, sk-hynix/micron wired).*
- [ ] **Delivery + feedback** — **surface decided 2026-07-20 (Ben): dual**
      — artifact page for reading (live, URL in `ROADMAP.md` §Delivery;
      re-published each `/daily`) + the Drive comment loop below, which is
      **gated on Ben's go** ("note it, don't build it yet"). The build:
      kestrel's own Drive folder; stable Doc per
      day upserted by title (destructive replace stays opt-in); comment
      pull (resolved excluded, quoted anchors kept) → dated feedback files;
      **ET digest-day used consistently** (the reference's UTC-yesterday
      mismatch dies here). Confirm which Google account owns the folder
      before wiring. *Done when: push → comment → pull round-trips on a
      real digest.*
- [ ] **Launch** — first kestrel daily digest ships **with the critic live**
      (a digest without the critic is explicitly labeled "no recall
      guarantee" and doesn't count as launch); weekly follows the first
      Saturday after. *Done when: two consecutive coverage-checked dailies
      + one weekly have shipped from this container.*

## Evidence, without bizdev

No promotion pipeline into `citations.json`. When an artifact's claim needs
durable evidence (the cited page could vanish), the capture lives in that
artifact's **bundle**. On disk:

- `provenance/` — **per-run** fetch manifests (every collector run writes
  one: source, params, fetched_at, item ids/urls).
- A **bundle** — **per-artifact**: `artifacts/bundles/<artifact-slug>/`
  containing `provenance.yaml` (the item list + pointers to the run
  manifests it drew from) and, only when evidence-grade, `captures/` of the
  cited source text. Daily digests get the lightweight form: a sidecar
  `<digest>.provenance.yaml`, no captures by default.

Kestrel owns its *outputs* (artifacts, bundles) durably — "never own" means
never owning the **source data**.

## Explicit non-obligations (superseding the old plan)

- No bizdev branch cleanup, STATUS fixes, doc reframes, pointer stubs, or
  path retirement — bizdev's state is bizdev's business.
- No sync-back of watchlist/thread edits, ever.
- No injest/lorchestra integration (architecture principle stands).

## Ben's calls

- ✅ **Buffer retention: 30 days** (2026-07-20) — cache semantics; deleting
  `buffer/` entirely must never lose anything. Diffable set (initial): Epoch
  AI CSVs — one prior snapshot each, prune-exempt.
- ✅ **Money lens scope + radar questions** — scoped 2026-07-20: capital in
  my markets + macro backdrop + wealth/power (NOT trading signal). Q7 live in
  radar.md; `watchlist.money` seeded (draft — Ben tunes entities; CAPI-style
  people cohort still to build with him).
- ✅ **Benchmark publications** — all three lenses set 2026-07-20, in
  `sources/benchmarks.yaml` (ai: Rundown/TLDR/Neuron/Daily Brief + Import
  AI/LWiAI weekly · mh: BHB/STAT/Fierce/MobiHealth · money: Money
  Stuff/Pro Rata/Unhedged/Bloomberg Tech + Odd Lots weekly).
- ✅ **`gcloud auth login`** — done 2026-07-20 (Ben, interactive); BigQuery
  GDELT backward-crawl path verified working from this container.
- ✅ **Delivery surface — dual** (2026-07-20): artifact page to read (live,
  URL in `ROADMAP.md`) + Drive Docs for comment steering; Drive build gated
  on Ben's explicit go.
