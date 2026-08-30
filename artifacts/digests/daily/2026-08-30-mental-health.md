---
lens: mental-health
date: 2026-08-30
status: building
window_start: 2026-08-30T05:00:00-04:00
as_of: 2026-08-30T10:15:00-04:00
coverage: pending
---

# Mental Health — 2026-08-30

*Curated agentic-interim, 05:00 ET → 10:15 ET, a Sunday morning. **Nine
dispatches**: five cluster sweeps scoped to both the uncurated 08-29
evening window and today, three coverage critics finalizing 08-29, and a
cold-thread rotation. California's legislature sits today and tomorrow;
three bills this lens tracks are one vote from the end of their session.*

## Today's throughline

**California is one day from adjournment with three AI-in-care bills
still unvoted, and the Legislature's own record — checked directly this
morning, not through press coverage — shows none of them has moved.**
SB 903, which would bar marketing a chatbot as "therapy" and require
licensed-professional oversight, was **item 103 on the Assembly's floor
file for today** and its history still ends at "ordered to third reading"
on 08-21. SB 1119, the children's companion-chatbot safety bill, still
ends at "read third time and amended" on 08-28. Neither is a hit, a slip,
or a death: leginfo has been observed to lag same-day floor action by
hours, the Assembly sits today and tomorrow, and **08-31 is the
constitutional backstop — a bill not voted by then dies for the
session.**

**AB 2575 turned out to need a step nobody had recorded.** After failing
its first Senate floor vote 18-10 on 08-28 and being saved same-day by a
40-0 reconsideration, the bill was **amended** when it came back — which
under Senate rules sends it to **second reading again** rather than
straight to a repeat floor vote. It is on the Senate's second-reading
file today, "in floor process," and now needs both that reading and the
repeat vote inside 48 hours. **The margin got narrower without anything
visibly happening**, which is the kind of detail that only comes from
reading the record rather than the coverage.

**Two bills already made it out, and this map had the votes but not the
posture.** AB 1979 (Bonta) — consumer health chatbots brought under the
Confidentiality of Medical Information Act, no clinical decision on AI
output alone — cleared the Assembly's concurrence 66-10 on 08-27 and is
at Engrossing and Enrolling. SB 503 — clinical-decision-support AI
bias-tested every three years, with a published intended-use and
known-risk statement — concurred 39-0 on 08-25 and is also enrolling.
**Both are on the Governor's desk track with a 09-30 deadline**, and both
are already on this ledger.

**And the xAI companion-harm litigation escalated its legal theory
while this map was not looking.** A new federal suit in the Western
District of Arkansas alleges Grok was **trained on real child sexual
abuse material** — not merely prompted into generating new material,
which is what every prior suit on this thread has alleged. That is a
materially different claim about where the harm originates. Separately,
on 08-21, **xAI itself became a plaintiff** for the first time, suing an
Arkansas man over alleged misuse of Grok.

## Regulation & legislation

- **SB 903 and SB 1119 both remain exactly one Assembly floor vote from
  passage, with no vote posted as of ~10:00 ET on their own deadline
  weekend.** Checked directly against the Legislature's bill-history
  records (`202520260SB903`, `202520260SB1119`). SB 903 cleared Assembly
  Appropriations 13-0 on 08-13 and was ordered to third reading on 08-21;
  SB 1119 passed the Senate 39-0 in May, cleared Appropriations 11-1 on
  08-13, and was read a third time and amended on 08-28. **Neither is
  enacted, neither has failed** — they are pending on the last working
  weekend of the session, and SB 1119 needs Senate concurrence after
  Assembly passage on top of that.
  ([SB 903 history](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260SB903),
  [SB 1119 history](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260SB1119))
  <!-- k: t=state-therapy-chatbot-bans e= axis=regulation-and-legislation -->

- **AB 2575's second attempt needs a second reading first — a procedural
  step this map did not have.** Because the bill was amended when
  reconsideration was granted on 08-28, it returned to second reading
  rather than going straight back to a third-reading vote. As of this
  morning it sits on the Senate's 08-30 second-reading file, "in floor
  process," with no second floor-passage vote recorded. **Both steps have
  to happen before 08-31.** The bill would shift liability for AI-caused
  patient harm onto AI developers and is opposed by Kaiser and the
  California Hospital Association.
  ([AB 2575 history](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB2575))
  <!-- k: t=kaiser-ai-clinician-backlash,payer-ai-claim-denial e=kaiser-permanente axis=regulation-and-legislation -->

