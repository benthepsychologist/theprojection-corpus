---
lens: global-capital
date: 2026-08-14
status: building
window_start: 2026-08-14T05:00:00-04:00
as_of: 2026-08-14T16:45:00-04:00
coverage: pending
---

# Global Capital — 2026-08-14

*Curated agentic-interim from `buffer/2026-08-14-*.jsonl`'s global-
capital lens (~1,700+ items before filtering, dominated by Anthropic-IPO,
CXMT, and Kevin Warsh recirculation from the last 48 hours) plus SEC
EDGAR direct data and WebSearch/WebFetch verification against primary
sources. Covers 05:00 ET through this digest's ~16:45 ET close. This was
a genuinely thin day on new information relative to 08-13: the day's one
real headline event is Berkshire Hathaway's Q2 2026 13F, filed on the SEC's
own deadline this afternoon and pulled directly from EDGAR's XML holdings
table rather than secondary reporting. Beyond that, most of today's high-
volume coverage is continued market reaction to stories already logged
08-13 (Anthropic's $2T IPO chatter, CXMT overtaking Tencent, the Nvidia
$500B financing platform, Kevin Warsh commentary) rather than new fact.
Checked and left out as recirculation, not new: CoreWeave's $104B backlog
and Tuesday's stock pop (that's the 08-11 Q2 print this map's
`ai-buildout-debt-risk` and `coreweave-backlog-bet` threads already have
on file in full); the EA/PIF/Silver Lake $55B leveraged buyout (closed
08-04, still generating explainer pieces); and Greg Abel's $6.8B Taylor
Morrison acquisition (announced/closed months ago per Berkshire's own
press materials — today's pieces are 13F-adjacent retrospectives, not a
new deal).*

## Today's throughline

The day's real news arrived on schedule and through the front door: SEC
EDGAR shows Berkshire Hathaway filed its Q2 2026 13F-HR at 16:05 ET, on
the deadline this map has been counting down to since it was logged
08-04. The filing itself, read directly from the XML holdings table
rather than any single outlet's framing, answers this lens's own
`berkshire-ai-capital-stance` watch cleanly: Berkshire's Alphabet stake
very nearly doubled in share count over the quarter (57.8M to 106.0M
combined Class A/C shares) and its dollar value grew faster still ($16.6B
to $37.8B) on top of price appreciation — the position Buffett himself
has framed as an AI-capex bet kept growing, sharply, and no other
AI-adjacent equity name joined it. The rest of the portfolio moved in a
distinctly non-AI direction: Berkshire exited Constellation Brands
entirely, trimmed Bank of America, Capital One and Kroger, grew Delta
significantly, and opened a token toehold in D.R. Horton — a housing/
consumer-defensive rebalancing sitting alongside, not instead of, the
AI-capex bet. Total disclosed equity value rose to $299.25B from
$263.1B, though a 13F discloses only long equity positions, not cash —
Berkshire's own Q2 earnings (already on this thread's record, 08-08) is
still the actual source for the cash figure. Elsewhere, the AI-buildout
debt story that turned skeptical yesterday continued quietly: AMD's bond
sale (logged 08-13 as "up to $5B") priced this morning at a final $4.75B,
with shares up 5.6% on the news — a clean confirmation of yesterday's
report rather than a new development in its own right.

## Deals & filings

