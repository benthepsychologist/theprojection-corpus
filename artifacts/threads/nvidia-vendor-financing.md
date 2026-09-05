---
thread: nvidia-vendor-financing
title: "Nvidia as Lender"
lens: global-capital   # corrected 2026-08-02 — was `money`, stale since the 2026-07-30 rename
entities: [nvidia, openai]
opened: 2026-07-27
---

# Nvidia as lender — timeline

*Watch:* The guarantee's actual structure and figure; rating-agency
treatment; each new customer-equity position.

## 2026-09-04 — Nvidia's own 10-Q puts its total equity-investment portfolio at $99bn, up from $7bn a year ago

- **Nvidia's fiscal Q2 FY2027 10-Q (period ended 2026-07-26, filed 2026-08-26 — the underlying filing predates this run's window, but the aggregated reporting on it is new today) shows non-marketable equity securities of $47.898bn, marketable equity securities of $42.783bn, and $3.3bn in equity-method infrastructure-financing investments, summing to the roughly $99bn total CNBC's synthesis reports — up from about $7bn a year earlier and about $2.2bn two years earlier, a roughly 13-fold increase in twelve months.** CFO Colette Kress is quoted saying investments in frontier AI labs alone have "approached $50 billion," and described the mechanism as a "flywheel" that gives portfolio companies "balance-sheet capacity to procure tens of thousands of GPUs" — the clearest company-side articulation yet of the customer-equity pattern this thread exists to track (Nebius, Naver, Intel, Groq, SB Energy, MediaTek, and now Hugging Face). Nvidia still trails Alphabet and Amazon, both of which report equity investments over $100bn. Filling this thread's own "each new customer-equity position" watch line with the aggregate figure rather than another single deal.
  ([SEC EDGAR 10-Q, primary](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm), [BigGo Finance, synthesizing CNBC](https://finance.biggo.com/news/54d7048e-1f8e-40ff-b5f9-5b9084d0133a)) ⟨daily 2026-09-04⟩

## 2026-09-03 — Nvidia confirms $12.93bn Hugging Face acquisition, its first outright buy of AI infrastructure rather than a stake in a customer

- **Nvidia agreed to acquire Hugging Face outright for $12.93 billion — its largest acquisition ever — and the structure disclosed in Nvidia's own 8-K is a genuinely different move from everything else on this thread.** The filing (SEC EDGAR, accession 0001045810-26-000078, Item 8.01, filed 2026-09-03 for the period 2026-09-02) puts it as "approximately $11.9 billion purchase price payable to Hugging Face stockholders, subject to certain adjustments," plus "an equity-based retention program of up to approximately $1.0 billion for Hugging Face employees joining NVIDIA" — the two instruments summing to the ~$12.93bn figure now being widely reported. Expected close is the first half of 2027, "subject to the satisfaction or waiver of customary closing conditions, including receipt of required regulatory approvals" — no specific regulator is named in the filing, and cash-vs-stock consideration is not specified there either; none of Nvidia's blog post, Hugging Face's public statements, or the press coverage I could reach specify it. It surpasses the ~$7bn Mellanox deal (2019/2020) as Nvidia's largest acquisition, though well below the ~$40bn Arm bid that regulators killed in 2020-2022.
  ([SEC EDGAR 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm), [Nvidia blog](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/), [TechCrunch](https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/)) ⟨daily 2026-09-03⟩
- **This thread has tracked Nvidia buying loyalty from customers that keep operating independently — Nebius's 9.3%, Naver's $1B, Intel's $5B, Groq's ~$20B licensing, SB Energy's $3.0bn, MediaTek's $3.5bn convertible bonds — but Hugging Face is full ownership of a neutral distribution layer Nvidia does not itself operate today, not a stake in a chip buyer.** Both companies moved fast to frame it as decentralizing rather than concentrating power: Nvidia's Justin Boitano (VP, Enterprise Computing) pledged "an open and neutral platform that interoperates with every cloud provider, every hardware company in the world," and Hugging Face CEO Clément Delangue said the deal "will allow the world and AI to be more distributed all over the world, and to avoid too much concentration of power" since "the vast, vast majority of what we do is open-source, open models, open datasets, that are by definition, neutral." Forrester analyst Naveen Chhabra offered the counter-read: Nvidia now gets visibility into which models and frameworks are trending across a platform with over 200,000 hosted company accounts, weeks before that shows up anywhere else, plus a direct read on the chip architectures future models will actually need — a demand-forecasting edge no other chipmaker gets from owning a "neutral" hub. Hugging Face reports ~$150M annualized revenue and hosts 3 million models, 1 million applications and 500,000 datasets across 18M+ developers, against a 2023 private valuation of $4.5bn and a previously-rejected $500M Nvidia offer.
  ([PCMag, via reader proxy](https://www.pcmag.com/news/open-and-neutral-nvidia-says-dont-worry-about-its-hugging-face-acquisition), [TechCrunch](https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/), [Nvidia blog](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)) ⟨daily 2026-09-03⟩

- **Nvidia's $12.93bn acquisition of Hugging Face cannot use the technology-licensing structure that let its Groq and Poolside deals dodge Hart-Scott-Rodino review — a direct-purchase deal this size requires HSR filings with the FTC and DOJ plus a waiting period before it can close, and Nvidia is already the subject of active US and EU antitrust inquiries into how it allocates GPU supply.** Nvidia VP of Enterprise Computing Justin Boitano pre-empted the vertical-foreclosure question — whether a company drawing roughly 92% of revenue from AI data-center hardware gains unfair advantage by owning the platform where developers discover and download models — by calling Hugging Face "almost structurally by definition kind of like a deconcentration platform" that lets proprietary APIs compete on a level field, arguing regulators will see the deal as "overwhelmingly positive." The Register published a sharper counter-argument the same day: Hugging Face has functioned as neutral "AI Switzerland" infrastructure since 2016, and "the temptation to use the platform to advance its hardware and software interests will inevitably prove too great," with Nvidia positioned to subsidize compute through partners and steer developers toward its own hardware by default. Nvidia's failed ~$40bn Arm bid (killed 2020–2022 by the FTC, UK, EU and China) is the case regulators are expected to measure this one against. Corrects nothing already on this thread but fills the antitrust/regulatory gap this run was specifically asked to check.
  ([wccftech](https://wccftech.com/nvidia-insists-its-12-93-billion-acquisition-of-hugging-face-will-escape-antitrust-scrutiny-calling-it-a-deconcentration-platform/), [The Register](https://www.theregister.com/ai-and-ml/2026/09/03/hugging-face-is-too-important-to-fall-into-nvidias-hands/5294363), [The Register, Delangue interview](https://www.theregister.com/ai-and-ml/2026/09/03/hugging-face-ceo-says-planets-aligned-for-nvidia-deal-aims-to-reach-100m-users/5294293)) ⟨daily 2026-09-04⟩
- **Hugging Face CEO Clément Delangue told CNBC his company approached Nvidia's Jensen Huang over the summer, not the other way around — "this summer the planets aligned... and a few weeks later, here we are"** — after concluding Hugging Face and open-source AI generally were "at the turning point" and needed "more resources, more scale, more visibility." He set a target of growing from 18 million to 100 million "AI builders" on the platform, saying Nvidia's backing gives "more chances to get there faster," and repeated the "deconcentration platform" framing as his own argument for why the deal preserves rather than threatens neutrality. Minor color against the acquisition-motive question, not a change to the deal terms already on this thread.
  ([CNBC](https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html)) ⟨daily 2026-09-04⟩

- **Mira Murati's Thinking Machines Lab is in talks to raise roughly $1 billion at a $40 billion valuation, with Accel in discussions to lead the round, according to TechCrunch's own source and The Information's reporting on 09-03** — below the $50 billion the company had reportedly sought earlier in the summer, and a step up from the $12 billion post-money of its $2 billion seed round in 2025, which Andreessen Horowitz led with Nvidia, GV, Lightspeed and Conviction participating. The Information separately reported the same day that Nvidia is discussing investing around $2.5 billion in the company — which, if it lands, would be Nvidia's latest direct equity stake in a model lab in a week that already put its Hugging Face acquisition and a $99 billion investment portfolio on the record. ([TechCrunch](https://techcrunch.com/2026/09/03/accel-reportedly-in-talks-to-lead-1b-round-for-thinking-machines-at-40b-valuation/)) ⟨daily 2026-09-05⟩

## 2026-09-01 — SB Energy, the SoftBank/OpenAI entity behind Nvidia's Ohio guarantee, files for a US IPO with real financials attached

- **SB Energy Corp — the SoftBank- and OpenAI-backed developer of the Ohio "PORTS" campus that Nvidia's up-to-$105bn lease guarantee underwrites — filed for a US IPO, disclosing a $439bn contracted backlog against a $3.21bn net loss on just $138.7m of revenue for the six months ended June 30, 2026** (versus a $215.5m loss on $83.3m revenue a year earlier). Nvidia has separately committed **$3.0bn in total** — a $1.5bn Class N private placement closing concurrently with the IPO, plus a $1.5bn Prepaid Forward Contract funded back on 2026-08-17 (⚠️ **corrected 2026-09-02**; this line originally read "$1.5bn in the IPO itself," which is only the private-placement half — see the S-1 detail below). This is the first time SB Energy's own numbers — not just the guarantee figure this thread has tracked since 08-15 — have been public: a company with no data center yet online carrying a backlog more than 100x its trailing revenue. JPMorgan, Goldman Sachs, Morgan Stanley, Citigroup and Mizuho are leading the offering; the company plans to list on Nasdaq as "SBE."
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-09-01/softbank-backed-sb-energy-files-for-ipo-to-tap-ai-power-thirst)) ⟨daily 2026-09-01⟩

- **Nvidia's total committed investment in SB Energy is $3.0 billion, disclosed in the S-1 as two instruments dated the same day — double the figure Nvidia's own press release described.** The filing (SEC EDGAR, accession 0001628280-26-059639, filed under registrant "SB Energy, Inc.," CIK 0002133037) discloses two same-day instruments dated August 17, 2026: a Prepaid Forward Contract under which Nvidia funded $1.5bn to SB Energy's Energy Global subsidiary that same day (already spent, already on the balance sheet), and a Share Purchase Agreement for a new non-voting Class N common stock, also $1.5bn, closing concurrently with the IPO — "reflecting an investment from NVIDIA of $3.0 billion in total between the Prepaid Forward Contract and the Share Purchase Agreement" in the filing's own words. This map's 08-17 entry, sourced to Nvidia's press release, read the $1.5bn Prepaid Forward Contract as the whole story and explicitly framed it as "correcting weekend reports of 'up to $3B' that described pre-announcement talks rather than final terms" — the weekend reports were closer to right; the press release described only one of two simultaneous instruments. WSJ's own 09-01 headline on the S-1 ("SB Energy Files for IPO With Nvidia Backing") independently states the same $3 billion figure; its full text was not reachable from here, so the filing itself is the source of record.
  ([SEC EDGAR S-1](https://www.sec.gov/Archives/edgar/data/2133037/000162828026059639/sbenergy-sx1.htm)) ⟨daily 2026-09-02⟩
- **The S-1's own risk factors state SB Energy is "substantially dependent on OpenAI as a tenant and strategic partner," and quantify why: OpenAI's PORTS-Pike Technology Campus lease alone accounts for 8.0 of the company's 8.8 GW-IT of signed data-center capacity — about 91% — with the remaining 0.8 GW-IT split between SoftBank's Cosmos campus and OpenAI's own Milam County buildings.** The filing separately discloses OpenAI holds 3,991,809 warrants at a nominal $0.01 exercise price (ten-year term, expiring the later of January 9, 2036 or antitrust clearance — reported by WSJ/Yahoo coverage of the filing at an estimated $5.5bn value) and a board designation right for as long as its stake exceeds 5%. A separate risk factor states plainly that "tenants whose guarantors lack investment-grade credit ratings, including OpenAI" present heightened credit risk — SB Energy's own filing characterizing its largest counterparty's credit as sub-investment-grade. On the backlog itself: of the headline $439bn figure, only about $82bn (19%) is expected to be recognized within the next eight years — $1bn in 24 months, $12bn in 25-48 months, $30bn in 49-72 months, $39bn in 73-96 months — with the remaining $357bn (81%) recognized "thereafter." Total related-party cash outflows to SoftBank and OpenAI (trademark royalty plus a $50m OpenAI software minimum-purchase commitment through 2028) are quantified at $50.1m — trivial next to the backlog, and the filing notes net related-party cash flow is expected to run positive (inflows from leases exceeding these outflows). SoftBank retains voting control and the company will be a Nasdaq "controlled company" post-listing; share count and price range are both blank ("to be filed by amendment"), consistent with a first S-1.
  ([SEC EDGAR S-1](https://www.sec.gov/Archives/edgar/data/2133037/000162828026059639/sbenergy-sx1.htm)) ⟨daily 2026-09-02⟩

## 2026-08-31 — Nvidia buys 90% of a $3.9bn MediaTek convertible-bond offering, its largest direct investment outside the US

- **Nvidia agreed to invest $3.5bn in MediaTek via convertible bonds — roughly 90% of MediaTek's entire $3.9bn overseas convertible-bond offering — deepening a collaboration built around Nvidia's NVLink Fusion platform**, which lets non-Nvidia chips (including MediaTek's custom silicon) plug into Nvidia's rack-scale data-center architecture. The bonds convert into MediaTek shares later rather than functioning as a straight equity buy today, extending the same stake-ladder pattern this thread already tracks (Nebius 9.3%, Naver $1B, Intel $5B, Groq ~$20B licensing) to a chip-design partner rather than a cloud/compute customer. MediaTek shares rose as much as 10% on the news.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-31/nvidia-to-invest-3-5-billion-in-chipmaker-mediatek), [TechCrunch](https://techcrunch.com/2026/08/31/nvidias-3-5b-mediatek-bet-reveals-its-plan-for-tackling-big-techs-ai-chip-buildout/)) ⟨daily 2026-09-01⟩

## 2026-08-29 — The pause gets a number and a mechanism: $36bn, and a customer-approval clause

**Nvidia's own quarterly filing puts the AI Compute Partnership program — the one it stepped back from on 08-28 — at $36 billion of total commitments, structured as take-or-pay/revenue-share agreements with a typical six-year term.** **This is the first dollar figure on the specific program**, distinct from the $105bn OpenAI guarantee and $500bn+ third-party platforms already disclosed in the same 10-Q: if utilization ran at 80% of capacity Nvidia would take a cut of the excess revenue, and if it ran at 20% Nvidia's take-or-pay obligation would require covering the shortfall itself. ⚠️ Reached via pickups of a WSJ story (reporters Anissa Gardizy and Berber Jin, 08-27) rather than the filing text directly re-verified here.
([SEC EDGAR, NVDA 10-Q](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm)) ⟨daily 2026-08-29⟩

**What actually drew the antitrust concern, reported for the first time: Nvidia told some cloud providers they could rent the guaranteed capacity only to Nvidia-approved customers, and said it preferred capacity spread across several smaller AI companies rather than concentrated with one large operator.** **That is customer allocation by a dominant supplier, not a pricing term** — courts treat the former with materially more suspicion, which is the specific legal exposure behind the vague "control" language in the 08-28 entry. Firmus Technologies (170,000-GPU Batam, Indonesia campus, up to $30bn of offtake — the underlying deal itself dates to 06-30 and isn't new) is named alongside SharonAI as an initial program signer now exposed to the pause. ⚠️ Same WSJ-derived sourcing chain as above; no primary Nvidia statement beyond the 08-28 spokesperson quote.
([businessmodelanalyst.com, summarizing WSJ](https://businessmodelanalyst.com/nvidia-ai-compute-partnership-customer-approval/)) ⟨daily 2026-08-29⟩

## 2026-08-28 — Nvidia pulls back from the revenue-share structure, and a customer's deal goes into limbo

**Nvidia stepped back from the AI-cloud revenue-sharing financing programme it launched in July, reportedly after its own employees flagged antitrust exposure and raised concerns about how far it could dictate customers' business operations.** **This is the first evidence on this thread that Nvidia is retreating from the circular structure voluntarily** — a materially different signal from a customer failing, which is what the thread has been braced for. Nvidia's spokesperson did not deny the pause, saying only that "the new business model we introduced in July... is still in place and continues to evolve due to high demand." ⚠️ WSJ-sourced and paywalled; no primary Nvidia statement or filing beyond the secondhand spokesperson quote. ([Yahoo Finance, WSJ-sourced](https://finance.yahoo.com/markets/stocks/articles/nvidia-nvda-pulls-back-financing-153423894.html), [Reuters via Yahoo](https://finance.yahoo.com/news/nvidia-pauses-revenue-sharing-deals-223140237.html)) ⟨daily 2026-08-28⟩

**SharonAI Holdings fell 4.2% to $56.73 with its $4.88bn Nvidia Master Cloud Services Agreement reported in limbo — six years, up to 40,000 Grace Blackwell GB300 GPUs, 72MW of Australian capacity.** **The customer balance sheet is where the pullback becomes visible**, and it is the first named deal this thread can point to as directly contingent on the financing programme continuing. ([TechStock²](https://ts2.tech/en/sharonai-stock-falls-4-2-as-nvidia-financing-pause-tests-4-88-billion-deal/)) ⟨daily 2026-08-28⟩

**Nvidia-backed Lambda raised about $1bn of JPMorgan-arranged private debt for GPUs tied to a Microsoft collaboration, at up to 3.75 points over the benchmark on a 4.4-year maturity against the ~7 years typical for the format.** **The short tenor is the signal, not the size** — lenders declining to take GPU depreciation risk over a normal loan life is the credit market asking the same question this thread asks from the equity side. Distinct from Lambda's separate $926M term loan B that closed 08-12. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-28/nvidia-backed-lambda-inks-1-billion-private-debt-for-chip-deal)) ⟨daily 2026-08-28⟩

## 2026-08-27 — The equity market answers; the credit market has not been asked

- **Nvidia's +8.74% close is the first market data point on the now-filed $105bn guarantee structure, and it did not read as debt-equivalent risk.** **But the thread's actual watch line asks about rating-agency treatment, and that remains unanswered:** the only agency actions on file — **Moody's Aa1 positive and S&P AA stable, both affirmed 2026-08-18** — predate both the 10-Q and this window by nine days. **No rating action, CDS print or other credit-market read has been produced since the guarantees were disclosed.** Recording the absence explicitly, because "the stock went up" is not an answer to "how do the agencies treat it." ⟨daily 2026-08-27⟩

## 2026-08-26 — The guarantees get a number, a cap and a filing date

- **Nvidia's Q2 FY2027 10-Q disclosed guarantees capped at $105 billion tied to
  an affiliate of OpenAI Group PBC for land, power and shell buildout, plus
  $3.5 billion of additional lease guarantees for AI cloud partners and a $25
  billion committed equity-investment pool for AI labs and infrastructure
  financiers.** **This is the first SEC-filed confirmation of the scale of these
  arrangements** — everything this thread has carried until now was reported
  deal value, not audited disclosure with a stated cap.
  ([SEC EDGAR, NVDA 10-Q](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm))
  ⟨daily 2026-08-26⟩

- **The same call detailed $500bn+ of planned third-party capital through
  financing platforms with Apollo, BlackRock, Blackstone, Brookfield, Goldman
  Sachs and KKR, alongside a take-or-pay/revenue-share model for NeoCloud
  partners.** **The mechanism this thread exists to trace is now visible end to
  end**: Nvidia guarantees the obligation, private credit funds it, and the
  capex never touches Nvidia's balance sheet.
  ([Q2 call transcript](https://www.marketbeat.com/instant-alerts/transcript-nvidia-q2-earnings-call-highlights-2026-08-26/))
  ⟨daily 2026-08-26⟩

- **Receivables concentration widened to five customers holding 72% of the
  balance, from three holding 56% at 2026-01-25.** Read against the guarantee
  disclosure rather than alone: the filing shows Nvidia both extending credit
  to the buildout and collecting from a small set of its builders.
  ([SEC EDGAR, NVDA 10-Q](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm))
  ⟨daily 2026-08-26⟩

## 2026-08-25 — Nvidia is reported in talks for a second Perplexity stake, sized to keep a chip-agnostic AI-search startup inside its ecosystem

- **Nvidia is reportedly discussing a new investment in Perplexity AI at a valuation of more than $30B — up 50% from the roughly $20B mark it carried a year earlier — that would add to a stake Nvidia already holds alongside backers Jeff Bezos and SoftBank.** The Information broke the story; neither company would comment on the talks, and the investment size was not disclosed. This is the same pattern the thread already tracks (Poolside, SSI, Groq, Cloverleaf) one company further down the stack: a chip vendor buying continued loyalty from a customer that could otherwise shop AMD or Cerebras for inference, rather than financing new compute capacity outright. ([SiliconANGLE](https://siliconangle.com/2026/08/24/nvidia-reportedly-eyes-another-investment-in-perplexity-ai-at-a-30b-valuation/)) ⟨daily 2026-08-25⟩

## 2026-08-24 — The Poolside deal this map twice declined to believe gets a reviewed document behind it

- ✅ **A story this thread closed as unverifiable has reversed on new evidence, and the reversal is the point.** For three runs the reported Nvidia-Poolside deal was traced to a single chain — Bloomberg's own headline read "... Newcomer Says," and The Information's 08-21 piece was itself citing a paywalled Newcomer post resting on an investor letter it said it had reviewed. **No Nvidia or Poolside spokesperson, filing or primary statement existed anywhere**, and on 08-23 this map stopped re-checking it. Today the Wall Street Journal reported it having **reviewed the shareholder letter itself**, which moves it from a newsletter chain to a document-based account.
  ([Forbes, 12:13 ET](https://www.forbes.com/sites/jonmarkman/2026/08/24/nvidia-pays-poolside-6b-to-license-its-model-factory-and-109-workers/)) ⟨daily 2026-08-24⟩
- **What the letter says the deal is: $6bn for a licence, $1bn for equity, and more than 100 engineers.** Nvidia pays **$6bn for a NON-EXCLUSIVE licence** to Poolside's "Model Factory" training pipeline, invests a separate **$1bn at a $12bn pre-money valuation**, and takes on **more than 100 Poolside engineers** to work on its open-weight **Nemotron** line — framed explicitly as building a US open-weight alternative to DeepSeek, Kimi and Qwen. **That shape matters for this thread:** it is not vendor financing in the Nebius/Naver/Intel/Groq mould of an equity stake in a customer, but a licence-plus-acquihire that buys capability rather than demand.
  ([Forbes, 12:13 ET](https://www.forbes.com/sites/jonmarkman/2026/08/24/nvidia-pays-poolside-6b-to-license-its-model-factory-and-109-workers/)) ⟨daily 2026-08-24⟩
  <!-- ⚠️ SOURCING, stated precisely: this is still not a company statement.
       It is the WSJ saying it reviewed a shareholder letter, reaching this
       map through a Forbes pickup. That is a real upgrade on the prior
       Newcomer chain and is why the closed call is being reopened — but
       "reviewed document, reported secondhand" is the standard it meets,
       not "confirmed by Nvidia". Nvidia's 08-26 Q2 FY2026 call is the
       natural primary-source test. -->

## 2026-08-23 — Michael Burry restates the Nvidia circularity thesis two days before earnings

- **Michael Burry restated his Nvidia circularity thesis two days
  before Wednesday's earnings print**, saying he expects the print to
  be "lights out" while calling "100% of announced revenue...
  circular." A fresh, dated restatement timed to the earnings
  catalyst — distinct from the 08-13 version already in circulation.
  Three aggregators (TradingView, Yahoo Finance, Stocktwits) carry a
  consistent quote with same-morning timestamps
  (2026-08-24T07:50-08:31Z = 03:50-04:31 ET).
  (TradingView / Yahoo Finance / Stocktwits)
  ⟨daily 2026-08-23⟩
- ⚠️ **Venue unconfirmed.** The quote is corroborated across three
  independent aggregators, but Burry's original post could not be
  reached. Treat the quote itself as confirmed and the platform it was
  posted on as not.
  ⟨daily 2026-08-23⟩

## 2026-08-21 — Nvidia buys into the land-and-power layer: a minority stake in Cloverleaf Infrastructure

- **Nvidia took a minority equity stake in Cloverleaf Infrastructure, a
  2024-founded developer that assembles land, power and shell for
  data-center sites** — reported by outside coverage as several hundred
  million dollars, a figure the two companies' own joint release declines
  to give. Cloverleaf has delivered gigawatt-scale projects in Wisconsin
  and Georgia and claims a 10-15 GW pipeline; Nvidia VP Nico Caprez's
  quoted framing — that "land, power and shell are the foundation" of AI
  factories — makes the intent explicit. It extends the customer-base
  equity pattern this thread already tracks (Nebius 9.3%, Intel $5B,
  Naver $1B, Groq ~$20B licensing) one layer further upstream, from the
  buyers of Nvidia's chips to the people who secure the sites those chips
  will sit in.
  ([Cloverleaf/Nvidia joint release](https://www.prnewswire.com/news-releases/cloverleaf-infrastructure-forms-strategic-partnership-with-nvidia-to-accelerate-data-center-infrastructure-development-302857329.html))
  ⟨daily 2026-08-21⟩

## 2026-08-19 — The mark-only-growth pattern this thread found in NVIDIA's 13F reproduces in SoftBank's

- **SoftBank's own 13F shows the same structure this thread logged in
  NVIDIA's Intel stake a week ago: 67% of a $18B disclosed US equity book
  in one Intel position ($12.14B, 86,956,522 shares), with the identical
  share count at both quarter-ends** — the position's filed value more
  than tripled purely on Intel's price move, no new buying. Two of
  Intel's largest disclosed stakeholders now show the same mark-only
  pattern in the same filing cycle. Intel fell 26.6% between the 06-30
  filing date and 08-14, so both marks are already stale in the other
  direction.
  ([qz.com](https://qz.com/softbank-intel-13f-sec-filing-081826)) ⟨daily 2026-08-19⟩

## 2026-08-18 — The final number is framed explicitly as an answer to the circular-demand question

- **Coverage of the signed $105B figure (see 08-17 entry below) is now
  explicitly framed around why it landed $145B below the number that
  first circulated.** Fortune's read: when a ~$250B figure surfaced in
  July, Nvidia shares dropped ~4.5% intraday on investor concern the
  buildout's demand was becoming artificial — lender-financed rather than
  end-customer-financed. The $105B cap that actually got signed and filed
  is read by the same outlets as a partial answer to that concern, not a
  reversal of it: the obligation is real and large, but bounded and
  phase-gated rather than open-ended.
  ([Fortune](https://fortune.com/2026/08/18/openai-data-center-deal-with-nvidia-comes-in-145-billion-lower-than-reportedsignaling-concerns-of-artificial-demand-for-chips/)) ⟨daily 2026-08-18⟩

## 2026-08-14 — The stake ladder has a filed number, and it is $63.4 billion ⟨caught late⟩

*Logged 2026-08-18. The 13F was filed 08-14 at 16:19:53 ET and sat
unread for four days while this thread described the same holdings in
prose.*

- **Nvidia's disclosed public-equity book is $63.44 billion as of
  2026-06-30, against $13.10 billion a quarter earlier.** The holdings:
  **Intel $29.99B · SpaceX $20.98B · CoreWeave $4.70B · Coherent $3.07B ·
  Nokia $2.21B · Synopsys $2.15B · Nebius $0.33B · Generate Biomedicines
  $0.014B.** This thread has carried the ladder as "Nebius 9.3% · Naver
  $1B · Intel $5B · Groq ~$20B licensing" since 07-27; the filing is the
  actual ledger and it is a different object.
  ([NVIDIA 13F-HR](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000065/information_table.xml)) ⟨daily 2026-08-18⟩
- **⚠️ The 4.8x is the wrong headline — only about $26B of the growth is
  buying.** Intel's share count is **identical across both quarters,
  214,776,632**, so its $7.93B → $29.99B move is entirely price. Nokia's
  share count is likewise unchanged at 166,389,351, and Synopsys's at
  4,821,717. Roughly $24B of the quarter's $50B increase is
  mark-to-market on positions Nvidia did not touch. Any account reading
  "Nvidia's Intel stake grew" is describing Intel's share price.
  ([NVIDIA 13F-HR](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000065/information_table.xml)) ⟨daily 2026-08-18⟩
- **The genuinely new vendor-financing behaviour is CoreWeave, and it is
  the smallest headline in the filing:** 24,277,573 → 47,213,353 shares,
  **+94%**, the only pre-existing position Nvidia added to. New positions
  are SpaceX (122,764,805 shares, ~$170.86 implied at 06-30), Coherent
  and a token Generate Biomedicines stake.
  ([NVIDIA 13F-HR](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000065/information_table.xml)) ⟨daily 2026-08-18⟩
- **⚠️ Two sourcing notes for anyone reading this block later.** Secondary
  reporting puts Intel at ~$22B after Intel's own 08-12 offering diluted
  the position; that is reported, not filed, and this thread carries the
  06-30 filing figure as primary. And **Naver does not appear in the 13F
  at all** — a 13F covers 13(f) securities only, so this thread's prose
  ladder and the filing's holdings are overlapping sets, not the same
  set. **Absence from the filing is not evidence of a disposal.**
  ⟨daily 2026-08-18⟩


## 2026-08-17 — Signed, and priced at $105B in the 8-K the press release didn't mention

- **Nvidia, OpenAI and SoftBank's SB Energy jointly announced the signed
  PORTS-Pike Technology Campus in Pike County, Ohio, with named quotes from
  Jensen Huang, Sam Altman and Masayoshi Son.** Nvidia provides credit
  support on land, power and shell buildout for an initial 4.25 IT-GW, with
  an option on the remaining 3.75; OpenAI is named customer for 8 IT-GW
  total. ⚠️ **Corrected 2026-09-02 — this passage was wrong, and it was wrong in the direction of a "correction."** Nvidia also confirmed a **$1.5B direct investment in SB Energy**,
  correcting weekend reports of "up to $3B" that described pre-announcement
  talks rather than final terms.
  ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-guarantees-sb-energy-s-ports-pike-technology-campus-in-ohio-to-exclusively-host-nvidia-ai-compute), [OpenAI](https://openai.com/index/openai-joins-ports-pike-project)) ⟨daily 2026-08-17⟩
- **The guarantee figure this thread has chased since 07-27 is now
  company-stated: $105 billion, capped, in NVIDIA's 8-K.** "NVIDIA's
  aggregate payment obligation is cumulatively capped at $105 billion for
  its initial commitment under the Agreements." Full trajectory: $250B
  (07-28) → up to $750B in combined SK Group/OpenAI talks (08-04) → under
  $120B, phase-one only, WSJ-sourced (08-15) → **$105B, filed** (08-17). The
  WSJ number was correct in direction and close in magnitude.
  ([NVIDIA 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)) ⟨daily 2026-08-17⟩
- **The instrument is a residual-value guarantee, not a project backstop —
  and OpenAI indemnifies Nvidia for anything Nvidia pays.** Nvidia covers
  "any shortfall between the guaranteed minimum value of a lease and amounts
  recovered through a replacement lease or sale" across ~4.25 GW of IT load.
  A "Trigger Event" is "(i) OpenAI's insolvency resulting in a default under
  a lease, or (ii) OpenAI's failure to make payments under a lease."
  Obligations run to each lease's 20th anniversary and attach only once
  ready-for-service conditions are met, expected beginning in 2028. Nvidia
  may extend credit support to ~3.8 GW more at sole discretion. And: "OpenAI
  has agreed to reimburse and indemnify NVIDIA for any and all amounts
  actually paid by NVIDIA to the Lessor" — recourse runs back to the party
  whose insolvency is the trigger.
  ([NVIDIA 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)) ⟨daily 2026-08-17⟩
- **⚠️ Map-integrity note: the 8-K was public at 08:41 ET, before this map's
  pass recorded the figure as missing.** ✏️ *Timestamp corrected 2026-08-18:
  this read "04:41 ET, four hours before" until the finalize pass checked
  EDGAR's own `ACCEPTANCE-DATETIME` header (`20260817084133`) and the
  submissions API (`2026-08-17T12:41:33Z`), which agree on 08:41 ET. The
  original was a UTC-to-Pacific conversion mislabelled as Eastern.* The
  morning read stopped at exhibit EX-99.1, the press release. The lesson carried forward:
  on any deal creating a financial obligation, the 8-K BODY (Items
  1.01/2.03) is the primary source and the press-release exhibit is not. ⟨daily 2026-08-17⟩
- **Groq — rung four on this thread's stake ladder — raised $350M at $3.5B,
  half its $6.9B September valuation, with Nvidia in the round.** Led by
  Disruptive with planned Nvidia participation. Nvidia hired founder/CEO
  Jonathan Ross and much of the senior silicon team in a $20B licensing deal
  in December; Groq has since abandoned its own LPU architecture and become
  a neocloud running Nvidia systems — 13 data centres, 6M+ developers,
  scaling 54 MW to 200+ MW in 2027. This is the first rung on the ladder
  (Nebius 9.3% · Naver $1B · Intel $5B · Groq ~$20B licensing) with a
  visible outcome, and the outcome is that an independent silicon competitor
  became a customer.
  ([TechCrunch](https://techcrunch.com/2026/08/17/groq-raises-350m-to-fuel-its-pivot-from-ai-chips-to-neocloud/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-17/groq-valued-at-3-5-billion-in-funding-round-after-nvidia-deal)) ⟨daily 2026-08-17⟩
- **Separately, Crunchbase reports semiconductor companies have participated
  in more than $250B of AI/robotics startup financings in 2026 to date, with
  Nvidia leading at 59 rounds year-to-date (up from 53 in all of 2025)** —
  including co-leading OpenAI's $122B round in March and a $5B cheque into
  Safe Superintelligence in July; AMD backed 19 startups including at least
  four $1B+ rounds, Samsung at least 17. Chip-vendor financing reads as a
  sector-wide systemic pattern, not just the headline Nvidia-OpenAI deals.
  ([Crunchbase News](https://news.crunchbase.com/venture/semiconductor-giants-nvda-intc-backing-ai-robotics-starups-2026/)) ⟨daily 2026-08-17⟩
- **Nvidia's own stock barely moved on it: +0.21% at $225.64.** ⚠️ A
  widely-circulating claim of a ~4.5% drop with a record CDS-spread jump is
  MISDATED — its sources reference a "$250B" deal size, the late-July
  figure, so the reaction described is the earlier one re-indexed. Not
  carried.
  ([Yahoo Finance live blog](https://finance.yahoo.com/markets/live/stock-market-today-monday-august-17-dow-sp-500-nasdaq-094421171.html)) ⟨daily 2026-08-17⟩

## 2026-08-15 — The guarantee is cut in half, and narrowed to phase one

- **Nvidia scaled back its planned OpenAI Ohio data-center guarantee
  from $250B to under $120B, and now covers only the first phase of the
  10-gigawatt SB Energy (SoftBank subsidiary) build on DOE land in Pike
  County rather than the whole project** — the change followed investor
  pushback over Nvidia's own exposure to the commitment, per WSJ; a deal
  could be signed "as soon as this weekend." This is the first hard
  resolution of "the guarantee's actual structure and figure" this
  thread has tracked since 07-27 — the number has moved $250B (07-28) →
  up to $750B in combined SK Group + OpenAI talks (08-04) → back down to
  under $120B for phase one alone (08-15). OpenAI is reportedly still
  negotiating a binding lease for the full project despite the narrower
  backstop — the guarantee shrank, the underlying build didn't.
  ([WSJ via Investing.com](https://www.investing.com/news/company-news/nvidia-cuts-planned-openai-data-center-guarantee-to-below-120-billion--wsj-4861735)) ⟨daily 2026-08-15⟩

## 2026-08-10 — Nvidia signs MOUs with six asset managers to mobilize $500B+ in third-party financing

- **Nvidia signed MOUs with six of the largest asset managers — Apollo,
  BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR — to
  establish "compute financing platforms" aiming to mobilize over $500
  billion in third-party capital for AI infrastructure, treating GPU
  capacity as a collateralizable asset class rather than depreciating
  hardware.** Non-binding — Nvidia's own release states the partnerships
  "remain subject to execution of the final agreements." Structured
  through private placements and special-purpose-entity bonds "capable
  of raising tens of billions at a time," off Nvidia's own balance
  sheet, aimed at the same frontier-lab/enterprise/cloud customer base
  this thread already tracks Nvidia backstopping directly (the OpenAI
  guarantee, the Nebius/Naver/Intel/Groq stake ladder). Goldman Sachs,
  the lone bank among the six, is positioned to lead public debt
  issuance while its own asset-management arm distributes the resulting
  returns. CEO Jensen Huang told CNBC he approached only these six firms
  and none turned him down, framing the goal as making AI compute "a new
  class of productive, investable infrastructure: AI factories" — a
  structural answer to this thread's own 07-27 entry (the first time the
  market priced Nvidia's own credit as the risk).
  ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital), [CNBC](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html)) ⟨daily 2026-08-10⟩
- **The same day, Bloomberg Opinion launched "AIndicators," a credit-market
  framework tracking whether lenders financing the AI buildout are
  getting cold feet** (wider risk compensation, shorter loan durations,
  tighter covenants) — framed against 19th-century railroad
  overbuilding. A second, independent data point that AI-financing
  credit risk is becoming its own watched beat, alongside this thread's
  CDS-widening story.
  ([Bloomberg Opinion](https://www.bloomberg.com/opinion/newsletters/2026-08-10/aindicators-hint-at-doubts-in-credit-markets)) ⟨daily 2026-08-10⟩

## 2026-08-04 — Reported scale jumps an order of magnitude: up to $750B in talks

- **Nvidia reportedly in talks for up to $750B in new AI-infrastructure
  deals** — $500B+ with SK Group, and up to $250B in lease guarantees to
  help OpenAI finance data-center compute (the same guarantee this
  thread has tracked since 07-27, now at roughly 3x the previously
  reported $250B figure on the OpenAI leg alone once the SK Group
  component is included). Terms still in flux, unconfirmed by either
  company.
  ([Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/nvidia-750-billion-deals-revive-102003935.html)) ⟨daily 2026-08-04⟩

## 2026-07-29 — CDS eases from the record; the record's date gets corrected

- **The $250B guarantee remains unconfirmed by any company, with terms
  unfinalized.**
  ([Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/nvidia-weighs-250-billion-guarantee-so-openai-can-lease-softbanks-10-gigawatt-ohio-campus)) ⟨daily 2026-07-29⟩
- **The separate ~$350B chip-financing negotiation is a distinct
  instrument from the guarantee.** ⟨daily 2026-07-29⟩
- **Nvidia's CDS eased to ~78bp from Monday's 82bp record.**
  ([Seeking Alpha](https://seekingalpha.com/news/4620575-oracle-leads-record-widening-in-hyperscaler-cds-spreads)) ⟨daily 2026-07-29⟩
- **Correction, stated plainly: the record CDS widening was Monday
  2026-07-27 (Bloomberg), not 07-28 as this repo's 07-28 digest recorded
  it** — an aggregator re-indexing error.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-27/nvidia-credit-risk-jumps-in-swaps-market-on-ai-deal-talk-reports)) ⟨daily 2026-07-29⟩

## 2026-07-28 — Record CDS day ⟨daily 2026-07-28⟩

- **The guarantee firmed to $250B** (WSJ tier-1; the $500B print didn't
  verify) — CDS record single-day widening. **+ $5B into
  pre-product SSI** the same day: the lender now backs companies with no
  product at all.
- **⚠ Date corrected (cross-sweep catch, 5am close 07-29):** this entry
  originally read "NVDA −5%" as a 07-28 move. It was **07-27** — close
  **$196.51, −4.99%**. **07-28** dipped ~2% intraday (low $192.74) and
  closed **+0.25% at $197.01**. The correction sharpens the thread rather
  than weakening it: credit and equity broke together on 07-27, then on
  07-28 **equity refused to follow while the CDS stayed wide**. A
  divergence between what the lender's debt costs and what its equity
  says is more informative than a one-day round trip.
  ([stockanalysis.com](https://stockanalysis.com/stocks/nvda/history/)) ⟨daily 2026-07-28⟩
- **Figure resolved, not contradicted:** NYT/Forbes's "$500 billion"
  headlines (07-27/28) refer to the **total project cost** of the Piketon,
  Ohio site (a former uranium-enrichment plant SoftBank is redeveloping
  with US/Japan government support) — Nvidia's own backstop stays $250B
  across every outlet. A **third, separate figure** also surfaced: Nvidia
  is weighing financing $350B of its own chip purchases for the same
  site. Deal isn't final until Commerce Secretary Lutnick signs off;
  Anthropic, Microsoft, and Google are named as competing bidders for the
  same capacity.
  ([Forbes](https://www.forbes.com/sites/tylerroush/2026/07/27/nvidia-and-openai-discussing-500-billion-data-center-heres-what-we-know/) /
  [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-26/nvidia-in-talks-on-250-billion-backing-for-openai-hub-wsj-says)) ⟨daily 2026-07-28⟩

## 2026-07-27 — The market answers ⟨daily 2026-07-27⟩

- **NVDA −4%, CDS wider on the guarantee reports** — the first time the
  market priced Nvidia's own credit as the risk.

## 2026-07-26 — The guarantee ⟨daily 2026-07-26⟩

- **WSJ: Nvidia in talks to guarantee $250–500B of OpenAI financing** for
  the 10GW Ohio campus (figure unresolved across outlets).

## ← Backstory ⟨steer 2026-07-27⟩

- **The stake ladder to date:** Nebius 9.3% (confirmed 07-20) · Naver $1B
  (07-27) · Intel $5B (Sep-25) · Groq ~$20B licensing (Dec-25) — equity
  and credit flowing from the vendor into its own demand base. Thread spun
  out of `ai-circular-financing-risk` (ben-steer: "thread it").
