---
lens: global-capital
date: 2026-08-09
status: final
window_start: 2026-08-09T05:00:00-04:00
as_of: 2026-08-11T07:40:00-04:00
coverage: done
---

# Global Capital — 2026-08-09

*Curated from `buffer/2026-08-09-*.jsonl`'s catch-up sweep, then a full
~23h backlog sweep completing the day (agentic-interim; collect.py 18/18,
`--since 2026-08-09T10:15:00Z`; sources: Google News RSS, sec_edgar
(returned 0 — EDGAR's own API 500'd all day, a real external outage, not
a pipeline bug), rss, federal_register). Most of the 805-item deduped
buffer was recirculation of stories already logged 08-04 through 08-08
(Nvidia-SpaceX, the $750B "circular financing" story, Intel-Fortinet,
SpaceX's lock-up expiry) — dropped after verification. Day now complete;
still `building` — the coverage critic needs ~5h past the 05:00 ET close,
waiting for the next pass.*

## Today's throughline

**Two real threads moved: a chip-supply-chain story (Apple testing
Chinese CXMT memory despite an unresolved pricing standoff, against
Beijing's explicit pivot to capital markets to fund AI champions) and a
sentiment crack in the Berkshire succession story (Michael Burry
publicly breaking with it).** The Red Sea/Hormuz situation — the only
item in the morning's thin first pass — kept generating headlines all
day but nothing materially new happened to it beyond a firmer oil price;
the IRGC's six conditions and the second Jazan strike stand as reported
this morning. Nothing today clears the flash-rail bar.

---

## Capital in my markets

- **Yemen's Houthis confirmed the drone strike on Saudi Aramco's Jazan refinery that started a fire overnight — the same facility hit in a nearly identical attack two weeks ago (07-25/27), now the second confirmed hit on this specific refinery inside the standing war.** Saudi Arabia's Ministry of Energy said industrial firefighting teams extinguished the blaze with no injuries; the Houthi military spokesman said the strike was "precise" and framed it as retaliation for Saudi incursions into Yemen's Saada/Hajjah airspace. Context worth holding alongside this: Aramco's own Q2 2026 earnings (released 08-04, outside this window) showed profit +33% YoY to $33.4B, driven by a realized crude price of $108.1/bbl (+62% YoY) — Aramco is a direct financial beneficiary of the same war now repeatedly hitting its own refining assets.
  ([NPR](https://www.npr.org/2026/08/09/nx-s1-5926387/yemens-houthis-claim-attack-on-aramco-oil-facility-in-saudi-arabia-and-other-middle-east-news), [CNBC](https://www.cnbc.com/2026/08/04/saudi-aramco-earnings-2q-oil-iran-war.html))
  <!-- k: t=red-sea-oil-shock axis=capital-in-my-markets -->

- **Iran's Revolutionary Guard hardened its Hormuz stance overnight, explicitly separating the reopening question from the Oman negotiations and listing six conditions the US would have to meet first — a genuine risk signal for the pending `iran-oman-hormuz-deal-signing` expectation (due ~08-12).** The six conditions: an end to threats against Iran, a permanent halt to military action against Iran and its regional allies, withdrawal of the US naval/air blockade force, war-damage compensation, sanctions removal, and release of frozen Iranian assets abroad. The IRGC's own framing: the strait is "a theatre of war... not just a waterway" until all conditions are met. Iran's Foreign Minister separately said Oman talks were "nearing their final stages" — meaning two different Iranian power centers are sending different signals about whether a deal is close or the reopening question is closed entirely.
  ([Punch](https://punchng.com/iran-wont-reopen-hormuz-until-us-meets-all-conditions-revolutionary-guards/), [Gulf News](https://gulfnews.com/world/iran-sets-new-conditions-for-hormuz-reopening-1.500635088))
  <!-- k: t=red-sea-oil-shock axis=capital-in-my-markets -->

- **Michael Burry publicly broke with Berkshire Hathaway, saying he no
  longer finds it "an attractive investment going forward" and reading
  new CEO Greg Abel's early cash deployment as "more framing moves than
  investment moves."** This is the first public negative read on a story
  this digest had been carrying positively — Abel's Q2 print (net stock
  buyer for the first time in 14 quarters, a $10B Alphabet stake add,
  $4.5B+ in buybacks) had been read as Berkshire finally deploying its
  ~$365-400B cash pile. Burry doesn't dispute the facts; he disputes what
  they mean, framing Abel as lacking Buffett's "patience for the fat
  pitch."
  ([Stocktwits](https://stocktwits.com/news-articles/markets/equity/post-buffett-berkshire-hathaway-can-t-keep-up-with-s-and-p-500-michael-burry-says-it-s-lost-its-attractive-tag/cZojiQnRJar))
  <!-- k: t=berkshire-ai-capital-stance e=berkshire-hathaway axis=capital-in-my-markets interp=yes -->

## Deals & filings

- **Apple is testing memory chips from China's CXMT for iPhones and
  MacBooks, days after CXMT rejected Apple's price-cut demands.** The
  talks are early-stage, scoped to China-market devices, driven by the
  AI boom's DRAM squeeze — CXMT can hold firm on price because Huawei
  and Xiaomi have already locked up its output at similarly high levels,
  flipping the usual buyer-leverage dynamic. HP and Acer already ship
  CXMT chips in non-US markets. Separately, CXMT was fast-tracked into
  the MSCI China All Shares Index effective today via a mega-IPO
  exemption, five weeks after a Shanghai debut that made it mainland
  China's most valuable stock.
  ([Reuters via Yahoo Finance](https://finance.yahoo.com/technology/articles/apple-tests-chinas-cxmt-memory-120655649.html), [SCMP](https://www.scmp.com/business/china-business/article/3363490/how-china-dram-champion-cxmts-msci-entry-could-lure-fund-inflows-cement-its-top-ranking))
  <!-- k: t=cxmt-memory-ipo,ai-memory-shortage e=cxmt,apple axis=deals-and-filings interp=yes -->

- **Beijing is explicitly using its $28 trillion combined stock-and-bond
  market as an AI industrial-policy tool — a break from its traditional
  subsidy/state-investment playbook, with CXMT's Shanghai debut as the
  marquee proof point.** Chinese tech firms have raised ~$217B via
  IPOs/bonds over two years, versus more than 6x that per dollar raised
  by US peers — the move opens access to China's $26T household-savings
  pool to narrow that gap.
  ([Bloomberg Law syndication](https://news.bloomberglaw.com/daily-labor-report/china-taps-28-trillion-capital-markets-to-challenge-us-in-ai))
  <!-- k: t=cxmt-memory-ipo axis=deals-and-filings interp=yes -->

## Power & lobbying

- **The Trump-vs-Cook Fed removal fight is starting to get a market price
  rather than just political commentary — analyst/prediction-market reads
  now put real odds (roughly 13-31%, varying by source and horizon) on
  Trump succeeding in removing Governor Lisa Cook before year-end.** The
  underlying action (the White House's letter via Deputy Chief of Staff
  Dan Scavino, giving Cook three weeks to respond to the same
  mortgage-fraud allegations) isn't new — it's the 08-07 revival
  `capital-context.yaml` already logged. What's new is the quantified
  market read on it.
  ([Semafor](https://www.semafor.com/article/08/10/2026/trump-takes-his-second-swing-at-feds-cook))
  <!-- k: t=fed-independence-fight e=kevin-warsh,lisa-cook axis=power-and-lobbying interp=yes -->

## 📊 Macro strip

- **Brent crude: confirmed ~$84.20/bbl, up modestly** — replaces the
  morning's directional-only note with an actual verified price; still
  Hormuz-tension-driven, no new incident behind the move.
- **30-year Treasury yield: ~5.20%** (TLT ETF data via Invezz) —
  essentially flat vs. `capital-context.yaml`'s 08-06 FRED read of 5.24%.
- **US public debt nearing $40 trillion** (Invezz, 08-09) — a fresh
  figure worth flagging outside the standing FRED-series pulls.
- **10Y-2Y spread: 0.44** (FRED, 2026-08-06 — no newer read surfaced;
  FRED/BoC collectors returned zero new items this run, normal cadence).

## ⏳ Upcoming & expected

- No entries due today for this lens.
- ⚠️ **`iran-oman-hormuz-deal-signing` (due ~08-12) — risk flag carried
  forward unchanged.** The IRGC's six conditions vs. the Foreign
  Minister's "final stages" contradiction stand exactly as reported this
  morning; no new movement toward or away from signing found in this
  window.
- `coreweave-q2-earnings` (08-11, 5pm ET) — swept clean, no pre-earnings
  signal either direction.
- `berkshire-q2-2026-13f` (08-14) — Q2 substance already broke 08-08
  (pre-answered); today's wrinkle is Burry's public negative read above,
  which the actual 13F line-items will make independently checkable.
- New candidates from today's sweep: `apple-cxmt-senate-deadline` 08-21
  (shared with the ai lens) · CXMT's next domestic-index inclusion step
  (STAR 50, ~December 2026, minor/mechanical).

## 🔄 Map changes

- `~ threads/red-sea-oil-shock` — real development (second Jazan
  refinery hit, IRGC hardening); timeline entry written.
- `~ threads/cxmt-memory-ipo` — real development (Apple/CXMT testing +
  MSCI fast-track); timeline entry written.
- `~ threads/berkshire-ai-capital-stance` — real development (Burry's
  public break); timeline entry written.
- `~ threads/fed-independence-fight` — light update (the market-pricing
  angle is new; the underlying action is not).

## 🧵 Thread candidates

- **candidate:** China's explicit capital-markets-as-AI-industrial-policy
  pivot (the $28T Bloomberg framing) — arguably bigger than the CXMT
  story it rode in on. Folded into `cxmt-memory-ipo` for now rather than
  split into its own thread; flagging in case Ben wants it broken out.
- Yesterday's `Fed independence fight` candidate (08-07 digest) was
  promoted to a live thread by Ben's 08-09 ruling — resolved, not
  carried forward as a candidate anymore.

---
The Red Sea conflict was the only story moving this morning; the rest of
the day brought two real developments instead — Apple quietly testing
Chinese memory chips despite Beijing's broader capital-markets-for-AI
push, and Michael Burry publicly souring on post-Buffett Berkshire —
plus a market now pricing real odds on the Fed's Cook fight. Everything
else in the day's buffer, including the Nvidia-SpaceX deal and the
SpaceX lock-up rally, checked out as older news re-syndicating.

## Appendix — Coverage check vs. benchmarks

**They led with → we missed:** Nvidia's $500B+ AI-compute financing
platforms with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs
and KKR — **1 real miss**, event-dated 2026-08-10 (just past this day's
05:00 ET cutoff), written up in the 08-10 digest instead. No other real
miss found against this day's own window.

**Benchmarks checked:**
- **Money Stuff** (Matt Levine, Bloomberg) — accessible via search; its
  08-10 column ("The Situation Is Fine") was retrospective on the
  07-30/31 Situational Awareness fund collapse, not new to this window.
- **Axios Pro Rata** — Cloudflare-blocked to direct fetch, as documented
  on prior passes.
- **FT Unhedged** — public RSS worked; its 08-10 edition led on the
  BoJ/jobs report, nothing AI-capital-specific for this lens.
- **Bloomberg Technology** — 403 on direct fetch, worked via search; no
  AI-capital miss surfaced beyond the Nvidia platform already logged
  above.