# ROADMAP — kestrel

*Decisions and sequence, hand-maintained. Build mechanics + done-whens live
in [`BOOTSTRAP.md`](BOOTSTRAP.md); live state in [`STATUS.md`](STATUS.md).
Refresh when a decision lands or a phase completes.*

## Delivery — dual surface (decided 2026-07-20; reframed 2026-07-22, Ben)

The digest markdowns in `artifacts/digests/daily/` are the **archive**,
never the reading surface. Two surfaces, split by job:

1. **Artifact page — the read. ⛔ RETIRED 2026-08-25** (Ben: "that
   predates the actual website... kill it utterly"). Was live 2026-07-22
   through 2026-08-25 at a stable private URL
   (`https://claude.ai/code/artifact/f2ca5acd-f093-4803-a75b-467afe02c639`,
   left unrepublished, not deleted). It predated `theprojection.org` (the
   real public site — built later, not part of this "dual surface"
   heading's original two) and had become a repeated size/Artifact-refusal
   fight every `/daily` run for a reader nobody was using once the site
   existed. The `/daily`/`/week` republish steps are
   gone; `render_read.py`'s parsing helpers survive and now serve the
   public-site pipeline instead (`readouts.py`, `publish/adapter.py`) —
   see AGENTS.md discipline 8. The rung-ladder plan below was written for
   this surface and is now moot in full, kept only as design history.

2. **Drive comment loop — the steering channel. 📋 DECIDED, NOT BUILT.**
   (Ben, 2026-07-20: "note it, don't build it yet.")
   Push each day's digests as Google Docs to kestrel's Drive folder; next
   morning's `/daily` pulls the prior day's Doc **comments** back in as
   feedback/steering. Builds when Ben calls it. Drive access rides platform
   infra (authctl — `gdrive:acct1`/`acct2` creds verified present
   2026-07-22; push script not built) — not bizdev.

### The live-page rung ladder (designed 2026-07-22; plan on file)

- **Rung 1 — inlined payload. ✅ BUILT.** Whole week inline (~100 KB
  interim; ~1 MB with real collectors — fine). Soft cap 600 KB with a
  pre-defined degradation rule (shell header).
- **Rung 2 — `mcp`+Drive lazy-load. 📋 designed, not built.** Inline hot
  week; cold depth (prior weeks, full thread archives) fetched on click
  from a `kestrel/render/` Drive folder via the viewer's Drive connector.
  **Climb when any of:** payload > ~1.5 MB · Ben reaches for pre-week
  history in the page > ~once/week · threads > ~30 wanting the archive
  tier · the comment loop gets its go. **Gates before wiring:** confirm
  the push account matches Ben's claude.ai Drive connector account
  (acct1 vs acct2); one observation session for the Drive tool's real
  request/response shape. Discipline: Drive render files are a disposable
  derived cache — deleting the folder loses nothing; full regenerate on
  every push, never append/merge on Drive.
- **Rung 3 — write-back steering from the page. ⛔ ceiling, Ben's call
  only.** "Track this" buttons writing steering files via the Drive
  connector; competes with the gated Docs comment loop.

## Salience, summaries, and the flash rail (BUILT — Ben, 2026-07-29)

> **Status: shipped the same day it was specced.** Ben's three decisions:
> **`critical` only reaches the rail**, **neutral register** for summaries,
> and **yes, the flash publishes to theprojection** — *"this is MY news feed
> FIRST. If its big world news it affects finance so its cohesive."* Built
> across `render_read.py`, `read-shell.html`, `publish_projection.py`, a new
> `layouts/partials/flash.html`, and `attention/flash.yaml`. What remains
> unbuilt is named in §6.

**The problem, found by Ben reading the page 2026-07-29:** the reading
surface ranks by **volume** and has no concept of **imminence** or
**magnitude**. It answers *"what got written about most this week,"* not
*"what should I look at first."* Measured that morning: the week's four
biggest scheduled events ranked 17th (`meta-capex`), 31st
(`arm-royalty-regime`), 34th (`qualcomm-dragonfly`) and *below every
thread card* (`fomc-july-decision`, which has `thread: null`), while
satellite-confirmed missile strikes on AWS data centres were visible only
as one bullet inside a mid-ranked thread. Ben: *"why is the giant set of
earnings this week not at the top of the feed… big world news always
lands. 9/11? front-page."*

**Applies to both surfaces** — the artifact read page AND theprojection.
Same payload contract, same ordering, different skins.

### 1. Page order — fixed, every page

1. **🚨 Flash rail** — if an active flash exists. Full width, above
   everything, unmissable.
2. **Executive summary** — a verdict line + 3-5 bullets.
3. **⏳ Today's calendar** — expectations due today/tomorrow, **including
   `thread: null` ones**. This is the specific fix for FOMC landing at the
   page bottom.
4. **Ranked content** — threads by the salience score below.
5. Everything else (loose items, entities, archive).

### 2. Salience score — replaces pure volume

```
score = weight × (V + I) + M

V (volume, what exists)     = 2×today_items + week_items        # unchanged
I (imminence, what's due)   = Σ over the thread's pending expectations:
                                due today       → 6
                                due tomorrow    → 4
                                due ≤ 3 days    → 2
                                due ≤ 7 days    → 1
                                passed-silent   → 5   (the loud outcome)
M (magnitude, how big)      = 8×flash_items + 3×major_items
```

- **`I` is why the earnings gauntlet was invisible** — dated expectations
  currently contribute **zero**. With `I`, a weight-2 thread whose print
  lands today scores 12 before a single item exists, which is correct: the
  reason to look at it is that it is *about to* move.
- **`M` is additive and NOT multiplied by weight** — a major event on a
  weight-1 thread is still major. Weight amplifies *ongoing attention*,
  not *magnitude*.
- **`M` needs a new curation field:** extend the item annotation to
  `<!-- k: t=… e=… axis=… sev=major|flash -->`. Default (absent) = 0.
  Discipline: `sev=major` is rare, `sev=flash` is exceptional — see the
  bar below.
- **Meta-threads** aggregate children's `V` and `I` as today (computed at
  render, never stored); `M` does NOT aggregate — a child's flash belongs
  to the child, or it goes on the rail.

### 3. The flash rail — "big world news always lands"

For events that would lead a *general* news front page, **whether or not
they touch our three lenses**. 9/11, an invasion, a head-of-state
assassination, a market-halting crash. Ben's requirement is that these
cannot be filtered out by a lens model that doesn't know what they are.

**New file `attention/flash.yaml`** (cross-lens, so it can't live in a
per-lens digest frontmatter):

```yaml
flashes:
  - id: iran-strikes-us-base-jordan
    date: 2026-07-28
    severity: critical | major
    headline: "one line, plain, no hedging"
    body: >
      two sentences maximum — what happened and what is verified
    sources: [{label: "...", url: "..."}]
    lenses: [all]              # or a subset when it genuinely is scoped
    filed: 2026-07-28          # OPTIONAL — the day it was WRITTEN; defaults to
                               # `date`. Set it explicitly on a LATE catch so
                               # the 24h runs from the catch, not from the
                               # event you missed.
    expires: 2026-07-29        # OPTIONAL and can only ever SHORTEN. A value
                               # LONGER than the filing day is IGNORED.
    logged_by: ben-steer | curate-add
```

**Lifetime — 24 HOURS, ENFORCED IN CODE (Ben, 2026-08-04: "24h and gone").**
A flash renders on its **filing day and no longer**. The cap is computed by
`render_read.flash_last_day()`, which every surface goes through (read page,
publish adapter, readout fingerprints all call `load_flash()`), so there is
exactly one place this is decided. An entry with no parsable `filed`/`date`
does not render at all.

⚠️ **This replaced a convention that did not hold.** The 24h rule lived only
in AGENTS.md discipline 10 from 2026-08-01, while the loader honoured whatever
`expires` the curator hand-wrote — so real rail time on the six live entries
was **2, 2, 3, 3, 4 and 4 days**, and a flash with no `expires` at all never
expired. Writing a longer `expires` is now a no-op. If a story still warrants
the rail tomorrow, that means a NEW event happened, and the
new-event-never-a-running-state rule already says to file a new flash for it.
`/week` still prunes expired entries, but that is now cosmetic tidying: an
expired entry cannot render regardless.

**The bar, deliberately high:** normally **at most one active flash**;
two is exceptional; three means the bar has drifted and the rail is
worthless. A flash is not "our biggest story today" — the executive
summary already carries that. It is "you would want to know this even if
you had never heard of kestrel."

**Verification rule:** a flash carries the same primary-source discipline
as everything else, and an unverified flash says so on its face. Speed
does not buy an exemption — a wrong flash is worse than a late one.

### 4. Executive summaries — every page

Ben: *"LLM generated → automated/mechanical over time."* The path is
staged so the surface never depends on a model being clever.

| stage | how it's produced | status |
| --- | --- | --- |
| **1 — write it** | Curation writes it, as it already does | 🚧 mostly plumbing |
| **2 — assemble it** | Template fills from structured facts (top-N by salience, ledger flips, map deltas); LLM writes only connective tissue | 📋 |
| **3 — derive it** | Fully mechanical rendering of salience + ledger state; LLM reduced to the one verdict line, or dropped | 📋 |

**Stage 1 is smaller than it looks:** the daily digests' per-lens
**"Today's throughline" already IS the lens executive summary** — it is
simply never exported to the site. Promoting throughlines into the publish
payload gets AI / Finance / MH roll-ups almost free. Only the
**cross-lens front-page summary** is genuinely new writing.

**Scope by page type:**
- **Front page** — cross-lens: the day's highlights, 3-5 bullets, each
  pointing at a thread.
- **Lens roll-ups (AI · Money · MH)** — that lens's throughline verdict
  plus its own top movers. **Built 2026-07-29 as real lens pages**
  (`/beat/<lens>/` then; relocated to `/news/<lens>/` in the 2026-08-03
  restructure), each carrying a full morning briefing — see
  §Structured summaries below.
- **Leaf pages** (a single thread, node, or claim) — a one-line
  **standfirst**, not a summary. The page *is* the detail; a summary above
  it is noise.

**Payload contract:**

```yaml
summary:
  scope: front | lens:<lens> | thread:<slug>
  date: YYYY-MM-DD
  verdict: "the single most important sentence"
  bullets:                       # 3-5, front and lens pages only
    - text: "one line"
      thread: <slug>             # optional pointer
  generated_by: llm | template | mechanical   # honesty about stage
```

### 4b. Two adjacent gaps found while speccing this (2026-07-29)

- **⛔ The read page does not render meta-threads at all.**
  `render_read.py`'s `load_threads()` never exports `parent`, and the
  shell has no meta handling — so nesting is **modelled but invisible** on
  the artifact page, and the documented behaviour *"a meta-thread's
  ranking score aggregates its children's item counts"* (threads.yaml
  header, AGENTS discipline 7, since 2026-07-23) **is not implemented
  there**. `tools/publish_projection.py` DOES export `parent`, so the same
  nesting renders on theprojection but not on Ben's own read. Directly
  relevant: `china-duv-lithography` was nested under
  `china-stack-independence` on 2026-07-29 and that relationship currently
  shows nowhere on the read page. Fix alongside the salience work — the
  score formula has to know about children anyway.
