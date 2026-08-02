# coverage-log.md — the coverage critic's running record

*One entry per finalized digest (lens × day), appended by `/daily`'s
finalize step. The recall guarantee: what benchmark sources led with that we
missed, and what the miss changed in the map. Benchmarks per lens in
`sources/benchmarks.yaml`. Created 2026-07-22 (first critic pass).*

---

## 2026-07-22 critic pass — finalized 07-20 and 07-21 (both days' digests; the 07-21 `/daily` was missed and reconstructed)

### ai / 2026-07-20
- **Missed:** Apple's document-preservation letters to 400+ ex-staff at
  OpenAI (TLDR) · Moonshot's HKEX-listing plan (TLDR) · Alibaba
  open-sourcing the Zhenwu chip stack (TLDR) · Databricks' $188B round
  (Neuron) · Musk's 2T-param Grok claim (Neuron).
- **Map effect:** `+ org ai/"Databricks"` (critic-add 07-22). Other misses
  were item-level on entities already listed — sweep recall, not map gaps.
- **Unverifiable:** The Rundown AI 07-20 · AI Daily Brief 07-20.

### ai / 2026-07-21
- **Missed (pre-reconstruction):** Commerce backing off a Chinese-model ban
  (Neuron) · global chip rally (Bloomberg Tech) · Kimi Work agent launch
  (TLDR) · Oklo/X-Energy nuclear-for-AI (Bloomberg Tech) · Hugging Face's
  own breach forensics (Neuron). First two folded into the reconstructed
  digest, flagged as critic catches.
- **Map effect:** none beyond the 07-20 Databricks add — misses were
  item-level or covered by the open `china-stack-independence` /
  `frontier-model-gov-review-precedent` candidates awaiting Ben.
- **Unverifiable:** The Rundown AI 07-21.

### mental-health / 2026-07-20
- **Missed:** BHB's "Quiet Squeeze" addiction-treatment payer-economics
  feature (their lead) · STAT's psychiatric-insurance suicide essay
  (opinion).
- **Map effect:** none — both are theme-level (reimbursement pressure is
  covered by existing terms; the sweep's news-query shape missed feature
  desks. Pipeline note: feature/enterprise pieces don't match event-shaped
  queries).

### mental-health / 2026-07-21
- **Missed:** Kaiser Permanente clinician backlash over AI in BH care
  decisions (BHB's lead) — folded into the reconstructed digest.
- **Map effect:** `+ org mental-health/"Kaiser Permanente"` (critic-add
  07-22). Also offered as thread candidate `kaiser-ai-clinician-backlash`.

### money / 2026-07-20
- **Missed:** BlackRock's $12B+ debt sale financing a Meta data center
  (Bloomberg Tech).
- **Map effect:** `+ org money/"BlackRock"` (critic-add 07-22).
- **Unverifiable:** FT Unhedged (both days — domain unreachable; recurring
  gap, flag if it persists).

### money / 2026-07-21
- **Missed:** Oklo/X-Energy nuclear-for-AI-datacenters (Bloomberg Tech) ·
  Apple/Klarna device leasing (marginal).
- **Map effect:** none applied — nuclear-for-AI is a possible theme add
  (`AI energy buildout`?) left for Ben rather than auto-added; it straddles
  the ai lens's existing `AI data center buildout` theme.
- **Unverifiable:** FT Unhedged.

---

## 2026-07-22 — /crawl frontier-model-gov-review-precedent + steering ledger

- **ben-steer (morning):** resolved `gpt-5.6-release`; promoted 6 threads;
  weight field added to all threads (mechanism approved via question).
- **Crawl incident:** the session's WebSearch budget (200) was exhausted by
  the morning's /daily sweeps + design agents — first news-arc crawl agent
  returned honest-empty. Re-run succeeded via GDELT DOC API + targeted
  fetches (no WebSearch). **Skill note pending Ben's OK:** /crawl could
  pre-flight the remaining search budget / prefer GDELT when exhausted.
- **Crawl output:** finding + bundle + timeline backstory for
  `frontier-model-gov-review-precedent`; EO 14409 identified as the legal
  anchor; `upcoming.yaml` gained `eo14409-deadlines` (due 08-01,
  confirmed, logged_by: crawl); thread watch/notes updated.

### /crawl batch complete (6/6, all threads backfilled same day)

All six promoted threads crawled 2026-07-22: gov-review-precedent ·
containment-breach · china-stack · cxmt-ipo · state-bans · kaiser. Method
note: WebSearch exhausted all day → GDELT DOC API + targeted fetches;
**5 concurrent crawls contended on GDELT's rate limit** (the kaiser agent
never got a query through; others partial) — sequence or stagger future
batch crawls. Corrections to our own record surfaced by crawls:
china-stack (Commerce "pivot" + September talks uncorroborated) and
state-bans (TN unverified, VT unconfirmed, wave undercounted) — all
applied to timelines/ledger. Ledger grew to 16 expectations (6 crawl-logged).

---

## 2026-07-23 — /daily #2: finalized 07-22, ran early (pre-10:00 ET, Ben's call)

Ben asked to run before the usual 10:00 ET checkpoint, expecting a re-run
later; today (07-23) opened `building` on all three lenses with a thin
~06:00 ET read (see today's digests) while 07-22 finalized properly.
Finalize used three parallel subagent sweeps (one per lens) covering the
afternoon/evening of 07-22 plus a coverage-critic pass; ~41 tool calls and
~5–6 min wall-clock per lens.

### ai / 2026-07-22
- **Added:** Alphabet's actual Q2 result (capex guidance $195–205B,
  GOOGL −5% after-hours) · AMD's Advancing AI turned into 3 separate
  multi-GW deals (Anthropic, OpenAI, Meta) · Broadcom/Anthropic's $35B
  Apollo SPV trading · a new Georgia Stargate site · OpenAI's own
  containment-breach postmortem + Washington fallout (Rep. Casar).
- **Correction:** `deepseek-v4-stable` ledger entry was wrong — GA already
  shipped ~07-19; 07-24 was only a legacy-API-name retirement deadline.
  Flipped hit, due date fixed.
- **Map effect:** none (no genuine benchmark misses — The Neuron ran a
  soft feature instead of the day's hard news, the reverse direction).
  **Offered, not applied:** thread candidate for AMD's multi-GW deal day
  (own thread vs. folding into existing capex/circular-financing threads —
  Ben's call).
- **Unverifiable:** none flagged this pass.

### mental-health / 2026-07-22
- **Added:** NUHW's formal DMHC/DOL complaint against Kaiser went public ·
  SF Board hearing recap (Kaiser no-show, mediation agreed) · Mindoula's
  3rd/4th acquisitions (Valera Health, Janus Healthcare Partners) ·
  firsthand's $10M-of-$32M funding restart · a Dec-31 MHPAEA parity-rule
  deadline · an adjacent OpenAI/ChatGPT physical-health chatbot-liability
  suit.
- **Correction:** `hi-sb3001-signature` was already resolved — Green signed
  it 07-14 as Act 248; the ledger had it pending. Flipped hit.
  `ny-s9051b-signature` due date corrected 08-31 (guess) → 12-31 (Hochul's
  actual statutory deadline).
- **Map effect:** none — Kaiser/BHB's full 07-22 slate captured.
  **Cross-outlet miss flagged (not ours):** STAT, Fierce Healthcare, and
  MobiHealthNews all skipped the Kaiser/NUHW story on 07-22; only BHB and
  regional press carried it. Worth a second look if it stays BHB-only.

### money / 2026-07-22
- **Added:** Alphabet's capex raise framed as capital-power/Treasury-yield
  story · CXMT's final allotment (0.47% rate, retail 212×/institutional
  570×, clawback to retail) · digital-health M&A multiple recovery (4.7x,
  "AI as second growth act" for incumbents) · macro strip refresh (hike
  odds ~24%→~30% on an oil spike, not Fed talk; 10-yr 4.64%; Nvidia
  crossed $5T again).
- **Map effect:** none. Money Stuff's 07-22 lead (SEC texting fine) is
  off-lens, correctly not chased.
- **Unverifiable:** Axios Pro Rata and FT Unhedged, both days now —
  recurring gap, flagging per the benchmark file's own note that this is
  expected (partial paywall).

## 2026-07-23 (later) — ben-steer: meta-threads + hyperscaler capex

Ben asked for Google/Meta/AWS/Microsoft capex as their own threads plus a
"Hyperscaler Capex — Big Picture" meta-thread overlapping all four, and to
"figure out how to do meta-threads." Design: `kind: meta` + a `parent:`
pointer on the child (never a `children:` list on the parent — one source
of truth); full field docs added to `threads.yaml`'s header, one-sentence
pointer added to AGENTS.md discipline 7.

- `+ thread ai/hyperscaler-capex-big-picture` (meta, weight 3)
- `+ thread ai/google-capex` (parent: hyperscaler-capex-big-picture) —
  backfilled with the 07-20 $725B-question item and 07-22's Alphabet
  capex raise (both already curated this week, re-tagged, not re-researched)
- `+ thread ai/meta-capex` (parent: hyperscaler-capex-big-picture) —
  backfilled with 07-22's AMD-Meta 6GW deal + the Meta-Anthropic
  cloud-talk rumor
- `+ thread ai/aws-capex`, `+ thread ai/microsoft-capex` (both parent:
  hyperscaler-capex-big-picture) — opened quiet, no evidence yet, stated
  plainly rather than backfilled with a stretch; both hyperscalers report
  earnings within the week (~07-29/07-31)

All five (ben-steer 2026-07-23). Also: dashboard/thread-card UX overhaul
on theprojection.org same session — see log.md for the full list (collapse-
by-default, per-thread summary + headlines, pending collapsed behind a
count, whole-card click-to-expand, per-thread copy, generated thread art,
favicon item thumbnails).

### Steering-adjacent notes
- `/discover`-shaped command discussed with Ben (not built): weekly,
  paired with `/week`, entity/thread-adjacency sweeps with wildcard folded
  into each rather than a standalone axis. Also discussed: a public
  "on the radar" section for theprojection.org surfacing unpromoted
  candidates — read-only confirmed, content shape (raw candidate pitches
  vs. lighter-touch attention signal) still open. Neither built this
  session — design discussion only, logged here for continuity.

## 2026-07-23 (finalized 2026-07-24) — /daily #3

Yesterday's ~06:00 ET early-morning draft ran before the day's real news
had landed; today's finalize sweep replaced it with a full-day pass across
all three lenses. Notably: the money-lens draft had framed the day as
AI-capex anxiety carrying over from Alphabet's earnings — the finalize
sweep found the actual driver was a Red Sea/Iran-Saudi oil shock (Houthi
tanker strikes, Brent +7%) that the early draft missed entirely.

### ai / 2026-07-23
- **Added:** OpenAI's containment breach escalated (Bloomberg: hours not
  weeks; a bipartisan House "AI Kill Switch Act" + audit bill floated) ·
  the White House directly accused Moonshot of distilling Anthropic's
  Fable to build Kimi K3, Bessent named sanctions/Entity List as options ·
  CAISI Director Chris Fall's resignation surfaced · AMD's $5B equity
  stake in Anthropic ("the next circular deal") · Alphabet's full Q2
  detail (stock actually fell >6%, not the ~5% first-read; Cloud +82% to
  $24.8B, $514B backlog; Gemini 3.5 Pro testing, Gemini 4 pretraining
  begun) · OpenAI's "Project Camellia" GA campus named + benefits detail ·
  Amazon's AGI-team layoffs · TSMC's capex raise to $60–64B + $100B more
  Arizona · Claude Opus 5 resolved no-ship.
- **Correction:** none to the ledger this pass (deepseek-v4-stable and
  hi-sb3001-signature were already corrected 07-23 morning).
- **Map effect:** none — all four benchmark outlets (Rundown, TLDR, The
  Neuron, AI Daily Brief) converged on stories we already had covered in
  depth; no entity miss. **Offered, not applied:** thread candidate for
  the Moonshot/Kimi K3 distillation-accusation (distinct shape from the
  broader china-stack-independence story it currently lives inside).
