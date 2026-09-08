---
lens: global-capital
date: 2026-09-07
status: final
window_start: 2026-09-07T05:00:00-04:00
coverage: done
---

# Global Capital — 2026-09-07

*Curated agentic-interim, **05:00 ET 09-07 → 05:00 ET 09-08**, the full
digest-day; finalized on the 09-08 10:00 ET run.
Sources: one capital cluster sweep, the 09-06 coverage critic for this
lens, and main-session verification of every price in the strip below
against Yahoo's own settlement series plus CNBC. **⛔ No deterministic
collectors ran — `cloud-researcher` is not installed and `buffer/` does
not exist, so there was no `sec_edgar`, `epfr_flows` or `gdelt` lane
behind any of this.** Material dated 09-06 is in yesterday's digest,
which this run finalized — with two corrections to it, both below.*

## Today's throughline

Oil is not a US market, and while American equities and bonds were shut for
Labor Day, Brent and WTI reopened on Sunday evening into a widening Gulf
war. Brent is an ICE London contract and WTI trades on CME Globex under
modified holiday hours; both opened at 18:00 ET Sunday, and this map spent
two days describing the lens as closed when it was not. They
reopened into the Gulf war widening onto Saudi soil: Aramco facilities
struck again, the 400,000-barrel-a-day Jizan refinery hit for the third
time since summer, and a US Defense Secretary saying publicly that the
United States will sink Iranian tankers. **Brent rose 1.5% to $97.73, as
high as $97.93, its strongest since 23 July; WTI rose 1.8% to $93.10.**
Goldman put $120 on the table as a risk case — explicitly not its base
case, which is a wide $80-120 depending on whether Gulf exports normalise
— and recommended natural gas and diesel as the cheaper hedges.

The more useful thing this run produced is a correction, not a price.
**This map carried Brent's Friday settlement as $92.68 for four days. It
was $96.28.** The disproof was sitting on the same line the whole time:
the "+0.8% on the day, +7.6% on the week" recorded beside the level
reconcile with $96.28 and would be −3.0% and +3.8% from $92.68. Worse than
the transposition, the map **noticed** the contradiction — its own
secondary sources were reporting $95-97 — and resolved it the wrong way,
writing a note that declared the transposed figure authoritative and
dismissed the correct reads as "intraday or a different contract." That
note was then copied onto the `red-sea-oil-shock` timeline. A wrong number
was defended against correct evidence for three days and reached the
public site. Both notes are now inverted in place rather than deleted, and
the fix is arithmetic that costs nothing: this lens prints a level and a
percentage change side by side every day, they check each other, and that
check had never been run.

## Capital in my markets