- **✅ The `NEW ·` item badge exists and was dead.** The shell has
  `if(it.day===P.today) … "NEW · "`, which never fired for the same reason
  the top strip was blank (`P.today` naming a day with no items). Live
  again as of the 2026-07-29 fix — worth knowing before adding more
  salience chrome, since a working NEW badge covers part of what `sev=`
  is for.

### 5. Decided (2026-07-29) — was "open questions"

- **Flash severity threshold → `critical` only.** `major` still exists as a
  severity and travels in the payload so the executive summary can fold it
  in, but it never renders as a rail banner.
- **Does the flash rail publish? → yes.** Ben: *"this is MY news feed
  FIRST. If its big world news it affects finance so its cohesive."* The
  rail is server-rendered from `data/payload.json` into
  `layouts/partials/flash.html`, included from the masthead, so it appears
  on **every page** — homepage, thread pages, map pages, claim pages.
  Verified in a clean Hugo build.
- **Voice → neutral register**, the same frame-neutral voice the digests
  use. Not first person.

### 6. What is built, and what is not

*(This section used to restate the three questions §5 answers. They were
decided 2026-07-29 and the answers now live above; what belongs here is
the build state.)*

| | state |
| --- | --- |
| Salience score (`weight × (V + I) + M`) | ✅ built |
| `sev=` writer + the flash question in `/daily` | ✅ built (`842885b`) |
| Flash rail, `critical` only, on every page | ✅ built |
| Executive readouts, 157 scopes | ✅ built |
| Structured summaries + the morning briefing | ✅ built |
| Lens pages (`/news/<lens>/`, were `/beat/` before 2026-08-03) | ✅ built |
| Meta-thread CARD rendering on the read page | 📋 not built |
| Summary stages 2-3 (mechanise the words) | 📋 not built |
| Auto-regeneration of readouts inside `/daily` | 📋 not built |
| Bullet link rate (44% sitewide) | 📋 deferred to next `/daily` |

