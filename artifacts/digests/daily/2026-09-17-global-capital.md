---
lens: global-capital
date: 2026-09-17
status: final
window_start: 2026-09-17T05:00:00-04:00
as_of: 2026-09-18T10:00:00-04:00
coverage: done
---

# Global Capital — 2026-09-17

*Curated agentic-interim, 05:00 ET 09-17 → 05:00 ET 09-18 (full
digest-day), in two passes (05:00-15:00 same-day, then a
close/overnight extension covering the US close, CoreWeave's final
pricing, and the Bank of Japan's decision, which landed inside this
digest-day's own window). Collector pipeline not installed in this
environment; this pass rests on WebSearch/WebFetch against
`attention/watchlist.yaml`, open threads, SEC EDGAR primary filings,
SoftBank's own IR bond page (checked directly via `python3 urllib`),
and `attention/capital-context.yaml` (asof 2026-08-25, read for
grounding on the rate-regime and conflict-risk-premium framing, not
treated as current itself). Finalized with the coverage critic against
`sources/benchmarks.yaml`'s `critics.global-capital.daily` list (Money
Stuff, Axios Pro Rata, FT Unhedged, Bloomberg Technology) — see
Appendix.*

## Today's throughline

The oil-driven rebound that started as an attempted morning bounce
became real by the close: the S&P 500 rose 1.12% to 7,637.72, the
Nasdaq Composite rose 1.69% to 26,418.30, and the Dow rose 0.62% to
51,779.85 — chipmakers leading — while the 10-year Treasury yield fell
back below the psychological 5% level it had crossed that morning,
easing 7.6bp on the day to 4.93% and pulling the VIX down more than two
points to 15.4. Brent extended Wednesday-into-Thursday's Saudi-pipeline-
restart selloff, its sharpest single-day drop in this map's recent
record, and kept falling overnight toward $102.57 by Friday morning as
Asian refiners absorb Aramco's rerouted Hormuz-adjacent cargoes. Then,
late in this digest-day's own window — after US markets had closed, and
before the 09-18 digest-day even opens — the Bank of Japan delivered a
second major event: a 25bp hike to 1.25%, its highest policy rate since
1995, on a split 7-2 vote (the two dissents, Toichiro Asada and Ayano
Sato, both reflationists appointed by Prime Minister Takaichi earlier
this year), citing upside inflation risk. The yen weakened and the
10-year JGB eased 4.9bp to 2.947% — the cross-border leg
`capital-context.yaml` has twice flagged as thin, now with an actual
decision and size attached rather than firming odds. On the financing
side, CoreWeave's convertible-note raise announced this morning grew
rather than shrank by the close: upsized from $3.0bn to $3.7bn at a
2.875% coupon due April 2033, alongside a new at-the-market equity
program for up to 35 million shares — the stock closed down 4.16% at
$79.88, a smaller decline than the morning's -5.69% print but still a
sell-off on a raise explicitly framed around investment-grade credit.
And a second SoftBank financing story broke alongside the first:
Bloomberg reported Apollo is negotiating to nearly double its Vision
Fund 2 NAV loan from $5.4bn to $9bn to keep funding the OpenAI
commitment, even as the headline $10-20bn dollar-bond roadshow that
concluded its own scheduled window today produced no pricing anywhere
by the time this digest closed.

## 📊 Macro strip

*vs. yesterday's 2026-09-16 digest (as finalized). Final closes for the
full 09-17 digest-day, plus the BOJ decision that landed inside this
same window after the US close.*

