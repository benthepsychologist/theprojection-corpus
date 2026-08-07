# Q5 — Do AI-therapy claims survive replication? (research memo, 2026-08-07)

Extends `ebp-crawl-digital-ai-science.md` §2 (AI chatbots as/in therapy) and the book manuscript at
`/workspace/the-evidence-gap-src/outlines/chapter-1.md` Act 6 (the chatbot wave's evidence
history). This memo does not re-derive either — it chases what they left open: whether Therabot
has an independent replication in flight anywhere, how the NEJM AI critique-letter exchange
actually resolved, what happened to Woebot's and Wysa's trial portfolios after 2025, Slingshot
Ash's evidence-vs-marketing gap, uptake of the Hua/Torous three-tier framework, and whether the
field's 16%-clinically-tested ratio is moving.

Method: ClinicalTrials.gov API + Europe PMC REST API used directly (structured, not
summarized-by-a-small-model) for trial registries and citation graphs; WebFetch against
STAT News, PubMed, and vendor/company pages for narrative detail. `ai.nejm.org` (NEJM AI, the
venue hosting the actual critique letters) returned HTTP 403 on every attempt — bot-blocked, not
paywalled-with-preview like STAT — so the letters' exact resolution text could not be independently
verified beyond what the base crawl file already extracted; flagged below rather than guessed at.
6 WebSearch calls used before this session's WebSearch budget was exhausted entirely (a
container-wide cap, not a per-task one); all further research after that point ran via WebFetch
and two structured APIs (ClinicalTrials.gov, Europe PMC), which is why the second half of this
memo is unusually citation-dense — those interfaces don't summarize, they return the record.

---

## TL;DR

- **Therabot itself still has zero independent replication.** ClinicalTrials.gov lists exactly two
  Therabot-branded studies and both are Dartmouth's own: the original 210-person NEJM AI trial
  (NCT06013137) and a new single-arm feasibility spinoff, Therabot-CALM, for cannabis use plus
  anxiety/depression (NCT06920238, Dartmouth again, no control arm). No outside lab has registered
  a Therabot trial.
- **But three genuinely new, non-Dartmouth generative-AI-therapy RCTs with active or human
  comparators have appeared and completed since the base crawl — none has published results yet.**
  Most notably a 222-person three-arm Chinese trial (chatbot "Emohaa" vs. individual human
  counseling vs. waitlist, NCT06992180) — the field's first registered head-to-head-vs-human-
  therapist design for a generative AI chatbot — completed September 2025 with results still
  unpublished as of this research pass.
- **Woebot shut its consumer app down June 30, 2025, and the wind-down of its regulatory-track
  trials predates the public announcement by two to three years.** Its FDA-breakthrough-track
  postpartum-depression trial and an adolescent-depression RCT were both terminated by "internal
  company decision" in 2022–2024 — well before founder Alison Darcy told STAT the shutdown was
  driven by the cost of FDA marketing authorization. Company pivoted to enterprise/B2B only.
