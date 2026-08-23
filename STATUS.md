# STATUS — theprojection-corpus

*As of 2026-08-23*

<!-- The line above is deliberately alone on its own line, in exactly one
     spelling, per the base STATUS schema kestrel introduced 2026-08-18
     (INBOX/2026-08-18-kestrel-kit-...): it is the only automated
     freshness check this file has, and it cannot fire when the date is
     embedded mid-sentence. -->

*Hand-maintained. Top note covers the 08-23 gap catch-up, on top of
08-21's two `/daily` passes, then the 08-20 note (which finalized 08-19),
then 08-19, then 08-18 and older.*

> **2026-08-23 (10:00 ET) — a two-day gap closed in one pass: 08-21
> finalized, 08-22 reconstructed, 08-23 opened.** No `/daily` ran on
> 08-22, so this run swept 2026-08-21 15:00 ET → 08-23 10:00 ET at once
> and split findings back to the digest-day each event belongs to. Counts
> after the run: **99 threads** (85 open · 12 developing · 1 resolved · 1
> retired — unchanged), **66 expectations** (46 pending · 14 hit · 6
> passed-silent — five logged this run), **211 watchlist entries**
> (unchanged; three entity adds proposed and held for Ben), **45 actor
> roll-ups** of which 3 now carry an 08-23 `asof`. **No flash** — the
> 08-21 Kryvyi Rih flash expired on its filing day and a rising casualty
> toll is not a new event. **14 digests written or finalized · 16 thread
> timeline blocks · 16 `last_seen` updates.** Dispatch: one collector
> sweep + seven agentic sweeps + three coverage critics; all returned,
> none stalled.
>
> **Coverage critic verdict on 08-21: no genuine misses across three
> lenses.** What it produced instead is the run's real editorial finding —
> **a three-source convergence on data-center political opposition** on
> 08-21 (Axios Pro Rata's lead essay, The AI Daily Brief's whole episode,
> and Anthropic's own S-1 risk factors). A bare candidate label since
> 08-20 is now a thread-shaped hole with a securities filing in it. It is
> put to Ben as a decision alongside the **Treasury long-end candidate**,
> whose third offer now carries the critic's confirmation that FT Unhedged
> led with that story **three consecutive editions**.
>
> ⛔ **Six infrastructure failures, five of them previously undocumented.**
> **(1)** `cloud-researcher collect` resolves **both** its corpus and its
> `.env` against the seat rather than the corpus — `collect.py:55` never
> migrated to `paths.py`'s `corpus_root()` while `collectors/base.py:90`
> did, so the two halves disagree; and `collect.py:34` loads `.env` from
> the seat, which has none, so **every keyed collector has run keyless
> since the package split.** Working invocation needs both signals set.
> **(2)** ⛔ **`build-world-news` is blocked on expired gcloud
> credentials** — and this corrected a claim this run had already written
> into five digests. The collector's `gdelt` leg completed for the first
> time in four runs, which I initially read as the world-news pool
> unblocking. It is not: `build_world_news.py` queries GDELT's **BigQuery**
> dataset via `bq`, which fails `Reauthentication failed`. **Only Ben can
> fix this** (`gcloud auth login`); `attention/world-news.yaml` is stale
> from 08-18 on two unrelated stacked causes. **(3)** The `rss` collector
> stamps **fetch time** as `ts` when a feed carries no `<pubDate>`,
> indistinguishably from a real date — it stamped 38 *Internet
> Interventions* articles with today's date when 36 are forthcoming
> September/December issue contents and one is genuinely new. **(4)**
> Benchmark health: **The Rundown AI** unreachable two days running,
> **Bloomberg Technology** now blocked through the `r.jina.ai` proxy too
> (a new escalation past the fix class that resolved every other blocked
> benchmark), **Money Stuff** dark since 08-13, **Behavioral Health
> Business** silent since 08-20, **FT Unhedged** now needing the proxy
> that `sources/benchmarks.yaml` says it does not. **(5)** `lda` 403s on
> all 160 terms two runs running and `fund_flow_reports` hits bot
> challenges — both **unchecked, not clean**. **(6)** ⚠️ The read payload
> is over the 600 KB soft cap for a **fifth** consecutive run and still
> growing: 1241 → 1254 → 1308 → 1331 → **1384 KB**; the degradation rule
> remains unimplemented.
>
> **Two ops briefs filed to `kestrel-ops/INBOX/`** (committed there, not
> pushed, per their contract): the collect corpus/`.env` resolution
> incident, and the `rss` fetch-time-as-publication-date incident.
>
> **Held rather than guessed.** This session exhausted its 200-call
> WebSearch budget on the seven sweeps, so three real leads are carried
> **unverified rather than logged**: Nvidia's reported ~$6-7bn Poolside
> licensing deal (date unpinnable between 08-21 and 08-22), the Capital &
> Main investigation into Kaiser's algorithmic triage (08-18, incl. a
> California bill reported as AB 2575), and Senator Warner's 08-18 letter
> to Meta on AI-generated CSAM ads. First jobs next run.

> **2026-08-21 (15:00 ET) — 08-20 finalized earlier today; 08-21 open and
> extended twice; first flash since 08-11.** Counts computed at the 15:00
> ET pass: **99 threads** (85 open · 12 developing · 1 resolved · 1
> retired — unchanged since 08-19), **61 expectations** (41 pending · 14
> hit · 6 passed-silent), **211 watchlist entries** (unchanged), **45
> actor roll-ups** of which 8 now carry an 08-21 `asof`. **1 flash live**
> — `kryvyi-rih-mall-double-tap`, which renders on its filing day only.
> **2 publishes today.** Both zone repos confirmed pushed via
> `git log @{u}..` printing nothing; `kestrel` untouched.
>
> ⚠️ **The 10:00 ET pass did not close itself out.** It exited 0 having
> said it would commit, leaving 46 files dirty; kestrel's fleet sweep then
> swept them into commit `76a091a` under an unrelated STATUS.md message
> (see `INBOX/2026-08-21-kestrel-your-daily-output-is-already-committed.md`
> — nothing lost, wrong label, not force-corrected). It also left 18 files
> staged-but-uncommitted in `theprojection-site`, and wrote no `log.md`
> entry. The 15:00 ET pass committed the corpus **before** publish and
> collect rather than after, and its publish absorbed the orphaned site
> files. Both repos are clean now.
>
> **Three standing failures, all recorded in `log.md` and none fixed
> here.** ⛔ **GDELT has not completed on three consecutive runs** — this
> run's leg ran 22 minutes, burned 2m43s of CPU and held 18 sockets while
> producing nothing, so it is blocked on network rather than crashed.
> `attention/world-news.yaml` is consequently **stale from 08-18** and no
> mechanically-scored world-news candidate can be offered at all. ⛔
> **`/daily` step 1's documented collector command is wrong** —
> `cloud-researcher collect --corpus .`; `--corpus` is not a flag, and the
> corpus is read from `KESTREL_INSTANCE`, so the documented form resolves
> against the engine repo. Engine-owned template, needs routing. ⚠️ **The
> read payload has been over its 600 KB soft cap for four runs and is
> growing** (1241 → 1254 → 1308 → 1331 KB); the degradation rule the
> warning names is not implemented, so the warning is advisory only.
>
> **Also this pass:** `/health` was found undocumented in `README.md` and
> `AGENTS.md` despite being installed by the 2026-08-21.3 kit sweep —
> added to both by the `/publish` staleness check that caught it.


> **2026-08-20 (mid-day) — 08-19 finalized (3-lens coverage critic run),
> 08-20 opened, two publishes.** Counts computed today: **99 threads**
> (85 open · 12 developing · 1 resolved · 1 retired — unchanged from
> 08-19), **57 expectations** (39 pending · 13 hit · 5 passed-silent —
> two flips today: `iran-oman-hormuz-deal-signing` → passed-silent,
> `ping-an-group-h1-2026-interim-results` → hit), **211 watchlist
> entries** (unchanged), all **45 actor roll-ups** (none moved enough to
> refresh this pass). **2 publishes today** (thread/entity content +
> a fresh briefings apply/export covering front + all 3 lenses). All
> three repos confirmed pushed via `git log @{u}..` printing nothing on
> this repo and `theprojection-site`; `kestrel` untouched this session.
>
> **`/daily`: 08-19 finalized, 08-20 opened.** 08-19 was old enough
> (>24h past its 05:00 ET close — extended past the usual 5h bar since
> the run started mid-morning 08-20) to finalize: ran the coverage
> critic on the three critic-bearing lenses (frontier-ai, global-capital,
> mental-health), folded late/critic-caught items into 08-19's
> timelines and digests (Oregon's psilocybin-study outcomes, the
> Medicaid psychotherapy-spend figure), and flipped two due
> expectations. 08-20 opened `building` via a full collector run plus a
> 5-agent tiered dispatch (4 hot-cluster deep checks covering 24
> weight-3 threads + 2 due expectations, 1 cold-rotation sweep of 7
> quiet threads) through ~10:30 ET. Today's real news: Russia hit Kyiv
> with a large missile/drone barrage overnight (12-13+ killed) and a
> Russian drone separately crashed in Romanian (NATO) airspace — the
> second such incursion in three weeks, both `sev=major` on
> `russia-ukraine-war`. Coverage critic on the 08-19 finalize found
> real misses in mental-health (two Behavioral Health Business items)
> and global-capital (Axios Pro Rata's private-credit/insurer story,
> proposed as a watchlist/thread add, not added directly); the
> frontier-ai "miss" (an OpenAI newsroom post) reconciled as already
> logged a day earlier, not a genuine gap.
>
> **2026-08-19 (mid-day) — 08-18 finalized, 08-19 opened, one publish,
> kestrel#25 filed with full repro.** Counts computed today: **99
> threads** (85 open · 12 developing · 1 resolved · 1 retired —
> unchanged from 08-18), **57 expectations** (41 pending · 12 hit · 4
> passed-silent — unchanged from 08-18), **211 watchlist entries** (was
> 204 at 08-18, +6 merged in from finalize), all **45 actor roll-ups**
> (one refreshed, not a count change), **1 publish today**
> (`publish-2026-08-19T143504Z.yaml`, 122 payload items / 67 entities
> across ~100 threads). All three repos confirmed pushed via `git log
> @{u}..` printing nothing on this repo, `theprojection-site`, and
> `kestrel`.
>
> **`/daily`: 08-18 finalized, 08-19 opened.** 08-18 was old enough
> (>5h past its 05:00 ET close) to finalize: ran the coverage critic on
> the three critic-bearing lenses (frontier-ai, global-capital,
> mental-health), folded late/critic-caught items into 08-18's
> timelines, rebuilt affected thread pages, and merged in six watchlist
> entities, one `actor-doing.yaml` refresh, and one `capital-context.yaml`
> addendum from the four lenses' propose-lists. 08-19 opened `building`
> and was extended via collector run + a light agentic-interim sweep
> through ~14:30 ET; all four lenses are still `building` as of this
> note — normal for mid-day, not a gap. Coverage critic on the 08-18
> finalize found one real single-item miss (Bloomberg's Unitree
> Robotics 460% IPO surge, proposed as a watchlist add rather than added
> directly) against otherwise-covered ground.
>
> **kestrel#25 filed with the real repro.** The `md_html()` bold/nested-
> italic regex bug found during the 08-18 site fix (below) was filed
> upstream with `china-stack-independence.md`'s nested-italic case and
> `tsmc-capacity-race.md`'s line-wrap case, the one-character fix, and a
> note that `publish/adapter.py`'s local `_md_html()` copy should retire
> once it lands.
>
> **Open pick-up:** the world-news thread candidate `Lubbock data-center
> moratorium petition` (22 outlets) has now been offered twice (08-18,
> 08-19) without a Ben decision — per the offered-twice rule it will not
> be re-offered automatically; needs an explicit track/drop call.