- **Brent crude rose 1.5% to $97.73 a barrel, touching $97.93 — its
  highest since 23 July — and WTI rose 1.8% to $93.10, also a late-July
  high, after Saudi Aramco facilities were struck again and US and Iranian
  forces fired on each other's ships over the weekend.** Both contracts
  reopened at 18:00 ET Sunday; the "closed until Tuesday" framing this map
  used for two days applied only to US cash equities and bonds.
  ([CNBC, 14:52Z](https://www.cnbc.com/2026/09/07/oil-prices-rise-to-6-week-high-after-iran-and-us-trade-blows-saudi-aramco-facilities-reportedly-hit.html))
  <!-- k: t=red-sea-oil-shock e=iran,saudi-arabia axis=capital-in-my-markets sev=major interp=yes -->
- **Goldman Sachs said crude could reach $120 a barrel if attacks on Middle
  East shipping intensify, while keeping its base case a wide $80-120
  range depending on whether Gulf exports normalise or the disruption
  broadens.** Commodities co-head Daan Struyven said "events over the last
  few days do suggest that the risk of shipping disruptions broadening and
  intensifying is an important one"; the bank recommended natural gas and
  diesel exposure as the hedge rather than crude itself.
  ([Bloomberg via BOE Report](https://boereport.com/2026/09/06/goldman-sees-120-bbl-oil-risk-if-attacks-on-middle-east-vessels-intensify-bloomberg-reports/),
  [Seeking Alpha](https://seekingalpha.com/news/4640546-goldman-sachs-warns-mideast-ship-attacks-could-push-oil-to-120?feed_item_type=news))
  <!-- k: t=red-sea-oil-shock e=goldman-sachs axis=capital-in-my-markets -->
- **Iran's Supreme National Security Council secretary Mohsen Rezaei said
  Tehran will declare a "restricted zone" from the US naval blockade line
  through the Strait of Hormuz into the Persian Gulf, adding any ship that
  enters it to Iran's sanctions list — with no published boundaries and no
  date beyond "coming days and weeks."** Hormuz transits are running 6-10
  vessels a day against a pre-war baseline near 130. For this lens the
  undrawn zone is the underwriting question: a war-risk premium prices a
  defined exclusion differently from an undefined threat.
  ([Al Jazeera](https://www.aljazeera.com/news/2026/9/7/can-iran-enforce-a-restricted-zone-in-the-strait-of-hormuz))
  <!-- k: t=red-sea-oil-shock e=iran axis=capital-in-my-markets -->

## 🌙 Late catches

- **SoftBank's Tokyo shares rose 11.2% in a single session, its largest
  one-day move since July's limit-up, as AI risk appetite returned across
  Asia.** ¥5,590 on Friday to ¥6,217 on Monday's close — verified directly
  against the settlement series for `9984.T` rather than taken from the
  headline. Asia traded a full session while US markets were shut, so this
  is the day's largest single move on any thread this map tracks, and it
  happened on a lens the sweep reported as closed.
  <!-- k: t=softbank-all-in e=softbank axis=equities sev=major -->

- **Rosneft shipped first crude from the $157bn Vostok Oil project**, the
  Russian Arctic development that routes exports to Asia over the Northern
  Sea Route rather than through sanctioned western channels. ⚠️
  Single-outlet (OilPrice.com) and not independently corroborated; the
  $157bn figure is the project's own long-standing headline number, not a
  new disclosure. Nothing on this map has owned Russian energy-project
  capital flows, so it is offered as a candidate below rather than forced
  onto `russia-ukraine-war`.
  <!-- k: e=russia axis=capital -->

## 📊 Macro strip

⚠️ **Read the timestamps.** US cash equity and bond markets were **closed**
for Labor Day — there is no US close today and no new Treasury print, so
Friday's 2-year 4.37% and 10-year 4.78% stand as the last reads. Every
level below was pulled in the main session with its own timestamp rather
than taken from a sweep report; **four figures in the sweep's proposed
strip were wrong and were discarded** (see the collection note).

**Brent** $97.73, +1.5%, intraday high $97.93, highest since 23 July —
against Friday's corrected $96.28 settle (CNBC 14:52Z) · **WTI** $93.10,
+1.8%, also a late-July high · **Nikkei 225** 66,399.84, **+2.12%** on
Monday's close (06:45Z) against Friday's 65,020.94 · **Hang Seng**
25,413.12, **−0.93%** (08:08Z) against Friday's 25,650.87 · **Shanghai
Composite** 3,932.70, **+0.07%** (07:00Z), essentially unchanged ·
**STOXX 600** 649.90, flat (+0.00%) · **FTSE 100** 10,822.13, −0.08% ·
**DAX** 26,006.53, −0.15% · **Gold** $4,476.60, **+1.06%** against
Friday's $4,429.80 · **USD/JPY** 154.34 · **EUR/USD** 1.16 · **2-year**
4.37% and **10-year** 4.78%, both carried from Friday, no US session.

**The read:** Asia split on the oil move — Tokyo up 2.1%, Hong Kong down
0.9% — while Europe did essentially nothing and gold took the safe-haven
bid. With no US session, the first American price of the Gulf's weekend is
Tuesday's open, which now has both the Aramco strike and the sink-the-
tankers statement to absorb at once.

## ⏳ Upcoming & expected

- 📋 **`canada-retaliatory-tariffs-effective-0908` (due tomorrow) — no
  change found.** Finance Canada's list of ~874 tariff items, published
  08-25 and effective 00:01 on 09-08, stands; no carve-out, delay or
  settlement surfaced over the weekend.
  ([Canada.ca](https://www.canada.ca/en/department-finance/news/2026/08/list-of-products-from-the-united-states-subject-to-counter-tariffs-effective-september-8-2026.html))
- 📋 **`oracle-q1-fy27-earnings` (09-10) — reconfirmed** at Oracle's own IR
  page: after the close, 4pm CT call. No pre-announcement; standing
  consensus around $19.1bn revenue and $1.73-1.74 non-GAAP EPS, with
  options pricing roughly an 11% move.
- 🆕 **Logged: `iran-hormuz-restricted-zone-boundaries` (due 09-21).**
- ⚠️ **`decart-acquisition-close` — grace expired, stays passed-silent.**
- 📋 **Next dated:** Treasury's first doubled buyback (09-09), US CPI and
  the Nippon Life hearing outcome (09-11), FOMC (09-16).

## 🔄 Map changes

- `✎` **Correction across four digests, one interpretation sidecar and the
  `red-sea-oil-shock` timeline:** Brent's 09-04 settlement `$92.68 →
  $96.28`, with the two notes that had defended the wrong figure inverted
  in place and marked (curate-add 09-07).
- `✎` **Correction, 2026-09-06 global-capital and front:** "markets closed
  until Tuesday" narrowed to US cash equities and bonds; oil reopened at
  18:00 ET Sunday, inside that digest-day (curate-add 09-07).
- `+` `upcoming.yaml`: `iran-hormuz-restricted-zone-boundaries`
  (curate-add 09-07).
- 📋 **Proposed, not applied:** add `restricted zone` / `exclusion zone` to
  `red-sea-oil-shock`'s terms — Iran's own phrase for a mechanism the
  thread does not yet name. Held for `/steer`.

## 🧵 Thread candidates

- **A Saudi energy-infrastructure thread** *(curator-noticed; first offer,
  shared with the world-news digest)* — Jizan struck three times in three
  months and Yanbu once, routed across three threads with none owning the
  target set. Terms: `Jizan refinery`, `Yanbu`, `Aramco facility`,
  `Ras Tanura`, `East-West pipeline`. **Track it?**

## 🚨 Flash

**None.**

## ⚠️ Collection note

⛔ **No collectors ran this session.** `cloud-researcher` is not installed
on this machine, so `sec_edgar`, `epfr_flows`, `gdelt`, `rss`,
`google_news_rss`, `openalex` and `federal_register` all did not run and
`buffer/` does not exist. No provenance manifests were produced.

🔴 **Four of the sweep's proposed macro figures were wrong and were
discarded in the main session.** The sweep reported the Shanghai Composite
at 4,575.02 (actual 3,932.70), the FTSE 100 at 14,666 (actual 10,822.13),
gold "~$4,400, bearish tone" (actual $4,476.60, **up** 1.06%), and USD/JPY
"above 156.00, dollar firm" (actual 154.34, dollar **softer**). It also
computed the day's oil move off this map's own transposed $92.68 baseline
and reported "+4.6%" where the true change from $96.28 was about +1.5%.
Its Nikkei and Hang Seng figures were right. **The pattern to take from
this: a sweep agent's index levels are not usable without re-derivation,**
and on a lens whose credibility is numbers, the strip has to be pulled in
the main session against a timestamped instrument — which is what was done
above.

⚠️ **Nineteen threads on this lens were not checked** — `treasury-long-end-intervention`,
`chip-hyperscaler-rotation`, `nvidia-vendor-financing`, `coreweave-backlog-bet`,
`softbank-all-in`, `pif-ai-buildout`, `cxmt-memory-ipo`, `ping-an-insurtech-ai`,
`allianz-ai-claims-automation`, `openai-ipo-timing`, `anthropic-ipo-timing`,
`spacexai-public-megacap`, `fidelity-buys-ai-labs`, `asset-managers-build-ai`,
`berkshire-ai-capital-stance`, `datacenter-backlash-capital-risk`,
`ai-trade-bear-turn`, `ai-circular-financing-risk`, `ai-buildout-debt-risk`.
The sweep's hard stop hit while the oil story was still being worked. On a
US holiday with no session and no filings the expected yield is low, but
**this is an unchecked window, not a clean one**, and it is recorded as such.

---

## Appendix — Coverage check vs. benchmarks

*Run 2026-09-08 at finalize. Full pass in `coverage-log.md`.*

**Benchmark status.** Money Stuff **dark** (author RSS latest item 09-03).
Axios Pro Rata **dark**, confirmed by its own words — the 09-04 edition
reads "cleaning out the notebook as we head into the long weekend."
FT Unhedged **published** ("Everything is awesome," on US stock strength)
but paywalled past the subhead and off the day's story. Bloomberg
Technology **unauditable** — a rolling homepage with no dated archive, the
same structural limitation logged on the prior pass and still unfixed.
**All four named benchmarks contributed zero usable leads**, the fourth
consecutive pass on which that has happened for a weekend or holiday.

**They led with → we missed:** nothing from the benchmarks.

> **The price strip is clean — every figure verified, and the Brent fix
> held.** Brent, WTI, all six equity indices, gold's Friday base, USD/JPY,
> EUR/USD and both Treasury yields were re-derived independently against
> Yahoo's own settlement series, the US Treasury's official daily par-yield
> curve, and CNBC's own text for the two oil prints. After a transposed
> Brent settle survived four days and was defended against correct
> evidence, this matters more than a clean audit normally would.

Two immaterial notes on that audit: the FTSE level prints 10,822.13 here
against Yahoo's 10,822.10, a three-hundredths-of-a-point closing-auction
difference, and **gold's Monday level ($4,476.60) could not be confirmed
against an independent source** — Yahoo has no bar at any granularity for
`GC=F` across the whole Labor Day session, so the Friday base is verified
exactly and the Monday print is internally consistent but unconfirmed.

**The real find came from the name-search pass, not the benchmarks:**
SoftBank's 11.2% Monday move, merged above as a late catch. It sat on one
of the nineteen threads this digest itself disclosed as unchecked — which
is the argument for keeping that disclosure honest rather than quiet.

**A false positive worth recording so it is not "found" again:** a
BlackRock/Larry Fink "$150 oil means global recession" story carried a
09-07 16:11 ET aggregator timestamp and looked like a strong miss. Its
real publish date, cross-checked across five outlets' indexed copies, is
**2026-03-25**. Aggregator re-serves are not new news; this is the fifth
instance logged.

**We had → they didn't:** the Rezaei escalation quote, the Goldman $120
scenario, and the whole Gulf risk-premium framing.

**⚠️ Access state, re-checked:** Reuters blocked both directly (401) and
through `r.jina.ai` (403, worse than previously logged). AP's reader-proxy
route now returns 200 where it did not before. Neither change is yet
pinned into `sources/benchmarks.yaml`; carried forward for a second pass.
