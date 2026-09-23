---
thread: datacenter-power-grid
title: "Grid & Turbines"
lens: ai
entities: [spacex]
opened: 2026-07-24
crawled: 2026-07-24
---

# Grid & Turbines — timeline

*Watch:* The grid is the binding constraint on the buildout (not chips) —
interconnection queues exploding, hyperscalers "bringing their own power"
via behind-the-meter gas at gigawatt scale, a hard equipment ceiling
(turbines sold out to 2030, transformers ~3yr), and the ratepayer +
environmental-justice fights that improvisation generates.

## 2026-09-21 — California joins the unilateral state-regulation pattern this thread tracks — Newsom signs seven data-center utility-cost bills

- **California Gov. Gavin Newsom signed seven bills (09-21) aimed at preventing AI data centers from passing utility costs onto residents — requiring the California Public Utilities Commission to create a new rate classification for data centers, forcing data centers to pay for local power-grid and water-system upgrades, requiring disclosure of estimated water use to local governments, and setting energy/water/fuel-consumption thresholds data centers must meet to qualify for streamlined approval.** "While the Trump administration moves toward deregulation, communities are left to deal with the consequences," Newsom said in the signing statement. This extends the exact pattern this thread already tracks in Virginia's Executive Order 22 (09-18, NDA ban + accountability framework) and Texas's Abbott rules (08-03/08-10) — a third major state acting unilaterally on data-center costs/siting while Congress stays on the sidelines. Caught late — signed 09-21, surfaced in this pass. ([The Verge](https://www.theverge.com/ai-artificial-intelligence/998453/california-ai-data-center-bills)) ⟨daily 2026-09-22⟩

## 2026-09-18 — Virginia's governor bans NDAs for data-center deals and orders faster noise rules, joining New York and Texas in unilateral state action while Congress stays on the sidelines

- **Virginia Gov. Abigail Spanberger signed Executive Order 22, banning executive-branch officials from signing non-disclosure agreements for data-center projects, ordering expedited noise regulations, a review of data centers' backup-generation operations, and creating a state AI task force to study workforce-displacement and privacy risks.** Alongside the order, Spanberger unveiled a "Data Center Accountability Framework" that calls for eliminating "by-right approval" (the kind Loudoun County — the self-described "data center capital of the world," which Virginia already is — used for years to let developers build with no additional local approval), removing some state subsidies, setting environmental guardrails, and protecting residents from the energy-price increases data centers are associated with. Environmental groups broadly praised the move; the Piedmont Environmental Council said it doesn't go far enough. The Verge frames Virginia as the latest in a pattern of unilateral state executive action on data centers with Congress on the sidelines — alongside Texas's Gov. Abbott (already on this thread, his 08-03 grid-connection moratorium and the OpenAI/Meta rules commitments below) and, per the same report, New York's Gov. Hochul (not previously on this thread — check whether her own order belongs here too). California's Gov. Newsom issued a separate AI-safety executive order the same day (logged on `openai-agent-security-incident`, not primarily a grid/siting story). ([The Verge](https://www.theverge.com/policy/997573/virginia-governor-spanberger-data-center-ai-task-force)) ⟨daily 2026-09-18⟩

## 2026-09-11 — Vistra raises $1.5bn to refinance its own preferred stock, not to build new generation, while Oracle issues a 2GW renewable RFP to offset a datacenter campus's emissions

- ⚠️ **Vistra priced $1.5bn of 31- and 40-year-plus junior subordinated notes — $850m at 7.00% due 2057 and $650m at 7.25% due 2057 — but its own use-of-proceeds language earmarks the money to redeem two series of existing preferred stock at their October/December 2026 reset dates, not to fund new generation capacity.** Vistra is one of the largest US independent power generators supplying the grid AI datacenters draw on; the catch matters because a large debt raise from a major generator could easily be read as buildout financing, and per Vistra's own SEC filing, it is balance-sheet refinancing instead. Closing is expected 2026-09-24. ([SEC EDGAR 424B5](https://www.sec.gov/Archives/edgar/data/1692819/000114036126036130/0001140361-26-036130-index.htm)) ⟨daily 2026-09-11⟩
- **Oracle issued an RFP for up to 2GW of new renewable generation (solar, wind, geothermal) in New Mexico, deliverable 2027–2031, to match emissions from its Project Jupiter datacenter campus in Doña Ana County — the same site that has already drawn local backlash over an original natural-gas power plan.** Oracle's revised plan (fuel cells rather than the original gas turbines) is now projected at 10 million tons of CO2/year, down from 14 million tons under the shelved gas plan, traceable to Oracle's own regulatory letter; the RFP is the mechanism for Oracle's stated commitment to 100% carbon-free energy matching by 2031 — a rare instance of a hyperscaler-class buyer naming a specific emissions-offset target with a number attached. ([energytech.com](https://www.energytech.com)) ⟨daily 2026-09-11⟩

## 2026-09-09 — DOE opens formal public comment on the bulk-power-system emergency order, the first concrete step toward its own 120-day rulemaking deadline

- **The Department of Energy's Office of Cybersecurity, Energy Security, and Emergency Response published a Request for Information implementing Executive Order 14421** (the bulk-power-system national-emergency order signed 08-26 and already on this thread), opening an eight-category public comment period on scope definitions, supply-chain risk, mitigation of already-installed foreign equipment, licensing, domestic manufacturing capacity and economic impact. **Written comments are due October 9, 2026, and DOE will hold a public webinar September 16, 2026, 3-4pm ET.** This is the first actual regulatory action under the order's 120-day rulemaking deadline (roughly 2026-12-24) that this thread flagged as the "industry's central open question" — the order itself named no Covered Foreign Entities and this RFI does not either; that designation still awaits the eventual rule. Also relevant to `ai-power-buildout`, which carries the same EO. ([Federal Register RFI, full text](https://www.federalregister.gov/documents/full_text/text/2026/09/09/2026-18370.txt)) ⟨daily 2026-09-10⟩

## 2026-09-08 — DOE closes a $1.9bn loan to bring a nuclear reactor's power back online for a hyperscaler's load

- **The Energy Department closed a loan of up to $1.9 billion to restart NextEra's Duane Arnold nuclear plant in Iowa, with a new NextEra-Google collaboration committing the restored output to AI demand.** This thread has tracked hyperscalers securing power through gas, solar, geothermal and interconnection-queue fights; a closed federal loan restoring existing nuclear capacity is a different mechanism again — restarted baseload capacity backed by public money rather than a developer-financed new-build or a behind-the-meter workaround. A *closed* loan is money committed, not an announced intent. ⚠️ The plant's capacity and restart-target year could not be confirmed from a 2026-dated source and are omitted. (DOE; PR Newswire; NextEra newsroom) ⟨daily 2026-09-08⟩

## 2026-09-03 — Flex buys a power-conversion supplier for $4.4 billion, aimed directly at the equipment ceiling this thread tracks

- **Flex agreed to acquire EPC Power for $4.4 billion, adding EPC's 800-volt data-center power architectures — digital rectifiers and solid-state transformers — plus grid-forming technology for storage and microgrids to Flex's Cloud and Power Infrastructure segment, which Flex plans to spin off as an independent public company in Q1 2027.** The deal is expected to close in Q4 2026, funded through a mix of debt and equity. This lands on exactly the constraint this thread's own watch names — transformers and grid-hardware lead times, reinforced by the 08-26 bulk-power-system emergency order (EO 14421) already logged here — as a supplier-side consolidation rather than a demand-side buildout announcement, the angle most of this thread's entries take. ([Investing.com](https://www.investing.com/news/company-news/flex-to-acquire-epc-power-for-44-billion-93CH-4888700), [SEC 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0000866374/000119312526382492/d108491dex991.htm)) ⟨daily 2026-09-04⟩

## 2026-08-31 — The grid-equipment supply chain becomes an IEEPA matter, with the datacenter buildout named in the order's reasoning

- **The federal government has put the grid's own hardware under emergency trade authority, and the reasoning it gave runs through the datacenter buildout.** Executive Order 14421, signed 08-26 and published in today's Federal Register, declares that foreign supply of bulk-power system electric equipment is "an unusual and extraordinary threat" and cites the growth of data centers and artificial intelligence as what has made the consequences of a supply disruption worse. The order defines the bulk-power system as transmission rated at 69kV and above, explicitly excluding local distribution, so its reach is the transmission-and-generation layer that large loads interconnect into rather than the last mile. **Its practical significance for this thread is a second constraint stacked on an already-constrained market**: the equipment classes it covers — transformers, turbines, inverters, battery storage — are the same ones whose multi-year lead times the buildout has been routing around, and Sec. 2(b) allows conditions to be imposed on equipment already in service, including replacement or removal, subject to a reliability and continuity-of-service check. ⚠️ Nothing is prohibited automatically: every prohibition requires a case-by-case determination by the Energy Secretary, and no such determination has been published yet. ([Federal Register, EO 14421 full text](https://www.federalregister.gov/documents/full_text/text/2026/08/31/2026-17843.txt), [Federal Register document page](https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system)) ⟨daily 2026-08-31⟩

## 2026-08-26 — Camellia's PSC clearance comes with a 1,000MW demand-response commitment

- **Georgia Power announced its 3.2 GW Camellia/OpenAI contract cleared PSC regulatory review at 9:00pm ET on 08-26**, attaching the specific grid-mechanism terms this thread tracks: OpenAI funds all of its own infrastructure, commits up to **1,000MW of flexible demand response** (Georgia Power can curtail the load at peak), and the deal is bundled into a "large-load" portfolio Georgia Power says nets ratepayers ~$950M/year in system savings starting 2029. ⚠️ Whether PSC staff affirmatively approved versus simply let their 08-25 objection-signalled deadline lapse is not independently confirmed in secondary coverage — full resolution-mechanism detail on `camellia`. If accurate, the demand-response commitment is a concrete instance of the "bring your own generation / shed load at peak" bargain this thread has been tracking in the abstract.
  ([Georgia Power, via PR Newswire — primary](http://www.prnewswire.com/news-releases/georgia-powers-contract-with-openai-approved-latest-approval-part-of-portfolio-of-large-load-contracts-delivering-approximately-950-million-in-annual-savings-beginning-in-2029-302861080.html),
  [WTOC](https://www.wtoc.com/2026/08/27/georgia-powers-openai-contract-effingham-county-approved-expected-lower-residential-bills/))
  ⟨daily 2026-08-26⟩

## 2026-08-26 — Amazon withdraws a groundwater bid after Virginia says no

- **Amazon Data Services withdrew its Virginia DEQ application to draw up
  to 6.4 million gallons a year from the Potomac aquifer for the proposed
  Birchwood Tech Campus in King George County**, after a DEQ report warned
  the aquifer could not absorb major new withdrawals and a state senator
  called the request "indefensible." Water is now doing what
  interconnection queues have been doing — a hard physical constraint a
  siting decision has to route around rather than negotiate.
  ([Virginia Mercury](https://virginiamercury.com/2026/08/26/amazon-changes-course-on-water-use-for-king-george-data-center-campus/))
  ⟨daily 2026-08-26⟩

## 2026-08-25 — US gas buildout outpaces China's, on AI load

- **A Global Energy Monitor analysis found the US now building roughly
  twice as much gas-fired capacity as China, with AI data-center demand
  the stated driver.** US gas capacity under development rose 50% since
  January, from 252GW to 378GW, after a 76% jump in projects under
  construction in the first half of 2026.
  ([Global Energy Monitor, via The Guardian](https://www.chinastrategy.org/2026/08/25/us-building-twice-as-much-gas-fired-capacity-as-china-in-ai-boom-analysis-finds/))
  ⟨daily 2026-08-25⟩

## 2026-08-24 — The buildout's demand reaches the electrical supply chain: two power-component acquisitions in one day

- **nVent Electric agreed to buy Maverick Power for $1.75bn, plus up to $550m of earnout tied to 2027-2028 performance.** Maverick (McKinney, Texas; ~900 employees; ~$700m of 2026 revenue) makes electrical power-distribution equipment specifically for data centres. The deal is expected to close in Q4 2026, funded with cash and new debt on a Bank of America bridge. **This is the buildout's demand showing up in the electrical supply chain rather than in chips or in grid capacity** — vendor consolidation one layer below the constraint this thread tracks.
  ([nVent, via GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/24/3349571/0/en/nvent-to-acquire-maverick-power.html)) ⟨daily 2026-08-24⟩
  <!-- Corporate press release, which this map normally trims. Kept because
       the dollar figure and the direct data-centre tie make it a real
       capex datapoint rather than newswire churn. -->
- **Infineon is acquiring C2i Semiconductors, a Bangalore maker of power-management chips for AI data centres**, on undisclosed terms, expected to close in Q3 2026. Smaller and less consequential than the nVent deal; recorded because it is the same lane on the same day — multiphase controllers and smart power stages, the component level of the same power problem.
  ([Infineon](https://www.infineon.com/press-release/2026/infpr202608-129)) ⟨daily 2026-08-24⟩

## 2026-08-10 — OpenAI and Meta commit to Abbott's Texas rules; a scale check on the gas buildout

- **OpenAI and Meta both formally committed to Gov. Greg Abbott's new
  data-center standards.** OpenAI's letter (compute CTO Uday
  Ruddarraju) pledged to pay for its own grid infrastructure, support
  new Texas electricity generation and minimize water use; Meta made a
  parallel commitment. Direct response to Abbott's still-open
  PUCT/ERCOT audit-and-moratorium order (this thread's 08-03 entry) and
  five days after Trump publicly called the pause "a mistake" (08-07
  entry below).
  ([OpenAI](https://openai.com/index/responsible-ai-infrastructure-texas/), [Houston Public Media](https://www.houstonpublicmedia.org/articles/news/energy-environment/2026/08/10/559042/texas-data-centers-trump-abbott-meta-openai/)) ⟨daily 2026-08-10⟩
- **An AFP analysis put a number on the behind-the-meter gas buildout
  this thread has tracked qualitatively since it opened: research firm
  Cleanview counts ~60 planned US data centers totalling 97GW of
  off-grid generation into the early 2030s — roughly Mexico's entire
  installed capacity — with OpenAI and Anthropic alone leasing 10+GW of
  it.** Even conservative assumptions put resulting emissions above
  200M tons of CO2/year (46M+ gasoline cars' worth); new US
  fossil-capacity announcements in H1 2026 alone exceeded any full year
  in the past decade. Cross-refs `ai-power-buildout`, `meta-gas-pivot`.
  ([France24/AFP](https://www.france24.com/en/live-news/20260811-ai-s-hunger-for-power-sparks-us-private-gas-plant-boom)) ⟨daily 2026-08-10⟩

## 2026-08-07 (late catch, added 2026-08-11) — Amazon is behind the single largest instance in the buildout's own aggregate dataset

- **Amazon has confirmed plans to buy power from Pacifico Energy's "GW
  Ranch" gas plant on an ~8,000-acre site it acquired in Pecos County,
  Texas — permitted for up to 7.65GW (35 turbines, 5GW nominal delivered
  output) and up to 33 million tons of CO2/year, which the New York
  Times reports could make it the single largest climate-pollution
  source in the country if built out to its full permit.** Cleanview's
  own satellite-imagery-and-permit tracing broke this 2026-08-07, NYT
  corroborated 2026-08-08 — the same firm and the same underlying
  dataset (60 planned sites, 97GW) this thread's 08-10 entry already
  cites in aggregate, without its largest single instance. Amazon's
  statement: it "believes in paying the full costs of powering our
  operations," and the campus is "powered by new on-site generation
  that won't raise electricity costs for Texas families."
  ([Cleanview](https://newsletter.cleanview.co/p/scoop-amazon-is-behind-one-of-the), [DataCenterDynamics](https://www.datacenterdynamics.com/en/news/amazon-acquires-8000-acre-site-in-pecos-texas-for-natural-gas-powered-behind-the-meter-data-center-report/), [Pacifico Energy](https://www.pacificoenergy.com/post/pacifico-energy-announces-gw-ranch-project-bringing-5-gigawatts-of-reliable-off-grid-power-for-ai-i)) ⟨daily 2026-08-10, added 2026-08-11⟩

## 2026-08-08 — DOJ backs xAI's bid to gut citizen-suit enforcement entirely

- **The Justice Department intervened in the NAACP's Clean Air Act
  citizen suit against xAI's unpermitted Southaven, Mississippi
  turbines, arguing the Constitution lets the President and federal
  agencies decide whether to enforce federal law at all** — not a
  narrow defense of xAI's turbines specifically, but a challenge to the
  citizen-suit provision itself, a cornerstone of environmental
  enforcement for 50+ years. The DOJ separately argues shutting down
  power to the turbines would harm national security because Colossus
  "supports Department of War operations." Escalates this thread's
  already-logged DOJ national-security shield into a precedent fight
  that could outlive this specific case.
  ([Fortune](https://fortune.com/2026/08/08/lazarus-26-years-citizen-suits-musk-xai/), [Earthjustice](https://earthjustice.org/press/2026/trump-administration-attempts-massive-power-grab-in-defense-of-musks-xai)) ⟨daily 2026-08-08⟩

## 2026-08-07 — Trump publicly calls the Texas pause "a mistake"

- **In a Punchbowl News interview, Trump called Texas's new data-center
  construction pause "a mistake... it could be bigger than oil,"**
  responding to Gov. Abbott's 08-03 moratorium on new grid connections
  pending an ERCOT/PUCT power-and-water audit. First time the President
  has weighed in directly on a specific state's data-center permitting
  fight — pulls what had been a state-level grid/water dispute into
  national politics. Same interview, Trump separately said Congress
  wants to regulate AI "out of business" (logged on
  `frontier-model-gov-review-precedent`).
  ([Texas Tribune](https://www.texastribune.org/2026/08/07/donald-trump-texas-data-centers-greg-abbott/)) ⟨daily 2026-08-07⟩

## 2026-08-05 — PJM's answer to the same-week Texas freeze: bring your own power or get cut off

- **PJM (the 13-state PA-to-Illinois grid operator) launched an "Interim
  Resource Adequacy Service"**: large loads (50MW+, i.e. essentially all
  data centers) must be registered, and must either secure their own
  bilateral power contracts (generation, storage, demand-response) or
  face curtailment ahead of other emergency measures once the rule bites
  in June 2027. States/utilities enforce it — PJM itself has no authority
  to curtail a customer directly — and can run their own "reliability
  backstop procurement" auctions to help data centers avoid curtailment.
  Trigger: capacity-auction costs hit $16.4B in the June auction, data
  centers were 38% of that, and PJM projects 30-34GW of new data-center
  demand by the early 2030s.
  ([Canary Media](https://www.canarymedia.com/articles/data-centers/pjm-data-center-plan)) ⟨daily 2026-08-05⟩
- **Filed alongside a separate, more immediate fix: a one-time "backstop"
  capacity auction**, submitted to FERC 2026-07-31, running 2026-09-30 to
  2026-10-21, to plug a 6.8GW shortfall from PJM's last base auction —
  can procure up to $20B in new generation capacity through 2027.
  ([Utility Dive](https://www.utilitydive.com/news/pjm-backstop-capacity-auction-ferc-data-centers/826792/)) ⟨daily 2026-08-05⟩
- 💡 **This thread went quiet 07-25 on the "equipment ceiling + DOJ
  shield" verdict; the story has moved from equipment scarcity to grid
  governance.** PJM is now doing structurally what Texas's PUCT/ERCOT
  freeze did procedurally the same week (see `ai-power-buildout` and
  `where-the-capex-lands`) — pushing the risk of an unbuilt or
  under-powered site back onto the developer instead of the ratepayer.
  ⟨daily 2026-08-05⟩

## 2026-07-24 — Opened + crawled

- **Thread opened** (ben-steer). ⟨steer 2026-07-24⟩
- **Verdict: severe, worsening, multi-dimensional — power is the gating
  factor.** The defining escalation is legal-political: the DOJ now invokes
  national security to keep unpermitted turbines running against a citizen
  Clean Air Act suit — the improvisation has outrun the regulatory system.
  ⚠ WebSearch budget exhausted (fan-out) — flagship + high-value claims
  re-verified via fetch; some figures RSS-only, flagged. ⟨crawl 2026-07-24⟩

## ← Backstory (crawl 2026-07-24 → artifacts/findings/datacenter-power-grid-2026-07-24.md)

## 2026-07 — The equipment ceiling + the ratepayer bill

- **GE Vernova's gas-turbine backlog hit 116 GW, sold out through 2030**
  ($176B total backlog, data-center orders >$5B YTD = 2x all of 2025) —
  even self-supply can't scale fast. Same week, PJM's market monitor:
  **data centers drove 38% of the latest capacity-auction charges (46%
  across four auctions)**; the 2028/29 auction cleared at the $325/MW-day
  price cap; FERC's chair warned PJM faces a "grave legitimacy crisis."
  ([GE Vernova](https://www.gevernova.com)) ⟨crawl 2026-07-24⟩

## 2026-06-16 — The DOJ national-security shield

- **The Trump DOJ moved to dismiss the NAACP Clean Air Act suit on
  national-security grounds** — arguing shutting the 57 unpermitted
  Southaven turbines threatens security because Grok "supports Department
  of War operations" (a DoD official called Grok "paramount national
  security," citing the Iran strikes). Converts an environmental-permitting
  fight into a federal-power question. Cross-refs `spacex-colossus`.
  ([NYT](https://www.nytimes.com/2026/06/16/climate/)) ⟨crawl 2026-07-24⟩

## 2026-04 — Improvising around the grid, at scale

- **Meta's "Hyperion" got ~7 new gas plants fast-tracked in Louisiana**
  (Entergy +$14B capex; a later ratepayer-protection order); **NAACP/SELC/
  Earthjustice sued xAI** over 27 unpermitted methane turbines (~495 MW,
  alleged 1,700+ t/yr NOx) at Southaven — "a de facto power plant without
  an air permit," in a historically Black neighborhood leading TN in asthma.
  ([Earthjustice](https://earthjustice.org)) ⟨crawl 2026-07-24⟩

## 2026-01 — EPA: the turbines ran illegally

- **EPA ruled xAI's Memphis turbines ran illegally** under a bogus
  "temporary" exemption — 35 operated, only 15 permitted. Memphis is really
  two braided sites: Colossus 1 (Boxtown, TN) + Colossus 2 (Southaven, MS).
  ([TechCrunch](https://techcrunch.com/2026/01/16/epa-rules-that-xais-natural-gas-generators-were-illegally-used/)) ⟨crawl 2026-07-24⟩

## Backstory — the queue + the equipment wall

- **ERCOT's large-load queue hit ~438 GW (+~300% YoY)**; large-transformer
  lead times are ~2.5–3yr (vs 4–6 weeks pre-pandemic), Wood Mackenzie
  projected a 30% transformer supply deficit; AEP Ohio's landmark
  data-center tariff (07-2025) is the template other states now copy
  (make data centers pay for their minimum contracted power). ⚠ ERCOT
  438GW + transformer figures RSS/secondary-sourced. ⟨crawl 2026-07-24⟩
