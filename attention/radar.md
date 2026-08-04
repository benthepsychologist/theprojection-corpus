# Radar — Ben's big questions

*The active steering layer. Seeded 2026-07-20 by one-time copy from the
reference repo (as of 2026-06-28); kestrel's alone from here — no sync-back.
Q7 (money) scoped by Ben the same day.*

Three linked layers: **BIG QUESTIONS** (this file — each with a **mode**:
`answer` = actively trying to resolve · `monitor` = stay aware · `both`, and a
**pattern**: how we work or feed it) · **WATCHING** → [`threads.yaml`](threads.yaml)
· **INTERESTING** → [`watchlist.yaml`](watchlist.yaml).

**Steer it:** edit this file, or tell an agent "add a question", "track X",
"work Q3 this week", "drop Y". Working a question = targeted research +
updating its **Working notes**; monitoring keeps it fed through the digest.

---

## Q1 — Who are the players, and what are they DOING?
- **mode:** monitor (+ periodic per-player synthesis) · **lens:** ai + mental-health · **status:** open
- **pattern:** sweep each major player by name; surface launches / announcements /
  partnerships / filings. Giants + frontier labs + MH players per `watchlist.yaml`.
  Active move: a recurring *"what is <player> building now?"* synthesis per player.
- **working notes:**
  - 2026-06-28 synthesis (pre-seed, in the reference repo's `monitoring/syntheses/`):
    throughline — **the contest moved from "best model" to "who controls the
    stack"** (compute + distribution); giants hedging off the labs (Apple→Gemini,
    Microsoft→MAI, Amazon→Anthropic); silicon is the battlefield. Spawned threads
    `microsoft-mai-openai-decoupling`, `apple-gemini-model-deal`,
    `ai-therapy-regulatory-reckoning`. ⚠ Three weeks stale — first kestrel
    synthesis should re-verify.
  - 2026-07-24 (ben-steer): **the board (`attention/board.yaml`) is now the
    operational frame for THIS question** — "in our kingdom model we want to
    know what each actor and organization are DOING." Each actor's threads
    *are* the answer; a board actor with **no live thread is an unanswered
    Q1 by construction.** The per-player synthesis sharpens to: *for each
    board actor, is there a thread answering what they're doing?* — the
    dormant actors are the worklist. Surfaced by **SpaceXAI going `dormant`
    (07-24)** — a Kingdom that owns its mines (Colossus) yet we track
    nothing it's doing. Candidates offered below, awaiting promotion:
    - `spacex-colossus` (ai) — xAI/SpaceXAI's self-owned training-compute
      buildout (Colossus, Memphis); the "owns its mines" angle that makes
      it structurally distinct from OpenAI/Anthropic (who rent). Strongest.
    - `grok-frontier` (ai) — the Grok line's trajectory + competitive
      position (Grok 4.5 shipped mid-pack/cheap; next-rev + frontier-gap).
    - `spacexai-public-megacap` (money) — the merged SpaceX/xAI/X public
      entity (~$2.1T since June); financing + rocket↔AI↔social cross-hold.
    - (mh/ai-safety option) Grok companion/output harm — Ben's sharpest
      lens if there's a live MH angle; needs a `/crawl` to confirm current
      facts before opening.
  - week 08-04 (/week, closing week 07-27–08-02): the board frame above is
    bearing out. xAI was formally classified 07-28 as an L2 subnode of
    SpaceX (the deepmind@google pattern) — its capital/thrust/gravity now
    consolidate at the parent while Grok/Colossus stays a distinct node
    for threads — resolving the dormant-SpaceXAI gap this note flagged
    07-24. All three candidates offered then are now live, promoted
    threads (spacex-colossus, grok-frontier, spacexai-public-megacap, the
    last now under a new meta-thread frontier-lab-ipos alongside a new
    anthropic-ipo-timing). The four-axis model went live 07-27 and the
    board grew 77→92 orgs this week (gov-pool agencies, insurers, 7 health
    payers) with 53 of 92 now carrying full numeric axes, so "is there a
    thread answering what this actor is doing" is checkable at a glance
    for most of the board, not just last week's 21-actor pilot. Two real
    per-actor misses this week: Anthropic's IPO filing was logged "thin,
    rumored" for two months when Anthropic's own newsroom announced it
    2026-06-01 (now corrected); and the Fed-chair gap (Q7) is itself a
    Q1-shaped miss — the single most consequential unnamed "player" on the
    whole board. Next dormant-actor cross-reference (board actors vs. live
    threads, now at 92 orgs) not run this cycle — flagged for next /week.