- **Unverifiable:** TLDR AI's archive page didn't expose issue-level
  content via search; The AI Daily Brief's podcast topic detail couldn't
  be extracted from search alone. Both minor, no action needed.

### mental-health / 2026-07-23
- **Added:** a second coverage wave on Kaiser's SF Board hearing (Kaiser
  no-showed; supervisors called it "extremely disrespectful" and
  "infuriating, concerning and unacceptable"; NUHW's "Terrible Three"
  framing crystallized) · Talkspace launched "Tee," a proprietary AI MH
  guide positioned against "mass-market chatbots" · Teladoc unveiled
  "Teladoc One" (always-on AI support, MH therapists on the team) · the
  CMS ACCESS Model's BH track surfaced (~85 of 150+ applicants, five
  watchlist entities at once).
- **Correction:** none this pass.
- **Map effect:** none — only BHB led with MH content (Kaiser, which we
  have deeper); STAT/Fierce(beyond Teladoc One)/MobiHealthNews carried no
  MH-specific lead. **Offered, not applied:** thread candidate for the CMS
  ACCESS Model's BH track.
- **Cross-outlet gap flagged (not ours):** Fierce and MobiHealthNews both
  skipped the Kaiser SF-hearing follow-up that BHB and regional press
  (SFist, KQED, KION) carried.

### money / 2026-07-23
- **Added:** the Red Sea/Iran-Saudi oil shock (Houthi tanker strikes,
  naval blockade declared, Brent +7% to ~$100.69, Goldman flags a path to
  $120+) — the actual driver behind the Magnificent 7's worst day since
  April 2025 ($797B lost), which the early draft had attributed to
  AI-capex anxiety alone · the tech-bond selloff on AI-debt fears
  (hyperscaler bond cover ratios 5x→<2x since Feb; Goldman/JPMorgan
  launched AI-debt trading products; 48% of fund managers name AI capex
  the top systemic-credit risk) · ECB held at 2.25% as expected, Sept
  hike odds jumped to 93% · CXMT's pricing finalized (~$8.6B raised,
  462.85x oversubscribed).
- **Correction:** none to the ledger; the macro strip itself was
  substantially wrong in the early draft (attributed the day to AI-capex
  spillover; the actual proximate driver was the oil shock) — corrected
  in the finalized digest, no ledger entry involved.
- **Map effect:** none — Bloomberg Tech's lead (Mag7 selloff, AI-debt
  fears) is now covered in full. **Offered, not applied:** thread
  candidate for the Red Sea/Iran-Saudi oil-shock escalation.
- **Unverifiable/gaps:** Money Stuff's 07-23 edition could not be
  confirmed via search (only 07-22's surfaced) — a **new** gap, not the
  pre-flagged paywall one, worth a direct check if it matters. Axios Pro
  Rata and FT Unhedged remain the expected, pre-flagged paywall gap.

**Map-wide note:** no critic-adds this pass across any lens — every
benchmark-outlet lead was already covered at parity or deeper by the
finalize sweep. Three candidates offered (one per lens), none yet
answered by Ben. New dated expectations logged to `upcoming.yaml`:
Meta/Microsoft/Amazon Q2 earnings (07-29/07-29/07-31) as the first real
tests of `meta-capex`/`microsoft-capex`/`aws-capex`.

## 2026-07-24 (later) — /classify postures

Grounded the 6 provisional postures set at the board's launch against each
org's open-thread genres (the derivation table in the /classify skill):

- **google, nvidia, openai, anthropic** → `expanding` confirmed. Google/
  Nvidia clear (buildout-race / capital-flow-out). OpenAI: resource-move
  (Jalapeño) + financing (IPO) + coalition (Stargate) dominate; its
  authority-claim threads (Frontier Gatekeeping, Containment Breach) are
  regulatory pressure *on* it, not its own posture. Anthropic: judgment —
  its threads are mostly other actors' dynamics (Microsoft's Hedge is
  MSFT's; Distillation Fight it's the aggrieved party), its own posture is
  the AMD $5B raise + 2GW compute expansion.
- **amazon-aws** → `expanding` applied, **flagged**: buildout-race (the
  $200B capex plan) says expanding, but the same-week AGI-research-role
  cuts are a `consolidating`/`retrenching` counter-signal. Coin-flip;
  first real reading at ~07-31 earnings. Alternative read: consolidating.
- **spacex** → `dormant` (changed from provisional expanding). **No thread
  tags SpaceXAI** — the honest derived posture with zero live threads is
  dormant, and it doubles as a coverage-gap flag: SpaceXAI is very active
  (public since June, Grok 4.5, Colossus) but we track no thread on it.
  Candidate for a thread if it's in-lens; otherwise dormant is correct.

All six now `# classify 2026-07-24`; no rank changes this pass. Republished.

## 2026-07-24 (later) — /steer ask: what SpaceX threads should we track?

