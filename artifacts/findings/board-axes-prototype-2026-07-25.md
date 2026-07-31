---
finding: board-axes-prototype
date: 2026-07-25
actors: [microsoft, nvidia, openai, blackrock, spacex, alibaba-qwen]
method: value-added gravity normalization (research 2026-07-25)
bundles: artifacts/bundles/{microsoft,nvidia,openai,blackrock,spacex,alibaba-qwen}-axes/
---

# The axis prototype — 6 actors, three axes, cited

The first pass at differentiating board actors by **capitalization** ($ commanded),
**optionality** (how free that capital is), and **gravity** ($ economy in orbit,
normalized to value-added). Six actors chosen to stress each axis. Every number
carries sources in the per-actor `*-axes/provenance.yaml` bundle; this is the
readable derivation and the cross-actor read.

## The gravity method — DEFLATION DEFERRED (Ben, 2026-07-25)

The crawls computed a value-added-dependent figure via:

> gross "ecosystem" figure × ~0.5 (value-added share) × dependency share (multi-homing haircut)

**But we are NOT applying that deflation yet.** The deflators (VA-share, dependency
haircut) are judged too weak and fragile, and right now we only compare companies
to companies — so **gravity below is stored as the GROSS figure**, with the deferred
VA-dependent number kept as a parenthetical for later. **Deflate when we compare to
nation-states** (a state's gravity = its GDP, already value-added, so a company's
gross must be deflated to compare honestly — raw $4T-Microsoft-vs-$3T-France flatters
the company ~2×). Caveat of not deflating: the gross figures are on **different bases**
(Alibaba GMV vs Microsoft partner-revenue vs OpenAI anchored-capex) so they are **not
yet apples-to-apples across actors**. The method is preserved, not discarded — see
`board.yaml` `axes.gravity`, `coverage-log.md` 2026-07-25, and the per-actor bundles.

## The cross-actor read (this is the payoff)

Gravity column is **gross** (deflation deferred); the VA-dependent figure is in
parentheses for when we normalize against nation-states.

| actor | commanded capital | optionality | gravity (GROSS; VA-dep deferred) |
| --- | --- | --- | --- |
| **BlackRock** | **~$15.3T** AUM (owns ~$170B) | **constrained** (fiduciary) | Aladdin ~$1.5B/yr (≪ capital) |
| **Microsoft** | ~$250B+ commandable | mixed (self-earmarking) | **~$3.0T** gross ($4T economy) *(~$0.9T VA)* |
| **Nvidia** | ~$200–300B commandable | **free** | ~$1.0T/yr gross *(~$375B VA)* |
| **OpenAI** | ~$180B raised | **locked** (earmarked+burning) | ~$1.0–1.4T stock *(~$57B/yr VA)* |
| **SpaceXAI** | ~$16B cash + $75B raise access | **free** (Musk ~82% vote) | ~$85B/yr gross *(~$30B VA)* |
| **Alibaba** | ~$44B liquid (falling) | constrained (China state) | ~$1.05T GMV *(~$43B VA)* |

Three findings fall straight out of the axes:

- **The axes genuinely separate actors a rank ladder would flatten.** BlackRock and
  Nvidia are near-inverses: BlackRock commands ~$15.3T but its gravity is
  negligible (~$1–2B/yr) — a **pure capitalization actor**; Nvidia commands ~1/200th
  of that but its gravity (~$375B/yr) **dwarfs its own capitalization ~4–5×** — it
  holds the mines everyone rents. One rung could never say that.
- **Optionality is the load-bearing axis.** OpenAI (~$180B, **locked** — ~85–90%
  pre-earmarked and burning) and SpaceXAI (**free** — Musk's ~82% voting control)
  are the poles. Capitalization alone would rank OpenAI far above SpaceXAI's
  ~$16B cash; optionality flips the story.
- **Gravity, normalized, behaves.** Microsoft's "$4T economy" deflates to **~$0.9T/yr**
  value-added-dependent; Alibaba's "$1T GMV" to **~$43B** (GMV is ~6% value-added,
  not 50%). Both land where an honest cross-actor comparison wants them.

## Per-actor notes

- **Microsoft** — the gravity proof: TTM revenue $318B × the IDC partner multiplier
  (~$9.39 blended, Microsoft-commissioned) reconstructs the ~$3.0T gross "economy",
  which deflates to ~$0.9T/yr. Optionality *mixed*: legally free treasury, but a
  rising majority self-earmarked to ~$107B/yr capex.
- **Nvidia** — the solid one. Capitalization is primary-sourced to the dollar
  (Q1 FY27 10-Q, two-source cross-check). Gravity's dependency share (CUDA lock vs
  substitution) is the only real swing (~$260–450B).
- **OpenAI** — the canonical cash-rich, freedom-poor actor. ~$1.0–1.4T of compute
  obligations against ~$180B raised. All figures private/leaked (Wikipedia's
  synthesis of Reuters/Bloomberg/The Information); no OpenAI-specific ecosystem
  study exists, so gravity is the weakest estimate.
- **BlackRock** — the commands-vs-owns case (~90×) and the model's proof that
  gravity ≠ capitalization. **Under-threaded** — a candidate for a dedicated thread.
- **SpaceXAI** — capitalization stated as market cap ~$1.52T (corrects our $1.56T
  anchor), but its *commanded-liquid* basis (~$16B cash + $75B raise access) differs
  from the operating-co peers — flagged as an open question below.
- **Alibaba** — the gross-vs-value-added trap in one actor. Also **under-threaded**
  for a $269B hyperscaler pouring its (shrinking) cash pile into a domestic compute
  stack under state influence.

## Open questions (for Ben)

1. **Capitalization basis is not uniform.** Operating cos (commandable liquid + debt),
   an asset manager (commanded AUM), a private lab (cumulative raised), a newly-public
   co (market cap) don't share one clean number. We need one definition, with the
   others as labeled side-figures. My lean: **capitalization = commanded/commandable
   deployable $**, market-cap/valuation always a separate label.
2. **Under-threaded actors** — BlackRock and Alibaba both warrant a dedicated
   "power-position" thread (tests the "each axis-actor is a thread" idea directly).
3. **Deflator sensitivity** — VA-share (~0.5) and dependency shares are analytical
   judgment, not cited. They move Microsoft's gravity $0.6–1.3T and Alibaba's $30–65B.
   Worth pinning house defaults so re-estimates stay comparable.

*Sources: the six `artifacts/bundles/*-axes/provenance.yaml` appendices. WebSearch
was exhausted this session (200/200); all crawls ran on WebFetch against primary
sources (SEC/IR/press) + reputable trackers, with vendor-commissioned and
reconstructed figures flagged as upper bounds.*