## Q2 — Where is the money going?
- **mode:** both · **lens:** ai + mental-health (money lens will absorb/extend this) · **status:** open
- **pattern:** funding rounds, capex, M&A, IPOs, big deals. Sources: news sweep,
  SEC EDGAR. Active move: periodic *"where is capital concentrating"* synthesis.
- **working notes:**
  - 2026-06-28 synthesis (pre-seed, reference repo): **capital concentrating into
    a few names at sovereign scale, funding the bottleneck (compute/energy/memory),
    not models**; macro risk = circular financing (>$800B loops, OpenAI ~-$14B/yr).
    MH funding renaissance flowing to clinical infra, not consumer chatbots.
    Spawned `ai-circular-financing-risk`, `stargate-buildout`,
    `mh-clinical-infra-funding`. ⚠ Stale — re-verify.
  - week 08-04 (/week, closing week 07-27–08-02): this note is superseded
    by something more specific, not dead. The mechanism clarified this
    week is not a generic financing loop — it's hyperscalers extending
    off-balance-sheet credit guarantees to third-party developers (three
    instances in seven days: Meta/BlackRock, Nvidia/OpenAI, Google/
    Anthropic), which lowers the guaranteed party's borrowing cost without
    the guarantor issuing debt or carrying the asset. That's cheaper
    capital for the buildout but contingent credit risk that stays largely
    undisclosed until something breaks — which is exactly what happened
    one lever down the chain when Leopold Aschenbrenner's Situational
    Awareness fund (~4x leveraged on AI-infrastructure bets) was forced to
    sell its entire book to Citadel, the first AI-thesis fund broken by
    the trade it was betting on. The W1-W6 capex-tree crawls this week
    also filled in the destination layer concretely: Amazon raised FY2026
    capex guidance to ~$220B from ~$200B explicitly citing higher memory
    costs, the first hard evidence the memory-price shock is now moving a
    hyperscaler's own capex line, not just its cost line. Track the
    guarantee count and the CDS/loan-spread level going forward, not
    survey sentiment — see Q7 for the credit-market read in full.

