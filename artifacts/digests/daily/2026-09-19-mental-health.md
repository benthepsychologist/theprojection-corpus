---
lens: mental-health
date: 2026-09-19
status: building
window_start: 2026-09-19T05:00:00-04:00
as_of: 2026-09-19T15:40:00-04:00
coverage: pending
---

# Mental Health — 2026-09-19

*Curated from 05:00 ET → ~15:30 ET Saturday (agentic-interim). The morning
pass covered 05:00-10:30 ET; this afternoon extension covers ~10:15 ET
through now, re-checking California's own bill-status pages directly, a
name-pass sweep of `/tmp/collect-0919pm/morning-google_news_rss.jsonl`
(11,227 rows, landed this morning, never read by the morning pass),
`buffer/2026-09-19-clinicaltrials.jsonl` (219 rows), and the now-current
`buffer/2026-09-19-rss.jsonl` (134 rows, extended past the morning's 128),
`-federal_register.jsonl` (47 rows), `-sec_edgar.jsonl` (424 rows) and
`-semantic_scholar.jsonl`/`-github.jsonl`. The afternoon
`google_news_rss`/`gdelt`/`sec_edgar`/`federal_register`/`clinicaltrials`
recollection (`--since 2026-09-19T14:00Z`) had not landed new rows as of
this pass's cutoff — `buffer/2026-09-19-google_news_rss.jsonl` still
matched the morning snapshot's exact row count (11,227) at last check.*

## Today's throughline

Disney named Karandeep Anand, until this week chief executive of Character.AI, as its first chief technology officer starting October 2, a year after Disney threatened to sue Character.AI over its use of Disney characters. The move leaves the chatbot company at the centre of the teen-harm lawsuits and state chatbot bans without its CEO. California's four AI and mental-health bills (AB 1979, AB 2575, SB 903 and SB 503) were still unsigned on Governor Newsom's desk Saturday afternoon, eleven days before his September 30 deadline; the Governor signed three unrelated bills the same day. A newly registered trial (DEONCAi 3-1) will test whether an agentic AI system improves shared clinical decision-making against a standard chatbot and a conventional decision aid.

`buffer/2026-09-19-rss.jsonl` grew from 128 to 134 rows this afternoon but
the six new rows are the same *Internet Interventions*/*Frontiers in
Psychiatry* journal-issue batch already ruled an aggregator-reindex false
positive on Friday's finalize, plus one unrelated STAT item (Jehovah's
Witnesses and blood-derived products) — nothing new. A name-pass sweep of
the 272 mental-health-tagged rows in this morning's `google_news_rss`
snapshot (ts ≥ 09:00 ET) surfaced nothing else dated to the window beyond
the Disney item above and routine market/analyst-note churn (HIMS, HCA,
UnitedHealth) already on this lens's radar.

## Capital & corporate

- 🕰 **CAUGHT LATE — Disney named Karandeep Anand, until this week the CEO
  of Character.AI, as the company's first-ever Chief Technology Officer,
  effective October 2, reporting directly to CEO Josh D'Amaro and owning
  enterprise technology, infrastructure, data/AI platforms, product and
  engineering across Disney's segments.** The hire is notable specifically
  for the history: roughly a year ago Disney sent Character.AI a
  cease-and-desist alleging unauthorized use of its characters, and a
  number of Character.AI's technical staff are reported to be following
  Anand to Disney. Character.AI is the entity at the center of this
  lens's `ai-therapy-regulatory-reckoning` and `state-therapy-chatbot-bans`
  threads (companion-chatbot harm litigation, state safety-bill lobbying);
  this doesn't move either thread's safety or legal questions on its own,
  but a CEO departure — with staff following — is a real change to who is
  running the company those threads track. Published 2026-09-18; missed
  by Friday's own passes, caught by this afternoon's sweep.
  ([The Walt Disney Company](https://thewaltdisneycompany.com/press-releases/the-walt-disney-company-names-karandeep-anand-to-newly-created-role-of-chief-technology-officer/), [Variety](https://variety.com/2026/biz/news/disney-cto-karandeep-anand-character-ai-1236866528/), [Deadline](https://deadline.com/2026/09/disney-chief-technology-officer-character-ai-1237107626/))
  <!-- k: t=ai-therapy-regulatory-reckoning,state-therapy-chatbot-bans e=character-ai axis=capital-corporate -->

## 🧪 Clinical trials

**One on-topic first-posted registration; the rest of the 219-row buffer
is generic-term noise.** Per this run's brief, every registration in
`buffer/2026-09-19-clinicaltrials.jsonl` matching more than one
non-generic watchlist term was individually checked against
ClinicalTrials.gov's own API rather than dismissed as a term collision —
most (`Canada`, `AMD`, `Big Health` as a substring, `measurement-based
care`, `single-session intervention`, `data center project/attack/
approval` as apparent mismatches) resolved to unrelated oncology,
cardiology and imaging trials with no real connection to this lens.

- **DEONCAi 3-1 (NCT07827924), first posted 2026-09-18 by the Harding
  Center for Risk Literacy: an online experiment testing whether an
  agentic large-language-model architecture can support shared
  decision-making and "informed intentions" in health care, compared
  against a standard LLM and an evidence-based decision aid.** Not yet
  recruiting. Directly on-topic for this lens's evidence base (does an
  AI system actually improve, rather than just accelerate, a health
  decision) — logged as a late catch since ClinicalTrials.gov posted it
  Friday.
  ([ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT07827924))
  <!-- k: t=ai-therapy-evidence axis=research-evidence -->

Also checked and NOT curated: an AI-agent smoking-cessation trial
(NCT07827066, Sun Yat-sen University, first posted 09-18 — behavioral but
not mental-health-specific), and four neuromodulation registrations
first-posted this week (NCT07819773 GAD device, 09-15; NCT07828457 rTMS
for autism social perception, 09-18; NCT07828483 Stanford focused
ultrasound for post-TBI depression, 09-18; NCT07829263 tDCS for cocaine
use disorder, 09-18) — all routine registrations, none yet recruiting or
reporting results, none tied to a tracked company.

## ⏳ Upcoming & expected

**No flips today; 6 pending.**

- 🚧 **`anthropic-wellbeing-grants-deadline-0921` — due 2026-09-21 (2
  days).** Nothing new today.
- 🚧 **`raine-jccp-cmc-0923` — due 2026-09-23 (4 days).** Nothing new
  today.
- 🚧 **`ca-ab1979-governor-action` / `ca-ab2575-governor-action` /
  `ca-sb903-governor-action` / `ca-sb503-governor-action` — all due
  2026-09-30 (11 days).** Confirmed still unsigned as of this afternoon,
  direct per-bill check against `leginfo.legislature.ca.gov` (repeated
  from this morning's check); the Governor's own press-release list
  (`gov.ca.gov/category/press-releases/`) posted three signings today —
  film/TV tax credits, election-interference protection, a state
  military-sovereignty bill — none of the four tracked bills.
- (`mhpaea-replacement-rule`, due 2026-12-31, and `compass-psilocybin-nda`,
  due 2026-12-31, remain pending and far out; omitted from the count
  above.)

## 🔄 Map changes

**None today.**

## 🧵 Thread candidates

**None.** The RAND/JAMA Pediatrics youth-AI-chatbot candidate (first
offered 09-17, carried without repetition on 09-18) found no new evidence
today and drops per this run's brief — track it again only if fresh
evidence lands.

---

A thin Saturday with one real catch: Disney hired Character.AI's own
CEO as its first chief technology officer, a leadership change at the
company two of this lens's threads track closely, missed by Friday's
passes and picked up this afternoon. One on-topic clinical-trial
registration also surfaced — an AI system built to support real health
decisions, not just answer questions. Everything else held in place: the
four California AI-therapy bills still unsigned at eleven days to
deadline, the Sword-Headspace close, the Raine v. OpenAI conference four
days out, Timothy Westlake's still-pending confirmation, and Anthropic's
wellbeing-grant window closing in two days.
