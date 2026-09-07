---
lens: global-capital
date: 2026-09-05
status: final
window_start: 2026-09-05T05:00:00-04:00
coverage: done
---

# Global Capital — 2026-09-05

*Curated agentic-interim, 05:00 ET Saturday → **05:00 ET Sunday**. Built at
10:45 ET, extended at 15:00 ET (a combined macro/financing/chips sweep, a
buffer-triage pass, a second collector round), and **finalized on the 09-06
run** — a lens sweep over all 20 capital threads and a buffer triage over
the Saturday-evening window, plus the coverage critic appended below.
Sources: the
deterministic collector lanes launched as separate processes at run start
(`google_news_rss` 6,444 items, `sec_edgar` 428, `gdelt` 90, `rss` 70,
`federal_register` 29), a macro/rates/allocators sweep that sourced
Friday's close, a financing-and-chips sweep that checked twelve issuers'
EDGAR submissions directly, a capex-and-sites sweep, and two buffer-triage
passes plus a dedicated second pass on the late lane. Markets are closed
until Tuesday 09-08 (Labor Day). Material dated 09-04 that landed after
Friday's 15:00 ET cut — the close, the yen, Anthropic's slip — is in
`2026-09-04-global-capital.md` as a 🌙 late catch.*

## Today's throughline

Brent settled Friday at $96.28, up 7.6% on the week — its steepest weekly
gain in months — with WTI up 10% and US diesel at a record $5.85 a gallon,
on the Gulf-base strikes, Ukrainian refinery hits and a Hormuz transit
count that fell to four vessels on Thursday against a fifteen-a-day
average. That is Reuters' settlement print, and it corrects two days of
"$95-97, no new driver" carried here from secondary outlets: the
settlement is the authoritative figure and the driver was there all along. The one thing that happened on
this lens on Saturday happened at sea, and the market that will price it
is closed until Tuesday. **CENTCOM disabled
two IRGC crude carriers off Kharg Island and Jask and destroyed a third in
the Gulf of Oman after the IRGC fired ballistic missiles at a US carrier
and a destroyer.** Kharg handles roughly 90% of Iran's crude exports; the
Downy was struck in its waters. Every prior oil event in this war — the
Sidr tanker toll, the sixteen ADNOC hits, the Gulf-base strikes that
whipsawed Brent between $95 and $99 this week — has been a shipping and
underwriting story. A strike at the export terminal's own anchorage is
the first that could reprice the terminal, and with Brent's last settlement at $96.28 — up 7.6% on the week, its steepest weekly gain in months — and no US session until 09-08, the first print to
carry it is three days away. The interpretation below is written to that
gap.

Everything else this lens learned today it learned about Friday. **The
chip-versus-tech decoupling held into the close** — the semiconductor index
finished up 3.38% while all three major averages closed lower, the 2-year
at 4.37% and the 10-year at 4.78% — so the resilience the morning read as
AI-specific survived the full session. **Anthropic's public S-1 slipped to
late September**, marketing from mid-October, the $15bn revolver first.
And the coverage critic found the sixth documented miss in the
cross-border-rates seam in nine days — Bloomberg's carry-trade-unwind
lead, the yen at a one-month high into the 09-18 BOJ meeting, sitting in
nine rows of Friday's buffer — and **this run opened `cross-border-rates`
as a thread on the critic's own authority**, the first time this map has
done that. The candidate had been offered three times. The seam is now a
place for matches to land rather than a recurring line in the coverage log.

## Capital in my markets

