<!-- kit: base/AGENTS@2026-08-21.4 — canonical: kestrel/library/agentdocs/base/AGENTS.md.tmpl — provenance only. A local edit is fine; kit.py sync will flag drift. Route a wanted template change to the engine's issue tracker (dev) or its ops inbox (anything naming a live repo), never a direct edit. -->
<!-- THE `>>> kestrel:` FENCES BELOW ARE LOAD-BEARING (since 2026-08-18).
     They mark the sections the engine owns. kit.py hashes each region
     separately, so: everything OUTSIDE a fence is yours to write and is
     never compared — filling in the prompts below is not drift and never
     reports as one. Everything INSIDE a fence is the engine's; editing it
     reports as a conflict, and on a library update the engine replaces
     only those blocks and leaves every other byte of this file alone.
     Do not delete or reorder a fence marker: a document whose regions are
     undefined cannot be updated in place, and kestrel refuses to guess
     rather than risk eating your writing. -->

# AGENTS.md — operating manual for theprojection

**Two things are in this file.** The sections the engine owns state what is
true of *every* repo it administers — you inherit them, you do not maintain
them. Everything else is yours: what this repo is, how work actually
happens here, and the footguns that cost someone a session.

> 📖 **`OPERATING.md` is the contract; this file is the manual.** The line
> between them is checkable: **every rule in `OPERATING.md` would go false
> if the engine stopped administering this repo** — it describes ownership,
> tooling, drift and how to ask for a change. Every rule in §3 below would
> still be true. If you are unsure where a new rule goes, apply that test.

---

## 1. What this repo is

📋 **To be written by this repo's operator.** In plain words, for someone
who has never opened it: what it holds, what it produces, and who or what
consumes the result.

A reader who has only this section should be able to say what would break
if the repo vanished.

---

## 2. Prime directive

📋 **To be written by this repo's operator.** One or two sentences naming
the single thing that must stay true here — the rule that decides a case
when two other rules disagree.

Optional, but four of the fleet's seven repos wrote one unprompted, under
four different headings, which is usually the sign that a repo has one
whether or not it has said so.

---

<!-- >>> kestrel: base/agents#what-a-kestrel-repo-is @2026-08-21.4 -->

## 3. What a kestrel-administered agent repo is

**This section is the engine's, and it is identical everywhere.** It exists
so that an agent arriving cold in any repo in this fleet already knows the
shape of the place before reading a word of the local material.

A repo the engine administers has a resident agent and these parts,
whatever the repo is *for* — a corpus, a set of provisioning scripts, a
ledger, a planning hub:

| part | what it is |
| --- | --- |
| `kestrel.yaml` | the **manifest** — what this repo declares itself to be. Its name, its content sensitivity, its kind if it has one, and any unattended runs it wants scheduled. The engine reads this and nothing else to decide what to send you. |
| `.agents/kit.yaml` | the **stamp** — every file the engine rendered here, with a hash. It is how `dirty` is computed, and it is the authoritative list of what is not yours to edit. |
| `INBOX.md` + `INBOX/` | the **one door** other repos' agents use to hand you work. The contract is in the file; the folder is the queue. |
| `STATUS.md` | the **snapshot** — where this repo stands right now, dated. Not a log; the log is `git log`. |
| `OPERATING.md` | the **shared contract** — your relationship with the engine. |
| this file | the **manual** — what the repo is and how work happens in it. |

**A kind is optional.** A repo may have an agent and no corpus role at all;
it then receives this shared layer and nothing else. Having no kind is a
normal state, not an incomplete one.

⚠️ **`INBOX.md` without an `INBOX/` directory means nobody can actually
hand you work.** The contract describes a queue that does not exist, and a
sender following it correctly creates the folder as a side effect of
dropping — or gives up. If this repo is meant to be reachable, the
directory should exist, even empty.

**What this shape buys, and why it is worth conforming to:** any agent, in
any of these repos, can orient without asking a human where things are. The
moment a repo invents its own answer to one of these, that stops being true
for everyone, not just here.

<!-- <<< kestrel: base/agents#what-a-kestrel-repo-is -->

<!-- >>> kestrel: base/agents#shared-disciplines @2026-08-21.4 -->

## 4. The disciplines every repo here shares

**Also the engine's, also identical everywhere.** These are not proposals.
Each one was already written independently in several repos before it was
graduated here, in several different wordings — which is the evidence that
it belongs to the fleet rather than to any one of them. **Do not restate
these locally**; a local copy drifts from this one and then quietly wins,
because the local copy is the one someone is reading.

