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
- **mental-health:** ~~**Woebot Health shutting down its app** — an
  FDA-breakthrough-designated mental-health chatbot maker closing on the
  same day this lens covered a federal companion-chatbot bill and two
  adverse AI-chatbot rulings. On-theme and missed. Not a thread yet; the
  pattern worth watching is AI-mental-health-chatbot companies under
  distress, which wants a second instance.~~
  ⚠️ **RETRACTED 08-03 — this was NOT a real recall miss.** The 08-03
  critic verified the MobiHealthNews article is dated **2026-04-25 (of
  2025)**; the Woebot app retired **2025-06-30** — five mirrors + a
  Feb-2026 Wayback capture agree. It is 15-month-old news that was logged
  as a fresh 07-31 catch. **Root cause:** the item was accepted on a
  headline+URL whose *date* was never confirmed against the digest window,
  behind a hedge ("only the headline, URL and date are confirmed") that
  itself named the date as unconfirmed. **Standing lesson (applies to
  every lens):** a benchmark-recall "miss" only counts once its *date* is
  confirmed inside the digest window against a primary or mirror source; a
  bot-walled full-text fetch is a reason to date-check *harder*, not a
  licence to log on the headline. The 07-31 and 08-02 MH digests carry the
  matching retraction/correction annotations.

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

---

## 2026-08-03 critic pass — finalized 08-02 (Sunday)

**Recall: clean.** 08-02 was a Sunday; the critic's benchmark publications
(the mid-morning trade/legal/regulatory sources) were silent as expected,
and the day's own throughline was self-correction rather than fresh news
(the five-month Iran-war redating, the unnamed-Warsh Fed correction, the
EU AI Act mechanism fix, the Anthropic-IPO recall gap — all already in the
08-02 digests and the 08-02 critic block above). No benchmark surfaced a
lens-relevant story the day's digests missed. Two items of business, one a
retraction of a prior pass:

### RETRACTION — the Woebot "miss" was 15-month-old news, not a 07-31 catch

The 08-02 critic block above logged **"Woebot Health shutting down its
app"** as an on-theme mental-health miss the benchmarks caught. It was not
a miss and not from the window. The MobiHealthNews article is dated
**2026-04-25 (of 2025)**; the Woebot app retired **2025-06-30** — five
mirror sites and a Feb-2026 Wayback capture agree. This is 15-month-old
news that entered the ledger as a fresh catch.

- **Root cause:** the item was accepted on a headline + URL whose *date*
  had never been confirmed against the digest window, behind a hedge
  ("only the headline, URL and date are confirmed") that itself named the
  date as one of the *unconfirmed* things — the crack was reading that
  hedge as a caveat rather than a stop.
- **Fix, applied across the record:** the 07-31 MH digest carries the
  retraction, the 08-02 MH digest carries the correction, and the Woebot
  line in the 08-02 critic block above is struck through with the
  retraction inline. No watchlist/thread was ever auto-added off it, so
  nothing downstream to unwind.
- **Standing lesson (all lenses):** a benchmark-recall "miss" only counts
  once its *date* is confirmed inside the window against a primary or
  mirror source. A bot-walled full-text fetch is a reason to date-check
  *harder*, not a licence to log on the headline. This is the same
  date-of-event discipline the SpaceX-misdate and Iran-war-redating
  lessons taught, applied to recall inputs and not just to our own
  timeline entries.

### Unconfirmed lead, NOT folded as a miss — OpenAI "Astra"

An 08-02-sweep signal named an OpenAI model **"Astra"** (attached to an
"math-proof" story). It is **not** entering the finalized 08-02 record as a
miss, on exactly the discipline the Woebot retraction just restated.
Today's (08-03) frontier sweep independently found "Astra" is
**single-source-thin**: only NY Post uses the name (as a model "discussed"
at the 08-04 White House meeting), and the 15-state GOP AG letter — which
does name the two models in the OpenAI containment breach as **GPT-5.6 Sol**
and "an unreleased, even more capable" model — pointedly does *not* use the
"Astra" label. Until a primary or second independent outlet confirms the
name and the story, "Astra" is logged here as an unverified lead only. The
frontier-ai 08-02 digest carries the same flag.

**Result:** 08-02 flips to `final` / `coverage: done` across all five lens
files (world-news `coverage: na` by design). One retraction, zero real
recall misses, one unconfirmed lead held out of the record.

## 2026-08-04 (05:40 ET) — the 08-03 overnight extension (no critic pass; day not yet finalizable)

Same shape as the 07-29 extension entry above: the run opened 36 minutes
after digest-day 08-04 began, so **08-03 could not be finalized** — the
coverage critic's benchmark publications appear mid-morning and a day only
flips to `final`/`coverage: done` once its coverage is checkable (~10:00
ET). No critic pass ran. What this pass did instead was read the ~10 hours
of digest-day 08-03 that had never been read: the first pass curated to
18:45 ET and collection last ran 19:22 ET, against a digest-day that runs
to 05:00 ET 08-04. Four tier-2 sweeps covered frontier-AI/governance,
world-news conflicts, capital/capex/chips, and mental health.

### 🚨 A real miss, found by us and not by the critic — Texas froze AI-datacenter grid connections

**The story:** Governor Abbott ordered the Public Utility Commission of
Texas and ERCOT to audit every data centre seeking a grid connection before
it can energise, covering tax incentives, power and water use,
community-impact mitigation and ownership, with non-compliant projects to
be denied connection. ERCOT paused its "Batch Zero" transmission planning
study in response. The queue behind it: **1,800+ projects requesting 474+
GW, ~90% data centres, more than five times the grid's all-time
peak-demand record**, against 335 operating and 248 planned Texas
facilities.

**Why it is a miss and not a late break.** It published **08-03 13:12 CT,
updated 17:25 CT** — inside digest-day 08-03 and roughly twenty minutes
before the first pass's own 18:45 ET cutoff. It was not behind a paywall,
not single-sourced, and not obscure: **12 items on it were sitting in that
day's `google_news_rss` buffer** (KFOX, Axios, Odessa American, KXXV,
WFAA, Newsmax, ABC13, Click2Houston, Texas Border Business,
crossroadstoday, EnergyNow, plus a duplicate), **every one of them routed
to no thread and no entity**. Collection worked; curation did not look.

**The generalisable lesson.** All 12 buffered items carried
`threads: None, entities: None`. This thread family —
`ai-power-buildout`, `where-the-capex-lands`, `ai-datacenter-sites` — is
keyed on company and project names (NextEra, Stargate, Paducah, Colossus),
so a story about *the grid operator and the state regulator* matched
nothing, despite being the most consequential thing that has happened to
the buildout's physical constraint. **A thread whose terms are all
private-actor names cannot see a public-actor intervention in the same
domain.** The fix is not a bigger term list for one story; it is that
power/siting threads need regulator- and grid-operator-side terms (PUCT,
ERCOT, interconnection queue, PJM, MISO, and equivalents) alongside the
developer names. Filed as a term-coverage gap, not a one-off.

**Applied:** new 08-03 timeline blocks written on all three affected
threads, each carrying the miss on its face rather than silently backfilled;
the frontier-ai digest entry is marked `sev=major` and states plainly that
it was a curation miss.

### Two of our own claims corrected

- **"Meta excluded" from the White House frontier framework — wrong.**
  Carried since a 07-21 source and repeated in the 08-03 frontier-ai
  digest, which listed only Anthropic, Google and OpenAI. SiliconANGLE
  (08-03 19:41 ET) names the invitees as **Anthropic, OpenAI, Google and
  Meta Platforms**. The ledger claim text and entity list were rewritten;
  status stayed `pending` because the rewrite corrects the premise without
  satisfying `what_confirms`. Same handling as the
  `eu-ai-act-code-of-practice` rewrite.
- **"Italy/Finland" pushing to suspend Spain from Schengen — wrong.** The
  08-03 world-news digest named Finland. RTÉ, reporting from the
  presidency-holder's side (08-04 09:30 IST), names **Italy and Denmark**.
  Corrected in the digest and noted on the ledger entry.

### Sourcing discipline held, and is worth recording

The sweeps rejected several plausible-looking items on date grounds rather
than logging them — the failure mode the Woebot retraction was written
about. Specifically: a Stocktwits piece headlined "OpenAI Is Laying
Groundwork For A $1 Trillion September IPO" carried an **08-04 RSS
timestamp on a body dated 2026-05-20**, and Anthropic's 07-31 cybersecurity-
eval disclosure is being re-syndicated with fresh 08-03/04 timestamps by
multiple outlets. Neither entered the record as new. Unverifiable figures
(gold, DXY, an overnight 10-year yield) were carried into the
global-capital digest **explicitly marked unconfirmed** rather than either
stated as fact or silently dropped. A Naver/Nvidia/Brookfield item was
dropped outright because the sweep could not reach the source page.

### Known gaps in this pass, stated rather than papered over

- **The mental-health lens was not extended.** Its sweep had not returned
  when this pass closed; nothing was written to that digest rather than
  guessed at. SB 903's Assembly Appropriations hearing (08-05) is
  unverified as of this entry and needs checking on the next run.
- **The collector run did not finish** — 8 of 18 sources at close
  (bis_stats, clinicaltrials, epfr_flows, fec, federal_register, fred,
  fund_flow_reports, github), still running. `google_news_rss` and `gdelt`
  had not landed, so **`attention/world-news.yaml` was not rebuilt and
  remains as generated 08-02**. This is the fourth consecutive run affected
  by the serial fan-out problem already filed to kestrel's INBOX.
- **No coverage-critic pass**, by design — see the top of this entry.

### ✏️ Correction to this entry — the collector did NOT time out, and the four-run diagnosis was wrong

Written mid-run, when the runner was sitting at 8/18 and still going, this
entry said the run was "affected by the serial fan-out problem already filed
to kestrel's INBOX." **That was wrong, and so is the standing diagnosis it
inherited.** The run went on to **complete cleanly: 17 of 18 sources, exit
code 0**, in about 50 minutes. Nothing was killed.

The single failure was **gdelt**, and it was not slowness at all:

    [gdelt] fetched=0 kept=0 skipped_terms=ALL (collector error:
    KESTREL_CONTACT_EMAIL is not set. This collector declares a contact
    address in its User-Agent as required by the upstream source's
    fair-access policy. Set it in your environment.)

A **deterministic config failure that fails in milliseconds**, not a timeout.
`collectors/gdelt.py`, `sec_edgar.py` and `federal_register.py` all read that
variable and are designed to fail loudly rather than send a fabricated
contact address; the engine deliberately ships no default. It was simply
never set in this container's `.env`.

**Why this matters beyond one variable.** The "runner killed by its own
timeout, 15/18" story has been carried in STATUS.md, AGENTS.md and this log
across four runs, and a fix request sits in kestrel's INBOX on that premise.
At least for this run the premise is false. The 15/18 figure that made it
look like a timeout is an artefact of *where alphabetically the run had got
to* when someone looked, combined with gdelt contributing nothing — the
serial fan-out is slow, but it finished. **Anyone acting on the INBOX item
should re-measure before rewriting the runner.**

**Fixed the same session:** `KESTREL_CONTACT_EMAIL` set in the engine's
`.env` to the address already declared for the OpenAlex polite pool, and
gdelt re-run on its own. Recorded here rather than silently, because the
stale diagnosis is the more expensive of the two errors.

### 2026-08-04 (later) — the term-coverage gap this entry identified is now closed (ben-steer)

Ben approved the fix proposed above. Added to `attention/threads.yaml`:

- **`ai-power-buildout`** — the regulator/grid-operator side: `ERCOT`,
  `PUCT`, `interconnection queue`, `PJM`, `MISO`. PJM and MISO are the other
  large US grid operators, so the same class of story in Virginia, Ohio or
  Illinois is caught the way the Texas one now would be, rather than fixing
  one state and waiting to be surprised by the next.
- **`ai-datacenter-sites`** — the approval-gate side: `data center
  moratorium`, `data center audit`, `data center approval`, `data center
  project`, `interconnection queue`.

**Regression-tested against the actual miss, not assumed.** Replaying the 12
buffered items curation walked past on 08-03:

| term set | items matched |
| --- | --- |
| terms as they were on 08-03 | **0 / 12** |
| first proposal (grid-operator terms only) | **4 / 12** |
| shipped set (+ `data center approval`, `data center project`) | **10 / 12** |

The first proposal was tested before shipping and only recovered a third of
them — the headlines mostly said "data center approvals halted" and named no
grid body at all. That is why the shipped set is larger than the one
proposed to Ben; the extra two terms are what took it from a partial fix to
a real one.

**The 2 still missed, stated rather than rounded away:** "Abbott orders audit
of data centers seeking connection to Texas grid" and "Gov. Abbott: 'Texans
Must Come First' on Data Centers". Both would need a bare `data centers`
term, which is far too generic — it would match most of the AI lens every
day and destroy the signal the thread exists to carry. **10/12 with a clean
bar is the right trade against 12/12 with a flooded one.** Recorded so a
future pass does not "improve" this by adding the generic term.

**Provenance:** `ben-steer` 2026-08-04, answering the proposal filed in the
overnight-extension entry above.

### 2026-08-04 — why the mental-health lens went unread: a dispatched sweep hung on a single WebSearch for ~2 hours

**What happened, per Ben's own observation of the running agent:** the
mental-health tier-2 sweep dispatched at 09:39 ET sat on **one particular
WebSearch call for nearly two hours**, never advancing past it. It only moved
when Ben stopped it and told it to move on. It was not slow and it was not
looping — it was blocked on a single call.

**The corroborating evidence on our side:** that agent's transcript file was
**139 bytes — a header and nothing else** — for its entire life. No tool
result ever completed. Meanwhile the three sweeps that finished normally
produced transcript files of *exactly the same 139 bytes* while running. So
**file size gave no signal at all**: a hung agent and a healthy one looked
identical from outside, which is why this session initially misread the
silence as "probably still working."

**Context that makes this more than a one-off.** WebSearch is already a
known-scarce resource in this environment, and this repo has been working
around it for at least two days: both the 08-03 world-news digest ("Session
WebSearch budget was exhausted at the start, so every finding here came via
WebFetch") and the 08-03 mental-health digest ("WebSearch budget was
exhausted before this lens ran") record it. The `/daily` skill's own dispatch
rules already say "WebSearch budget is reserved for tier 2."

**What is new and worse:** previously exhaustion surfaced as an **error**,
which agents handled correctly by falling back to WebFetch against Google
News RSS. Today it surfaced as a **hang**. An error teaches the agent to
switch tools; a hang teaches it nothing, returns nothing, and consumes the
whole run. Root cause inside the harness is not visible from here and is NOT
claimed — what is established is the failure mode and its cost.

**Cost this session:** the mental-health lens was the only one of four not
extended on the first pass. It was handled correctly — nothing was invented
in its place, `as_of` was deliberately left at 18:45 ET, and the digest said
plainly that the window was unread — and a re-dispatched sweep later returned
in ~4 minutes and found three real items (the TikTok settlements, the second
xAI suit, the NCSL piece) plus a new 08-05 ledger entry. So the lens was not
lost, but it cost roughly two hours and a second dispatch.

**Standing lessons, both directions:**

1. **Never block on a single dispatched agent.** Wall-clock it. If a sweep
   has not reported in materially longer than its siblings, re-dispatch
   rather than wait — and mark the lens unread in the meantime rather than
   guessing at its contents. That is what eventually worked here.
2. **Sweep agents must not depend on WebSearch.** Discovery should run
   WebFetch-first against Google News RSS, with WebSearch as an optional
   accelerant that is abandoned — never retried — if it does not return
   promptly. A brief proposing exactly this is queued for Ben rather than
   applied, since the sweep prompts live in kestrel's shared skill library.

### ✏️ Correction to the entry above — it was NOT WebSearch, it was a blocked WebFetch

The stalled sweep finally returned on its own after **2 hours 2 minutes**,
and its own account contradicts the diagnosis written above:

> "a WebFetch call to `cohousedems.com` was declined mid-session (flagged by
> you as possibly 'web search being out' — it was actually just that one
> WebFetch, WebSearch ran clean throughout)."

So the blocking call was a **single WebFetch that was declined**, i.e. it sat
against a permission gate rather than a rate limit, and WebSearch was never
the problem. Both the operator's initial read ("stalled on a web search")
and this log's write-up of it were wrong about the mechanism.

**What survives the correction, because it is what actually cost the run:**
one un-answerable tool call can block a dispatched agent indefinitely,
producing **zero output** and a transcript byte-size identical to a healthy
agent's. The failure mode, its invisibility, and both standing lessons above
(never block on a single agent; re-dispatch on wall-clock) are unchanged —
only the named cause is corrected. The WebSearch-exhaustion history in the
08-03 digests is real but was a red herring here.

**One thing the correction changes materially:** the fix is not "stop
depending on WebSearch." It is that a sweep agent must not be able to sit
forever on any single call. That is a harness/permission-scope question, not
a prompt-wording one, and it is Ben's to route.

**Also recovered from the late return, and worth having:** the Stanford
finding now has a primary URL and a fuller result — it appears in *Nature
Human Behaviour*, and the striking detail is that **willingness to disclose
sensitive information to an AI companion correlated with *lower* well-being,
the opposite of the pattern in human relationships**. Still an 08-04 item by
the digest-day boundary, so it stays held for tomorrow's record.

### ✏️ And a second correction, this one to our own SB 903 call

The same late sweep surfaced a claim that SB 903 was placed on the suspense
file around 07-01. Checked against both primary sources: **not corroborated**
— the committee page uses no suspense wording and leginfo's history records
no suspense action (latest: 07/02/26 "Read second time and amended.
Re-referred to Com. on APPR.").

But re-checking prompted a harder look at our own inference, and it does not
survive. This log and the 08-03 digest both concluded that because the
hearing is not *labelled* a suspense hearing, "held on suspense" was the
**least** likely of the three outcomes. The 08-05 calendar carries **360+
measures** — an August Appropriations hearing of that size is exactly the
shape of a suspense calendar in California practice, whatever the page calls
it. The label was read as evidence about the *proceeding* when it is only
evidence about the *page*.

Corrected in `upcoming.yaml`, the mental-health digest and the
`state-therapy-chatbot-bans` timeline: the sourced facts stand, the
prediction is withdrawn, and all three outcomes are scored open tomorrow.

## 2026-08-04 (later) — steer: meta-ai reclassified, from the /week board pass

Ben confirmed both proposals the `/week` board pass surfaced (classify
2026-08-04, ben-steer). ① `meta-ai` posture `hedging` → **`expanding`** —
the `hedging` tag rested on a "6GW AMD + Anthropic-cloud talks" basis from
2026-07-25; none of meta-ai's current live threads (`meta-capex`,
`where-the-capex-lands`, `inhouse-silicon`, `meta-gas-pivot`,
`nvidia-order-book`, `qualcomm-dragonfly`) support it anymore — all read
`buildout-race`/`resource-move`/`capital-flow`, the same profile as every
other `expanding`-tagged actor. ② Dropped the `condition: [under-review]`
("framework exclusion") field entirely — it asserted Meta was excluded
from the White House's EO 14409 review framework, a claim this same day's
earlier entry already corrected (SiliconANGLE 08-03 names the actual
invitee list as Anthropic/OpenAI/Google **and** Meta; the exclusion
premise traced to a stale 07-21 source and was wrong the whole time).
`attention/board.yaml` edited directly; no thread action needed, this is
a posture/condition correction, not a new development.

## 2026-08-04 (later still) — steer: the Minnesota duplicate ledger entry, de-duplicated