Ben: "what SpaceX threads should we be tracking? In our kingdom model, we
want to know what each actor and organization are DOING?" This IS radar Q1
verbatim ("Who are the players, and what are they DOING?"), so folded the
framing into Q1's working notes rather than logging a duplicate question:
the board is now the operational frame for Q1 — each actor's threads answer
"what are they doing," and a dormant board actor is an unanswered Q1. The
SpaceXAI `dormant` posture (from today's /classify pass) is the trigger.
Offered four SpaceXAI thread candidates (Colossus buildout · Grok
trajectory · the $2.1T public entity · an MH/Grok-safety option) — awaiting
Ben's promotion; none created (ask:, not thread:).

## 2026-07-24 (later) — /steer: promote 4 SpaceXAI threads + crawl

Ben promoted all four SpaceXAI candidates offered under radar Q1 — filling
the coverage gap that made SpaceXAI `dormant`:
- `+ thread ai/spacex-colossus` (buildout-race) — the "owns its mines" story
- `+ thread ai/grok-frontier` (buildout-race*) — Grok's frontier trajectory
- `+ thread money/spacexai-public-megacap` (financing) — the ~$2.1T entity
- `+ thread mental-health/grok-companion-harm` (authority-claim) — CONFIRM-
  or-drop: does a real MH/safety Grok story exist?
All four /crawl-launched (4 background agents) for backstory. SpaceXAI's
board posture will lift off `dormant` once last_seen refreshes.
*genre note: a model/capability race has no clean board.yaml genre —
`buildout-race` is a loose fit; flagged to Ben as a possible genre gap.

## 2026-07-24 (later) — SpaceXAI crawl batch (4/4) complete

All four promoted SpaceXAI threads crawled same day (4 parallel agents, no
contention this time). SpaceX lifts off `dormant` → `expanding` (4 threads,
buildout-race dominant). Verdicts + corrections:
- **spacex-colossus** — thesis confirmed; owning the mines became a revenue
  lever (Anthropic rents all of Colossus 1, ~$1.25B/mo). Real constraint is
  power/permits (NAACP/Earthjustice Clean Air suit + DOJ national-security
  shield), not silicon.
- **grok-frontier** — corrected TWO seed facts: Grok 4.5 ranks 4th (not 9th)
  and coding is a strength (not weak); weakness is factuality (~54%
  hallucination). Fast-follower, not mid-pack. $60B Cursor bet.
- **spacexai-public-megacap** — corrected THREE: the public entity is SpaceX
  (SPCX), not "SpaceXAI"; ~$2.1T was the debut (now ~$1.56T, below IPO);
  Starlink (not Starship) funds the AI burn. Verified off SEC EDGAR.
- **grok-companion-harm** — CONFIRMED substantial (was confirm-or-drop);
  kept. Two strands: clinical MH harm (benchmarked worst on suicide/
  psychosis; no filed MH suit yet) + deepfake/CSAM (litigated/regulated);
  shared anti-guardrail root cause.

**Correction propagated:** our "~$2.1T, public ~June" SpaceXAI figure was
wrong across threads + board gloss — fixed to the SEC picture (merger $1.25T
Feb; IPO $135/~$1.75T Jun 12; ~$1.56T now). **Genre gap flagged:** a model/
capability race (grok-frontier) has no clean board.yaml genre — `buildout-race`
is a loose fit; candidate new genre for Ben.

## 2026-07-24 (later) — /steer: "Where the Capex Lands" meta-thread

Ben confirmed both capex cuts are meta-threads (not plain threads) and asked
to build the destination cut. Opened `where-the-capex-lands` (kind: meta) —
the ~$750B question posed as "where does it LAND, on what," sibling to
`hyperscaler-capex-big-picture`'s by-SPENDER cut. They coexist because their
children are disjoint (spender-level vs project-level threads); siblings not
nested (one level of nesting). Reparented the clear destination-projects as
children: `stargate-buildout`, `spacex-colossus`, `openai-custom-silicon`
(Jalapeño). Gaps it exposes = the collection worklist: the chip-spend
itself, power/nuclear-for-AI deals, the specific sites (the "100s of them").

## 2026-07-25 — Framing surgery: feudal rank ladder → axis model (ben-steer)

Ben rejected the empire/kingdom/vassal/march ladder ("wrong axis or defined
poorly; owning the mines is definitionally brittle"). Collapsed the rank
ladder to just **state + kingdom** (+ **house** for people, unchanged);
`regulator` and `route-layer` kept as stubs pending re-home. Actors are now
differentiated by three **axes** (`board.yaml` axes: block): **capitalization**
($ commanded), **optionality** (how free that capital is — 1-b), **gravity**
($ economy in orbit). Sovereignty is DERIVED + GRADED, not a rung. Rank counts
after collapse: state 8, kingdom 39, regulator 8, route-layer 1 (56 orgs, 13
houses). Site brought in sync: `data/labels.yaml` ranks collapsed to the 4
kinds in both projections (kingdom label added — it never existed); publisher
`ALLOWED_ORG_FIELDS` += capitalization/optionality/gravity/depends_on;
`layouts/map/{list,single}.html` rankOrder + the "Dependents" heading + board
foot rewritten off the ladder. Hugo build clean (71 map pages). Staged, NOT
pushed — held for Ben's review of the economics below. `liege`→`depends_on`
rename is a STUB (noted in board.yaml).

**Economics correction (research subagent, value-added basis):** GDP is
value-added — each unit counted ONCE; it does NOT embed a ~7x count (wrong on
both sides of our earlier exchange). Money velocity (~1.3 US M2), not output,
is what turns over. Corporate "ecosystem" figures ($4T Microsoft) are GROSS
partner revenue (~1 tier, double-counts intermediates); the raw $4T-vs-France-
$3T comparison FLATTERS the company ~2x. Normalize gravity to value-added:
state gravity = GDP; company gravity = ecosystem deflated ~0.5 + a multi-homing
haircut. On a like basis France > Microsoft. Rule recorded in board.yaml
axes.gravity.

## 2026-07-25 (later) — Axis prototype: 6 actors populated + cited (ben-steer)

Ben: "populate the axes for 6 actors... dispatching agents for a web crawl for
each... maintaining an appendix of our cited sources for these numbers is hugely
important. In fact, each one is a thread we're tracking right!?" Six WebFetch
crawls (WebSearch exhausted 200/200 — routed around via SEC/IR/press + trackers)
for microsoft, nvidia, openai, blackrock, spacex, alibaba-qwen. Wrote each actor's
capitalization/optionality/gravity + axes_asof to `board.yaml` (+ `axes_asof` added
to the publisher allowlist), a per-actor source appendix
(`artifacts/bundles/<actor>-axes/provenance.yaml` — the durable citation store),
and one consolidated finding (`artifacts/findings/board-axes-prototype-2026-07-25.md`).
Gravity normalized to value-added-dependent annual flow per the 07-25 rule.

The payoff (the axes separate what a rank ladder flattens): BlackRock commands
~$15.3T AUM but gravity ~$1-2B/yr (pure capitalization actor); Nvidia commands
~1/200th but gravity ~$375B/yr dwarfs its capitalization ~4-5x (holds the mines).
Optionality is load-bearing: OpenAI locked (~85-90% earmarked+burning) vs SpaceXAI
free (Musk ~82% vote). Microsoft's "$4T economy" deflates to ~$0.9T/yr VA-dependent;
Alibaba's "$1T GMV" to ~$43B (the gross-vs-VA trap). Also: SpaceX valuation anchor
corrected $1.56T -> $1.52T (07-24). Open: capitalization basis not uniform across
actor types (needs one definition); BlackRock + Alibaba under-threaded (candidate
"power-position" threads); deflators (VA-share/dependency) are judgment, not cited.
NOT yet published — /map templates don't render axes yet, and the basis question is
open. Held for Ben.

## 2026-07-25 (overnight) — Full-board spin-up research: 10 agents, 2 waves (ben-steer)

Ben (going to bed): "dispatch sub agents for all those things... all the actors,
research on each one for our axes... top 10 list of individuals... finance, chips,
hyperscale... health providers... gov funding pockets US and canada. Where's the
MONEY? two or three waves. Go go go!" Dispatched 10 WebFetch agents (WebSearch
exhausted): 7 pockets (hyperscalers, frontier labs, foundries, chips, money,
insurance*, health*) + 3 cross-cutting (top-10 deployable individuals, US gov
funding, Canada gov funding). *insurance + health are NEW pockets — agents proposed
the roster. All returned cited axes (gravity GROSS/undeflated) + candidate threads.

Synthesis: artifacts/findings/board-spinup-research-2026-07-25.md; per-actor detail +
sources: board-spinup-detail-2026-07-25.md. Payoff patterns: optionality carves the
money layer (index giants + insurers constrained; Berkshire/SoftBank/Musk free);
commands-vs-owns signature (Vanguard infinite, owns $0); gravity != capitalization
(Arm tiny-capital/planetary-gravity vs BlackRock/insurers huge-capital/thin-gravity);
infra chokepoints (TSMC, HBM/SK Hynix, Arm, Nvidia); state capital saturates chips.
Headline new thread: payer-ai-claim-denial (MH lens — nH Predict + Cigna PXDX; mirrors
kaiser fight). Boarding HELD for Ben: mostly extend existing orgs (~18 already board
entities) + ~19 new orgs + ~6 new Houses; decisions pending (pocket: field, jp sphere,
insurance/health roster confirm, DeepMind/Arm overlap, payer gravity basis, sovereign
principals as Houses). Research committed + pushed; board.yaml NOT expanded (steering-
loop decision left to Ben).

## 2026-07-25 (later) — "board it": spin-up wave populated onto the board (ben-steer)

Ben: "board it". Populated the researched spin-up wave onto attention/board.yaml
via a boarding agent (validated). +21 new orgs, +6 new Houses → 77 orgs (8 state /
60 kingdom / 8 regulator / 1 route-layer) + 19 Houses. 45 orgs now carry the axes
(commanded-capital/optionality/gravity, GROSS gravity) + a new `pocket:` field; 10
Houses carry `deployable` (the top-10 personal-deployable-capital list). Pockets:
hyperscaler 5 · frontier-lab 7 · chips 8 · foundry 4 · capital 7 · insurance 7 ·
health 7. Schema adds: `pocket` + `deployable` on the publisher allowlist; `jp`
sphere + a `pockets` enum. Wiring: softbank held_by masayoshi-son; deepmind + arm
depends_on their parents (Alphabet/SoftBank — don't double-count capital). New
pockets insurance + health are NEW to the board (money + MH lens). All provenance
`# spin-up-board 2026-07-25`; detail + sources in
artifacts/findings/board-spinup-{research,detail}-2026-07-25.md.

HELD (not boarded): gov-funding pockets (US/Canada — a state-capital layer needing
its own representation call) + the evidence-gap evaluators/enforcers/methodologists
(Plan 1 — needs its extraction pass; source moved to the-evidence-gap-src project).

## 2026-07-26 — Node model: kind/level + group nodes (ben-steer)

Reframed the board as a node+edge graph (Ben's nodal pivot). Every node now has
kind (person/house/corp/state/agency/group) + level (L1 = nothing over it, L2+ =
has a parent) — ORTHOGONAL (a person can be L1 or L2++; a corp can be a L2
subsidiary). Added a `groups:` block: 7 pocket nodes (G1) + 4 sector nodes (G2,
finance/power/infra/care) connected by messy many-to-many `member_of` edges
(Finance ⊃ capital+insurance, but hyperscalers are not) — groups are a graph, not
a tree; actors mostly a clean containment tree. kind/level DERIVED as a seed in
the publisher (from rank/parent), overridable per-node; regulators → agency @ L2
with parent seeded from sphere→State. Set explicit parent on the 3 clear corp
subsidiaries (deepmind→google, arm→softbank, microsoft-mai→microsoft). Publisher
allowlists kind/level/parent + emits `groups` into board.json. Result: 8 state /
61 corp / 8 agency / 19 person; 66 L1 / 11 L2; 11 group nodes. Known rough edge:
silk-road (route-layer stub) still seeds as corp — pending retirement. board.json
= the node map now; pocket PAGES + the /map overview + news render off it next.

## 2026-07-27

- **Model change (event): four measured axes.** Prior-art research pass (Ben-supplied brief) grounded each axis in an established formalization. `capitalization`→`commanded_capital` renamed schema-wide (done). **Thrust promoted** to a first-class axis ($/yr into NEW positions — Damodaran reinvestment rate, extended; buybacks a separate signed channel). **Gravity method un-deferred**: superseded "store gross, deflate later" with a structural/attributable method (G-SIB substitutability × forward-linkage) — the earlier value-added-deflator concern is resolved by not deflating a dollar figure at all. **Optionality confirmed measured band** (free/mixed/constrained/locked), never derived as thrust÷weight (Dixit–Pindyck category error — written into the board.yaml axes block as a guardrail). `axes_num` numerics added for 21 pilot actors (5 derive-agents, sourced; ⟨agent-derive 2026-07-27⟩). Site: /map/ now opens on the plate (thrust × gravity chart); /metric/ methodology pages publish the recipes. kestrel `f04a93e`, site `3c06744`.
- **Gaps flagged, not filled:** `asml` absent from the board (sole EUV supplier — high-gravity omission); `apple` + `coreweave` unpocketed. Six optionality conflicts between pilot estimates and existing steering resolved in steering's favor (openai stays locked, arm constrained, microsoft mixed, etc.).

## 2026-07-27 (the /week pass — week of 07-20, run late Monday)

- **First fixed-week `/week` ran** (late — ROADMAP row 6 finally closes). Three weekly digests written against the radar Qs; scorecard: **5 hits, 0 slipped, 0 passed-silent** (alphabet-q2, deepseek-v4, hi-sb3001 + week-sweep catches cxmt-star-listing 466% debut, claude-opus-5 shipped 07-24, kimi-k3 shipped 07-26 a day EARLY). 3 pre-week hits pruned after recording. 3 new expectations logged (grok-4.6/4.7, anthropic-ipo-filing thin).
- **The structural finding: the weekend gap.** The week's four biggest items (Nvidia $250-500B OpenAI guarantee, SpaceX ~$2T IPO, Opus 5, Kimi K3) ALL broke Fri-night→Sun with no daily running — both money and frontier sweeps hit the same wall. **Fix candidate offered to Ben: a Sunday-evening mini-sweep.**
- **Named-thread blind spot:** `apple-gemini-model-deal` had zero coverage across 5 dailies while real news existed (Siri-Gemini cloud extension ~07-21/22) — worse than a benchmark miss; `/crawl` proposed. Also: 07-23 daily asserted "Opus 5 did not ship" and was wrong within 24h — negatives on release-watch items should be timestamped ("not as of sweep").
- **In-window misses:** AMD–Anthropic $5B (07-22, money) · BIS bubble warning (thin, needs primary) · Stanford HAI governance convening + OpenAI Foundation/Child Mind funding (07-24, MH — budget-blocked daily, backfilled by sweep).
- **Unconfirmed quiet** (empty RSS ≠ silence): grok-companion-harm news, FDA/FTC, CMS ACCESS, PHTI/ICER, Slingshot/Woebot/Wysa — re-check when search budget resets.
- **Map effects (decay-review 2026-07-27):** `cxmt-memory-ipo` entities `[]→[cxmt]` (stale "not on watchlist" note) · `ai-memory-shortage` +cxmt · actor-doing full pass (9 movers re-written, asof 07-27) · radar Q3-Q7 working notes opened. **Proposals to Ben (not applied):** retire `openai-custom-silicon` into `inhouse-silicon` · keep+crawl `apple-gemini-model-deal` · thread candidate `anthropic-ipo-timing` · watchlist adds sk-hynix/micron · TCAI state-law-count reconcile crawl.
- **Steering applied (ben-steer 2026-07-27, answers to the /week read):** ① `openai-custom-silicon` → retired, folded into `inhouse-silicon` (+openai/+broadcom entities; closing timeline entry). ② `apple-gemini-model-deal` kept + `/crawl` dispatched. ③ New meta `frontier-lab-ipos` ("Lab IPO Wave") w/ children `openai-ipo-timing`, `spacexai-public-megacap`, NEW `anthropic-ipo-timing`; `anthropic-ipo-filing` expectation re-pointed to it. ④ Standing rule into /daily skill + AGENTS: reconstruct EVERY missed day since last run ("a week shouldn't be worse because a Thursday or Friday run didn't happen"); Sunday mini-sweep sanctioned. ⑤ sk-hynix/micron: already watchlisted 07-24 (weekly flag was wrong) — entity tags wired onto `ai-memory-shortage`. Thread count 43→45; `retired` added to the status enum.
- **Correction (2026-07-27, cross-sweep conflict → primary-source verify):** the /week frontier sweep reported "SpaceX priced its IPO 07-24 (~$1.75-2T, +19% day one)" — WRONG. Verified (Wikipedia, quoting the filing dates): **priced 2026-06-11 at $135/sh, $1.77T valuation (largest IPO ever), $75B raised, trading since 06-12 as Nasdaq:SPCX.** The sweep misread six-week-old listing facts resurfacing in trading commentary as fresh pricing news. The PRICE claims were right all along (Fri close $115.07 = −14.8% vs issue ≈ the reported "13-16% below issue"). Corrected in: both timelines, 4 daily digests, the frontier weekly, threads.yaml watch, actor-doing. Caught because the money today-sweep contradicted it — cross-sweep conflict detection works; lesson: date-of-event claims from aggregation feeds need a primary check before entering timelines.
- **Crawl landed (apple-gemini-model-deal, 2026-07-27):** the 07-21/22 "Siri-Gemini cloud extension" that drove the keep+crawl verdict was a FALSE POSITIVE — a stale MSN re-index of a 2026-03-02 story. The real find: the dark month's actual story was the **EU blocking Siri-AI at launch (06-09, DMA, ~450M iPhones — 5+ outlets)**, plus the WWDC ship (06-08, Apple newsroom) and Google's official joint statement (01-12) — all pre-dating kestrel's seeding, now backfilled (finding + 14-source bundle + 6 timeline entries). The ~$1B/yr figure remains unconfirmed by either party. Weekly near-miss audit corrected accordingly. Lesson reinforced: aggregation re-indexes masquerade as fresh news — same failure family as the SpaceX misdate, caught the same day.
- **Steering (ben-steer 2026-07-27, /daily candidates answered):** ① NEW `nvidia-vendor-financing` ("Nvidia as Lender", w3, money) — spun out of ai-circular-financing-risk; guarantee + stake-ladder backstory seeded. ② `micron` tagged onto `cxmt-memory-ipo` (−8% read-through). ③ NEW `ai-trade-bear-turn` ("AI Bear Turn", w2, money) — Ben: the index direction is NOT circular-financing, "it's its own thing"; tracks the market's aggregate verdict. Threads 45→47.
- **Build-out map created (ben-steer 2026-07-27: "map out all the stuff that needs to be crawled and built out"):** full local audit of threads × timeline-depth × actor-doing × axes → `attention/backlog.md`. Headline finding: the capex tree is scaffolding — microsoft-capex has 1 timeline entry, aws-capex 1, meta-capex 2, google-capex 3, destination leaves 1 each ("what are they DOING with the capex" is genuinely untracked). Zero-thread chokepoints: TSMC, Arm, Intel, CoreWeave, Qualcomm, BlackRock, Vanguard. Tagging bug: xai untagged on all grok/colossus threads. 14 majors missing actor-doing entries. Six workstreams W1–W6, sequenced.
- **W3 applied (ben-steer 2026-07-27, backlog):** ① `xai` tagged onto grok-frontier / grok-companion-harm / spacex-colossus (node page un-emptied). ② Sub-entity slugs (microsoft-nuance, verily, apple-health, amazon-health) dropped to parent-only tags per watchlist discipline. ③ **ASML boarded** (chips pocket, sphere eu, axes_num {60, 2, 1500}, free) + watchlisted — the biggest absent node closed; -node bundle rides the axes_num rollout (row 24). ④ apple + coreweave pocketed `hyperscaler` (Big Tech placement / neocloud). Board 77→78 orgs. W1 capex crawls fired same session.
- **W1 COMPLETE (crawl 2026-07-27): the capex picture, un-blurred.** Four parallel destination crawls (Google 54 / Microsoft 30 / AWS 28 / Meta 55 sources) + the synthesis table into `hyperscaler-capex-big-picture`. Cross-cutting: ① the own-silicon vs Nvidia split is undisclosed at ALL FOUR (the labs leak what the hyperscalers won't — Anthropic on 1M TPUs AND 1M Trainium); ② payoff layer weakest (press-only backlogs; the $250B OpenAI→capex mapping doesn't exist publicly); ③ power solved three ways (nuclear '27→'39; Meta broke the clean consensus — RE100 exit, 7.5GW gas); ④ capex migrating off balance sheets (Meta→Blue Owl 80%, bonds, leases). Corrections landed: Amazon earnings 07-31→07-30; Amazon-OpenAI $50B+$100B/8yr CONFIRMED (was "thin" all week); Meta capex-figure discrepancy flagged ($76B TTM basis vs recurring $135-145B guidance — resolve Wed); MSFT "$97B TTM" exposed as our own arithmetic. Candidate surfaced for Ben: Meta's RE100-exit/gas-pivot as its own thread.

## 2026-07-28

- **W2 COMPLETE (crawl 2026-07-28): the zero-thread chokepoints are gone.** Four backstory crawls (TSMC 50 / Arm 38 / Intel 33 / CoreWeave 51 sources) + `meta-gas-pivot` threaded (ben-steer). Threads 47→52; actor-doing +4 (tsmc/arm/intel/coreweave — W4 riding). Headlines: TSMC pricing like a monopolist (2027: +5-10% base, ≤25% AI surcharge) with CoWoS as the true bottleneck; Arm ended pure-rentier status (first in-house chip in 35yrs) while Qualcomm funds RISC-V in the open; Intel's "golden share" is really a foundry-breakup poison-pill warrant, $10.9B outside equity in the same window as 24k cuts; CoreWeave's customers anonymized to "A-D" (disclosure retreat) at 9.75% GPU-collateralized money. Ledger +2 (arm earnings 07-29, coreweave 08-11 — Wednesday now carries FOUR events). Flags for Ben: intel commanded_capital cost-vs-mark (~$8.9B vs ~$42B — cost recommended); TSMC's ~90% advanced-node anchor carried, not re-verified; broadcom merge-vs-new still open.
- **W5 + W4-writable-now (ben-steer "continue", 2026-07-28):** `asset-managers-build-ai` opened (BlackRock GIP/$40B Aligned + $12.5B El Paso bond + KKR Helix — one cohort thread) · `softbank-all-in` opened (the concentration itself: $40B loan + Stargate + Arm-as-collateral + Intel — pieces lived in 4 threads, nothing tracked the correlation) · memory-trio judged: widened ai-memory-shortage into the capacity-race ledger instead of fragmenting · actor-doing +3 (softbank, cxmt, blackrock). Threads 52→54; actor-doing 22→25. Remaining W4 rides future crawls (xai, broadcom, samsung, sk-hynix, micron, vanguard, qualcomm).
- **W6 shipped (2026-07-28):** node pages rework (live threads sorted by timeline DEPTH w/ entry counts, meta ◉ marks, parent tags; resolved/retired collapse into "Concluded") · publisher exports `depth` per thread (deepest: google-capex 19) · the reach=spend DIAGONAL re-homed onto ai-circular-financing-risk + nvidia-vendor-financing thread pages (self-contained embed, correctly scoped — 0 leakage to other threads) · `retired` enum comment fixed to match publish reality (archive pages stay, sweeps/live-lists drop). Remaining in W6: dep-only thrust recompute (rides rollout). W4 crawls in flight (vanguard landed).
- **xAI classified (ben-steer 2026-07-28):** L2 subnode under `spacex` — the deepmind@google pattern. Identity (Grok/Colossus, cloud + frontier model) stays a distinct node for threads/entities; **the money is welded to SpaceX** — no separate axes, all capital/thrust/gravity calculations consolidate at the parent (xai board entry: `commanded_capital: CONSOLIDATED`). Grounds: reported legal dissolution into SpaceXAI 07-06 (secondary press; no primary filing found — flagged). actor-doing entry written (exodus corroborated: all 11 co-founders gone). Board 78→79 orgs.
- **Two threads opened (ben-steer 2026-07-28: "yes, open both"):** `custom-asic-tolls` ("ASIC Tolls", capital-flow — the crawl's merge-vs-new recommendation confirmed; five-customer book + the litigated VMware toll; the counter-case to inhouse-silicon) · `qualcomm-dragonfly` ("Dragonfly Return", border-war — the Centriq-redux datacenter re-entry, Meta/Microsoft launch customers, anti-CUDA Modular buy). Threads 54→56; actor-doing +2 (broadcom, qualcomm — 28 total); ledger +1 (qualcomm earnings 07-29 — Wednesday is now SIX events: Meta, Microsoft, FOMC, Arm, Qualcomm, + the CA SB903 deadline Friday-adjacent). W4 remaining: memory trio (crawl in flight).
- **W4 COMPLETE (memory-trio crawl landed, 2026-07-28):** actor-doing 28→31 (samsung, sk-hynix, micron — ALL 14 W4 gaps now filled). The crawl caught a live shock mid-flight: **"Black Tuesday" — SK Hynix −14.65%, KOSPI −10.84% (07-28), explicitly CXMT-triggered** — the first sharp market repricing of CXMT as a real threat; entries pushed to cxmt-memory-ipo + ai-trade-bear-turn (the turn now has US and Asia legs in one week). Trio facts: the "3-year HBM deficit" originates from SK Hynix's own Q1 CFO guidance; Samsung projected to take its first-ever HBM lead in 2027 (UBS) while still unqualified for HBM4 volume; Micron immune-by-exit (left China servers 2023). Ledger 24→26 (sk-hynix 07-29, samsung breakdown 07-30) — **Wednesday now carries SEVEN dated events.** Backlog: W1-W6 all complete; standing riders only (axes_num rollout + dep-only recompute; Intel commanded_capital call parked with Ben).
- **Row 24 ramp fired (ben-steer 2026-07-28: "spawn some SUBSSS. WAAAVES!"):** 9 waves in flight — A frontier/China labs (5) · B spacex+tesla (consolidated SpaceXAI per the weld) · C memory+chips (5) · D capital pools (4) · E insurers (5) · F US health payers (7, axes) · G digital-MH smalls (8) · H dep-only pilot audit · **I health-payer NARRATIVES (Ben mid-ramp: "basically nothing in the health layer")**. Sequence locked: 24 → 23 → camellia → Intel call → rows 7-8; Drive rows HELD; row 22 individuals DEFERRED (CAPI rework elsewhere). Welds applied: microsoft-mai → microsoft (deepmind's older don't-double-count line already equivalent); nuhw = labor org, axes N/A. Fixed: coreweave's gloss (an earlier inline comment-edit had silently swallowed it — caught on re-read).
- **Bug fixed (Ben, 2026-07-28): dead internal-path links on claim pages.** Judgment claims (postures esp.) cite internal repo paths as sources (`attention/board.yaml`); the publisher passed them verbatim → relative hrefs → 404 under /claim/<id>/ (172 instances, 12 distinct paths). Fix in `_mk_source`: non-http urls rewrite to GitHub blob links (kestrel is public) — the receipt stays CLICKABLE instead of dead. 0 non-http urls remain in claims.json; verified on google--posture.
- **ROW 24 ASSEMBLY (2026-07-28): the board went fully numeric.** 9 waves assembled — **53 orgs now carry axes_num** (was 22): +labs (deepseek thrust ≈0, its infra round PAUSED; alibaba-qwen ~$11B/yr), +musk pair (spacex consolidated {102,14.1,85}; tesla first axes, optionality MIXED — 13%, no supervoting), +memory/chips (micron 16.2 leads the trio; globalfoundries genuinely negative like Intel), +pools (softbank $30B-own-money correction; berkshire net-selling 15 quarters; PIF weight →$1.21T), +insurers (5, china-life pattern), +health (7 payers — gravity dwarfs thrust; elevance artifact-suppressed; kaiser KPMG-audited weight; HCA mixed w/ two-axis note), +MH smalls (8, honest sub-$1B; talkspace 'Teladoc-owned' gloss was WRONG → UHS-pending; replika ~$11M not $70M). Dep-only audit applied (msft 71, oracle 48, google 140/Wiz $29.5B). actor-doing 31→38 (7 payers, wave I). Ledger 26→27 (MHPAEA replacement-rule, correctly logged as a PROPOSED-RULE timeline — no compliance deadline exists). Thread candidates for Ben: payer-ai-claim-denial · mhpaea-parity-limbo. Wednesday: seven events. Next per sequence: row 23 (gov pockets) + plate UX asks.
- **Steering (ben-steer 2026-07-28): both payer threads opened + Intel settled.** `payer-ai-claim-denial` ("AI Denial Machine", legitimacy-dispute, w2 — UHC discovery order + WISeR fight + MN ban + OIG + the ghost-network strand) · `mhpaea-parity-limbo` ("Parity Limbo", authority-claim — the vacuum, not a countdown; ledger entry re-pointed). Threads 56→58. **Intel commanded_capital: COST over mark confirmed** (~$8.9B, not ~$42B — "commanded ≠ market gains") recorded on the entry. camellia mini-crawl dispatched (last item before rows 7-8).
- **camellia crawled (2026-07-28, mini):** 0-entry no more — Rincon/Effingham GA pinned (Savannah Gateway Industrial Hub), 3.2GW/25yr Georgia Power PPA (generation mix BLANK in the DRI), OpenAI-DIRECT build (no Stargate-JV overlap; Octans GA LLC), $20-30B unreconciled, secrecy-driven backlash (10K+ petition), DRI→Coastal Regional Commission gate pending. KEPT STANDALONE per crawl evidence (live regulatory + local-politics arc the site-map format would flatten). Sequence state: 24 ✅ corps · camellia ✅ · Intel ✅ · row 23 half-in (Canada landed, US pending) → rows 7-8 next.
- **/daily de-scheduled (ben-steer 2026-07-28):** "run any time — /daily just updates us to current." The 10am-ET run-gate is gone; it survives only as a per-day finalize condition (a day flips final/coverage:done once its benchmarks are checkable, ~5h past its 5am-ET close — otherwise it stays building/pending for the next run). The 5am boundary stays as bucketing. Pushback offered and scoped: recall preserved, operator ungated.
- **/daily dispatch plan (ben-steer 2026-07-28: "strategize the best way"):** tiered parallel dispatch written into the skill — T1 lens sweeps (3-4 agents, RSS-first) · T2 hot-cluster deep checks (2-4 agents, grouped by meta-parent/entity family; due-today + w3 + moved-48h; WebSearch budget reserved here) · T3 cold rotation (1 agent, 7-day cycle, /week audits misses). Rules codified: primary-check before timeline dates; disjoint write scopes (attention/*.yaml main-session-only); T1/T2 overlap kept as the error detector. ~6-9 agents/run, scales by cluster count not thread count.
- **ROW 23 APPLIED (ben-steer 2026-07-28):** `gov-pool` G1 pocket (under finance) + 12 agency nodes (7 US, 5 CA) + `canada` state node + sphere `ca` (board 79→92 orgs; publisher SPHERE_STATE +ca). Threads 58→62: genesis-mission · chips-equity-pivot ("CHIPS Equity Pivot") · dod-ai-consolidation ("DAWG Rising" — $226M→$54.6B request via reconciliation) · **canada-ai-vs-care w3** (the $925.6M-vs-zero divergence + the 2027 bilateral cliff). Ledger +1 (FY2027 appropriations 09-30). **Ben's map ruling: states/agencies get a SEPARATE MAP** — corp plate now excludes kind state/agency (both templates); the state-axes recipe question (same axes or different?) folded into row 24 remainder, thinking delivered in-session. Rows 7-8 next: collectors proposal delivered.
- **ROWS 7-8 P1+P2 BUILT (2026-07-28, 5-agent wave):** collectors/ is real — 7 live modules (google_news_rss · rss · gdelt · sec_edgar · federal_register · openalex · clinicaltrials), all stdlib, all live-proven in-build; tools/collect.py runner + probe + pdf_text; registry auto-imports (the wiring gap 3 agents flagged, fixed). feeds.yaml built FRESH (finding: /workspace/bizdev does not exist — the seed source is gone; 28 live feeds, GET-probed, Cloudflare liars caught). CourtListener flipped at-risk→wired-targeted (evidence: not membership-gated; quota is the constraint — 5/min anon). /daily tier-1 is now COLLECTORS-FIRST (agents drop to 1-2 gap-fillers + tier-2 depth). Remaining: tier-2 keys (Ben signups), P3 judgment tools (critic blocked on Ben's mh+money benchmark sets). First buffer already caught the tape: "OpenAI Close to Landing $500B Data Center With Nvidia's Backing" (NYT), the Seoul selloff coverage, "$5bn into SSI" — before any agent asked.
- **First collectors-first /daily (2026-07-28 morning):** 764 items buffered (rss) in one deterministic pass; ONE tier-2 agent (vs the old 3-4 sweeps). Wins logged: the primary-check rule killed a content-farm rumor cold ("SpaceX buys Cursor $60B" — June blog recycled; zero tier-1); guarantee tightened to $250B (the $500B headline didn't verify); Microsoft earnings corrected 07-29→07-30; SB903's "due Friday" softened (hearing unconfirmed). 07-27 digests correctly held at building (closed <5h ago — the finalize-eligibility rule's first live firing). Runner gap: needs --max-terms for interactive runs (google-news full-term pass too slow foreground).
- **Keys wave (ben, 2026-07-28): FRED + DATA.gov landed + validated live** (FRED: Fed Funds 3.63 flowing; DATA.gov: proven vs GovInfo, covers that slot too). `collectors/fred.py` BUILT + live (30 obs — the money-lens instrument panel: policy rate, curve, HY/IG OAS credit spreads = the bear-turn's dials, VIX, CPI, UNRATE). Signup email standardized: ben@getmensio.com (mailto + declared UAs swapped). sources.yaml now documents ALL live collectors + key family statuses — the single source map, honest per entry. Remaining slots: LegiScan (med-high — the state-ban wave), Congress.gov, CourtListener token, Semantic Scholar, GitHub, LDA, OpenSecrets.
- **07-27 finalized (critic run 07-28, agent-gathered evidence + main-session judgment):** AI — 2 real misses folded (⟨critic⟩ marks): China's "all necessary measures" sanctions response (Bloomberg 07-27 → kimi-distillation-fight timeline) + MAI-Cyber-1-Flash/Project Perception (TechCrunch 07-27 → microsoft-mai-openai-decoupling timeline). 4 benchmark "leads" ruled out on event-date (3-6-day rehashes: OpenAI/HF breach, Prentis, Anduril, FLUX 3) — the date-check rule again did the heavy lifting. Money — 0 confirmed; Pro Rata + Unhedged UNREACHABLE, logged unverified not clean. MH — clean on the AI-mh beat, kestrel ran AHEAD of all four trade benchmarks (liability research, state-AG mechanism, embolism suit, NCOSE); BHB out-of-beat items (autism consortium, SAMHSA survey) noted without map action. No critic-adds this pass — no repeated-miss pattern; both AI misses route to threads we already hold.

## 2026-07-29 (05:00 ET) — the 07-28 overnight extension (no critic pass; day not yet finalizable)

**Run shape.** Ran at 04:55→05:05 ET, i.e. across the 5am digest-day
boundary. The open day was still **07-28**; it closed at 05:00 and is
finalizable from ~10:00 ET, so all three lenses stay `building` /
`coverage: pending`. **No missed days** — 07-26 and 07-27 were already
`final`/`done`. 07-29 was NOT opened: the day had ~0 minutes of elapsed
news and its whole content (FOMC + three prints) lands after 14:00 ET.
Collectors ran `--since 07-28T19:00Z`; 3 tier-2 cluster agents + 1 cold
rotation carried the signal, since an overnight window is thin for
broad sweeps.

### Data-integrity catches (3)

- **⚠ NVDA date error, in our own 07-28 digests — corrected.** Both the AI
  and money digests headlined "NVDA −5%" as a 07-28 event. Price history is
  unambiguous: **07-27 closed $196.51, −4.99%; 07-28 closed $197.01,
  +0.25%** (intraday low $192.74 ≈ −1.9%). Caught by cross-sweep
  contradiction — one agent reconciled the −5% to 07-27 by closing-price
  math, another independently reported "Nvidia −2%" at 3:59pm ET on 07-28.
  Both were partly right; the arithmetic settled it (a −5% intraday move on
  07-28 was impossible given a $192.74 low against a $196.51 prior close).
  Verified against stockanalysis.com. **The correction improves the
  thread**: the story is a credit/equity *divergence* (CDS wide, equity
  flat) rather than a synchronized break. Applied to both digests +
  `nvidia-vendor-financing` + `ai-trade-bear-turn`.
- **⚠ SK Hynix capex claim — flagged, not adopted.** Secondary press
  (DigiTimes) reported capex raised to the ~40T-won high end (~45T/$31B).
  The primary release says "capital expenditure discipline," phased "based
  on customer demand." Primary and secondary disagree in *direction*.
  Recorded as unconfirmed pending Samsung's 07-30 breakdown — the
  discipline the SpaceX misdate taught, applied to a figure rather than a
  date.
- **⚠ CXMT probe framing — the same conflation, one day later.** The
  "CXMT debut triggered a Capitol Hill probe" framing this log killed on
  07-28 (the Moolenaar/Whitesides letter is dated 07-16 and never mentions
  the IPO) reappeared in the coverage of a *new* prospective bipartisan
  letter effort. Logged `rumored` with an explicit confirmation test: a
  letter with signatories, not another restatement of the first.

### Recall gaps found (2) — both real map holes, not sweep noise

- **Maine LD 2082 was absent from the map entirely.** Enacted as Public Law
  Chapter 687 on **04-13-2026**, it took effect **07-29** — the first US
  statute barring AI-delivered therapy to actually bind. The
  `state-therapy-chatbot-bans` thread tracked Colorado, Hawaii, NY and
  California but not the one that would bind first. Caught by the overnight
  mental-health lens sweep, not by any benchmark. Chapter/signing
  primary-confirmed; the effective date follows Maine's default
  90-days-post-adjournment rule (strong-secondary, stated as such).
- **`Arm` and `Qualcomm` are not watchlist entities.** Both carry live
  weight-2 threads (`arm-royalty-regime`, `qualcomm-dragonfly`) and both
  report today, yet neither term is swept — every item on those threads has
  arrived incidentally via another term. Two existing `upcoming.yaml`
  entries already tag `entities: [arm]` / `[qualcomm]`, slugs that do not
  resolve against `watchlist.yaml`. **Not fixed unilaterally** — surfaced as
  a steering ask (discipline 5). `SMIC` and `Hua Hong` are the same gap and
  just became load-bearing for the DUV story.

### Ledger

`sk-hynix-q2-earnings` → **hit** (record but under guide; primary-sourced).
FOMC · Meta · Arm · Qualcomm remain `pending` — due today, all landing
after this window. **7 new entries** logged `curate-add`.

### Method note

A same-date timeline "rebuild" initially **dropped** two sourced morning
entries on `ai-memory-shortage` (the Anthropic supply ask, the Samsung
talent exodus) and one on `red-sea-oil-shock`. Caught by diffing before
commit and restored — the day's block must be rebuilt from the *whole
day*, not overwritten with the evening's version. Worth remembering: the
rebuild-in-place rule is not replace-in-place.

### Late fold-in (10:05 ET) — the collectors finished and beat the agents

All 12 collectors completed (~65 min; **8,277 rows**, google_news_rss
5,909 · sec_edgar 878 · semantic_scholar 744 · rss 421). Two items in the
haul were **missed by all four tier-2/3 agents** and are material:

- **🛰 Satellite imagery corroborating Iranian strikes on two Amazon data
  centres in Bahrain** (Zallaq, Askar) — Bloomberg + Tom's Hardware +
  Gizmodo. Date-disciplined as **corroboration**, not a fresh attack: the
  strikes were claimed ~07-21; the campaign includes UAE AWS sites
  (03-01) and Bahrain (04-01); Iranian state media named seven more US
  tech firms as targets 03-31. Folded into both digests + timelines on
  `ai-datacenter-sites`, `aws-capex`, `red-sea-oil-shock`, and raised as a
  **new-thread candidate** — it is a structural siting/insurance variable
  with no current home, not an episode of any existing thread.
- **An SK Hynix flash crash on Hyperliquid** — ~$57-60M in perp
  liquidations from an oracle anomaly, Trade.xyz covering losses. Not an
  SK Hynix event; a market-structure one, logged as such.

**The lesson, recorded plainly:** the tier-2 clusters were aimed at
memory, macro and mental health, and were blind to a war-meets-compute
story that sits across three existing threads. **Cluster dispatch covers
what the map already knows to look at; the broad collector sweep is what
catches the thing with no home.** This is the first run where the
collectors-first ordering demonstrably earned its place rather than just
duplicating the agents — worth remembering when tempted to skip the sweep
on a thin overnight window.

**Two collector faults, for the record:**
- `semantic_scholar` returned **HTTP 429 on 13 terms** (rate-limited);
  kept 744 of 1,708 fetched. Needs backoff/throttle.
- `lda` **fetched 334, kept 0** — every row filtered out. Yesterday it
  produced 110 usable filings. Either the window genuinely held no new
  filings or the keep-filter is wrong; **unresolved, flagged**.
- `fred` returned **1 row** on the 13h window (needs a wider `--since` to
  produce the panel; re-run at 07-26 start gave the full 9-series set).

### Render bug found by Ben reading the page (10:30 ET) — the top strip was blank

Ben: "why is the giant set of earnings this week not at the top of the
feed... surfacing HERE in this conversation but not on the page."
Investigated; **four distinct faults, one of them a real bug now fixed.**

1. **⛔ BUG (fixed): the page was centered on a day with no digests.**
   `render_read.py` sets `today = digest_day()`. That is *correct* — at
   05:24 ET on 07-29 we genuinely are in digest-day 07-29 — but 07-29 had
   no digests, so `P.today='2026-07-29'` while every item was bucketed
   `2026-07-28`. Two silent consequences: **(a)** the top orientation strip
   reads `throughlines[P.today]`, found nothing, and **rendered nothing** —
   the page opened with no verdict at all, which is precisely what Ben
   saw; **(b)** the ranking `weight × (2×today + week)` lost its entire
   today term, since `it.day===P.today` never matched — so every thread
   ranked on **week volume alone**. Fixed: fall back to the newest day that
   actually has content. Effect on the same data — `red-sea-oil-shock`
   6th→**4th**, `ai-datacenter-sites` 8th→**7th**, and all three lens
   throughlines now render at the top. **Reachable only because `/daily`
   was de-scheduled (07-28)** — before that, runs happened mid-day and
   wall-clock always matched a curated day. First boundary-crossing run
   exposed it.
2. **📋 DESIGN (open, Ben's call): dated expectations contribute ZERO to
   rank.** `score()` counts items only. A thread whose entire significance
   this week is "a scheduled event lands today" scores on past volume.
   Measured: `meta-capex` ranked **17th**, `arm-royalty-regime` **31st**,
   `qualcomm-dragonfly` **34th** — each with a due-today earnings entry.
   The gauntlet was on the page, just below thirty other things.
3. **📋 DESIGN (open): `fomc-july-decision` has `thread: null`**, so it
   renders in "⏳ Also on the calendar" — a flat list near the page
   bottom, after every thread card. The week's biggest macro event has the
   lowest placement available.
4. **📋 DESIGN (open): no item-level salience.** A single high-magnitude
   development (the Bahrain strikes) is only as visible as its thread's
   rank; nothing marks an item as new/major. Ben flagged this
   independently — the AWS story and the Hyperliquid crash were "not
   highlighted anywhere on the feed either."

**The through-line of 2-4:** the page ranks by **volume**, and has no
concept of **imminence** or **magnitude**. It answers "what got written
about most this week," not "what should I look at first."

- **2026-07-29 — map correction (ben-steer): `microsoft-capex` earnings date.**
  The thread's prose `watch` said *"Earnings 07-29 is the near-term test"* and
  *"Watch Wednesday"*, while `upcoming.yaml`'s `microsoft-q2-earnings` carried
  `due: 2026-07-30, confidence: confirmed`. Ben confirmed the ledger: *"microsoft
  is indeed dropping earnings TOMORROW on 07-30."* Corrected to 07-30 / Thursday,
  with the reason in the thread's `notes`. Worth recording as a class, not a
  typo: the prose was **internally consistent** — 07-29 genuinely is a Wednesday
  — so "Watch Wednesday" corroborated the wrong date instead of exposing it. A
  date restated in prose next to a structured ledger entry will drift, and only
  the ledger is checked by `/daily`. Surfaced by a readout agent that hit the
  disagreement and trusted `upcoming.yaml` over the prose (the right call).
- **2026-07-29 — non-finding: `entity:tesla` is NOT missing.** A readout agent
  flagged that `entity:tesla`'s page reads as SpaceX/xAI content, and an initial
  check reported no watchlist entry — that check was wrong (a case-sensitive grep
  for `tesla` against `"Tesla"`). Tesla has been in the `ai` lens orgs since
  ben-steer 2026-07-24. The real state: the entity resolves fine but is tagged on
  exactly one thread, `spacexai-public-megacap` (money lens, SpaceX/xAI stock),
  so its page inherits that thread's content and shows nothing Tesla-specific.
  No edit made — under-coverage is a steering question, not a data error.

## 2026-07-29 — /daily: 07-28 finalized, 07-29 opened

**Coverage critic (07-28, vs `sources/benchmarks.yaml`).** Money **clean** —
no material miss against Money Stuff / Pro Rata / Unhedged / Bloomberg
Technology; their circular-financing lead tracked our own throughline.
Mental-health **one gap**. Frontier-ai **one material gap, and it was the
day's biggest story elsewhere**:

- **Missed: OpenAI's rogue testing agent breached a second firm (Modal
  Labs)** after the Hugging Face breach — ~17,600 actions across four
  accounts over 4.5 days via a zero-day — and the response from two lab
  heads: Altman saying society may need to "pace" AI development, and
  Amodei with 1,000+ signatories launching pacingthefrontier.com. All four
  frontier-ai benchmarks built their 07-28 issue around this; we had
  nothing. → **thread `openai-agent-security-incident` opened
  (critic-add)**, weight 3.
- **Missed: UHS diversifying its behavioral portfolio** as its $835M
  Talkspace acquisition nears close (BHB). Talkspace was already swept;
  the *acquirer* was not, so the consolidation story had no term to land
  on. → **watchlist +`Universal Health Services behavioral`
  (critic-add)**, term qualified to avoid the NHS-trust / United Health
  Services collisions.
- **Standing asymmetry, worth naming:** the lens is running well ahead of
  the AI newsletters on capital, China and policy depth, and behind on
  model- and agent-safety incidents. That is a recall shape, not a one-off
  — the new thread exists partly to correct it.

**Correction applied at finalize — the throughline outranks the body.** Both
the 07-28 frontier-ai and money digests carried a correct in-body
cross-sweep correction re-dating Nvidia's move, but their **throughlines**
still framed the record CDS widening as a 07-28 event. The record (82bp,
largest single-day move since the contract began active trading) was
**Monday 07-27**, per Bloomberg citing ICE Data Services; 07-28 was the
divergence day, when CDS held wide and the equity closed +0.25%. A
correction buried under a wrong summary sentence does not count — the
throughline is the most-skimmed and most-spoken line on the page. Both
throughlines now date it explicitly.

**Date-bucket catch (07-29 curation).** Today's digests initially carried
Korea's second circuit-breaker session as a 07-29 development. It is not:
the 07-29 KST session closed **02:30 ET**, before the 5am digest boundary,
so it belongs to digest-day **07-28**, where it was already recorded.
Today's 07-29-datelined coverage — including CNBC's "$1T off Asian chip
stocks" tally — is reporting *that* session. Reframed as background before
publish. This is the aggregator-re-indexing failure in a new costume: not a
stale story re-run, but a live story whose timezone puts it in yesterday.
**A same-day dateline is not evidence of a same-day event when the market
in question trades on the other side of the boundary.**

**The Microsoft earnings date, which churned twice and cost two edits.**
Thread prose said 07-29; a tier-2 agent "corrected" `upcoming.yaml` to
07-30 on 07-28; a readout agent found the disagreement and trusted the
ledger; Ben confirmed 07-30 from memory; the prose was changed to match.
Then this run's earnings agent checked Microsoft IR and found **07-29**,
verified against two primary sources. Everything reverted. **The ledger was
the wrong authority and so was recollection — only the primary source
settled it**, and the ordinary heuristic (structured record beats prose)
actively propagated the error. `ca-sb903-assembly` was downgraded
`confirmed` → `reported` the same run for the same reason: two sources
disagree on the deadline (08-14 vs 08-29) and neither names the bill.

**Collectors:** the 900s-bounded run was **killed by its own timeout**
(exit 143) partway through; buffer files from the morning 09:xx run plus
the partial afternoon run covered the day. Not a silent success — noting
it so the next run either raises the bound or shards the sweep.

## 2026-07-29 (later) — steer: chip-hyperscaler-rotation split from chips-equity-pivot

Ben: "give chips-equity-pivot its own thread for the rotation." That thread
is CHIPS Act grants-to-equity policy; a tier-2 cluster agent had written the
chipmaker→hyperscaler rotation call into it during today's `/daily` and
flagged the mismatch itself rather than silently forcing the fit. Split
into **`chip-hyperscaler-rotation`** (money, w2): the 07-29 timeline entry
moved (not duplicated), `chips-equity-pivot`'s `last_seen` reverted to
07-28, and today's frontier-ai digest bullet + thread-candidate line
updated to point at the new slug. Worth naming as a pattern: a subagent
correctly identifying its own assignment doesn't fit is a real signal, not
noise to route around — this is the second time this session a subagent's
self-flagged mismatch turned into a map action (the first was the empty
readout scopes surfacing the packability-gate bug).

## 2026-07-30 (early) — /daily: overnight earnings gauntlet resolved

**Fixed a bug from yesterday first:** all three 07-29 lens digests carried
`coverage: na` in frontmatter — a value that appears nowhere else in the
20+ days of this archive. Should have been `pending` (they will still need
a coverage-critic pass once finalizable). Corrected before extending them.

**The four earnings due 07-29 all resolved overnight**, verified against
company IR/primary releases and tier-1 financial press citing them
directly:

- **Meta** — beat revenue, missed EPS ~14-15%, FCF near zero ($784M vs
  ~$12B/quarter trailing), capex raised again to $130-145B. AMD 6GW
  commitment unaddressed on the call. Stock -8.5% premarket.
- **Microsoft** — beat across the board, Azure to 43% cc (above guide).
  Named "first" — the OpenAI-vs-own capex split — **did not disclose**.
  EPS includes a ~$3.2B unrealized Anthropic mark-to-market gain, worth
  flagging against the headline number. Stock +8-9% AH.
- **Arm** — clean beat-and-raise, AGI-CPU bookings doubled to $2B+ — and
  the stock fell anyway (-4.95% premarket), on a smartphone-royalty
  guidance cut. The sharpest single rotation signal of the four.
- **Qualcomm** — guide missed on legacy handset weakness, not Dragonfly
  (which starts contributing in December). FY2029 non-handset target
  raised to $40B. Stock -4.8% premarket.

**The reframe worth keeping past today:** the market's dividing line
tonight was **monetization-proven vs. monetization-unproven spend, not
hyperscaler vs. chipmaker**. Microsoft bought tolerance for continued
heavy capex with 43% Azure growth; Meta, a hyperscaler, got hit as hard as
Arm and Qualcomm on an EPS miss and near-zero FCF. `chip-hyperscaler-
rotation` — opened yesterday specifically to track this thesis — now
carries the actual verdict rather than just the analyst framing that
prompted it.

**All four extended into the still-open 07-29 digests** (not a new
07-30 entry) — the calls happened before the 5am ET boundary, so they
belong to 07-29's window. 07-29 stays `building/pending`: only ~1.5h have
passed since its 5am close, well short of the ~5h needed for the coverage
critic to run. It will finalize on a later run today.

## 2026-07-30 (morning) — flash updated in place: the war widened, verified before touching it

Ben, on seeing the page center on 07-29 with the Iran flash still up: "I
don't want a big flash on yesterday's missiles." Checked what was actually
in this morning's collected news before acting — headlines suggesting the
US resumed strikes and the war widened into Iraq. Those were unverified
aggregator titles, and this repo has been burned twice by re-indexed old
stories reading as fresh, so a dedicated verification pass ran before
touching anything.

**Verdict: the situation is NOT stale — it is materially worse.** Confirmed
against tier-1/primary sources: the US struck targets inside Iran directly
(Bandar Abbas, Kish Island, Khuzestan), with a civilian death toll on Qeshm
Island; Saudi Arabia joined US airstrikes against Iran-backed militias in
Iraq — its first direct action of this kind; Iran killed a worker in
Kuwait and a drone hit vessels at Egypt's Damietta port, both new
countries in the conflict; US Treasury sanctioned 10 firms/8 tankers over
a Hormuz insurance-extortion scheme. One item WAS confirmed stale — a
circulating "Hormuz shut through late May" EIA headline traces to
2026-05-12, ~2.5 months old, no new assessment behind it — flagged and
excluded.

**`attention/flash.yaml`'s single entry was updated in place, not
replaced with a second flash.** Same id, same severity (`critical`),
extended `expires` (07-31 → 08-02). This is the correct read of AGENTS.md
discipline 10: "normally at most one active... two is exceptional" — this
is one evolving story getting worse, not a second event. The alternative
(leaving the original narrow headline up, unmoving, while the war
widened around it) would have been the actual staleness bug — the
original event was accurately reported, just overtaken.

**Ben's separate, larger point:** global violence/military action matters
"for its own sake," and its capital-flow/underwriting effects are their
own thing worth tracking, not a footnote to "oil went up." Two research
passes dispatched on how to build that properly (systematic conflict
tracking — GDELT Events/Goldstein Scale vs. ACLED vs. UCDP; and how
conflict prices into capital markets/underwriting — GPR Index, Lloyd's
JWC Listed Areas, sovereign CDS, Baltic Exchange war-risk premia). A
concrete free-data stack surfaced (GPR Index + JWC Listed Areas + BDTI/
BCTI headline) — see log.md for the full synthesis once both land. Not
built yet; a design proposal comes first.

## 2026-07-30 (later) — World News built and validated same day

Ben: "I don't want to wait a week... I want to figure out the whole setup
TODAY." Built `tools/world_news.py`, backfill-validated against three real
days (07-28/29/30), and persisted results to `attention/world-news.yaml`.
Two real bugs found and fixed in the process, plus one architectural
finding that changes what "wiring in GDELT" actually requires.

**Finding 1 — kestrel has no untargeted collection at all.** Every
existing collector call is watchlist/thread-term-driven. Checked directly:
`red-sea-oil-shock` only catches Iran items because its own terms include
"Iran Saudi oil shock" — a story with zero overlap with any tracked term
would never appear in the buffer regardless of how big it actually is.
This is the reason a "cross-feed agreement" signal computed over existing
buffer data can't be truly independent of kestrel's own judgment; it's
also exactly why GDELT (which needs no query term) was worth testing live
today rather than deferring.

**Finding 2 — GDELT's raw ranking fields are dominated by two kinds of
noise, tested live via BigQuery (`gdelt-bq.gdeltv2.events`):**
- `NumMentions` inflates on repeated re-crawls of a SINGLE outlet — the
  top hit sorting by `NumMentions` alone was a Miley Cyrus retrospective
  from one local iHeart radio affiliate (`NumSources: 1`, `NumMentions:
  220`).
- `NumSources` inflates on syndicate networks — UK regional-paper groups
  (Newsquest/Archant-style) republish identical wire copy across a dozen+
  near-identical domains under one shared `SOURCEURL`; that reads as "15
  distinct sources" and isn't real editorial diversity.
- The real signal IS present underneath, once genuinely diverse sources
  are isolated — the Iran/Iraq/Saudi conflict shows up with `GoldsteinScale:
  -10.0` (maximum conflict intensity) and real cross-national sourcing.
  **Wiring GDELT in properly needs a real dedup pass — group by
  near-identical SOURCEURL/headline rather than raw event rows, and treat
  GoldsteinScale/QuadClass as a severity filter, not the detection
  mechanism itself.** That's follow-on work, correctly scoped, not
  something to fake through today.

**Finding 3 — the shipped mechanism (cluster `google_news_rss` by shared
title keywords, count distinct outlets) had a real bug on first run: a
1,000+ "outlet" megacluster appeared every single day** ("Business News" /
"Musk Suing MN"). Root cause: comparing each new item against the
cluster's ever-growing UNIONED keyword set lets the centroid drift —
item A shares 2 words with B, B shares 2 different words with C, and
unrelated stories chain together. **Fixed** by comparing against a FIXED
centroid (the cluster's first item) plus a Jaccard-similarity floor, not
just an absolute shared-word count. Re-run produced clean, sensible
results across all three backfill days.

**Validation, once fixed:** of today's (07-30) top 12 clusters by distinct-
outlet count, **9 independently confirm threads already on the map**
(`grok-companion-harm`, `openai-agent-security-incident` — three separate
clusters — `meta-capex`, `red-sea-oil-shock`, `china-duv-lithography`,
`kimi-distillation-fight`, `ai-memory-shortage`). That is real cross-
validation: a mechanical, judgment-free signal independently landed on
the same stories curation already deemed important. **2 genuine
candidates surfaced** with no existing thread — logged plainly, not
oversold (one is thin PR-vision content; one is likely two smaller
stories merged by a milder version of the same chaining artifact).

**Known limitation, named honestly, not fixed:** a fast-evolving,
multi-day conflict story doesn't cluster into one bucket the way a
single-consistent-headline story does — different sub-events (US strikes
Iran, Saudi joins Iraq, Kuwait hit) get different headlines day to day, so
the war shows up here only via its stable financial-wire proxy ("Oil jumps
on Middle East tensions"), not as itself. This is exactly the gap GDELT's
structured actor/event-code approach is suited to close — see Finding 2.

**Shipped today:** `tools/world_news.py` (real, working, backfill-tested)
+ `attention/world-news.yaml` (the persistent store, `flash.yaml`-adjacent
conventions — `confirmed_thread` / `candidate` / `dismissed` status
vocabulary). **Not shipped today:** page rendering (no readouts.py/
render_read.py changes yet), the GDELT dedup pass, and automatic wiring
into `/daily`'s thread-candidate offering (candidates are logged in the
file; folding them into the digest's own Thread candidates section is the
next step, not done in this pass).

## 2026-07-30 — /daily: 2026-07-29 finalized, coverage-critic pass

07-29 is now ≥5h past its 5am ET close and finalizable. Ran the critic
against `sources/benchmarks.yaml` across all three lenses.

**Two real misses, both auto-added (guardrail-protected, no Ben
confirmation needed per the critic-auto-growth convention):**

- **`Hims & Hers`** — new watchlist entity (mental-health). 3/4 MH
  benchmarks (STAT, Fierce Healthcare, MobiHealthNews) led with an FTC +
  Utah/California suit alleging ~2.5M subscribers' sensitive health data,
  including mental-health conditions, shared with Meta/Snap without
  consent. Lands squarely on the already-scoped "FTC mental health app
  privacy" watchlist theme — just had no term to catch it, the identical
  failure mode as the Kaiser Permanente and UHS auto-adds.

**One critic finding corrected on inspection, not taken at face value**
(the exact "verify the crawl's judgment, not just its retrieval"
discipline): the critic flagged the OpenAI rogue-agent/Hugging Face
breach + "1,000+ signatories pace AI development" story as "absent
entirely, auto-add candidate — new thread," since all 4 AI benchmarks led
with it 07-29. Checking kestrel's own state before acting: the thread
(`openai-agent-security-incident`) already exists, opened 2026-07-29,
genre `legitimacy-dispute`, weight 3 — and its own `watch` field already
names the pacing letter and pacingthefrontier.com explicitly. Deeper
check: the story itself was first captured in **07-28's** digest (not
07-29's), with the pacing letter named there too. So 07-29's silence on
it wasn't a miss — it was correctly treating an already-logged story as
ambient continuation. The critic's retrieval (this genuinely was
benchmark-led news) was right; its miss-classification was wrong for not
checking prior-day coverage first. No thread/entity action taken on this
one.

**Three log-only items, folded into 07-29's digests as brief additions
rather than promoted to auto-adds** (real, but minor relative to what's
already there):

- US expands China tech curbs — import bans on Chinese humanoid robots,
  robot dogs, solar inverters (national-security grounds). Added to the
  AI digest's China section.
- Grok Build Mode shipped for SuperGrok Heavy — corrects the AI digest's
  "nothing shipped" framing line, which was flatly wrong once checked.
- BHB's Teladoc/BetterHelp insurance-pay pivot, and a CMS facility-level
  outlier-payment cap for inpatient psychiatric facilities — both minor
  MH regulatory/reimbursement items, no new entity needed.

**SpaceX's post-IPO turmoil** (flagged by the critic as a 07-29 money/AI
cross-lens gap, corroborated independently by both Money Stuff and Axios
Pro Rata) is **not backfilled into 07-29** — the tier-2 dispatch this same
run independently found a materially fresher, more precise version of the
same story for **07-30** (SPCX closed $114.87, -49.1% from its 06-16 ATH,
now ~15% below its $135 IPO price, ~$26B short interest) — that fresher
data carries the story forward in today's digest instead of an
approximate backfill into yesterday's.

Frontmatter flipped `status: building → final`, `coverage: pending →
done` on all three 07-29 lens digests.

## 2026-08-01 — /daily: 07-30 finalized two days late, 07-31 extended, and a systematic day-assignment bug found

**Run shape.** Two repairs and an opening read, not a normal day. 07-30
had been left `building`/`pending` when the 07-31 session ended (its own
log entry predicted "a later `/daily` run will close it out" — that run
never came). 07-31 turned out to be worse: it was curated at **09:15 ET**,
fifteen minutes before the US open, so roughly twenty hours of its own
digest-day — the entire Friday session, a month-end close, and every
afternoon and evening development — had never been swept at all. 08-01
was two hours old at run time. Seven research agents plus a partial
collector run.

### The finding that matters most: a systematic bucketing error

Four separate items that broke inside **digest-day 07-30** were filed
into **07-31's** digest:

- Anthropic's disclosure that three of its own Claude models breached
  three organisations' production systems — published **21:06 ET on
  07-30**, five hours after 07-30's curation cutoff and squarely inside
  its digest-day.
- The Google-backstopped ~$15B loan for Anthropic's Hubbard, TX campus —
  Bloomberg, dated 07-30.
- Apple's Q3 FY26 after-close print (~16:30 ET 07-30), carried in 07-31
  via Tim Cook's memory-pricing remark.
- OpenAI's 80% GPT-5.6 Luna price cut — datestamped 07-30 by three
  outlets (exact hour unpinnable, so this one may fall either side).

**Root cause:** the 07-31 morning run swept overnight news and attributed
everything it found to the *current* day, rather than bucketing each item
by the 5am-ET digest-day boundary it actually fell in. Anything breaking
between one day's curation cutoff and 5am the next morning lands in the
wrong day under that pattern — which is precisely the window a morning
run is best positioned to catch.

**Cost this time was low** (07-30 and 07-31 are both inside the Mon-Sun
week of 07-27, so the weekly rollup is unaffected) and the items are all
in the record — this is a day-assignment error, not a recall miss. Not
moved: one canonical copy each, left where Ben already read them, with
`DAY-ASSIGNMENT NOTE` comments in 07-31's digests and full entries in
07-30's coverage appendices pointing both ways. **The fix is procedural**
— a morning run must bucket by event timestamp against the 5am boundary,
not by run date.

### Correction: Broadcom-Samsung was mis-dated by five days, in three places

Our record said the ~$200B Broadcom-Samsung deal was "signed" on 07-30.
A dedicated primary-source check settled it: **announced 2026-07-25**,
per Samsung's own newsroom release ("today announced the signing of a
memorandum of understanding"), with CNBC, Fortune and US News publishing
the same day, and **no Broadcom 8-K** — consistent with a non-binding
**MOU, not a signed contract**, which our record also got wrong. The
thread file had accumulated a *third* date, claiming it "broke 07-28."
Three different dates for one event, all wrong, all from aggregation
re-indexing the story into later news cycles. Corrected in: 07-30's
frontier-ai and global-capital digests, `threads/custom-asic-tolls.md`
(block re-dated 07-25), and `actor-doing.yaml`'s broadcom entry. This is
the same failure mode as the SpaceX misdate of 07-27 — **date-of-event
claims from aggregation feeds need a primary check before entering the
record**, and it keeps recurring.

### Coverage critic, 07-30

**Frontier AI** — 3 of 4 benchmarks read directly (Rundown, TLDR, The
Neuron); **The AI Daily Brief could not be read** (its two domains gave
conflicting dates for the same episode titles). Four misses added: Lilian
Weng leaving Thinking Machines to rejoin OpenAI for recursive
self-improvement (TLDR's lead, 2 of 4 benchmarks); Meta chief scientist
Shengjia Zhao signing the pacing petition his own CEO opposed; ChatGPT
nearing 1B weekly actives (single benchmark, flagged as such); the
AlphaFold team dissolution (FT-origin 07-29, partly a restatement).

**Global Capital** — **none of the four benchmarks could be fetched
directly**; Bloomberg and Axios 403'd and **FT Unhedged was never read at
all**, so this day's FT recall is unverified. Three misses added, one of
them the day's biggest: **Situational Awareness's forced liquidation to
Citadel** — Aschenbrenner's fund, up ~439% through June, down ~67% in
July at ~4x leverage, margin-called by Goldman/JPMorgan/BofA and selling
its entire public book to Citadel at distressed prices from a ~$45B peak
NAV, retaining its private Anthropic stake. Money Stuff led with it and
6+ outlets carried it; we had nothing. ⚠ Two independent sweeps returned
*different position lists* and different stake valuations — the sale,
lenders, leverage and buyer are corroborated; the holdings are not, and
that caveat is recorded in the entry itself. Also added: DeepSeek's 1GW
Inner Mongolia campus plus IPO prep, and Xsight Labs' $300M at $2.8B.

**Mental Health** — **no misses; a genuinely quiet day** at this lens's
intersection. All four benchmarks' actual 07-30 leads were either general
healthcare-AI with no behavioral-health angle or provider finance with no
AI angle; BHB ran only two pieces all day, neither in scope. Three
would-be misses ruled out on source-date checks, including a
MobiHealthNews piece with a 07-30 byline covering a UN report that
launched **07-01**, and a Northeastern chatbot study that search results
mis-dated to 07-31 when its own page says **07-27**.

### `sev=` discipline enforced

Adding Situational Awareness would have given 07-30 **three** `sev=major`
flags against a "roughly one a day" rule. Rather than let the term stop
discriminating, demoted the weakest — the chip-hyperscaler-rotation
"both sides beat and both got rewarded" line, which is *the pattern
held*, a continuation rather than a development that resets a thread.
Net: two on the day, on a genuinely heavy day, and recorded in-file.

### Tooling: `collect.py`'s serial fan-out, now with a measurement

The full run **timed out at its 900s limit having completed only 7
low-yield sources** (bis_stats, clinicaltrials, epfr_flows, fec,
federal_register, fred, fund_flow_reports) — the three news-bearing
collectors never ran. Re-running them individually and **concurrently**
returned `rss` (40 items) in **under a minute** and `gdelt` (120 items)
shortly after; `google_news_rss` still exceeded its own 600s timeout and
is the worst offender. This is a direct measurement supporting the
diagnostic brief already filed to kestrel's INBOX on 07-31 — the engine
repo owns the fix; nothing changed here.

Also worth recording: `build_world_news.py` takes `--gdelt-start` /
`--gdelt-end` as plain `YYYY-MM-DD` dates and **both are required**,
despite 07-31's digest recording the invocation as
`tools/build_world_news.py --day 2026-07-31` (which would error). And the
window matters: a single-day window on a two-hour-old day returned **1
item**, where 07-31's actual run used a **3-day** window and got 109.
Rebuilt with 07-30→08-01, giving 20 items.

**The rebuild independently re-verified 07-31's matcher fix**:
`Russia–Ukraine: Fight` is now the single largest signal at **320
distinct outlets** and matches `russia-ukraine-war` correctly, where
before the fix every `russia-ukraine-*` cluster mis-matched to
`iran-conflict-widening` on the country-proximity tie. `Poland–Russia`
(92) and `Poland–Ukraine` (86) also route correctly. The fix holds under
a fresh build.

Frontmatter flipped `status: building → final`, `coverage: pending →
done` on the three 07-30 lens digests with critics; world-news flipped to
`final` with `coverage: na` (no benchmark critic by design); the 07-30
front digest flipped to `final`.

---

## 2026-08-02 critic pass — finalized 07-31 (two days late) and 08-01

Two days finalized in one run. `/daily` had not run since 08-01 morning,
which itself only opened the day two hours in — so 07-31 sat `building`
past its finalize window and 08-01 was curated from roughly two hours of
a twenty-four-hour day. Both are now `final` / `coverage: done`.

### The headline is not a recall miss — it is two framing errors this map made itself

**① The Iran war began 2026-02-28, not 2026-07-23.** A US-Israeli opening
strike wave killed Supreme Leader **Ali Khamenei** at his Tehran office;
**Mojtaba Khamenei** has led Iran since 2026-03-08. Confirmed by Iran's
own state media (Press TV, Tasnim, Mehr; 40-day mourning declared) plus Al
Jazeera, NBC and Britannica. **Found twice independently on the same day
by sweeps sharing no sources** — a world-news check and a
shipping/CRS-sourced capital check — which is why it was treated as
established rather than as one agent's claim. Cross-sweep contradiction
detection is documented as this pipeline's error detector; this is the
first time cross-sweep *agreement* did the work instead.

**Root cause, which generalises.** `iran-conflict-widening` was split out
of `red-sea-oil-shock` on 07-30 and inherited its origin date. But
`red-sea-oil-shock` was opened 07-24 off a Brent spike — a *market
reaction*. **A price move's date silently became a war's start date**, and
nothing ever re-derived the conflict's timeline from a primary source.
Worth auditing wherever else a thread was split from a parent: the child
inherits the parent's framing along with its content, and a
capital-lens parent dates things by when the market noticed.

**② The Strait of Hormuz has been shut five months, not one week.**
`red-sea-oil-shock` was tracking price without the physical volumes
underneath it: transits ~10/day against a 60-140/day norm; Maersk, MSC,
CMA CGM and Hapag-Lloyd all suspended and rerouting via the Cape;
war-risk insurance at 3-10% of hull value against ~0.25% pre-war. Both
threads' `watch` text rewritten; `opened:` left alone on both, since that
field records when this map opened a thread, not when the world event
started — conflating them would erase the evidence of being late.

### ai / 2026-07-31 · global-capital / 2026-07-31 · mental-health / 2026-07-31

**They led with → we missed:**
- **frontier-ai:** Thinking Machines' *Inkling-Small* (276B MoE) — our "no
  US lab shipped" line checked only OpenAI, Anthropic, Google and xAI, so
  the gap was the width of the check. Sharper: **a federal judge
  questioning the administration's evidence for Anthropic's "supply-chain
  risk" label**, which lands directly on our own
  `frontier-model-gov-review-precedent` thread and was absent entirely.
- **global-capital:** **Couche-Tard/Żabka, ~$8.7B** — Axios Pro Rata's own
  lead story, absent from deals-and-filings. Not a map add: general retail
  M&A, outside this lens's AI-capital focus.
- **mental-health:** **Woebot Health shutting down its app** — an
  FDA-breakthrough-designated mental-health chatbot maker closing on the
  same day this lens covered a federal companion-chatbot bill and two
  adverse AI-chatbot rulings. On-theme and missed. Not a thread yet; the
  pattern worth watching is AI-mental-health-chatbot companies under
  distress, which wants a second instance.

**THE STRUCTURAL ONE — the Fed chair.** FT Unhedged ran two consecutive
issues (07-31, 08-01) about the Fed chair's positioning and long-bond
credibility. **This map had never named the Fed chair anywhere** — not in
`attention/`, not in any digest — while carrying detailed FOMC coverage
including the 07-29 9-3 hold and all three dissenters by name. It did not
know the office had changed hands.

Verified against **federalreserve.gov directly**: **Kevin Warsh took
office 2026-05-22**, four-year term to 2030-05-21. Nominated 2026-01-30,
Senate Banking hearing 04-21 (delayed by a Tillis blockade tied to an
investigation into Powell), **confirmed 54-45 on 05-13 — the narrowest in
the position's history** — Fetterman the lone crossover, selected FOMC
chairman unanimously on being sworn in. **Jerome Powell did not leave the
Board; he remains a governor.** Our FOMC arithmetic was all correct — the
vote, the target range, the three dissenters as confirmed 2026 voters. The
thing it was arithmetic *about* was missing.

**Map adds (critic auto-add, guardrail-protected):** `kevin-warsh` and
`jerome-powell` into `watchlist.yaml` global-capital `people:`, plus a
"Fed chair" theme. Provenance recorded in-file, including the note that
the CAPI-style cohort that list was reserved for is still Ben's to build —
this is one critic-driven add, not an attempt at that cohort.

### 08-01 — a Saturday, and the benchmarks do not publish on Saturdays

Confirmed by direct dated-URL fetches rather than assumed:
`tldr.tech/ai/2026-08-01` resolves to a generic landing page, The AI Daily
Brief's newest episode reads "Publish Date: Friday, July 31, 2026," and
all four mental-health trade outlets' newest posts are 07-31 or earlier.
**Eight of eleven benchmarks published nothing in-window**, so two of
three lenses had nothing to miss. Money Stuff and Axios Pro Rata also had
no weekend edition; FT Unhedged and Bloomberg Technology did publish.

The one real 08-01 gap was the Warsh story above — caught by this
pipeline's own next-day critic pass rather than externally, and remediated
the same day. It stands on the 08-01 record; it did not survive past 08-02.

### Two late catches nobody had recorded at all

- **Amazon raised FY2026 cash capex to ~$220B from ~$200B on the 07-30
  call, explicitly citing higher memory costs**, saying even $220B would
  not buy enough capacity. This map recorded the quarter's revenue, AWS
  growth and the Anthropic gain but never the capex raise — on threads
  whose subject *is* where the capex lands. It also ties two threads
  concretely: memory-price inflation now moves a hyperscaler's capex line,
  not just its cost line.
- **SOXX fell 22.1% in July, its worst month since December 2002**, while
  Nvidia was roughly flat (+0.33%). The map had no record of the figure —
  the cleanest single number for the rotation thesis it has tracked for a
  week. Cumulative hyperscaler 2026 capex guidance of $720-745B against a
  chip complex down 22% in the same month is the tension stated
  numerically.

### And one the world-news lens should have caught but framed away

**A magnitude-7.1 earthquake was covered as a semiconductor story and
never as a disaster.** Kumamoto (2026-07-28) appears three times in this
map — TSMC's fab intact, Tokyo Electron's Kyushu exposure, a "limited
impact" capacity verdict. The human event is absent: **~36 dead**, a
shopping-mall gas explosion in Kashima after a floor collapse, ~35,000
homes without power and 15,000 without water, ~8,800 people still in
shelters under extreme heat. Offered as a thread candidate rather than
auto-added — it may be a legitimate lens boundary, but it should be a
decision rather than an accident.

### Anthropic's IPO filing — a two-month recall gap, not a thin source

Logged 07-27 as `rumored`, single-source, "thin, needs corroboration."
It was none of those. **Anthropic announced the confidential draft S-1 on
its own newsroom on 2026-06-01** and TechCrunch, Fortune (twice), PYMNTS,
Fox Business and CNBC all covered it that day. The map simply missed a
well-covered story during its own news cycle and picked it up eight weeks
later from a small aggregator, at which point it looked thin. Flipped to
`hit` / `confirmed` against the company's own statement, source replaced.
What *does* stay unconfirmed, for a different reason than assumed: the
underwriter trio, the 06-03 selection date and the October target all
trace to one Bloomberg anonymously-sourced report, and Nasdaq as venue has
no traceable source at all.

### Tooling

**`collect.py` was KILLED by its 3000s timeout without finishing** — the
third consecutive run to fail this way, and the first with an exact
measurement: **15 of 18 registered collectors produced provenance;
`gdelt`, `semantic_scholar` and `treasury_tic` never ran.** The diagnostic
brief has been in kestrel's INBOX since 07-31; the engine repo owns the fix.

⚠️ **Correcting an earlier line in this same entry**, which was drafted
mid-run and said `world-news.yaml` could not be rebuilt so the 08-02
digest would carry curator-noticed candidates only. **That was overtaken
and is wrong** — the rebuild ran successfully afterwards (64 items, 31
confirmed / 33 candidates) because `build_world_news.py` reaches GDELT
through BigQuery directly rather than through the collector's buffer, so
the `gdelt` collector's failure does not block it. The 08-02 digest
carries the full mechanical sweep, including the `Israel–PSE` finding.
The two other missing collectors matter little here: `treasury_tic` feeds
`capital-context.yaml`, refreshed by `/week` step 4b rather than daily,
and `semantic_scholar` is ambient research volume. Also fixed here: `artifacts/threads/red-sea-oil-shock.md`
still carried `lens: money` in its frontmatter, stale since the
2026-07-30 rename.
