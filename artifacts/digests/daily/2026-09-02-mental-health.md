---
lens: mental-health
date: 2026-09-02
status: building
window_start: 2026-09-02T05:00:00-04:00
as_of: 2026-09-02T15:00:00-04:00
coverage: pending
---

# Mental Health — 2026-09-02

*Curated agentic-interim, 05:00 ET → **15:00 ET** Wednesday. Sources: 8
hot-cluster sweeps at 10:00 ET plus a 26-thread cluster sweep at 15:00 ET,
plus the deterministic collector lanes. ⚠️ **The news collectors did not run
today** — see the note at the end. The day's real mental-health news is
dated 08-31/09-01 and is folded into `2026-09-01-mental-health.md` as a 🌙
late catch; that digest's own 15:00 ET read called the day quiet and had to
be corrected on the finalize, which is worth knowing before reading this
one.*

## Today's throughline

Four of California's five pending AI-and-mental-health bills sat still
today and the fifth moved one procedural step, leaving all of them on
Governor Newsom's desk or one signature short of it. **SB 903, SB 1119 and
AB 2575 remain at "ordered to engrossing and enrolling"** as of 08-31, none
yet formally presented to the Governor; **AB 1979 was formally Enrolled on
09-01**, the step immediately before presentment; and SB 503 has been with
the Governor since 08-30. Newsom has until roughly 09-30 on all of
them, and his office has posted no bill-action release on either day. **This
is expected quiet, not a gap** — every one of those statuses was read off
the Legislature's own pages rather than inferred from coverage, which on
these bills has been running days behind the roll call.

## Regulation & legislation

- **California AB 1979 was formally Enrolled on 09-01, putting it one step
  ahead of the three bills this lens has been counting down.** AB 1979
  (Bonta) brings consumer health chatbots under the Confidentiality of
  Medical Information Act and bars clinical decisions from being made on AI
  output alone without human review. Enrollment means the final text has
  been printed and certified — the step immediately before presentment to
  the Governor. No presentment date, signature or veto has posted. ⚠️ Dated
  09-01, caught on the 09-02 afternoon sweep from the bill's own status page.
  ([AB 1979 bill status, California Legislature](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB1979))
  <!-- k: t=ai-therapy-regulatory-reckoning e= axis=regulation-and-legislation -->

- **The other four tracked California bills: no movement, verified against
  the Legislature's own pages rather than inferred.** SB 903, SB 1119 and
  AB 2575 all remain at 08-31's "ordered to engrossing and enrolling" /
  "Senate amendments concurred in. To Engrossing and Enrolling," with no
  enrollment, presentment, signature or veto. **SB 503** (on
  `payer-ai-claim-denial`) remains "Enrolled and presented to the Governor
  at 6 p.m." on 08-30, matching what is already on that timeline. All five
  `*-governor-action` ledger entries stay correctly open to 09-30.
  <!-- k: t=ai-therapy-regulatory-reckoning,state-therapy-chatbot-bans,payer-ai-claim-denial e= axis=regulation-and-legislation -->

## Research & evidence

None dated 09-02. The `clinicaltrials` and `semantic_scholar` buffers were
read and returned noise rather than signal: two topical-looking
ClinicalTrials hits (NCT05555875, NCT06778564) are **old registrations
surfaced by keyword match**, not new trials, and all fourteen
semantic_scholar entries are false-positive term collisions — "Universal
Health Services behavioral" matching unrelated Indonesian HIV/nutrition
papers, "Hims & Hers" matching a paper on Agatha Christie. **Recorded
because a checked-and-empty result is a different thing from an unchecked
one**, and this lens's own critic pass has twice now turned up real academic
findings that a thinner check would have missed.

## Payers, providers & the money

None dated 09-02. Targeted checks on Kaiser mediation, Character.AI and Grok
litigation, FDA and FTC chatbot action, MHPAEA rulemaking, and the Compass
Pathways NDA all returned previously-known background only.

## ⏳ Upcoming & expected

**Ledger checks today** (full evidence in `attention/upcoming.yaml`) — all
five checked directly against the Legislature's own pages, all **still open
until 2026-09-30**, none signed or vetoed:
`ca-sb903-governor-action` · `ca-sb1119-governor-action` ·
`ca-ab2575-governor-action` · `ca-ab1979-governor-action` (with the
enrollment progress above) · `ca-sb503-governor-action`.

**Due in the next 7 days:** none on this lens's ledger.

**Due 09-14:** `fda-psychedelic-public-hearing` — the FDA's hybrid public
hearing on "Considerations for Potential Future Therapeutic Use of
Psychedelic Drugs," White Oak campus, 12:30-4:30pm ET, implementing EO
14401. Written comments stay open through 2026-10-05. Also 09-14:
`sword-headspace-acquisition-close-0914`.

## 🔄 Map changes

- `+` two watchlist terms, `National Survey on Drug Use and Health` and
  `NSDUH` (critic-add). The reasoning matters more than the terms: this is
  the second single-source substance-use-trend finding in under a week
  (cannabis use disorder after 08-31's stimulant use disorder), and **both
  trace to the same underlying federal survey rather than to either
  trade-press write-up.** Watching the survey is cheaper and more reliable
  than catching the riffs on it.
- `+` two timeline entries on `ai-therapy-evidence` from the coverage critic
  — the two JMIR papers described in yesterday's digest.
- **On record from the critic, not yet acted on:** move JMIR Mental Health
  (and ideally npj Digital Medicine) from the `weekly_add` tier to
  every-pass checking. It published twice yesterday, both directly on this
  lens's flagship evidence thread, and the standing rotation would not have
  caught either. The cost is one feed fetch.

## 🧵 Thread candidates

- **A substance-use-trend frame** — carried forward from yesterday's critic
  pass, not re-offered as new. Two single-source findings from the same
  federal survey in under a week. The watchlist terms are the cheap half;
  whether it earns a thread is your call, and a third instance would settle
  it either way. **Promote?**

## 🚨 Flash

**None.**

## ⚠️ Collection note

`google_news_rss`, `rss` and `gdelt` produced no buffer file for 09-02
across two full collector runs. `federal_register` **did** run — its
provenance manifest confirms a 14:00:40Z pass against this map's full term
list returning `items: []`, which is a confirmed-empty result rather than a
missing one, and the sweep verified that distinction against the manifest
rather than assuming it. Today's legislative checks came from direct
`leginfo.legislature.ca.gov` fetches, cross-checked across bill status,
history and nav pages.

---
Four of five tracked California bills sat still and the fifth moved one
procedural step, verified against the Legislature's own pages rather than
waiting on the trade press. On this lens that is a clean result — but
yesterday's digest made the same call at the same hour and was wrong by five
items, so it is worth reading this one as "checked and empty," not "quiet."