- **Berkshire Hathaway's Q2 2026 13F, filed 2026-08-14 at 16:05 ET —
  exactly on the SEC's own deadline — shows its Alphabet stake nearly
  doubled in share count over the quarter and no other AI-adjacent
  equity joined it.** Pulled directly from EDGAR's XML holdings table
  (accession 0001193125-26-352200, period of report 2026-06-30):
  combined Alphabet Class A + Class C shares rose from 57.83M to 106.0M
  (+83%), dollar value from $16.63B to $37.76B (+127%, share-count growth
  plus price appreciation) — consistent with, and now confirming in
  filed-position form, the $10B-in-Q2 figure Berkshire's own earnings call
  disclosed 08-08. Total disclosed 13F equity value rose to $299.25B from
  $263.1B a quarter earlier (13Fs disclose only long equity positions, not
  cash). No Nvidia, Microsoft, or any other AI-adjacent name appears
  anywhere in the 29-issuer portfolio. Elsewhere in the filing: Berkshire
  exited Constellation Brands entirely, trimmed Bank of America (513.6M
  to 483.4M sh), Capital One (7.15M to 3.0M sh, -58%) and Kroger (50M to
  39M sh), grew Delta sharply (39.8M to 57.3M sh, +44%), and opened a
  token new position in D.R. Horton (3,564 sh, ~$580K) — a real
  rebalancing toward housing/consumer names sitting alongside, not
  displacing, the Alphabet buildout. This directly resolves the
  `berkshire-q2-2026-13f` upcoming.yaml expectation: **HIT**, filed
  precisely on its due date.
  ([SEC EDGAR filing index](https://www.sec.gov/Archives/edgar/data/1067983/000119312526352200/0001193125-26-352200-index.htm), [13F information table (XML)](https://www.sec.gov/Archives/edgar/data/1067983/000119312526352200/56757.xml))
  <!-- k: t=berkshire-ai-capital-stance e=berkshire-hathaway axis=deals-and-filings interp=yes sev=major -->

- **AMD's bond sale — logged 08-13 as "up to $5 billion" — priced this
  morning at a final $4.75 billion across four tranches, with the
  longest tranche tightening about a quarter-point from initial price
  talk to +0.9 points over Treasuries; AMD shares rose 5.6% on the
  print.** A clean close on yesterday's story rather than a new
  development — the pricing confirms the AI/Anthropic-stake framing
  press coverage attached to the raise held through final terms, without
  AMD itself ever making that link explicit in official documentation.
  ([GuruFocus](https://www.gurufocus.com/news/9035192/amd-stock-jumps-56-while-475-billion-debt-deal-lands))
  <!-- k: t=ai-buildout-debt-risk axis=deals-and-filings -->

## 📊 Macro strip

- **Brent crude: ~$88.38/bbl, +1.51%** (tradingeconomics.com, 2026-08-14)
  — up from yesterday's $87.11 close; Hormuz risk premium ticking back up
  after Thursday's overnight ADNOC tanker attack (logged on 08-13's
  digest/`red-sea-oil-shock`), still not a sharp spike.
- **30-year Treasury yield: 5.216%** (Thursday's auction result, carried
  forward — no new 30-year auction today) — the standing print from
  08-13's finalize.
- **VIX: 14.63** (FRED, 2026-08-13, most recent available read) —
  unchanged from yesterday's macro strip.
- **September FOMC rate-hike probability: ~30.4%** (market-implied,
  per today's coverage of the July inflation prints) — down from
  readings earlier this week, as the soft PPI/jobless-claims pair logged
  08-13 continues feeding into rate expectations; no new hard data
  today, this is the market repricing the same prints.

## ⏳ Upcoming & expected

- `berkshire-q2-2026-13f` — **HIT**, filed 2026-08-14 at 16:05 ET, on
  its due date. See Deals & filings above for the full read.
- `decart-acquisition-close` (due ~08-17) — still unresolved; no new
  reporting found today past 08-13's Anthropic report and Musk's denial
  that SpaceX is the buyer. 3 days out.
- `iran-oman-hormuz-deal-signing` (due 08-19) — no new signature; the
  standoff continues (see Macro strip). 5 days out.
- No other global-capital-relevant expectations came due today.

## 🔄 Map changes

- `~ threads/berkshire-ai-capital-stance` — the Q2 2026 13F results
  (Alphabet stake nearly doubled, no new AI-adjacent name, non-AI
  rebalancing elsewhere); timeline entry written, resolving the thread's
  own core watch item.
- `~ threads/ai-buildout-debt-risk` — AMD's bond final pricing ($4.75B);
  brief addendum to yesterday's entry, not a new dated block.

## 🧵 Thread candidates

- No new candidates today. The data-center-landlord/REIT candidate
  offered 08-13 (twice) got no further data points today; per the
  reappearance rule it was offered once more in 08-13's finalize and now
  drops rather than recurring a third time.

**Flash test: No.** Nothing today clears the "would this lead a general
news front page independent of these lenses" bar — Berkshire's 13F is a
real, on-schedule data point for this lens specifically, not a general-
news event; AMD's bond pricing is a routine confirmation; and the day's
highest-volume coverage (Anthropic IPO chatter, CXMT, Warsh commentary)
is all continued reaction to stories already flashed-tested and passed
over on 08-13.

---
Berkshire Hathaway filed its Q2 13F right on the SEC's deadline this
afternoon, and the filing itself — read straight off EDGAR rather than
anyone's summary — shows the Alphabet stake nearly doubled in share
count over the quarter to $37.8 billion, with no other AI-adjacent
equity joining it, while the rest of the portfolio rebalanced toward
housing and away from a handful of consumer names. AMD's bond sale from
yesterday priced final at $4.75 billion, confirming the story rather than
adding to it. Otherwise today was mostly yesterday's stories still
circulating — Anthropic's $2 trillion IPO chatter, CXMT's new-most-
valuable-in-China status, Kevin Warsh commentary — with oil ticking back
up slightly on Thursday night's tanker attack but nothing sharp enough to
call a new event.