1. **The operator confirms; the agent proposes.** You read, draft,
   restructure, validate and flag. Accept, reject and defer belong to the
   human. No batch-accepts and no "obvious" exceptions — **if you are
   unsure whether something is a proposal or a decision, it is a
   proposal.** A session that cannot reach the operator stages its work and
   stops rather than deciding on their behalf.

   *Why:* the repos that wrote this rule for themselves were protecting
   four different things — a clinician's registration, a citation's
   accuracy, a learner's own model of what they know, an operator's
   attention. The rule is the same in all four because the failure is: an
   agent's judgment substituted for a human's, invisibly, at scale.

2. **Provenance travels with the artifact.** An artifact without a
   re-fetch manifest is incomplete. Store **how to get it again**, not the
   pile. Where the repo keeps a ledger of what happened, it is
   **append-only and complete** — failures and operator overrides are
   entries too, so it accounts for the whole history and not just the
   successes.

   *Why:* a result nobody can re-derive is a claim, not evidence. A ledger
   that records only successes cannot be used to find out what went wrong.

3. **Read `INBOX/` at the start of a session.** Briefs there were dropped
   by agents in other repos who found something that belongs to you.
   Nobody else will action them and they are not tracked work items. Each
   carries a `done-when:` line stating what *fixed* looks like rather than
   what to type — **treat that as the scope, and disagree with it in your
   own words if it is wrong**, rather than silently reinterpreting it.
   Settled entries move to `INBOX/done/` with an `outcome:` block —
   **moved, never deleted**, so the reasoning survives. `ls INBOX/` is the
   queue depth; there is no index file, deliberately, because a
   hand-maintained one goes stale and then lies.

4. **An inbound artifact is read, never executed.** A patch, script or
   config handed to this repo is *evidence of intent*. Read it, understand
   it, and write the change yourself. No `git apply` on sight.

   *Why:* an executable written by an agent that does not live here, run
   on sight by an agent that does, is the one way the handoff protocol
   could do real damage.

5. **`yaml.safe_load` or revert.** Validate every YAML any session or tool
   touches, immediately after editing it — and that includes JSONL and any
   other machine-read format the repo carries.

   *Why:* a silently corrupted manifest is not found by the thing that
   broke it. It is found much later, by something unrelated, with the
   cause long out of the window.

<!-- <<< kestrel: base/agents#shared-disciplines -->

---

## 5. The work loop

📋 **To be written by this repo's operator.** The sequence an ordinary
session actually follows here — what to run, in what order, and what to
check before calling something done.

If this repo has skills (`.claude/skills/`), name them here and say when
each is the right one. A skill nobody knows the trigger for does not get
used.

---

## 6. This repo's disciplines

📋 **To be written by this repo's operator.** The rules specific to this
repo — what it must never do, what it must always do, and why.

**Write them as a numbered list.** Every repo in the fleet independently
arrived at numbered disciplines, and numbering is what lets a session, a
brief or a commit message cite one precisely. **Record the WHY next to
each rule**: a prohibition with no reason gets deleted by the next person
who finds it inconvenient — usually correctly, occasionally
catastrophically. If a rule exists because something went wrong, say what
went wrong.

Do not restate §4 here. Extend it.

---

## 7. Never do this

📋 **To be written by this repo's operator.** The repo-specific footguns —
the ones that cost someone a session, not the ones generally true of
software.

**This section holds what is permanently true; `STATUS.md` holds what is
currently broken.** A gotcha that will be fixed is status. A gotcha that is
a standing property of the tool is a discipline and belongs here.

---

## 8. Working with the operator

📋 **To be written by this repo's operator.** Standing preferences,
recurring asks, the things worth flagging without being asked. Optional —
delete this section if the repo has none.

---

<!-- >>> kestrel: base/agents#extending @2026-08-21.4 -->

## 9. Extending this file — the rules

**Adding to this file is normal and needs no permission.** The engine seeds
the shape and owns §3, §4 and this section; everything else is yours to
write at any length. Four rules, so that every repo does not invent its own
convention:

1. **Add sections; do not rewrite the seeded ones' purpose.** The numbered
   sections are the questions every repo has to answer. Answer them in your
   own words. Renumbering or repurposing them makes the fleet's docs stop
   being comparable, which is the one thing a shared skeleton buys.
2. **Do not edit inside an engine region — and everything outside one is
   genuinely yours.** The `>>> kestrel:` fences mark content the engine
   maintains for the whole fleet; it is hashed per region, so an edit
   inside reports as a conflict while your own sections are never compared
   at all. If one of those fleet-wide rules is wrong, it is wrong
   everywhere — route it, do not patch it locally.