- **Wysa now has a company-co-authored null result on its own core clinical claim.** A 2026
  mixed-methods RCT at a London NHS trust (co-authored by Wysa's own chief scientist) concludes
  "there is no evidence that Wysa treats depression in this study" — badly underpowered (76
  randomized, 30 lost to follow-up) but a real negative data point from inside the company, not
  from a critic.
- **Slingshot Ash's evidence base is still one uncontrolled, non-peer-reviewed observational
  report** (Nov 2025, no control group, 48% of users showed minimal/no improvement) **and the
  company has since pulled the product out of the UK** (Jan 2026) over unresolved medical-device
  regulatory classification — a marketing-vs-evidence gap STAT itself characterized as a study
  that "lands with a thud."

---

## What changed 2021→2026

**The uptake-ratio question has a fresher, narrower answer than the base crawl's 16% figure, and
it complicates rather than resolves the story.** The base crawl cites Hua & Torous (*World
Psychiatry*, Oct 2025, PMID 40948070): 160 chatbot studies 2020–2024, only 16% clinically
efficacy-tested. That figure spans *all* chatbot types (rule-based, retrieval-based, generative).
The first meta-analysis to isolate *generative-AI-specific* chatbots — Zhang et al., *JMIR Mental
Health*, 2025 (doi 10.2196/78238), search completed March 2025 — found 26 studies in narrative
synthesis but only **14 met criteria for meta-analysis** (RCT, active-non-chatbot comparator,
sufficient statistics), covering N=6,314 total. Pooled effect: ES=0.30, **p=.047** — barely
clearing significance — with a 95% prediction interval of **−0.85 to 1.67**, meaning a genuinely
new study or setting could plausibly show no effect or a negative one. Two further chatbot-wide
meta-analyses landed in 2026: Gong et al. (*JMIR*, 29 RCTs through Feb 2026, CBT-oriented chatbots
only) found moderate depression reduction post-intervention (g=−0.55) that shrinks to small
(g=−0.32) at follow-up and goes **nonsignificant for anxiety at follow-up** (g=−0.19); Sohn et al.
(*npj Digital Medicine*, 39 RCTs through Oct 2025, all chatbot types) found smaller pooled effects
(g=0.31 depression, g=0.28 anxiety). Read together: the absolute count of RCT-grade evidence has
grown since the Hua/Torous baseline (14–39 qualifying RCTs across different inclusion criteria, vs.
an implied ~26 clinically-tested studies in the 160-study base), but not dramatically, and the
generative-AI-specific subset's own meta-analysis is watching a wide, zero-crossing prediction
interval — this is "barely holding," not "clearly improving."

**A vendor published a null result on itself for the first time.** The Central and North West
London NHS Foundation Trust ran a mixed-methods RCT of Wysa as a bridge intervention for patients
on the Talking Therapies waitlist (*International Journal of Social Psychiatry*, 2026,
doi 10.1177/00207640251415507), co-authored by Meinert, Milne-Ives, Taylor, **Inkster** (Wysa's
own chief scientist and the author of Wysa's 2018 foundational evidence paper the book cites),
Paik, Ananthakrishnan, Orr, Costelloe, Shankar. Of 2,161 screened, 625 invited, 99 consented, only
76 were randomized (2:1) and 30 were lost to follow-up. The paper's own conclusion: "there is no
evidence that Wysa treats depression in this study" — heavily hedged by the small sample, but a
real negative finding published with the company's own scientist's name on it, not extracted by a
critic. This sits alongside a second, structurally separate Wysa evidence stream: NICE's 2026
Early Value Assessment of "digital front door" pre-assessment tools for NHS Talking Therapies
(HTE10055) reviewed four products (Limbic Access, Wysa Digital Referral Assistant, Censeo Digital,
AskFirst) and found peer-reviewed evidence existed for only two — Limbic and Wysa — with Limbic's
evidence markedly stronger (referral-increase odds ratio 1.10, plus documented access gains for
Asian, Black, and non-binary users) than Wysa's. Two different Wysa products (a therapeutic
chatbot vs. a referral-triage assistant) are now sitting on two different, both middling-to-weak,
2026 evidence readouts — worth not conflating in the feed.

**Woebot's shutdown looks, on the trial registry, like the tail end of a multi-year wind-down
rather than a sudden 2025 event.** STAT (July 2, 2025) and multiple secondary outlets report the
consumer app retired June 30, 2025, for roughly 1.5 million historical users, with founder Alison
Darcy attributing it to "the cost and challenge of fulfilling the FDA's requirements for marketing
authorization" and the FDA not having "figured out how to regulate" LLM-based updates. But
ClinicalTrials.gov shows the company running 14 registered trials since 2020 — the deepest RCT
portfolio of any chatbot maker in this space — and several of the most clinically ambitious ones
were terminated years before the public announcement: the postpartum-depression-as-adjunct-to-TAU
trial (NCT05551195, terminated May 2023, "internal company decision"), a six-month WB001
follow-up (NCT05693792, withdrawn), the W-PPMA postpartum trial (NCT05662605, terminated 2024),
and an adolescent-depression-vs-educational-app RCT (NCT05486611, terminated 2022 for enrollment
difficulty). Several smaller studies did complete normally (the original WB001 pivotal test, the
Anchor substance-use study, a W-GenZD adolescent feasibility study). The pattern reads as the
FDA-breakthrough-device regulatory track stalling from roughly 2022 onward, with the 2025
announcement formalizing a decision effectively made years earlier. One independent commentary
(feltreal.org) frames the lesson bluntly: "The market did not reward Woebot for doing things
right. The market rewarded speed and engagement" — Woebot had the strongest evidence base in the
sector and still couldn't sustain the consumer product built on it.

**Slingshot Ash went from launch to its first evidence release to a regulatory retreat within
about six months, and none of the three steps involved peer review.** Ash launched July 2025
(a16z-backed, ~$93M raised, marketed as "the first AI designed for therapy"). Its first outcome
data, released November 2025, was a single-arm observational study (no control, no randomization,
~305 participants, 82% women) self-reporting improvement over 10 weeks — 76%/77% reporting
decreased depression/anxiety symptoms, but 48.2% classified as showing minimal or no improvement,
36.4% concurrently on psychiatric medication, and 23.9% concurrently in psychotherapy, none of
which the design controls for. STAT's own follow-up coverage was headlined "Therapy chatbot study
lands with a thud." Europe PMC shows zero peer-reviewed publications from this study as of this
research pass — it exists only as a company report/preprint. Two months later (Jan 23, 2026),
Slingshot withdrew Ash from the UK market entirely, citing the absence of "a clear regulatory
pathway for wellbeing products like ours" — Ash is marketed as a non-medical wellbeing product, and
the withdrawal reads as an attempt to avoid being reclassified as a medical device before that
question is forced. Separately, Slingshot has complained directly to the FDA that news coverage
has "skewed the public's perception of risk" for products like Ash — an unusual instance of a
vendor pushing back on regulatory/media scrutiny rather than commissioning better evidence.

**The Hua/Torous diagnosis has spread fast; the specific three-tier framework's citation-as-adopted
-standard has not, at least not yet by name.** The paper has 17 citing works within roughly a year
(Europe PMC, as of this crawl), spanning eating disorders, EHR-integrated LLMs, rehabilitation
science, and youth mental health. None of the abstracts reviewed explicitly say "we apply the
Hua-Torous bench/pilot/efficacy framework," but the diagnosis it makes — insufficient staged
evaluation before clinical deployment — is being independently re-derived: a Stanford group
(Lee, Handler, Mungle, Hernandez-Boussard, *JAMIA*, 2026) proposes its own parallel **3-stage
safety framework** for AI mental-health chatbot governance, without citing Hua/Torous by the search
terms used here. Torous himself continued publishing into 2026 with the same skeptical line: Bodner,
Lim, Schneider, Torous (*Current Opinion in Psychiatry*, 2026) reviewed Feb 2024–July 2025
literature and concluded "current evidence is insufficient to determine their efficacy or safety in
clinical practice" — most studies still lack active controls, adverse-event reporting is rare, and
emotional-dependence/parasocial risks are "largely unexamined." The most institutionally
significant development is a **Campbell Collaboration systematic-review protocol** (Soni, Singh,
Kumar, registered 2026) — the social-science equivalent of a Cochrane review — to formally assess
AI-based-psychotherapy effectiveness by country, AI architecture, underlying psychotherapeutic
model, human-therapist involvement, and diagnostic category. This is the first sign of
Cochrane/Campbell-tier synthesis infrastructure being built specifically around this question;
no completion date was stated in the abstract.

---

## Current state of the dispute

**Therabot's core empirical claim (effect sizes "approaching gold-standard therapy") remains
un-replicated and un-retracted — the dispute settled into a published argument, not new data.** The
base crawl already documents two formal critique letters (Heckman et al.; Gratch & Essig, both
2025) targeting the wait-list-only "nocebo" comparator, the non-independent evaluation (the team
that built Therabot also evaluated it), and the misapplied human-therapeutic-alliance measure, plus
a Dartmouth-authored response letter (AIp2500680). This research pass could not independently
verify what that response letter concedes or defends — `ai.nejm.org` returned HTTP 403 on every
fetch attempt across multiple entry points (direct DOI resolution, PMC, PubMed search), which reads
as active bot-blocking rather than a paywall preview, so the exchange's exact resolution content
is a genuine access gap, not a settled fact this memo can report on. What *is* independently
verifiable is that no active-comparator, independently-run Therabot trial has been registered
anywhere — meaning the critique's central methodological demand (test it again, properly) has not
yet been met empirically by anyone, Dartmouth included. The Therabot-CALM follow-up (NCT06920238)
is single-arm and feasibility-only, not a response to the control-group critique.

**The field is, for the first time, running the exact designs the Therabot critics demanded — just
not on Therabot.** Three non-Dartmouth trials registered and completed since the base crawl give
the dispute its first real empirical test cases, though none has published: Emohaa's three-arm
China trial (chatbot vs. human individual counseling vs. waitlist, N=222, Central University of
Finance and Economics, completed Sept 2025) is the field's first head-to-head-vs-human-therapist
generative-AI design; a University of Pennsylvania crossover RCT of the Elomia chatbot against an
active (not wait-list) comparator, Penn's own digital wellness modules (N=63, completed May 2025);
and an older Hong Kong AI-chatbot-vs-telephone-hotline comparison (observational, not RCT,
2021–2024). None of the three has posted ClinicalTrials.gov results or a peer-reviewed publication
as of this pass — the dispute's actual resolution is sitting, unpublished, in three different data
sets right now.

**Woebot's and Slingshot's trajectories are, structurally, the same story on a five-year lag.**
Woebot built the deepest evidence base in the sector and still could not sustain a consumer product
against the FDA-authorization cost of doing LLM updates properly — the strongest-evidence player
exited. Slingshot has built essentially no independent evidence (one uncontrolled company report,
zero peer review) and is now hitting the same regulatory wall from the opposite direction — trying
to stay classified as "wellbeing," not a medical device, specifically to avoid the evidentiary bar
Woebot couldn't clear. Wysa sits in between: real trial infrastructure, a company scientist willing
to publish a null result, but that null result is exactly what it looks like — no clean signal
either way from the vendor's own house.

---

## Key sources

| Source | Venue / date | Design | Finding |
|---|---|---|---|
| ClinicalTrials.gov NCT06013137, "Chatbot for Depression, Anxiety, and Eating Disorders" | Dartmouth-Hitchcock, completed Aug 2024 | **RCT, N=210, parallel, single-masked outcomes assessor** | The original Therabot trial underlying the NEJM AI paper; no results posted on the registry yet. |
| ClinicalTrials.gov NCT06920238, "Use of a Generative AI (Gen-AI) Chatbot for Anxiety and Depression Among Persons With Cannabis Use" | Trustees of Dartmouth College, completed April 2026 | Single-arm, N=15, device feasibility | Therabot-CALM spinoff; not a replication — no control arm, feasibility-only. |
| ClinicalTrials.gov NCT06992180, "Generative Artificial Intelligence Intervention and Individual Psychological Counseling on Emotional Distress in Young Adults" | Central University of Finance and Economics (China), completed Sept 2025 | **3-arm RCT, N=222, single-masked outcomes assessor** | Chatbot "Emohaa" vs. individual human counseling vs. waitlist — the field's first head-to-head-vs-human-therapist generative-AI design found; results unpublished. |
| ClinicalTrials.gov NCT06725147, "Elomia - Digital Mental Health and Well-Being" | University of Pennsylvania, completed May 2025 | **Crossover RCT, N=63, active comparator (not waitlist)** | Elomia chatbot vs. Penn Digital Wellness Resources; results unpublished. |
| Zhang, Zhang, Xiong, Sui, Tong, Lin, "Generative AI Mental Health Chatbots as Therapeutic Tools: Systematic Review and Meta-Analysis" | *JMIR Mental Health*, 2025, doi 10.2196/78238 | **Meta-analysis, 14 RCTs (of 26 studies reviewed), N=6,314** | First GenAI-specific meta-analysis. ES=0.30, p=.047 (barely significant), 95% PI −0.85 to 1.67 (crosses zero widely); concentrated in non-WEIRD countries, gaps for young children/older adults. |
| Gong, Yao, Xie, Huang, Kishimoto, Berenbaum, Mu, "Efficacy, User Engagement, and Acceptability of CBT-Oriented Psychological Chatbots" | *JMIR*, 2026, doi 10.2196/82677 | **Meta-analysis, 29 RCTs (search to Feb 2026)** | Moderate depression reduction post-intervention (g=−0.55) shrinking to small at follow-up (g=−0.32); anxiety small post-intervention (g=−0.26), nonsignificant at follow-up (g=−0.19). |
| Sohn, Ha, Park, Kim, Lee, Oh, Lee, Kim, "Systematic review and meta-analysis of chatbots in the management of depressive and anxiety symptoms" | *npj Digital Medicine*, 2026, doi 10.1038/s41746-026-02566-w | **Meta-analysis, 39 RCTs, N=7,401(dep)/7,621(anx)**, Jan 2017–Oct 2025 | g=0.31 depression, g=0.28 anxiety; larger effects in clinical/subclinical vs. nonclinical samples. |
| Meinert, Milne-Ives, Taylor, Inkster, Paik, Ananthakrishnan, Orr, Costelloe, Shankar, "Real-World Testing of an AI Conversational Agent... Mental Health Referral Care Pathway" | *International Journal of Social Psychiatry*, 2026, doi 10.1177/00207640251415507 | **Mixed-methods RCT, N=76 randomized (of 99 consented, 2:1), 30 lost to follow-up** | Wysa at Central and North West London NHS Foundation Trust; company-co-authored (Inkster is Wysa's chief scientist). Conclusion: "no evidence that Wysa treats depression in this study" — underpowered but a genuine null result. |
| Fleeman, Mahon, Bryning, Beale, Boland, Greenhalgh, Dundar, "Digital front door technologies to pre-assess people before assessment for NHS Talking Therapies [HTE10055]: early value assessment" | NICE, *Health Technology Assessment*, 2026, doi 10.3310/gjab1822 | **NICE Early Value Assessment / systematic review** | Evidence found for only 2 of 4 reviewed products (Limbic Access, Wysa Digital Referral Assistant); Limbic's evidence markedly stronger (referral OR=1.10, minority-access gains); Wysa's referral-triage evidence base comparatively thin. |
| STAT News, "Woebot Health shuts down pioneering therapy chatbot" | statnews.com, July 2, 2025 | Reporting | Consumer app retired June 30, 2025 (~1.5M lifetime users); founder Alison Darcy attributes shutdown to FDA marketing-authorization cost/uncertainty over LLM updates, not lack of evidence. |
| ClinicalTrials.gov, Woebot Health-sponsored trial registry (14 studies) | Various, 2020–2024 | **Registry review, not a single study** | Postpartum-depression pivotal-track and adolescent-depression RCTs both terminated by "internal company decision"/enrollment difficulty in 2022–2024 — the regulatory-track wind-down predates the public 2025 shutdown announcement by 2–3 years. |
| The Hemingway Report, "Reflections on Slingshot's Real World Study" | thehemingwayreport.beehiiv.com, Nov 2025 | Independent critique of company report | Single-arm, N=305, no control; 48.2% minimal/no improvement; 36.4% concurrently medicated, 23.9% concurrently in therapy, uncontrolled for; causality not established. |
| STAT News, "Slingshot pulls therapy chatbot Ash out of UK over regulatory concerns" | statnews.com, Jan 21, 2026 | Reporting | Ash withdrawn from UK Jan 23, 2026; CEO cites absence of "clear regulatory pathway for wellbeing products"; company simultaneously lobbying FDA that press coverage "skewed" public risk perception. |
| Hua, Siddals, Ma, Galatzer-Levy, Xia, Hau, Na, Flathers, Linardon, Ayubcha, Torous, "Charting the evolution of AI mental health chatbots from rule-based systems to LLMs: a systematic review" | *World Psychiatry*, Oct 2025, PMID 40948070 | **Systematic review, 160 studies, 2020–2024** | 16% of studies clinically efficacy-tested (77% still early validation); proposes 3-tier bench/pilot/efficacy evaluation framework. Base-crawl source, re-verified with exact framework tier names here. |
| Lee, Handler, Mungle, Hernandez-Boussard, "Building safer artificial intelligence mental health chatbots: a framework for transparency, evaluation, and shared accountability" | *JAMIA*, 2026, doi 10.1093/jamia/ocag078 | Governance framework paper | Stanford group proposes an independently-derived 3-stage safety/evaluation framework — same diagnosis as Hua/Torous, not an explicit citation-adoption of it (by the terms searched). |
| Bodner, Lim, Schneider, Torous, "Efficacy and risks of artificial intelligence chatbots for anxiety and depression: a narrative review of recent clinical studies" | *Current Opinion in Psychiatry*, 2026, doi 10.1097/yco.0000000000001048 | **Narrative review**, Feb 2024–July 2025 literature | Torous's continued 2026 position: "current evidence is insufficient to determine efficacy or safety in clinical practice"; most studies lack active controls; adverse-event reporting rare; dependence/parasocial risks unexamined. |
| Soni, Singh, Kumar, "Protocol: Effectiveness of Artificial Intelligence-Based Psychotherapy in Treating Mental Disorders" | *Campbell Systematic Reviews*, 2026, doi 10.1177/18911803261439274 | **Registered systematic-review protocol** | First Cochrane/Campbell-tier synthesis effort aimed specifically at this question; will stratify by country, AI architecture, therapeutic model, human-therapist involvement, diagnostic category. Completion timeline not stated. |
| Cuijpers, Harrer, Furukawa, "Innovations to improve outcomes and uptake of psychotherapies for mental disorders: a state-of-the-art review" | *World Psychiatry*, 2026, doi 10.1002/wps.70002 | State-of-the-art review | Classes chatbots as one "digital field" innovation among many; maturity "from dozens of supporting trials to few or none"; no single innovation will be a "paradigm-shifting silver bullet." |

---

## What the book already establishes

`the-evidence-gap-src/outlines/chapter-1.md` Act 6 (read-only; cited here, not re-researched) is
accurate as of its lock date on every fact this memo touched:

- **Scene 6.1** correctly anchors Woebot's founding (2017, Alison Darcy), its genre-defining
  Fitzpatrick et al. 2017 RCT (N=70), FDA breakthrough device designation (2021, postpartum
  depression), and Wysa's NHS IAPT-pathway partnerships and 2022 breakthrough designation.
  **This memo's addition:** the outline was locked before Woebot's June 30, 2025 shutdown and
  before Wysa's 2026 null-result RCT and NICE's 2026 mixed digital-front-door verdict — both are
  events after the outline's evidence horizon, not corrections to it.
- **Scene 6.2** correctly frames Slingshot's Aug 2024 seed/July 2025 Series A ($93M total) and the
  2025 Ash launch. **This memo's addition:** the outline stops at "launched the Ash consumer
  chatbot in 2025" — the Nov 2025 uncontrolled study, its critical reception, and the Jan 2026 UK
  withdrawal are all after the outline's evidence horizon.
- **Scene 6.4** correctly identifies the Hua/Torous 2025 review, its 16%/160-study figure, its
  three-tier bench/pilot/efficacy framework, and Torous's Nov 18, 2025 congressional testimony as
  the chapter's evidentiary anchor for "the evidence question reborn." **This memo's addition:**
  Torous continued the identical position into 2026 (Bodner/Lim/Schneider/Torous, *Curr Opin
  Psychiatry*), and a Campbell Collaboration protocol — the first Cochrane-tier synthesis effort on
  this exact question — was registered in 2026, both outside the outline's stated Nov 2025 horizon.
- **The book's source-tier note on Bakul Patel/FDA Pre-Cert and the WSJ paywall workarounds**
  (§"Source-tier notes for the writer") describes exactly the access problem this memo hit with
  `ai.nejm.org`: the NEJM AI critique-letter exchange central to the Therabot dispute is
  bot-blocked, not just paywalled, and the book's own critique-letter citations
  (`AIp2500390`/`AIp2500453`/`AIp2500680`) should carry the same "pull via subscription before
  verbatim quotation" flag the book already applies to WSJ's Cerebral pieces and Brian Anderson's
  Fierce Healthcare quote.

No genuine *contradiction* of the book's claims was found — everything above is post-outline-lock
extension, not correction.

---

## Feed implications

The feed already tracks `ai-therapy-evidence` and the base crawl's "Candidates for the feed"
section proposed this exact standing question as item #1 ("Does the Therabot/Dartmouth
generative-AI-therapy finding replicate in an independent trial with an active... control?"). This
memo's findings sharpen that question and add adjacent ones the base crawl didn't have data for.

**Term/entity refinements:**
- Add **Becky Inkster** (Wysa chief scientist) to the entities-worth-watching list — she is now the
  named co-author of a company publishing a null result on its own product, a distinct role from
  the "vendor evidence marketing" pattern the feed otherwise tracks.
- Add **Slingshot AI / Ash — UK withdrawal** as a distinct sub-thread under the existing
  "generative AI therapy: evidence vs. hype" thread candidate; it's now a live regulatory-status
  story (MHRA classification), not just an evidence-quality one.
- Note for the Woebot entity entry: status should read "consumer app shut down June 2025,
  enterprise-only pivot" rather than treating it as an active consumer product — several sources
  the feed might otherwise cite (FDA breakthrough designation, adolescent trial protocols) describe
  trials that were terminated, not just paused.

**Registrable dated expectations:**
- **Emohaa 3-arm RCT (NCT06992180) results** — study completed Sept 10, 2025; typical
  registry-to-publication lag for a psychology RCT runs 12–24 months, so results/publication would
  be expected by roughly **Q3–Q4 2027**. This is the field's first head-to-head-vs-human-therapist
  generative-AI trial to watch for a result either direction.
- **Elomia crossover RCT (NCT06725147) results** — completed May 30, 2025; same lag logic puts
  expected publication around **mid-to-late 2027**.
- **Campbell Collaboration AI-psychotherapy systematic review (Soni/Singh/Kumar)** — protocol
  registered 2026, no stated completion date; Campbell reviews typically run 1–3 years from
  protocol to full review, so **watch for the full review by 2028–2029** as the field's first
  Cochrane-tier verdict on this question.
- **Slingshot Ash UK regulatory resolution** — company stated it is in active discussion with the
  UK government "seeking a remedy" as of the Jan 2026 withdrawal; worth a near-term
  (**next 6–12 months**) check on whether Ash returns to the UK under a medical-device
  classification or stays withdrawn.

---

*Access gaps flagged rather than filled: (1) `ai.nejm.org` 403'd on every attempt (direct URL, DOI
resolution, PMC, PubMed cross-search) — the critique-letter exchange's exact resolution content
(AIp2500390/AIp2500453/AIp2500680) rests entirely on the base crawl file's prior extraction, not
independently re-verified here; (2) this session's WebSearch budget was exhausted mid-task (a
container-wide 200-call cap, not specific to this memo) — remaining research after that point ran
entirely on WebFetch plus the ClinicalTrials.gov and Europe PMC REST APIs, which is why source
density rises sharply in the second half of this memo; (3) neither the Emohaa nor Elomia trial has
posted ClinicalTrials.gov results or a preprint yet, so "does a non-Dartmouth active-comparator
trial replicate Therabot-style findings" remains genuinely unresolved, not just under-published.*
