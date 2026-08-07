# Q3 — Are the somatic bets outrunning their evidence fixes? (research memo, 2026-08-07)

Scope: three fast-moving "somatic" mental-health treatment bets — psychedelics
(psilocybin/MDMA), ketamine/esketamine, and GLP-1 drugs' psychiatric
side-effects — plus neuromodulation (SAINT/SNT) as a comparison case where the
evidence arguably *did* catch up. Builds on
`/tmp/claude-1000/-workspace-theprojection-corpus/036c1dc4-d8ab-4c00-953b-f57adf9e61cd/scratchpad/ebp-crawl-therapy-science.md`
section 6 (part of the 2026-08-07 EBP crawl); this memo verifies and deepens
that section against primary sources — trial registrations
(ClinicalTrials.gov), the FDA's own guidance document, published registry
papers, and state program data — rather than press releases.

Method: WebFetch against ClinicalTrials.gov's API, PubMed/PMC, FDA-adjacent
regulatory-press coverage (RAPS, FDAMap, Psychedelic Alpha), and Oregon Health
Authority pages; 4 WebSearch calls (query budget ran out mid-task — see
Limits below).

---

## TL;DR

- **Compass Pathways' two pivotal Phase 3 psilocybin trials were both fully
  enrolled before the FDA had published even a *draft* version of the
  blinding-design guidance they're now supposed to satisfy.** COMP005 started
  dosing January 19, 2023; COMP006 started February 14, 2023; the FDA's first
  draft psychedelic-trial guidance wasn't published until June 2023, and the
  final version — the one requiring active-placebo/expectancy-questionnaire
  designs — didn't land until July 2026, months *after* both trials had
  already collected their primary-endpoint data (COMP005: May 2025; COMP006:
  February 2026). The trials could not have built in a fix that didn't exist
  yet.
- **Only one of the two trials even partially matches the FDA's preferred
  fix, and neither trial registered a formal blinding-integrity measure.**
  COMP006 uses a sub-perceptual 1mg psilocybin dose as an "active
  comparator" — one of the two options the FDA's final guidance now
  recommends. COMP005 uses a plain "matched placebo" (the design category
  the FDA faulted in MDMA's rejection), and Compass's own chief medical
  officer, Guy Goodwin, told Psychedelic Alpha the placebo-controlled
  COMP005 exists more to characterize safety than to prove efficacy — "the
  less we peek, the better." Neither trial's ClinicalTrials.gov registration
  lists a blinding-assessment/expectancy-questionnaire outcome measure.
- **Transcend Therapeutics holds an accelerated-review voucher for a drug
  whose pivotal trial doesn't have primary data yet.** EMPOWER-1, its Phase 3
  trial of TSND-201 (methylone) for PTSD, only started enrolling in April
  2026 — the same month the National Priority Vouchers were issued — with
  primary completion not expected until December 2027. The regulatory fast
  lane opened before the trial that's supposed to justify it produced a
  single result.
- **Esketamine's "18% real-world remission" framing doesn't hold up as a
  single number, and the source cited for "France's ELLIPSE registry" in the
  underlying crawl is misattributed** — the real ELLIPSE study (n=211, 31
  French sites) hasn't published full outcome numbers yet; the actual
  published French registry with numbers is a *different* study, ESKALE
  (n=157). ESKALE's remission rate climbs from 19.7% at month 1 to 43.8% at
  month 3 — near trial-comparable — before high discontinuation (79.6%
  stopped before scheduled end) erodes the picture again. The gap is real,
  but it's a trajectory, not a flat 18%.
- **Neuromodulation is the one somatic bet where a real confirmatory trial
  has landed.** SAINT/SNT went from a single 30-patient trial (2022) that
  underpinned FDA 510(k) clearance and nationwide commercial rollout, to a
  proper sham-controlled RCT (Kratter et al., *World Psychiatry*, 2026, n=48)
  replicating the effect — 50.0% remission active vs. 20.8% sham (p=0.035) —
  four years later. The effect size is far more modest than the "80–90%"
  figure that circulated off the original small trial, but it replicated.

---

## What changed 2021→2026

**Psychedelics.** In 2021, MDMA-assisted therapy for PTSD looked like the
psychedelic field's best approval bet — MAPS/Lykos had two positive Phase 3
trials and a "breakthrough therapy" designation. That collapsed in August
2024: FDA's Complete Response Letter cited functional unblinding (patients
and raters could tell who got MDMA) and cardiovascular safety, backed by a
lopsided advisory-committee vote (2–9 on efficacy). The FDA didn't stop at
rejecting Lykos — it spent the next two years writing trial-design rules for
the whole psychedelic class, drafted June 2023 and finalized July 2026:
active-placebo alternatives (sub-perceptual doses or other psychoactive
comparators), expectancy-evaluation questionnaires pre- and post-treatment,
blinded central raters, and paired dose-response designs. Meanwhile the
political environment moved the opposite direction: an April 2026 executive
order and FDA National Priority Vouchers compressed review timelines from
10–12 months to 1–2 for Compass Pathways (psilocybin/treatment-resistant
depression), Usona Institute (psilocybin/major depressive disorder), and
Transcend Therapeutics (methylone/PTSD). Compass now has two positive Phase
3 readouts (COMP005 June 2025, COMP006 February 2026) and is targeting an
NDA filing in Q4 2026 — but as detailed above, both trials' designs were
locked in before the guidance meant to fix MDMA's failure mode existed.