3. **Say what a thing IS before you say how it is doing.** A name, an
   identifier, a status marker, a filename — each is a pointer. A pointer
   with no unpacking beside it has told the reader nothing. This applies to
   what you write here and to what you report from here.
4. **Do not restate `OPERATING.md` or §4.** If a rule is fleet-wide, it is
   already stated once. A local copy drifts and then quietly wins.

**When something here should NOT be local:** if a second repo would want it
*identically*, it belongs in the engine's library so it can be rendered for
everyone. The test is not "is this useful elsewhere" — most things are — it
is **"would another repo want this unchanged."** Route it per
`OPERATING.md`'s jurisdiction section.

<!-- <<< kestrel: base/agents#extending -->

---

📋 **Everything below this line is yours.** Add whatever this repo needs
that the sections above did not anticipate — a data model, a CLI reference,
a cookbook, a runbook, an architecture note.

<!-- kit: composed from attention/AGENTS.md.part.tmpl -->

<!-- kit: attention/AGENTS.part@2026-08-21.4 — canonical: kestrel/library/agentdocs/attention/AGENTS.md.part.tmpl — provenance only. This is a PART: it appends to the base AGENTS.md rather than replacing it (kit.py PART_SUFFIX), so a reader gets the shared layer AND this kind's disciplines in one file. -->

---

## The `attention` kind — its directive and disciplines

*Appended by the kestrel kit for this repo's declared kind. The sections above are the fleet-wide base; these are what this kind adds. Neither is this repo's own — write yours below both.*

## Prime directive

**Buffer and extract; never own.** The external sources are the source of
truth. The product is the operator's awareness and understanding across
this instance's declared lenses (ai · global-capital · mental-health · world-news) — surfaced in daily/weekly
digests, steered through `attention/`.

## Disciplines

1. **No canonicalization, no datastore.** Never build ingest/canonize/upsert
   machinery here. `buffer/` is a disposable cache — if deleting it would
   lose anything, something is misdesigned.
2. **Provenance with every artifact.** An artifact without a re-fetch
   manifest is incomplete. Store *how to get it again*, never the pile.
3. **Zero bizdev coupling.** (Ben, 2026-07-20; scope pinned in
   BOOTSTRAP.md.) After the one-time seed, nothing here imports, calls,
   reads from, writes to, or waits on bizdev. Shared workstation infra
   (`authctl`/`gorch`) and one-time seed reads of other knowledge are
   allowed — they're platform, not bizdev. Evidence-grade capture, when an
   artifact needs it, lives in that artifact's bundle.
4. **Perishability rule.** Fetch-on-demand by default; `diffable` sources
   keep one prior snapshot; genuinely perishable capture belongs outside
   this repo.
5. **The attention map is Ben's.** `attention/` edits follow Ben's steering
   ("track X", "drop Z") or the coverage critic's logged additions — record
   *why* on every change.
6. **Inclusive surfacing, selective promotion.** Don't silently drop
   in-scope signal at collection time; judgment lives in curation, and the
   coverage critic audits the misses.
7. **Threads are the unit of reporting; entities sit above them** (Ben,
   2026-07-22). A *thread* is a narrative (`threads.yaml` + its timeline
   artifact `artifacts/threads/<slug>.md`); an *entity* is a durable
   subject — a person/org/topic, always a watchlist entry (slug rules in
   the watchlist header; the entity→threads index is derived at render
   time, never maintained as a file). Items tag both (`<!-- k: -->`
   annotations in the digests — the durable tagged item record); an item
   may belong to several threads. `attention/upcoming.yaml` is the dated
   expectations ledger (checked every /daily; passed-silent is the loud
   outcome). **Meta-threads** (Ben, 2026-07-23): a `kind: meta` thread
   groups sibling threads that point up at it via `parent:` — one level
   of nesting, pointer lives on the child (never a `children:` list on
   the parent, same one-source-of-truth reasoning as items→threads). Full
   field docs in `threads.yaml`'s header.
8. **Derived render surfaces are views, not artifacts.**
   `artifacts/read/index.html` is regenerated byte-equivalently by
   `kestrel render-read` from attention/ + digests + timelines — it needs
   no provenance sidecar, and deleting it loses nothing.