- 🕰 **The FDA opened the regulatory mechanism this lens's own evidence
  thread said was missing.** The agency released a discussion paper on
  regulatory approaches for generative-AI-enabled medical devices, with
  public comment open **through 2026-10-19**. `mh-evidence-infrastructure`
  logged a "facts label" proposal on 08-15 explicitly against the absence
  of a federal mechanism to carry it; this is that mechanism opening.
  Dated 08-18, caught by the cold rotation.
  <!-- k: t=mh-evidence-infrastructure,mh-evidence-watch e= axis=regulation-and-legislation -->

## Courts & accountability

- 🕰 **A new federal suit alleges Grok was TRAINED on real child sexual
  abuse material — a different allegation from every prior suit on this
  thread.** Filed in the Western District of Arkansas around 08-27/28 and
  corroborated across Ars Technica, Politico, Gizmodo, CyberScoop and
  others. Every earlier claim here has been that Grok *generated* abusive
  material on prompting; this one locates the harm in the training corpus
  itself. ⚠️ **Allegation, not finding** — no court has ruled.
  <!-- k: t=grok-companion-harm e=xai sev=major axis=courts-and-accountability -->
- 🕰 **xAI flipped to plaintiff on 08-21**, suing an Arkansas man over
  alleged misuse of Grok — the first offensive legal move by the company
  on a thread that has otherwise only recorded suits against it.
  <!-- k: t=grok-companion-harm e=xai axis=courts-and-accountability -->
- ⚠️ **The Minnesota preliminary-injunction ruling is still pending**, no
  ruling found through today since the 08-19 hearing. ⏸️ **One report
  held OFF the timeline for want of a source:** a Wyoming plaintiff
  alleging Grok generated roughly 7,000 explicit deepfakes of her from a
  childhood photo surfaced across several outlets 08-17→28, but the
  filing date and whether it is a new suit or an amendment could not be
  established — the article URLs 404'd and the docket check was not
  reachable within budget. Recorded as unconfirmed rather than written.
  <!-- k: t=grok-companion-harm e=xai axis=courts-and-accountability -->

## Big tech into health

- 🕰 **OpenAI shipped "ChatGPT for Teens" — a guardrail layer, not a
  health product, which answers this thread's open question in one
  direction.** Age-gated defaults, a homework-redirecting Study Mode and
  parental controls, roughly a year after teenagers were already using
  the product at scale. `openai-health` has been asking whether OpenAI
  would formalise a health posture that raises its standard of care;
  **this is the other answer** — safety bolted onto a general product.
  Dated 08-18, caught by the cold rotation.
  <!-- k: t=openai-health,bigtech-into-health e=openai axis=big-tech-into-health -->
- 🕰 **Apple's AI health coach has a concrete window again.** Gurman via
  9to5Mac puts the long-slipping "Mulberry" coach at a **September
  hardware event, or failing that iOS 27.1 in October** — replacing the
  open-ended timeline this thread has carried since July. **Still no
  mental-health-specific detail**, which is the part this lens actually
  needs. Dated 08-29.
  <!-- k: t=apple-health-arm,bigtech-into-health e=apple axis=big-tech-into-health -->

## Payers, providers & the money

- ✎ **A correction of grain, not of fact, on UHS–Talkspace.** The
  acquisition's SEC 8-K puts **aggregate cash consideration at $870.6M**
  against the $835M headline enterprise value already on
  `mh-clinical-infra-funding` — the gap being option and RSU cash-out
  treatment. The close date on the record (**2026-08-17**) is correct;
  what was late was this map's catching of it on 08-29, not the deal.
  Surfaced by the coverage critic and recorded here rather than on the
  timeline, since the thread already carries the deal in full.
  <!-- k: t=dtx-payment-paradox e= axis=payers-providers-money -->
- **Kaiser and NUHW: no weekend movement.** No new bargaining session,
  strike notice, or Rogers Behavioral Health response; NUHW's own newest
  post is 08-24, older than the American Prospect piece already on file.
  Recorded as a checked null, not an absence of checking.
  <!-- k: t=kaiser-ai-clinician-backlash e=kaiser-permanente axis=payers-providers-money -->

## ⏳ Upcoming & expected