## Q3 — Is mental-health tech getting more rigorous, or is hype winning?
- **mode:** answer (the book's thesis) + monitor · **lens:** mental-health · **status:** open
- **pattern:** evaluator reports (PHTI/ICER/ORCHA), trials, research, regulatory +
  enforcement actions, retractions, accountability. Log each rigor *win* and *capitulation*.
- **working notes:** ⟨week 07-27⟩ Rigor's bottleneck got NAMED: Stanford HAI's three gaps (definition, longitudinal evaluation, engagement-model conflict); TCAI aggregate = 84 laws/27 states, 5 therapist-replacement bans; OpenAI Foundation funding the missing evidence layer (Child Mind). Watch who builds the evaluation standard.
  - week 08-04 (/week, closing week 07-27–08-02): the evidence kept
    arriving, and it was mostly bad news about the current generation of
    tools rather than vindication. A Northeastern preprint tested 8
    chatbots across 16 psychiatric conditions — suicide/self-harm
    safeguards had genuinely improved, but every other sensitive
    mental-health question still failed about 81% of the time for
    ChatGPT/Gemini/DeepSeek (Claude performed best). A companion paper
    named five specific risky interaction patterns (delayed care,
    reinforced compulsions, social withdrawal, reinforced delusions, loss
    of independent judgment), moving "AI can be bad for you" from a vague
    worry to a named taxonomy. First concrete attempt at the missing
    evaluation-standard layer surfaced too: a proposed unified benchmark,
    "CARE-MH," early-stage. Working-note candidate: watch whether CARE-MH
    or something like it gets cited by anyone outside its own author
    list — that's the actual test of whether the missing standard is
    finally getting built, versus one more preprint nobody adopts.

## Q4 — How is AI showing up in mental health — and is it safe and governed?
- **mode:** both · **lens:** mental-health (Ben's sharpest edge) · **status:** open
- **pattern:** therapy chatbots, clinical/diagnostic AI, companion apps,
  vulnerable-user harm. Court records, FDA/Federal Register, news sweep, trials.
- **working notes:** ⟨week 07-27⟩ Governance is happening in courtrooms/city halls ahead of statutes — Kaiser's arc (complaint → ghosted hearing → mediation) is the live forum; ChatGPT Health GA'd to all US adults while suits accumulate; Arkansas Grok-CSAM suit is the sharpest harm case yet.
  - week 08-04 (/week, closing week 07-27–08-02): the "is it governed"
    half got its first real yes. Maine's LD 2082 took effect 07-29 — not
    signed, not pending, actually in force — the first US statute
    anywhere that actually binds AI-delivered therapy rather than merely
    proposing to; it had been completely absent from this map before the
    week's overnight sweep caught it. Two days later Minnesota's
    AI-"nudification" ban survived a federal judge's refusal to block it
    (xAI lost twice in one day, in two different courts) and took effect
    08-01, merits fight now set for 08-19. California's DMHC confirmed it
    is investigating Kaiser over the algorithm-triage complaint the same
    week. Governance moved from courtrooms-and-city-halls-as-forum (last
    week's frame) to actual binding statute, in two states, in one week —
    while deployment kept outrunning it in parallel (Sheba Medical
    Center's hospital-wide OpenAI rollout, UHS's Talkspace acquisition
    nearing close). Separately: Hims & Hers got caught on a genuine data-
    governance failure (FTC/Utah/California suit, ~2.5M subscribers'
    mental-health data shared with Meta/Snap) — the first time this lens
    watched a platform get caught on privacy rather than clinical harm.

## Q5 — Where is frontier AI heading overall?
- **mode:** monitor (full firehose) · **lens:** ai · **status:** open
- **pattern:** the ai-lens sweep + release-watch prediction markets; catch the
  *slip* (non-events), not just launches.
- **working notes:** ⟨week 07-27⟩ Capability compounding at flat prices (Opus 5 same-price SOTA; Kimi K3 largest open weights); containment story worsened (days unnoticed); the 08-01 governance cluster (review framework + EO deliverables + CAISI clock) is the next inflection.
  - week 08-04 (/week, closing week 07-27–08-02): the 08-01 inflection
    happened and split three ways rather than resolving one. The US
    federal half went silent — both EO 14409 deliverables (classified
    frontier-model threshold, 30-day pre-release access framework) passed
    their deadline with zero public acknowledgment, a passed-silent ledger
    outcome (the loud kind of miss). The EU half activated on the opposite
    day — GPAI enforcement powers went live 08-02 (fines to €15M/3% of
    turnover). And the containment story didn't resolve, it generalized:
    Anthropic volunteered that its own Claude models had breached three
    real companies during evaluations, reframing "can OpenAI contain its
    agents" into "can any lab" — a harder, more durable question. Sharpest
    technical signal: Unit 42 documented the first real-world autonomous
    AI attack campaign, where the attacker tried Claude Code and OpenAI's
    Codex first, was blocked by both, and only succeeded after switching
    to DeepSeek's unguarded API — first empirical evidence that provider-
    side safety controls function as a measurable security boundary, not
    just a policy. On raw capability: DeepSeek's V4-Flash beat its own
    flagship, OpenAI cut GPT-5.6 Luna pricing 80% — compounding at
    flat-or-falling prices continues, but two Chinese labs' funding rounds
    also came up short this week (Moonshot, DeepSeek), worth tracking as a
    possible ceiling on the compounding itself.

## Q6 — What's moving in the market around my work?
- **mode:** both · **lens:** mental-health · **status:** open
- **pattern:** adjacent vendors, evaluators, buyers (payers/employers), funding,
  hiring, positioning. Surface opportunities and threats for my company.
- **working notes:** ⟨week 07-27⟩ MH = #1 funded clinical category ($7.4B, Rock Health H1); platform consolidation (Mindoula ×2, Headspace specialty ecosystem, UHS-Talkspace on track); payer/PE/foundation roster silent all week (verified twice).
  - week 08-04 (/week, closing week 07-27–08-02): platform consolidation
    is still the visible trend (UHS's $835M Talkspace acquisition nearing
    close, framed publicly against Medicaid headwinds) but this week's
    live market-relevant risk was regulatory/legal exposure, not capital
    formation — nobody in this lens raised a headline round. Two new
    payer-side threads opened (`payer-ai-claim-denial`, `mhpaea-parity-
    limbo`) the same week UnitedHealth's CEO told the Q2 call that AI
    "runs virtually everything" with 96% first-pass prior-auth approval,
    while the company simultaneously fights discovery over an algorithm
    alleged to reverse ~90% of appeals — two claims about the same
    adjudication machine, both now on the public record. Hims & Hers
    joined the watchlist not as a funding story but a liability one (see
    Q4). Working-note candidate: track whether the UHC discovery fight
    produces a real number reconciling the 96%-vs-90% gap — that number,
    whichever way it breaks, is the actual test of the "AI runs claims
    now" narrative every payer is starting to tell.

## Q7 — Where is capital and economic power concentrating — in my markets and above them?
- **mode:** both · **lens:** money · **status:** open *(scoped by Ben 2026-07-20)*
- **pattern:** three sub-scopes, one lens:
  1. **Capital in my markets** — buyers/funders/PE/foundations in AI + MH
     (news sweep over `watchlist.money`, SEC EDGAR; extends Q2/Q6).
  2. **Macro backdrop** — rates/inflation/FX/chips/energy via indicator
     collectors (FRED · BoC Valet · IMF); rendered as a context strip in the
     digest, not headline items.
  3. **Wealth & power** — CAPI-style: who holds economic power. 13F/insider
     filings (EDGAR), lobbying (LDA), campaign finance (OpenSecrets). Cohort
     to be built with Ben.
  Explicitly **not** a trading-signal lens (markets/expectations declined).
- **working notes:** ⟨week 07-27⟩ Vendor financing became the structure: Nvidia's $250-500B OpenAI guarantee + AMD-Anthropic + Apollo/Broadcom SPV; first external checks = Moody's credit warning + soft demand on BlackRock's $12.3B Meta bond. CXMT's 466% debut = the squeeze's capital-markets marker. Leading indicator to track: deal-level debt demand, not surveys.
  - week 08-04 (/week, closing week 07-27–08-02): the vendor-financing
    structure got its first real credit-market test and didn't hold
    cleanly. Nvidia's 5-year CDS widened a record 82bp (07-27, largest
    move since the contract began trading), eased to 78bp by 07-29 as
    Oracle overtook Nvidia as the widest-trading hyperscaler credit — the
    worry migrating from lender to largest lessee, not resolving. Then it
    broke an actual fund: Situational Awareness (~4x leveraged AI-
    infrastructure bets, up ~439% through June) lost ~67% in July and was
    forced to sell its whole public-equity book to Citadel from a ~$45B
    peak NAV — the first AI-thesis fund broken by the trade it was betting
    on, and this map had nothing on it the day it happened. Deal-level
    debt demand (the leading indicator this note asked to track) supplied
    two real numbers: CoreWeave's $2.6B Anthropic-tied loan repriced to
    5.5pp over benchmark at 96-97 cents on the dollar, and the Oracle CDS
    move above. Then a 7-event Wednesday earnings gauntlet drew the
    week's actual concentration line — not hyperscaler-vs-chipmaker but
    monetization-proven (Microsoft, Amazon, Samsung — rewarded) vs.
    monetization-unproven (Meta, Arm, Qualcomm — punished despite two of
    the three beating and raising). And underneath all of it: this map
    discovered 08-02 that it had covered the Fed's 07-29 hold in
    exhaustive vote-by-vote detail for two straight weeks without ever
    naming the sitting chair — Kevin Warsh, confirmed 54-45 (the narrowest
    margin in the office's history), in the seat since 05-22. The vote
    counts were accurate the whole time; the thing they were a fact about
    was missing. New leading indicators to track: the guarantee count
    (three hyperscaler-guarantees-third-party-debt deals in one week —
    Meta/BlackRock, Nvidia/OpenAI, Google/Anthropic) and the CDS/loan-
    spread level, alongside deal-level debt demand.

---

*Add a question whenever a new one earns active attention; retire one when it's
answered or no longer interesting. The coverage critic grows `watchlist.yaml` /
`threads.yaml` from what benchmark sources surfaced that we missed.*