| line | value | vs. last read |
| --- | --- | --- |
| US 10-year Treasury | 4.93%, -7.6bp on the day | closed back below 5% after touching 5.016% this morning — snapped the eight-session rising streak; CNBC ties the pullback to the oil move and a calmer post-Fed read, not Treasury's buyback campaign |
| US 30-year Treasury | 5.28%, -6.6bp on the day | eased in step with the 10-year |
| Brent | $104.82 settle (-1%), after trading as much as 3.6% lower intraday on the Saudi restart plan | fourth straight down session; Friday-morning Asian trading takes it further, to ~$102.57 |
| S&P 500 | 7,637.72, +1.12% | premarket rebound became a real afternoon rally, held into the close |
| Nasdaq Composite | 26,418.30, +1.69% | chipmakers led |
| Dow | 51,779.85, +0.62% | recovers roughly a third of Wednesday's 631-point FOMC-day drop |
| VIX | 15.4, -2.3pts | volatility easing off Wednesday's post-hike spike |
| DAX / FTSE 100 | 25,716.71 (+0.70%) / 10,816.14 (+1.19%) | both closed higher, tracking Wall Street's oil-driven rebound |
| Nikkei 225 | 64,136, +0.33% (Thursday's already-closed session) | BOJ decision landed after Tokyo's close; Friday's reaction is 09-18's story |
| **BOJ policy rate** | **1.25% (+25bp), split 7-2 vote** | first hike since June; highest rate since 1995; yen weakened, 10-year JGB eased 4.9bp to 2.947% |

## Capital in my markets

- **The market follow-through this map flagged to check arrived within a
  day: the 10-year Treasury yield rose above the psychological 5% level
  to 5.016% Thursday, extending Wednesday's post-hike move rather than
  reversing it — the second consecutive day the "fiscal dominance" test
  this map has carried since August has resolved against the
  intervention thesis.** A same-day equity rebound (the Dow up roughly
  250 points intraday per CNBC) is being driven by falling oil and
  yields easing off their highs, not by Treasury's buyback campaign — the
  one clear "good news" morning since the hike is externally driven, not
  evidence the intervention is working.
  ([FXStreet](https://www.fxstreet.com/news/us-10-year-treasury-yield-nears-5-after-fed-rate-hike-middle-east-tensions-raise-inflation-fears-202609170501), [CNBC](https://www.cnbc.com/2026/09/16/stock-market-today-live-updates.html))
  <!-- k: t=treasury-long-end-intervention axis=capital-markets -->
- **Brent traded as much as 3.6% lower, near $102, Thursday before
  settling down about 1% at $104.82, as Saudi Arabia
  announced a concrete partial-restart plan for the East-West pipeline —
  half its 7 million bpd capacity back "within days," full capacity
  within about six weeks — while bypassing the damaged section, and
  separately began routing extra crude to Asian refiners via
  ship-to-ship transfers near Oman's Sohar port, just outside Hormuz.**
  WTI settled down 52 cents at $101.91 (CNBC). The intraday swing is the
  sharpest this map has logged recently, and the move is the first genuine de-escalation signal on the pipeline side of the
  war since the 09-10 drone strike — arriving one day after a Fed hike
  priced partly on oil-driven inflation risk.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-09-16/saudis-seek-to-resume-half-of-key-oil-pipeline-within-days), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-16/oil-extends-slump-as-saudi-arabia-moves-to-restore-key-pipeline), [CNBC](https://www.cnbc.com/2026/09/17/oil-prices-today-wti-brent-hormuz-iran-war.html))
  <!-- k: t=red-sea-oil-shock axis=capital-markets interp=yes -->
- **The morning's attempted rebound became a real afternoon rally that
  held into the close, and it pulled the 10-year Treasury yield back down
  with it: the S&P 500 and Nasdaq both closed up more than 1% (chipmakers
  leading), and the 10-year eased 7.6bp on the day to 4.93%, snapping the
  eight-session rising streak that had carried it above 5% this
  morning.** This is the second consecutive day this map's own "fiscal
  dominance" test has produced a clean read, and both days point the
  same direction: Wednesday's selloff and this pullback both track the
  Fed/oil/inflation-expectations axis, not anything Treasury's
  TGA-funded buyback campaign is doing — a hiking, hawkish Fed drove the
  long end up, and falling oil (not the buyback) is what is now pulling
  it back down.
  ([TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-17-2026), [Investing.com market news](https://www.investing.com/news/stock-market-news))
  <!-- k: t=treasury-long-end-intervention,red-sea-oil-shock axis=capital-markets -->
- **Late in this digest-day's own window — after the US close, and the
  day before its own reported due date — the Bank of Japan hiked its
  policy rate 25bp to 1.25%, the highest since 1995, on a split 7-2 vote,
  citing upside inflation risk.** The two dissents, board members Toichiro
  Asada and Ayano Sato, are both reflationists appointed by Prime
  Minister Sanae Takaichi earlier this year — the first time this map has
  a named split on a BOJ decision rather than just a probability. The yen
  weakened (0.45% to ¥156.64, continuing to soften toward ¥157 in early
  Asian trading) and the 10-year JGB eased 4.9bp to 2.947% — a rate cut
  in the JGB itself even as the policy rate rose, consistent with the
  hike having been fully priced in (Reuters' poll had put odds at 97%).
  This is the cross-border leg `capital-context.yaml` has twice flagged
  as thin and this map's own `cross-border-rates` thread opened
  specifically to track — now with an actual decision, size and
  dissenting-vote detail attached, not just firming odds.
  ([CNBC](https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-18/boj-hikes-rates-at-fastest-pace-since-1990-as-inflation-persists), [Japan Times](https://www.japantimes.co.jp/business/2026/09/18/economy/boj-meeting-september/))
  <!-- k: t=ai-buildout-debt-risk,cross-border-rates axis=capital-markets interp=yes -->

## Deals & filings

- **CoreWeave's convertible-note raise grew rather than shrank between
  this morning's announcement and the close: upsized from $3.0bn to
  $3.7bn, priced at a 2.875% coupon due April 2033, with an initial
  purchasers' option for a further $500M within 13 days — and the stock
  sold off on the news rather than rallying, for a second time this
  thread has logged that reaction.** Terms per CoreWeave's own release:
  conversion price ~$97.85 (a 22.5% premium over Thursday's $79.88
  close), settlement 2026-09-22, net proceeds ~$3.6bn (~$4.1bn if the
  option is exercised), earmarked first for capped-call transactions to
  blunt dilution on conversion and the remainder for general corporate
  purposes. **A second financing move landed alongside it: an equity
  distribution agreement (an at-the-market program) for up to 35 million
  additional shares** — debt and dilutive equity issuance on the same
  day. CRWV closed at $79.88, -4.16% — a smaller decline than the
  morning's -5.69%/$78.61 print, but still a sell-off on a raise
  explicitly framed around reaching investment-grade credit, the second
  time this map has logged the market reading a CoreWeave balance-sheet
  move as a risk signal rather than a confidence builder (see 09-11's
  sympathy rally off Oracle's backlog print, against the same-week
  balance-sheet-concern selloff it reversed).
  ([StockTitan, pricing terms](https://www.stocktitan.net/news/CRWV/core-weave-prices-upsized-3-7-billion-convertible-senior-notes-mehpzqf6tg8n.html), [SEC EDGAR, CoreWeave 8-K/EX-99.1](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000429/ex9911.htm), [Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/09/17/stock-market-today-sept-17-coreweave-falls-on-convertible-debt-and-share-sale-announcement/))
  <!-- k: t=coreweave-backlog-bet axis=deals interp=yes -->
- **A second SoftBank OpenAI-financing story broke the same day as the
  bond roadshow's own close: Apollo Global Management is negotiating to
  nearly double a loan secured against SoftBank's Vision Fund 2 assets,
  from $5.4bn to $9bn, to keep funding SoftBank's $64.6bn OpenAI
  commitment.** This is a net-asset-value (NAV) loan — financing raised
  against a fund's underlying portfolio value rather than a single
  stake — that Apollo first provided in 2021 and already expanded once,
  to $5.4bn, within the past year; the size of any increase is not yet
  finalized and the talks may not result in a revised agreement. Read
  against `softbank-all-in`'s own "everything collateralizes everything
  else" framing: this is a third simultaneous SoftBank financing lever in
  play this week (the still-unpriced $10-20bn dollar-bond roadshow below,
  plus this NAV-loan expansion), each pledging a different slice of the
  same concentrated AI bet.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-09-17/apollo-mulls-raising-softbank-loan-to-9-billion-for-openai-bets), [Japan Times](https://www.japantimes.co.jp/business/2026/09/17/softbank-loan-apollo/))
  <!-- k: t=softbank-all-in axis=deals -->

## ⏳ Upcoming & expected

**One hit, confirmed a day ahead of its own due date; one flip to
passed-silent; one re-check that stays pending. All three reported below
for the main session to apply to `attention/upcoming.yaml`.**

- ✅ **`boj-september-meeting-0918` — HIT, one day ahead of its 09-18 due
  date** (the decision itself landed within this 09-17 digest-day's own
  05:00-05:00 ET window, since Friday-Tokyo-afternoon falls Thursday
  evening ET). The Bank of Japan hiked 25bp to 1.25%, its highest since
  1995, on a split 7-2 vote — board members Toichiro Asada and Ayano
  Sato, both reflationists appointed by PM Takaichi, dissenting — citing
  upside inflation risk. Both halves of `what_confirms` are answered: the
  size (25bp, not a larger move despite Takata's earlier hint one was
  possible) and the JGB/yen reaction (yen weakened 0.45% to ¥156.64,
  10-year JGB eased 4.9bp to 2.947%). Bessent's public pressure on Tokyo
  (NHK, 09-01/02) got the hike it was pushing for.
- ⚠️ **`softbank-openai-bridge-bond-pricing-0917` — passed-silent,
  confirmed on re-check.** The $10-20bn dollar-bond roadshow's own
  scheduled window (Citigroup, New York, 09-14 to 09-17) closed today
  with no coupon, size or launch reported by any outlet checked across
  both this pass and the finalize pass (Bloomberg, Reuters-relay
  coverage, aggregator pickups). SoftBank's own IR bond page, checked
  directly via `python3 urllib`, lists nothing dated later than the
  09-04 ¥1tn retail bond's own terms-and-conditions release (20260904) —
  no new press release for a dollar/euro 144A issue exists on the
  company's own site as of this finalize pass. "Due today" was Reuters'
  own reported timeline (09-10), not an estimate this map made up, so
  the date passing with the roadshow's own window closed and zero
  evidence either way is the loud outcome this status exists for.
- 🚧 **`nvidia-500b-financing-first-close` — stays pending, re-checked.**
  (Thread `nvidia-vendor-financing`, owned by another agent this run —
  researched and reported here per this run's thread-ownership split,
  not written to that thread's timeline.) No named deal converts one of
  the six MOU partners (Apollo, BlackRock, Blackstone, Brookfield,
  Goldman Sachs, KKR) into a signed transaction as of this pass; still
  "subject to execution of final agreements" language, no dollar
  commitment or first project disclosed. `due_precision` is month, with
  12 days of September left — not yet a full month of silence.

## 🔄 Map changes

- `~ artifacts/threads/treasury-long-end-intervention.md` — gained a
  close-of-day 2026-09-17 bullet (final close figures: 10-year 4.93%,
  S&P/Nasdaq/Dow closes) appended to the existing today's-dated block.
- `~ artifacts/threads/red-sea-oil-shock.md` — unchanged from the
  10:00-15:00 pass; Friday-morning oil's further decline toward $102.57
  belongs to 09-18's own digest-day, not backdated here.
- `~ artifacts/threads/coreweave-backlog-bet.md` — 2026-09-17 entry
  extended with final pricing terms ($3.7bn upsized, 2.875% coupon, the
  new ATM equity program, final close price).
- `~ artifacts/threads/softbank-all-in.md` — 2026-09-17 entry extended
  with the Apollo/Vision-Fund-2 NAV-loan-expansion finding (a same-day,
  separate SoftBank financing story from the bond roadshow already
  logged there).
- `~ artifacts/threads/ai-buildout-debt-risk.md` and
  `~ artifacts/threads/cross-border-rates.md` — both rebuilt in place
  (same 2026-09-17 date) with the actual BOJ decision, superseding the
  morning's "odds firmed further" entries now that the event itself has
  happened.
- One new interpretation added this pass: the BOJ hike read against
  `capital-context.yaml`'s `rate_regime`/cross-border framing and this
  map's own 08-19/09-08 JGB-carry-unwind precedents — see sidecar
  `2026-09-17-global-capital.interp.yaml`. The two interpretations from
  the morning pass (oil/pipeline mechanism, CoreWeave credit-repricing
  read) stand unchanged; the CoreWeave one's scenario 2 (the sell-off
  holding rather than reversing) reads stronger now that the raise grew
  rather than shrank and the stock still closed down.
- `attention/threads.yaml` — `last_seen` bump proposed for
  `softbank-all-in`, `coreweave-backlog-bet`, `ai-buildout-debt-risk`,
  `cross-border-rates`, `treasury-long-end-intervention`,
  `red-sea-oil-shock` (all touched this digest-day; applied by main
  session). Open question carried from the morning pass, still not
  resolved: `ai-buildout-debt-risk` and `cross-border-rates` currently
  split ownership of BOJ coverage (per `upcoming.yaml`'s `thread:` field
  vs. `cross-border-rates`'s own "09-18 is the first test" watch line) —
  both now carry a 09-17 BOJ entry; a call for `/week` rather than
  resolved here.
- `attention/upcoming.yaml` — three resolutions proposed above (BOJ hit,
  SoftBank bond passed-silent, Nvidia $500B re-check stays pending).

## 🧵 Thread candidates

**None today.** Every real item lands on an existing thread
(`treasury-long-end-intervention`, `red-sea-oil-shock`,
`coreweave-backlog-bet`, `softbank-all-in`, `ai-buildout-debt-risk`,
`cross-border-rates`) — no new candidate.

---

The oil-driven rebound that started as an attempted morning bounce
became real by the close: the S&P 500 and Nasdaq both closed up more
than 1%, and the 10-year Treasury yield fell back below 5% to 4.93%,
snapping its eight-session rising streak — the second straight day this
map's "fiscal dominance" test resolved the same direction, the Fed/oil
axis moving the long end, not Treasury's buyback campaign. Brent
extended its sharpest single-day drop in this map's recent record as
Saudi Arabia's pipeline-restart plan took hold, and kept falling
overnight. Then, after the US close, the Bank of Japan hiked 25bp to
1.25% on a split 7-2 vote — its highest rate since 1995 — weakening the
yen and easing the JGB, the cross-border leg this map has tracked as
thin finally landing with a real decision attached. CoreWeave's
convertible-note raise grew from $3.0bn to $3.7bn between announcement
and pricing, plus a new share-sale program, and the stock still closed
down more than 4% — a second instance of the market reading fresh
AI-infrastructure debt as a risk signal rather than a vote of
confidence. SoftBank's $10-20bn bond roadshow closed its own scheduled
window with no pricing anywhere, going passed-silent, even as a second,
separate SoftBank financing story broke the same day: Apollo in talks
to nearly double a Vision Fund 2 loan to $9bn to keep funding the OpenAI
bet.

## Appendix — Coverage check vs. benchmarks

**They led with → we missed:** No confirmed miss this pass. All four
`global-capital.daily` benchmarks were checked against what they led
with on 09-17. Money Stuff's 09-17 column ("The Whole Indian Options
Trade Was Too Good") confirmed to exist via author-page RSS
(pubDate Thu 17 Sep 2026 18:46 GMT) with a dek naming "compute futures
manipulation, AI Ebitda add-backs and AI safety stereotypes" as
sub-items, but the article body is fully paywalled past the boilerplate
even through the r.jina.ai reader proxy — no concrete, sourceable fact
could be confirmed behind the dek, so this is logged as checked-not-
confirmed rather than a miss. Background research found a real backdrop
for the "compute futures" line (the CFTC's 08-17/08-19 comment-seeking
on AI-compute-futures contracts, Nodal Exchange's 09-03 launch plan)
but nothing dated 09-17 specifically. FT Unhedged's 09-17 edition
("Getting to know Mr Warsh," pubDate Thu 17 Sep 2026 05:30 GMT) is
commentary on Chair Warsh's reaction-function messaging — a story this
map's own ledger already closed in depth (`jackson-hole-warsh-keynote`,
resolved hit 08-28) — not a fact-level miss. Axios Pro Rata's
reader-proxy transport returned a stale cached page (title "Axios Pro
Rata: Slowdown," dated May 2026) rather than a current edition — not
checkable this pass, a transport failure rather than a clean check.
Bloomberg Technology's homepage likewise returned a stale cache (dated
March 2025) — not checkable, consistent with this benchmark's standing
"no dated archive" problem.
**Both covered:** The BOJ decision, CoreWeave's pricing, the oil/equity
rebound, and the FOMC-hike follow-through all matched general
financial-press coverage.
**We had → they didn't:** The Apollo/SoftBank Vision Fund 2 NAV-loan
expansion talks and the SoftBank dollar-bond roadshow's passed-silent
outcome were this digest's own finds, sourced to Bloomberg/Japan Times
and SoftBank's own IR page respectively rather than any of the four
benchmarks.