- ⚠️ **`ca-sb903-floor-vote` — DUE TODAY, and not yet decided.** Not a
  hit, not a slip, not passed-silent: the Assembly sits today and
  tomorrow and the vote has not posted. **08-31 is the hard backstop** —
  if no vote is recorded by adjournment the bill dies for the session and
  this entry becomes passed-silent with a real outcome behind it.
- ⚠️ **`ca-sb1119-assembly-floor-vote` (08-31)** — pending; floor vote
  plus Senate concurrence both still to happen.
- ⚠️ **`ca-ab2575-senate-floor-vote` (08-31)** — pending, and now needs a
  second reading before the repeat vote (above).
- ✅ **`ca-ab1979-governor-action` and `ca-sb503-governor-action` (both
  09-30)** — both bills confirmed **through the Legislature and at
  Engrossing and Enrolling**. The expectations stand as logged; what is
  new is that the legislative half is definitively finished.
- ⚠️ **`meta-warner-csam-response` — stands passed-silent**, re-confirmed
  today against Warner's Senate press page and Meta's newsroom directly.
  Fifth check. No senator has joined, no FTC or state-AG action, no
  outlet has covered the silence.
- 📋 **Next 7 days:** SB 903 · AB 2575 · SB 1119 all by 08-31
  adjournment · France's social-media ban 09-01 (⚠️ its verification
  mechanism is now itself in doubt — see the world-news digest) · Sword
  Health's acquisition of Headspace closes 09-14 · Anthropic's
  wellbeing-grant applications close 09-21 · FDA gen-AI device comments
  close 10-19.

## 🔄 Map changes

- ✅ **08-29 finalized** with a critic appendix and `coverage: done`.
  **The critic found no misses, and this is the strongest of the three
  null results** — every "clean" verdict is backed by an outlet's own
  feed timestamp rather than an absent response, and the academic layer
  was swept six sources deep (JMIR, npj Digital Medicine, JAMA, Lancet
  Psychiatry, medRxiv, Psychiatric Services attempted) rather than the
  two the 08-28 pass missed on.
- ⛔ **One blind panel named:** **Psychiatric Services**
  (`ps.psychiatryonline.org`) is hard-blocked by a Cloudflare challenge
  that survives a Googlebot UA, **and is not tracked in
  `sources/benchmarks.yaml` at all.** Until that is solved the academic
  sweep has one panel it cannot see every pass — so today's clean
  JMIR/npj result should not be read as the academic layer being covered.
- ✎ **Precision note on the 08-29 digest, recorded rather than
  corrected:** npj Digital Medicine *did* publish two papers dated 08-29
  (a breast-ultrasound classifier and a haematology cytomorphology
  framework). Both oncology; neither mental-health-relevant. The digest's
  "nothing dated in window" was imprecise and substantively right.
- ✎ **Four timeline blocks in this lens today** —
  `state-therapy-chatbot-bans`, `kaiser-ai-clinician-backlash`,
  `grok-companion-harm` (two), plus cold-rotation catches on
  `openai-health`, `apple-health-arm` and `mh-evidence-infrastructure`.
- 🕰 **Quiet in this lens on the cold rotation**: `neuromodulation-evidence`,
  `psychedelic-regulatory-sprint`, `ai-psychosis`, `google-health`,
  `mh-evidence-infrastructure` (moved), `grok-companion-harm` (moved).
  On `psychedelic-regulatory-sprint` the rotation found only
  stock-sentiment coverage recycling a February Phase 3 readout — an
  ambient match, correctly not written.

## 🧵 Thread candidates

See the front digest for the full set. **Algorithmic clinical triage as
its own harm mechanism** reached its second and final offer on 08-29 and
drew no answer; per the rule it **leaves the pool today**, and is noted
here because Kaiser and Rogers Behavioral Health both remain live on
`kaiser-ai-clinician-backlash` without a home for the cross-provider
pattern.

---
California's legislature is one day from adjournment with three
AI-in-care bills unvoted, and its own record — read directly this
morning — shows SB 903 sitting at item 103 on today's floor file with no
result posted, SB 1119 in the same holding pattern, and AB 2575 needing a
second reading before it can even retry the vote it lost on Wednesday.
Two other bills, AB 1979 and SB 503, are already enrolled and on the
Governor's track. A new federal suit says Grok was trained on real child
sexual abuse material rather than merely prompted into making it, and xAI
sued somebody itself for the first time. Meta's silence toward Senator
Warner survived a fifth check.