**Ketamine/esketamine.** Spravato (esketamine) has been FDA-approved since
2019 on trial remission rates in the 30–50% range. The 2021–2026 arc is the
usual trial-to-real-world story: registries in France, Spain, Italy, and
elsewhere have been filling in behind the pivotal trials, generally showing
lower early response than trials promised, converging somewhat by month 3,
and then eroding again as real-world patients — sicker, more
treatment-lines-deep, less monitored — drop out of maintenance treatment at
much higher rates than trial populations did.

**GLP-1s.** This strand didn't really exist as a mental-health story before
2023; it emerged entirely from the semaglutide/tirzepatide obesity boom.
Observational cohorts (some showing ~98% relative increases in psychiatric-
disorder risk) collided with pooled RCT safety data showing no increased risk
and a small wellbeing benefit — a textbook confounding-by-indication problem
that, as of this research, still has no purpose-built trial resolving it.

**Neuromodulation.** SAINT/SNT is the outlier case: FDA 510(k) clearance
(K220177, ~2022) and commercial rollout preceded a confirmatory trial by
about four years, but the confirmatory trial has now actually happened
(2026) and replicated the direction of effect, if not the original's touted
magnitude.

---

## Current state of the dispute

The live question the underlying crawl posed — "is psilocybin's approval
outrunning the methodology fix FDA itself just wrote?" — has a sharper,
more falsifiable answer after checking the trial registrations directly:
**yes, by simple chronology, for the specific fix (expectancy questionnaires,
formal blinding-integrity endpoints) the FDA's final guidance calls for.**
The pivotal trials were designed and dosed years before that guidance
existed in final form, so they could not contain it. What's genuinely
contested is whether that matters: Compass's own CMO frames COMP005 as a
safety study more than an efficacy study, which — if taken at face value —
is itself a tacit concession that the placebo-controlled arm's efficacy
signal is compromised by the exact problem that sank MDMA. COMP006's use of
a low, sub-perceptual psilocybin dose as an "active comparator" is closer to
what FDA now recommends, but it's worth noting Compass adopted that design
for cost/trial-logistics reasons that predate the guidance, not because it
was chasing the guidance.

Usona's evidence base is the more interesting sub-question the deep-dive
turned up: Usona's own confirmatory trial (NCT03866174, n=347, psilocybin vs.
**niacin active placebo**, enrolling since January 2020) is a genuinely
stronger blinding-control design than Compass's flagship COMP005 — Usona
built in the "active placebo" fix half a decade before it became an FDA
recommendation. But Usona has no Phase 3 program visible on
ClinicalTrials.gov at all; its accelerated-review voucher currently appears
to rest on that Phase 2 result, not on any registered confirmatory Phase 3.
That's a real open question for the feed to track: is Usona's NDA going to
lean on a single Phase 2, and will FDA accept that under voucher pressure?

Transcend Therapeutics is the cleanest example of the "voucher before data"
pattern: EMPOWER-1 (its actual Phase 3) began enrolling the same month its
voucher was granted and won't have primary data until the end of 2027 —
over a year after Compass's targeted approval window.