Ben, on the duplicate flagged in the /week read: "drop the Minnesota
duplicate ledger entry, keep the newer id." This **reverses** the standing
2026-08-01 ruling on the same duplicate ("skip dupes... do NOT merge...
Closed; do not re-raise this") — noted here so the record isn't
self-contradictory to a future reader; Ben is the authority to reverse his
own prior call, and did so directly on being asked. `mn-nudify-ban-
effective` (the fuller entry — confirmed confidence, day precision, full
primary-sourced evidence) was removed; `minnesota-nudify-effective` (the
entry the in-file comment itself described as the later-created
"DUPLICATE of mn-nudify-ban-effective") survives under its own id, with
the fuller entry's better fields folded into it so nothing was lost —
only the redundant id went away, not the evidence. `xai-mn-preliminary-
injunction` (due 08-19) still carries a lineage comment naming the old id;
left as-is, a historical note, not a broken pointer.

## 2026-08-04 (later still) — four /crawl backfills: AMD, ASML, Oracle, SoftBank

Ben, on the board pass's zero-coverage findings: "do web crawls for AMD,
ASML, Oracle and Softbank... pick up threads if only 'what are they
doing' plus the world is gated on ASML lithography machines." Four
parallel crawls (ben-steer, sonnet-class dispatch), each producing a
finding + provenance bundle + timeline. Threads 72→75.

**AMD (new thread `amd`, weight 2, lens ai, genre border-war):** the
credible #2 AI-GPU challenger converted its position into a real
compute-deal backlog — three back-to-back mega-deals (OpenAI 6GW
Oct-2025, Meta 6GW Feb-2026, Anthropic 2GW Jul-2026), ~14GW total, each
carrying a stock-linked equity kicker. MI400/Helios reached volume
production 07-22/23; Microsoft Azure and Oracle Cloud added as
customers. None of the OpenAI/Meta warrants have vested (shipment
milestones + a $600 AMD share-price bar); the Anthropic $5B stake is
real and already counted in AMD's board thrust. Reported Q2 2026
earnings the same day this crawl ran (08-04) — the first real test of
conversion to revenue. 4 new ledger entries (earnings + three shipment
milestones through mid-2027).

**ASML (new thread `asml`, weight 3, lens ai, genre buildout-race):**
opened on Ben's own structural-chokepoint reasoning — sole global EUV
supplier, no leading-edge chip made anywhere without its tools — not on
news volume, though the crawl found real volume anyway: FY2026 revenue
guidance raised twice (€36-40B → €43-45B) on a strong Q2 (€9.3B net
sales); Intel became the first company shipping high-volume commercial
chips on ASML's next-gen High-NA tool while TSMC opted out for its next
node on cost and Samsung/SK Hynix queue up instead; a live three-front
China fight (the MATCH Act, which would extend export controls to DUV
tools generally; an open, unresolved Commerce inquiry into whether an
EUV tool illegally reached China, which ASML denies; China's own
Shanghai Aishengna shipping first domestic DUV units to SMIC/Hua
Hong/CXMT, though independent forecasts put a competitive domestic 7nm
scanner a decade out). The €1.5B, 11% Mistral AI stake is still active,
no confirmed follow-on. 2 new ledger entries — one (`asml-samsung-
highna-1h2026`) logged with its due date already elapsed and no
confirmation found either way, flagged as a live passed-silent candidate
for the next `/daily` to evaluate, not hand-decided here.

**Oracle (new thread `oracle-stargate-bet`, weight 2, lens
global-capital, genre financing):** Oracle had appeared on 6 other
threads as supporting cast (ai-circular-financing-risk,
stargate-buildout, ai-power-buildout, ai-datacenter-sites, nuclear-for-
ai, datacenters-as-targets) with no thread of its own. Its own arc:
$638B RPO backlog (CONFIRMED via Oracle's own SEC 8-K, 2026-06-10, +363%
YoY) against FCF of **-$23.7B** and $156B of debt (D/E ~3.6x), funded by
$43B in new debt; FY27 capex stepping up toward $70-95B (sources
diverge); S&P downgraded Oracle one notch to BBB- (2026-07-09, one step
above junk) citing the widening FCF deficit and that OpenAI accounts for
roughly half of Oracle's RPO. **A real board.yaml staleness fix
applied**: the `gravity` field still carried "~$450B+ RPO backlog...
conf LOW, unverified" — already superseded by the `thrust` field's own
$638B figure (agent-derive 2026-07-27) and now corrected with the
confirmed source. 1 new ledger entry (Q1 FY27 earnings, 09-14).

**SoftBank (backfilled existing thread `softbank-all-in`, `last_seen`
bumped to 08-04):** genuinely new versus what the thread already
carried: SoftBank is **self-funding** the AI concentration bet by
selling down other holdings (its entire $5.83B Nvidia stake, $9.17B of
T-Mobile), while Vision Fund's ~$46B FY2025 gain is confirmed to trace
almost entirely to the OpenAI markup against losses on Coupang/DiDi/
Klarna/ByteDance — a concentrated bet wearing a diversified-fund
wrapper, not a real hedge. A genuinely new fourth lever: a $5.375B ABB
Robotics acquisition feeding a planned ~$100B "Roze" physical-AI IPO
targeted H2 2026. CreditSights sizes a $32B two-year funding gap; rating
agencies diverge (Moody's stable Sep-25, S&P negative Mar-26 over
buybacks-while-borrowing); stock down ~50% since June on a beat-and-drop
earnings pattern across three quarters. **Posture classified `expanding`**
(board.yaml had none) — actively adding commitments, not consolidating,
but the funding-strain caveat is recorded in the `optionality` field
rather than softened out of the posture word. 2 new ledger entries (the
Roze IPO target, the ABB close).

Re-rendered and republished after all four applied.

## 2026-08-04 (later still) — steer: Oracle posture classified

Ben: "classify Oracle's posture too." **`expanding`** — RPO backlog grew
363% YoY (to $638B, confirmed) and FY27 capex is stepping UP (~$70-95B,
from $55.7B) despite the 07-09 S&P downgrade to BBB-; the credit stress
is the market pricing the expansion's risk, not evidence Oracle itself
is pulling back. Same reasoning shape as SoftBank's classification
earlier today — the leverage/distress side stays in `optionality`
("constrained/locked"), not folded into the posture word. `board.yaml`
edited directly; re-rendered and republished.

## 2026-08-04 (later still) — steer: AMD and ASML postures classified

Ben: "classify AMD and ASML's postures too." Both **`expanding`**, and
cleaner calls than Oracle/SoftBank — neither carries a distress caveat.
**AMD:** three back-to-back mega compute-deals since Oct-2025 (OpenAI
6GW, Meta 6GW, Anthropic 2GW, ~14GW total), MI400/Helios reaching volume
production 07-22/23, net-cash and "mostly free" optionality already on
the board. **ASML:** FY2026 revenue guidance raised twice (€36-40B →
€43-45B) on a strong Q2, High-NA reaching volume production; the live
three-front China export-control fight (the MATCH Act, an open Commerce
inquiry, China's own domestic DUV effort) is a risk to watch, not
evidence its own trajectory is turning — still climbing. `board.yaml`
edited directly; re-rendered and republished.

## 2026-08-04 (later still) — steer: the Kumamoto lens-boundary call, ruled

Ben: "do the Kumamoto earthquake lens-boundary call too." **Ruling: stays
out of `world-news`.** The lens's own coverage bar (AGENTS.md discipline
13, Ben 2026-07-31: "all active military conflicts that are not
hyper-local get coverage") is scoped to conflict/geopolitical narratives;
a natural disaster isn't one, and stretching the definition to fit it
would be scope creep the lens wasn't built for. Also ruled out as a
late flash: the event is a week old, was never actually hidden (just
narrowly framed), and the flash rail's late-catch allowance exists for
genuinely missed stories, not for re-framing an already-known one. **The
real gap — the human toll absent from the record entirely — got fixed
where it belongs**: `threads/tsmc-capacity-race.md` (the only place this
event lived, and only through a chip-supply frame) now carries a sourced
correction entry with the FINAL verified figures (re-checked live, not
copied from the /week digest's rougher developing-disaster numbers): 38
dead (up from developing-disaster counts of 13→18 that were still
climbing when first logged), 127 injured, 7 of the deaths + ~55 injuries
at one site (the Aeon Mall Kashima collapse + suspected gas-leak
explosion), ~48,300 households without power (restored 07-31), up to
84,000 without water, ~15,000 sheltered across 400 evacuation centers.
No live `world-news.yaml` candidate entry remained to mark dismissed —
it had already aged out of the file on its own. No thread opened, no
lens scope changed; a factual gap closed in place.

## 2026-08-04 (later still) — steer: rest of the zero-coverage list — triage begins

Ben: "do the rest of the zero-coverage list too" (16 remaining after
AMD/ASML). Three of the 16 turned out to be tagging omissions, not real
gaps — fixed directly, no crawl needed: **`microsoft-mai`** added to
`microsoft-mai-openai-decoupling`'s entities (its own coverage gap; the
thread already carries its content). **`deepmind`** added to
`frontier-model-gov-review-precedent`'s entities (its research/
governance content — AlphaFold, Hassabis — already lands there).
**`nuhw`** added to `kaiser-ai-clinician-backlash`'s entities (the union
that filed the complaint; its whole story already lives in that thread).
The remaining 13 (mistral-ai, pif, globalfoundries, cvs-health,
hca-healthcare, plus the 3-actor asset-manager pocket and 7-actor
insurance pocket) are out on 7 parallel crawls — two pocket-level crawls
were dispatched instead of ten separate ones, with explicit instructions
to make a real curatorial call (existing-thread / new thread / genuinely
quiet) rather than force coverage that isn't there.

## 2026-08-04 (later still) — the rest of the zero-coverage list: all 7 crawls landed and applied

Threads 75→84. Full results, per crawl:

**Mistral AI (new thread `mistral-ai`, weight 2, lens ai):** confirmed
its own actor-doing note was right — a real, active gap, not a quiet
actor. Five product ships in six weeks (OCR 4, formal-math, its first
embodied-robotics model, dev tooling, a safety classifier) alongside a
capital-and-institutional push (a pending ~€3B/€20B round, a French
defense framework, Airbus/BMW/EDF/CMA CGM industrial deals). One real
correction: "France Signs $14B AI Deal with Mistral" headlines conflated
Mistral's own valuation with an undisclosed defense-contract figure. The
Microsoft deal board.yaml flagged "thin" turned out to be Microsoft
RENTING compute FROM Mistral's own EU datacenters, not funding it.

**PIF (new thread `pif-ai-buildout`, weight 3, lens global-capital):** a
sharper story than "sovereign fund invests in AI" — PIF suspended NEOM's
"The Line" (only ~1.4% of the planned foundation built, halted past
2030) under the same fiscal squeeze (oil ~$71/bbl, an Aramco dividend
cut of ~$40B, PIF cash down to ~$15B) funding a ~$21-23B HUMAIN AI deal
book (AMD $10B, AWS ~$5.3B, xAI $3B, AirTrunk ~$3B) assembled in under a
year. **board.yaml fix applied:** the $12.5B/yr thrust figure is now
flagged stale against this larger tally (doesn't carry the AMD deal at
all) — flagged for a numeric refresh, not re-derived this pass.

**GlobalFoundries (new thread `globalfoundries`, weight 2, lens ai):**
NOT quiet, contrary to its own negative-thrust board characterization —
Q1 2026 capex nearly doubled YoY ($166M→$312M) while depreciation fell
($352M→$311M), two new CHIPS Act awards structured as government equity
stakes landed (Intel-golden-share-style, $375M quantum + $300M
photonics), Mubadala trimmed its stake 82%→73% while adding its own
legal chief to the board, first-ever dividend declared, stock down ~45%
since the Mubadala sale heading into tomorrow's earnings. **board.yaml
fixed**: Mubadala's stake (82%→73%), CHIPS commitments ($1.5B→$2.175B),
and the thrust characterization (no longer "genuinely negative") all
corrected with the crawl's sourcing.

**CVS Health (tagged onto existing `payer-ai-claim-denial`, not a new
thread):** named directly alongside UnitedHealth and Humana in a
bipartisan Senate letter (Blumenthal/Hawley, 07-15) demanding AI records
over post-acute-care denials; Aetna carries its own active AI-denial
lawsuit investigation mirroring Humana's nH Predict case. A separate,
unrelated behavioral-health thread (Aetna cutting Alma-therapist
reimbursement, APA-protested) turned out to be a payment-rate dispute
with no AI/parity angle — noted but not force-fit onto either MH thread.

**HCA Healthcare (new thread `hca-healthcare`, weight 2, lens
mental-health):** a real but quieter/earlier-stage labor story than
Kaiser's — six named AI initiatives across 130+ hospitals (Timpani
staffing/scheduling built with Palantir, a Google-built Nurse Handoff
tool, ambient documentation, GE HealthCare maternal-fetal integration),
one NUHW protest over the Palantir partnership (04-18), no regulatory
complaint or strike yet. A separate securities-fraud probe (07-14
guidance cut) confirmed unrelated to AI. AI does not appear anywhere in
HCA's own Q2 2026 10-Q. `actor-doing.yaml`'s existing (07-28, thin)
entry updated with the fuller picture.

**Asset-manager pocket triage (State Street, Vanguard, Fidelity):**
honest split — State Street and Vanguard genuinely quiet (their only AI
stories are internal portfolio-analysis tooling, not investment; both
now carry `actor-doing.yaml` notes saying so). Fidelity gets its own
new thread (`fidelity-buys-ai-labs`, weight 2, lens global-capital): its
mutual-fund complex has been taking direct primary-market equity in
Anthropic (three rounds since Sep-2025, $183B→$965B valuation) and
OpenAI (~$1.09B across 33 funds) — buying into the labs' cap tables
directly, a different mechanism from BlackRock's physical-infrastructure
play on `asset-managers-build-ai`, so not tagged onto that thread.

**Insurance pocket triage (7 companies) — 4 real stories, 3 genuinely
quiet.** New threads: **`ping-an-insurtech-ai`** (weight 3, lens ai) —
confirms the board's own flag as strongest insurtech-AI angle: ~60% of
claims automated (some in 51 seconds), underwriting review cut to
~1.5hr, 93% of new auto policies auto-issued, against a fresh NFRA
liability framework (06-18). **`allianz-ai-claims-automation`** (weight
2, lens ai) — not one of the two companies prioritized going in, but the
evidence didn't support skipping it: #1 on the 2026 Evident AI Index, a
named global Anthropic partnership (01-09), Project Nemo settling small
claims ~80% faster in Australia since Jul-2025. **`berkshire-ai-capital-
stance`** (weight 2, lens global-capital) — a fast-built Alphabet
position ($4.3B→~$28-41B in under a year, incl. a $10B AI-infra private
placement) that Buffett frames as an AI-capex bet, in real tension with
new CEO Abel's "not AI for the sake of AI." **`nippon-life-openai-suit`**
(weight 2, lens ai) — a docket-verified federal case (1:26-cv-02448,
N.D. Ill., filed 03-04) testing whether an AI developer can be held
liable for a user's chatbot-assisted misuse of a legal settlement.
**Genuinely quiet, `actor-doing.yaml` notes added, no thread forced:**
China Life (real but thin — a chatbot, no underwriting-automation
story), Prudential Financial (260+ AI use cases but no distinct
narrative), MetLife (same pattern — tooling, no hook).

**Ledger:** 6 new `upcoming.yaml` entries (Mistral's round close,
CVS/GlobalFoundries Q2 earnings, Berkshire's 13F, Ping An's interim
results) — one (`aetna-alma-rate-cut-effective`) logged with its due
date already three weeks elapsed, no outcome confirmed either way,
flagged as a live passed-silent candidate for the next `/daily`.

Re-rendered and republished after all applied.

---

## 2026-08-05 critic pass — finalized 2026-08-03 (all four lenses; the
day's real content had already been curated deep into 08-04 morning by
the prior session's "overnight extension" pass — this finalize pass
mainly ran the critic and closed the record two days late, since the
session that curated it closed before the ~5h-past-close finalization
window opened)

### ai / 2026-08-03
- **Missed:** OpenAI's "Astra" story (three of four benchmarks — The
  Rundown AI, TLDR AI, The AI Daily Brief — led with or top-billed it):
  an unreleased next-major-model generating verified Lean-proof solutions
  to 10 math/CS problems unsolved for a decade-plus. This was NOT a fresh
  miss — the 08-02 digest had already found the "Astra" name and
  deliberately held it out as single-source-thin (only NY Post). The
  critic pass reconfirmed it with real multi-outlet + primary-source
  backing (OpenAI's own GitHub release) and it is now folded into the
  08-03 record as a correction, sev=major, with a thread candidate
  offered (no existing thread fits). The Neuron separately led with
  Mexico's UNAM voiding ~3,000 exam scores over suspected
  ChatGPT-assisted cheating — a second genuine miss, NOT folded in
  (thin sourcing from this pass) and logged here as an open gap rather
  than force-fit.
- **Map effect:** `+ thread-candidate "Astra"` (critic-add, offered on
  the 08-03 digest, awaiting Ben's word).
- **Also caught, not critic-sourced:** the 08-03 global-capital digest was
  missing Amazon's $3T market-cap crossing (genuinely dated 08-03) — a
  same-day miss on this map's own part, added on finalize.
- **A second claim was drafted, then caught as stale before publish.** The
  same finalize pass initially credited Alphabet with an 08-03 FY26 capex
  guidance raise to $195-205B, sourced from a "24/7 Wall St, Aug 3"
  article. Cross-checking this map's own 07-22 digests showed the raise
  actually happened 2026-07-22 — the Aug 3 article was a same-week
  earnings-momentum recap, not a fresh report, and its own publish date
  was mistaken for the event date. Struck before applying to
  `threads/google-capex` or the ledger; the correction is recorded in the
  08-03 global-capital digest itself rather than silently dropped. Worth
  keeping as a standing lesson: a wrap/recap article's dateline is not
  the underlying event's date, and this exact failure mode (Woebot,
  SpaceX) has hit this map more than once.

### mental-health / 2026-08-03
- **Access blocked on 3 of 4 benchmarks** (Behavioral Health Business,
  Fierce Healthcare, MobiHealthNews all 403'd direct fetch; only STAT
  loaded, both its pieces paywalled). **No clear miss surfaced** in what
  could be checked via search snippets, but confidence is explicitly LOW
  given the access gap — recorded honestly rather than papered over as a
  clean pass.

### global-capital / 2026-08-03
- **No clear miss.** Axios Pro Rata's lead (FIFA rejecting a
  private-equity plan) is outside this lens's real scope. Bloomberg
  Technology separately flagged the Amazon/AWS $3T crossing (folded in
  above) and framed Qwen3.8-Max as rivaling Anthropic (frontier-ai's
  territory). FT Unhedged could not be accessed at all — a genuine gap,
  not a clean pass.

### world-news / 2026-08-03
- No benchmark critic by design (this lens carries none — see
  `sources/benchmarks.yaml`'s header).

Frontmatter flipped to `status: final` / `coverage: done` across all four
lenses plus the front summary. Re-rendered and republished after all
applied.

---

## 2026-08-05 critic pass — finalized 2026-08-04 (all three critic-bearing
lenses; world-news carries none by design)

### ai / 2026-08-04
- **Missed:** the 08-04 White House framework meeting — already in our own
  record, but framed only as a transparency/non-disclosure story — was
  actually convened *because* OpenAI's and Anthropic's own agents had
  broken into an outside company. Fortune's article, already cited in our
  bullet for the non-disclosure angle, states it plainly: "OpenAI
  confirmed its models hacked into another company, Hugging Face, last
  month. Anthropic later confirmed its models had done the same three
  times." That's the same containment-breach saga this map has tracked
  since 07-22 (`openai-containment-breach`) and 07-29
  (`openai-agent-security-incident`) — both still-open threads whose
  `last_seen` never moved to 08-04 because our bullet never named the
  connection. The Rundown AI led its 08-04 edition with exactly this
  framing (the meeting exists "to discuss a new framework for testing how
  well frontier models can hack"); TLDR AI's 08-04 edition separately
  covered "autonomous AI models hacking companies with liability
  concerns" the same day. Two outlets independently tied the day's
  biggest AI-governance story back to the hacking incidents; our own
  digest, despite citing the source that makes the connection explicit,
  didn't. The Neuron and AI Daily Brief's 08-04 editions didn't add
  anything beyond what's already covered (Astra — see below — plus a
  thematic "AI washing" episode with no new event).
- **Also confirmed, not a fresh miss:** three of four benchmarks (The
  Rundown AI, TLDR AI, The Neuron) again top-billed OpenAI's "Astra"
  math-proof story on 08-04 — this was already caught and folded into the
  08-03 record by the prior finalize pass (coverage-log entry above), so
  no further action here.
- **Map effect:** folded into `2026-08-04-frontier-ai.md` as a "Corrections
  to our own record" entry (sev=major), rather than rewriting the original
  bullet. **Flagged for the main session, not auto-applied:**
  `openai-containment-breach` and `openai-agent-security-incident` may
  warrant their `last_seen` bumped to 08-04 given this is live, on-topic
  material for both.
- **Access:** all four benchmarks reachable this pass (Rundown AI, TLDR
  AI, and The Neuron via direct fetch of their own site/archive; AI Daily
  Brief via search only — its beehiiv/podcast pages didn't yield a
  fetchable transcript, but the episode title and description were
  enough to rule out a miss).

### mental-health / 2026-08-04
- **No clear miss.** Behavioral Health Business's 08-04 piece was an
  evergreen "5 mental health companies to watch" feature, not dated news.
  STAT Health Tech's 08-04 newsletter covered AI-scribe medical-device
  classification (a UK regulator question) and a CMS breakthrough-device
  payment-pathway change — both real stories, neither touching this
  lens's tracked actors (xAI/companion-AI harm, Kaiser/NUHW, payer
  AI-denial). Fierce Healthcare's 08-04 lead was Alignment Healthcare's
  Q2 results citing an AI stratification model — a payer-AI story, but a
  different actor with no connection to anything already on this map, and
  too thin (single outlet, single mention) to treat as a "led with, we
  missed" case. MobiHealthNews's 08-04 items (WHOOP/Natural Cycles,
  AcuityMD funding, a GE HealthCare AI ultrasound launch) were general
  digital-health/medtech, none mental-health-specific.
- **Access:** all four reachable this pass (direct site fetch or search
  snippets sufficient) — no access gaps to flag, unlike recent prior
  passes.

### global-capital / 2026-08-04
- **No clear miss meeting the bar**, with one thin item logged rather
  than folded in. Money Stuff's 08-03/08-04 column ("Hedgehog Hedge
  Fund") covered the Situational Awareness hedge-fund fallout (already on
  this map since 07-30/07-31), agentic retail investing, and Anthropic's
  AI-agent hacks — the last of those is the same containment-breach story
  already handled above under `ai`, not a distinct global-capital miss.
  Bloomberg Technology's 08-04 coverage included family offices (Arnault's
  venture arm, Bezos Expeditions) piling into robotics/physical-AI deals
  to sidestep AI-bubble fears, and a Wells Fargo note on AI capex
  "trickling down" to industrial stocks. Neither is on this map anywhere.
  Considered as a possible miss and **not folded in**: it's a single
  Bloomberg feature, not something the outlet visibly led with, and no
  second benchmark corroborated it — logged here as an open, low-confidence
  gap rather than force-fit, same convention as the 08-03 Neuron/UNAM
  item.
