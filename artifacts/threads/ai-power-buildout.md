---
thread: ai-power-buildout
title: "Power Buildout"
lens: ai
entities: [spacex, microsoft, amazon-aws, oracle]
opened: 2026-07-24
---

# Power Buildout — timeline

*Watch:* Where the capex lands in POWER — the real bottleneck. Nuclear-for-AI (SMRs, Oklo/X-Energy), gas turbines (the Colossus permit fights), grid deals, and the energy-justice/permitting battles. Category meta under where-the-capex-lands.

## 2026-08-31 — An executive order restricts foreign-made grid equipment, and names AI load growth as the reason the threat sharpened

- **An executive order signed 2026-08-26 and published in today's Federal Register declares a national emergency over foreign-produced bulk-power system electric equipment, and its scope list is the AI buildout's own shopping list.** Executive Order 14421 invokes the International Emergency Economic Powers Act and the National Emergencies Act to prohibit "any acquisition, importation, transfer, or installation" of such equipment where the Energy Secretary determines it was designed, developed, manufactured or supplied by a "Covered Foreign Entity" and poses an undue risk of sabotage or supply disruption. The equipment defined as in scope includes **generation turbines, large generators, backup generators, substation transformers, grid-connected inverters, battery energy storage systems, high-voltage circuit breakers and industrial control systems** — the exact classes this thread has tracked as the buildout's binding constraint. The order's own recitals give the reason: "The rapid growth of advanced manufacturing, **data centers, artificial intelligence**, and defense production has increased the Nation's dependence on abundant, reliable electricity and magnified the consequences of a successful attack or supply disruption on the bulk-power system." The prohibition bites on transactions initiated after 08-26 and, under Sec. 2(b), the Secretary may also order equipment already installed to be isolated, replaced or removed. ⚠️ **No country or company is named in the order itself** — Sec. 3(b) leaves the designation of Covered Foreign Entities to the implementing rules, which is where the actual scope will be set. ([Federal Register, EO 14421 full text](https://www.federalregister.gov/documents/full_text/text/2026/08/31/2026-17843.txt), [Federal Register document page](https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system), [White House fact sheet](https://www.whitehouse.gov/fact-sheets/2026/08/fact-sheet-president-donald-j-trump-declares-a-national-emergency-to-secure-americas-bulk-power-system/), [Utility Dive, 08-27](https://www.utilitydive.com/news/trump-declares-emergency-moves-to-block-some-foreign-made-equipment-from-g/828959/)) ⟨daily 2026-08-31⟩
- **The order sets two dated deadlines that make it checkable rather than merely declaratory.** Sec. 3(b) requires the Energy Secretary, within **120 days** of 08-26 — by roughly **2026-12-24** — to "publish rules or regulations implementing the authorities delegated to the Secretary by this order," which is where Covered Foreign Entities get designated and licensing procedures get set. Sec. 4(a) requires him, within **180 days** — by roughly **2027-02-22** — to submit recommended revisions to the Federal Acquisition Regulation prioritising US-manufactured energy infrastructure, after which the FAR Council has 90 days to consider proposing them for comment. Utility Dive's 08-27 report frames the 120-day rulemaking as the industry's central open question, quoting the Edison Electric Institute on wanting to "maintain the reliability and affordability of electricity" and an industry representative saying there is "a need for a lot more clarity" about what counts as foreign-designed equipment, particularly software. ([Federal Register, EO 14421 full text](https://www.federalregister.gov/documents/full_text/text/2026/08/31/2026-17843.txt), [Utility Dive](https://www.utilitydive.com/news/trump-declares-emergency-moves-to-block-some-foreign-made-equipment-from-g/828959/)) ⟨daily 2026-08-31⟩

## 2026-08-30 — SpaceX confirms it is building its own turbine-blade foundry to cut gas-turbine lead times for AI power

- **SpaceX confirmed it is building a turbine-blade casting foundry in Bastrop, Texas**, next to its existing Starlink factory, aiming to manufacture the single-crystal, vacuum-cast blades in-house rather than buy from the handful of suppliers who currently master the process — a move Musk said could cut gas-turbine deployment time by "up to 18 months." SpaceX bought roughly 830 acres for the site between March and June 2026. This is the first instance this thread has recorded of a hyperscaler-adjacent buyer trying to vertically integrate around the turbine-supply bottleneck itself, rather than just contracting further back in the existing chain (per this thread's 08-15 pipeline-deal entry). ([TechCrunch](https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/)) ⟨daily 2026-08-30⟩
- **The same article ties the foundry push directly to unresolved pollution complaints at SpaceX's existing Memphis gas-turbine fleet** — the NAACP has repeatedly accused the xAI-linked operation there of running turbines without required permits or pollution controls, and a cited Virginia study estimated eight full-time gas turbines could cause 3.4–6.5 additional premature deaths annually in an affected population of 2.5 million, concentrated in already-marginalized communities. Faster turbine deployment and unresolved permitting/pollution exposure are now the same story. ([TechCrunch](https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/)) ⟨daily 2026-08-30⟩

## 2026-08-28 — Amazon adds ~200MW of Swedish wind

- **Amazon signed four Swedish wind PPAs totalling 199MW** — three against Mirova's "Saena" portfolio of operating farms (Boarp 17.5MW, Dållebo 18MW, Fågelås 31.5MW) and one for 132MW from OX2's 189MW Fageråsen farm in Dalarna County — reportedly taking its contracted Swedish power past 1GW, tied to local data-centre expansion. ⚠️ **UNVERIFIED DATE, secondary source only:** this rests on a trade-press listing; Amazon's own release could not be retrieved to pin the announcement timestamp, and the MW figures and counterparties are that outlet's.
  ([Data Center Dynamics](https://www.datacenterdynamics.com/en/news/amazon-signs-199mw-worth-of-ppas-across-sweden-with-ox2-and-mirova/)) ⟨daily 2026-08-28⟩

## 2026-08-27 — New Jersey makes big data centres report what they burn and drink

- **Governor Mikie Sherrill signed S3379, requiring every data centre over 100MW in New Jersey — new and existing — to file semiannual reports to the Board of Public Utilities for three years**, disclosing total energy consumption, the cooling-versus-IT-equipment split, peak daily water use, water sourcing, and on-site and backup power supply. It follows a July law requiring data centres to bring their own clean energy and creating a separate large-load ratepayer class. **This is a disclosure mandate, not a siting decision, and that is exactly why it matters to this thread** — the energy-justice fights it tracks have been fought without data, and a state regulator is now building the instrument to measure the thing before deciding about it.
  ([New Jersey Monitor](https://newjerseymonitor.com/2026/08/27/data-centers-water-energy-use-law/), [bill text](https://legiscan.com/NJ/bill/S3379/2026)) ⟨daily 2026-08-27⟩

## 2026-08-26 — The Camellia deadline resolves: the campus clears, ratepayer terms attached

- **Georgia Power announced its 3.2 GW Camellia contract with OpenAI "cleared" PSC regulatory review, at 9:00pm ET on 08-26** — the outcome of the 08-25 deadline this thread already logged, where staff had signalled they would object absent changes. The power-economics terms Georgia Power attaches: OpenAI funds 100% of its own infrastructure, commits up to 1,000MW of flexible demand response (load it can be asked to shed at peak), and the contract is framed as delivering ~$950M/year in system-wide ratepayer savings starting 2029 across Georgia Power's large-load portfolio. ⚠️ Whether PSC staff affirmatively signed off or simply let the deadline pass without filing the referral they had signalled is not independently confirmed — flagged for follow-up on `camellia` and `ai-datacenter-sites`. If the demand-response and cost-allocation terms hold as described, this is a rare case in this thread's coverage of a siting fight producing enforceable grid terms rather than just a permit.
  ([Georgia Power, via PR Newswire — primary](http://www.prnewswire.com/news-releases/georgia-powers-contract-with-openai-approved-latest-approval-part-of-portfolio-of-large-load-contracts-delivering-approximately-950-million-in-annual-savings-beginning-in-2029-302861080.html),
  [WTOC](https://www.wtoc.com/2026/08/27/georgia-powers-openai-contract-effingham-county-approved-expected-lower-residential-bills/))
  ⟨daily 2026-08-26⟩

## 2026-08-25 — Regulator deadline on Camellia; a campus that brings its own generation

- **Georgia PSC staff hit their deadline to refer or object to Georgia
  Power's 3.2 GW Project Camellia contract with OpenAI, having signalled
  they would object absent changes.** The Effingham County campus is to
  be delivered in phases 2028-2032. This is the first of this thread's
  siting fights to reach a state utility regulator rather than a county
  zoning board — a materially higher bar.
  ([The Current GA](https://thecurrentga.org/2026/08/25/psc-deadline-arrives-for-georgia-powers-3-2-gigawatt-openai-data-center-contract/))
  ⟨daily 2026-08-25⟩

- **Backers of "Project River" filed rezoning and annexation applications
  for an $11.3bn Bradley County, Tennessee campus pairing a large data
  center with on-site natural-gas and biomass generation.** Public forums
  are set for 09-01 and 09-12 before any vote. The bring-your-own-
  generation pattern routes around the interconnection queue that has
  been the binding constraint at most of this thread's other sites.
  ([Chattanoogan](https://www.chattanoogan.com/2026/8/26/522510/Proponents-Of-Bradley-County-Project.aspx))
  ⟨daily 2026-08-25⟩

- **A Global Energy Monitor analysis found the US now building roughly
  twice as much gas-fired capacity as China, with AI data-center demand
  the stated driver.** US gas capacity under development rose 50% since
  January, from 252GW to 378GW, after a 76% jump in projects under
  construction in the first half of 2026.
  ([Global Energy Monitor, via The Guardian](https://www.chinastrategy.org/2026/08/25/us-building-twice-as-much-gas-fired-capacity-as-china-in-ai-boom-analysis-finds/))
  ⟨daily 2026-08-25⟩

## 2026-08-24 (late catch, added 2026-08-25) — The Lancium equity stake becomes a 15+ GW deployment platform

- **Three days after taking an equity position in Lancium, Nvidia turned
  the whole of that company's powered-land portfolio into a deployment
  platform for its own full AI-factory stack.** Lancium's campuses — 4 GW
  of leased capacity plus a development pipeline exceeding 15 GW of
  powered land — will be built out against Nvidia DSX reference designs,
  including DSX MaxLPS (Nvidia claims up to 40% more GPUs inside the same
  power budget) and DSX Flex (adjusting an AI factory's draw with the
  grid). Lancium is a Blackstone portfolio company; Nvidia's investment
  amount was not disclosed. **The mechanism this thread tracks — power as
  the binding constraint — is being answered by vertical integration
  rather than by new generation:** the same megawatts carry more compute,
  and the developer's pipeline is pre-committed to one vendor's
  architecture before the power exists. Cross-refs `nvidia-order-book`,
  `where-the-capex-lands`, `ai-circular-financing-risk`.
  ([Lancium press release, primary](https://www.prnewswire.com/news-releases/lancium-announces-partnership-with-nvidia-to-advance-gigawatt-scale-ai-factory-development-across-its-15-gw-portfolio-302858393.html),
  [Data Center Knowledge](https://www.datacenterknowledge.com/data-center-construction/lancium-nvidia-partner-on-gigawatt-scale-ai-data-centers))
  ⟨daily 2026-08-24⟩

## 2026-08-21 — Nvidia takes an equity position in a data-center power/land developer

- **Nvidia's minority investment in Cloverleaf Infrastructure puts a chip
  vendor directly into the power-and-siting bottleneck this thread
  tracks.** Cloverleaf's entire business is securing land and power for
  data-center campuses — gigawatt-scale projects already delivered in
  Wisconsin and Georgia, a claimed 10-15 GW pipeline — and Nvidia is now
  an owner of it rather than a customer downstream of it. The financial
  detail is thin by design: outside coverage puts the stake in the
  several-hundred-million range, the joint release gives no figure.
  Tracked as a financing move on `nvidia-vendor-financing`; noted here
  because the constraint it is buying into is power, not silicon.
  ([Cloverleaf/Nvidia joint release](https://www.prnewswire.com/news-releases/cloverleaf-infrastructure-forms-strategic-partnership-with-nvidia-to-accelerate-data-center-infrastructure-development-302857329.html))
  ⟨daily 2026-08-21⟩

## 2026-08-17 — FERC's 60-day large-load interconnection deadline landed; outcome unconfirmed

- ⚠️ **FERC's June 18 show-cause orders to six grid operators (PJM, MISO, SPP, CAISO, ISO-NE, NYISO) — declaring large-load (>50MW) interconnection tariffs "presumptively unjust" — carried a 60-day deadline to justify existing rules or file reform proposals, landing 2026-08-17.** Multiple law-firm trackers confirm the deadline; what any operator actually filed by/at it is UNCONFIRMED — needs a follow-up check against FERC's own docket. ([FERC](https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration), [Akin Gump](https://www.akingump.com/en/insights/blogs/speaking-energy/ferc-issues-landmark-show-cause-orders-on-large-load-interconnection)) ⟨daily 2026-08-18⟩

## 2026-08-17 — The Ohio site's power bill: at least 10 GW of new generation, $4.2B into the grid

- **The signed PORTS-Pike Technology Campus deal (Nvidia/OpenAI/SB
  Energy, Pike County, Ohio) commits SB Energy and SoftBank to build
  at least 10 GW of new power generation — yielding 8 IT-GW of
  AI-factory capacity — and to invest at least $4.2B in regional grid
  infrastructure through a partnership with AEP Ohio**, explicitly
  framed as protecting ratepayers. Nvidia is also putting $1.5B
  directly into SB Energy itself (correcting weekend reports of "up
  to $3B," which described pre-announcement talks), and OpenAI is
  adding an incremental $40M to SB Energy's existing $40M
  community-benefits fund.
  ([NVIDIA](https://nvidianews.nvidia.com/news/nvidia-guarantees-sb-energy-s-ports-pike-technology-campus-in-ohio-to-exclusively-host-nvidia-ai-compute), [OpenAI](https://openai.com/index/openai-joins-ports-pike-project)) ⟨daily 2026-08-17⟩
- 💡 **The generation-plus-grid-plus-community package arriving
  bundled into one site's announcement** is the same buildout pattern
  this thread has watched assemble piecemeal elsewhere — ONEOK's gas
  supply deal (08-15), PJM's self-supply-or-curtail rule (08-05) — now
  packaged as a single project's stated terms rather than separate
  filings. ⟨daily 2026-08-17⟩

## 2026-08-15 — A pipeline company becomes a named gas supplier for a data-center power plant

- **ONEOK signed an agreement to supply natural gas to a dedicated
  1GW power plant built to serve AI data-center demand** — a ~$100M
  pipeline-infrastructure buildout for ONEOK, disclosed alongside its
  Q2 2026 print (full-year net income guidance raised to ~$3.6B
  midpoint); COO Sheridan Swords said ONEOK is "in late stages of
  discussions with a couple of other opportunities to supply AI data
  centers." First named instance of a midstream gas-pipeline company
  (as opposed to a generator or turbine maker) contracting directly
  against AI data-center power demand — the gas-turbine side of this
  thread's buildout getting a supply-chain layer one step further back
  than the plants themselves.
  ([Motley Fool](https://www.fool.com/investing/2026/08/14/this-boring-pipeline-stock-just-signed-a-deal-to-p/)) ⟨daily 2026-08-15⟩

## 2026-08-07 — Nvidia buys into the power layer directly

- **Nvidia will invest up to $3B in Lancium, the Blackstone-backed power
  developer behind Stargate's Abilene, Texas campus** — $2B initial for a
  ~20% stake, up to $1B more on grid-hookup milestones, valuing Lancium
  (land + power interconnects) at roughly $10B; Lancium is weighing a
  2027 IPO. First time Nvidia has taken a direct stake in a power
  developer rather than a data-center operator or a lab — extends the
  "compute landlord" pattern one layer further down. Cross-refs
  `ai-circular-financing-risk`, `nvidia-order-book`.
  ([The Information](https://www.theinformation.com/articles/nvidia-invest-3-billion-blackstone-backed-power-firm-behind-stargate)) ⟨daily 2026-08-07⟩

## 2026-08-05 — PJM's mirror to the Texas freeze: bring your own power, or the states cut you off

- **PJM (the 13-state mid-Atlantic grid operator — separate from Texas's
  ERCOT) rolled out an "Interim Resource Adequacy Service": data centers
  of 50MW+ must line up their own power (bilateral deals with generators,
  storage, demand-response) or face curtailment starting June 2027**,
  with enforcement pushed onto individual states since PJM itself can't
  mandate curtailment. Driven by capacity-auction costs hitting $16.4B in
  June and 30-34GW of new data-center demand forecast by the early 2030s.
  Full detail on the `datacenter-power-grid` child thread.
  ([Canary Media](https://www.canarymedia.com/articles/data-centers/pjm-data-center-plan)) ⟨daily 2026-08-05⟩
- 💡 Same instinct as the Texas PUCT/ERCOT freeze below, independently
  arrived at by a different grid operator in the same week — the buildout
  is now hitting a self-supply-or-get-cut-off wall on two separate US
  grids at once. ⟨daily 2026-08-05⟩

## 2026-08-04 — Datacenter operators tap banks for billions to unlock grid connections

- **Letters-of-credit deals (~$10B currently in discussion)** meant to
  reassure utilities that ratepayers won't be left holding
  infrastructure costs if an AI-datacenter project fails — real
  financing stress underneath the buildout, and a direct echo of the
  Texas PUCT/ERCOT freeze below.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-04/ai-power-demands-spur-builders-to-seek-billions-in-bank-pledges)) ⟨daily 2026-08-04⟩

## 2026-08-03 — Texas freezes new AI-datacenter grid connections pending an audit (caught 08-04, missed on the day)

- **Governor Abbott ordered the Public Utility Commission of Texas and
  ERCOT to audit every data centre seeking a grid connection before it can
  energise** — covering tax incentives, power consumption, water use,
  community-impact mitigation and ownership — with the directive that "any
  project that fails to comply... must be denied connection to the Texas
  grid."
  ([Texas Tribune](https://www.texastribune.org/2026/08/03/texas-data-center-project-audit-greg-abbott/)) ⟨daily 2026-08-03⟩
- **ERCOT paused its "Batch Zero" transmission planning study in response**
  — the first cohort already moving through its revised approval process,
  now halted mid-review. ⟨daily 2026-08-03⟩
- **The queue this lands on: 1,800+ projects requesting 474+ GW, ~90% of it
  data centres — more than five times the grid's all-time peak-demand
  record**, against 335 operating and 248 planned facilities statewide.
  ⟨daily 2026-08-03⟩
- 💡 **Why this thread should treat it as a step-change, not another
  permitting fight:** every prior entry here tracked power being *procured*
  — nuclear PPAs, gas turbines, DOE site conversions. This is the first
  time the *interconnection itself* has been withheld as policy, by the
  state hosting the largest share of the queue. The binding constraint
  moved from generation to permission. ⟨daily 2026-08-03⟩
- ⚠️ **Process note, kept deliberately:** this published 08-03 13:12 CT and
  **12 items on it sat in that day's own collector buffer routed to no
  thread**. Curation missed it; the overnight extension pass caught it. A
  detection failure, not a sourcing one. ⟨daily 2026-08-03⟩

## 2026-07-30 — Catch-up: a second Cold War DOE site becomes a $100B AI power build (event 07-28/29, missed at the time)

- **NextEra and Brookfield will develop a $100B AI data-center campus at
  DOE's Paducah, KY site** — a former Cold War uranium-enrichment plant —
  paired with 4.6GW of dedicated power generation. Announced via DOE's
  own release 07-29, corroborated same-day by Reuters/WSJ/FT/Bloomberg;
  this thread's most recent entry (07-27 crawl) doesn't have it.
  ([POWER Magazine]) ⟨daily 2026-07-30⟩
- **No hyperscaler/lab tenant named** — unlike Stargate/Portsmouth
  (OpenAI), every account frames this as a NextEra/Brookfield-led
  speculative build. Open gap. ⟨daily 2026-07-30⟩
- 💡 **Worth the curator's own eyes:** this is a *second* former-DOE-
  nuclear-site-to-AI-campus conversion inside one week (after
  Portsmouth/Piketon, 10GW/OpenAI, flagged 07-28) — a possible pattern,
  not tagged `sev=` per the rarity discipline but flagged plainly.
  ⟨daily 2026-07-30⟩

## 2026-07-27 — The power book, four actors ⟨crawl 2026-07-27⟩

- **Google:** solar-dominant (TotalEnergies 1GW/28TWh · Clearway 1.17GW) +
  TVA/Kairos — the first US Gen-IV utility PPA (2030).
- **Microsoft:** TMI/Crane restart tracking 2027 (DOE $1B loan, NRC/FERC
  cleared) · Chevron Kilby $7B/2.7GW/20yr · ~40GW renewables claimed
  (secondary, unreconciled vs a 34GW figure).
- **Amazon:** Talen/Susquehanna 1.92GW firm 17-yr (~$18B, restructured to
  dodge the FERC kill) · X-Energy SMR option to 5GW-by-2039.
- **Meta — the reversal:** QUIT RE100, pivoting to a 7.5GW GAS buildout
  (07-23/24) even while holding a ≤6.6GW nuclear RFP (Oklo/TerraPower/
  Vistra) + NextEra 2.3GW solar. The clean-power consensus broke first
  at Meta.

## 2026-07-24 — Opened

- **Thread opened** (ben-steer) — meta-thread — groups the child threads below. ⟨steer 2026-07-24⟩

## ← Backstory