9. **Public publish is default-on, field-allowlisted, machine-checked — not
   hand-gated** (Ben, 2026-07-22: "no private information on here... I
   don't want to hand gate the feed. This is MY feed."). **The site**
   (`/workspace/theprojection-site`) is a separate public repo this instance feeds via
   `kestrel publish`
   — never the reverse, and no other path writes there. Every thread
   publishes unless individually held back with `public: false` in
   `attention/threads.yaml` — an escape hatch, not a gate. What still holds
   the line: only a hardcoded field allowlist is exported (never `notes`,
   never raw internals), and every export is secret-scanned before it's
   staged as a mechanical backstop. A run with zero publishable threads is a
   no-op — it must never wipe the live site back to empty.
10. **The surfaces rank by salience, and the flash rail always lands**
    (Ben, 2026-07-29). Thread rank is `weight × (V + I) + M` — volume,
    **imminence** (a dated expectation coming due is a reason to look
    *before* anything has happened), and **magnitude** (`sev=major|flash`
    on an item annotation). Every page opens in a fixed order: **flash rail
    → executive summary → today's calendar → ranked content.** The
    **flash rail** (`attention/flash.yaml`) carries general-news events
    that must land regardless of lens — Ben: *"9/11? front-page."*
    **`critical` only** reaches the rail, **normally at most one active**,
    and it **publishes to the site on every page** (Ben: *"this is MY
    news feed FIRST. If its big world news it affects finance so its
    cohesive"*). A flash carries the same primary-source discipline as
    everything else — a wrong flash is worse than a late one.
    **A flash is a NEW EVENT, never a running state** (Ben, 2026-08-01:
    *"lapse flash, flash only new things, escalate means need flash"*).
    It describes the discrete event that triggered it and is **never
    edited to carry a conflict's evolving state forward**; when its
    trigger recedes it **lapses on its own `expires` date** rather than
    being extended. **An escalation is itself a new event and earns its
    own new flash** — a materially bigger strike, a new theatre, a new
    combatant, an ordered offensive. This **reverses** the 2026-07-30
    update-in-place precedent (where the Iran flash was widened via an
    `updated:` field). Accepted consequence: a fast-escalating conflict
    can briefly put an old entry and its successor on the rail at once;
    that overlap self-clears and is not the "bar has drifted" failure the
    at-most-one rule describes.
    **A flash lives 24 hours — "flash means today"** (Ben, 2026-08-01:
    *"flash messages should expire in 24h typically. flash means today."*).
    **ENFORCED IN CODE since 2026-08-04**, not a convention the curator is
    trusted to follow (Ben: *"fix the thing where flash messages stay for
    longer than a day. 24h and gone."*). `render_read.flash_last_day()`
    computes the cap: **a flash renders on its filing day and no longer.**
    `filed` defaults to `date`; **`expires` can only SHORTEN a flash's life,
    never extend it**, and an entry with no parsable filing day does not
    render at all. There is no "exception with a stated reason" any more —
    a longer `expires` is silently ignored rather than honoured. If it is
    still on the rail after a day it has stopped being a flash and become a
    headline. Corollary, still live: an event that surfaces **late** gets
    24h **from filing**, which is why `filed` exists — set it explicitly on
    a late catch and add a note saying so; being missed does not buy a fresh
    lifespan, but it does not cost one either.
    **Why this became code** (2026-08-04): the rule existed in this file
    from 2026-08-01 and was violated immediately and repeatedly, because the
    loader honoured whatever `expires` was hand-written —
    `iran-strikes-cancelled-deal-claimed` ran **3 days**,
    `ceuta-mass-border-crossing` ran **4**. A separate latent bug meant a
    flash with no `expires` at all never expired. Same lesson as discipline
    12's summary shape: *asking* for a constraint does not hold, so the
    store enforces it. This supersedes the 3-5 day `expires` values used
    through 2026-07-31.
    Executive
    summaries are written in the digests' **neutral register**; the
    per-lens "Today's throughline" *is* the lens summary, and
    `<date>-front.md` is the cross-lens one. Full spec + what is still
    unbuilt: **ROADMAP §Salience**.
11. **Every page carries an executive readout** (Ben, 2026-07-29).
    `BREAKING` (same-day) · `NEWS` (7 days) · `SUMMARY` (the curated built
    understanding — "that is the point"). **BREAKING and NEWS are derived
    mechanically** by `kestrel readouts` from the dated item record and no
    model may touch them; **only SUMMARY is model-written**, by
    sonnet-class agents, and only when a fingerprint over that scope's
    inputs changes. Bullets always link somewhere. `front` prefers the
    hand-curated `<date>-front.md` over the model. Run
    `--scan` → `--pack-stale` → agents → `--apply`. **The front + 3 lens
    scopes (the fuller "briefing" — `gist`/`lead`/`sections`/`watch`) are
    now refreshed every `/daily` run (step 6a)**, not by hand — a rename
    that orphans a stored scope key (e.g. `lens:money` after the Global
    Capital rename, 2026-07-30) is caught by `--export`, which drops any
    scope no longer in `all_scopes()`. Full spec + the stale-figure
    failure that shaped it: **ROADMAP §Executive readouts**.
12. **The summary is a SHAPE, not a request** (Ben, 2026-07-29: *"I
    wanted bullets and emojis and delight. It's still just a paragraph."*).
    Asking a model for structure does not hold — v1 asked, and all 160
    summaries came back as single paragraphs. So the store holds **slots a
    template lays out**, and `--apply` **rejects** anything that misses
    them: a thread/entity/node scope gets `gist` · `bullets`
    [{emoji,text,url}] · `watch`; **front and beat scopes get a fuller
    morning briefing** — `gist` · `lead` · `sections` · `watch`. In a
    briefing, **`lead` is ranked by salience with NO lens quota** and the
    front's **`sections` are exactly this instance's lenses**, so nothing goes
    dark while the ranking stays honest; a fact appearing in both is
    deliberate — the lead is the ranking, the sections are the coverage.
    **The lenses are pages** (`/news/<lens>/`, nested under the
    `/news/` dashboard since the 2026-08-03 restructure), not just the
    dashboard's filter chips. Emoji come from a fixed typed set and never
    carry a fact alone. Two rules learned building it: a validator that
    makes good prose worse is the bug (a sentence may end on a quotation),
    and **a briefing cannot cover what it was never shown** — packs get
    `PACK_LIMITS`, far above the display caps, because the front has 100+
    items in the window and an 8-item pack silently hid the day's leads.

13. **World News is mechanical and restrained — the sibling signal to the
    flash rail, not a duplicate of it** (Ben, 2026-07-30). Flash is
    Ben's own editorial judgment ("would this lead a front page");
    `attention/world-news.yaml` is a computed fact — N distinct outlets
    covering a story, generated by `kestrel build-world-news` (merging
    `google_news_rss` clustering with a deduped GDELT feed), never a
    model or a curator. Kept deliberately small ("on the radar, not
    drowning out my real targets") and matched against `threads.yaml` on
    two tiers (country-pair proximity for multi-country headlines,
    keyword overlap against a thread's title/terms/watch — never its
    full timeline — otherwise). `candidate`-status items compete for the
    same 1–3 daily thread-candidate slots as curator-noticed ones,
    tagged `(world-news, N outlets)`. No new persisted state: a promoted
    candidate becomes a real thread the normal way, and the next build
    auto-matches it and drops it from the pool on its own. Full spec:
    ROADMAP §World News. **A promoted candidate becomes a `lens:
    world-news` thread** (2026-07-30) — a fourth lens, but deliberately
    narrow: no watchlist entity sweep, no coverage-critic benchmark set,
    threads arrive only via this mechanism. It carries its own thin
    daily digest (`<date>-world-news.md`) alongside the three primary
    lenses'. A thread is world-news when it's the conflict/geopolitical
    narrative itself; its downstream capital-market read stays
    global-capital's job, cross-referenced (`iran-conflict-widening` vs.
    `red-sea-oil-shock` is the reference split — same origin event, one
    thread per lens, deliberately, not one thread wearing two hats).
    **The coverage bar, stated directly** (Ben, 2026-07-31, promoting
    `russia-ukraine-war` after it sat as an unanswered candidate for a
    day: "All active military conflicts that are not hyper-local get
    coverage."). Read together with "kept deliberately small" above:
    small applies to *detection volume* (the mechanical sweep itself
    stays restrained, no term-list expansion), not to which real wars
    clear the bar for promotion once surfaced — a genuine active
    military conflict above hyper-local scale is a yes, not a judgment
    call re-litigated per war.

14. **Global Capital interprets; it doesn't just aggregate** (Ben,
    2026-07-30 — full rename from `money`: "'finance' is boring 'Global
    Capital' is interesting to me"). Every relevant item can carry a
    generated, confidence-tagged `interpretation` — `{mechanism,
    confidence, scenarios[{direction, why, precedent?}], context_note}` —
    alongside its sourced bullet, never replacing it. **The guardrail is
    enforced, not decorative**: `kestrel readouts`'s
    `validate_interpretation()` requires a real `mechanism` unconditionally,
    and above `confidence: speculative`, at least one scenario needs a
    genuine `precedent` or the whole interpretation is rejected — the same
    "shape enforced, not merely requested" discipline as every other
    summary shape here. Read against **`attention/capital-context.yaml`**,
    a macro-wide sibling to `actor-doing.yaml` — daily curation reads it,
    never writes it; it refreshes on its own weekly, `/week`-adjacent
    cadence (step 4b) from 5 real collectors (Treasury TIC, BIS, IMF,
    EPFR, fund-flow reports). `/steer capital-context ...` only ever
    touches the snapshot's `framing` (what the next refresh emphasizes),
    never a reading's value directly — a wrong reading is a collector bug.
    Generated reasoning is visually unmistakable from sourced fact (its
    own accent, `#5A4B8C`) and has a full receipt one click away at
    `/interpretation/<slug>/`. Full spec: DESIGN.md Part 2.

## The operating rhythm — commands + cadence (set 2026-07-20)

The loop runs on nine in-repo slash commands (`.claude/skills/`), rendered
against fixed templates (`templates/`):

| command | cadence | what |
| --- | --- | --- |
| `/start` | session open, read-only | continuation briefing (docs + memory + git) fused with live pipeline state: digest status, expectations due, flash rail, freshness, **push safety on both repos**, doc drift → names the next move |
| `/daily` | **any time, any frequency** — catch up to now (Ben 2026-07-28: no clock gate; a day finalizes only once its coverage is checkable, ~5h past its close) | reconstruct missed days + finalize finalizable days (+ coverage critic) → upcoming check → collect → curate + tag → timelines → map deltas + candidates → render + republish the page → take steering |
| `/week` | Saturday (or when convenient; week is fixed Mon–Sun) | radar-question synthesis · expectations scorecard · near-miss audit · **decay review** (Ben answers in the read) |
| `/steer <words>` | any time | one utterance → small provenance-tagged map edits, logged |
| `/crawl <thread>` | on demand | backward crawl → finding + provenance bundle + timeline backstory backfill |
| `/map` | any time, read-only | status card: lenses, thread freshness, radar, pipeline state, gates, board |
| `/classify <actor>` | on demand | propose an actor's node kind (person/house/corp/state/agency/group) + level + posture/condition + four-axis estimate (commanded_capital/thrust/gravity/optionality) → apply on confirm; `/classify postures` sweeps provisional postures (the logic `/week` runs) |
| `/publish [--push]` | on demand, separate from `/daily` (not auto-chained) | push public-flagged threads to the public site; stages only by default, `--push` commits/pushes/deploys live — no confirmation needed on this pipeline (Ben, 2026-07-23), plus a quick fact-check that the site's own `about.md`/`README.md` claims still match this repo's actual publish behavior |
| `/health` | any time, read-only | four signals in one command: kit drift against the installed stamp, whether `STATUS.md` still describes reality, git state (uncommitted/unpushed), and `INBOX/` depth. Answers "is this repo in the state its docs claim" — useful opening a session, closing one, or before trusting a doc |
| `/wrap` | any time — a **CHECKPOINT, not a closer** (runs fine several times a day) | persist the session: sanity gate → `STATUS.md` refresh (anti-rot, rewrite-never-patch) → `log.md` append → commit incl. provenance receipts → site-tree triage → push + `git log @{u}..` verification on both zone repos (the engine checked read-only, **flag-never-push**) → wrap card |

Re-running `/daily` later the same day is safe (building digests rebuild in
place). **Collection is collectors-first since 2026-07-28** (18 registered
sources via `kestrel collect` as of 2026-08-03 — grown from the original
12; agents only fill gaps + tier-2 depth — the skill's dispatch plan);
curation/critic remain agentic until P3 lands. **Sweep runtime — the
figures here were stale twice and are now reconciled (2026-08-13).** The
short version: **a full sweep runs in roughly a third of the time the old
note claimed, because the engine changed underneath it.**

`kestrel collect` **stopped running collectors serially on 2026-08-05** —
it now fans them out across a thread pool, so wall clock collapses toward
the single slowest collector's own lane instead of summing every lane.
That is the cause of the drop, and it is worth stating plainly because the
instance-side sessions that re-measured it could see the speedup but not
its reason:

- **~59 min** — measured 2026-08-04, **pre-parallelisation**, 17/18 sources,
  exit 0. Correct for its day; obsolete now.
- **~17 min** — measured 08-06 (18/18, timed off the run's own provenance
  manifests) and repeated 08-07, both **post-parallelisation**, at
  comparable or larger volumes.

⚠️ The 08-04 per-collector split (**semantic_scholar ~23 min / 39%,
google_news_rss ~14 min / 24%, gdelt ~11½ min / 20%**) is a **serial-era**
measurement and almost certainly no longer describes where time goes —
treat it as history, not a budget. It does **not** hang and is **not**
killed by a timeout; an earlier claim that it was ("killed on three
consecutive runs, 15/18 sources") was an artefact of reading alphabetical
progress mid-run while GDELT failed separately in milliseconds.

⚠️ **Do not parallelise *inside* `semantic_scholar`** regardless of the
above — `base.pace()` is a plain `time.sleep()`, not a shared limiter, so
concurrent workers in that one lane would 429-storm. The fan-out is across
collectors, never within one.

⚠️ **`KESTREL_CONTACT_EMAIL` is NOT persistently set**, correcting this
file's own earlier "that variable is now set" — which was true only of the
session that wrote it. A later check found it absent from the instance's
`.env`, `~/.bashrc`/`.profile`/`.zshrc`, and `/etc/environment`. Set it
explicitly at the start of a run (matching the contact documented in the
instance's own source docs) or `federal_register`/`gdelt` run unkeyed.
Measurements and the fix options are in kestrel's INBOX
(`2026-08-04-…-collect-py-timings-
remeasured.md`, amending the 07-31 item); the engine repo owns the fix.

## The steering loop (the growth mechanics — draft, Ben 2026-07-20)

The attention map grows and decays as a side effect of Ben *reading*, never
by batch rewrites. Big agent passes (re-triages, syntheses) only ever
**propose into the surface Ben reads** — he steers, the map moves.

1. **Daily surface** → Ben reads the digest.
2. **In-line steering** — "track X" / "drop Y" / "go deeper on Z" via Doc
   comments, chat, or the daily read. Low friction; words, not tickets.
3. **Small same-day edits** — each reaction becomes one logged map edit or a
   backward crawl. Incremental, never wholesale.
4. **Critic auto-growth** — benchmark misses add entities/threads without Ben.
5. **Weekly decay review** — threads with aging `last_seen` surface as prune
   candidates in the weekly read; Ben confirms kills in the same pass.

Rules: every map edit carries provenance (`ben-steer` · `critic-add` ·
`synthesis-spawn` · `decay-review`); the digest renders its own **map
deltas** (added/dropped/why); each daily may offer 1–3 **thread candidates**
("want me to track this?") that Ben promotes with a word. Scoped exception
(2026-07-22): `attention/upcoming.yaml` additionally accepts `curate-add`
and `crawl` tags — expectations are dated claims, not attention-map
structure, so noticing one during curation/crawling may log it directly;
the four core tags stay exclusive for watchlist/threads/radar. Timeline
entries carry `⟨daily|crawl|seed|steer YYYY-MM-DD⟩` markers pointing into
artifacts that already have manifests.

**The board** (`attention/board.yaml`, 2026-07-24) is a power-structure
layer *over* the map — the major actors (Houses = people, orgs = the
realms they hold) in neutral structural kinds, projected into costume on
the site (its `data/labels.yaml`) and swappable live. **The
model changed 2026-07-25** (Ben): the feudal rank *ladder*
(empire/kingdom/vassal/march) was the wrong axis and is gone. **It became a
node graph on 2026-07-26:** every actor is a **node** with an orthogonal
`kind` (person · house · corp · state · agency · group) and `level`
(L1 = nothing over it · L2+ = has a `parent`); **pockets** (`tier: G1`) and
**sectors** (`tier: G2`) are **group nodes** joined by `member_of` edges, not
tags. Actors are differentiated NOT by a rung but by
**four measured axes** (`board.yaml` `axes:` — model completed 2026-07-27,
full schema in `DESIGN.md` §2, public recipes on the site's `/metric/`
pages): **commanded_capital** ($ the actor directs — renamed from
`capitalization`, done), **thrust** ($/yr committed to NEW positions;
buybacks+dividends tracked separately as a signed negative channel),
**gravity** ($/yr third-party economy that breaks if it stops —
structural/attributable method, substitutability × forward-linkage, never
gross ecosystem headlines; supersedes the earlier stored-gross/deflation-
deferred position), and **optionality** (encumbrance band
`free/mixed/constrained/locked` — measured, NEVER derived as thrust÷weight).
Numeric values in `axes_num` ($B; a 21-actor pilot 2026-07-27, rolled out
to **53 of 92 orgs** 2026-07-28) drive
the `/map/` plate — the POWER view (re-encoded 2026-07-27, Ben): four
optionality columns (free→locked) × log-weight height, **size = gravity**,
**fill = burn (thrust÷weight) as heat**, ring = sector (neon). The earlier thrust×gravity
diagonal view is queued to live on the circular-financing thread pages. **Sovereignty is derived + graded**, not a
primitive you score. The old vassal/`liege` idea becomes a **dependency**
relationship — stubbed (`liege`→`depends_on` rename pending). It's part of
the map: edits accept a `classify` provenance tag alongside `ben-steer`,
carry a coverage-log line, and republish through
`kestrel publish` (`data/board.json` + `data/claims.json` → the
`/map/` node/pocket/sector pages + a `/claim/<node>--<dimension>/` page per
metric). **Every metric is a claim with a cited source** — the value is the
summary, the claim page is the receipt (*a metric with no
visible source is a bug*); source data lives in per-node bundles
(`artifacts/bundles/<slug>-node/provenance.yaml`), and the full node + claim
schema is **[`DESIGN.md`](DESIGN.md)**.
`/classify` proposes a node kind + level + posture + axis estimate; `/steer`
board verbs apply decided ones. A change of kind or level is still
an **event — loud, logged, a thread offered; never silent** (spec §8.5).
Threads carry a neutral `genre` (board vocabulary) that drives the
per-actor rollups. **Three layers per actor** (Ben, 2026-07-24): STRUCTURE
(`board.yaml` — kind/House/holdings + the axes), ACTIVITY (its threads),
and a standing SYNTHESIS (`attention/actor-doing.yaml` — the "what are they
doing now" roll-up shown atop each `/map/<slug>/` page). The synthesis is
refreshed on `/daily` (for actors that moved) and `/week` (full pass);
it's a roll-up of threads + posture, not fresh research.

## ⚠️ This file is a kit artifact — see `OPERATING.md`

`AGENTS.md`, `CLAUDE.md` and the installed skills are **rendered from the
engine's library** and tracked by hash. Editing one here is legitimate;
back-porting it yourself is not.

**All of it — the ownership map, why `dirty` is the correct outcome, the
jurisdiction rule, and how to file an engine brief — lives in
`OPERATING.md` beside this file**, identical in every repo the engine
tends. It is not restated here, because this section used to be the
place three separate instructions to go edit the engine directly
accumulated (2026-08-01, corrected 2026-08-04); one shared statement is
harder to drift than three copies.

⚠️ The one thing worth repeating, because it was the specific failure:
**never run an "adopt" from here** to push a local fix into the canonical
template. That writes into the engine. File the brief instead.

## Session close

`OPERATING.md` §6 owns the general shape (log → commit with receipts →
push → verify the push). Two things are specific to this kind:

1. **Your `log.md` entry names what changed in `attention/`** — the map
   is the product, so a session that moved it and did not say how is
   unfinished.
2. **The run's provenance manifests are part of the commit.** They are
   receipts, not scratch, and they are easy to leave untracked precisely
   because the publisher writes them *after* the work they describe is
   already committed.

**Why step 2 is written down** (Ben, 2026-07-29, pre-split — the reasoning
holds, only the repo name changed): `/publish --push` pushes the **site
repo** (`/workspace/theprojection-site`), not this repo — it fires the site's deploy
hook and nothing else. Nothing in `/daily`, `/publish` or any other command
ever pushes this repo on its own, so unpushed work accumulates *silently
across sessions* and looks fine locally. Found 2026-07-29 (pre-split, in
what was then kestrel's own working tree) with **17 commits unpushed** —
six from that session and **ten inherited from the previous evening's**,
which had also closed without pushing. A clean `git status` is not
evidence the work is safe; check `git log @{u}..` — on this repo AND on
`/workspace/kestrel` and `/workspace/theprojection-site`, since none of
the three ever push each other — before calling a session done.

## Your publish surface

**Your publish adapter is yours, not the engine's.** (**Operational** — `publish/adapter.py` exists in this repo.)

The engine's publish core is generic orchestration — the run loop, the
secret scan, the git push, the guarantees. **What pages exist, what data
ships, and any step you add to the publish flow live in this repo's own
adapter file.** This is the specific thing a session once got wrong,
telling the operator a feature needed an engine change when the whole
change was a method here.

**Your site, if you have one, is YOURS — including its docs.** If this
instance declares a site (`/workspace/theprojection-site`), that repo is your publish surface, and you are its only
content writer. Two things follow, pulling opposite ways:

- ✅ **You own it.** The engine manages nothing there — no rendered docs,
  no hashes, no drift reporting. Its `AGENTS.md`, `README.md`, layouts,
  CSS and deploy config belong to whoever works in it, usually you.
- ⛔ **Its generated content is not hand-editable, by you or anyone.**
  Whatever your adapter writes is overwritten wholesale on the next
  publish. A fix belongs **here** — in the records, or in the adapter that
  renders them — never in the site.

**Why the engine stopped managing sites** (2026-08-14): a site has no
agent of its own. Pushing a doc into one from the engine produced a single
file that either duplicated what the site already said or froze and went
stale — one carried a wrong path for ten days while the site's own README
stayed accurate. This contract is the replacement, and it lives on this
side because you are the one who writes there.
