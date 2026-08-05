# STATUS — theprojection-corpus (instance #1; formerly kestrel's in-tree data; formerly named theprojection-data until the 2026-08-05 rename)

*Hand-maintained. **As of 2026-08-05**. Top note covers the repo's
identity rename and the `/daily` catch-up that followed it; the 08-04
(evening) `/week` + board-coverage note, the morning `/daily` note, the
q1/q2 research-workshop note, and the 08-03/08-02 `/daily` notes sit
under it.*

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

## Next

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