The GLP-1 dispute remains genuinely unresolved and, per this research,
**structurally** unresolved: no registered trial anywhere uses a psychiatric
scale (MADRS, HAM-D, PHQ-9, GAD-7) as a primary endpoint for a GLP-1 drug.
Mass adoption (tens of millions of prescriptions) is running years ahead of
any trial capable of settling the confounding-by-indication question.

Esketamine and neuromodulation both show the more encouraging pattern:
evidence *is* catching up to deployment, just slower than the marketing.
ESKALE's month-3 remission (43.8%) isn't far off trial territory; SNT's
confirmatory RCT replicated a real, if smaller, effect. Ketamine and TMS
have simply had more years in the field to let that catch-up happen than
psilocybin has.

---

## Key sources

| Source | Type | Key finding |
|---|---|---|
| ClinicalTrials.gov NCT05624268 (COMP005) | Primary registration | Single 25mg dose vs. "matched placebo" (not active); enrollment started 2023-01-19; no registered blinding-integrity outcome |
| ClinicalTrials.gov NCT05711940 (COMP006) | Primary registration | 25mg vs. 10mg vs. 1mg (active comparator); enrollment started 2023-02-14; no registered blinding-integrity outcome |
| ClinicalTrials.gov NCT03866174 (Usona pivotal) | Primary registration | n=347, psilocybin vs. niacin active placebo; enrolling since 2020-01-23; results posted 2026-04-22 |
| ClinicalTrials.gov NCT07456696 (Transcend EMPOWER-1) | Primary registration | Phase 3, n=300, methylone/PTSD; started 2026-04-02, primary completion not until 2027-12 |
| Psychedelic Alpha, "Compass Pathways' Psilocybin Clears First Phase 3 Hurdle" (2025) | Trade press w/ direct quotes | CMO Guy Goodwin: COMP005's placebo design raises functional-unblinding concerns; trial's "real purpose is the safety side" |
| RAPS, "Psychedelics: FDA offers clarifications, compromises in final clinical trial guidance" (Jul 2026) | Regulatory trade press | Final guidance: active-placebo alternatives, dose-response characterization, driving-safety studies |
| FDAMap, "Designing the Un-blindable Study" (Jul 2026) | Regulatory trade press | Final guidance detail: low-dose active controls, blinded central raters, expectancy questionnaires, two-monitor session staffing |
| Yu et al., "Inaugural year of regulated psilocybin services in Oregon," *Frontiers in Psychiatry*, 2026 (PMID 42233004) | **Peer-reviewed, real-world program data** | n=5,935 clients / 5,375 sessions in 2025; adverse event rates 2.42 (behavioral) and 2.79 (medical) per 1,000 sessions; 84–91% white, 32.6% out-of-state; no clinical outcome scales collected |
| ESKALE registry, France, 26 hospital sites (PMC11919239) | **Peer-reviewed real-world registry** | n=157 (112 completers); remission 19.7% (month 1) → 43.8% (month 3) → 35.9% (at discontinuation); 79.6% discontinued before scheduled end |
| ELLIPSE registry, France, 31 sites (PMC12437346) | Registered protocol / conference abstract | n=211; full 12-month efficacy results not yet published as of this research — often cited (including in the source crawl) as if results were in, which overstates what's public |
| Barcelona TRD case series (PMC12437101) | Small real-world case series | n=32; 21.9% complete remission — this is the paper the source crawl mislabeled as "ELLIPSE" |
| ClinicalTrials.gov query, GLP-1 + psychiatric primary outcome | Registry search (negative result) | No registered trial uses a depression/anxiety scale as a PRIMARY outcome for any GLP-1 drug, as of Aug 2026 |
| Kratter et al., "Stanford neuromodulation therapy for treatment-resistant depression: a randomized controlled trial confirming efficacy, and an EEG study," *World Psychiatry*, 2026 (PMID 41536095) | **Peer-reviewed sham-controlled confirmatory RCT** | n=48 (24 active/24 sham); remission 50.0% vs. 20.8% (p=0.035); response 54.2% vs. 25.0% (p=0.039); L-ACC beta power as predictive EEG biomarker |
| Cole et al., "Stanford Neuromodulation Therapy (SNT)," *American Journal of Psychiatry*, 2022 | Original small RCT (n=30) | The trial underlying FDA 510(k) clearance (K220177) and commercial SAINT rollout; source of the widely-repeated "80–90%" figure |
| Psychedelic Alpha, "Compass Closes Out Phase 3 With 6-Month COMP006 Data, Eyes H1'27 Launch" (Jul 2026, paywalled beyond headline) | Trade press | Compass's own current framing is "H1'27 launch" — later/softer than Commissioner Makary's publicly floated "approval by late 2026" |