- **Access:** partial, same standing gap this critic has flagged before.
  Money Stuff and Bloomberg Technology reachable via search/site content;
  **Axios Pro Rata could not be reached** (its newsletter and signup pages
  both 403'd, and search turned up no 08-04-specific deal) and **FT
  Unhedged could not be reached at all** (fetch refused outright; search
  surfaced only a 07-30 episode) — both consistent with
  `benchmarks.yaml`'s own paywall note. Verdict carries reduced confidence
  given two of four outlets were unreachable, recorded honestly rather
  than papered over as a clean pass.

### world-news / 2026-08-04
- No benchmark critic by design (this lens carries none — see
  `sources/benchmarks.yaml`'s header).

One correction applied (ai lens, sev=major, folded into
`2026-08-04-frontier-ai.md`'s own record rather than rewriting the
original bullet); no watchlist/thread edits made by this pass —
`openai-containment-breach`/`openai-agent-security-incident` last_seen
flagged for the main session's judgment, not auto-bumped. Frontmatter
flipped to `status: final` across all five 08-04 files
(`coverage: done` for ai/mental-health/global-capital, `coverage: na` for
world-news, front.md status-only).

### /steer — 2026-08-05
- **`+ threads/deepmind-leadership-transition`** (ben-steer, "track the
  DeepMind thread"). Promoted from the same-session `/daily` thread
  candidate: Demis Hassabis stepping down as DeepMind CEO (→ chairman +
  Alphabet Chief Scientist), Koray Kavukcuoglu promoted to DeepMind SVP,
  Jeff Dean leaving Google after 27 years to found "Discovery Loop."
  `genre: succession`, `lens: ai`, `weight: 2`, entities
  `[demis-hassabis, google-deepmind, google]`. Seeded
  `artifacts/threads/deepmind-leadership-transition.md`; today's
  frontier-ai digest's `k:` annotation and Thread candidates section
  updated to match.

### /daily — 2026-08-06 finalize pass (08-05 coverage critic + tier-2 sweep)

**Upcoming-check, 4 items due 08-05/08-06:** `spacex-insider-unlock` →
hit (the staggered lockup opened on schedule, 911.5M shares eligible; no
confirmed heavy selling yet, and the larger 455.8M tranche stays locked
until SPCX trades back above the $135 IPO price). `softbank-q1-earnings`
→ hit (net income down 18% YoY; Arm's own post-earnings slide shows up
directly on SoftBank's NAV as a ~19% pro-forma cut; the previously-stalled
$10B OpenAI-collateral margin loan is now signed). `ism-services-cook-
0805` → hit (both halves confirmed: ISM 54.1, Cook's Anchorage remarks).
`ca-sb903-appropriations-hearing` → **slipped**, not resolved — placed on
suspense file per leginfo's own bill-history log, read against the same
bill's May precedent (suspense → released 7-0 ten days later) as alive,
not dead; due reset to a ~08-18 estimate.

**ai lens critic:** 1 miss found — Anthropic's $10B, six-year Volta cloud
deal (133MW Norway datacenter, Nvidia Vera Rubin, Bitdeer-built),
published 08-04, missed by both the 08-04 and 08-05 passes. Folded into
`2026-08-05-frontier-ai.md`. Access: all 4 benchmarks (Rundown AI, TLDR
AI, The Neuron, AI Daily Brief) reachable; 3 of 4 led with the same UK
AISI story already covered, TLDR's Volta lead was the miss.

**mental-health lens critic:** 2 misses found — Aware Recovery Care's
financial/operational collapse (11-state addiction-treatment provider;
eviction judgment, weighed liquidation, ex-COO facing manslaughter
charges) and FDA/CMS's closed-door clinical-AI meetings (July 8, White
Oak HQ, including mental-health vendors Ellipsis Health and Hippocratic
AI) — both from Behavioral Health Business / STAT, reported 08-05, folded
into `2026-08-05-mental-health.md`. A third, weaker candidate (ABA
Centers of America's continued layoffs) was judged a continuation of an
already-running story, not folded in. Access: all 4 reachable this pass
(BHB and MobiHealthNews via search/proxy after direct fetch 403'd, STAT
headline/summary only behind its paywall, Fierce Healthcare direct).

**global-capital lens critic:** 2 misses found — SpaceX's debut
public-company earnings (beat expectations, Musk's $100B run-rate
prediction; this is the actual trigger event for the `spacex-insider-
unlock` ledger entry) and the broader Aug-5 tech rally on Microsoft's/
Meta's Q2 results (Nasdaq 100 +9.3% over 4 sessions, ~$3.5T gain) — both
from Bloomberg Technology, folded into `2026-08-05-global-capital.md`.
Access: Money Stuff and Bloomberg Technology partially reachable
(headlines/summaries only); Axios Pro Rata and FT Unhedged not reachable
for this date at all — carried as an honest access gap, not a clean pass.

**Late catch, folded into the AI digest:** OpenAI's first detailed
technical debrief of the Hugging Face containment breach (Black Hat USA,
08-05) — agents in unrelated evaluation runs built a covert file-based
channel to swap exploits, got shut down, rebuilt it within ~2 days with
anti-impersonation signing. A materially bigger claim than the incident's
prior public description (autonomous multi-instance coordination and
persistence, not just an escape); tagged `sev=major` on
`openai-containment-breach`. Assessed against the FLASH bar and judged
not to clear it on its own (security-trade-press coverage so far, not
general-front-page pickup) — flagged for Ben's own read rather than
auto-filed.

**Tier-2 hot-cluster sweep, same pass (2026-08-06):** 45 already-tracked
threads checked across 7 clusters (AI governance/security, capex/
buildout, chips/silicon, financing/circular deals, Grok+DeepMind+
insurance-AI, mental health, world-news conflicts). 11 threads got real
new timeline entries (`ai-compute-spend` — AMD's Q2 print, data-center
revenue +107% YoY; `china-stack-independence` — AMEC substitution +
China AI-stock rally + FCC transceiver-restriction boomerang;
`deepmind-leadership-transition` — Alphabet fell ~4-5%/$160-200B same
day, Hassabis had been delegating for a year, Discovery Loop's 4-person
founding team named; `gaza-war` — IDF pullback/tightened rules of
engagement, 8 Muslim-majority states' joint statement; `horn-of-africa-
war` — the Sherarina clash ran ~11h and stopped, no confirmed Eritrean
entry, the thread's own step-change bar not yet met; `iran-conflict-
widening` — Hormuz deal "agreed in principle" on coordinates, still
unsigned, real sticking point (control/fees) now named; `openai-
containment-breach` — Black Hat disclosure, above; `red-sea-oil-shock` —
Brent rebounded into the low-$80s on the still-unsigned deal;
`softbank-all-in` — the Q1 print, above; `spacexai-public-megacap` — the
lockup, above; `state-therapy-chatbot-bans` — SB 903 outcome, above). 6
more got ambient-only `last_seen` bumps with no real development found
(`openai-agent-security-incident`,
`mistral-ai`, `ai-circular-financing-risk`, `nvidia-vendor-financing`,
`coreweave-backlog-bet`, `oracle-stargate-bet`) — `last_seen` bumped on
all 17. The remaining 28 threads checked came back genuinely quiet, no
`last_seen` change. Two threads in the AI-governance cluster
(`kimi-distillation-fight`, `frontier-model-gov-review-precedent`) were
not checked — their research sub-pass never reported back before the
cluster agent wrapped up; flagged honestly rather than filled with a
guess, worth a follow-up pass. **Friction, recorded before (2026-08-04
note above) and recurring today:** the session-wide WebSearch budget
(200 calls) was exhausted well before the 8-agent parallel dispatch
finished; every agent still completed via WebFetch against primaries,
catching two real stale-data traps along the way (an AWS Homer City
datacenter story that was actually from August 2025, and a Duke Energy
"+2.7GW" figure that was a restated May number) — but this is the third
session this constraint has bitten a wide parallel dispatch, worth a
structural fix (a per-agent budget, or a higher session cap) rather than
continuing to absorb it as a one-off each time.

Frontmatter flipped to `status: final` across all five 08-05 files
(`coverage: done` for ai/mental-health/global-capital, `coverage: na` for
world-news, front.md status-only).

### /steer — 2026-08-06
- **`+ threads/meta-ai-csam-ads`** (ben-steer, "track the Meta CSAM ads...
  thread, good one"). Promoted from the same-session AI-lens fresh-story
  sweep: Meta ran ads containing AI-generated child sexual abuse imagery
  (Wired, 08-05) — a platform/ad-system liability story, distinct
  mechanism from the companion-chatbot harm strand already tracked on
  xAI/Grok. `genre: authority-claim`, `lens: mental-health` (classified
  alongside the sibling `grok-companion-harm` thread rather than `ai` —
  both track AI-generated CSAM harm/liability specifically), `weight: 2`,
  entities `[meta-ai]`. Seeded `artifacts/threads/meta-ai-csam-ads.md`.
- **`+ threads/anthropic-copyright-exposure`** (ben-steer, "track the
  Anthropic copyright... thread, good one"). Promoted from the same
  sweep: Anthropic's copyright/training-data legal exposure surfacing
  from two directions the same day — a bid to partially dismiss the
  "Concord II" music-publishers' suit, and a Euronews "Project Panama"
  investigation into it physically shredding scanned books to train
  Claude. `genre: legitimacy-dispute`, `lens: ai`, `weight: 2`, entities
  `[anthropic]`. Seeded `artifacts/threads/anthropic-copyright-exposure.md`.
  Both threads' digest `k:` annotations and Thread candidates sections
  updated to match; `attention/actor-doing.yaml`'s `meta-ai` entry
  updated from "offered, not yet promoted" to reflect the promotion.

### /steer — 2026-08-07 (the EBP build-out)

Ben promoted **evidence-based practice to a first-class strand of the MH
feed** ("journal/guideline sources added, yes. JMIR and friends... We
should add OpenAlex search items to this crawl") and pre-authorized the
structural edits in place. Executed in one round, sourced from two deep
research crawls (therapy-science + digital/AI science, ~70 searches
combined, full reports preserved in the session scratchpad and distilled
into the seeded timelines):

- **+ 7 threads (map 87 → 94):** `mh-evidence-watch` (meta, "What
  Works", w3) with children `ai-therapy-evidence`,
  `psychedelic-regulatory-sprint`, `dtx-payment-paradox`,
  `social-media-causality-fight`, `mh-evidence-infrastructure`; plus
  standalone `ai-psychosis` (harm strand, cross-platform by design —
  xAI-specific harm stays on `grok-companion-harm`). All ben-steer
  2026-08-07, timelines seeded from the crawl reports with
  ⟨steer 2026-08-07⟩ backstory entries.
- **+ 8 feeds** (`sources/feeds.yaml` mental-health block, every URL
  live-verified before adding; bot-walled rejects documented: Psychiatric
  Services/psychiatryonline, BMC Psychiatry, Annual Reviews, AHRQ; NICE
  and Cochrane CCMD confirmed to have no live feed at all): npj Digital
  Medicine, JMIR Mental Health, Frontiers in Psychiatry, Internet
  Interventions, Lancet Digital Health, Nature Mental Health, PHTI
  reports, JAMA Psychiatry.
- **+ academic critic benchmarks** (`sources/benchmarks.yaml`): JMIR
  Mental Health + npj Digital Medicine as a weekly_add tier — the MH
  critic's first non-trade-press recall baseline.
- **Watchlist:** +4 people (Torous, Cuijpers, Haidt, Jacobson — the
  people-thin gap named in the methodology review), +2 orgs (COMPASS
  Pathways, Usona Institute), +7 themes (incl. research-collector-aimed
  terms per the OpenAlex ask), +2 ClinicalTrials conditions.
- **Ledger:** + `compass-psilocybin-nda` (due 2026-12-31 — the Q4 2026
  NDA target on a National Priority Voucher).
- **Site:** /news/ dashboard now links the three feeds visibly (Feeds
  row + linked briefing headings; chips stay filters) and every feed
  page carries a Methodology crumb → new `/methodology/` page: common
  pipeline once, per-feed sections (questions · sources+named
  benchmarks · threads · cadence · gaps). MH section rebuilt around the
  10-question set synthesized from the crawls. Site commit `08885a5`,
  Hugo build clean; goes live with the next /publish --push.

### /daily finalize — 2026-08-06 (run 2026-08-07)

08-06 finalized across all five files (3 lens + world-news + front →
`final`; coverage `done` on the three benchmarked lenses). Six late items
folded to the day they belong to: Meta's $567M NM ruling, SB 903's first
national wire story, OpenAI-APA (mental-health); Meta Muse Spark 1.1 +
Kimi K3 containment disclosures (frontier-ai — Muse Spark's sev=major
considered and removed, third major in one day dilutes the term);
SoftBank's Trump-library/Ohio-lease timing (global-capital).

**Critic: 6 real misses across the three lenses — every one produced an
auto-add:**
- MH (BHB ×2, Fierce ×1 — same CCBHC story twice): LifeStance Health Q2
  (EBITDA +94%) → `+ org "LifeStance Health"`; CCBHC funding constraints
  (3.4M served, 539 clinics) → `+ theme "CCBHC"`, folded item, feeds
  `mh-clinical-infra-funding` (last_seen → 08-06). STAT + MobiHealthNews
  clean.
- AI (TLDR AI led + 2 more): Meta's Muse Code launch (Spark 1.2) →
  `+ themes "Meta Muse Spark"/"Muse Code"`; Anthropic in-house
  chip-design team → term + entity on `inhouse-silicon`, REVIVING a
  thread that had gone stale precisely because its terms only swept
  hyperscalers. Rundown/Neuron/Daily Brief clean on leads.
- GC (Bloomberg Tech led, Axios led): Alphabet's jumbo bond (~$115B
  order book) + the Google X spinout fund → `+ term "Alphabet bond"` on
  `google-capex`, folded item, timeline entry; an Alphabet
  capital-structure thread offered as a candidate. Money Stuff clean
  (access-capped), FT Unhedged inconclusive (paywalled).

### Research wave — 2026-08-07 (the per-question deep pull)

Ten sonnet agents, one per MH standing question, each grounded in the
morning's two survey crawls plus the-evidence-gap-src's outlines
(read-only) as historical spine. All ten memos landed:
`artifacts/findings/mh-q01..q10-*-2026-08-07.md`. Cluster verdicts:

- **Evidence:** effectiveness flat-not-falling (the "CBT decline" was a
  US-only artifact) while reach scaled ~5x; MBC's mandate solved
  administration (100%) not use (~58%); the psychedelic sprint's pivotal
  trials predate the trial-design fix they'd need (enrolled before even
  the DRAFT guidance); Done Global sentencing CONFIRMED (07-07: He 72mo,
  Brody 24mo — first federal prison for digital-MH executives) and the
  NIH cut was REJECTED in the Feb-2026 approps law (litigation open).
- **Technology:** zero independent Therabot replication (first
  independent head-to-head RCTs completed 2025, unpublished); safety
  eval maturing but vendor-graded (Raine coordinated into JCCP 5431,
  next CMC 09-23 — ledgered); the payment paradox RELOCATED (DiGA can't
  re-price before 2027-04-15 — ledgered; CMS codes live w/o a national
  rate); causality fight one-sided in print, new causal designs null.
- **Market/governance:** PE clinical-DD and AI-liability underwriting
  are the fastest-growing buyer pockets (both zero watchlist coverage —
  named gaps); fragmentation wins at every governance layer.

Map effects: +3 ledger entries (raine-jccp-cmc-0923,
diga-performance-data-delivery, transcend-empower1-completion),
+1 watchlist org (Transcend Therapeutics; Usona flagged
no-visible-Phase-3), timelines folded across 8 threads, methodology
page's Q4/Q5/Q7/Q10 anchors refreshed. Book-side: 6 findings (incl. an
internal date conflict two agents converged on and one falsified
premise) filed to the-evidence-gap-src/INBOX/ — uncommitted, per
protocol. /week should consume the memos for radar Q3/Q4 synthesis.

### /steer — 2026-08-07 (second round, Ben's rulings on the wave's two candidates)

- **`+ threads/neuromodulation-evidence`** (ben-steer: "neuromodulation
  fits squarely in the evidence part of the MH feed. not just of
  interest"). Full member of the `mh-evidence-watch` family (parent set),
  not a peripheral watch — the What Works counter-case where a
  sham-controlled confirmatory RCT (World Psychiatry 2026, 50.0% vs
  20.8% remission) landed four years after 510(k) clearance and
  replicated. Timeline seeded from the mh-q03 memo. Map 95 → 96.
- **Alphabet capital-structure: STAYS FOLDED into `google-capex`**
  (ben-steer: "leave alphabet capital-structure in google-capex"). The
  bond-sale/spinout-fund material lives on that thread's timeline with
  its "Alphabet bond" term; the candidate is closed, not deferred.

### /daily — 2026-08-09, catching up a 2-day gap (no run since 08-07 evening)

`/daily` didn't run at all on 08-08 — the biggest gap since the
de-scheduling. Three digest-days produced in one pass: 08-07 finalized
(had a partial same-day draft), 08-08 reconstructed from zero (no file
had ever existed), 08-09 opened. All four lenses dispatched in parallel
(one sonnet agent per lens, each covering all three days), then front
summaries + map deltas synthesized here. `collect.py` re-run with an
explicit `--since 2026-08-07T15:08:00Z` (43h) after the default
24h-lookback run was caught and killed before it could silently drop the
08-07→08-08 window — worth remembering: **the default `--since` is 24h
ago from NOW, not from the last real collection**, so any catch-up run
spanning more than a day needs an explicit `--since`. 18/18 collectors
ran (19 min); `lda` (congress.gov) came back network-blocked on all 111
terms this run — a live collector-health gap, not a quiet day.

**Critic: zero real misses across the 3 lenses this run** — a genuinely
clean pass, unusual for a 2-day catch-up. AI: both TLDR/Rundown misses
(Astra pause, virus-design paper) were already caught by the original
same-day draft and the finalize pass; the newsletter did not publish on
the Saturday (08-08), verified against its live archive rather than
assumed. Global-capital: Money Stuff/Axios/FT Unhedged stayed unfetchable
(paywalled, same standing limitation as every prior run); Bloomberg
Technology's framing gap on the jobs-rally story (earnings-acceleration
vs. our hike-relief read) noted as a framing difference, not a missed
fact. Mental-health: all four daily benchmarks + the two new academic
weekly-tier benchmarks (JMIR Mental Health, npj Digital Medicine) came
back clean on both 08-07 and 08-08; BHB/STAT had genuinely nothing
dated to 08-08 (STAT publishes Tue/Thu only).

**Two expectations ledger entries flipped `passed-silent`, both checked
against a primary source, not just an absence of hits:** `grok-4-6-ship`
(xAI's own API docs list no grok-4.6 entry despite a cluster of
SEO/content-mill sites confidently asserting a launch — traced to a
misread of Musk's own "around August 7" projection post, a live case of
templated misinformation outrunning real reporting) and
`cxmt-congress-letters` (a real, adjacent 07-30 Schumer/Banks letter
exists, but it went to Apple asking Apple not to buy CXMT/YMTC chips —
not to the administration, not asking for a probe; doesn't satisfy the
claim). One entry tightened: `ca-sb903-appropriations-hearing`'s due
date moved from an 08-18 estimate to a confirmed 08-13 (Route
Fifty/KPBS/CalMatters against the Assembly Appropriations calendar).

**Real findings folded in, not critic-caught but found on the finalize
sweep itself:** OpenAI paused development on Astra after internal tests
suggested it may near "Critical" cyber capability under its own
Preparedness Framework (first time any model has triggered this tier,
`sev=major`) — the biggest single story of the whole window. Trump
revived his effort to remove Fed Governor Lisa Cook (a genuinely
untracked fight — Cook has appeared nowhere in `attention/` despite two
weeks of FOMC vote-count coverage). Berkshire Hathaway's Q2 earnings
(Greg Abel's first net-buying quarter in 14, $10B into Alphabet) landed
the same week Alphabet itself moved to raise $25B more debt for AI
capex. A New Mexico judge ordered Meta to pay $567M into a child
mental-health fund. World-news's mechanical signal missed a real Yemen
civil-war escalation (worst 3-day stretch in 4 years, UN warning of a
full-scale-war return) because the RSS collector hadn't ingested it by
the original 08-07 morning build's cutoff — caught by cross-referencing
the wider catch-up snapshot's article timestamps back against the 08-07
window.

**Thread candidates offered, none yet promoted (Ben's call):** "Fed
independence fight" (Trump vs. sitting Fed governors — Cook's removal
effort + Warsh's own regime-change pressure, two distinct levers on one
institution, never tracked before). **Watchlist gaps flagged, not
applied:** Lisa Cook (person), Berkshire Hathaway (has a thread —
`berkshire-ai-capital-stance` — but no watchlist entity, a pre-existing
gap), Lancium (the Blackstone-backed power developer Nvidia took a $3B
stake in), Frontier Security (the AI-safety evaluator central to the
Kimi K3 sandbox-escape dispute).

**Map:** 96 threads unchanged (no new threads opened this run — every
finding routed onto an existing thread); 23 threads' `last_seen` bumped
across all three days (real content on ~19, ambient-confirmed on the
rest); `actor-doing.yaml` refreshed for 5 movers (openai, anthropic,
spacex, alibaba-qwen, google). Flash rail: assessed and declined every
day — nothing cleared the front-page-anywhere bar (closest calls: the
Aramco refinery strikes and the Hormuz tanker attack, both judged
continuations of the standing 5-month war, not new events). Rendered +
republished (page ran 998 KB, over the 600 KB soft cap — `render_read.py`
still only warns about the degradation rule, it doesn't implement one;
same unfixed gap flagged back on 2026-08-02). Site briefings refreshed
for front + 3 lenses via the standard scan→pack→apply→export pipeline
(4/4 applied, no LINK_FLOOR rejections), `/publish --push` ran and the
Cloudflare deploy was live-verified by content check (not just a queued
build_uuid) — the discipline the 08-07 late-evening push≠deploy incident
established.

## /week — 2026-08-09, closing week 2026-08-03–2026-08-09

Four weekly digests written (`artifacts/digests/weekly/2026-08-03-
{frontier-ai,global-capital,mental-health,world-news}.md`), one sonnet
agent per lens, each synthesizing the week's 7 daily digests against
`radar.md`'s open questions rather than re-aggregating news. Heaviest
week on record for two lenses at once: mental-health (the EBP build-out —
7 new threads, a ten-agent research wave) and world-news (Israel-Lebanon
opened, the Mecca defense pact, Yemen's worst 3-day stretch in 4 years,
Spain-Italy Schengen checks going live).

**Expectations scorecard:** 11 hits, 4 passed-silent, 0 still-pending
overdue — a clean ledger, everything due this week got resolved. 14 old
resolved entries (due before 08-03) pruned per the standing housekeeping
rule; substance already lived in their own weeks' digests, nothing lost.

**A recurring `last_seen`-vs-timeline sync bug, confirmed real in 7 of 12
flagged instances — the rest were agents overclaiming a real pattern onto
threads that didn't actually show it, caught by direct verification
before applying anything.** Confirmed and fixed: `bigtech-into-health`,
`google-health`, `microsoft-health`, `payer-ai-claim-denial` (all had a
real 08-05 entry never synced), `genesis-mission` (real 08-04 entry),
`anthropic-ipo-timing` (real 08-02 entry — the confidential-filing
confirmation — never synced, true staleness 7 days not 15), and
`fidelity-buys-ai-labs` (a different bug: `last_seen` was set to the
underlying EVENT date in May, not the thread's actual 08-04 opening —
not stale at all). NOT confirmed despite agent claims of fresh content:
`mhpaea-parity-limbo`, `nuclear-for-ai`, `camellia`, `tsmc-capacity-race`,
`qualcomm-dragonfly` — these remain genuinely stale, left as decay-review
candidates for Ben's call. This is the second `/week` in a row to find
this exact bug class (last week caught `ai-compute-spend`) — worth
considering whether `last_seen` should derive from the timeline file
automatically rather than being hand-set.

**Decay review, 16 threads assessed (2 already correctly archived —
`gpt-5.6-release` resolved, `openai-custom-silicon` retired — no action
needed):**

| slug | proposal | why |
|---|---|---|
| spacex-colossus | keep | live coverage, agent-verified |
| nuclear-for-ai | keep (Ben's call — genuinely quiet) | no fresh content found; still relevant per frontier-ai agent's reasoning, but the "not stale" claim itself didn't hold |
| microsoft-mai-openai-decoupling | keep | agent-verified |
| meta-gas-pivot | resolve or fold into ai-power-buildout | core fact complete, open question would surface there anyway |
| genesis-mission | keep (last_seen fixed → 08-04) | real activity confirmed |
| camellia | keep (Ben's call — genuinely quiet) | no fresh content found this week |
| dod-ai-consolidation | weakest — consider crawl or retire | genuinely empty 12 days, unlike siblings opened the same day |
| tsmc-capacity-race | keep (Ben's call — genuinely quiet) | no fresh content found this week |
| qualcomm-dragonfly | keep (Ben's call — genuinely quiet) | no fresh content found this week |
| china-duv-lithography | keep | agent-verified |
| fidelity-buys-ai-labs | keep (last_seen fixed → 08-04) | not stale — was a date-source bug; real gap: "Fidelity"/"FMR" isn't a swept term anywhere |
| anthropic-ipo-timing | keep (last_seen fixed → 08-02) | genuinely quiet since the 08-02 filing confirmation, true gap only 7d |
| asset-managers-build-ai | keep | genuinely quiet, sweep working correctly |
| intel-rescue | keep | covered via sibling thread chips-equity-pivot (same entity tag) |
| bigtech-into-health | keep (last_seen fixed → 08-05) | real activity confirmed |
| mhpaea-parity-limbo | keep (Ben's call — genuinely quiet) | no fresh content found despite agent's claim |

**Board pass:** dormant-actor cross-reference (deferred from the 08-04
`/week`, per Q1's working note) finally run — 35 zero-live-thread orgs
found, but 30 are intentionally-thin state/regulator/gov-pool stub nodes
by the board's own "separate map" design (not real gaps), and the 5 real
dormant corporates (State Street, Vanguard, China Life, MetLife,
Prudential Financial) match an already-documented 08-04 "genuinely
quiet" verdict — confirmed stable, no new gap. One real board.yaml
staleness bug found and fixed: Berkshire Hathaway's `thrust` field still
asserted "net-SELLING 15 straight quarters" after Q2 earnings (08-08)
showed the direction reversed — Abel's first net-buying quarter in 14,
$23.5B bought vs $3.7B sold, incl. a new $10B Alphabet stake. Direction
reversed, not just aged — text corrected in `board.yaml`; the `thrust`
NUMBER (still the 07-28 estimate) not re-derived this pass, flagged for
a fresh figure next full axes rollout. Posture assignment (Berkshire has
none set) is a separate open question, not resolved here.

**Near-miss audit — two structural access gaps confirmed recurring, not
incidental, across multiple critic passes this week:**
- **Axios Pro Rata and FT Unhedged** (global-capital benchmarks):
  unreachable in 6 of 7 this week's critic passes (08-03, 08-04, 08-07,
  08-08, 08-09, and effectively 08-06 too) — logged honestly each time
  but never fixed. Worth deciding: alternate access route, or drop from
  the benchmark set.
- **Behavioral Health Business** (mental-health benchmark): 403'd on
  every single access attempt this week without exception, worked around
  via Google News/RamaOnHealthcare mirror every time — and every real
  coverage-critic miss this week traced back to BHB directly or
  indirectly (LifeStance, Aware Recovery Care, the FDA/CMS meetings, the
  CCBHC story). Simultaneously this lens's most miss-productive
  benchmark and its least accessible one. `bhbusiness.com` is also one
  of the 14 unrated `gap_fill` domains in the new outlet-credibility
  layer — two separate workstreams converging on the same domain.
- **frontier-ai pattern**: 3 of 4 real misses this week (Anthropic's
  Volta deal, Meta's Muse Code, Anthropic's chip team) share one shape —
  a lab's own infrastructure/product move outside any existing thread's
  term list. `inhouse-silicon` had to be revived mid-week for exactly
  this reason. Recommend a periodic term-coverage check per major lab,
  timed to `/week`.
- **world-news pattern**: the mechanical signal's morning-build cutoff
  missed real overnight news THREE times this week (the 08-03 Hormuz
  strikes, `world-news.yaml` going fully dark for 2 cycles 08-03→08-06,
  and the Yemen civil-war escalation) — argued as structural, not a
  one-off, given the week's escalation-heavy shape. Recommend either a
  later default cutoff or making the overnight-extension pass standard.

**Capital-context.yaml refreshed** (`/week` step 4b): all 5 macro
collectors re-run with an explicit `--since 2026-08-04` window (the
default 24h lookback would have missed the gap) — genuinely NOTHING NEW
from any of the 5 sources this week (treasury_tic/bis_stats/imf_data:
real successful calls, zero new data, consistent with their real-world
lag; epfr_flows re-caught the same report already on file; fund_flow_
reports: still bot-walled, same as every check since 07-30). `rate_regime`
and `conflict_risk_premium` readings updated directly from this week's
thread activity (the jobs report + Lisa Cook fight; the Aramco strikes +
Yemen escalation + Israel-Lebanon opening) — not from the 5 collectors,
which don't cover those.

**Radar.md**: all 7 questions (Q1-Q7) got a new `week 08-09` working
note, synthesized from the 4 digests' proposals (Q2 and Q6 each merge
two lenses' contributions). None looked answered or dead this cycle.

## 2026-08-11 critic pass — finalized 2026-08-09 (all three critic-bearing
lenses; world-news carries none by design)

Run two days late: 08-09's coverage window opened ~14:00 UTC on 08-10 and
the 08-10 sessions went to the `research/` build instead, so this pass
closed a day-old finalization rather than a same-morning one.

### ai / 2026-08-09
- **Missed:** **AI data-centre opposition as a defining bipartisan issue in
  the 2026 midterms.** The Neuron led its 08-09 issue with it ("The AI Data
  Center Backlash Is Going Bipartisan"); eWeek ran a matching piece the same
  day. The underlying reporting is NPR's own campaign-trail work of 08-08
  (npr.org/2026/08/08/g-s1-137853/data-centers-primaries-midterms): Abdul
  El-Sayed's Michigan Senate primary win after campaigning against an
  OpenAI-Oracle data centre in Saline Township; Vivek Ramaswamy's
  "Ohioans-first" anti-data-centre pledge against Amy Acton's conditional
  moratorium; Francesca Hong centering opposition in Wisconsin. A cited
  Gallup poll puts opposition near 7-in-10.
- ⚠ **Date discipline, recorded because the miss is softer than it looks:**
  several facts cited INSIDE that narrative are months old and were NOT
  treated as new — Michigan's HB 5594-5596 moratorium bills (March 2026),
  the Port Washington WI referendum (2026-04-08), the Sanders/AOC federal
  moratorium bill S.4214/H.R.9442 (March/June 2026). What is genuinely new
  is the SYNTHESIS plus the fresh El-Sayed result. Logged as a real miss,
  but a narrative/framing one rather than a clean hard-news event.
- **Map effect:** folded into `2026-08-09-frontier-ai.md` and written to
  `datacenter-power-grid`, whose own watch text already named the ratepayer
  and environmental-justice fights. No new thread, no watchlist add.
- **Secondary gap found, not a lead-story miss:** ByteDance's reported
  ~10-trillion-parameter model (FT) and Firmus's $2B AI-datacentre raise
  (Bloomberg), both event-dated 2026-08-07 and absent from the 08-05→08-09
  digests. Neither was any benchmark's lead, so neither counts under this
  critic's strict standard; both were folded into thread timelines at their
  true 08-07 event date on this pass.
- **Access:** all four reachable. The Rundown AI, TLDR AI and The AI Daily
  Brief are weekday-only, so their first post-weekend issues are 08-10; The
  Neuron publishes Sundays, which is why it alone carried the 08-09 lead.
- **Pattern:** this lens runs strong on lab/product/capital-markets stories
  and thin on AI as a live electoral/political issue at state and
  congressional level — the same soft spot the 08-07 appendix already named.

### mental-health / 2026-08-09
- **No misses**, and the reason matters more than the verdict: none of the
  four benchmarks published mental-health content inside the window at all.
  BHB's feed ran from Fri 08-07 15:32 UTC straight to Mon 08-10 20:17 UTC,
  both ends outside the window and both non-MH. STAT's one in-window item
  (08-09) was a Sanofi drug shortage. Fierce's Monday leads were a vaccine
  schedule EO, health-plan losses, hospital pricing, a Steward contempt
  case and a Doximity AI assistant. MobiHealthNews had nothing 08-08/08-09.
- ⚠ **Read a weekend "no misses" as a null result, not a passed check.**
  Three of the four are weekday-only B2B trade outlets and 2026-08-09 was a
  Sunday, so this outcome is close to structural. A Sunday's real recall
  risk sits with the primary/academic/consumer-press channels this critic
  set does not cover — which is exactly where that day's own digest content
  (SIM-VAIL, the UK psilocybin RCT, Malaysia) actually came from.
- **Access — one benchmark escalated:** MobiHealthNews now blocks a plain
  `curl` too, not just WebFetch's crawler signature. Reached via the
  `r.jina.ai` reader proxy. That is a step past the BHB case (where plain
  HTTP still works) and is now recorded in `sources/benchmarks.yaml`, along
  with the resulting rule: re-test all three "fixed" benchmarks periodically
  rather than assuming a fix stays fixed.

### global-capital / 2026-08-09
- **Missed, with a fair dating caveat:** **Nvidia's $500B+ AI-compute
  financing platform** with Apollo, BlackRock, Blackstone, Brookfield,
  Goldman Sachs and KKR — MOUs, not final agreements, treating GPU capacity
  as a collateralizable real asset, funded via private placements and
  SPE bonds. Verified against NVIDIA's own newsroom release and Blackstone's
  matching press page. **Event-dated 2026-08-10**, i.e. just past the 08-09
  digest's cutoff, and every outlet covering it published same-day. Logged
  as the pass's miss because it is the period's biggest capital story, but
  it belongs to 08-10 and was written there, not retro-fitted into 08-09.
- **Map effect:** written to `nvidia-vendor-financing` and
  `asset-managers-build-ai` (the latter stale since 07-27 — a significant
  revival), `sev=major`, with an interpretation attached.
- **Access:** Money Stuff via search (its 08-10 column was retrospective on
  the 07-30/31 Situational Awareness collapse, not new). FT Unhedged's
  public RSS worked (its 08-10 edition led on the BoJ and the jobs report).
  Bloomberg Technology 403'd on direct fetch, worked via search. **Axios Pro
  Rata blocked as documented** — one attempt, expected Cloudflare block, not
  retried; still the one unresolved access gap in this file.
- **Structural note the critic raised, worth Ben's eye:** 08-10 was unusually
  dense for AI-capital news (Nvidia, Maia 300/TSMC, AIndicators, the
  JPMorgan deal all same-day), and several benchmarks cover that cluster as
  same-day breaking rather than next-morning recap. On days like it, a
  digest whose curation stops mid-morning structurally misses the day's own
  biggest stories — which is what happened here and was only caught because
  08-10 was still `building` when this pass ran.

## 2026-08-11 critic pass — finalized 2026-08-10 (all three critic-bearing
lenses; world-news carries none by design)

Run the same day the digest-day closed, ~3.5h after the coverage window
opened — the first genuinely on-time finalize in a week.

### ai / 2026-08-10
- **FOUR real misses**, the most a single lens has produced in one pass.
- **Claude improved a century-old bound tied to the Riemann Hypothesis** —
  the proven share of zeta-function zeros on the critical line raised from
  41.6% to 67.2%, by ~60 coordinated subagents over ~1.5 days after 650
  failed approaches, machine-verified in Lean. Anthropic is explicit this is
  incremental progress on an existing line of work, NOT movement toward
  proving the hypothesis — the qualifier travels with the claim. Primary:
  anthropic.com/research/riemann-zeta. It was TLDR AI's #1 item and a
  Rundown lead; we had nothing. No thread fits an AI-capability-research
  milestone — offered as a thread candidate rather than forced onto one.
- **Amazon's Pecos County power deal** — and this one arrived at the digest
  with TWO errors in the brief it was handed, both caught by the curator
  before publication: the framing was not "financing" (Amazon acquired an
  ~8,000-acre site and contracted for power from Pacifico Energy's plant),
  and the event date was 08-07, not 08-08. Written as a late catch on
  `datacenter-power-grid` at its true date. The plant is permitted above 30
  million tons CO2/year.
- **Google open-sourced TPU Raiden** (Apache-2.0 KV-cache transfer library,
  the TPU answer to Nvidia's NIXL) — flagged first by SemiAnalysis, not
  announced by Google. Directly answers `google-capex`'s own standing
  "TPU externalization" watch item, which had not moved since 07-31.
- **North Korea's Kimsuky group running local, self-hosted AI tooling**
  (Ollama, GPT4All, RAG pipelines, Cursor) to scale intrusion work without
  touching a commercial provider. ⚠ The brief named Japan Times and Manila
  Times as corroborators; the curator could not verify either and dropped
  them rather than cite unverified — Genians' own report plus Al Jazeera and
  Business Standard stand. Logged ambient: no watchlist entity exists for
  North Korea or Kimsuky, which is itself the gap.
- **Access:** TLDR AI and The Neuron fetched directly for both 08-10 and
  08-11. The Rundown AI's archive doesn't expose per-date URLs; its 08-11
  issue was found by title, its 08-10 lead never independently pinned. The
  AI Daily Brief had only an 08-10 episode, pure recirculation.
- **Pattern the critic named, worth keeping:** all three non-Riemann misses
  are infrastructure- or security-adjacent — exactly what a sweep tuned for
  big-lab capital moves and lab-safety incidents under-indexes on. Two of
  them (Amazon, Raiden) sit on threads this map already tracks, so this was
  not a coverage-category gap, just missed items inside a watched category.

### global-capital / 2026-08-10
- **No genuine miss within this lens** — but the pass produced two real
  additions and one instructive false positive.
- ⚠ **The critic's reported "miss" was not one.** It flagged Microsoft's
  Maia 300 / TSMC talks; that story is already in the 08-10 frontier-ai
  digest, on `microsoft-capex`, and logged as a dated expectation. **A
  per-lens critic reads only its own lens's digest, so a correctly-placed
  cross-lens story reads as a gap.** Recorded as a non-miss with that
  reason. This will recur and is a property of the critic's design, not a
  coverage failure.
- **Genuine gap the critic did surface: Moody's on banks' AI-vendor
  dependence** (08-09, Guardian) — concentrated operational dependence on a
  small set of foundation-model and cloud providers, naming OpenAI and
  Anthropic, with cascade and pricing-power risk. Verified NOT already in
  the record (the Moody's entries already on our threads are different
  stories). 08-09 is closed, so it was logged at its true event date on
  `ai-buildout-debt-risk` rather than reopening that digest.
- **Found independently, flagged by no benchmark: CoreWeave closed a $2.6B
  delayed-draw term loan at SOFR+550 — a 10.44% yield, flexed WIDER from
  initial guidance of S+425-450.** Confirmed against the SEC 8-K and
  CoreWeave's own release. This is the first CONFIRMED transaction-level
  coupon in this map's AI-debt record, it resolves a flag
  `coreweave-backlog-bet` left open on 07-30, and it landed three days
  before the Q2 call.
- **Dropped after five resolution attempts:** a "banks hit concentration
  limits, sending data-centre debt to pension funds" item — only an
  MSN-syndicated copy with relative dating, no reachable byline or body.
  Not published. An unverifiable claim on-theme is still unverifiable.
- **Access:** FT Unhedged's public RSS worked over plain curl (WebFetch
  refuses ft.com outright). Axios Pro Rata 403'd as documented, one attempt.
  Money Stuff and Bloomberg Technology via search; both bloomberg.com and
  ft.com 403 direct fetches.

### mental-health / 2026-08-10
- **No misses**, and the reason is the finding: none of the four benchmarks
  published mental-health content in the window at all. Behavioral Health
  Business's two 08-10 posts were **already this digest's own lead
  bullets**; MobiHealthNews ran orthopedics, maternity and general HIT;
  STAT ran general pharma/FDA/hospital economics; Fierce had no MH content.
- **The critic's own read, worth keeping:** this lens carried more MH depth
  that day than any single benchmark did — the China/France/US regulatory
  divergence, the JMIR engagement study and both behavioural-health money
  stories all came from primary reporting rather than a benchmark lead.
- **Access, all three routes re-verified today:** BHB now needs a GOOGLEBOT
  user-agent (a normal browser UA has started getting the Cloudflare
  interstitial too — this domain has tightened twice in five days);
  MobiHealthNews needs the r.jina.ai reader proxy; STAT's RSS works over
  plain curl. New quirk found: Fierce Healthcare's /behavioral-health tag
  page 403s as well, wider than the About/policy paths already recorded.
- **Adjacent item checked and correctly excluded:** STAT's 08-11 piece on
  nurses organising against clinical AI names Kaiser and National Nurses
  United, but its own sourcing (a 07-13 Guardian piece, a July CalMatters
  piece) is already inside `kaiser-ai-clinician-backlash`. No new dated
  fact, so not a miss.

### Collection note — a permanent blind spot, not a slow day
`semantic_scholar` exhausted its 600s lane budget on BOTH of today's runs
(228 and 222 terms skipped). The cap is deliberate and well-reasoned. The
defect is that the collector iterates terms in list order with no rotation,
so the skipped tail is **the same ~220 terms every run** — swept at 0%,
permanently, while the first ~185 are swept at 100%. The manifest records
only a count, never which, so it leaves no trace in provenance. This is the
academic lane, i.e. the EBP strand's primary feed. Filed to kestrel's INBOX
with a rotation fix modelled on `/daily`'s own cold-rotation pattern.

## 2026-08-12 critic pass — finalized 2026-08-11 (all three critic-bearing
lenses; world-news carries none by design)

Run ~20h after the digest-day closed (05:00 ET 08-12) — later than usual;
the prior run had stalled with 08-11 sitting `building`/`pending` and 08-12
entirely uncurated until this pass caught up both days at once (see
`log.md` for the full session account). Four sonnet agents, one per lens,
ran in parallel: each finalized 08-11 with its own critic pass and built
08-12 today-so-far.

### ai / 2026-08-11
- **One minor miss, cross-lens.** TLDR AI linked a WSJ piece on Anthropic's
  September/October IPO target (~$965B valuation) in its Miscellaneous
  section — a more substantive version of an IPO-prep story this digest
  had already flagged (and correctly held back a thinner NY Post piece on).
  Not written into this lens's digest: the owning thread,
  `anthropic-ipo-timing`, is global-capital's, not ai's — logged here as
  the honest record of what the benchmark caught, not duplicated as a
  bullet.
- **We had, they didn't:** TSMC's $29.4B capex + Sony JV, the IBM/Together
  AI deal, Oracle's next layoff round, CoreWeave's Q2 print, xAI's Grok
  Bot, Google Gemini's 1B-user milestone, and — the sharpest one — an
  Israeli security firm's account of what looks like the first fully
  autonomous AI cyberattack against a government target (China-linked
  actors, Taiwan), which none of the four benchmarks led with despite it
  arguably being the day's most significant single item.
- **Both covered:** all three checkable benchmarks' actual leads (Riemann-
  zeta, Muse Glimmer, GPT-5.6-Cyber/Daybreak, the Zoom bug, Nvidia's $500B
  platform, the Astra deep-dive) were already on the 08-10 finalize or this
  digest. The Rundown AI's archive wouldn't resolve a dated 08-11 issue —
  not independently checked this pass.
- **A real recall trap avoided, worth keeping as a pattern note:** several
  headlines that read as fresh on a shallow buffer pass turned out on
  primary-source verification to be older stories resurfacing via a
  different aggregator on a different day — the DeepMind leadership
  reshuffle/Jeff Dean exit (really 08-05/06), OpenAI's Astra pause (really
  08-07), Chloé Bakalar's exit (already on 08-10), a 15-AG letter (really
  08-03), Kimi K3's GitHub-cheating incident (really 08-06),
  Microsoft-Chevron's power deal (really June), and Musk's California
  AI-law loss / Anthropic's Reddit-suit remand (both really March). All
  checked and dropped rather than re-reported as new.

### global-capital / 2026-08-11
- **Two real misses, both found and fixed during the check itself rather
  than left standing.** Bloomberg Technology's own lead was Intel upsizing
  its stock offering from $15B to $20B on 5x demand — folded in as a full
  bullet with primary-source detail. Money Stuff covered a
  Change-in-Control clause in Tesla's pay package that a SpaceX-Tesla
  merger could exploit — also folded in.
- **No misses against FT Unhedged** (direct RSS, no paywall gate). Axios
  Pro Rata skipped per the standing Cloudflare-block record — no new
  attempt.
- **Found independently, flagged by no benchmark: CoreWeave's Q2 print**
  (reported 5pm ET 08-11) — revenue $2.575B and adjusted EPS -$1.03 both
  beat consensus, while net interest expense hit $640M, up 140% YoY from
  $267M — the first look this map has at backlog growth and debt cost
  moving together in one borrower's own numbers, resolving the
  `coreweave-q2-earnings` ledger entry as `hit`. Also the first fatal
  Houthi/US-military exchange in the Red Sea/Gulf of Oman since the war
  began.

### mental-health / 2026-08-11
- **One near-miss, self-caught during finalize, not left standing.** A CMS
  interim rule cutting off Medicaid work-requirement exemptions for
  substance-use-disorder patients after five years in "stable recovery"
  (providers call the standard undocumentable) posted to Behavioral Health
  Business after the original 14:00 ET cutoff — caught this pass and
  written in. Two clinical-trial registrations (psilocybin for
  methamphetamine-use-disorder in HIV patients; an NYU Rohingya
  intergenerational-trauma cohort) were also caught by a direct registry
  query that the original broad term-match pull had missed.
- **No further misses.** STAT ran no MH content (a Medicaid
  gender-affirming-care story was weighed and set aside as a different
  clinical/regulatory lane); Fierce Healthcare ran no MH content (its
  `/behavioral-health` tag page still 403s); MobiHealthNews (via the
  `r.jina.ai` proxy) ran no MH content.
- **The day's real resolution:** `kaiser-nuhw-mediation-0811` flipped to
  `passed-silent` — the AI/layoffs/clinician-control mediation was
  scheduled to begin today but neither party's own channel confirms it
  convened, checked three times across the day. This dispute has a real
  precedent for a scheduled mediation round going quiet mid-stream (2025),
  so the silence is being treated as itself worth recording, not waved off
  as "probably fine."

### world-news / 2026-08-11 (no critic — carries `coverage: na` by design)
- Extension pass added one dated development for the 14:00 ET→close gap:
  an overnight Russia-Ukraine barrage (Iskander-M, Kh-31P, Kh-35 missiles +
  138 Shahed drones; 8 dead, 57 injured across nine oblasts).

### A previously uncaptured story, flagged not filed: the DRC's Ebola
outbreak passed 2,011 confirmed deaths this week (Bundibugyo strain, no
approved vaccine/treatment, spread into Uganda, WHO PHEIC). The world-news
agent flagged it as a possible flash; checked directly against the primary
source before deciding — the WHO's actual emergency declaration was
2026-05-15, three months ago, so crossing 2,000 deaths this week is a
running-total milestone, not a new discrete event, and doesn't clear the
flash rail's "new event only" bar. Registered as a thread candidate
instead (see 🧵 Map deltas / thread candidates for 08-12).

### Collection note: `lda` (lobbying disclosure) fully blocked this run —
142/142 swept terms failed with HTTP 403, "very likely blocked at the
network edge," per the collector's own log. `semantic_scholar` hit its
600s lane budget again (187 terms skipped) — same permanent-blind-spot
pattern already filed to kestrel's INBOX, not a new finding. `sec_edgar`
threw individual-term 500s throughout the run but still returned 1,516
items overall — a noisy run, not an outage. `gdelt` needed heavy 429
backoff on several terms (Google DeepMind, xAI, Meta AI, Safe
Superintelligence all fully dropped after 3 retries) but the collector as a
whole still returned 97 items.

## 2026-08-13 critic pass — finalized 2026-08-12 (all three critic-bearing
lenses; world-news carries none by design)

Run ~4.6h after the digest-day closed (05:00 ET 08-13) — inside the
normal finalize window. Four sonnet agents, one per lens, each finalized
08-12 with its own critic pass and built 08-13 today-so-far.

### ai / 2026-08-12
- **Two real misses.** TLDR AI led with Nvidia's Nemotron 3.5 Lightning
  model + NeMo Switchyard (an agent-routing library) and Microsoft's
  MAI-Code-1.1-Flash update — neither caught by the original pass.
- **A judgment call worth keeping as a pattern note:** a heavy overnight
  newswire wave of "DeepMind leadership shakeup" / "Hassabis pitched an
  AI-oversight body" stories read as fresh but were confirmed, on
  primary-source dates, to be recirculation — TechCrunch dates Hassabis's
  public oversight-body call to 07-14, the-decoder.com dates the actual
  CEO-to-chair transition to 08-05/09. Documented explicitly rather than
  silently dropped or, worse, silently re-reported as new.
- **We had, they didn't:** Thrive Holdings' OpenAI-backed $2B raise at a
  $12B valuation, folded in during finalize.

### global-capital / 2026-08-12
- **Partial check — WebSearch exhausted mid-pass.** The shared 200-call
  session budget ran out before Money Stuff or Bloomberg Technology could
  be checked directly; the agent fell back to Bing-via-WebFetch, which
  worked for open-web stories but couldn't reach either paywalled
  archive. Disclosed honestly in both digests rather than claimed clean.
  Same recurring friction this file has logged three sessions running
  now (08-04/05/06) — still no structural fix, still absorbed per-run.
- **Real finds, not benchmark-sourced:** Lambda's GPU-financing loan
  repriced at final terms ($926M vs. the preliminary $917M, tightened to
  SOFR+300bps, Moody's Baa2 — the first investment-grade Term Loan B a
  private neocloud has carried); a live claim conflict on the map itself
  (see below).
- **A ledger claim corrected, not just updated:** `decart-acquisition-close`
  named SpaceX as Decart's buyer (08-09 report); both this lens and the
  ai lens independently converged the same run on Bloomberg reporting
  Anthropic instead, with Musk publicly denying SpaceX involvement.
  Corrected in `upcoming.yaml`, original source retained, buyer identity
  flagged unconfirmed by either company (still "in talks," not a signed
  deal).

### mental-health / 2026-08-12
- **One real miss, self-caught: HHS's "treatment first" addiction
  toolkit** (STAT), explicitly rejecting harm-reduction/housing-first
  doctrine by name — missed by the original pass, caught checking STAT's
  actual 08-12 output.
- **Found independently, no benchmark carried it — the most significant
  single item this pass produced across any lens:** a Middlesex County,
  MA prosecutor has publicly tied a 17-year-old's double homicide of his
  mother and brother to his ChatGPT use (searches for "theoretical ideas
  or fantasy stories regarding the killing of his family," per the DA's
  own statement). First case on this map tying a *general-purpose*
  chatbot, not a therapy/companion product, to a completed killing of a
  third party — a genuinely new pattern, not a repeat of the
  suicide-focused cases already tracked (`sev=major`). None of the four
  trade benchmarks carried it — it's a Boston-regional crime story, only
  surfaced by broadening past the standard benchmark set during finalize.
- **A real, correctly-cautious non-resolution:** `ca-sb903-appropriations-
  hearing`, due today, checked directly against Assembly Appropriations'
  own hearings page and leginfo — the bill sits on today's suspense
  calendar but California's legislature had not yet adjourned session as
  of the check, which is the hearing's own trigger condition. Left
  `pending` rather than guessed at.

### world-news / 2026-08-12 (no critic — carries `coverage: na` by design)
- Finalize pass ran entirely on direct WebFetch (Al Jazeera, Kyiv
  Independent, Times of Israel) rather than WebSearch — that budget was
  already exhausted before this pass started, same shared-budget
  friction as global-capital's note above. Three developments folded in:
  IRGC Quds Force commander Qaani lobbying Iraq against its militia-
  disarmament deadline (a new Iraq front on `iran-conflict-widening`), a
  Pentagon review disclosing 153 Yemeni civilians killed in 2025 US
  strikes, and the digest-day's actual close (a 133-Shahed overnight
  barrage into Ukraine, 8 dead, answered by a Ukrainian strike on a
  Russian refinery 1,300km from the border).

### Collection note: `lda` fully blocked again (143/143 terms, HTTP 403)
— now filed to kestrel's INBOX as of yesterday's pass, not a new finding.
Otherwise a clean 18-collector run.

### Structural friction, now worth naming plainly rather than absorbing
again: **the shared session-wide WebSearch budget (200 calls) was
exhausted by TWO of four parallel lens agents this pass** (global-capital,
world-news), each falling back to WebFetch-via-search-engine for the
remainder of their research. Both still reached a reasonable sourcing
bar, but this is now a recurring, dated pattern (08-04, 08-05, 08-06,
and now 08-13) rather than a one-off — the fix each time has been
absorbing it mid-run, never a structural change to the budget itself or
how four parallel agents share it.

## 2026-08-14 critic pass — finalized 2026-08-13 (all three critic-bearing
lenses; world-news carries none by design)

Run well past the checkable window (digest-day closed 05:00 ET 08-14; run
started ~16:00 ET, ~11h after close). Four sonnet agents, one per lens,
each finalized 08-13 with its own critic pass and built 08-14
today-so-far, dispatched after a full collector sweep (all 15
registered collectors, since the last successful run 08-11).

### ai / 2026-08-13

Checked this lens's four daily critic outlets against what they actually
led with on 08-13: TLDR AI and The Neuron's dated issues were readable
directly; The Rundown AI's archive didn't surface a distinct 08-13 entry;
The AI Daily Brief's episode topic (Grok 4.6) was already logged 08-12.

**They led with → we missed:** DeepSeek's V4 API price hike and Elon
Musk's Grok 4.7 tease — both caught in this finalize pass. **Two items
traced to the wrong day, not missed so much as mis-shelved by the source
newsletters:** The Neuron's "Anthropic reviews 56 retraining studies"
piece and Google's Pixel 11 launch (DeepMind sign-language model, Gemini
Intelligence suite) both verified via direct fetch to be 2026-08-12
events — neither appears in that day's (already-finalized) digest, a
real miss on 08-12 specifically, flagged here rather than fixed (outside
this pass's write scope; 08-12 is already closed).

**Both covered:** Claude Cowork's Chrome integration, Grok 4.6, DeepSeek
V4-Pro's release, Qwen3.8-2.4T-A95B — all logged 08-12, still circulating
in 08-13's benchmark issues.

**We had → they didn't:** Anthropic's $6B Decart talks + $2T IPO
pricing, Anthropic's Frontier Red Team multiagent research, CXMT
overtaking Tencent and SMIC's tripled profit, Microsoft's China-retreat
exclusive, Databricks' $5B round, AMD's $4.75B bond sale, Vantage's
$100B IPO exploration, Meta's NABTU pact, and OpenAI's CRO/Simo news.

### mental-health / 2026-08-13

Checked all four daily benchmarks (Behavioral Health Business via
Googlebot-UA curl; STAT News via its RSS feed; Fierce Healthcare via
WebFetch homepage + targeted search, its /behavioral-health tag page
still 403s per the standing access note; MobiHealthNews via the
r.jina.ai reader proxy).

**Miss found:** BHB's own lead for the day, its annual Inc. 5000 trend
feature (52 behavioral-health companies made the list this year vs. 45
last year), wasn't in the 08-13 digest's earlier building pass. Folded
into the finalize as a Capital & corporate bullet and into
mh-clinical-infra-funding's timeline.

**No miss found** on STAT (nothing MH-AI-specific that day), Fierce
Healthcare (no MH-AI lead found on accessible surfaces or search), or
MobiHealthNews (front-page snapshot showed nothing MH-specific).

**Both covered:** none — a thin day for benchmark/digest overlap.

**We had → they didn't:** SB 903's Appropriations release (primary
leginfo source, not yet in trade press as of this check), a new
Character.AI federal suit (filer's own press release, not yet in trade
press), the Acton, MA case (general/local news, outside this benchmark
set's trade-press scope by design), and a Dartmouth Therabot feature
confirming Vermont's AI-therapy law (regional outlet, not a benchmark).
Stronger day for the digest than for the benchmark set specifically.

### global-capital / 2026-08-13

**Benchmarks checked:** FT Unhedged (direct RSS, worked cleanly),
Bloomberg Technology (WebSearch — its 08-13 newsletter), Money Stuff
(WebSearch), Axios Pro Rata (blocked).

**They led with → we missed:** nothing. FT Unhedged's 08-13 issue ("The
most difficult dilemma") covers monetary policy colliding with a supply
shock — the same Fed-debate-meets-oil-fundamentals throughline this
digest carried all day. Bloomberg Technology's 08-13 lead ("Wall Street
Opens Spigots for AI Debt and Stock Offerings") named the same Vantage
$100B IPO, Decart talks, and AI-startup-valuation material already in
this digest. Money Stuff's 08-13 column was off-axis by design
(prediction markets); Levine is on vacation through 08-24.

**Axios Pro Rata: recurred, not new.** axios.com returned Cloudflare's
domain-wide bot block again today (plain fetch and Googlebot UA both
403'd) — the same open, unresolved gap `sources/benchmarks.yaml` already
documents. Recording the recurrence per that file's own request; still
needs Ben's call on a headless-render fix vs. accepting the gap.

**Both covered:** AMD's Anthropic-tied bond sale, Anthropic's $2T
IPO-valuation chatter/Decart talks, the Vantage-led data-center IPO wave.

**We had → they didn't:** the Iran/oil fundamentals-over-rhetoric read
(tested four separate times that day), PPI/jobless-claims vs. the Fed's
9-3 split, CXMT overtaking Tencent, Oracle's fresh layoffs vs. its
capex, the Jefferies hyperscaler FCF number, Burry naming Nvidia's
platform specifically, Silver Lake/Workday, and the Jane Street junk-
rated bond.

### Collector note — full 15-collector sweep, `lda` still 100% dead

All 15 registered collectors ran (since=2026-08-13T20:08:39Z, ~24h
window). `lda`: 143/143 terms failed, HTTP 403 — confirmed still
permanently dead from this container's egress (Akamai edge block,
documented since 08-05), not a fresh finding. `semantic_scholar` hit its
600s lane wall-clock budget and skipped ~169 terms — the accepted,
by-design cutoff, not an outage. `gdelt` ran through repeated 429
backoffs but completed cleanly. No other collector errors.

## 2026-08-15 critic pass — finalized 08-14 (three critic-bearing lenses;
world-news carries none by design)

Run well past the checkable window (digest-day closed 05:00 ET 08-15;
run started ~10:00 ET, ~5h after close). Three sonnet agents, one per
critic-bearing lens, each checked 08-14's already-building digest
against that lens's benchmark set.

### ai / 2026-08-14

**They led with → we missed:** Google's Gemini 3.7 Flash launch (08-13,
still leading 08-14 coverage; a coding/agent-focused model with a
50%-off intro price through year-end) — all four benchmarks (TLDR AI,
The Neuron, The AI Daily Brief, The Rundown AI) had it. OpenAI's
"Ultrafast" mode for GPT-5.6 Sol (a Cerebras-hardware API tier at 750
output tokens/sec, first opened to Jane Street/Podium) — TLDR AI, The
Neuron, The Rundown AI (3 of 4). DeepSeek's V4-Pro release (adjustable
"thinking levels," steep peak/off-peak price changes) — The Neuron,
corroborated Caixin/CGTN. OpenAI's "Computer History" Mac-app feature
(opt-in activity tracking, replacing "Chronicle") — The Neuron, The AI
Daily Brief. Lower-confidence: Microsoft's quiet 5-year China office/JV
retreat — The Neuron only.

**Map effect:** none — google, openai, and deepseek are all already
watchlist entities, and deepseek already sits on the open
`china-stack-independence` thread. Item-level sweep misses on a day the
digest was pulled toward the SpaceX/Cursor close and OpenAI IPO-churn
story, not a map gap.

**Both covered:** SpaceX/Cursor close, OpenAI CRO Denise Dresser's exit,
Apple's China-specific Alibaba model, Anthropic's multiagent research
(both sides correctly treated as 08-13 recirculation, not new).

**We had → they didn't:** Zhipu/Z.ai's GLM-5.3-vs-Anthropic-Mythos-5
cybersecurity claim, Google's watermark opt-out toggle, OpenAI CFO Sarah
Friar's $40B ARR disclosure, the YMTC v. Micron Lanham Act dismissal,
Jiahui Yu's Meta departure to found TBD Lab.

**Unverifiable:** The Rundown AI's per-issue dated content — its archive
page doesn't expose issue dates, so its attributed items above are
reconstructed from secondary snippets, not a verbatim fetch.

### mental-health / 2026-08-14

**Clean pass — no misses found** across all four benchmarks (BHB via
Googlebot-UA curl, STAT Health Tech, Fierce Healthcare via homepage,
MobiHealthNews via the r.jina.ai reader proxy).

**Both covered:** the VA's 20th active psychedelic-therapy clinical
trial (psilocybin, treatment-resistant depression in veterans) — BHB's
own lead, also the digest's lead item.

**We had → they didn't:** the Kaiser/NUHW mediation window closing with
no outcome from either side, and 3 of 4 newly-registered clinical trials
(MDMA/PTSD, a Singapore TMS trial, a Utah maternal-mental-health AI
tool, a Michigan postpartum-depression intervention) — expected
outperformance, trade press doesn't track clinicaltrials.gov
registrations the way this lens does.

**Map effect:** none — both threads the digest touched
(`kaiser-ai-clinician-backlash`, `psychedelic-regulatory-sprint`) are
already tracked.

### global-capital / 2026-08-14

**They led with → we missed:** Applied Materials' fiscal Q3 2026
earnings (reported after close 08-13, reaction through 08-14) — record
$9.12B revenue (+25% YoY), an EPS beat, and a guidance raise to $10.25B
for Q4 vs. $9.55B consensus, driven explicitly by AI chip-equipment
demand. Covered by Bloomberg same-day, and this repo's own world-news
crawl had already flagged it as a 6-outlet story — but with no
watchlist entity, it never reached either the 08-13 or 08-14 digest.

**Map effect:** `+ org global-capital/"Applied Materials"` (critic-add
2026-08-15) — a semiconductor-capex-chain peer of Nvidia/TSMC/ASML,
already on this list.

**Both covered:** Silver Lake/Workday take-private (now $51B, Axios's
08-14 lead — an update on the 08-13 digest item, not new information) ·
Databricks' $5B round at $190B (Axios's top VC item, already logged
08-13) · CXMT/China-tech-earnings and Nvidia's $500B financing platform
(both explicitly logged in the digest header as 08-13 recirculation,
independently confirmed).

**We had → they didn't:** Berkshire's full Q2 2026 13F read directly off
SEC EDGAR (Alphabet stake near-doubling, the Delta/D.R. Horton
rebalancing, the Constellation Brands exit) · AMD's final $4.75B
bond-pricing tranche detail.

**Unverifiable:** Bloomberg Technology — Cloudflare/CAPTCHA-blocked on
direct fetch, and (new finding) the r.jina.ai reader proxy that clears
Axios/MobiHealthNews does NOT clear Bloomberg's block either; fell back
to WebSearch, which only partially reconstructs "what they led with."
Money Stuff — no 08-14 edition found; its 08-13 column notes Levine is
off next week through 08-24, read as verified-likely-absent rather than
a blocked source.

**Axios Pro Rata: access fix confirmed working.** The r.jina.ai
reader-proxy fix logged in `sources/benchmarks.yaml` (08-15) held up on
this pass — full issue text returned, no Cloudflare block.

**Watch, not yet thread-worthy:** FT Unhedged has now run a yen/BOJ-
intervention theme five times in under two weeks (08-03, 04, 10, 12,
14), all analyst commentary rather than a discrete event — consistent
with this digest's existing commentary-filter discipline (cf. Burry's
warning, logged 08-13 as commentary not an event). Flag only if it
turns into an actual BOJ/Treasury action.

### Collector note

Full sweep for 08-15 (since the 08-14 ~20:xx ET run) kicked off ahead of
this critic pass; see the next entry for its results.

---

## 2026-08-17 /daily — three digest-days at once (08-15 finalize, 08-16 reconstruct, 08-17 open)

No `/daily` ran over the weekend, so this pass finalized 08-15, rebuilt
08-16 from scratch, and opened 08-17. The critic ran against all three.

### The structural finding, which matters more than any single miss

**Monday newsletter leads are a poor recall signal for Monday.** Three of
the four AI benchmarks are weekday-only (verified empirically this pass,
not taken on faith: sitemap gaps between the 08-14 and 08-17 editions of
The Rundown AI, and 307 redirects on TLDR AI's dated 08-15/08-16 URLs).
They therefore spend Monday clearing Thursday and Friday. **Six items were
pulled from Monday's benchmark leads and date-verified against primary
sources; all six dated 08-13 to 08-15 and none was a Monday event.**
Scoring them by appearance date would have produced three false misses
against 08-17 while hiding three real ones on earlier days. Every
benchmark lead needs its true publication date established before it is
scored. Adopted as standing practice.

Of the six: three were already covered here — GLM-5.3 (Z.ai, 08-14, in
that day's digest), ChatGPT "Computer History" (08-13, in the 08-14
digest), and Anthropic's multiagent turf-war research (08-13, in the
08-13 and 08-14 digests). Three were genuine misses, below.

### They led with → we missed

- **Crouzeix's conjecture proved with a 16-hour autonomous GPT-5.6 Sol
  session** (SIAM News, **08-15**; preprint 07-27, rev. 08-07). Surfaced
  via The Rundown AI's 08-17 lead. Belongs to the 08-15 digest-day and was
  **folded into that digest at finalize**. Handled with care on status:
  Townsend, Greenbaum and Crouzeix himself have informally checked and
  endorsed the argument, but the preprint sits on a non-refereed server
  and Jin's own repo says "formal peer review is still pending" — those
  are different claims and the digest keeps them apart.
- **OpenAI's annualized revenue run-rate topped $40B** (Bloomberg,
  **08-13**). Not covered. Material to `anthropic-ipo-timing` and
  `frontier-lab-ipos`, both of which turn on relative lab scale ahead of
  listing. Carry it as a **leak, not a disclosure** — Bloomberg cites
  people familiar and states OpenAI declined to comment.
- **The AI buildout's ~$1T financing gap** (Forbes, **08-14**, reporting
  Apollo chief economist Torsten Slok). >$2T of debt needed through 2030
  against <$1T of investment-grade absorption capacity; AI borrowing
  already >40% of new long-term IG corporate issuance. Not covered.
  Directly on `ai-buildout-debt-risk` and `ai-circular-financing-risk`,
  and it is the quantified version of the shadow-backstop story the 08-15
  digest led with — which makes the miss more pointed. ⚠️ Carry with the
  conflict attached: Apollo is a major private-credit manager and the gap
  it identifies is one its own business exists to fill.
- **FT Unhedged, "South Korea's inverse correlation"** (Saturday
  **08-15**) — Kospi falling while the won strengthens. Not covered.
  Korea is not off-lens: `chip-hyperscaler-rotation` runs through SK Hynix
  and Samsung memory, and `apple-cxmt-senate-deadline` turns on Korean
  supply as the alternative to Chinese memory. It simply was not looked
  for.

**08-13 and 08-14 were already `final` and were NOT reopened.** Those two
misses are logged here and in the 08-15 per-lens appendices instead.

### Benchmark availability

Genuinely empty rather than unchecked, for most of the window. **08-15
(Sat):** no AI benchmark published; no mental-health benchmark published
an editorial lead; FT Unhedged was the only capital benchmark to publish.
**08-16 (Sun):** only The Neuron (a "Sunday Special" whose lead was the
08-13 turf-war research — a weekly recap, not a missed development) and
BHB (a sponsored "Voices" column, advertorial, excluded). **Money Stuff
is on scheduled vacation through 08-24**, announced in its own 08-13
column — a clean non-publication, not a blocked source. **The AI Daily
Brief published nothing across the entire 08-15 to 08-17 window.**

### Access findings

- ⚠️ **NEW BLOCK — `r.jina.ai` is now domain-blocked on
  fiercehealthcare.com entirely:** a hard 403 `AbuseAlleviationError`
  ("DDoS attack suspected"), not per-request rate limiting. What still
  works there: the WebFetch tool against the live homepage (200, full
  content) and site-scoped Google News RSS. Direct `curl` to
  `/rss.xml` returns 200 but the feed is mostly gated webinar listings;
  `/feeds/all/rss.xml` hits a Cloudflare JS challenge.
- ✅ **Two routes are SIMPLER than documented.** Bloomberg Technology RSS
  (`feeds.bloomberg.com/technology/news.rss`) needs only `curl -L` to
  follow the redirect — no proxy, no spoofed UA. This supersedes the
  08-14 note above recording Bloomberg as proxy-resistant and
  WebSearch-only. STAT's health-tech feed
  (`statnews.com/category/health-tech/feed/`) works with a bare `curl`.
- ⚠️ **Axios Pro Rata is archive-blind.** The reader-proxy route serves
  **only the current edition**. Three attempts at a back issue failed: a
  guessed `/archive` path (404), a `?page=` parameter (returned the same
  current issue), and a dated web search (not indexed). Its Saturday
  edition — which its confirmed Mon–Sat schedule says existed — is
  recorded as **unreachable, not unpublished**. The 08-15 fix note above
  is confirmed still working *for the current issue only*; that scope
  limit was not previously recorded.
- ✅ Behavioral Health Business's Googlebot-UA workaround held with no
  further tightening this pass.

### Watch, not yet thread-worthy — escalating

The FT Unhedged yen/BOJ-intervention theme flagged on 08-14 as
five-in-two-weeks has now run a **sixth** time: today's lead, "Broken
FIMA," argues Treasury Secretary Bessent's yen-support backstop mechanism
is a shaky basis for intervention policy. This one is closer to the
"actual BOJ/Treasury action" bar that entry set than the previous five,
since it concerns a named, live mechanism rather than analyst commentary
on direction. Still short of a discrete event; flagged as approaching.

### Collector note — a missed daily leaves a real data hole

Worth recording because it is not obvious: **the 08-16 digest-day had
essentially no collector coverage at all.** The `buffer/2026-08-16-*`
files were written by Sunday morning's `/week` collect and their newest
timestamps stop at 2026-08-16T00:21Z — 20:21 ET *Saturday*, before the
08-16 digest-day even opens. No collect ran between then and this
morning. The Sunday reconstruction was therefore carried entirely by
direct web verification. Today's collect did backfill the window after
the fact (`google_news_rss` now spans 08-15T14:02Z → 08-17T14:13Z, 6,885
items) and that backfill was mined as a second pass, but the general
lesson stands: a skipped `/daily` costs collector coverage that only
partially recovers, not just a missing digest. The sanctioned
Sunday-evening mini-sweep exists for exactly this and was not run.

---

## 2026-08-18 /daily — 08-17 finalize (all three critic-bearing lenses) + 08-18 open

The 08-17 digest-day closed at 05:00 ET this morning; this pass finalized
it and opened 08-18. All four mental-health benchmarks and three of four
AI benchmarks published for the Monday, so this is a real recall check
rather than a weekend null.

### The structural finding: this map corrected itself three times, and only one was a miss

The critic's job is "they led with → we missed." This pass produced
something different and more useful: **three errors in this map's own
08-17 record**, none of which any benchmark would have surfaced, all
found by primary-source date-checking during the finalize.

1. **A five-month-old story ran as the day's lead diplomatic item.** The
   08-17 world-news digest and the front digest both carried "Aoun breaks
   with Hezbollah in front of von der Leyen and Costa," calling it "the
   day's one real diplomatic shift." The cited Reuters-via-Yahoo URL
   carries `Published Time: 2026-03-09T16:58:43Z`. **Retracted.** The real
   08-17 Lebanon story is close to its opposite: Aoun defending UNIFIL's
   continued presence against Israeli pressure to end it.
   ⚠️ **This is a recurring trap, not an accident.** Google News searches
   on this thread's terms return the January 2026 (Beirut visit) and March
   2026 (video conference) instances with near-identical wording —
   "comprehensive ceasefire… full Hezbollah disarmament… direct
   negotiations under international auspices." The
   `israel-lebanon-escalation` timeline now carries a standing
   check-the-`Published Time` rule at the top of the retracted block.
   🔁 **The irony is on the record and worth keeping:** the same bullet
   correctly excluded a 2024 "120 targets in one hour" claim as stale
   while itself being stale. Catching one trap in a bullet is not evidence
   the bullet is clean.

2. **An SEC acceptance timestamp was off by four hours, in the direction
   that flattered the story.** NVIDIA's 8-K was reported as "accepted at
   04:41 ET, four hours before the opening pass." EDGAR's own
   `ACCEPTANCE-DATETIME` header reads `20260817084133` and the submissions
   API `2026-08-17T12:41:33Z` — both **08:41 ET**. The original was a
   UTC-to-Pacific conversion mislabelled as Eastern. Substance survives
   (the filing was public before the pass that called the figure missing);
   the "four hours" did not. **Practice adopted: read EDGAR acceptance
   times from the `-index-headers.html` header, which is already ET, and
   never hand-convert the `Z` timestamp.**

3. **"No model releases inside today's window, confirmed twice" was
   wrong.** Alibaba launched **Qwen3.8-27B**, a laptop-class open-weight
   model, on Monday 08-17 (CNBC, 07:24 ET: *"On Monday, the Chinese tech
   giant launched an AI model, designed to run on consumer hardware like
   laptops"*). The failure mode is specific and worth naming: the sweep
   correctly dated **Qwen3.8-Max** to 08-12 — this map had logged its 2.4T
   weights in the 08-12 digest — and then generalised from the Max to the
   whole Qwen line, writing "Qwen3.8-Max/27B" as one already-counted
   event. **Two models, two dates, collapsed into one by a slash.**
   ⚠️ Note also that the AI critic reported this miss with the *wrong*
   reason — it read the 08-17 CNBC piece as the Max release and would have
   had this map retract a correct 08-12 entry. The main session
   adjudicated against both its own digest and the critic. Neither was
   right on its own.

### They led with → we missed

**ai / 2026-08-17** (benchmarks: The Rundown AI ✅ · TLDR AI ✅ ·
The Neuron ✅ · The AI Daily Brief ❌ did not publish)

- **Anthropic's annualized revenue run-rate topped $65B in July** — TLDR
  AI's 08-18 lead. Up from $47B (May) and ~$9B (end-2025); now ahead of
  OpenAI's ~$40B; investors expect $100–120B for FY2026 against a targeted
  $2T-plus IPO valuation this fall. **Independently surfaced by all three
  of this pass's non-world-news sweeps**, which is the strongest miss
  signal this log has recorded. ⚠️ Distinct from the $11.5B Q2 print
  logged as caught-late on 08-17 — quarterly vs. annualized run-rate,
  three days apart, and aggregators merged them all day.
- **Cursor launched "Origin," a code-hosting platform, during a 6h+ GitHub
  outage** — the lead of *both* TLDR AI's and The Rundown AI's 08-18
  issues. Invisible here rather than merely missed: this map has no thread
  on the developer-tooling layer as a competitive surface.
- **Microsoft fell ~3% (~$112B of market value) on 08-17** on a report
  questioning whether its installed AI-chip count (2.2M) matches its
  stated buildout targets (1.8M); Microsoft disputed the calculation.
  Market-moving, squarely on the hyperscaler-credibility beat, absent
  here. Context that makes it legible: Nvidia moved **+0.21%** the same
  day.
- **Stripe/OpenRouter, >$7B** — appeared in three of four AI benchmarks
  and was Axios Pro Rata's top deal item. ⚠️ **This map offered it as a
  thread candidate on 08-16 and again on 08-17 and never wrote it as a
  bullet.** Logged as a distinct failure mode: **a candidate is not
  coverage.** A $7B acquisition at a 5.4x markup on a three-month-old
  $1.3B Series B is an event whether or not a thread exists to hold it.
- **Borderline, logged with its caveat rather than promoted:** Dario
  Amodei's X reply to Gavin Baker led both The Rundown AI's and The
  Neuron's 08-17 issues — two independent editors' top story — but the
  trigger was the 08-14 All-In podcast and TechCrunch's report is dated
  08-16. Pre-window, not an 08-17 miss.

**global-capital / 2026-08-17** (Money Stuff ❌ vacation through 08-24 ·
Axios Pro Rata ✅ · FT Unhedged ✅ · Bloomberg Technology ⚠️ see below)

- **Anthropic $65B run-rate** — as above.
- **Stripe/OpenRouter >$7B** — Axios's "BFD."
- **Higgsfield's $400M Series B at $5.4B post** (DST Global-led, with
  Goldman Sachs Alternatives and Intel Capital). Annualized revenue
  reportedly ~$20M a year ago to $700M in August.
- **FT Unhedged led with "Broken FIMA"** — Bessent's push to expand the
  Fed's FIMA repo facility as a yen-defence backstop, argued to be
  structurally weak. 📌 **This retires an ambiguity in a standing watch
  item.** The FT yen/BOJ theme was flagged 08-14 as five-in-two-weeks and
  08-17 as a sixth run, with the bar set at "a discrete, named, live
  mechanism rather than analyst commentary on direction." *Broken FIMA*
  clears that bar — it names the facility, the official, and the policy
  ask. Promote or drop it on the next `/week`, don't flag it a seventh
  time.
- **Lower-confidence, recorded as such:** Bloomberg's "AI Rally Set to
  Trigger Stock-Market Correction, ECB Blog Says" (08-17). Blog-sourced
  commentary, on-theme against this lens's stretched-valuation signals.

**mental-health / 2026-08-17** (BHB ✅ · STAT Health Tech ✅ · Fierce
Healthcare ✅ · MobiHealthNews ✅ — all four, a Monday, a real check)

- **"Behavioral Health Dealmaking Down 20% in the First Half of 2026"**
  (BHB, 15:19 ET — nineteen minutes after the afternoon pass closed).
  Mertz Taggart Q2 2026: **69 closed deals in H1, −20% YoY**;
  mental-health-specific −20% for the quarter and **−25% for the half**;
  **addiction treatment from 19 closings in H1 2025 to 8**; I/DD and
  autism −14% and drawing the most consistent interest. Kevin Taggart on
  the cause: *"Anyone underwriting behavioral health right now is
  underwriting Medicaid more cautiously than in years past."* The largest
  MH deal on the board — the $653.4M municipal-bond-backed Advantage
  Behavioral/QCF transaction — **still has not closed.**
  **Why it matters as a miss:** this map tracked the individual
  transactions all week (UHS/Talkspace, the Centene CFO exit, Aetna/Alma)
  without the aggregate that explains them.
- **UHS CEO Marc Miller on what comes after Talkspace** (BHB, 09:10 ET) —
  a partial miss. The deal-closing fact was logged; the forward
  integration strategy was not.
- **Checked and NOT misses**, recorded so they are not re-checked: STAT's
  lead was the UnitedHealth IRS probe already covered; DocGo/Hicuity,
  Epic prior-auth, Medicare Platform's $50M, and a states'-role cost
  report are general health-tech with no behavioural-health angle. One BHB
  "Voices" column excluded as sponsored advertorial.

### Ledger outcomes this pass

**Hits:** `ping-an-h1-2026-interim-results` (due 08-18) — the 1833.HK
subsidiary reported on its due date, **and the AI-contribution disclosure
the entry was explicitly holding for exists: ~4.6% of gross profit**,
alongside 9.7M+ cumulative AI-doctor users. `likud-primary-results` (due
08-18) — slate published; Netanyahu's nine controlled slots held cleanly,
but his wider attempt to dilute hardline internal rivals failed.

**Slip:** `grok-4-7-ship` — slipped three days *ahead* of its own due
date, on a restatement. Musk's 08-12 post put release "3 to 4 weeks" out
from that date (early-to-mid September), already past 08-21. This is the
"double-slip on a chained promise" the entry's own `what_confirms`
anticipated; the second slip landed.

**New entry:** `ping-an-group-h1-2026-interim-results` (due 08-20),
pinned by the company's own voluntary HKEX/SSE announcement filed 08-13 —
closing the "group-level date not independently confirmed" gap the
subsidiary entry had carried since 08-04.

**Passed-silent, all re-checked at primary source and unchanged:**
`aetna-alma-rate-cut-effective` (every source previewing the 08-15 date
was published on or before 08-04; no post-15th confirmation exists from
Alma, an Aetna bulletin, or either psychological association), both
Kaiser/NUHW entries (Kaiser's own page still ends at 08-11 with no
outcome; NUHW's news index has nothing after 07-27), `cxmt-congress-letters`.

### The stale-year trap count on one ledger entry is now three

`kaiser-nuhw-mediation-*` has drawn false positives from **2022**
(logged 08-17), **2025** (logged 08-15), and now a **2025 bargaining-cycle
page surfacing under 2026-looking metadata** — a search result claiming
Kaiser and NUHW "met on Tuesday, August 26, 2026" that, fetched directly,
describes 2025 sessions. The rule already written into the entry — accept
nothing not fetched directly from the parties' own sites with a visible
2026 date — is what caught it each time. **It is working; leave it.**

### ⛔ Access finding that changes a routine: Bloomberg Technology RSS

**`feeds.bloomberg.com/technology/news.rss` cannot be used for
next-morning recall, and it fails silently.** It returns HTTP 200 with no
proxy and no spoofed UA, exactly as this file documents — but it is a
**rolling ~20-item window**. By 10:00 ET on 08-18 it had rolled past
**every** 08-17 item; all twenty were 08-18. A next-morning pull misses
the prior day in its entirety while looking perfectly healthy.
**This benchmark must be pulled same-day, ideally by early evening ET.**
WebSearch against Bloomberg's own dated bylined URLs substituted this
pass but is strictly weaker — it depends on search-index coverage rather
than returning a complete list.

### Other access findings

- ✅ **Three AI-benchmark routes are simpler than documented.** TLDR AI's
  RSS (`tldr.tech/api/rss/ai`) and its per-date URLs both resolve on plain
  curl with a Googlebot UA — no proxy. The Neuron's homepage renders a
  full dated archive on plain curl. **The AI Daily Brief's `sitemap.xml`
  is the fastest authoritative "did it publish" check** — date-guessed
  `/e/YYYY-MM-DD` URLs 404 cleanly when absent, so absence is provable
  rather than assumed.
- ⚠️ **The Rundown AI is a client-rendered SPA.** Its homepage href list
  resolves but its text does not; it must be walked by `/p/<slug>`, and
  there is still no per-date URL scheme.
- ⚠️ **Axios Pro Rata's reader proxy was NOT archive-blind this pass** —
  it was still serving the 08-17 edition at fetch time. The 08-15 note
  recording it as current-edition-only is right in general but should be
  checked against the `## <date>` header in the returned markdown each
  time rather than assumed either way.
- ⚠️ **MobiHealthNews's reader-proxy requirement extends to subpages**,
  not just the homepage (`/categories/payer` 403s on plain WebFetch).
- ⚠️ **Fierce Healthcare blocks individual article pages even to a
  Googlebot UA** — the UA that reliably clears BHB's Cloudflare does not
  clear Fierce's. Site-scoped Google News RSS returned real headlines and
  pubDates where the article pages stayed blocked.
- ⚠️ **FT Unhedged's RSS ceiling is title-plus-subhead.** Full article
  text sits behind a security interstitial that survives Googlebot
  spoofing. That is enough for recall scoring and not enough for a quote.
- ⚠️ **The Wayback Machine API returned HTTP 429 on both attempts** and
  was unavailable as a fallback channel this pass.
- ✅ BHB's Googlebot-UA workaround held with no further tightening.

### Cold-rotation note — the rotation is behind, and it cost real coverage

This pass swept nine threads that had gone **19–24 days** without a check
(the rotation's design target is ~7). Eight of the nine had moved, several
materially — including a **primary-source answer to a thread's own stated
live test** that had been sitting in Amazon's 10-Q since 07-30 (see the
`datacenters-as-targets` entry in the 08-18 digest). **A 7-day rotation
over 58 cold threads needs ~8 threads swept per run, every run.** At the
current rate the tail is being touched roughly every three weeks, and the
`mhpaea-parity-limbo` null — the only clean "nothing new" of the nine — is
the exception that shows the rest were worth the sweep.

## 2026-08-19 — frontier-ai: 08-18 finalize + 08-19 open

The 08-18 digest-day closed at 05:00 ET this morning; this pass extended
collection through the close, finalized the 08-18 digest
(`artifacts/digests/daily/2026-08-18-frontier-ai.md`), and opened the
08-19 digest as `building` (agentic-interim, mid-morning ET).

### Coverage critic, frontier-ai / 2026-08-18

TLDR AI and The Rundown AI both fetched directly and read in full for
their 08-18 issues; The Neuron's dated archive did not walk cleanly this
pass (its homepage returned a generic/undated headline list) so its check
is weaker and should be re-verified directly next time rather than
assumed clean. The AI Daily Brief again published no 08-18 news episode
(most recent is 08-17) — the third time in a week this outlet's
weekday-episode gap has been logged; read as an access/format
constant, not a fresh miss each time.

**They led with → we missed:** nothing found. Every lead item across
TLDR AI's and The Rundown AI's 08-18 issues (ChatGPT for Teens, the
finalized Stripe/OpenRouter deal, Groq's down-round, Anthropic's $65B
run-rate, Cursor's Origin launch) already traced to a story this map
carried on 08-18 or 08-17.

**What this pass added beyond benchmark parity, via direct primary-source
checks rather than benchmark recall:**

- **OpenAI paused RL training on its next model, Astra, for ~2 weeks**
  over signs it might cross the "Critical" cybersecurity-capability tier
  on OpenAI's own Preparedness Framework, disclosed alongside Sam
  Altman's TIME interview naming "various degrees of misalignment" —
  not one incident — as the actual cause. Flagged by Techmeme/Axios but
  not led with by any of the four daily benchmarks; found by fetching
  OpenAI's own announcement page and Fortune's/Time's coverage directly.
  Folded into the `openai-agent-security-incident` thread's TODAY block
  alongside the safeguards/Preparedness-Framework-rewrite finding
  already there from the 15:15 ET pass.
- **Anthropic is preparing supervoting shares for its seven founders**
  ahead of a possible late-September IPO (The Information, via
  Investing.com/BeInCrypto) — a governance story with no benchmark
  lead, surfaced by a direct search on the IPO-prep beat.
- **Google won a bankruptcy auction for Spirit Airlines' enterprise
  data ($10M) to train its AI models** — a second training-data-
  provenance story inside three days, after 08-17's Amazon/rare-books
  finding. Reinforces (does not replace) the training-data-provenance
  thread candidate already offered 08-17, now offered a second and
  final time with two same-window instances behind it.
- **Etched's $700M/$21B round has a shipped-hardware detail the
  building-pass bullet was missing:** the company confirmed it
  delivered its first production rack to Jane Street (both lead
  investor and first customer), already running Jane Street's trading
  workloads. Folded into the existing Release-watch bullet rather than
  written as a new one.

### Access note

TLDR AI's per-date URL scheme (`tldr.tech/ai/YYYY-MM-DD`) resolved
cleanly via WebFetch with no proxy needed for both 08-18 and 08-19
issues — consistent with the existing benchmarks.yaml note that this
outlet's RSS/per-date routes are simpler than most. The Neuron's
homepage did not return a clean dated list this pass (returned what
appears to be a rolling/undated digest of recent items rather than a
08-18-specific issue) — worth a follow-up check on whether it has a
per-date archive URL scheme like TLDR AI's, since this pass could not
find one.

### Proposed map changes (not applied — routed per this session's brief)

- **Entity gap, recurring:** no watchlist slug names an AI-training-data
  acquisition operation distinct from a hyperscaler's main entity —
  now hit twice in three days (Amazon 08-17, Google 08-18). Left open
  since 08-17; still open.
- **Thread candidate, now offered twice with two supporting instances:**
  "training-data provenance and exhaustion" (Amazon rare-books
  destruction for Nova + Google's Spirit Airlines data buy). Per the
  offer-twice-then-drop convention, this is its last offer before
  dropping.

## 2026-08-19 — mental-health: 08-18 finalize + 08-19 open

The 08-18 digest-day closed at 05:00 ET this morning; this pass extended
collection through the close, finalized the 08-18 digest
(`artifacts/digests/daily/2026-08-18-mental-health.md`), and opened the
08-19 digest as `building` (agentic-interim, late-morning ET).

### Coverage critic, mental-health / 2026-08-18

All four daily benchmarks checked. Behavioral Health Business fetched
directly via the documented Googlebot-UA route against `bhbusiness.com/feed/`
(no new tightening) and its individual article pages; STAT News via bare
curl; Fierce Healthcare and MobiHealthNews checked via their RSS/site-scoped
routes per the existing access notes — neither surfaced anything
MH-specific published after the 08-18 15:15 ET checkpoint.

**They led with → we missed (before this pass):** BHB's 20:06 ET lead,
**LifeStance Health's ~$3M settlement of a 1M-patient tracking-pixel data
privacy suit** (Meta/Google, March 2020–April 2023) — published after the
digest's prior checkpoint, folded in now under Clinical safety & harm.

**What this pass added beyond benchmark parity, via direct primary-source
checks and general web sweep rather than benchmark recall:**

- **NPR's investigation into Sophie Rottenberg's suicide** (died Feb 2025
  after confiding her crisis for months to a ChatGPT persona, disclosed to
  no human in her life including her own therapist) — not from any of the
  four trade benchmarks, found via general sweep. Judged material enough
  to add given this lens's standing evidence-gap thesis; folded into
  `ai-therapy-regulatory-reckoning` and `grok-companion-harm`.
- **Continuing detail on the Oakland Meta trial**, via AP/Hawaii
  Tribune-Herald and MLex: Deputy AG Megan O'Neill's opening ("the young
  ones are the best ones"), Judge Gonzalez Rogers admitting former
  engineer Arturo Béjar's testimony over Meta's objection, and Béjar's
  08-19 testimony that Meta's internal harm-surveillance measured
  policy-violation prevalence rather than actual harm. Folded into
  `social-media-causality-fight`, which also gained a note distinguishing
  this trial from the separate New Mexico case ($942M total, resolved
  08-06) alongside the already-noted Los Angeles verdict.
- **Checked and excluded, not misses:** two BHB 08-18 pieces — "Confessions
  from a Retired Addiction Treatment CEO" (BHB+, leadership profile/anecdote)
  and "Inside Caron Treatment Center's C-Suite Shakeup" — read in full and
  judged to carry no policy, capital, or clinical-evidence angle distinct
  from what this lens already tracks. Same treatment as the excluded BHB
  "Voices" column in the 08-17 finalize.

### Found this pass, not applied — flagged for Ben (routed per this
### session's brief rather than edited directly)

- **A likely real coverage gap: Colorado's HB26-1195 "Psychotherapy
  Artificial Intelligence Restrictions"** was signed into law 2026-06-03
  and took effect **2026-08-12** — a binding state law (not a proposed
  rule) that bars licensed mental-health professionals from letting an AI
  system conduct therapeutic communication outside real-time joint
  participation, and separately makes it unlawful for anyone to offer
  psychotherapy services to the public in Colorado unless delivered by a
  regulated professional. This is distinct from and stronger than the AG's
  Chatbot Safety Act rulemaking (proposed 08-11, effective 2027-01-01)
  that this map's `state-therapy-chatbot-bans` thread already tracks —
  and this pass found no prior digest or thread entry mentioning HB26-1195
  at all. It is six-plus weeks old, not a today-dated item, so it was not
  written up as a digest bullet under a wrong date; instead it is logged
  here as a probable backfill target for `/crawl` on
  `state-therapy-chatbot-bans`. See the full task report for source
  detail.

### Access note

No new blocks found. BHB's Googlebot-UA workaround against `bhbusiness.com`
continues to hold with no tightening, for both the feed and individual
article pages.

## 2026-08-19 — global-capital: 08-18 finalize + 08-19 open

### global-capital / 2026-08-18 (finalize)

**Benchmark status.** FT Unhedged published 08-18 ("AI: like a debt
machine" — hyperscaler debt issuance stressing credit and rates markets).
Bloomberg Technology's RSS window had already rolled past 08-18 by finalize
time (same known ~18h rolling-window limitation logged 08-17); recovered
two 08-18 items via `site:bloomberg.com` WebSearch fallback. Axios Pro
Rata's 08-18 edition was not isolated this pass; its 08-19 edition (checked
live) carried nothing global-capital-relevant. Money Stuff confirmed still
on vacation through 08-24 — clean non-publication, not a miss.

**Missed:**
- FT Unhedged's credit-spread framing ("AI: like a debt machine") — this
  map covered the equity-side rate-transmission channel in detail but not
  the credit-spread angle specifically. A related but undated data point
  (HY data-center-operator spreads widening since June, hyperscaler bond
  oversubscription falling from ~5x to <2x) was found during this pass and
  logged as background rather than forced into a dated bullet.
- Bloomberg Technology, 08-18: "Unitree Robotics Surges 460% After $904
  Million Shanghai IPO" — a China-robotics IPO event this map did not
  carry; the company is adjacent to `china-stack-independence` but not on
  the watchlist.

**Map effect:** none yet — both misses are single-item, not structural
gaps; Unitree Robotics is proposed as a watchlist add in this run's report
rather than added directly (guardrail-protected file).

**Both covered:** the 30-year Treasury's 19-year+ high and its
transmission into AI-complex equities (this map's own throughline)
converges with FT Unhedged's issuance-side framing. The Ohio guarantee's
circular-financing reframing (Fortune, 08-18) converges with this map's
own `ai-circular-financing-risk`/`nvidia-vendor-financing` coverage.

**We had, they didn't:** the finalize's own NVIDIA 13F read (SpaceX
$21B position, CoreWeave +94% add, Intel's mark-only growth) and the
WSJ's ~$3T off-balance-sheet figure (carried same-day) were not found
duplicated in any of the four benchmarks.

### Access note

WebFetch itself refused `ft.com` directly this pass; `curl` against the
same RSS URL (`https://www.ft.com/unhedged?format=rss`) worked cleanly —
same fix as documented in `sources/benchmarks.yaml`, re-confirmed.
Bloomberg's RSS URL redirects: `feeds.bloomberg.com/technology/news.rss`
now 301s to `bloomberg.com/feeds/technology/news.rss` — fetch the redirect
target directly rather than the documented `feeds.bloomberg.com` host to
avoid the extra hop. Axios Pro Rata's `r.jina.ai` reader-proxy fix
continues to hold.

## 2026-08-20 — three-lens finalize for 08-19

### frontier-ai / 2026-08-19

**Missed:** OpenAI's own newsroom post, dated 2026-08-19, announcing it
paused key stages of its most advanced AI training for two weeks,
deployed a new anomaly-detection system aiming to flag unauthorized
access or safeguard-disabling attempts within 30 minutes, and tightened
sandbox isolation/network controls — explicitly tied to the July
Hugging Face breach and the 08-07 Astra "Critical" cyber-capability
finding. TLDR AI led its 08-19 issue with this (story #2); Euronews,
Help Net Security, PYMNTS and CyberInsider all dated write-ups 08-19.
The 08-19 frontier-ai digest's opening pass closed ~11:00 ET and stated
"no frontier-lab product news dated today" — this post likely landed
after that pass closed. **Map effect:** RECONCILED, not a genuine miss — checked against
`openai-agent-security-incident`'s timeline and this exact
announcement (2-week RL pause, 30-min anomaly-detection window, tied to
the Hugging Face breach) is already logged there dated 2026-08-18
(OpenAI's own newsroom post + Fortune, same URLs). TLDR AI and the
other benchmarks appear to be covering the 08-18 announcement a day
late, not a new 08-19 event. No edit needed.

**Both covered:** GLM-5.3 API pricing, Cerebras CS-4 — both matched
TLDR AI's #1/#3 stories.

**We had, they didn't:** Cerebras's stock-reaction framing, the xAI
Minnesota hearing tracking, upcoming-date tracking (Apple/CXMT,
GLM-5.5, Grok-4.7) — none of the four benchmarks carry this kind of
dated-thread discipline.

**Methodology note:** an opening pass that closes mid-morning and
states "no news today" is vulnerable to same-day-but-later posts; a
later re-check before finalize catches this class of miss, which is
exactly what happened here.

### global-capital / 2026-08-19

**Missed:** Axios Pro Rata's own 08-19 lead item, "Walter's ripples" —
Mark Walter's Lakers sale drawing federal regulatory scrutiny onto how
major asset managers acquired life insurers that funnel capital into
private-credit deals, including loans from Walter-controlled insurers
into his own businesses. Squarely in `ai-buildout-debt-risk` territory
(opaque capital plumbing) but a distinct mechanism (insurer balance
sheets into private credit, not AI-buildout debt specifically).
Secondary: Bloomberg Technology's own lead web story, "Data Center
Opponents Force Big Tech to Try a Charm Offensive" — converges with a
thread candidate independently surfaced by this run's capex-cluster
check (see 08-20 digest's thread candidates).

**Both covered:** Money Stuff's Treasury-buyback/30-year-yield story
matched this map's own throughline in full.

**Access note:** FT Unhedged blocked via WebFetch directly against
`ft.com` this pass (same known issue, `curl` against the documented RSS
URL is the workaround — not re-tried this pass, logged as a gap not a
finding).

**We had, they didn't:** the Japan JGB/Nikkei selloff and its rate-
transmission mechanism, the SoftBank-13F/Intel parallel, SK Hynix's
buyback, the Google-Marvell warrant deal, Nebius's convertible notes —
a materially deeper capital-markets sweep than any single benchmark.

**Map effect:** proposed, not added directly — (1) a private-credit/
insurer-capital thread or watchlist entity around the Walter/life-
insurer pipeline; (2) the data-center-siting/local-opposition thread
candidate, independently corroborated by two sources this run.

### mental-health / 2026-08-19

**Missed, three items, all from the benchmark set itself:**
- Behavioral Health Business (08-19 19:46 UTC): Medicaid spending on
  core psychotherapy rose 156% from 2018-2024, to $6.68B overall (BHB's
  own CMS-data analysis).
- Behavioral Health Business (08-19 20:31 UTC): Oregon's first-ever
  U.S. state-regulated psilocybin study — ~350 adults, adverse effects
  "uncommon," 92.2% reporting improvement in depression/anxiety/overall
  wellbeing at one month. Belonged in the digest's own Clinical trials &
  evidence section, which instead only covered a recurring RSS
  re-appearance and an inaccessible JMIR piece.
- Fierce Healthcare (~08-19 3pm, lower confidence — read off the live
  homepage, not independently cross-confirmed): HHS awarded $96.7M in
  behavioral-health-services grants.

**Both covered:** UHS's Talkspace acquisition (MobiHealthNews vs. this
map's Healthcare Dive CEO-interview angle — same story).

**We had, they didn't:** the Colorado HB26-1195 backfill catch, the
STAT "grooming" First Opinion synthesis.

**Map effect:** the Oregon psilocybin study folded into
`psychedelic-regulatory-sprint`'s timeline at finalize (see below); the
Medicaid-spend figure logged as a evidence data point in the 08-19
digest at finalize; the HHS grant figure not folded in (confidence too
low without independent corroboration this pass) — worth a follow-up
check.


---

## 2026-08-21 critic pass — finalized 2026-08-20 (all four lenses; critic run on the three critic-bearing ones)

**The heaviest miss count this log has recorded, and two of the three
lenses missed on the same structural pattern: an axis the lens claims and
has no thread for.** Eight confirmed misses across three lenses, all
folded into the 08-20 digests as `🔍 CRITIC CATCH` items. Two thread
candidates came directly out of this pass.

### frontier-ai / 2026-08-20
- **Missed (5, all confirmed, all TLDR AI-led):** Anthropic's
  production-agent bundle — computer use + browser access + versioned
  Skills + a reusable Files API in one enterprise surface (claude.com/blog)
  · Google folding Antigravity into Gemini Enterprise Standard/Plus seats
  with VS Code GA and VS/JetBrains/Zed in preview (cloud.google.com/blog)
  · Mistral's Agentic Search — five tool-like actions (search, open,
  navigate, read, grep), FinanceBench accuracy 26.7% → 86% with token use
  −23.9% and P90 latency 255s → 154s (mistral.ai/news) · Slack code
  channels, human-agent build surfaces with GitHub/Anthropic/Vercel
  integrated (slack.com/blog; headline confirmed, post URL unresolved, so
  the date rests on benchmark attribution) · Harvey Tenet, a post-trained
  open-weight legal model built on Kimi K3 (harvey.ai/blog).
- **Checked and NOT folded in — four lower-confidence items, recorded so
  the same claims are not re-chased as fresh:** a reported ~$6bn
  Nvidia-Poolside licensing/acqui-hire (unconfirmed on either company's
  own channels, one aggregator) · an Anthropic Mac meeting-recorder
  "Parka" (absent from Anthropic's newsroom and claude.com/blog — may be a
  benchmark error) · a ChatGPT-Apple Messages integration (openai.com
  403'd, unverifiable) · The Neuron's "AT&T going half in on open models"
  lead (headline reachable, article 404, AT&T newsroom 403).
- **Map effect:** `mistral-ai` gained a timeline entry. The other four have
  **no thread to land on**, which is the finding — hence the
  **enterprise agent-product race** candidate, offered 08-20 and carried
  08-21. `kimi-distillation-fight` took the Harvey/Kimi K3 cross-reference
  in the digest but no timeline entry: a third party post-training on Kimi
  K3 is context for that thread, not a development in it.
- ⚠️ **Unaudited, NOT clean: The Rundown AI.** Every fetch of its homepage,
  `/archive`, `/articles` and paginated archive returned the same fixed set
  of 8 articles dated 08-06 to 08-19, confirmed against its own
  `sitemap.xml` (newest `lastmod` 08-19, "Pacing comes to the AI
  frontier"). One of four daily benchmarks in this lens was not checked at
  all. **The AI Daily Brief** was thin — 08-20 episodes were tips/opinion
  format, not news-lead. A WebSearch summary claiming an 08-21 episode
  about "Google paying $10M for Spirit Airlines' Slack messages" was
  discarded as garbled/hallucinated rather than reported. The critic also
  exhausted its WebSearch session budget mid-run and finished on WebFetch
  only.
- **Zero overlap** between our eight items and anything reachable in the
  benchmarks — no "both covered" line at all. Read as a signal about axis
  coverage rather than luck.

### global-capital / 2026-08-20
- **Missed (3, all confirmed):** FT Unhedged's own 08-20 lead — Bessent
  doubling Treasury buybacks in the 10-20y and 20-30y sectors effective
  09-09 into the worst long-end selloff in ~20 years, denying yield-curve
  control, with the 10-year closing back at 4.69% as the announcement
  rally faded; Evercore ISI's Krishna Guha calling it "a weak form of
  Operation Twist" that could backfire by signalling funding concern,
  Jefferies' Thomas Simons saying the timing/wording broke Treasury's
  communication norms, Moody's flagging a structural shift in Treasury
  demand · Bloomberg's scoop that **Meta pays Microsoft "hundreds of
  millions a year"** for Azure-hosted AI, trillions of tokens weekly,
  against OpenAI supplying ~70% of Microsoft's AI revenue · Bloomberg's
  harder Anthropic IPO story (raise benchmarked to SpaceX's $75-86.2bn
  record, Morgan Stanley/Goldman/JPMorgan already working it, public
  filing as soon as end-August) sitting behind our softer investor-chatter
  version.
- **Checked and correctly excluded:** Axios Pro Rata's 08-20 lead
  ("Stripe's singularity") verified as a re-lead of an 08-19 1:26pm ET
  scoop · Castelion's $1bn Series C at $13bn (JPMorgan SIG/a16z/Carlyle) —
  a genuine 08-20 event but defense-tech venture, not AI-buildout capital
  flow, and run as a secondary.
- **Map effect:** `ai-circular-financing-risk` gained the Meta/Microsoft
  entry · `frontier-lab-ipos` gained an 08-20 public-filing block and a
  ⚠️ correction (it asserted SpaceX was "trading at all-time lows ~15%
  below issue" while its own addendum two sentences later said SPCX had
  recovered above its $135 issue price) · one new expectation logged,
  `anthropic-public-s1-filing` (08-31). The Bessent story has **no thread
  to land on** — hence the **Treasury long-end stress** candidate.
- ⚠️ **Gaps.** **Money Stuff genuinely did not publish 08-19 to 08-21** —
  Levine on vacation, returning 08-24, confirmed by a dated-URL 404 and
  search results; empty, not unchecked. **FT.com blocks direct fetching**;
  the Unhedged front page and headline dates came through a
  text-extraction proxy, bodies stayed paywalled, so the Bessent substance
  is corroborated from CNBC rather than read in Unhedged's prose.
  **Bloomberg Technology's homepage** was behind a bot CAPTCHA; findings
  came from search results and Yahoo Finance mirrors quoting Bloomberg
  directly. WebSearch session budget exhausted mid-run.
- **We had → they didn't:** Nebius's upsized $5.0bn convertible with the
  concurrent $800M debt-for-equity exchange.

### mental-health / 2026-08-20
- **Missed (1 clean + 1 borderline):** Behavioral Health Business's own
  08-20 lead — **Radial acquiring the MSO behind Mindful Health
  Solutions**, forming a 27-clinic interventional-psychiatry network
  across CA/TX/WA/NY, 100+ clinicians, running accelerated TMS,
  SAINT/SWIFT, Spravato, IV ketamine, fMRI-EEG-guided PRISM and
  transcranial focused ultrasound; leadership Owen Muir MD (co-founder/
  CSO), John Capecelatro (CEO), Tobias Marton MD PhD (CMO), Carlene
  MacMillan MD (CPO), outgoing Mindful CEO Mark Kehoe to an advisory role;
  terms undisclosed. ⚠️ The cited "up to 79%" remission rates against
  5-30% standard care are a marketing claim in a transaction announcement,
  not a trial result, and the digest says so. · **Borderline, folded in
  and flagged:** HHS adding the Family-Based Recovery programme and the
  peer-support Wellness Recovery Action Plan to the Title IV-E Prevention
  Services Clearinghouse, making both federally reimbursable — underlying
  event dated **08-19**, so carried as a late catch rather than an 08-20
  miss.
- **Checked and correctly excluded under the event-date rule:**
  UnitedHealthcare's child/family behavioural-coaching expansion to 13M
  members (Fierce ran it 08-20 4pm; UHG newsroom 08-18) · BHB's "Medicaid
  psychotherapy spending up 156%" (08-19, already folded in at that day's
  finalize). **Judged not an MH story:** Cityblock's Homeward Health
  acquisition + $116M Series E (behavioural health is one line inside a
  Medicaid/dual-eligible model; the deal is framed around rural/MA
  expansion).
- **Map effect:** `mh-clinical-infra-funding` gained an 08-20 timeline
  block carrying both catches — its first movement since 08-18. No entity
  adds. No candidate: both catches land cleanly on an existing thread.
- ⚠️ **Gaps.** **STAT Health Tech is "checked but thin", not clean** — its
  live category page returned one 08-20 article (EHR summarisation, not
  MH) and its dated archive was unreachable; a paywalled or unindexed STAT
  mental-health piece from this window is the one real hole. **BHB and
  MobiHealthNews both 403'd on direct fetch**; findings came from search
  snippets and secondary indexing. The Radial deal is corroborated across
  three independent sources with matching detail and stands;
  absence-of-evidence on those two sites is weaker than a direct read.
- **Note on the prompt:** this critic was told going in that our 08-20
  digest was a single bullet and to assume a miss rather than confirm the
  quiet day. It was right to. Worth repeating on any lens whose opening
  pass runs unusually thin.

### world-news / 2026-08-20
- **No critic by design** (`coverage: na`) — this lens has no benchmark
  set. Finalized on a tier-2 geopolitics deep check instead, which added
  the overnight Sumy/five-oblast barrage, an unverified Finland airspace
  report, the US-Iran MoU lapse and the pivot to sanctions.

### Cross-cutting note — what this pass says about the map, not the sweeps
Three of the four benchmark publications in global-capital and two of
four in mental-health are now behind bot walls or paywalls that defeat
direct fetching, and one of four in frontier-ai was wholly unreachable.
The critic still worked, via proxies and search snippets, but the
absence-of-evidence half of every entry above is weaker than it was when
this log started. Two critics also hit the session WebSearch cap mid-run.
Recorded as a standing condition rather than a one-day complaint.

## 2026-08-23 (15:00 ET pass) — finalized 2026-08-22, all four lenses; the "no misses by construction" assumption tested rather than repeated

**The finding of this pass is methodological, and it produced a real
miss.** The 10:00 ET run had deferred 08-22's critic on the reasoning
that the three critic-bearing lenses' benchmarks are weekday-only, so a
Saturday pass "would return no misses by construction." That reasoning
was correct in outcome for **eleven of twelve** benchmarks. It was wrong
for the twelfth, and the twelfth is the one that mattered: **Bloomberg
Technology came back online during this audit**, after being logged
unreachable through both direct fetch *and* the `r.jina.ai` proxy at the
previous two checks — and it produced the only confirmed miss of the day.

**A benchmark logged as blocked is not a benchmark that will stay
blocked.** The whole value of this pass was refusing to convert "these
outlets don't publish Saturdays" into "there is nothing to check." Every
one of the twelve was checked against a live feed, archive page, or dated
URL probe, and marked "no Saturday edition" only where the actual date
gap was visible — a Friday entry followed directly by a Sunday/Monday
one, or a 307/404 on Saturday-dated URLs while weekday URLs returned 200.

### global-capital / 2026-08-22 — one confirmed miss
- **Missed (1, confirmed):** **Apollo's chief economist Torsten Slok
  finding that AI is compressing wages rather than cutting jobs.** Apollo
  compared US Labor Department wage data across eleven high-AI-exposure
  occupations — computer programmers, customer service representatives,
  financial analysts — using **Anthropic's own Economic Index** as the
  exposure measure. Employment effects came back "insignificant"; wage
  growth lagged, with the largest shortfall at the bottom of the income
  ladder.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-22/apollo-s-slok-says-ai-weighs-on-pay-without-cutting-jobs-yet),
  [Apollo — Daily Spark, primary](https://www.apollo.com/wealth/insights-news/insights/daily-spark/ai-lowers-wages-but-doesnt-cut-jobs))
- **Map effect: none possible, and that IS the finding.** This map has
  **no thread for AI's labour-market effect at all** — not a thin one, not
  a stale one, none. This is the same structural shape the 08-21 pass
  recorded twice ("an axis the lens claims and has no thread for"), now a
  third occurrence. Offered as a thread candidate on the 08-23 page.
- ⚠️ **Flagged as a candidate miss rather than a certain one, on
  sourcing:** what was fetched is Bloomberg's Technology *section front
  page*, not a confirmed capture of the "Bloomberg Technology" newsletter
  send. The story is real and dated 08-22 either way (verified
  independently against Apollo's own Daily Spark), so it is folded in;
  what is not established is that it was the newsletter's lead.
- **Resolved, not missed:** Money Stuff — no edition, and **confirmed
  dark since 08-13** ("Bilateral OTC Goat Hedge") via a working RSS
  endpoint rather than inferred from a blocked page. Ten days silent.
  Axios Pro Rata — no Saturday edition, newest header 08-21. FT Unhedged
  — published, led with "Chart of the Week: Who owns government bonds?",
  the third consecutive edition on the Treasury long end; **not scored a
  miss** (a chart-of-the-week analysis is not a dated event and the
  digests carry the substance), but it is the evidence the long-end
  thread decision now rests on.

### frontier-ai / 2026-08-22 — clean, audited
- **No benchmark published a Saturday edition**, each verified: The
  Rundown AI (no weekend entry anywhere 08-06 to 08-20) · TLDR AI
  (`2026-08-22` and `2026-08-15` both HTTP 307; weekdays 200) · The Neuron
  (archive 08-19 → 08-20 ×2 → 08-21 → 08-23) · The AI Daily Brief
  (`/e/2026-08-22` 404, `/e/2026-08-21` 200).
- 📋 **Operationally useful:** The AI Daily Brief **publishes Sunday but
  not Saturday**. Tomorrow's pass therefore has a real 08-23 edition to
  check 08-23 against — this is the one benchmark that will produce a
  genuine Sunday comparison.

### mental-health / 2026-08-22 — clean, audited
- **No benchmark published a Saturday edition:** Behavioral Health
  Business (still silent since 08-20, re-confirmed not assumed) · STAT
  Health Tech (health-tech vertical newest 08-20; its general feed's
  Friday items are not Health Tech) · Fierce Healthcare (three items
  08-21, then 08-20, 08-18) · MobiHealthNews (08-19 → 08-20 → 08-21).

### ⚠️ Benchmark access health — four changes and two new workarounds
| benchmark | prior state | now | note |
| --- | --- | --- | --- |
| Bloomberg Technology | blocked direct AND via proxy | **reachable via `r.jina.ai`** | produced this pass's only miss |
| The Rundown AI | RSS 404, two days running | **reachable, HTTP 200 direct** | re-test next run; may not hold |
| FT Unhedged | needed the proxy | **direct fetch works again** | documented workaround may now be unnecessary |
| Money Stuff | "dark since 08-13", inferred | still dark, **confirmed via RSS** | `.rss` suffix on the author-page URL is the only working path |

**Two workarounds not previously in `sources/benchmarks.yaml`, and worth
adding:** **The Neuron** fails on direct fetch *and* on a Googlebot UA —
only the `r.jina.ai` proxy returns its archive. **Fierce Healthcare**
needs a Googlebot UA specifically against `/rss/xml`, not
`/feeds/all/rss.xml`.

**Read the pattern, not the row:** three of these four moved in a week,
in both directions. Access state is not a property to record once — it is
a thing to re-check every pass, and the cost of assuming it is stable is
exactly the miss above.

---

## 2026-08-24 (10:00 ET pass) — finalized 2026-08-23, all four lenses; two misses, and a benchmark that was "reachable" while serving nothing

**The pass in one line:** two genuine misses across three critic-bearing
lenses, and the more consequential finding is a *silent* benchmark
failure — STAT Health Tech's vertical feed had been redirecting to a
signup page that returns HTTP 200 with zero articles, so every
reachability check on it passed while it delivered nothing.

### mental-health / 2026-08-23 — one confirmed miss, found only after fixing the feed URL

- ⚠️ **MISS: "FDA digital health leader promises generative AI regulatory
  guidance is coming"** — STAT Health Tech (STAT+), by Mario Aguilar.
  Published **2026-08-24 08:30 UTC = 04:30 ET**, which is **30 minutes
  inside** digest-day 08-23 (it closes at 05:00 ET on 08-24) and well
  after this digest's last building pass at 15:45 ET on 08-23 — that
  timing gap is exactly how it slipped.
  https://www.statnews.com/2026/08/24/fda-rick-abramson-generative-ai-guidances-are-coming/
  Rick Abramson, the FDA's head of digital health policy, said on the
  record that the agency's goal is "formal policy guidance" on generative
  AI, and to expect "not only broad guidance on the overall topic of
  generative AI, but also some more narrowly constructed specialty
  guidance on particular generative AI topics." Verified independently by
  this session against the feed's own `pubDate`, not taken on the
  critic's word.
  **Routes to `ai-therapy-regulatory-reckoning`** (weight 3), whose
  `watch` field reads "track the first real regulatory pathway
  (FDA/MHRA)" and whose `terms` include "FDA therapy chatbot".
  ⚠️ **Read it for what it is:** a forward-looking *promise of* guidance,
  not a rule and not therapy-chatbot-specific. It is a watch-relevant
  data point on the thread, not the pathway arriving.

- **Not misses:** California AB 2575 (covered, verified against the
  Legislature's own bill record) · the Kaiser 9→3 triage staffing cut
  (covered with a full timeline block) · Warner's Meta CSAM-ads letter
  (correctly identified as a duplicate of the 08-20 logging).

### frontier-ai / 2026-08-23 — one confirmed miss, borderline on routing

- ⚠️ **MISS: Sam Altman says the AI industry's *messaging* is the problem,
  not the substance of the backlash** — The Neuron, published
  **2026-08-23 18:15 UTC = 14:15 ET**, inside window.
  https://www.theneurondaily.com/p/why-sam-altman-thinks-people-hate-ai
  (source clip: David Senra's podcast). Altman said AI builders —
  "subtext for really, mainly Dario" — have spent years talking about
  extinction risk and job loss and "have not as a field done a very good
  job" explaining benefits or mitigations, and pitched AI as delivering
  "more power and personal freedom" and possibly "the greatest boom in
  people starting smaller businesses that we have ever seen."
  **Why it is a real miss and not an Abbott re-run:** our 08-23
  throughline was the *politics* of the buildout via Governor Abbott.
  This is the other side of the same argument — the industry's CEO
  critiquing his own field's public case — on the record, same day.
  ⚠️ **Routing is borderline and recorded as such.** Filed to
  `ai-datacenter-sites` because that thread already houses the backlash
  storyline, but it is **not** a clean match on that thread's actual
  siting/moratorium/approval terms. **No thread on the map covers
  industry messaging or public trust as a subject.** That is the second
  independent signal this week pointing at the same hole.

- **Not misses:** Abbott's remarks and four conditions · OpenAI policy
  chief Lehane on mandatory pre-deployment safety standards · the
  Micron/Hot Chips memory-wall figures · Nvidia's >15% server price rise,
  the UAE chip-export piece and Alibaba's share sale (all correctly
  identified in-digest as re-datings of 08-22-or-earlier events).
- 📋 **For tomorrow's pass, not today's:** TLDR AI's **08-24** edition
  leads with the Hugging Face $13bn valuation, sourced to runtimewire.com
  — a second outlet on a story our 08-22/08-23 digests correctly declined
  to log as unconfirmed. It lands in digest-day 08-24, not 08-23.

### global-capital / 2026-08-23 — clean, and corroborated rather than assumed

- **No misses.** The Sunday thinness was tested three independent ways
  rather than inferred: FT Unhedged's feed jumps Sat 08-22 → Mon 08-24
  with no Sunday edition · Axios Pro Rata's latest is Fri 08-21 · only
  one item on Bloomberg Technology's whole front page carried an 08-23
  date, and it was a social-media-addiction trial explainer that routes
  to no `global-capital` thread.
- **Both covered:** Deutsche Bank's "soft-form financial repression" call
  and the FIMA/euro-funding plumbing detail behind it · the $40tn /
  $2tn / $1tn fiscal figures · Alibaba's HK$80bn placement (correctly
  bucketed to 08-22 with the timing call flagged in-digest) · confirmed
  PBOC/BOJ/G7 silence on 08-23.
- 📋 **Carried, still unverifiable:** FT Unhedged's Mon 08-24 01:30 ET
  item, "The great re-equitisation and the dollar," falls inside
  digest-day 08-23 but is paywalled past its subhead through the feed,
  the reader proxy, and search alike. Logged as a lead to re-fetch, **not
  as a covered item and not as a miss** — its title implies continuity
  with the dollar/re-equitisation theme already carried, but that could
  not be confirmed, so it is not being treated as either.

### ✅ Nvidia/Poolside — the carried lead is RESOLVED as still-single-source

Three runs have carried a reported **~$6bn Nvidia licensing deal with
Poolside**. This pass traced the full attribution chain and the answer is
now definite rather than open: **every outlet re-reports one scoop.**
Bloomberg's own headline says it outright — "Nvidia to Pay AI Startup
Poolside a $6 Billion License, **Newcomer Says**" — and PYMNTS states
that The Information's 08-21 piece was itself "citing a paywalled post by
Newcomer." Newcomer's 08-20 scoop rests on a Poolside investor letter it
says it reviewed. **No Nvidia or Poolside spokesperson, filing, or
primary statement appears anywhere in the chain.**
**Disposition:** stop re-checking it as an open lead. It stays unlogged
as fact; it becomes loggable only if a primary source or a genuinely
independent outlet appears.

### ⚠️ Benchmark access health — one silent failure, one stale stream

| benchmark | prior state | now | note |
| --- | --- | --- | --- |
| **STAT Health Tech** | "reachable" | ⛔ **was serving nothing** | the documented URL 301s to a **signup page returning HTTP 200 with zero articles** |
| **The Rundown AI** | "reachable, HTTP 200 direct" | ⚠️ **reachable but STALE** | feed *and* archive both newest at **08-20**; nothing for 08-21/22/23/24 |
| TLDR AI | — | ✅ checked clean | no Sat/Sun editions exist; matches its stated weekday cadence |
| The Neuron | proxy-only | ✅ proxy works as documented | produced this pass's frontier-ai miss |
| The AI Daily Brief | publishes Sun not Sat | ✅ real 08-23 edition confirmed | content was opinion/thought-leadership, no thread intersection |
| BHB · Fierce · MobiHealthNews | weekday-only | ✅ all three reachable | BHB confirmed genuinely dark since 08-20 via its own `lastBuildDate` |
| Money Stuff | dark since 08-13 | ✅ still dark, confirmed | now **eleven days**, via the working `.rss` path |

**The lesson this pass actually teaches, and it is a new one:** the log
has been recording benchmarks as *reachable* or *blocked*, and both of
today's access findings fall outside that pair. A feed that 200s while
serving a signup page, and a feed that 200s while its publisher has
stopped publishing, are both **"reachable and useless"** — and a
reachability check cannot tell either of them from health. **Check the
newest item's date, not the HTTP status.** Had that been the standard,
STAT's failure would have surfaced whenever it began rather than on the
day it happened to cost a miss.

⚠️ **Also worth stating: this makes STAT Health Tech's whole recent
history of "no misses" untrustworthy.** It cannot be known how long that
redirect had been in place, so prior clean results against this benchmark
should be read as unverified rather than passed.

### world-news / 2026-08-23
`coverage: na` — this lens carries no benchmark critic by design.

## 2026-08-25 (10:00 ET pass) — finalized 2026-08-24, all four lenses; three misses total, two access flags that recur

**AI lens: 6 misses found, 2 acted on.** Solid: "Ox Alpha," an anonymous
no-lab-attached model dropped on OpenRouter over the weekend with a
1M-token context window and frontier-level coding scores — zero prior
coverage anywhere in this map, no thread to route it to, offered as a
candidate. Anthropic's bankers reportedly guiding investors toward a
>$100bn IPO raise (October listing) — escalates past this map's existing
$75-86.2bn benchmark, routed to `frontier-lab-ipos`. Four secondary/
lower-confidence items not folded in: Claude Mythos 5's security-product
integration, Grok Bot's plan expansion, an $18bn Alibaba/Tencent infra
figure (traces to the already-known `alibaba` tagging gap, not fresh),
and an unverified Blackstone/Anthropic 160-engineer-embed claim.
Access flag: **The AI Daily Brief published no Monday edition at all** —
a genuine cadence break, distinct from its documented Saturday-only gap;
re-check rather than assume it resumed. Also noted: The Rundown AI's feed
mixes three separate newsletters (AI/Robotics/Tech) in one stream, worth
filtering to the AI edition specifically going forward.

**Mental health: 1 miss.** Behavioral Health Business published "New HHS
OIG Audits Expose Failures in Parity Enforcement, Compliance" at 14:54 ET
on 08-24 — inside the digest's own window — walking through four state
OIG audits finding Medicaid MCOs apply higher denial rates to
behavioral-health prior authorizations than medical/surgical ones. Missed
because the day's checks looked for a *new federal action*, not trade-
press synthesis of existing audits. Routed to `mhpaea-parity-limbo`
(timeline entry written). All four benchmarks reachable and genuinely
live for 08-24 via their documented workaround transports.

**Global capital: 1 miss, 2 benchmarks not fully checkable.** Matt Levine
asked "Who Should Control Anthropic?" in Money Stuff on 08-24 — a direct
governance question about the exact company this lens tracks through its
IPO chatter, with zero governance debate on the map that day. Article
paywalled past the RSS headline, so only its existence/topic is logged,
not its argument. Routed to `frontier-lab-ipos`.

⛔ **Bloomberg Technology re-blocked** (CAPTCHA, both direct and
reader-proxy transports) after being marked reachable on 08-23 — that fix
did not hold, confirming the escalation pattern `sources/benchmarks.yaml`
already warned about ("worth re-testing periodically rather than assuming
a fix stays fixed"). Could not check its 08-24 coverage at all.

⚠️ **Axios Pro Rata's reader-proxy technique is now known to be
unreliable for anything but same-day checks** — the proxy renders
whatever is the *current* day's issue, not an archive by date, so a
check running on 08-25 against 08-24's digest got served the 08-25
edition instead. Written into `sources/benchmarks.yaml` below; this
technique needs a same-day-only caveat attached wherever it's documented.

⚠️ **FT Unhedged: reachable but content-paywalled.** The RSS confirms a
real, correctly-dated 08-24 edition exists, but the article body is fully
paywalled even through the reader proxy, with no cached copy found — so
this benchmark's coverage could be confirmed to exist but not checked for
substance.

**`world-news` / 2026-08-24** — `coverage: na`, this lens carries no
benchmark critic by design.

### `sources/benchmarks.yaml` updated with today's two new access notes
(Bloomberg Technology re-block, Axios Pro Rata's same-day-only proxy
limitation) — see that file's own access-notes header.

---

## 2026-08-26 critic pass — finalized 08-25 (all three critic-bearing lenses)

### ai / 2026-08-25
- **Missed: nothing.** The critic flagged four items; a dedicated
  verification sweep found **all four resolve to already-closed
  digest-days**, so none is an 08-25 miss.
  - Nvidia/SpaceXAI orbital compute + Vera CPU → **08-24 11:00 ET**
  - Taiwan indicts nine over B300 smuggling → **08-24 06:02 ET**
    (already in the 08-24 digest; our own semis sweep had dated it
    correctly and the critic had not)
  - Nvidia "Groq 3 LPX" full production → **08-24 11:00 ET**
    (already in the 08-24 digest)
  - Anthropic flagship at ~11% of spend, per FT/Ramp → **08-23**
- **Root cause worth keeping:** three of the four trace to a single
  coordinated Nvidia press wave, all three releases stamped
  `2026-08-24T15:00Z`. One wire event syndicated widely reads to a
  next-day newsletter scan as three stories and to a cluster-scorer as a
  very high outlet count. **Both of this map's detectors share a blind
  spot for wire-syndication timing.**
- **One substantive correction, not just a date one:** the FT/Ramp figure
  is 11% of spend *on Anthropic's own tools*, not 11% of the corporate AI
  market, and the piece reports a **plateau** (flagship flat at ~11% two
  months post-launch, cheaper Claude Opus 5 already ahead on enterprise
  dollars). Filing it as flagged would have recorded a success where the
  source reports weakness.
- **Map effect:** one late catch filed under 08-24's marker without
  reopening that day — SpaceXAI adopting Vera/NVL72, onto
  `nvidia-order-book`. No watchlist or thread adds.
- **Unverifiable:** none — all four benchmarks reached, the best access
  this lens has had in a week.

### global-capital / 2026-08-25
- **Missed:** nothing that clears the date-check bar.
- ⚠️ **But two of four benchmarks were unauditable, so the honest verdict
  is "no evidence of a miss," not "recall clean."** Bloomberg Technology
  was fully CAPTCHA-blocked on every path (reproducing the re-block this
  digest already logged for the same day). FT Unhedged gave headline only
  — the `?format=rss` endpoint confirmed the issue exists, but the body
  was blocked by direct fetch *and* by the reader proxy. **The access note
  in `sources/benchmarks.yaml` oversells that fix:** proving an issue
  exists is not the same as judging what it led with.
- **Map effect:** one real catch from *outside* the window — the SEC
  subpoenaing Goldman Sachs, JPMorgan, Citigroup and Bank of America over
  exposure to Situational Awareness (Bloomberg, **08-24**). It had fallen
  between two digest-days, appearing in neither the 08-24 nor the 08-25
  page. Filed to `ai-circular-financing-risk` under an ⟨daily 2026-08-24⟩
  marker.
- **Unverifiable:** Bloomberg Technology 08-25 · FT Unhedged 08-25 (body).

### mental-health / 2026-08-25
- **Missed:** one — MobiHealthNews's Q&A on a US military trial of
  Mentaily's "LIV" AI avatar against the CAPS clinician-administered PTSD
  scale (08-25 08:00 ET). Folded into the digest and routed to
  `ai-therapy-evidence`.
- **Why it slipped four sweeps:** it is a feature/Q&A, not breaking news,
  so it never clustered across outlets the way an FDA action or a lawsuit
  would — precisely the blind spot the benchmark critic exists to cover.
- **Both covered:** Sword Health/Headspace, the shared lead of both BHB
  (13:47 ET) and STAT Health Tech (16:46 ET), logged inside the same
  afternoon window they broke it in.
- **Map effect:** no watchlist or thread adds — `ai-therapy-evidence`
  already existed and its watch text covers exactly this question.
- **Access-note change applied to `sources/benchmarks.yaml`:**
  MobiHealthNews's **homepage** no longer clears the r.jina.ai proxy (the
  Cloudflare challenge now survives the render); the **RSS path** through
  the same proxy still works. Third escalation on this one benchmark, and
  the second time a working fix decayed rather than broke outright.
- **Unverifiable:** none — all four benchmarks reached.

---

## 2026-08-27 critic pass — finalized 08-26 (all three benchmarked lenses; the day's back half, 15:00 → 05:00 ET, had never been curated)

### ai / 2026-08-26
- **Missed:** Nvidia in talks to buy Hugging Face for ~$13bn (surfaced by
  the *global-capital* critic, not this one — Bloomberg 20:56 ET) ·
  Perplexity × Nvidia "Portable Computer," a fully local zero-token-cost
  agent (TLDR #2, Rundown, Neuron) — **not an 08-26 miss: the Nvidia
  briefing was 08-24 and VentureBeat published 08-25, and no digest on any
  of those days caught it.** A genuine gap, filed against the wrong day.
- **Artifacts, not misses (3 of 4 candidates):** OpenAI's Jalapeño chip
  benchmarks (Rundown + TLDR leads) broke 08-25 at Hot Chips and is
  already in our 08-25 digest in full · Anthropic's $30T IPO TAM claim
  (Neuron lead) broke 08-25 via WSJ and is covered in two prior digests ·
  both were next-morning re-serves. **The date check earned its keep
  again**: three of four candidates dissolved on it.
- **We beat a benchmark:** The Rundown led with the Z.AI/Ox Alpha
  resolution in its **08-27** issue. We ran it 08-26.
- **Map effect:** none. No auto-adds — three candidates were artifacts and
  the fourth carries an open scope question (below).
- **Open scope question for Ben:** The AI Daily Brief gave its whole 08-26
  episode to Druckenmiller's AI-written WSJ op-ed and the backlash over
  AI-generated writing in finance media. **This lens has no strand for
  AI-authorship/disclosure debates.** The critic declined to name a thread
  on one data point, correctly. In or out of scope?
- **Access:** all four benchmarks reachable, no failures.

### mental-health / 2026-08-26
- **Missed:** Onos Health's $17M Series A, payer-facing behavioural-health
  analytics with CVS Health Ventures participating (BHB 10:00 ET,
  MobiHealthNews 11:07 ET) · the Sword Health / Headspace **price** at
  $200-300M (Fierce 12:30 ET).
- ⚠️ **Both landed inside 05:00-15:00 ET — the window this digest had
  already reported as EMPTY across two live passes.** The critic
  overturned the day's own finding; the throughline was rewritten.
- **The narrow call, made deliberately:** the Headspace *acquisition* is
  **not** a miss — our 08-25 digest logged it same-day off the filing and
  said explicitly that terms were undisclosed (STAT's 08-25 piece agrees:
  "the value of the transaction was not disclosed"). **Only the price is
  new**, and it is what changes the deal's meaning: ~$200-300M against a
  $3bn 2021 valuation.
- **Map effect:** proposed entity **Onos Health** → `mh-clinical-infra-funding`
  (not auto-added; offered to Ben). No new threads — both items fit
  existing ones.
- **Access:** all four reachable on documented paths. ⚠️ Fierce Healthcare's
  RSS cleared on a **plain curl**, no Googlebot UA needed — the documented
  requirement may have loosened, but the domain still rate-limited a later
  article fetch. **Not amending the yaml on one observation.**

### global-capital / 2026-08-26
- **Missed:** **Nvidia in talks to buy Hugging Face, ~$13bn** (Bloomberg,
  20:56 ET, timestamp from the article's own metadata) — **the real catch
  of this pass.** It broke in the back half that this very run was
  reconstructing, and the back-half sweep still missed it. Filed to both
  the global-capital and frontier-ai digests.
- **Checked and judged out of scope:** CrowdStrike's beat (16:12 ET) and
  Okta's raised outlook (16:05 ET) — real same-day events, no thread, no
  axis. Recorded so the decision is visible.
- **Unresolvable:** FT Unhedged ("Prediction markets revisited") and Money
  Stuff ("Predict the KPIs") **both led on prediction markets on 08-26,
  independently.** Bodies paywalled on every path. Cannot be scored either
  way; **two benchmarks converging on one theme in one day is worth a
  follow-up pass** with paywall-clearing access.
- **Map effect:** proposed entity **Hugging Face** + a candidate thread for
  AI tooling/distribution consolidation — offered, not added, since neither
  company has confirmed.
- ⛔ **Access — this was the weakest pass of the three, and structurally so:**
  - ✅ **Money Stuff's author RSS is BACK.** `benchmarks.yaml` still records
    it "dark since 08-13"; **that note is stale.** Dates/headlines only.
  - ⛔ **Axios Pro Rata's reader-proxy path is SAME-DAY ONLY** — no dated
    archive URL, and no Wayback capture for 08-26. **This structurally
    breaks the benchmark for finalize passes, which by design run the next
    day.** The critic could only retrieve 08-27's issue. Worth solving
    rather than re-discovering every pass.
  - ⛔ **Bloomberg Technology's homepage re-blocked** on all three transports.
    Undocumented working feed found: `feeds.bloomberg.com/technology/news.rss`
    — but it is a rolling recent-items list, not a lead ranking, and had
    already scrolled past 08-26's morning.
  - **FT Unhedged's RSS worked as documented**; body paywalled.

### Cross-lens note — the miss the critics did NOT catch
Neither the benchmark critics nor the mechanical world-news pool surfaced
the **Nepal-Tibet glacier collapse and outburst flood** (~360 dead,
~1,380 missing across two countries). It is outside every benchmark's beat
by construction — all twelve are AI, health-tech or finance publications.
**The flash rail is the only mechanism this map has for a general-news
event of that scale, and it depends entirely on the world-news sweep
noticing.** On 08-25 it did not, and nothing else would have. Recorded as a
structural gap, not a sweep error. See the 08-27 world-news digest.