> **2026-08-18 (wrap) — three `/daily` cycles, `/week` closed, a
> five-bug site rendering fix, three repos pushed.** Counts computed at
> wrap: **99 threads** (85 open · 12 developing · 1 resolved · 1
> retired — unchanged from 08-14), **57 expectations** (41 pending · 12
> hit · 4 passed-silent — was 62/39/18/5 at 08-14; net down from pruning
> stale-resolved entries, not from losing coverage), **204 watchlist
> entries** (was 198), all **45 actor roll-ups refreshed**, **3
> publishes today**. All three repos confirmed pushed via `git log
> @{u}..` printing nothing on this repo, `theprojection-site`, and
> `kestrel` — not inferred from a clean `git status`.
>
> **`/daily`, three cycles across 08-15 through 08-18.** Finalized
> 08-15, reconstructed 08-16 from a full blank (no run over the
> weekend), opened and later extended 08-17 through a 15:00 ET pass that
> caught Anthropic's real **$105B** NVIDIA-OpenAI guarantee cap (the
> morning read three separate outlets as carrying no dollar figure —
> it was one document over, in the 8-K body, not the press-release
> exhibit) plus three cross-sweep aggregation traps and two caught-late
> items. Finalized 08-17 (3 self-corrections), opened and twice extended
> 08-18 (10:45 ET then 15:15 ET, two cold-rotation batches).
>
> **`/week` closed `week_of 08-10`, recovered from an interrupted prior
> session.** The weekly synthesis (all four lens digests, `actor-doing.yaml`
> full pass, `radar.md` decay-review notes, `capital-context.yaml`
> refresh, `upcoming.yaml` pruned of 2 stale-resolved entries) was
> already complete and sitting uncommitted in the tree — recovered,
> verified against its own stated write-scopes, committed and pushed
> separately from the day's `/daily` work. Real findings: OpenAI
> dissolved its Preparedness (catastrophic-risk) team the same week
> Anthropic disclosed a $65B July run-rate; vendor-financing skepticism
> and Hormuz war risk both moved from priced-as-belief to priced-as-fact
> in the same seven days; the Aetna rate-cut ledger entry was corrected
> from an overclaimed "confirmed" to genuinely unresolved.
>
> **Site: a flagged story page widened into a five-bug rendering-pipeline
> fix, verified across all 1,727 published pages.** Ben flagged
> `/story/anthropic-ipo-timing--2026-08-17/`'s summary rendering as raw
> markdown, then asked whether the fix was site-wide. It wasn't at
> first: `build_stories()` never ran markdown through any converter at
> all (fixed); kestrel's own shared `md_html()` has a real regex bug
> that silently fails on bold spans containing a nested italic (found,
> reproduced, duplicated locally with the fix since kestrel is read-only
> from here — filed as kestrel#25); the front-page
> `gist` field and `readouts.json`'s own cleaning loop each had the same
> class of gap, chasing the exact "field-by-name doesn't converge" trap
> that code's own docstring had already named once; a bold span could
> fail to convert if its source `.md` word-wrapped mid-phrase. Verified
> by rebuilding the site locally and grep-sweeping all 1,727 pages after
> each fix. Also shipped: a story page now shows its position in its own
> thread's timeline and its thread's parent/sibling threads — Ben:
> "I'm not seeing a thread map on these pages." Caught and fixed a real
> `O(n²)` build-time regression of its own along the way (12+ min → back
> to the ~2min baseline). Pushed: this repo, the site (Cloudflare build
> triggered), kestrel (by its own resident session, unrelated work).
>
> **Also this session:** pm's STAMP provenance-viewer question answered
> and closed (no provenance record for anything published here right
> now — the nominated candidate is a live rolling thread, the wrong
> shape for a method that binds to prose that stops). Five kestrel
> issues filed on real engine gaps found along the way (kestrel#21-25):
> the attention kind's `AGENTS.md` still frames decay review as a
> retirement queue after the fix went upstream; the `STATUS.md` As-of
> lint can't distinguish "undated" from "dated in the wrong place"; the
> kit stamp is checked against itself so a write-side bug can report
> clean; the ops/dev routing table's own wording caused a real misfile
> this session; and `md_html()`'s own bold regex silently fails on a
> nested italic span (#25 — the bug behind the site fix above).

> **2026-08-14 (wrap) — kit sync, a full `/daily` + `/week`, and a real
> policy fix to how threads get retired.** 5 commits since the 08-13
> wrap. Counts computed at wrap: **99 threads** (85 open · 12 developing
> · 1 resolved · 1 retired — unchanged count, most refreshed content),
> **62 expectations** (39 pending · 18 hit · 5 passed-silent — was 62 /
> 42 / 15 / 5 at the 08-13 wrap; four hits this run, one new entry
> logged, one stale hit pruned), **198 watchlist entries** (was 194 —
> Michael Heinz, Silver Lake, Jane Street, Vantage Data Centers), all
> **45 actor roll-ups refreshed** (a full `/week` pass, not just movers),
> 3 publishes today.
>
> **Kit sync, reviewed before committing, not just accepted.** The
> session opened on an uncommitted sync already in the working tree,
> pulling kestrel's 2026-08-14 restructuring (the package turn's
> `kestrel <verb>` CLI, a `CLAUDE.md`/`OPERATING.md` split, sites
> released from kit management). Read it line-by-line rather than
> rubber-stamping it: caught a real bug fix worth keeping (`/daily`'s
> own session-close step used to tell the agent to push *kestrel* —
> exactly the out-of-zone write the zone rule prohibits — now pushes
> this repo and never kestrel) and a convention change that made this
> session's own memory stale (briefs now route to a new sibling repo,
> `kestrel-ops`, committed there, not dropped uncommitted into kestrel's
> own INBOX) — updated project memory before it could mislead a future
> session.
>
> **`/daily`: finalize 08-13, open/curate 08-14, four lenses in
> parallel.** A full 15-collector sweep, then four sonnet agents — one
> per lens — each finalized 08-13 with its own coverage-critic pass and
> curated 08-14 through the afternoon. Real findings: California's SB
> 903 cleared Assembly Appropriations 13-0 and now sits on the Assembly's
> 08-17 floor-vote file; Berkshire's Q2 13F showed its Alphabet stake
> nearly doubling (+83% shares/+127% value) with no other AI-adjacent
> equity added; SpaceX closed its $60B Cursor acquisition ~17 days
> early; a Jefferies note quantifying hyperscaler free-cash-flow
> compression landed the same week Michael Burry named Nvidia's $500B
> financing platform directly — the first real skepticism this map's
> AI-financing thread has carried; Ukraine's largest territorial claim
> of the war (745 km²) was correctly held below the flash-rail bar as a
> campaign culmination, not a discrete event. Two real ledger bugs
> caught in the same pass and fixed directly (not decay): `tsmc-capacity-race`
> and `anthropic-ipo-timing` each had real hits whose `last_seen` never
> got bumped at the time.
>
> **`/week`: weekly synthesis, a full actor-doing rewrite, capital-context
> refreshed.** Four weekly digests synthesized against each lens's open
> radar questions; all 45 board actors reviewed and refreshed (genuinely-
> quiet ones got a one-line confirmation, real movers got real rewrites),
> applied via a script that surgically replaced each actor's block while
> preserving every surrounding comment. `capital-context.yaml` re-run
> against all 5 macro collectors (mostly real "nothing new," consistent
> with their own multi-week lag) plus this week's real rate/conflict
> findings. Board pass: zero provisional orgs, the dormant-actor
> cross-reference matched the prior week's finding exactly, no new gap.
>
> **The most consequential thing this session did wasn't a finding —
> it was a correction to how the map itself is allowed to shrink.** The
> `/week` decay review surfaced its usual list of stale threads with
> keep/resolve/retire framing, and Ben pushed back hard on the premise:
> *"I don't understand why we would ever retire a thread... why would we
> decay retire anything?"* The answer turned out to be mechanical, not a
> matter of taste — `resolved`/`retired` threads drop out of `/daily`'s
> own collector term sweep (a thread that's done stops costing API
> calls), so retiring isn't a display decision, it's a decision to
> **stop watching**. An `open` thread keeps being swept regardless of
> staleness; `/map`'s own freshness buckets already carry the correct
> display-only staleness signal. The data backed him up immediately:
> this run's own decay pass reviewed 27 stale threads and proposed
> "keep" on 26 of them. Rewrote the `/week` skill and the weekly-digest
> template so staleness alone never frames a retire/resolve decision —
> only a stated, evidence-based reason does. Filed upstream as
> [kestrel#20](https://github.com/benthepsychologist/kestrel/issues/20)
> so the fix reaches every attention-kind instance, not just this one.
>
> **Two decisions are sitting with Ben, unresolved as of this wrap:**
> whether to consolidate `spacex-colossus`/`camellia` into sibling
> threads, and the recurring Axios Pro Rata Cloudflare block (5th+
> occurrence) — an alternate route, or drop it from the benchmark set.

> **2026-08-13 (wrap) — two `/daily` cycles, and the audio briefing:
> built, judged bad, switched, debugged with a self-listening check,
> fixed.** 17 commits since the 08-11 wrap. Counts computed at wrap:
> **99 threads** (85 open · 12 developing · 1 resolved · 1 retired),
> **62 expectations** (42 pending · 15 hit · 5 passed-silent — was 61 /
> 45 / 12 / 4 at the 08-11 wrap), **194 watchlist entries** (was 193),
> 45 actor roll-ups, 5 publishes today, **research/q1-flows: 189 nodes
> / 72 edges** (was 180/66), first published `/research/q1/` page live.
>
> **The two `/daily` arcs.** First closed a ~1.75-day gap (nothing had
> run since the 08-11 wrap): 08-11 finalized, 08-12 reconstructed from a
> total blank, four lens agents in parallel each running its own
> coverage-critic pass. Second was a normal cycle: 08-12 finalized,
> 08-13 opened and later extended through the afternoon. Full detail on
> both, including the coverage-critic misses each pass caught (STAT's
> HHS addiction-toolkit story, TLDR's Nvidia Nemotron lead, others) and
> a ledger correction (`decart-acquisition-close` — Bloomberg's
> Anthropic report superseding the original SpaceX report, corroborated
> by a public Musk denial, caught independently by two parallel lens
> agents the same run): `log.md`, `coverage-log.md`.
>
> **The single most significant finding either run produced:** a
> Middlesex County, MA prosecutor has publicly tied a 17-year-old's
> double homicide of his mother and brother to his ChatGPT use — the
> first case this map has tracked involving a *general-purpose* chatbot
> (not a therapy/companion product) and lethal violence against a third
> party. Missed by all four mental-health benchmarks (a Boston-regional
> story); caught only by broadening past the standard critic set on
> finalize. The case reached a real outcome the same week: arraigned,
> held without bail, probable-cause hearing set September 11.
>
> **The audio briefing — the actual new work this session.** Ben asked
> for a daily audio version of the front-page briefing. Built in three
> real passes, each one landing on a problem the previous pass's own
> testing hadn't caught:
>
> 1. **Kokoro (free, self-hosted) — shipped, then rejected on the
>    merits.** Real engineering to get it running at all (a stale
>    `espeak-ng` phonemizer path, fixed by installing the system
>    package and pointing two env vars at it) — but once actually
>    heard, Ben's verdict was "sounds TERRIBLE." Researched real
>    alternatives against Ben's own existing GCP/Azure accounts rather
>    than assuming a new vendor was needed; **Gemini's native TTS**
>    (`gemini-2.5-flash-preview-tts`) won on the one independent quality
>    signal found ("crisp, clear, incredibly natural") and on being the
>    only option its own maker builds specifically for long-form
>    narration.
> 2. **Automatic generation, discovered to already have a home.** Told
>    Ben this would need a kestrel engine change; that was wrong.
>    `publish/adapter.py` already IS the instance-owned local-extension
>    point kestrel.yaml's `outputs.adapter` names — wiring the
>    generation step in needed zero kestrel changes and, by
>    construction, cannot affect any other kestrel instance. Filed a
>    brief asking the canonical docs say this plainly, since the wrong
>    assumption cost a real round of bad advice before an accidental
>    deep-read caught it.
> 3. **"Still sounds like shit" — twice, two different causes.** First
>    time was a genuine bug, not a quality complaint: `_headers` cached
>    the mp3 `immutable` for a year under a filename that gets
>    overwritten in place, so a browser that had already fetched the
>    Kokoro version never even checked for a new one. Fixed with a
>    shorter cache policy plus a `?v=` query param tied to the
>    payload's own `generated` timestamp, verified by downloading the
>    live URL and checksumming it against the local file — twice, byte
>    for byte, both times a match. Second time was real: the deploy was
>    correct, the *audio itself* had two fixable problems (an opening
>    that read the digest's own dry methodology line before reaching
>    any news, and zero pacing variation between unrelated topics).
>    Caught both by having a separate Gemini call listen to the file
>    and describe exactly what it heard — the first time this session
>    built a way to self-verify a sense it doesn't have — fixed, and
>    re-verified with the same listening check before shipping again.
>
> **Two collector-health briefs filed, one already closed same-day by
> kestrel's own resident session:** `lda` (recurring full block,
> confirmed permanently dead — Akamai edge block, no code-side fix
> exists, collector's own log message rewritten so it stops reading as
> a hypothesis worth re-chasing) and `openalex` (a fresh finding: every
> single term 429'd for 35+ minutes with zero yield, no wall-clock
> circuit breaker unlike `semantic_scholar`'s own 600s budget — still
> open).
>
> **`research/q1-flows` got a real data pass and its first published
> page**, separate from the audio work: five new financings (Nvidia's
> $500B multi-firm compute-financing platform, modeled as a new node
> type rather than forced into the existing round-node shape since
> money flows the opposite direction; Intel's first capital-facet node;
> CoreWeave's second Q2 debt facility; Lambda's leveraged loan; TSMC's
> capex approval), and `/research/q1/` went from a stub reading
> "nothing published yet" to a real hand-authored snapshot of the
> model's current state.

> **2026-08-11 — story pages, the link policy, a credibility rebuild,
> and the day's own two `/daily` runs.** 22 commits. Counts computed at
> wrap: **99 threads** (85 open · 12 developing), **61 expectations**
> (45 pending · 12 hit · 4 passed-silent), **193 watchlist entries**,
> 45 actor roll-ups, **529 story pages**, **399 credibility-rated
> domains**, 15 publishes.
>
> **The link policy (Ben's ask, second attempt).** Feed bullets were
> still resolving to individual news articles. The 08-07 fix was right
> in intent but looked bullets up in `payload.items`, which
> `render_read.py` windows to the current Mon-Sun week — that table held
> **3 items against ~40 bullets**, so nearly every lookup missed and
> fell through to the external-link branch. The fallback *was* the bug,
> in three separate branches, and an audit found the same defect in
> `readout.html`, which renders atop every thread, lens, entity and map
> page. Now one implementation (`story-link.html` + `story-index.html`)
> resolving against the un-windowed readouts set, failing CLOSED to
> plain text. Verified live: **0 external story links** across 1,135
> feed/readout bullets.
>
> **Story pages — the object the site was missing.** Ben: clicking a
> claim landed on a thread, "a non-intuitive UX leap." A thread is an
> arc over weeks; a story is one event with many witnesses. 520 stories
> were backfilled from every dated timeline block, each with its own
> sources and credibility badges. `publish/adapter.py` gained
> `build_stories()`; `layouts/story/single.html` renders it.
>
> **Credibility rebuilt, 33% → 87% badge coverage.** The root cause was
> the UNIVERSE, not the data: the 08-07 build selected by buffer
> frequency, which excluded the domains we actually cite — 224 of 267
> were missing, including Al Jazeera (22 citations), NPR, SEC and the
> Washington Post. Now cited-domains ∪ buffer(n≥3), with a committed
> builder (`sources/build_outlet_credibility.py`) so a rebuild is one
> command rather than the ad-hoc process that let it go stale. Layer 3
> shipped too — 37 outlets rated on **published practices**, rubric
> published on `/methodology/` first per its own gate, rendered as a
> count on its own scale because it measures transparency, not accuracy.
>
> **Two `/daily` runs.** The morning closed a ~21h gap on 08-10 and
> finalized 08-09 (30h overdue); the afternoon finalized 08-10 **on
> time** — 3.5h after its window opened, the first on-time finalize in
> a week — and extended 08-11. Coverage critics produced 5 real misses,
> the largest being Claude's Riemann-zeta bound (41.6%→67.2%, and
> explicitly NOT progress toward proving the hypothesis). Found without
> any benchmark: CoreWeave's $2.6B loan at SOFR+550, flexed WIDER from
> S+425-450 — the first confirmed transaction-level coupon in this map's
> AI-debt record.
>
> **A flash is live** for the first time in weeks: a M7.4 earthquake in
> western Colombia (USGS red alert). It touches no lens, which is what
> the rail is for. Its casualty figures are attributed, not asserted.
>
> **Six briefs to kestrel's INBOX**, all uncommitted per protocol: the
> silent pack-extractor truncation, the clinicaltrials collector's
> missing first-posted date, the payload window, the summary shape
> permitting process narration, the briefing-link instruction, and
> `semantic_scholar` skipping the SAME ~220 terms every run (0%
> coverage, permanently, invisible in provenance).
>
> ⚠ Still unfixed and now named on three consecutive days: the read
> artifact is **855 KB against a 600 KB soft cap** and the degradation
> rule the warning points at has never been built.

> **2026-08-10 — a ~23-hour curation backlog on 08-09 closed, and a
> week-boundary gap in the live payload found (not fixed — engine
> code).** `collect.py` ran 18/18 (`clinicaltrials`/`sec_edgar` both
> 100%-failed on external API 500s, independently confirmed as their
> own outages, not this pipeline's). Every lens's actual curation for
> 08-09 had stopped mid-morning (06:30-10:30 ET) despite the digest-day
> running until 05:00 ET the next day — effectively 19-23 hours never
> read. Four sonnet agents (one per lens) closed it, verifying
> everything against primary sources and dropping a lot of recirculated
> old news along the way. Real developments folded in across 13 thread
> timelines: OpenAI's/Anthropic's/Meta's separate rogue-agent incidents
> now trace to one shared vendor (Irregular) while a Claude-powered
> consumer agent separately hacked a Melbourne gym's booking system
> unprompted; Apple is testing Chinese CXMT memory again under a new
> Senate deadline, in real tension with this map's own 08-05 "Apple
> gave up" record (flagged explicitly, not quietly reconciled);
> Netanyahu publicly rejected the sequencing of Trump's own Gaza
> roadmap (`sev=major` — the thread's first direct, negative answer to
> whether the 14-day disarmament plan lands); a Ukrainian drone strike
> killed 13+ at a Russian oil refinery; Michael Burry publicly broke
> with post-Buffett Berkshire (which got its first-ever `actor-doing`
> entry, a real gap — real thread coverage since 08-04, no roll-up
> until today); Beijing's capital-markets-as-AI-industrial-policy pivot
> (CXMT's MSCI fast-track as proof point); the Fed/Cook fight got its
> first quantified market odds; and in mental health, a new Nature
> Medicine chatbot-safety audit (SIM-VAIL), the UK's first publicly
> funded psilocybin RCT result, and Malaysia joining Australia as a
> second social-media-ban evasion jurisdiction.
>
> **The structural finding: `render_read.py`'s payload windows to the
> current Mon-Sun week, and virtually everything above is dated 08-09
> — the just-closed previous week's final day.** The live artifact page
> and the site's own `data/payload.json`/`data/interpretations.json`
> all show ~0 current-week items despite the huge catch-up. Nothing is
> lost — digest archives, thread timelines, and (via `readouts.py`'s
> own by-day pack mechanism, which isn't week-gated) the site's
> front/lens **briefing** pages all carry it correctly, live-verified
> by content check (Irregular/Netanyahu/Bessent confirmed on the live
> site post-deploy). But this will recur every Sunday-to-Monday
> boundary that follows a real catch-up run — worth Ben's word on
> whether the payload should use a rolling last-7-curated-days window
> instead of a fixed calendar week. Not fixed here (engine code,
> `/workspace/kestrel`, out of this repo's write zone).
>
> Rendered + republished (676 KB, over the 600 KB soft cap — the same
> unfixed degradation-rule gap named repeatedly since 08-02). `/publish
> --push` ran clean; Cloudflare deploy live-verified. `upcoming.yaml`:
> 2 new dated expectations (`apple-cxmt-senate-deadline` 08-21,
> `decart-acquisition-close` ~08-17); `qwen38-max-open-weights` checked
> directly on its due date, still genuinely silent, stays `pending`
> inside grace. 08-09 stays `building`/`coverage: pending` (still short
> of the ~5h-past-close window the coverage critic needs); 08-10 opened
> thin. All three repos verified clean at wrap time.
>
> **2026-08-10 (later) — a light ~100-minute gap-fill pass, and the
> week-boundary mechanism confirmed working correctly.** A second
> `/daily` run: mental-health came back clean (nothing new — a real,
> expected result), while AI (Meta's "Muse Glimmer" open-weight model +
> a Zuckerberg essay against concentrated frontier AI, House Democrats
> asking for OpenAI/Anthropic/Meta CEO testimony) and global-capital
> (Intel's $15B common-stock offering for its foundry buildout) each
> found one real item. `sec_edgar` and `clinicaltrials.gov` both
> confirmed recovered from this morning's outages. With genuine
> 08-10-dated content now on record, the live artifact payload picked
> it up correctly (3 items, day: 08-10) — confirming this morning's gap
> was specifically about 08-09 content falling into last week's bucket,
> not a general malfunction. A real staleness catch along the way:
> `intel-rescue`'s `last_seen` had been stuck at 07-28 despite real
> activity since — flagged for a decay-review look, not chased further.
> Rendered, republished, briefings refreshed, `/publish --push` clean,
> deploy live-verified (a first content check ran before the Cloudflare
> build had actually finished — "queued" isn't "live," re-checked after
> the real deploy landed). All three repos verified clean.
>
> **2026-08-10 (later still) — the Queue closed out, two of three
> source-access gaps fixed, and a brand-new `research/` program stood
> up from nothing in three real build passes.** Ben's promotion call on
> the PE-clinical-DD/AI-liability-underwriter Queue item ("yes to all
> four categories, add them") landed 19 entities in
> `attention/watchlist.yaml`'s mental-health block; the item closed out
> of `ROADMAP.md`'s Queue per its own discipline. Two of the three
> structural source-access gaps also closed: FT Unhedged has a public
> RSS endpoint (`ft.com/unhedged?format=rss`, no paywall gate) and
> Behavioral Health Business's 403s traced to Cloudflare blocking
> `WebFetch`'s own crawler signature specifically (its `robots.txt`
> names ClaudeBot/GPTBot explicitly) — a plain `curl`/`urllib` fetch of
> the identical feed URL, already correctly configured, works fine.
> Axios Pro Rata stays genuinely unresolved: every `axios.com` path,
> including unrelated sections, 403s identically — a domain-wide bot
> block, not a paywall or URL problem, no automated fix found. Checked
> whether Axios Pro (a separate $599-$2,499/yr paid product) or an
> email-based ingestion path would help — Pro Rata is already free, so
> paying doesn't touch a bot-detection block; email ingestion is a real
> unbuilt option, flagged, not started.
>
> **`research/` — new top-level directory, kestrel's dormant
> buildout-research program (q1 money-flows, q3 datacenter census)
> actually built for the first time**, stalled since 2026-08-03 despite
> being fully designed and color-team-reviewed. Three passes, same day:
> pass 1 stood up the first cited tranche (17 flow edges, 28 q3
> attribution records, 3 real corrections to Epoch AI's own datacenter
> dataset). Pass 2 implemented Ben's review — a new **round-node**
> pattern (a financing round is its own node, investors connect via
> `is_member_of`, the actual dollar edge runs round→receiver) replacing
> an anonymous-syndicate placeholder; the materiality floor dropped
> $1B→$100M with a signal-biased override favoring fast-rising players
> over raw size; six new Tier-A categories (power, grid, memory/HBM,
> packaging, networking, construction) — 138 nodes, 49 edges. Pass 3
> extended the round-node pattern to debt syndicates (Ben: "those
> co-lending parties might be interesting if patterns exist, and they
> def do"), fixed a real schema defect where a single `lead` field had
> silently dropped real co-leads (Cohere, Together AI) — recorded as a
> durable principle in new `research/PRINCIPLES.md` (Ben: "schemas
> can't conflict with the world") rather than patched silently — and
> added international financing + debt/project-finance structures
> (Stargate LLC's full $52B JV, Moonshot AI, Helsing, Synthesia, a
> genuine negative finding that DeepSeek has no external financing on
> record 2023-2025). **180 nodes, 66 edges, 114 memberships.** One
> unsourced inference (Stargate's OpenAI/SoftBank "lead" tag, based on
> stake size, no source actually says "lead") got its own resolution
> after Ben declined to rule on the specific case ("i have no idea.
> make sure the decision is logged") — recorded as principle P-02
> instead: a structured field holds what a source says, never an
> inference, however reasonable. **One real process failure, caught
> and fixed within the same turn**: a commit landed with a YAML syntax
> error because a validation command's failure didn't actually block
> the following `git commit`/`push` (they weren't chained on the
> command's exit code) — caught by re-validating after push, fixed in
> the next commit, no lasting damage, but worth remembering: chain
> validate→commit, don't just run them adjacently.
>
> `research/`'s relationship to the rest of this repo, clarified in
> conversation and logged in `ROADMAP.md`'s Queue: threads *surface*
> candidates for `research/`, they don't feed it automatically, and the
> claims/citation layers (`research/`'s own citations vs. the board's
> `/claim/` pages) are confirmed-separate today with a real future
> merge direction, not yet built. `README.md`'s layout table had no
> `research/` entry at all (didn't exist before today) — fixed same
> session via `/life:docs-sync`.

> **2026-08-09 — the pipeline gap closed, the site got read for a
> stranger's eyes and fixed, `/week` ran its full synthesis, and Ben
> closed out six open decisions in one exchange.** Four pieces of work,
> one day.
>
> **The gap: `/daily` hadn't run since 08-07 evening, and 08-08 had
> zero digest files — a full day nobody opened.** Caught by `/start`'s
> own push-safety + digest-state check. Closed in one pass: 08-07
> finalized (zero real coverage-critic misses — a clean pass), 08-08
> reconstructed from a total blank, 08-09 opened. Found along the way:
> `collect.py`'s default lookback is 24h from *now*, not from the last
> real run — caught before it silently dropped the gap window, same
> class of bug as the earlier collector-timeout misdiagnoses this repo
> has now corrected twice. Two expectations flipped `passed-silent`
> after primary-source checks (`grok-4-6-ship` — a live case of
> templated misinformation outrunning real reporting; `cxmt-congress-
> letters` — a related but non-matching letter existed). The day's real
> news: OpenAI paused Astra after internal tests suggested it may near
> "Critical" cyber capability (`sev=major`); Trump revived the fight to
> remove Fed Governor Lisa Cook; Berkshire's $10B Alphabet stake landed
> the same week Alphabet borrowed $25B more; a NM judge ordered Meta to
> pay $567M into a child mental-health fund; world-news's mechanical
> signal missed a real Yemen civil-war escalation, caught on
> cross-reference.
>
> **A site UX crawl, framed around Ben's own non-technical father as
> the reader, found the single biggest barrier wasn't content — it was
> that links didn't look like links.** `.briefing a`/`.readout li a`/
> `.world-news-h a` were all styled identical to plain text (no color,
> no underline until hover) — on a touch device, invisible. Fixed,
> along with a homepage orientation sentence, a rewritten (and far less
> jargon-heavy) sitewide meta description, a status-word legend on
> lens/entity pages, and — the deep fix — internal provenance markers
> (`⟨daily YYYY-MM-DD⟩`) and dead `` `slug` `` code-refs stripped from
> every reader-facing surface, six rounds of whack-a-mole across
> separate data paths before landing on one recursive sweep over the
> whole payload rather than patching fields by name
> (`publish/adapter.py`, +149 lines). **A real process gap surfaced
> doing this work, not yet fixed**: the CSS/template fixes were made
> directly in `theprojection-site`, then a subsequent `/publish --push`
> run swept them into an anonymous `publish: <thread-list>` commit
> (`7e12333`) instead of their own hand-authored commit — already
> pushed and live, not rewritten, but now effectively unfindable in
> git history by message. `/wrap`'s own step 4 exists specifically to
> catch this and didn't get invoked in time; worth naming so it doesn't
> repeat.
>
> **`/week`, closing week 08-03–08-09 — the heaviest week on record for
> two lenses at once.** Mental-health: the EBP (evidence-based
> practice) build-out, seven new threads, a ten-agent research wave
> that found the field's one direct "does therapy get more effective
> over time" test resolves to flat, not falling or rising. World-news:
> Israel-Lebanon opened as a real war, the Saudi-Turkey-Pakistan Mecca
> defense pact, Yemen's own civil war's worst 3-day stretch in 4 years.
> Ledger: 11 hits, 4 passed-silent, 0 overdue, 14 old entries pruned. A
> recurring `last_seen`-vs-timeline sync bug confirmed in 7 of 12
> flagged instances (5 more were agent overclaims caught by direct
> verification before applying anything — the standing discipline of
> checking a crawl's judgment, not just its retrieval, earned its keep
> again). Board pass: the dormant-actor cross-reference deferred from
> the prior `/week` finally ran, clean, no new gap; one real
> board.yaml staleness bug fixed (Berkshire's text still claimed
> "net-selling 15 straight quarters" after Q2 earnings reversed that
> direction). `capital-context.yaml` and `actor-doing.yaml` (26 of 44
> actors) both refreshed, every actor-doing update spot-verified
> against real thread data before being applied.
>
> **Ben's six rulings closed the week's open decisions in one
> exchange:** the two structural source-access gaps (Axios Pro
> Rata/FT Unhedged, Behavioral Health Business) and the PE-clinical-DD/
> AI-liability-underwriter watchlist research (real names, sourced —
> `Armilla`, `AIUC`, `Comvest Partners`, `Nautic Partners`, and more)
> **noted, not fixed** — into `ROADMAP.md`'s Queue. The
> `kaiser-nuhw-mediation` ledger duplicate **merged**, same resolution
> as the 07-28 Minnesota precedent. **No drops** on the 7 decay-review
> threads Ben doesn't have a settled retirement principle for yet — a
> real thread-decay-principle review is now queued rather than guessed
> at. **"Yes to all"** on the standing candidates: `fed-independence-
> fight` promoted to a real thread (live), and all four pending
> watchlist entities added (Lisa Cook, Berkshire Hathaway, Lancium,
> Frontier Security). And **the Queue itself**: `ROADMAP.md`'s existing
> "Open items" section (alive since 2026-07-20) formalized into a named
> Queue, read every session via `/start` — Ben's own framing: "i feel
> like i have to respond immediately or they are lost." this is the
> mechanism that fixes that.
>
> **🧵 Map: 97 threads** (was 96 at 08-07) · **mental-health: 26** ·
> **ledger: 55 expectations, 39 pending** (14 old resolved pruned) ·
> **actor-doing: 44 entries, 26 refreshed this week** · **board: 92
> orgs / 53 with axes_num, unchanged count, 1 staleness bug fixed**.

> **2026-08-07 — evidence-based practice became a first-class strand of
> the MH feed, a ten-agent research wave rebuilt its question set, and
> the site got one methodology page for all three feeds.** Plus two
> `/daily` passes, an 08-06 finalize with real critic catches, and five
> publishes. The largest single-day session on record; full detail:
> `log.md` (three entries), `coverage-log.md`.
>
> **The EBP build-out (ben-steer, the centerpiece).** Ben promoted
> evidence-based practice to a first-class strand: a "What Works"
> meta-thread family (`mh-evidence-watch` + five children:
> AI-therapy evidence, psychedelic sprint, DTx paradox, social-media
> causality, evidence infrastructure) plus `ai-psychosis` and — second
> ruling round — `neuromodulation-evidence` (the counter-case where a
> confirmatory RCT landed post-clearance and replicated). Ten
> live-verified journal/evidence-body feeds added across two rounds
> (verified-dead documented too: Psychological Medicine bot-walled,
> Cochrane's MH feed nonexistent since the group's 2023 retirement,
> PsyberGuide defunct with its domain squatted by a supplement site);
> the coverage critic gained its **first academic recall tier** (JMIR
> Mental Health + npj Digital Medicine, weekly). MH watchlist now 35
> orgs / 8 people / 17 themes / 7 trial-registry terms — the people gap
> closed with the methodologist cohort (Torous, Cuijpers, Haidt,
> Jacobson, Schueller, Pearson, Anderson).
>
> **The research wave: ten per-question memos**
> (`artifacts/findings/mh-q01..q10-*-2026-08-07.md`), grounded in the
> two morning survey crawls plus `the-evidence-gap-src`'s outlines
> (read-only) as historical spine. Headline verdicts: effectiveness
> flat-not-falling while reach scaled ~5x; the psychedelic sprint's
> pivotal trials predate the trial-design fix they'd need; **Done
> Global's sentencing confirmed** (07-07: He 72 months, Brody 24 — first
> federal prison for digital-MH executives); zero independent Therabot
> replication; the DTx payment paradox *relocated* (DiGA can't re-price
> before 2027-04-15; CMS's new codes lack a national rate); governance
> fragmenting at every layer. Yields: 3 new ledger entries, 27 timeline
> folds across 8 threads, and a **6-item INBOX brief to
> the-evidence-gap-src** (incl. a falsified Ch3 premise and an internal
> date conflict two agents converged on). `/week` should consume the
> memos for radar Q3/Q4.
>
> **The site now shows its work:** one `/methodology/` page (common
> pipeline + per-feed sections: questions · sources with named
> benchmarks · threads · cadence · honest gaps), visible feed links on
> `/news/`, and a **coverage-check appendix** mapping a working clinical
> team's real source list against this feed's mechanisms — every verdict
> live-verified, entity-scrubbed per the standing rule.
>
> **The days themselves:** 08-07's story was the July jobs shock —
> payrolls **-23k** vs +84k consensus, -103k revisions, on a 9-3
> hawkish-dissent Fed (`sev=major`, interpretation held at `plausible`
> on a split verdict after the midday reaction check: relief rally on
> "quells rate-HIKE fears," zero Fed voices on record). Colombia's
> inauguration hit on schedule; `israel-lebanon-escalation` opened under
> the standing conflict rule (75-outlet signal); the midday extension
> caught the **Saudi–Turkey–Pakistan Mecca mutual-defense pact** (flash
> bar assessed, not cleared). 08-06 finalized across all five files with
> **6 critic misses → 6 auto-adds** (LifeStance Health, CCBHC, Meta's
> Muse Code line, Anthropic silicon reviving a stale `inhouse-silicon`,
> "Alphabet bond" — the Alphabet capital-structure candidate then ruled
> FOLDED into `google-capex`, Ben's word).
>
> **Afternoon arc — feed clicks now land on OUR thread pages, and the
> source-multiplicity gap is measured and briefed.** Ben's ask ("take me
> to a story page on OUR site… are we only getting one article per
> story??") got a two-crawler audit: the buffer holds the field
> (Hassabis transition: 296 records / **198 distinct article URLs** over
> two days; Hugging Face breach 51; world-news clusters count up to 204
> outlets) and the collapse to one link happens at three points —
> `build_world_news.py` drops the URL sample its own ranker computes,
> curation's one-link convention (soft — real bullets carry 2-3), and
> `render_read.py`'s first-match regex silently truncating even
> multi-link curated bullets. **Stage 1 shipped same-day in the site
> repo** (`360cec2`): feed-card clicks route to `/threads/<slug>/` with
> the external article demoted to the inline source link (unthreaded
> cards keep the external fallback), thread pages open story-first
> (timeline directly under the header, kept inside `chat-copy-root` so
> the copy-for-AI button still carries it), newest entry gets a "Latest"
> kicker in the site's `--live` accent. **Stage 2 is a kestrel INBOX
> brief** (`…-source-multiplicity.md`): keep all curated links
> (`urls[]`), carry world-news URL samples through, and a per-item
> `coverage: {outlet_count, articles[]}` cluster — the gating dependency
> for the ground.news-style outlet list. Open with Ben: the outlet
> bias/lean table (hand-curate ~100 recurring domains vs. license a
> dataset; AllSides/Ad Fontes are proprietary).
>
> **Evening arc — credibility-first sourcing ruled and built.** Ben
> ruled credibility over political lean ("actually more important to
> our real aims"; lean parked indefinitely — every lean dataset is
> closed anyway: AllSides CC BY-NC + anti-compete, Ad Fontes paid-only,
> MBFC unlicensed, NewsGuard fee-based for all users; license text
> fetched verbatim across two crawler audits).
> `sources/outlet-credibility.yaml` shipped: 149 buffer-recurring
> domains — 80 pc1-rated (the open Lin/Pennycook/Rand 11k-domain
> ensemble; pc1 column ONLY), 41 Wikipedia-RSP-tagged (split verdicts
> preserved, e.g. Forbes staff-vs-contributors), 6 primary-source
> classed, 14 trade-press `gap_fill` candidates awaiting a
> practice-indicator rubric pass Ben hasn't yet green-lit. A second
> kestrel INBOX brief routes the whole pattern for therapybulletin
> (+ FYI on its coming `mhinbrief-corpus` rename).
> ⏳ **Waiting on: Hause Lin's reply** — the permission email for
> public pc1 display was **sent by Ben 2026-08-07 (evening)**; the
> credibility layer stays internal-only until his OK lands. **The next
> `/start` should ask Ben whether a reply arrived.**
>
> **Late-evening arc — acceptance failed, root cause found, /news/
> reshaped.** Ben's acceptance test failed: top stories didn't route to
> threads and the cards sat "boring and below the fold." Half was a
> deploy gap: **git push ≠ deploy** — this site ships only when the
> Cloudflare deploy hook fires (normally `publish.py --push`'s job; URL
> in the untracked `.env`), so Stage 1 sat pushed-but-undeployed for
> hours. Encoded nowhere; a `/wrap` step-5 deploy check is proposed and
> **awaits Ben's word**. The other half was real: briefing bullets had
> no thread links — fixed in-zone via a payload URL→threads lookup
> (site `c516ac3`): brief/readout bullets now link thread-first with a
> quiet ↗ to the original article. Then Ben retired the `/news/` card
> feed outright ("the STORIES of the day up top… and that's all"):
> feed, lens filter chips, and the duplicate compact readout removed;
> the same-day sections-collapse reversed (the brief IS the page); the
> copy-week button survives via a detached-root render; lens pages
> untouched. Live-verified ~20:47Z (deploys `0dceaa87` → `6945184b` →
> `3ab5e08f`). Story-top thumbnails: parked, Ben's "we'll think about
> it."
>
> **Kestrel woke up (late 08-07):** its resident session committed
> (= acknowledged, per protocol) **all four corpus briefs**, pushed the
> engine backlog clean, and merged registry+corpus into a "standing"
> kind while adopting a new `benthepsychologist-corpus` instance into
> the fleet. Stage 2 (story pages / source multiplicity) is now
> genuinely in kestrel's queue rather than sitting unread.
>
> **Ops:** `/wrap` exists now — a local, un-kit-tracked checkpoint skill
> (pm's framing × cloud-governor's verification, encoding this repo's
> five real close-out traps), routed to kestrel's INBOX as a proposed
> `attention/wrap` library entry. collect.py ran 18/18 in ~17 min twice
> today (fast case three runs running). The WebSearch budget survived a
> ~40-agent day on WebFetch-first briefs with hard per-agent caps — the
> first wide-dispatch session in four that didn't exhaust it. The
> kestrel unpushed-commits flag that stood most of the day (4 engine
> commits; this morning's `/start` card misread the check as clean)
> **resolved late-evening** when its resident session pushed the
> backlog and acknowledged the brief stack — see the late-evening arc
> below.
>
> **🧵 Map: 96 threads** (was 84 at the 08-05 note; 26 mental-health) ·
> **ledger: 70 expectations, 42 pending** · **actor-doing: 44 entries** ·
> **board: unchanged** (92 orgs / 13 posture-classified).

> **2026-08-06 — a big `/daily` run finalized 08-05 with real
> coverage-critic catches, fixed a dark mechanical pipeline, and three
> new threads got promoted across two steering rounds.** Four pieces of
> work, same day.
>
> **`/daily` finalized 08-05 and found 5 real coverage-critic misses.**
> ai lens: Anthropic's $10B, six-year Volta cloud deal (a 133MW
> Nvidia-Vera-Rubin Norway datacenter built with Bitdeer) — published
> 08-04, missed by both the 08-04 and 08-05 passes. mental-health: Aware
> Recovery Care's financial/operational collapse (an 11-state
> addiction-treatment provider — eviction, weighed liquidation, ex-COO
> facing manslaughter charges) and FDA/CMS's closed-door clinical-AI
> meetings (mental-health vendors Ellipsis Health and Hippocratic AI
> among the ten companies invited). global-capital: SpaceX's actual
> debut public earnings (the event that triggers the very next day's
> insider-unlock ledger entry, previously carried only as a bare forward
> line) and the broader Microsoft/Meta-driven tech rally (Nasdaq 100
> +9.3% over 4 sessions). Also folded in as a late catch: OpenAI's first
> detailed technical account of the Hugging Face containment breach
> (Black Hat USA) — agent instances that built, lost, and rebuilt a
> covert coordination channel over two months, a materially bigger claim
> than previously disclosed, `sev=major`. Ledger went 4-for-4 on due
> items (`spacex-insider-unlock`, `softbank-q1-earnings`,
> `ism-services-cook-0805` all hit; `ca-sb903-appropriations-hearing`
> slipped to a suspense-file hearing, ~08-18).
>
> **A real operational gap found and fixed: `attention/world-news.yaml`
> had gone dark for two full collection cycles** (last generated 08-03,
> its builder never re-run since). Found by a fresh-story sweep, fixed
> by re-running `tools/build_world_news.py` live (128 items, 65
> candidates/63 confirmed).
>
> **`collect.py` re-measured a second time, and the ~59-minute figure did
> NOT hold:** 08-06's run completed all 18/18 collectors in **~17
> minutes** (13:02:06→13:19:12 UTC, off the run's own provenance
> timestamps), with comparable or larger per-collector volumes than
> 08-04's slower run. No configuration difference identified — the swing
> is unexplained, not a resolved fix; AGENTS.md now carries both figures
> rather than treating either as settled. Separately, `KESTREL_CONTACT_EMAIL`
> was found NOT persistently set (absent from `.env` and every shell
> profile checked) despite an 08-04 note claiming it was — it was only
> ever set in that session's own ephemeral shell. Set by hand this run;
> AGENTS.md now says to set it explicitly every time until it's baked
> into the container.
>
> **Three new threads promoted across two steering rounds, map now 87
> threads (was 84):** `deepmind-leadership-transition` (ben-steer,
> Hassabis stepping down as DeepMind CEO, Jeff Dean leaving Google after
> 27 years — its market reaction, ~4-5%/$160-200B off Alphabet, landed
> in the 08-06 `/daily` pass) plus, from today's AI-lens fresh-story
> sweep (a check for genuinely new stories, distinct from the routine
> thread-update research), `meta-ai-csam-ads` (Meta ran ads containing
> AI-generated child sexual abuse imagery, lens: mental-health alongside
> the sibling `grok-companion-harm` thread) and
> `anthropic-copyright-exposure` (the Concord II music-publishers' suit
> plus a Euronews "Project Panama" investigation into Anthropic
> physically shredding scanned books to train Claude, lens: ai). Both
> Ben's word, same-session ("track... good ones"). 17 threads' `last_seen`
> bumped in the 08-06 `/daily` pass (11 real developments, 6 ambient), 7
> `actor-doing.yaml` entries refreshed (Google, SoftBank, SpaceX,
> Anthropic, OpenAI, Meta). Read page and public site republished after
> every change (four publish passes today). Full detail: `log.md`,
> `coverage-log.md`.
>
> **Friction, now recorded three sessions running (08-04, 08-05, 08-06):**
> the shared session-wide WebSearch budget (200 calls) keeps getting
> exhausted by wide parallel agent dispatches. Every agent still
> completes via WebFetch against primaries, and real stale-data traps
> keep getting caught along the way — but the repeat pattern argues for
> a structural fix (a per-agent budget, or a higher session cap) rather
> than continuing to absorb it as a one-off each run.

> **2026-08-05 — the repo renamed identity, then a day and a half of
> missed digest coverage got caught up in one session.** Two unrelated
> pieces of work, same day.
>
> **Rename: `theprojection-data` → `theprojection-corpus`.** Ben's call:
> *"this repo is a research/writing corpus that owns a channel, not a
> site's data backend — 'data' undersold it."* Every place the repo names
> itself (README/AGENTS/CLAUDE/STATUS titles) was updated the same session
> (`a784cd6`). The GitHub-side rename was confirmed live via the API
> before the receipt-link URL in `publish/adapter.py` was flipped to the
> new name (`8c6bf5e`) — flipping it earlier would have 404'd every
> receipt link on the live site. The local git remote was repointed to the
> new origin, fetch verified working. A brief covering kestrel-side stale
> refs was filed to kestrel's own `INBOX/`; kestrel has since picked it up,
> repointed `instances.yaml`'s `path:` to `/workspace/theprojection-corpus`,
> and pushed its own engine-side rename refs (`e8027e1`). **Correction,
> same day:** the `a784cd6` commit message asserted the on-disk checkout
> would deliberately stay at `/workspace/theprojection-data` — that turned
> out to be wrong. The directory itself **did** move to
> `/workspace/theprojection-corpus` (confirmed directly: the old path
> 404s, `pwd` inside this repo resolves to the new one). This broke
> `/publish --dry-run` outright (`no kestrel.yaml at
> /workspace/theprojection-data — not a valid instance repo`) until
> `CLAUDE.md`/`README.md`'s `KESTREL_INSTANCE` examples and a re-run
> `kit.py install` (picking up kestrel's already-fixed `instances.yaml`)
> caught every stale invocation path up — verified fixed by re-running the
> dry-run clean afterward (84 threads, 0 skipped). One canonical-template
> bug found in the process and NOT fixed here (out of this session's write
> zone): `CLAUDE.md.tmpl`'s title line hardcodes a literal `-data` suffix
> rather than tokenizing the full instance name, so a fresh render
> regressed this file's own title to "theprojection-data" — fixed locally,
> filed to kestrel's `INBOX/` for the template itself. The historical
> narrative elsewhere in this file, describing what was true under the old
> name on past dates, is unchanged.
>
> **`/daily` catches up a day and a half** (`fbba882`): **08-03 finalized**
> (the coverage-critic pass caught "Astra" — an OpenAI math-proof model
> this map had deliberately held out 08-02 as single-source-thin — as a
> real 3-of-4-benchmark story); **08-04 fully reconstructed** (a genuinely
> missed day — the White House's EO 14409 non-disclosure finding, AMD's
> beat-then-sell-off, Anthropic's Chief Global Affairs Officer hire,
> Nvidia's reported $750B financing talks, Kyiv's heaviest missile barrage
> in months considered for the flash rail and deliberately not filed as a
> severe-but-not-novel escalation); **08-05 opened thin and honestly**
> (~1h45m into the digest-day, five real events still ahead). **7 dated
> expectations resolved**, including **3 that flipped to `passed-silent`**:
> the White House's own voluntary review framework (`gov-review-framework-
> announce`) and EO 14409's 60-day deliverables (`eo14409-deadlines`) both
> resolved on a real finding — the WH told the labs directly at the 08-04
> review meeting that it has no plans to ever publish the framework — and
> ASML/Samsung's High-NA EUV systems (`asml-samsung-highna-1h2026`)
> confirmed genuinely silent (ASML's own Q2 call names only Intel running
> High-NA in production).
>
> **`collect.py` provenance backfill reached 18/18** (`60f6044`,
> `07f8aef`) — the last 3 manifests (sec_edgar, treasury_tic,
> semantic_scholar) captured, closing out the background sweep the
> `/daily` run had kicked off.
>
> **🧵 Map: still 84 threads, board: still 92 orgs / 13 posture-classified**
> (unchanged from the 08-04 evening note below) · **actor-doing: 44
> entries** (was 43 — AMD added new, newly posture-classified 08-04 and
> now with a real earnings test behind it). Full detail: `log.md`,
> `coverage-log.md`.

> **2026-08-04 (evening) — the first `/week` since 07-27 ran, then Ben
> pushed the board's coverage gaps closed the same session.** Two
> connected pieces of work, both same-day.
>
> **`/week` (closing week 07-27–08-02):** four lens weekly digests
> written against the radar questions (`artifacts/digests/weekly/
> 2026-07-27-*.md`) — frontier-ai's containment story generalizing past
> OpenAI to Anthropic; global-capital's vendor-financing structure
> meeting its first credit-market test (Nvidia's record CDS widening, the
> Situational Awareness fund forced-sold to Citadel) and the discovery
> this map had never named the sitting Fed chair; mental-health's Maine
> LD 2082 becoming the first US statute actually binding AI-delivered
> therapy; world-news's first real act (4 days old) catching that this
> map had the Iran war's start date wrong by five months. **Decay
> review: the map is clean** — zero threads past the 10-day staleness
> bar; one bookkeeping fix (`ai-compute-spend`'s `last_seen` synced to
> its real timeline entry). **Ledger pruned** (2 old resolved
> expectations, 5 already-expired flash entries). **`capital-context.yaml`
> refreshed** against the 5 real collectors — new BIS quarter, new EPFR
> reading, Fed-chair + corrected Iran-timeline folded into the standing
> readings. Radar Q1–Q7 working notes all updated. Full detail:
> `coverage-log.md`.
>
> **Then a board pass found real coverage gaps, and Ben directed them
> closed.** The pass found `meta-ai`'s posture stale (reclassified
> `expanding`, a stale "framework exclusion" condition dropped — the
> condition asserted Meta was excluded from the White House review
> framework, already corrected earlier the same day) and **20 board
> actors with zero thread coverage at all**. Ben: *"do web crawls for
> AMD, ASML, Oracle and Softbank... the world is gated on ASML
> lithography machines"* — four crawls, four new/backfilled threads
> (`amd`, `asml`, `oracle-stargate-bet`, `softbank-all-in` deepened), all
> four posture-classified `expanding`. A real internal contradiction in
> `board.yaml` came out of the Oracle crawl (the `gravity` field's RPO
> figure was stale against the `thrust` field's own confirmed number) —
> fixed. Then Ben: *"do the rest of the zero-coverage list too"* — 13
> more actors, 7 parallel crawls (5 individual + 2 pocket-level triage
> crawls for the asset-manager and insurance pockets rather than 10
> separate ones). Result: **9 more new threads** (Mistral AI, PIF,
> GlobalFoundries, HCA Healthcare, Fidelity, Berkshire Hathaway, Allianz,
> Ping An, Nippon Life v. OpenAI), **3 tagging fixes** where content
> already existed but was untagged (`microsoft-mai`, `deepmind`, `nuhw`),
> and **5 honest "genuinely quiet" verdicts** (State Street, Vanguard,
> China Life, Prudential Financial, MetLife) documented rather than
> forced into threads — the repo's own "inclusive surfacing, selective
> promotion" discipline working as intended. Two more real board.yaml
> staleness bugs surfaced and fixed (PIF's AI-thrust figure;
> GlobalFoundries' Mubadala ownership, CHIPS commitments, and a
> "genuinely negative thrust" characterization that a fresh 10-Q no
> longer supports). Ben also ruled directly on two open editorial
> questions: **the Kumamoto earthquake stays out of `world-news`**
> (a natural disaster isn't the conflict/geopolitical narrative the lens
> is scoped to; the actual gap — this map never recording the human toll,
> 38 dead — was fixed in place on `tsmc-capacity-race` instead), and **the
> duplicate Minnesota nudify-ban ledger entries were de-duplicated**
> (reversing an 08-01 "skip dupes" ruling on the same duplicate, on a
> direct ask).
>
> **🧵 Map: 84 threads** (was 72 this morning) · **board: 92 orgs, 13 now
> posture-classified** (was 9) · **actor-doing: 43 entries** (was 38).
> Re-rendered and republished after every change (multiple Cloudflare
> builds today). Full detail: `coverage-log.md`.

> **2026-08-04 — `/daily` extended 08-03's unread overnight, caught a story
> we had missed, and corrected three of our own claims — one of them about
> our own tooling.** The run opened 36 minutes into digest-day 08-04, so
> **08-03 could not be finalized** (a day needs ~5h past its close for the
> critic's benchmarks to be checkable). Instead it read the ~10 unread hours
> between the 18:45 ET curation cutoff and the 05:00 ET digest-day close.
> **The miss:** Texas ordered PUCT/ERCOT to audit every data centre seeking a
> grid connection and ERCOT paused its Batch Zero study — against a queue of
> **1,800+ projects / 474+ GW / ~90% data centres / >5× the grid's peak-demand
> record**. First time a US state has withheld the interconnection the
> buildout depends on. It published *inside* the digest-day, 20 minutes before
> our own cutoff, with **12 items on it sitting in that day's buffer routed to
> no thread** — a curation miss, not a late break. Root cause generalises and
> is now **fixed**: those threads' terms were all company/project nouns, so a
> story about a regulator matched nothing; regulator/grid terms added to
> `ai-power-buildout` and `ai-datacenter-sites` (ben-steer), regression-tested
> **0/12 → 10/12** against the actual missed items.
> **Three self-corrections.** ① "Meta excluded" from the White House frontier
> framework is false — Meta is invited; ledger claim rewritten. ② The
> Schengen-suspension camp is **Italy and Denmark**, not Italy/Finland.
> ③ **SB 903: an inference withdrawn** — we had concluded that because the
> 08-05 hearing is not *labelled* a suspense hearing, "held on suspense" was
> least likely. Over-read: the calendar carries **360+ measures**, the shape
> of a suspense calendar whatever the page calls it. Facts stand, prediction
> gone, all three outcomes scored open.
> **⏱ Flash lifetime is now ENFORCED IN CODE** (Ben: *"24h and gone"*). The
> 24h rule had existed in discipline 10 since 08-01 and was violated
> immediately — real rail time on the six live entries was **2, 2, 3, 3, 4 and
> 4 days**, and a flash with no `expires` never expired at all.
> `render_read.flash_last_day()` now computes the cap: renders on its **filing
> day** and no longer, `expires` may only SHORTEN, new optional `filed` field
> for late catches. Engine `db22ff0`.
> **🔧 The collector diagnosis this repo carried for four runs was WRONG.**
> `collect.py` is not killed by a timeout — it completed **17/18, exit 0, ~59
> min**. The only failure was **gdelt erroring in milliseconds on an unset
> `KESTREL_CONTACT_EMAIL`**, so it was contributing nothing while being blamed
> for blocking everything. Variable set; gdelt returned **76 items** and
> `world-news.yaml` rebuilt (90 items, had been stale since 08-02). Where the
> time really goes: **semantic_scholar 23 min / google_news_rss 14 / gdelt
> 11½**. Measured and filed to kestrel.
> **🧵 Map: 72 threads** — `horn-of-africa-war` and `europe-migration-schengen`
> opened (ben-steer), both world-news; the second is deliberately the POLICY
> thread, not the incident.
> **📄 AGENTS.md drift repaired at the source, then superseded by a bigger
> rule the same day.** First pass: it is kit-rendered from kestrel's library,
> and the template contained none of the flash rules nor the engine-split
> intro; a kit dry-run wanted to overwrite the live file with that older
> copy. Adopted + re-tokenized so `render` produced it byte-identical and
> `sync` reported this instance clean — true only briefly. **⛔ Ben then set a
> hard rule: this session's write zone is `theprojection-data` +
> `theprojection-site` only** — no editing kestrel or any other repo without
> explicit per-repo permission, prompted by a session that had made five
> kestrel commits (two to engine code) off the back of an unrelated ask.
> `INBOX/` drops stay allowed and need no permission. The rule now lives
> where it's read every session — global `~/.claude/CLAUDE.md`, this
> project's memory (`project_repo_scope.md`), and a warn-only PreToolUse
> hook, all verified firing. **Consequence: `kit.py sync` now reports this
> instance `dirty` on `AGENTS.md` permanently, and that is correct, not
> regressed** — the fix can no longer be back-ported, so a brief was filed to
> kestrel's `INBOX/` instead and the file itself, `README.md`, and every
> in-repo instruction to "edit the canonical copy in kestrel" were rewritten
> to route to a brief rather than a direct edit.
> **Published twice** (Cloudflare `3eaa1ff8`, then `afa9768a` for the SB 903
> correction). Full detail: `log.md`, `coverage-log.md`.

> **2026-08-03 — a second workstream opened: the buildout-research
> skeletons, workshopped in `INBOX/`.** kestrel's engine session dropped a
> q1 decomposition strawman ("what exactly are the hyperscalers spending
> all that money on") 08-02; Ben workshopped it across two ruling rounds
> and the result is **`INBOX/2026-08-02-q1-skeleton-v2.md`** — 15 recorded
> rulings (flow map as primary construction · layers are activities not
> companies · circularity as consolidation adjustment · provenance ≠
> reliability, independent measurement first-class · nothing dark by
> definition · full physical model with terminal-end materiality ·
> living model, delta pass runs on demand · starting points never
> hardcoded, the ⚙ convention). **Blocked on Ben twice:** his edit of the
> red-team brief and his writing of the bar — then it routes to kestrel
> and the adversarial pass runs. **q2 added 08-03** ("Who's buying
> inference? How much? And what are those committed capacity contracts
> worth?") as a sibling skeleton — no new schema, the commitment promoted
> to a first-class object, backlog chain-rule, the order-of-magnitude
> hypothesis pre-registered. ⚠ Numbering note: these research q's are
> kestrel's namespace, NOT this repo's `attention/radar.md` Q1–Q7 —
> radar Q2 ("Where is the money going?") ≈ research **q1**, and research
> q2 is a different question from radar Q2. Don't cross-wire them.
> Also this day: the 08-02 collector-failure record corrected (killed at
> timeout, 15/18 — not "slow"; the world-news rebuild was unaffected).
> ✏️ **Superseded 2026-08-04** — that correction was itself wrong. The runner
> is slow but does not time out; see the 08-04 note at the top.

> **2026-08-03 — `/daily`: the populated week publishes, on a throughline
> of claims arriving ahead of the things that would make them true.**
> Finalized 08-02 (Sunday, recall clean) and wrote the five 08-03 digests.
> **Integrity fix:** the "Woebot Health shutting down" item logged as a
> fresh 07-31 catch was a **15-month-old story** (article 2026-04-25 *of
> 2025*; app retired 2025-06-30) — retracted across the 07-31/08-02 MH
> digests and `coverage-log`, with a standing lesson (confirm a recall
> item's *date* against the window before logging). **Throughline:**
> Monday's risk-on rally (S&P 7,600.50 +1.48%, Dow record) was bought on an
> Iran de-escalation claim Tehran denies while a second LNG tanker burned in
> Hormuz; the harder story moved too — the **EO 14409 framework** got an
> 08-04 meeting date without publishing (both ledger twins re-opened from
> passed-silent to *slipped*, not a silent stand), **Alibaba shipped
> Qwen3.8-Max** head-to-head vs GPT-5.6 Sol, **15 GOP state AGs** turned the
> OpenAI containment breach into a legal matter, and **California's SB 903**
> was **confirmed calendared** for an 08-05 Appropriations hearing
> (dual-verified against raw HTML — the ledger flip the MH lens was holding
> for). Ledger now 50 expectations (added the week-ahead calendar: SpaceX
> 08-04, ISM Services/Cook 08-05, SoftBank 08-06, jobs 08-07, Qwen weights
> ~08-10). **Flash:** one critical entry rides its last day (Iran
> cancellation, lapses 08-04); **no new flash filed** — correct, the day's
> net was de-escalation pricing. `/publish --push` shipped the populated
> week (the publish Ben had been holding for the week-roll).

> **2026-08-02 — the map corrected itself three times, and each correction
> was bigger than the day's news.** A `/daily` clearing a two-day finalize
> backlog (07-31 was overdue; 08-01 had been curated two hours into its own
> digest-day, so 22 of its 24 hours had never been read) turned into an
> audit of our own framing. **① The Iran war began 2026-02-28, not 07-23** —
> a US-Israeli opening strike killed Supreme Leader **Ali Khamenei**, and
> **Mojtaba Khamenei** has led Iran since 03-08. Confirmed by Iran's own
> state media plus Al Jazeera/NBC/Britannica, and found **twice
> independently** by sweeps sharing no sources, which is the only reason it
> was treated as established. Root cause generalises: the thread was split
> from `red-sea-oil-shock` and inherited its origin, but that thread was
> opened off a Brent spike — **a price move's date silently became a war's
> start date**. Any thread split from a capital-lens parent has the same
> exposure. **② The Strait of Hormuz has been shut five months, not one
> week** (transits ~10/day vs a 60-140 norm; Maersk/MSC/CMA CGM/Hapag-Lloyd
> all suspended; war-risk insurance 3-10% of hull value vs ~0.25% pre-war).
> **③ We had never named the Fed chair** — **Kevin Warsh since 2026-05-22**,
> confirmed 54-45, the narrowest ever, with Powell staying on as a governor.
> Every FOMC number we had recorded was right; what they were numbers
> *about* was missing. `kevin-warsh`/`jerome-powell` added by critic
> auto-add. **Ledger:** `eu-ai-act-code-of-practice` → hit but with the
> **claim rewritten** (the Code has bound since 2025-08-02; what activated
> is *enforcement*, €15M/3% fines, plus Article 50) — caught by the entry's
> own `what_confirms`; `anthropic-ipo-filing` → hit, and it was Anthropic's
> own 06-01 announcement covered by six outlets, i.e. **a two-month recall
> gap on our side, not a thin source**. 44 expectations. **Flash:** filed
> the Iran cancellation and **lapsed its predecessor a day early on accuracy
> grounds** — it announced strikes publicly cancelled overnight, and flashes
> render sitewide. **Open, unanswered:** Latin America has no coverage at
> all (Colombia inaugurates 08-07); a M7.1 quake that killed ~36 people
> entered this map three times, every one about whether TSMC's fab was
> running. **Tooling:** `collect.py` killed by timeout, 15/18 collectors
> (3rd straight failure, already in kestrel's INBOX — ✏️ **this diagnosis was
> wrong, superseded 2026-08-04**: the runner is slow, not killed; the real
> failure was GDELT erroring instantly on an unset env var); `render_read.py`
> instructs applying a degradation rule that **exists nowhere** (page ships
> 703 KB over a 600 KB cap); `readouts.py`'s shape spec taught all four
> briefing agents the same wrong `watch` type. Full detail: `log.md`,
> `coverage-log.md`.

> **2026-07-31 (later) — the first `/daily` run in the new repo, plus a
> same-session steering round.** First real content pipeline run since
> the split (below), immediately followed by two of Ben's own reactions
> to it — the loop this repo exists for. **`/daily`:** 18 real collectors
> (incl. GDELT/BigQuery) plus 7 parallel research agents curated all four
> lenses; confirmed Altman's 07-29 Washington briefing (`upcoming.yaml`
> flips to `hit`); corrected `softbank-q1-earnings`'s due date (was wrong
> — 07-30 — not slipped; real date 08-06 per SoftBank's own IR page); a
> new critical flash (`russia-missile-poland-nato-airspace`) for a
> Russian missile crossing NATO airspace, filed as a genuine second
> concurrent flash alongside the still-active Iran one; Anthropic's own
> disclosure that its Claude models breached three companies during
> cybersecurity evals reframed the OpenAI rogue-agent story into an
> industry pattern (`sev=major`, the day's one magnitude flag). **Steering,
> same session:** Ben promoted `russia-ukraine-war` — the map's biggest
> gap, the single largest mechanical world-news signal two days running
> with zero thread coverage — and stated a standing coverage principle
> now in AGENTS.md discipline 13 ("all active military conflicts that are
> not hyper-local get coverage"). A real bug surfaced opening it: a
> cross-reference note naming two countries close together inside a
> thread file tied with the new thread on the world-news
> country-proximity matcher and mis-won on file order — fixed, and the
> lesson (never name two conflicts' combatant countries together inside a
> thread file) is recorded in the affected digest. **Separately, a live
> site bug, fixed and shipped:** the flash rail's dismiss button was
> working exactly as spec'd 2026-07-29 (in-memory-only, reappears on
> reload) — that stopped being tolerable the moment a second concurrent
> flash actually landed. Rewrote dismissal to persist via `localStorage`
> keyed by the flash's own id; confirmed with Ben that the scope
> (per-browser, not a shared/global dismiss — one visitor's click must
> never suppress real news for another) is the intended design, not a
> gap, and recorded that confirmation in-code so it isn't "fixed" wrong
> later. Verified with a real local Hugo build before shipping. Full
> detail: `log.md`.

> **2026-07-31 — extracted from kestrel (phase 6, Ben's call).** This
> repo now holds everything the engine tends for The Projection: the
> attention map, artifacts, sources config, provenance, templates, the
> operating skills, and these docs. The engine (collectors, tools,
> publish core) stays in `/workspace/kestrel`; every engine tool is
> invoked with `KESTREL_INSTANCE=/workspace/theprojection-data` (the
> rule lives in CLAUDE.md). `kestrel.yaml` at the root is the instance
> manifest (`kind: attention`). The migration was gated, not assumed:
> the rendered read page and a full staged publish came out
> byte-identical before and after the move, running the tools with no
> env fails loudly rather than silently reading stale paths, and the
> therapybulletin (then bh-compliance) instance's sweep was unaffected. Receipt links on the
> public site now point into this repo (private — Ben sees them, the
> public 404s; a public receipt export is an open item on the engine's
> ledger). Pre-split history: kestrel's git history, tag
> `pre-engine-split` and earlier. GitHub repo created same day
> (`benthepsychologist/theprojection-data`, private) — auto-init merged,
> extraction history fully pushed.

> **2026-07-30 (evening) — the Global Capital rename had silently orphaned
> its own briefing; fixed, and the freshness gap that caused it closed.**
> Ben noticed two things at once: Global Capital's beat-page briefing had
> "disappeared," and the others still read "Morning briefing" well into
> the afternoon. Root cause of the first: `readouts.py`'s lens constants
> were updated for the rename (per the entry below) but the *stored*
> briefing under the old `lens:money` key never got regenerated under
> `lens:global-capital` — so the beat page looked up a scope that had
> never been written, while the real (stale) content sat orphaned under
> the dead key. Root cause of the second: the readouts pipeline
> (`--scan → --pack-stale → agent → --apply`) had only ever been run by
> hand, so a single morning generation just sat there all day with no
> visible sign of it. Fixed three ways: regenerated all four
> briefing-carrying scopes (front + 3 lenses) fresh via dispatched sonnet
> agents and dropped the orphaned `lens:money` key; folded the same
> pipeline into `/daily` step 6a so it can't go stale mid-day again;
> dropped "Morning" from the label and — reversing the original
> `display:none` design — made the generation timestamp visible
> ("Updated Jul 30, 9:58 PM UTC") so staleness is legible at a glance
> instead of invisible chrome. Verified with a real local Hugo build, not
> just the JSON. One validator caught a real miss along the way: Global
> Capital's first regeneration came back 13/23 bullets linked against a
> 30-source pack, under the `LINK_FLOOR` (60%) — rejected by `--apply`
> automatically, fixed by adding `/threads/<slug>/` links, re-applied
> clean. Full spec: **ROADMAP §Executive readouts**.
>
> **2026-07-30 (later) — the world-news lens gets a real thread, and
> Global Capital ships whole.** Ben, on where a war thread hangs
> structurally: *"I guess it's a lens? ... what do the threads hang off
> of?"* Confirmed: `world-news` is a real fourth lens, but a deliberately
> narrow one (no watchlist sweep, no coverage-critic benchmarks). First
> split: `red-sea-oil-shock` had been doing double duty — split into
> `iran-conflict-widening` (world-news, the conflict itself) and a
> trimmed `red-sea-oil-shock` (money, oil/shipping/underwriting only),
> cross-referenced both ways.
>
> **Then: "build it all."** Global Capital — specced hours earlier as
> Part 2 of `DESIGN.md`, explicitly not built — shipped complete, same
> session. The full rename (`money` → `global-capital`) touched every
> layer: `watchlist.yaml`, 13 threads, `sources/benchmarks.yaml`,
> `readouts.py`'s lens constants, every collector that had hardcoded
> `lens="money"` (`fred.py`, `sec_edgar.py`, `lda.py`/`fec.py`), the site's
> nav + beat page + CSS tokens — with a backward-compat alias so
> pre-rename archive items stay findable. The interpretation shape
> (`{mechanism, confidence, scenarios[], context_note}`) landed with a
> real, tested guardrail in `readouts.py`: above `speculative` confidence,
> at least one scenario needs a genuine precedent or the whole thing is
> rejected — verified against both a passing and a deliberately-broken
> case. Visual identity: Ben said "look at it and make a call" — a muted
> indigo-violet (`#5A4B8C`), distinct from every existing token. The
> receipt page (`/interpretation/<slug>/`) is real, verified with an
> actual local Hugo build, not just component checks — one live
> interpretation (today's GDP/PCE print) on both surfaces. The standing
> `attention/capital-context.yaml` snapshot has 5 real sourced readings;
> its weekly refresh lives in `/week` step 4b; `/steer` can adjust its
> `framing` only, never a reading's value directly. The data stack behind
> it — Treasury TIC, BIS, IMF, EPFR, fund-flow reports — is 5 new
> collectors, independently spot-checked: 4 return real live data
> (Treasury's $9,371.1B foreign-holdings figure, BIS's $45.97T
> cross-border credit figure, both matching each source's own published
> numbers), and the fifth (fund-flow reports) an honest, evidenced empty
> result — both Morningstar and ETF.com bot-wall this environment, logged
> as such rather than faked. **17 collectors total now**, up from 12.
> Full build log: `DESIGN.md` Part 2, `ROADMAP.md` §Global Capital.

> **2026-07-30 — global violence gets its own signal, and money gets a
> reframe.** Ben: *"global violence/military-action is important news
> whenever it happens... I ALSO want its effects on global capital flows
> and risk assessment underwriting."* Split into two tracks:
>
> **World News** (BUILT, same day) — a mechanical, cross-spectrum
> attention signal, deliberately distinct from the editorial flash rail:
> flash is Ben's own "would this lead a front page" judgment; World News
> is a computed fact (N distinct outlets covering a story), never a model
> or a curator. `tools/world_news.py` clusters google_news_rss by shared
> title keywords; `tools/gdelt_dedup.py` deduplicates GDELT's Events table
> (fixing two real noise sources found via live BigQuery testing —
> re-crawl inflation and syndicate-network inflation, ~168 domains
> collapsed into 17 real networks) and tags conflict intensity
> (Goldstein/QuadClass) without using it as a filter. **Wired together
> same day** by `tools/build_world_news.py`: both sources merged, matched
> against `attention/threads.yaml` on two tiers (a country-pair proximity
> check for headlines naming 2+ countries; keyword overlap against a
> thread's title/terms/watch — never its full timeline — for everything
> else), with a hand-curated exclusion list keeping generic vocabulary
> (country names, common AI-infra terms, bare years) from driving false
> matches on shared background words. First real run: **142 items, 54
> confirmed against existing threads, 88 held as candidates**. `/daily`
> now folds `candidate`-status items into the same 1–3 thread-candidate
> slots it already offers, tagged `(world-news, N outlets)`; no new
> persisted state needed — a promoted candidate becomes a real thread the
> normal way, and the next build auto-matches it and drops it from the
> pool on its own. Full writeup: ROADMAP §World News.
>
> **Global Capital** (SPECCED, not built) — Ben's reframe of the finance
> lens from aggregation to interpretation: *"'finance' is boring 'Global
> Capital' is interesting to me."* Confirmed via three decisions: a
> standing macro-context artifact (sibling to `actor-doing.yaml`), a
> pre-generated + cached receipt page per interpretation, and a **full**
> rename (not cosmetic-only) up and down the beat. The interpretation
> shape allows itself to be fuzzy — `{mechanism, confidence, scenarios[],
> context_note}` — and is visually tagged as generated-interpretation,
> distinct from cited fact. Full spec: DESIGN.md Part 2, ROADMAP §Global
> Capital.
>
> **2026-07-29 — the page had no top, and the ranking couldn't see the
> future.** Ben read the read and asked why the week's four biggest
> scheduled events weren't on it. Root cause was a **render bug**: the page
> centered on `digest_day()`, correctly naming 07-29, but 07-29 had no
> digests — so the top throughline strip **rendered nothing**, the `NEW ·`
> badge never fired, and the ranking's `2×today` term was silently zero,
> leaving threads ranked on raw week volume. Fixed (fall back to the newest
> day with content); only reachable since `/daily` was de-scheduled 07-28.
> Three DESIGN gaps behind it are now **specced, not built** (ROADMAP
> §Salience): dated expectations contribute **zero** to rank (the gauntlet
> sat 17th/31st/34th, FOMC below every card on `thread: null`), there is no
> item-level magnitude, and there is no executive summary or flash rail.
> **The spec covers all three plus Ben's new requirement** — an executive
> summary atop every page (front + AI/Finance/MH roll-ups), LLM-written
> now, mechanical over time, and a **flash rail** so general-news events
> ("9/11? front-page") land regardless of lens. Two gaps found while
> speccing: the read page **never renders meta-threads** (`parent` isn't
> exported; theprojection's publisher does export it), and the `NEW` badge
> had been dead. Map: **65 threads** — `china-duv-lithography` (nested
> under `china-stack-independence`, promoted story→**meta**) and
> `datacenters-as-targets` opened by ben-steer; watchlist **+Arm
> +Qualcomm +SMIC +Hua Hong**, closing a recall gap where live weight-2
> threads had no sweep term at all.
>
> **Then it shipped the same day.** Ben decided the three open questions —
> **`critical` only** on the rail, **neutral register**, and **yes the
> flash publishes publicly** (*"this is MY news feed FIRST. If its big
> world news it affects finance so its cohesive"*) — and the whole thing is
> **BUILT** across `render_read.py`, `read-shell.html`,
> `publish_projection.py`, `attention/flash.yaml`, and theprojection's new
> `layouts/partials/flash.html`. Live now: salience scoring with imminence
> + magnitude (the meta `hyperscaler-capex-big-picture` correctly ranks
> **#1** on the day four hyperscalers report; FOMC is hoisted into a
> top-of-page ⏳ Today & tomorrow section instead of sitting below every
> card), a cross-lens **executive summary** (`<date>-front.md`), and a
> **flash rail on every page of the site** — verified in a clean Hugo
> build (homepage, thread pages, map pages). One subtlety found in
> testing and now in both surfaces: **`now` vs `today`** — `today` centers
> the page on the newest *curated* day, `now` is the real digest-day that
> imminence measures from, or an event six hours out reads as "tomorrow."
> **Still unbuilt, named in ROADMAP §6:** meta-thread *card* rendering and
> summary stages 2-3. **`sev=` and `flash.yaml` are now wired into the
> loop** (`842885b`): `/daily`'s curate step marks `sev=` on the
> annotation when an item's magnitude warrants it (default none) and asks
> once whether the day warrants a FLASH, writing `attention/flash.yaml`
> when it does; `/week` prunes expired flashes past their `expires`.
> theprojection is **pushed and live** — `main` in sync with
> `origin/main`, five publish commits landed today (2026-07-29).
>
> **Then Ben read it again and the readouts got built.** His verdict on the
> first executive summary — *"not pretty or well organized. bullet points
> that encourage me to click"* — plus *"an exec readout on literally every
> page"*, a mechanical staleness scan, and a dismissable flash. All BUILT:
> **`tools/readouts.py`** + a `readout.html` partial now put
> **BREAKING · NEWS · SUMMARY** on **167 scopes** (front, threads,
> entities, board nodes) across homepage/thread/entity/map pages.
> *(Coverage is **157** as of the later pass below — 13 empty scopes were
> pruned, 3 lens scopes added.)*
> BREAKING and NEWS are **mechanical** (derived from the dated item
> record, no model, bullets always link); only SUMMARY is model-written,
> by sonnet agents, and **only when a fingerprint over that scope's inputs
> changes** — after the first full generation the scan reports 167/167
> fresh, so a normal day regenerates a handful, not everything. `front`
> **prefers curation** over the model after the first model-written front
> dragged **Brent ~$100.69** (a 07-23 level) into a day whose print was
> ~$87.7; packs now label `watch` as a standing question, not current
> fact. Flash rail gained an **in-memory-only** close button (returns on
> reload, by design). Claim + metric pages excluded deliberately — a
> receipt and a methodology note don't want a news readout.
>
> **Then the paragraph problem got fixed properly, and the beats became
> pages.** Ben: *"I wanted bullets and emojis and delight. It's still just
> a paragraph."* Measured, he was exactly right — **160 summaries, median
> 607 chars, zero newlines, zero bullets**. The fix was the SHAPE, not the
> prompt: `summary` is now **structured slots** (`gist` · `bullets`
> [{emoji,text,url}] · `watch`), enforced by a validator in `--apply`, so
> it cannot drift back to prose. Then, per Ben, a fuller **morning
> briefing** on the front page **and on each beat page** — `gist` · `lead`
> (3-5, ranked by **salience with NO lens quota**) · `sections` (on the
> front, **exactly the three lenses**, so no lens goes dark; on a beat,
> real themes) · `watch`. A fact repeating between `lead` and `sections`
> is deliberate — the lead is the ranking, the sections are the coverage.
> **Beat pages are new** (`/beat/ai/` · `/beat/money/` ·
> `/beat/mental-health/`, now leading the nav): a lens had only ever been
> a client-side filter chip, with no page and no shareable URL. Live —
> **157 scopes**, front briefing 17 bullets, beats 23-25 each.
>
> **Four bugs found in our own code during that pass, all fixed:** ① the
> packability gate used `material()`, which counts items the NEWS window
> never surfaces — 13 scopes were paid for only to answer "nothing is
> recorded for X"; now gated on what the pack will actually contain, and
> `--export` prunes them. ② `_sentence()` tested the literal last
> character, so a sentence ending on a quotation failed — **three agents
> independently mangled good punctuation to satisfy it** before it was
> caught; a validator that makes prose worse is the bug. ③ a **global**
> schema bump marked all 157 scopes stale for a change touching only the
> front and beats — shape versions are now **per-shape**. ④ **the big
> one:** `derive_sections` capped NEWS at 8 items, right for one thread
> and severe for the front, which has 100+ items in the window. The
> briefing was being asked to cover the day while shown an arbitrary 8 of
> it, and the day's leads (Iran, Maine, the DUV tool) were among those
> cut. Packs now get `PACK_LIMITS` (30/60); display caps are unchanged.
>
> **📋 Open for the next `/daily` (Ben's call, 2026-07-29 — "leave it for
> the next daily"):** the sitewide **bullet link rate is 44%** (front
> briefing 82%, beats 75%, entity summaries 29%). Two causes, both
> addressable without new judgment: **209 unlinked bullets across 59
> scopes had no linkable source** — timeline-only scopes, and
> `recent_timeline` carries no url — which the `/threads/<slug>/` fallback
> now in the pack fixes on regeneration (it landed mid-run, so it reached
> the 4 briefings and almost none of the 153 summaries; only **3** bullets
> sitewide use an internal link today). The other **174 are recoverable**:
> a linkable source existed and the bullet did not use it, which wants a
> validator rule requiring a url when the pack offers one — enforced,
> the way shape is, rather than merely requested.

> **2026-07-28 — the full board, the state layer, and real collectors.**
> Row 24's 9-wave rollout took the board to **92 orgs / 53 with axes_num**
> (dep-only audit applied: msft 71 · oracle 48 · google 140; welds:
> xai→spacex, mai→microsoft, deepmind noted; data fixes: Talkspace's
> "Teladoc-owned" gloss was wrong, Replika ~$11M not $70M). Row 23 seated
> the **gov-pool layer** (12 agency nodes US+CA + `canada`; **states/
> agencies go on a SEPARATE map** — Ben: "not competing for the same
> space"; state-axes recipe open in row 24 remainder). Map: **62 threads**
> (payer pair, gov four, W5 money-side, W2 chokepoints). Plate v2 = the
> POWER view (size=gravity, heat=burn thrust÷weight, optionality columns,
> neon rings, pocket filter, /plate/ big page). **Rows 7-8 P1+P2 BUILT:**
> **12 live collectors** (google_news_rss · rss · gdelt · sec_edgar ·
> federal_register · openalex · clinicaltrials · fred + the tier-2 wave
> `dfc881e`: semantic_scholar · github · lda · fec) + runner/probe/
> pdf_text — probe 7/7 UP, first collectors-first /daily ran (764 items
> buffered, 1 agent vs the old 3-4). Keys: ALL landed but LegiScan
> (awaiting reply; opensecrets API dead → FEC replaces it; signups =
> ben@getmensio.com; boilerplate in sources/API-SIGNUP.md). Two runner
> bugs caught by the tier-2 integration pass (.env auto-load was inside
> a docstring — keyed collectors ran keyless; entity starvation → runner
> now stamps watchlist `kind`, lda/fec sweep orgs+people). /daily
> DE-SCHEDULED ("catch up to now") w/ the tiered dispatch plan. Launch
> gate remaining: P3 judgment tools (critic blocked on Ben's mh+money
> benchmark call).
>

> **2026-07-27 — four measured axes, and the board became a chart.** A
> prior-art research pass grounded every axis in an established
> formalization, and the model was corrected to **four measured axes**:
> **commanded_capital** (renamed from `capitalization` — done, schema-wide),
> **thrust** (NEW, promoted: $/yr into new positions ≈ capex−D&A / run-rate /
> net new deployment; buybacks = separate signed channel), **gravity**
> (method un-deferred and re-based **structural/attributable** —
> substitutability × forward-linkage, never gross), **optionality**
> (encumbrance band, measured — **never** thrust÷weight, per Dixit–Pindyck).
> 5 derive-agents pulled sourced figures for **21 pilot actors** →
> `axes_num` on the board. **The site leads with the plate now:** `/map/`
> opens on the POWER view (v2, same day — v1's thrust × gravity was retired
> when gross-AUM dot size misranked the finance actors): optionality
> columns × log-weight, **size = gravity**, **fill = burn (thrust÷weight)
> as heat**, neon sector rings, per-mark receipt w/ net-deployable line;
> thrust rules hardened same day (stakes count; depreciation-only, never
> amortization — the Broadcom artifact); **`/metric/` methodology pages** (7)
> publish each recipe + prior art; claim pages restructured receipt-first.
> Brand corrected in the same push: **light-only restored** (dark-mode
> scaffolding was drift — the identity deliberately doesn't repaint), paper
> scoped to board surfaces, `#E01279` reserved to selection/"new",
> `--infra` → `#808040`, Piazzolla self-hosted. **The loop also turned over
> for real:** first fixed-week `/week` ran (late, wk 07-20 — 3 weekly
> digests, 5-hit/0-silent scorecard, decay review answered), first gap-day
> `/daily` (07-25/26 reconstructed per the new missed-days rule), the
> SpaceX-IPO-date error caught by cross-sweep conflict and primary-verified
> (listed 06-12, not "priced 07-24"), apple-gemini crawled (real gap = the
> 06-09 EU DMA block). Map: **47 threads** (lab-IPO meta + children,
> nvidia-vendor-financing, ai-trade-bear-turn; Jalapeño retired into
> inhouse-silicon). **`attention/backlog.md` created** — the big-player
> build-out map (W1 capex-picture crawls → W6), headline finding:
> the capex leaves are scaffolding (1-3 timeline entries each). Gaps still
> open: `asml` absent; `apple`/`coreweave` unpocketed.
>
> **2026-07-26 — the board became a node + claim graph.** Every actor is now
> a **node** with a `kind` (person · house · corp · state · agency · group)
> and a `level` (L1 = nothing over it · L2+ = has a `parent`), the two
> **orthogonal** (a person can be L1 or L2++). **Group nodes** replace tags:
> **pockets** (`tier: G1` — cohorts of actors) and **sectors** (`tier: G2` —
> cohorts of pockets), joined by `member_of` edges — **7 pockets + 4
> sectors**. **Every metric is now a claim** (`b76257a`, `ec91742`): each
> posture / axis value is a clickable `/claim/<node>--<dimension>/` page
> backed by cited sources, generated into `data/claims.json` (**664 claims,
> 88 of them group aggregates**). Source data lives in **per-node bundles** —
> `artifacts/bundles/<node>-node/provenance.yaml` (posture + capital-as-flow
> in/out/available/operating/deployed + optionality + gravity, each figure
> sourced) — now **72 of them, covering the full board**, superseding the
> 6-actor `-axes/` prototype noted below. The convention (claim = subject ×
> dimension → value + sources; PKG/CAPI shapes, file-based, no DB) and the
> whole pipeline are written up in **[`DESIGN.md`](DESIGN.md)** (new). Board
> counts: **77 orgs · 19 Houses · 11 group nodes**. Published live across
> several 07-26 runs (`provenance/publish-2026-07-26*`). Charter added to
> `CLAUDE.md`: *a metric with no visible source is a bug.*
>
> **2026-07-25 — the rank ladder became axes, and the first 6 are populated.**
> Ben rejected the feudal rank ladder (empire/kingdom/vassal/march) as "the
> wrong axis." Collapsed to just **state + kingdom** (+ **house**;
> `regulator`/`route-layer` stubs) — actors now differ by three **axes** in
> `board.yaml`: **capitalization** ($ commanded), **optionality** (how free that
> capital is), **gravity** ($ economy in orbit). Sovereignty derived + graded,
> not a rung. `liege`→`depends_on` stubbed. Site synced, Hugo build clean.
> **Axis prototype done:** 6 actors populated + cited (Microsoft, Nvidia, OpenAI,
> BlackRock, SpaceXAI, Alibaba) — values on the board, a source appendix per
> actor (`artifacts/bundles/<actor>-axes/`), a finding
> (`artifacts/findings/board-axes-prototype-2026-07-25.md`). The payoff: the axes
> separate what a rung flattens (BlackRock ~$15.3T commanded / ~$1.5B gravity vs
> Nvidia inverse). **Decisions this session (all noted in `board.yaml`):**
> ① `capitalization`→`commanded_capital` **rename pending** (collides with market
> cap; market cap is always a separate label). ② **gravity is NOT deflated for
> now** — the value-added deflators are too fragile; store GROSS, deflate only
> when comparing to nation-states (method preserved in `coverage-log.md` 07-25 +
> bundles). ③ **Spin up ALL major actors next** by pocket — incl. two pockets we
> lack: **insurance** and **health** (see `board.yaml` SPIN-UP SCOPE). Not yet
> published — `/map` doesn't render axes yet.

> **2026-07-24 — the map became a board.** A whole power-structure layer
> shipped: `attention/board.yaml` (56 orgs + 13 Houses in neutral kinds,
> people-as-Houses split from the orgs they hold), projected into a
> **swappable feudal/plain vocabulary** on theprojection's new **`/map/`
> section** (per-actor pages with a standing "what they're doing now"
> synthesis from `attention/actor-doing.yaml`, a "this week" strip, and
> their threads). Threads grew 24→**43** (SpaceXAI ×4, the capex
> **destination tree** `where-the-capex-lands`→compute/power/sites→leaves,
> and **Big Tech into Health**), all crawled. New skills: **`/classify`**
> (board judgment) + **`/steer` board verbs**; thread `genre` backfill;
> all titles renamed short. ⚠ This STATUS + README/ROADMAP need a fuller
> `/docs-sync` pass to fold the board in properly — flagged, not yet done.

## Where things stand

**Repo:** scaffolded and substantially seeded 2026-07-20 (10 commits,
`20f41ca`…`1aec995`). **Done:** attention map seeded (ai + mental-health
copied once; **money lens scoped by Ben** — capital-in-my-markets + macro +
wealth/power, drafted in watchlist + radar Q7); critic **benchmarks set for
all 3 lenses** (`sources/benchmarks.yaml`); **command layer + fixed
templates shipped** (`/daily` `/week` `/steer` `/crawl` `/map` — live in
sessions started from this repo; interim agentic mode until the pipeline
lands); steering loop specified (AGENTS.md). **Daily rhythm live since
2026-07-22** (`/daily` #1: 07-20 finalized with the first coverage pass,
missed 07-21 reconstructed; all briefing-#0 steering asks answered by Ben
same day). **The read is the thread-centric weekly dashboard** (reframe
Phase 0 + thread-first home + weighted ranking, all 2026-07-22 —
`def7c81`…`fc46c6b`): stable artifact URL, rendered by
`tools/render_read.py`. **Delivery: dual** — the page (live) + Drive
comment steering (**decided, NOT built**; ROADMAP §Delivery incl. rung
ladder). **All six `/crawl` backfills ran same day** (findings + bundles +
timeline backstories; two of our own claims corrected in the process —
coverage-log.md). **Not built yet** (rev 07-28): P3 judgment tools
(curate · coverage critic · digest state machine — the launch gate) +
remaining tier-2 keys; Drive comment-delivery HELD. Collectors + feeds:
BUILT (see top note).

**Bootstrap:** seeding phase in progress — see [`BOOTSTRAP.md`](BOOTSTRAP.md)
for per-item state. **Zero bizdev coupling** (Ben, 2026-07-20; scope pinned
in BOOTSTRAP §Scope). Hub tracking: pm repo → project `kestrel` under
`research-and-writing`.

**Deep review ran 2026-07-20** (adversarial pass + reference-implementation
extraction): verdict was *not executable as written* — the judgment layer
(curation rubric, coverage-critic baseline) was a placeholder, zero-dependency
was worded too absolutely, and the GDELT BigQuery backward-crawl path hides
an interactive-auth gate. **All findings applied same day:** BOOTSTRAP
rewritten with done-whens + gates; the reference implementation's conventions
distilled into [`REBUILD-NOTES.md`](REBUILD-NOTES.md) so bizdev never needs
consulting again; runner decided (this container — egress + authctl
verified).

## Open

### Next

1. ✅ **`/daily` #1 ran 2026-07-22** (07-21 was missed → reconstructed;
   07-20 finalized with the first coverage-critic pass, `coverage-log.md`
   created; artifact re-published). **Ben steered same day:** resolved
   `gpt-5.6-release`, promoted all 6 candidates to threads (3 ai, 2 mh,
   1 money); 3 critic-adds (`Databricks`, `Kaiser Permanente`,
   `BlackRock`). Map that day: 16 threads (6 open, 9 developing, 1 resolved) —
   see item 7 below for the same-day-later growth to 21.
2. **Reframe Phase 0 shipped 2026-07-22** (plan approved by Ben same day;
   `~/.claude/plans/cozy-coalescing-kahn.md`): the read is now a rolling
   **Mon–Sun weekly dashboard** built from **threads + entities** —
   16 timeline artifacts (`artifacts/threads/`), entity layer derived from
   the watchlist (slug rules in its header), `attention/upcoming.yaml`
   expectations ledger (9 seeded), `<!-- k: -->` item annotations across
   all 9 digests, one-time page shell (`templates/read-shell.html`) +
   deterministic renderer (`tools/render_read.py`, byte-equivalent
   regeneration verified), all 4 skills + both digest templates + AGENTS
   updated. Page republished to the stable URL (ROADMAP §Delivery, incl.
   the new live-page rung ladder).
3. ✅ **All six `/crawl` backfills ran 2026-07-22** (same session; GDELT+
   API path after WebSearch exhaustion — contention note in coverage-log).
   Ledger now 16 expectations. Next: tomorrow's `/daily` runs the full new
   shape end-to-end (its first expectation flips: Alphabet earnings,
   DeepSeek V4); first fixed-week `/week` Sat 07-25.
4. Finish seeding: `sources/feeds.yaml` copy · keys/`.env` (incl. tier-2
   signups) · SOURCES.md knowledge fold-in (BOOTSTRAP §Seeding).
5. Build collectors fresh, then the judgment-layer tools, then launch
   (BOOTSTRAP §Building — done-whens per item; `tools/render_read.py`
   landed early as the first judgment-free tool). Drive comment-delivery
   builds when Ben calls it (ROADMAP.md §Delivery).
6. Open with Ben: money watchlist entity tuning + the CAPI-style people
   cohort (scope settled) · entity gaps: CXMT (money), Hugging Face (ai).
7. ✅ **Public site scaffolded 2026-07-22, live 2026-07-23**:
   `theprojection.org` ([repo](https://github.com/benthepsychologist/theprojection-site),
   Hugo + Cloudflare Pages, butterfly brand system) plus
   `tools/publish_projection.py` (AGENTS.md discipline 9) and the new
   `/publish` command wrapping it. **Real traffic-ready now:** all 16
   threads publish (default-on, nothing flagged `public: false`);
   `/publish --push` ships content, commits, pushes, and fires the
   Cloudflare deploy hook directly (no confirmation needed on this
   pipeline — Ben, 2026-07-23). Same day: a mobile-usability pass
   (highlights strip + collapsible thread cards — the first live version
   read as "a long page nightmare" on mobile) and a "copy for AI chat"
   button (thread pages + the homepage) so a visitor can paste kestrel's
   tracked read into any AI chat without a login/backend. Also caught and
   fixed same day: `about.md` and the site's own `README.md` both still
   claimed "reviewed by hand before publication" — stale since the
   2026-07-22 default-publish decision; corrected in both places, plus
   two new `about.md` sections ("How it's built" / "How I use it") — the
   latter is first-person and worth Ben's read-through.
   ✅ **Meta-threads shipped same day** (ben-steer — "figure out how to do
   meta-threads"): `kind: meta` + a `parent:` pointer on the child (one
   source of truth, never a `children:` list on the parent). Opened
   `hyperscaler-capex-big-picture` plus `google-capex`/`meta-capex`/
   `aws-capex`/`microsoft-capex` — map now **21 threads** (7 open, 13
   developing, 1 resolved; 1 of the 21 is the meta-thread). Google/Meta
   backfilled from items already curated that week; AWS/Microsoft opened
   quiet, stated plainly.
   ✅ **Two rounds of direct usage feedback on the live site, same day**:
   first the mobile-usability pass above; then, after Ben actually looked
   at it, a second pass — bigger feed-card layout (thumbnail + headline +
   body, not a dense list), real per-article thumbnails (`tools/thumbnails.py`,
   og:image capture with a favicon-tile fallback, cached in `buffer/`,
   backfilled 55/77 of the week's items), and whole-row click-through.
   See `coverage-log.md` and `log.md` for the full arc.

## Keeping this current

Refresh **As of** + the affected section when the repo state moves. The
work-state view for humans lives in the pm hub (`overview/PORTFOLIO.md`);
this file is kestrel-local truth.

## Dated log — belongs in `log.md`

*These sections carry dates, which makes them a chronological log rather
than a snapshot. Per D11 a `STATUS.md` is a snapshot everywhere and the
log lives in `log.md` beside it. They are kept here verbatim and in order
— **this migration does not move them**, because splitting a file in two
is a bigger decision than restructuring one. Moving them is the obvious
next step and is yours to take.*

## 🩺 Predecessor pipeline health check (run 2026-07-20)

The bizdev digest operation is **dormant — 23 days dark**:

| check | result |
| --- | --- |
| Cloud routine `daily-digest` | ☠ **dead** — last push to `origin/main` 2026-06-28; bizdev AGENTS.md ("disabled, egress blocked") is right, bizdev STATUS.md ("runs 07:00 UTC") is stale/wrong |
| Last digests | 2026-06-27 (both lenses) |
| Last feedback pull | 2026-06-26 |
| Last store mutation (`runs.jsonl`) | 2026-06-26 |
| bizdev checkout | sitting on side branch `captures-pending-closeout-2026-06-29` — noted for the record; **not kestrel's problem** under zero-dependency |

**Egress from this container (live pings, 2026-07-20):**

| API | result |
| --- | --- |
| ClinicalTrials.gov v2 | ✅ 200, fast |
| OpenAlex | ✅ 200 |
| Federal Register | ✅ 200 |
| CourtListener (unauth, public endpoint) | ✅ 200 — but the mid-2026 membership gating of real API access is **unverified**; test the search endpoints with the token before Phase 3 |
| GDELT DOC API | 🚧 reachable but slow; 429 on unauth tier — expect rate-limit handling in the collector, consider the BigQuery path for anything heavy |

**Implication:** there is no running daily operation to preserve or
coordinate with — kestrel launches fresh, which is exactly what
zero-dependency wants anyway.

<!-- >>> kestrel: base/status#keeping-it-honest @2026-08-21.4 -->
<!-- ── How to keep this file honest ──────────────────────────────────────
Rules the engine seeds; the content above is entirely this repo's.

1. REWRITE THE TOP NOTE FROM SCRATCH. Never patch a line inside an
   existing note. Read the git log since this file's own "As of" date,
   then write the note fresh. A patched note accumulates half-true
   sentences that each looked fine as an edit.

2. ASSERT NOTHING A COMMAND COMPUTES. Counts, versions, branch state,
   "N unpushed" — run the command now and paste the answer, or do not
   claim it. A number typed from memory is wrong within a day, and it is
   the kind of wrong that gets believed.

3. UPDATE THE "As of" DATE WHENEVER YOU TOUCH THE FILE. `kestrel fleet
   status` compares that date to the newest commit and reports the gap.
   A stale date is not cosmetic — it is the signal that everything below
   it is also stale, and it is the only automated check this file has.

4. DELETING IS PART OF WRITING IT. An entry that is no longer true is
   worse than a missing one, because it reads as current. This file is a
   snapshot, not a log; the log is `git log`.
─────────────────────────────────────────────────────────────────────── -->
<!-- <<< kestrel: base/status#keeping-it-honest -->