## Sequence

| # | what | state |
| --- | --- | --- |
| 1 | Briefing #0 (first `/daily`) | ✅ 2026-07-20 |
| 2 | Ben's steering on briefing #0 proposals | ✅ 2026-07-22 (all 7 applied) |
| 3 | Daily rhythm: finalize + coverage critic | ✅ first pass 2026-07-22 (covered the missed 07-21) |
| 4 | **Thread-centric weekly reframe, Phase 0** (timelines · entities · upcoming.yaml · annotations · shell + renderer · skills) | ✅ 2026-07-22 |
| 5 | Reframe Phase 1: 6 `/crawl` backfills (gov-review → state-bans → china-stack → containment → kaiser → cxmt) | ✅ all 6 same day, 2026-07-22 |
| 6 | Reframe Phase 2: first fixed-week `/week` with expectations scorecard | ✅ ran 2026-07-27 (late — wk of 07-20; 3 weeklies, 5 hits/0 passed-silent, decay review answered; the miss birthed the gap-day rule) |
| 7 | Finish seeding | 🚧 2026-07-28 — feeds.yaml ✅ (built fresh; bizdev absent — see BOOTSTRAP) · SOURCES fold-in MOOT · **keys = Ben signups pending** (.env.example scaffolded w/ URLs) |
| 8 | Collectors + judgment tools | 🚧 2026-07-28 — **collectors ✅** (7 live modules + runner/probe/pdf_text; /daily tier-1 now collectors-first) · P3 judgment tools (curate · coverage critic · state machine) remain — critic blocked on Ben's mh+money benchmark call |
| 9 | Drive comment-delivery build (§Delivery above) | ⛔ **HELD** (Ben, 2026-07-28) |
| 10 | Money lens tuning + CAPI-style people cohort (with Ben) | 📋 |
| 11 | Rung 2 live-page (§ladder above) | ⛔ **HELD** (Ben, 2026-07-28; climb triggers also unmet) |
| 12 | Public site: meta-threads + feed-card visuals + real thumbnails | ✅ 2026-07-23 |
| 13 | **The board** (`attention/board.yaml`: 56 orgs + 13 Houses) + the site `/map/` section (per-actor pages, swappable feudal/plain vocabulary) + `/classify` skill + `/steer` board verbs; threads grown to 43 | ✅ 2026-07-24 |
| 14 | **Framing change** — feudal rank ladder rejected → three **axes** (capitalization/optionality/gravity, **gravity stored gross — value-added deflation deferred until nation-state comparison**); sovereignty derived; `liege`→`depends_on` stubbed | ✅ 2026-07-25 |
| 15 | **Axis prototype** — 6 actors populated + cited (Microsoft/Nvidia/OpenAI/BlackRock/SpaceXAI/Alibaba); values on the board, source-appendix bundle per actor, finding `board-axes-prototype-2026-07-25` | ✅ 2026-07-25 |
| 16 | **Full board spin-up by pocket** — ALL major actors (money: Big Four asset managers **+ insurance** · power: hyperscalers + frontier labs · infra: foundries + chips · **+ a health pocket**; scope in `board.yaml` SPIN-UP SCOPE). Carries pending decisions: `capitalization`→`commanded_capital` rename, gravity value-added deflation (deferred), `pocket:` field, `jp` sphere, insurance/health roster confirm | ✅ **boarded + published live 2026-07-25** (10-agent wave `board-spinup-research-2026-07-25` → +21 orgs/+6 Houses; board now **77 orgs · 19 Houses**) |
| 17 | Render axes on the `/map/` pages + publish the board with values | ✅ **2026-07-26 — via the claims layer** (every value → a clickable `/claim/` receipt) |
| 18 | **Node model** — every actor a node with orthogonal `kind` (person/house/corp/state/agency/group) + `level` (L1/L2); pockets/sectors become **group nodes** (`member_of` edges, not tags) — 7 pockets + 4 sectors | ✅ 2026-07-26 (`3949400`) |
| 19 | **Claims layer** — every metric → a clickable `/claim/<node>--<dimension>/` page with cited per-node bundles; pocket/sector **aggregate claims**; **664 claims** (88 aggregate); schema in **[`DESIGN.md`](DESIGN.md)** (PKG/CAPI convention, file-based) | ✅ 2026-07-26 (`b76257a`, `ec91742`) |
| 20 | **Four-axis model** — prior-art research pass grounds every axis in an established formalization; **thrust promoted** (Damodaran reinvestment rate, extended), `capitalization`→`commanded_capital` **rename done**, gravity **un-deferred** → structural/attributable method (G-SIB substitutability × forward-linkage), optionality confirmed measured band (never thrust÷weight); `axes_num` numerics on a 21-actor pilot (5 derive-agents, sourced) | ✅ 2026-07-27 |
| 21 | **The plate + metric pages** — `/map/` opens on the thrust × gravity chart (size = weight · fill = optionality band · ring = sector · quadrants Builders/Bettors/Rentiers/Vaults); `/metric/` methodology pages (7 recipes + prior art); claim pages receipt-first; brand corrected (light-only restored, paper board-scoped, `#E01279` reserved, `--infra` #808040, Piazzolla self-hosted) | ✅ 2026-07-27 (site `3c06744`, build `23835d1d`) |
| 22 | **Most-deployable individuals** — a House-level axis: personal deployable capital, top-10 ranked + sourced (Musk ~$200B benchmark) | 📋 **DEFERRED to the end** (Ben, 2026-07-28: "individuals is a different direction, and I'm reworking CAPI a bit elsewhere") |
| 23 | **Government funding pockets** — US + Canada state-capital layer | ✅ 2026-07-28 — `gov-pool` pocket approved, 12 agency nodes + `canada` state seated (92 orgs), 4 threads opened (genesis-mission · chips-equity-pivot · dod-ai-consolidation · canada-ai-vs-care w3). **States/agencies go on a SEPARATE MAP** (Ben: "not competing for the same space") — plate excludes them; state-axes recipe question folded into row 24 remainder |
| 24 | **`axes_num` full rollout** — four-axis numerics for the rest of the corps (states/persons per-kind recipes later) + dep-only thrust across the board + sources into the -node bundles. (ASML/pockets sub-items done W3.) **Sequence set by Ben 2026-07-28: 24 → 23 → camellia → Intel commanded_capital call → rows 7-8.** Health layer explicitly in-scope (Ben mid-ramp: 'basically nothing in the health layer' — wave F axes + wave G digital-MH + wave I payer narratives). | ✅ **corps rollout DONE 2026-07-28** (9 waves, 53 orgs now carry axes_num; dep-only audit applied; welds; health axes+narratives). Remaining under this row: states/persons per-kind recipes |
| 25 | **Plate v2 (power view) + thrust rules + the build-out map** — plate re-encoded same day (size = gravity, heat = burn thrust÷weight, optionality columns, neon rings; v1's AUM-dominated sizing retired); thrust hardened (stakes in · depreciation-only, never amortization); **`attention/backlog.md`** created (W1 capex-picture crawls → W6) — the working queue for the board build-out | ✅ 2026-07-27 |
| 26 | **Salience + flash rail + executive readouts + structured summaries + beat pages** — thread rank by `weight × (V+I) + M`; `attention/flash.yaml` (editorial, `critical`-only); `tools/readouts.py` (BREAKING/NEWS mechanical, SUMMARY model-written); summary shape enforced as slots (`gist`/`bullets`/`watch`, or a fuller `lead`/`sections` briefing on front + new `/beat/<lens>/` pages) | ✅ 2026-07-29 (see §Salience, §Executive readouts, §Structured summaries) |
| 27 | **World News** — GDELT deduped + wired to `google_news_rss` clustering, matched against threads on two tiers, folded into `/daily`'s thread-candidate offering | ✅ 2026-07-30 (see §World News) |
| 28 | **Global Capital** — interpretive reframe of the money lens (standing macro-context artifact, fuzzy generated interpretation, receipt page, full rename) | ✅ SPECCED + BUILT 2026-07-30, same day (see §Global Capital) |

## Queue — surfaced, not yet decided

**What this section is for** (named and formalized 2026-08-09, Ben: "i
feel like i have to respond immediately or they are lost" — this is the
answer). A finding, friction point, or open question that surfaces
mid-session and doesn't need an answer in the same breath goes HERE
instead of being lost when the session ends. This section already
existed as "Open items" since 2026-07-20 — this is that same list,
formalized and dated consistently, not a new mechanism. It's the right
home because `/start` already reads `ROADMAP.md` on every session open
(the continuation briefing), so anything logged here surfaces again on
its own, unprompted, rather than needing to be remembered. Rules: every
entry gets the date it surfaced and who/what surfaced it; entries are
removed (not just checked off) once genuinely resolved, with a one-line
note of the resolution folded into whichever section actually owns that
decision (Sequence table, a discipline in AGENTS.md, etc.) — this list
is a waiting room, not an archive.

- **`research/`'s citation layer and the board's claims layer should
  eventually merge — confirmed direction, not built** (Ben, 2026-08-10:
  "so long as the merge is in the roadmap"). Today they're fully
  separate: the claims layer (`/claim/<node>--<dimension>/` pages) is
  tied to `board.yaml`'s axis values only; `research/`'s edges carry
  their own parallel citation format (`capture_ref`, source URLs).
  Nothing technically connects `attention/threads.yaml` to `research/`
  either — the relationship is "threads surface things research/ might
  want," a human/agent noticing overlap and manually promoting a news
  item into a cited `research/` edge, not an automated pipe. The
  plausible future shape: an interpretation citing a `research/` flow
  edge as its evidentiary basis, the same way it cites a news URL
  today. No design work done yet — flagging so the direction survives
  between sessions, per this section's own purpose.

- Interim-mode friction (2026-07-20): one lens sweep exhausted its
  web-search budget — mitigated 2026-07-22 by splitting the ai sweep in
  two; keep splitting on recurrence.
- Container gap (2026-07-22): no system tzdata — `tzdata` pip wheel
  installed user-level for zoneinfo (render_read + future collectors
  depend on it); bake into env setup when collectors land.
- **Structural source-access gaps** (surfaced 2026-08-09 `/week`) —
  **2 of 3 RESOLVED 2026-08-10** (`8832e1d`, see `sources/benchmarks.yaml`
  for the full writeup): FT Unhedged has a working public RSS endpoint
  (`ft.com/unhedged?format=rss`, no paywall gate); Behavioral Health
  Business's feed URL was already correct — the 403s were Cloudflare
  blocking WebFetch's own crawler signature specifically, not the URL;
  fixed by fetching via Bash/curl instead. **Axios Pro Rata still open,
  genuinely no automated path found** — a domain-wide Cloudflare block
  (the bare homepage and unrelated sections 403 identically), not a
  paywall or URL problem. Decision needed: drop it from
  `sources/benchmarks.yaml`'s critic set and accept the gap, or invest
  in a bigger fix (headless-browser render / non-cloud IP routing).
- **Thread-decay/retirement principle needs a real review — Ben doesn't
  have a settled view yet** (surfaced 2026-08-09 `/week`: "threads dont
  decay. not sure what our principle is here... no drops"). Seven
  threads this week's decay review flagged as genuinely quiet
  (`nuclear-for-ai`, `camellia`, `tsmc-capacity-race`,
  `qualcomm-dragonfly`, `mhpaea-parity-limbo`, `meta-gas-pivot`,
  `dod-ai-consolidation`) were all kept, none resolved/retired, per this
  ruling. AGENTS.md discipline currently reads `status: open | developing
  | resolved | retired (decay-review kill — folded/abandoned rather than
  concluded)` — that's the ONLY written principle, and it doesn't say
  when quiet becomes dead. Needs a real session with Ben to define it
  (a time bound? a "genuinely dead vs. just between developments"
  test? something else?) before the next `/week` decay review runs into
  the same ambiguity again.
- ~~PE clinical-DD / AI-liability underwriter candidates~~ **RESOLVED
  2026-08-10** — Ben: "yes to all four categories, add them." All 19
  names (11 PE behavioral-health roll-up sponsors, 8 AI-liability
  underwriting entities) added to `attention/watchlist.yaml`'s
  mental-health orgs block, with confidence caveats preserved as
  comments (`d5c5946`).

**Built 2026-07-29:**

- `attention/flash.yaml` — schema, the bar, lifecycle, and the first entry.
- Salience score live on the read page: `weight × (V + I) + M`, with
  meta-threads aggregating children's V and I.
- **`now` vs `today` split** — a subtlety found in testing. `today` centers
  the page on the newest *curated* day; `now` is the real digest-day.
  Imminence and calendar labels measure from `now`, or an event six hours
  away reads as "tomorrow." Both surfaces carry it.
- `⏳ Today & tomorrow` hoisted above the thread list, including
  `thread: null` entries — the FOMC fix.
- Flash rail on both surfaces; executive summary on both.
- `parent` + `genre` now exported by `render_read.py` (the meta-thread gap
  from §4b is half-closed: the payload carries it and the score uses it).

**Closed since this was written (2026-07-29, `842885b`):** `sev=` and
`flash.yaml` both have writers now — `/daily`'s curate step sets
`sev=major|flash` on the annotation when magnitude warrants it and asks
once whether the day warrants a FLASH, and `/week` prunes expired
flashes. The "summary is parsed as a single paragraph" gap is closed too;
see §Structured summaries below.

**Not built — named honestly:**

- **Meta-thread CARD rendering on the read page.** The score aggregates
  children, but a meta's card still doesn't list them as linked rows the
  way the threads.yaml header describes. Payload has what's needed.
- **Summary stages 2 and 3.** The summary is now *structured* rather than
  prose (slots a template lays out), but a model still writes the words.
  Stage 2 is deriving those bullets mechanically from the salience
  ranking; stage 3 drops the model to a single verdict line, or entirely.

## Executive readouts on every page (BUILT — Ben, 2026-07-29)

Ben, after seeing the first executive summary: *"not pretty or well
organized. bullet points that encourage me to click... leverage cheap
sonnet class LLMs to put an exec readout on literally every page.
timestamp behind the scenes. mechanical scan to see what needs updating…
that curated built understanding is the point."*

**Shape, per page:** `BREAKING` (same-day) · `NEWS` (last 7 days) ·
`SUMMARY` (the understanding). Rendered BREAKING → NEWS → SUMMARY rather
than the order Ben listed — same-day is a strict subset of this-week and
the more urgent of the two, so listing it second would bury it under
items it supersedes. Trivial to flip.

**The split that makes it cheap and safe:**

- **BREAKING and NEWS are mechanical.** `tools/readouts.py` derives them
  from the dated item record. No model touches them, so they cannot drift
  from what the digests say. Bullets link to the source, or failing that
  to the owning thread — never a dead end (Ben: "encourage me to click").
- **Only SUMMARY is model-written**, by sonnet-class agents, and only
  when a **fingerprint** over that scope's real inputs changes (item ids,
  timeline dates/headings, `last_seen`, pending expectations, active
  flashes). `--scan` reports staleness; a normal day moves a handful of
  scopes, not 157.
- **`front` prefers curation over the model.** `<date>-front.md` is
  written at curation from same-day verified facts and wins. Learned the
  hard way: the first model-written front pulled **Brent ~$100.69**, a
  07-23 level, into a day whose actual print was ~$87.7 — a 14-day item
  window drags stale figures forward. Packs now also label `watch` as a
  *standing question, not current fact*, which was the other half of that
  failure.

**Coverage: 157 scopes** — front, the three lenses, threads, entities and
board nodes that have any material. **Packability is judged on what the
pack will actually contain**, not on a raw item count: gating on the
latter passed 13 scopes whose only items had already aged out of the NEWS
window, so a model call was spent to answer "no activity" and that
non-answer rendered under a *Summary* heading. No breaking, no news, no
timeline entry → no readout, and `--export` prunes the stored record so
the section disappears. **Claim (753) and metric (8) pages are excluded by
design** — a claim page is one metric's receipt and a metric page is a
methodology note; a rolling news readout on either is noise.

**Pipeline:** `--scan` → `--pack-stale` (or per-scope `--pack`) → sonnet
agents → `--apply` (validates) → `--export` → `/publish --push` writes
`data/readouts.json` → the `briefing.html`/`readout.html` partials render
it on homepage, beat, thread, entity and map pages.

**Timestamp made visible (reversed 2026-07-30).** Originally rode in a
`title` attribute and a `<time datetime>` with `display:none` — Ben's
"timestamp behind the scenes" was read as "the *system* uses it
mechanically," not "hide it from the reader." That held until a lens
rename silently orphaned `lens:money`'s stored briefing (the new
`lens:global-capital` scope had never been generated, so its briefing
section just didn't render — Ben: "the briefing for Global Capital seems
to have disappeared") while the other three pages sat on a single
morning generation with no visible sign they'd gone stale mid-day. Fixed
two ways: the label dropped "Morning" (it can now regenerate any time of
day, not just once each morning), and `.briefing-stamp` is now visible
("Updated Jul 30, 9:58 PM UTC") instead of `display:none`, so staleness
is legible at a glance instead of invisible chrome.

**Display caps vs pack caps.** The rendered readout shows at most 6
breaking / 8 news — it is a glance, not an archive. The *pack* gets far
more (`PACK_LIMITS`, 30/60), because the same function feeds both and the
small cap is actively harmful on a wide scope: the front has 100+ items in
the window, so an 8-item pack handed the model an arbitrary 8 and hid the
day's actual leads from it. **A briefing cannot cover what it was never
shown.**

**Flash dismissal** (same session): a close button on the rail, **in
memory only** — no cookie, no storage, no query param — so it stays
closed for the view and returns on reload, which is exactly what Ben
asked for and is why there is no persistence code to go wrong.

**Not built:** stage 2/3 mechanisation of the summary itself (the shape is
now structured, but a model still writes the words — just a cheap one on a
tight trigger).

**The `LINK_FLOOR` validator rule (deferred 2026-07-29, built and enforced
2026-07-30):** `_check_link_floor()` now rejects an `--apply` payload
outright when fewer than 60% of a briefing's bullets carry a url and the
pack offered ≥3 linkable sources — a model that has links available and
doesn't use them fails validation the same as a bad shape, it doesn't get
silently stored. Caught for real the first time it ran under this rule:
the `lens:global-capital` regeneration came back 13/23 linked against a
30-source pack, got rejected, and was fixed by adding `/threads/<slug>/`
links to the unlinked bullets before re-applying.

**`/daily` step 6a now runs this pipeline every time** (folded in
2026-07-30 — see the daily skill), covering front + the 3 lens scopes
specifically, since those are the only ones with a `briefing` and the
only ones the public site's `/news/` dashboard + lens pages render. The other ~150
thread/entity/node `summary` scopes are a separate backlog, refreshed on
request rather than every run.

## Structured summaries + the morning briefing (BUILT — Ben, 2026-07-29)

Ben, on the first structured-summary pass: *"I wanted bullets and emojis
and delight. It's still just a paragraph."* He was right, and it measured:
**160 summaries, median 607 characters, zero newlines, zero bullets.**

**The fix is the SHAPE, not the prompt.** Asking a model for structure
does not hold — v1 asked and got 160 paragraphs. The store now holds slots
a template lays out, and `--apply` **rejects** what misses them:

| scope | shape |
| --- | --- |
| thread · entity · node | `gist` · `bullets` [{emoji,text,url}] · `watch` |
| **front · beat** | `gist` · `lead` · `sections` · `watch` (the briefing) |

**The briefing** (Ben: *"Morning briefing on the front page and on each
beat page… a little more chunky than the thread pages since presumably
more happened. It should COVER everything that's in the executive summary
now. Easier to scan, not less information."*) — `lead` is **3-5 bullets
ranked by salience with NO lens quota**; the front's `sections` are
**exactly the three lenses**, so nothing goes dark while the ranking stays
honest; a beat page's sections are real themes within it. **A fact
appearing in both `lead` and a section is deliberate** — the lead is the
ranking, the sections are the coverage. That is what makes it read as a
briefing rather than a list.

**Lens pages** (built 2026-07-29): `/news/ai/` · `/news/global-capital/` ·
`/news/mental-health/`. A lens had only ever been a client-side filter chip
— no page, no shareable URL, and nowhere for a per-lens briefing to live.
The dashboard chips stay filters; turning them into links would kill the
in-page filtering they exist for.

**Restructure, 2026-08-03 (Ben):** these were `/beat/<lens>/` and led the
site nav until the front page became a **projects hub** (three cards — News
· The Map · Research). The whole news surface — the dashboard, its filter
chips, the cross-lens briefing, and the three lens beats — moved under
**`/news/`** (beats now `/news/<lens>/`; `layouts/beat/` → `layouts/news/`;
the adapter writes `content/news/` since commit `dccb200`). The nav now
leads with **News**, not the individual beats. The projects-hub front page
carries no briefing of its own; the cross-lens front briefing renders on
the `/news/` dashboard.

**Emoji are typed** (money · legal · buildout · research · risk · health ·
geopolitics · market · deal · launch) and never carry a fact alone — the
voice pipeline strips all but six status emojis.

**Two rules learned building it, worth keeping past this code:**

- **A validator that makes good prose worse is the bug.** `_sentence()`
  tested the literal last character, so a sentence ending on a quotation
  failed. Three agents independently mangled correct punctuation — moving
  the period outside the quote, dropping the quote marks — to satisfy it.
- **Shape versions are per-shape, not global.** A global schema bump
  marked all 157 scopes stale for a change touching only front and beats.
  `SUMMARY_SHAPE_VERSION` / `BRIEFING_SHAPE_VERSION` each participate in
  their own scopes' fingerprints, so a shape change migrates through the
  normal scan → pack → apply loop without re-running the other shape.

## Global Capital — the interpretive reframe of the money lens (SPECCED + BUILT 2026-07-30)

**Origin:** Ben, reading the page 2026-07-30, on the money lens: *"'finance'
is boring, 'Global Capital' is interesting to me... it's not just
aggregating news items, it's reviewing them through this lens and offering
possible interpretations about how this might change the global picture. Or
regional picture."* Full schema in **[`DESIGN.md`](DESIGN.md) Part 2**;
this section is the decision log.

**The shape of the ask, as it landed across the conversation:**
- **Scope widens** — rates, war, risk reassessment become capital-flow
  *drivers*, not separate topics next to it.
- **Editorial mode changes** — interpretation, not just aggregation. Every
  relevant item can carry a generated reading of what it might mean for
  where capital moves, not just a sourced fact.
- **Interpretation stays visibly fuzzy** — real branching scenarios
  ("could go this way because X, or that way because Y"), not one
  hedge-everything paragraph.
- **Generated reasoning must be unmistakably generated** — its own visual
  band, distinct from sourced fact.
- **It must not invent on thin evidence** — a confidence tag, enforced like
  a validator, with an explicit rule: name a mechanism or a precedent, or
  mark it `speculative` and say why.
- **A deeper receipt exists behind a click** — historical precedent,
  the branching scenarios spelled out, links to background — same
  "summary on the surface" convention Part 1's claim pages already use.
- **Read against a standing picture**, not reasoned fresh each time — a
  persistent capital-context snapshot, refreshed from real macro data
  (Treasury TIC, BIS, IMF GFSR, EPFR's free newsletter — see DESIGN.md §12
  for the full free-vs-gated breakdown), that daily interpretation consults
  rather than inventing context from nothing.
- **This changes the beat, not just its label** (Ben: *"up and down the
  beat, not just the global label"*) — the watchlist scope, the thread
  genre, the digest axis list, the curation rubric all get touched.

**Decided in this design pass, and shipped the same day (2026-07-30):**

| question | decision |
| --- | --- |
| Trigger | per-item, where a real mechanism is identifiable (not forced onto every bullet) |
| Visual | its own labeled band, `--interp:#5A4B8C` / `#EEEAF7` tint — "look at it and make a call" |
| Guardrail | `speculative` / `plausible` / `well-supported`, enforced in `readouts.py`'s `validate_interpretation()` |
| Receipt generation | pre-generated + cached at curation time, not on-click |
| Standing context | yes — a macro-wide sibling to `actor-doing.yaml`, read-only from `/daily`, refreshed weekly (`/week` step 4b) |
| Lens rename | full — `money` → **`global-capital`**, the internal key changed everywhere, not just the display label |
| `/steer` on the context artifact | yes, but `framing` only — never a reading's `value` directly |
| Data-source wiring order | all 5, same day, not staged |

**Built same day — this is no longer a spec, it's running code:**

- `attention/capital-context.yaml` — the standing artifact, 5 real sourced
  readings (rate regime, cross-border credit, external position, fund
  flows, conflict risk premium). Refresh mechanics in
  `.claude/skills/week/SKILL.md` step 4b.
- `tools/readouts.py`: `normalize_interpretation()` +
  `validate_interpretation()` — the confidence/mechanism/precedent
  guardrail, verified against both a passing and a deliberately-broken
  case.
- The interpretation sidecar + receipt pipeline:
  `<date>-global-capital.interp.yaml` → `render_read.py`'s
  `parse_digest()` → `data/interpretations.json` →
  `content/interpretation/<id>.md` → `layouts/interpretation/single.html`
  at `/interpretation/<day>--<slug>/`. Verified end-to-end with a real
  local Hugo build, not just component checks — one real interpretation
  (today's GDP/PCE print) live on both surfaces.
- The lens rename across `watchlist.yaml`, 13 threads' `lens:` field (not
  ~12 — the actual count), `readouts.py`'s `LENS_SLUGS`/`LENS_LABEL`/
  `LENS_BEATS`, every collector that hardcoded `lens="money"`
  (`fred.py`, `sec_edgar.py`, `lda.py`/`fec.py` CLI defaults),
  `render_read.py`/`publish_projection.py`/`collect.py`'s lens constants,
  `read-shell.html`'s filter chips (with a `money`→`global-capital`
  backward-compat alias so pre-rename archive items stay findable), and
  theprojection's `hugo.yaml` nav + `/beat/money/`→`/beat/global-capital/`
  + `main.css` tokens. Digests dated before the rename keep their
  historical filename/frontmatter — not rewritten.
- Collectors for the DESIGN.md §12 data stack — all 5 built
  (`treasury_tic`, `bis_stats`, `imf_data`, `epfr_flows`,
  `fund_flow_reports`), 4 independently verified returning real live
  data, 1 (`fund_flow_reports`) an honest, evidenced 0 (both Morningstar
  and ETF.com bot-wall this environment).

**Related but separate — tracked here, not part of this spec:** "World
News" / Big World News, a cross-spectrum attention signal (mechanical, not
interpretive — detects *that* something is getting broad coverage, doesn't
interpret it). Distinct mechanism, same conversation; see the next section
— **built the same day**, not just specced.

## World News (BUILT — Ben, 2026-07-30)

**Origin:** a mechanical, cross-spectrum attention signal — what the whole
media ecosystem covers today, *"whether it's the New York Times or the
Atlantic or crazy right-wing conspiracy nuts"* — kept small on purpose so
it never competes with the three real lenses. Distinct from the flash
rail (editorial: "would this lead a front page," Ben's own call) — this
is a computed fact, no model, no judgment, same discipline as
`readouts.py`'s mechanical BREAKING/NEWS. **Now a real (narrow) fourth
lens** for threads that are irreducible to the other three — see
"Promotion rule" below — but detection stays exactly this restrained;
only the thread-hosting layer grew.

**Ben: "I don't want to wait a week... I want to figure out the whole
setup TODAY."** Built and backfill-validated same day, against three real
days (07-28/29/30) — not a week of live observation.

**What shipped:** `tools/world_news.py` clusters `google_news_rss` items
by shared title keywords and ranks by **distinct outlet count** — the
cheap MVP over the paid/enterprise-gated products (AllSides, Ground News,
NewsWhip) that build the same concept but don't offer a self-serve free
tier. Results persist to `attention/world-news.yaml`, a `flash.yaml`-
adjacent file with its own status vocabulary (`confirmed_thread` /
`candidate` / `dismissed`).

**Two real bugs found and fixed the same session — both worth keeping
past this code:**

- **A keyword-chaining clustering bug produced a nonsense 1,000+-outlet
  megacluster every single backfill day.** Comparing each new item against
  a cluster's ever-growing UNIONED keyword set lets the centroid drift —
  item A shares 2 words with B, B shares 2 *different* words with C, and
  unrelated stories chain together. Fixed by comparing against a FIXED
  centroid (the cluster's first item) plus a Jaccard-similarity floor, not
  an absolute shared-word count.
- **GDELT's raw ranking fields are noisy in two distinct, real ways**,
  confirmed live via BigQuery (`gdelt-bq.gdeltv2.events`, kestrel's
  existing verified GCP auth): `NumMentions` inflates on repeated
  re-crawls of a single outlet (top hit sorting by it alone: a Miley Cyrus
  retrospective from one local radio affiliate, `NumSources: 1`); `Num-
  Sources` inflates on syndicate networks (UK regional-paper groups
  republish identical wire copy across a dozen+ near-identical domains
  under one `SOURCEURL`, reading as "15 distinct sources" with no real
  editorial diversity). The real signal — the Iran/Iraq/Saudi conflict at
  `GoldsteinScale: -10.0` — is genuinely there underneath, but wiring
  GDELT in properly needs a real dedup pass (group by near-identical
  SOURCEURL/headline, treat Goldstein/QuadClass as a severity filter, not
  the detection mechanism). **Correctly scoped as follow-on work, not
  faked through today.**

**Validation, once fixed:** of today's (07-30) top 12 clusters by distinct-
outlet count, **9 independently confirmed threads already on the map**
(`grok-companion-harm`, `openai-agent-security-incident` ×3, `meta-capex`,
`red-sea-oil-shock`, `china-duv-lithography`, `kimi-distillation-fight`,
`ai-memory-shortage`) — a judgment-free mechanical signal landing on the
same stories curation independently deemed important. **2 genuine
candidates surfaced with no existing thread**, logged plainly rather than
oversold (one thin PR-vision item; one likely two smaller stories merged
by a milder version of the same chaining artifact).

**Known limitation, named honestly, not fixed:** a fast-evolving,
multi-day conflict story doesn't cluster into one bucket the way a
single-consistent-headline story does — different sub-events (US strikes
Iran, Saudi joins Iraq, Kuwait hit) get different headlines day to day, so
the war surfaces here only through its stable financial-wire proxy ("Oil
jumps on Middle East tensions"), not as itself. Exactly the gap GDELT's
structured actor/event-code approach is suited to close.

**A finding that reframes the whole effort:** kestrel's existing
collection is **entirely watchlist/thread-term-driven** — `red-sea-oil-
shock` only catches Iran items because its own terms include "Iran Saudi
oil shock." A story with zero overlap with any tracked term would never
appear in the buffer at all, regardless of size. This is why an untargeted
source (GDELT needs no query term) matters, and why this signal can never
be *fully* independent of kestrel's own judgment while it leans on
`google_news_rss` alone.

**Promotion rule** (Ben: *"if it's worthy of my attention it's worthy of
potentially covering"*) — a `candidate` item is offered exactly the way
any other thread candidate is, in the digest's own Thread candidates
section. No separate promotion mechanism. **A promoted candidate becomes
a `lens: world-news` thread** (2026-07-30, Ben — asked directly: "where
does Iran and Ukraine war go... what do the threads hang off of?") — a
fourth lens, deliberately narrow: no watchlist entity sweep of its own,
no coverage-critic benchmark set, threads arrive only through this
mechanism. Carries its own thin daily digest alongside the three primary
lenses'.

**First real split, same day:** `red-sea-oil-shock` had been doing
double duty — conflict narrative and capital-markets read in one file,
`lens: money`. Split into `iran-conflict-widening` (world-news — who's
fighting whom, where it's widening, what diplomacy is doing) and
`red-sea-oil-shock` (money — oil/shipping/underwriting, kept, trimmed).
Same origin event, one thread per lens on purpose, not one thread
wearing two hats.

**Not built yet:**

| | state |
| --- | --- |
| Detection + backfill validation | ✅ built, same day |
| `attention/world-news.yaml` persistence | ✅ built |
| Page rendering (the quiet capped strip) | ✅ built + live, same day — both surfaces |
| GDELT dedup pass | ✅ built + validated, same day — `tools/gdelt_dedup.py` |
| GDELT wired into the live feed | ✅ built 2026-07-30 — `tools/build_world_news.py` merges both sources, uniformly matched against existing threads; 142 candidates generated for 2026-07-30 (54 confirmed, 88 held for review) |
| Automatic wiring into `/daily`'s thread-candidate offering | ✅ built 2026-07-30 — `.claude/skills/daily/SKILL.md` step 5, folded into the same 1–3 daily slots as curator-noticed candidates |
| `world-news` as a thread lens + its own thin digest | ✅ built 2026-07-30 — first thread `iran-conflict-widening`, split from `red-sea-oil-shock` |
| UCDP as a slower credibility cross-check | 📋 not built |

### The GDELT dedup pass (built same day, `tools/gdelt_dedup.py`)

Three-pass pipeline, all independently re-verified against the real
BigQuery output (not taken on the builder's word): **(1)** article-level
dedup — group by `SOURCEURL`, collapse GDELT's multiple event-rows-per-
article to one, fixing the `NumMentions` re-crawl inflation by
construction; **(2)** syndicate detection via exact (numeric CMS id,
slug) co-occurrence across domains, connected-components clustering, no
ownership database needed — recovered a ~61-domain Australian network, a
~50-domain UK Newsquest-style network, and a previously-unnamed ~22-domain
global content-syndication network, collapsing 168 domains into 17
networks; **(3)** story clustering on structured fields (sorted CAMEO
country-pair + event code when both actors carry a real CAMEO code;
location + actor name otherwise), with Goldstein/QuadClass carried as a
`CONFLICT`/`COOP`/`MIXED` **tag**, never a filter.

**A real bug found and fixed mid-build:** an early version coalesced
`Actor1CountryCode` (CAMEO, `"USA"`) with `Actor1Geo_CountryCode` (FIPS,
`"US"`) — two different code systems for the same country — manufacturing
spurious "bilateral" pairs like `('US','USA')`. Fixed by requiring both
sides be a true 3-letter CAMEO code before treating an event as
international.

**Validated, re-run independently against the cached data:** the Iran/
Iraq/Saudi/Kuwait/Egypt conflict surfaces clearly across several
country-pair buckets (`IRN-USA` 205 domains, `IRN-JOR` 164, `IRQ-SAU` 116,
`IRN-SAU` 94, `IRN-IRQ` 74 — all `GoldsteinScale` ≈ −10.0, maximum
conflict intensity) rather than one merged story — an honest, named
tradeoff of pairwise clustering. The Miley Cyrus/UK-syndicate noise from
the naive approach is confirmed suppressed: the same article that
inflated to `NumMentions: 220` off one outlet is now correctly one row,
appearing once, never surfacing in any top-N ranking.

**Cost, confirmed via `bq show`:** `gdelt-bq.gdeltv2.events` (904M rows)
has **no partition or cluster keys** — a date-range `WHERE` clause does
not reduce bytes scanned; cost is driven by column count alone (~165GB,
~$1/run regardless of a 1-day or 7-day window). Results cache to
`buffer/gdelt_cache/` (gitignored), so a repeat window is free.

**Named limitations, in the tool's own header, not hidden:** the
`domestic-generic` buckets are real category aggregations ("US +
Fight"), not single stories — GDELT's Events table carries no title/text
at all, so headlines shown are a best-effort proxy decoded from the URL
slug.

### Wiring GDELT into the live feed (`tools/build_world_news.py`, built 2026-07-30)

Merges `world_news.py`'s google_news_rss clustering with `gdelt_dedup.py`'s
GDELT output into `attention/world-news.yaml`, matched against existing
threads on two independent tiers — a headline naming 2+ recognized
countries uses ONLY a proximity check (both names within 400 characters
somewhere in the thread's full timeline text; closest match wins, no
fallback); everything else uses keyword overlap against the thread's
*short* fields only (title/terms/watch — never the full timeline, which
let incidental word co-occurrence in a long document outscore genuine
relevance). A hand-curated exclusion list (`MATCH_GENERIC`) keeps country
names, common AI-infra vocabulary (nvidia, blackwell, compute, silicon,
agent…), and bare years from driving false matches on shared background
words rather than real subject overlap — found by checking the full
written output against real threads, not just spot-checking a handful of
cases. Two `gdelt_dedup.py` bugs surfaced during integration and were
fixed there: a same-country self-pair miscoded as international
(`Actor1CountryCode == Actor2CountryCode` produced "United States–United
States"), and generic institutional/nationality nouns (POLICE, IRANIAN,
COMMUNITY…) slipping through as named actors.

First real run (2026-07-30): 142 items, 54 confirmed against existing
threads, 88 held as candidates. One known ambiguity accepted rather than
chased further: "Iran–Jordan: Fight" ties between `datacenters-as-targets`
and `red-sea-oil-shock` (28 vs. 25 characters) because both threads'
timelines legitimately discuss Iran and Jordan in adjacent context — a
real data ambiguity, not a matching bug.