No formal umbrella meta-analysis exists yet across the psychedelic pivotal
trials (too new/unpublished in full); the esketamine and neuromodulation
rows above are individual registries/RCTs, not meta-analyses — flagged
because the underlying crawl's section 6 already cited the one real
meta-analysis in this space (2025 esketamine add-on-effect meta-analysis)
and this memo didn't find a reason to revise that citation.

---

## Feed implications

The feed already tracks this territory via `psychedelic-regulatory-sprint`
(thread, opened 2026-08-07, parent `mh-evidence-watch`) and the
`compass-psilocybin-nda` ledger entry (`upcoming.yaml`, due 2026-12-31). This
research supports refining both rather than opening new duplicate threads:

1. **Sharpen `psychedelic-regulatory-sprint`'s `watch` text with the
   chronology finding.** The current text says approval "may be outrunning
   the methodology fix" as an open question; this research resolves the
   narrow chronology question with dates (both pivotal trials fully enrolled
   before even the June 2023 draft guidance existed) — worth folding in as a
   dated fact, not just a live tension, next time the thread's notes get
   touched.
2. **Add a ledger check tied to Transcend's EMPOWER-1 primary-completion
   date (Dec 2027)** — a concrete, falsifiable marker for whether a
   voucher-holder's data catches up to its regulatory fast-track, parallel
   to the existing Compass NDA entry. Worth its own `upcoming.yaml` line
   rather than folding into `compass-psilocybin-nda`, since it's a different
   company/molecule/indication on a materially later data timeline.
3. **Usona's status is an open question worth a `watch` note, not yet a
   ledger claim** — no confirmed source for what trial(s) will support its
   NDA under the voucher; flagging it as unresolved is more honest than
   asserting a date.
4. **Correct the ELLIPSE/ESKALE mixup if section 6 of the source crawl gets
   promoted into any watchlist/entities note** — the crawl's citation for
   "France's ELLIPSE" (PMC12437101) is actually a small Barcelona case
   series; ESKALE (PMC11919239) is the actual published French registry
   with numbers, and the real ELLIPSE study's full results aren't public
   yet. Not urgent (this memo is the citable fix), but worth not
   re-propagating.
5. **Consider whether esketamine/ketamine and GLP-1 warrant their own child
   threads under `mh-evidence-watch`**, parallel to
   `psychedelic-regulatory-sprint` — right now neither has a dedicated
   thread despite both being live, contested strands with fresh 2026 data
   points (ESKALE's trajectory, the continued absence of a GLP-1 psychiatric
   RCT). Watchlist already has `COMPASS Pathways` and `Usona Institute` as
   entities; `Transcend Therapeutics` is not yet in `watchlist.yaml` and
   probably should be, given it now holds a voucher and has a dated Phase 3
   completion to watch.
6. **Neuromodulation (SAINT/SNT) is a genuine "of interest" counter-thread**
   — the one somatic bet in this set where a real confirmatory RCT landed
   in 2026, four years after commercial deployment began. Worth a light
   thread of its own or a line inside `mh-evidence-watch`'s notes as the
   comparison case for "evidence eventually catches up" against the
   psychedelic sprint's "evidence hasn't caught up yet."

---

## Limits

WebSearch ran out mid-task (a session-wide budget, not specific to this
memo — 4 calls were used here before it reported exhausted). Everything
after that point is WebFetch-only, which mostly worked but meant a few
targets (Oregon's raw quarterly PDF, Usona's own newsroom, cdphe.colorado.gov)
returned 403/404/placeholder pages rather than data; Colorado's Natural
Medicine program specifically could not be checked — its service data (if
any exists yet) is not confirmed either way in this research. The Compass
"H1'27 launch" framing and the September 2026 FDA hearing are both only
confirmed at headline level (full Psychedelic Alpha coverage is
paywalled) — worth a follow-up pass once/if that hearing occurs.