- **US Central Command disabled two IRGC crude carriers off Kharg Island
  and Jask and destroyed a third in the Gulf of Oman on Saturday, after the
  IRGC fired ballistic missiles at a US carrier and a destroyer that
  "successfully evaded" them.** The strikes hit "critical components" to
  render the M/T Downy and M/T Stark 1 inoperable rather than sink them,
  limiting spill risk, and the unladen M/T Kylo was destroyed after its
  crew abandoned ship; no casualties either side. Kharg Island handles
  roughly 90% of Iran's crude exports, and the Downy was hit in its waters
  — the first US strike on Iranian tanker traffic at the terminal itself
  rather than in transit. Brent settled Friday at $96.28, +7.6% on the week, its steepest weekly gain in months, with US diesel at a record $5.85/gal; no US session until Tuesday 09-08.
  ([CNN, via KVIA](https://kvia.com/news/us-world/cnn-world/2026/09/05/us-military-says-three-iranian-tankers-struck-in-gulf/), [AP, via KSAT](https://www.ksat.com/news/world/2026/09/05/iran-accuses-the-us-of-targeting-a-tanker-near-kharg-island-and-other-mideast-news/))
  <!-- k: t=red-sea-oil-shock,iran-conflict-widening e=united-states axis=oil sev=major interp=yes -->
- **AI companies have pledged about $265 million to super PACs and
  political groups for the 2026 midterms, a Wall Street Journal analysis
  found — making AI, alongside crypto and betting, the leading industry
  spender of the cycle — The Independent reported on Saturday, framing the
  money as arriving "as data center backlash sweeps through communities."**
  The parts were on the record separately: Leading the Future, the
  Andreessen Horowitz/Greg Brockman-backed super PAC, at $140 million
  raised per Reuters (a16z's $50 million and the Brockmans' $25 million in
  FEC filings); Anthropic's self-disclosed $40 million to Public First
  Action, a 501(c)(4) backing AI regulation; and Leading the Future's
  "Build American AI" affiliate running buildout-defence ads in Wisconsin,
  Ohio and Kansas since late August. New is the aggregate and its framing
  as a response to local opposition — the industry's political spend set
  against the backlash this thread tracks for the first time. A tally of
  pledges, not disbursements; the Journal's own analysis could not be read
  directly. ([The Independent, via Yahoo News](https://ca.news.yahoo.com/ai-companies-dumping-265m-midterms-122332804.html), [WSJ, 07-22](https://www.wsj.com/politics/policy/anthropic-doubles-midterm-spending-to-40-million-to-push-ai-regulation))
  <!-- k: t=datacenter-backlash-capital-risk e=anthropic,openai axis=policy -->

## Deals & financing

Nothing dated 09-05. One 09-03 item reached the record on the afternoon
run: **FluidStack, the GPU-cloud builder holding a roughly $50 billion
multi-year capacity agreement with Anthropic, reached an $18 billion
valuation per Forbes**, closing the round Bloomberg reported in April as
~$1 billion in talks led by Jane Street — a third independent capacity
vendor alongside CoreWeave and Nebius, and a price on the counterparty
carrying a large share of Anthropic's committed compute. The company had
no mention anywhere in this corpus until now. On
`anthropic-infrastructure-buildout`.

Twelve issuers' EDGAR submission feeds — Nvidia, AMD,
Intel, Broadcom, Micron, CoreWeave, Oracle, Arm, Qualcomm, GlobalFoundries,
TSMC, ASML — were read directly for Friday-after-close filings: four
routine Form 3/4 insider transactions and nothing else. No rating action
or bond pricing for CoreWeave, Oracle, xAI or Meta. No first deal under
Nvidia's $500bn compute-financing platform (ledger due 09-15). The
financing news of the window is Friday's, in the late catch and the
frontier-AI digest: Anthropic's slip and revolver, Thinking Machines'
$40bn round with Nvidia at $2.5bn, Moonshot's $3-5bn, Nscale's $3.5bn
pre-IPO ask.

## 📊 Macro strip

*Friday's close, carried forward — no session today.* **S&P 500** 7,718.60
(-0.38%) · **Nasdaq Composite** 26,506.99 (-0.29%) · **Dow** 53,414.25
(-0.51%) · **SOX** 11,735.26 (+3.38%) · **2-year** 4.37% · **10-year**
4.78% (Treasury daily par yield curve) · **Dollar index** ~99.15 · **Brent**
$96.28 settle (+7.6% w/w, Reuters) · **WTI** $91.48 · **US diesel** record $5.85/gal · **Sept hike odds** 58-65% at Friday's close by
tracker · **Yen** 155 range, one-month high · **Next US session** Tuesday
09-08 · **Next dated tests** Canada's counter-tariffs 09-08, Treasury's
first doubled buyback 09-09, Oracle Q1 FY27 09-10, FOMC 09-16, BOJ 09-18.

## ⏳ Upcoming & expected

- 🚧 `canada-retaliatory-tariffs-effective-0908` — **still open until
  09-08**, no Friday or Saturday confirmation, delay or exemption update
  beyond the 08-25 product list (15/25/50% tiers, ~C$27.6bn of US goods);
  no US response found.
- ⚠️ `decart-acquisition-close` — passed-silent, grace to 09-07, re-checked
  and still silent.
- `+` **`anthropic-public-s1-late-sept`** (09-30, reported) — see the late
  catch. `+` **`ratepayer-protection-act-floor-vote-0911`** (week of
  09-08, rumored) — Roll Call has House Republicans without consensus on
  timing or scope; a slip is the likelier outcome and is itself the signal.
- 📋 `oracle-q1-fy27-earnings` (09-10, unchanged), `nvidia-500b-financing-
  first-close` (09-15), `fomc-september-decision` (09-16),
  `boj-september-meeting-0918` — the last now with a thread to land on.

## 🔄 Map changes

- `+` **thread `cross-border-rates`** (global-capital, weight 2,
  **critic-add**) — opened on the coverage critic's auto-growth authority
  after the sixth documented miss in the seam; the candidate was offered
  09-02, 09-03 and 09-04. Terms: carry trade, yen carry trade, carry trade
  unwind, BOJ rate decision, Ueda rate hike, Takata BOJ, JGB yield, gilt
  yield, OAT spread, Katayama BOJ. First entry: the 09-04 yen move. **Ben
  can retire it with a word; the case is the miss count, not a theory.**
- `+` watchlist terms `carry trade`, `yen carry trade`, `carry trade
  unwind` (critic-add; `yen intervention`, also proposed, was already on).
- `✎` **afternoon run:** entries merged on `datacenter-backlash-capital-risk`
  (the $265m tally, above) and `anthropic-infrastructure-buildout`
  (FluidStack, 09-03); the combined afternoon sweep over all 30 lens
  threads found nothing else dated 09-05 — Canada's 09-08 counter-tariffs
  re-checked on Finance Canada's own page, still on; no Saturday Fed or
  Trump rate statement; no weekend BOJ/MOF comment beyond the record.
- `✎` timeline entries merged on `chip-hyperscaler-rotation` (the close),
  `red-sea-oil-shock` (South Korea's walk-back, 09-04; the tanker strikes,
  09-05), `anthropic-ipo-timing`, `nvidia-vendor-financing` (Thinking
  Machines, 09-03), `datacenter-backlash-capital-risk` (Starlink discount,
  Ratepayer Protection Act), `nuclear-for-ai` (PJM/Oklo, 08-28).
- `+` two dated expectations logged on this lens (above), six across the
  map.
- `✎` standing synthesis refreshed for `anthropic`, `openai` and
  `united-states` in `attention/actor-doing.yaml`.

## 🧵 Thread candidates

- ✅ **The cross-border rate leg is no longer a candidate** — opened as
  `cross-border-rates` this run (above). Offered 09-02, 09-03, 09-04; the
  "second and final offer" rule was overridden on 09-04 because the misses
  kept coming, and a sixth arrived.
- **Venezuela** *(second offer; cross-lens with world news)* — Chevron's
  $7bn-plus commitment to more than double production from its Venezuelan
  joint ventures, welcomed publicly by the Treasury Secretary, in a country
  whose head of state is in custody. A US major's multi-billion bet with
  Treasury applauding is this lens's story as much as the other's. **Track
  it?**

## 🚨 Flash

**None.** A tanker strike with markets closed is a Tuesday-open question,
not a front page.

## ⚠️ Collection note

All lanes launched with the right environment and landed. `google_news_rss`
took twenty-five minutes and arrived after the first triage pass closed;
a second dedicated pass read it. `sec_edgar` logged HTTP 500 on EDGAR
full-text search for many terms yet wrote 428 rows, and the financing
sweep's own direct `data.sec.gov` submission queries for all twelve issuers
worked cleanly — the lane's 500s are on the full-text endpoint, not on
EDGAR itself. Friday's close was sourced from Treasury's own daily yield
curve CSV (the HTML table misread on two fetches and was abandoned for the
CSV) and from two independent market wraps; individual Intel, AMD and
Nvidia closes could not be sourced and are left blank. ⚠️ `theprojection
build-world-news` blocked for a third day on the BigQuery credential.

## 🌙 Late catch — the 09-05 evening window (15:00 ET → 05:00 ET)

One item dated 09-05 reached the record on the finalize, and it was in
Saturday's buffer rather than the evening's:

- **In the week before the Fed's 09-15/16 meeting the president, the vice
  president, the Treasury secretary and senior counselor Peter Navarro all
  publicly urged the Fed not to raise rates or to cut them — Navarro
  calling FOMC members "clowns" on Steve Bannon's show on Friday and a hike
  "careless," Vance saying "we believe that the Fed should be lowering
  interest rates," Bessent arguing the Fed does not hike into a supply
  shock until second- or third-order effects show — on top of Trump's
  Friday threat to halt trade with surplus countries unless the Fed cuts,
  the first time he has tied tariffs to Fed policy.** CNBC's Saturday tally
  is the first to frame the four as one campaign, ten days out with the
  hike priced near 60% and Friday's CPI the last data point; the president
  has still not criticised Warsh by name, and the precedent CNBC reaches
  for is May 2019, when Pence, Mnuchin and Kudlow all called for cuts and
  the Fed cut two months later. The Navarro and Vance remarks were not on
  `fed-independence-fight` until now.
  ([CNBC](https://www.cnbc.com/2026/09/05/trump-warsh-fed-september-rate-hike.html))
  <!-- k: t=fed-independence-fight e=united-states axis=policy -->

Two more finalize additions are dated earlier and live in their own days'
records: **Japan's $550 billion investment pact re-pointed at AI and
chips** — Akazawa in Washington on Friday, nine rows of Saturday's buffer,
caught by the critic's wire backstop — is a 🌙 late catch in
`2026-09-04-global-capital.md` and a thread candidate on the 09-06 digest;
and **CXMT's DRAM share reaching 10%** (Counterpoint, 09-04), already in
Friday's frontier-AI digest, now also carried on `cxmt-memory-ipo`, the
thread that will need it when the prospectus comes. Nothing else dated
09-05: no weekend Fed, BOJ or MOF statement, Canada's counter-tariffs
still on for Tuesday 12:01 a.m. per Finance Canada's own list, Oracle's
Thursday date confirmed by its own IR page, the EDGAR lane empty on a
Sunday as expected.

## 🔍 Coverage critic — digest-day 2026-09-05

**Verdict:** one real miss, and it came entirely from the wire backstop —
the first formal run of the proposal `coverage-log.md` has carried since
late August. **Japan and the US advanced the $550 billion investment pact
with AI and semiconductors now at its center**, per Akazawa's own remarks
in Washington on Friday, carried by Bloomberg (timestamped 01:31Z 09-05),
Japan Times, SCMP and Kyodo, and sitting in nine rows of Saturday's
`google_news_rss` buffer — eight of them tagged to the AI lens by term
match, one to this lens via "SoftBank." A curation miss the lens-tagging
helped cause. The benchmark set itself was null: Money Stuff silent by its
own feed, FT Unhedged weekday-only by its own dated items, the two
same-day-only pages unauditable and Bloomberg Technology CAPTCHA-walled on
both documented transports.

| benchmark | state | evidence |
| --- | --- | --- |
| Money Stuff | dark 09-04 and 09-05 | `.rss` author feed's newest item Thu 09-03 18:24 GMT |
| FT Unhedged | dark for 09-05 | `www.ft.com/unhedged?format=rss` newest item Fri 09-04 05:30 GMT; nothing over the weekend |
| Axios Pro Rata | same-day-only, not auditable | reader proxy returned a stale generic page |
| Bloomberg Technology | same-day-only; CAPTCHA'd | "Are you a robot?" on direct and proxy fetch — reachable 08-23, blocked 08-25, blocked again |

**They led with → we missed:** the Japan pact (curated into the 09-04
digest as a late catch, dated 09-04; no thread — candidate on 09-06).
**Unverifiable at pass time, resolved by the main session:** CNBC's
"Trump turns up the heat on Warsh" — the critic could not resolve the URL
through Google News' rate limit; found in CNBC's own RSS and curated above.
**Both covered:** the tanker strikes, Friday's close and Brent's
settlement, the carry-trade unwind, Anthropic's S-1 slip, Canada's
tariffs. **We had → they didn't:** the interpretation written to the
Tuesday-open gap; the EDGAR direct reads.

**Structural:** the benchmark set is a weekday instrument, and this pass
confirms it in both directions again; Bloomberg Technology's reachability
is unstable pass to pass; and `news.google.com` itself rate-limited the
reader proxy mid-pass, which means a story whose only fetchable copy is
Google-News-wrapped cannot currently be resolved to a real URL when the
publisher also blocks — the Reuters synthetic-diamond exclusive under the
same pact was left as corroboration for that reason. **Proposed:** the
pact as a thread; terms `Akazawa`, `Japan investment pact`, `$550 billion
pact`; and the backstop run on weekday passes too, lightly — the one
finding this pass produced came from it. **Access:** FT Unhedged's working
RSS path is `www.ft.com/unhedged?format=rss`, not `/newsletter/unhedged`;
investing.com is now permanently blocked to anonymous fetches.
