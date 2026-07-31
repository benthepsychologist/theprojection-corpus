---
thread: meta-capex
kind: crawl-finding
date: 2026-07-27
bundle: artifacts/bundles/meta-capex-2026-07-27/
method: >
  Four parallel sonnet subagents, one per source family (SITES / SILICON /
  POWER / PAYOFF), each running WebFetch against Google News RSS search
  (news.google.com/rss/search) plus attempts at primary sources (Meta
  newsroom/IR, Broadcom, Reuters/CNBC/Bloomberg direct). Across all four
  sweeps, essentially no Google News redirect link or direct-outlet page
  resolved to full article body text via WebFetch (403/404/stub-only) —
  every claim below is sourced to RSS-listing metadata (title, outlet,
  exact pubDate, redirect URL), not fetched body copy, unless marked
  "primary" or "full text." No figure, date, or URL was fabricated;
  where outlets disagree or a figure could not be corroborated, it is
  flagged (thin) rather than resolved by guessing.
---

# Meta's capex destination — where the ~$135-145B goes, and the credibility test

**The throughline:** Meta's capex guidance escalated through 2026 — **$135B**
guided at the Jan 28 2026 Q4 call, **$145B** the figure recurring in
Apr-Jul 2026 coverage — and this crawl could **not corroborate the "~$76B
TTM" figure** given in the crawl brief; a dedicated RSS query for that
exact phrase returned zero items. Flag this as an open discrepancy, not
resolved here (possibly a stale/earlier trailing-spend read, distinct from
the forward guidance number). What the money is buying: three named
gigawatt-scale campuses (Hyperion/LA, Prometheus/OH, El Paso/TX) plus
"tent" data centers built in ~3 months for speed; a silicon strategy
splitting between in-house MTIA chips (accelerating, 4 new generations
shown March 2026) and Nvidia/Broadcom-partnered compute (the "600K
H100-equivalents" figure is stale, superseded twice); a power-sourcing
push that is simultaneously green (NextEra, nuclear RFP, geothermal) and
walking back its clean-energy pledge (Meta quit RE100 this week, 07-23/24,
citing a 7.5GW Louisiana gas buildout); and a payoff narrative
(Zuckerberg's "superintelligence" framing, the $14.3B Scale AI stake,
unproven ad-revenue attribution) that a Moody's credit warning
(2026-07-24) directly challenged four business days before Meta's
2026-07-29 earnings.

## 1. SITES — where the physical buildout stands

- **Hyperion (Louisiana) — confirmed 5GW / $50B+, expanding this week.**
  Reuters, CNBC, and Data Center Dynamics independently reported the same
  day that Meta's Richland Parish campus expanded to **5 gigawatts** and
  crossed **$50 billion** in investment (medium — RSS-listed, multi-outlet
  same-day convergence).
  ([Reuters via Google News](https://news.google.com/rss/articles/CBMirAFBVV95cUxPQnJpUGtNQXFzaExPZlhub1lVWlM1S01ya3VLVlo1dUlFMzZBcWF5Mm1KdXhPdmg0b0NJMVlseTNlMGRsWksxUnQ4UXFmQWpySGhOWEpiaGk5bHhsSFZ5X1VtRXVCQ0dLTG9FWGNlVDhKT1Z6c1F4TnRKaVNVVGw5dmxLOFdRTm5KdWc4VUM3dGR1LV8yanp2eDlRR2ZHU19ZMDJfcmxzN2RkZHlW)) ⟨2026-07-13⟩
  - Bloomberg's earlier report put the same project at **$200 billion**
    (2026-05-18) — a much larger figure than the now-standard $50B; not
    reconciled here, likely a different scope (total multi-decade
    ecosystem vs. discrete capex). **(thin, unreconciled)**
    ([Bloomberg via Google News](https://news.google.com/rss/articles/CBMihgFBVV95cUxPRFBfZktZYmFuZWJkNV9pcTM5b004dllfaUNTel9aakZ5NVhUYkRIZnF0eXJKVEpEcFNvNmM0WTVvNll5c2o1elZURmdHdXkwaTVSUEh1Wm9peGVyRkdUbi03T3cxY3NKXzFEeEFWNWtORnAtOGhjRnlwV1ZreFUxVjczQ2FZQQ))
  - **This week, 07-23→07-27:** Meta **quit the RE100** clean-energy
    pledge amid a **7.5GW Louisiana gas buildout** for Hyperion
    (TechCrunch 07-23, MLQ.ai 07-24); Meta **sold 80% of the Louisiana
    data center to Blue Owl Capital**, timed to gas-plant regulatory
    approval (Startup Fortune, 2026-07-27, thin/single-outlet); and the
    NYT ran an investigative piece, **"How Meta Got Everything It Wanted
    in a Secret Louisiana Data Center Deal"** (2026-07-27, headline-level
    only, body not resolved).
    ([TechCrunch via Google News](https://news.google.com/rss/articles/CBMiugFBVV95cUxPbV82R1o2SFVLdGFOTW1Md3NYMXhtdjg5VlZ4bWRBZjJQNlpOOVNXTDJ6aDdnQTI1eUF6UkFkR2xINklyN3o1dnQwc3cwRDhOY3d5NzFacVdSTHRMZmdXTGpXejZEMkJfeFhUVEc2UnBMX2hDMGI5c0trc0tlanBYbEFzLXQ2TjBHVEZhbEZLZWF1S0FDUWJCS0NzZzNadGZMZGV3UlZsMGRJZWJXdGZOSHU0Q2E2LXZZU1E)) ·
    ([NYT via Google News](https://news.google.com/rss/articles/CBMigwFBVV95cUxOcUlaenRqekZMbnpqR25zZmJoZ2xHRVZlOUc1WDdiZWRPc2JuT0FkZEs2VHpybElkSkVka3R4MVlzUVBjSWR4cnNsNGxRLTJHRHFlamROTnhZVzN2NU1NUVozcENDVjlCR09BWldKc3k4ZndSVzU3Qlh2SnFiZ2ZaRnJvVQ))
- **Prometheus (Ohio) — no clean 2026 GW re-statement.** Originally
  unveiled at **1GW** (2025-07-15, Economy Middle East / TechSpot),
  described by NBC4 as the "world's highest capacity data center"
  slated to open in 2026 (2025-09-23, thin — never independently
  confirmed as opened). Banks sold **$3B in debt** for Prometheus
  specifically (Bloomberg, 2026-04-08). The 6.6GW nuclear figure (below)
  spans multiple Meta projects, **not Prometheus alone** — treat
  "Prometheus = 6.6GW" as unconfirmed.
  ([TechSpot via Google News](https://news.google.com/rss/articles/CBMikAFBVV95cUxPZlBtaVp4eWx2UXNKaEt2UmprMmtoMDYtNE5BRmM1a24tQ0YtdlZNVGVHRmNya09qN0hEcjEtMTF0NjExRUtfVF93WV9XMV9xd2x0OFRjTnEzMEpMb2Z3MEJJUUZtRU5TNWdKay05ZW1sWFpQMHcyd1VXem53T3pmZ0hmMkYzeTRJSHpDMGlnMTI))
- **El Paso (Texas) — 1GW campus, capex up 6x to $10B, expanding, facing
  local pushback.** CNBC (2026-03-26) reported Meta boosted its West
  Texas investment **sixfold to $10 billion**; Meta broke ground on the
  1GW campus (2025-10-17) and filed to add **12 new buildings**
  (2026-04-21, Data Center Dynamics). **This week:** El Paso City Council
  ended new tax breaks for future data centers (07-21) and a resident
  "Block Party" protest ("get out of our town") ran 07-25/26 — community
  opposition is intensifying in real time (KTSM/KVIA, thin).
  ([CNBC via Google News](https://news.google.com/rss/articles/CBMipAFBVV95cUxQQzlUNzhaWENtQV9WLW1FTVBXYTVJT1JXWUY2VGdyQTBDak5feTBqdXJYWWlMVE1ubDJZSGpzVno3dEZ0TVpkYkNzS2F2Z0NMd2Q1V2h0UURmRjRueXhZOUdZSHRrV2tENWRDNlJyWnpMaUpjQTdXVlIxbHpVcEJWc2RfZnh6UkJsOU02ajV6QVpTZkpIUTJVTWdOYzNGaFp2NVJnZQ))
- **Tent buildouts — real, ~3-month build time, off-grid power.**
  Confirmed multi-outlet: tent structures at Ohio (New Albany) and
  Tennessee (Gallatin) sites cut build time roughly in half vs.
  traditional shells (Tom's Hardware, MLQ.ai, TechCrunch, Tech Times, all
  2026-06-04/05); originally reported 2025-07-14/15 alongside the
  Hyperion unveiling. Power source described inconsistently — "jet
  engines" (Tom's Hardware) vs. "400MW off-grid gas" (MLQ.ai) — likely
  the same turbine generation described two ways, **not reconciled**.
  ([Tom's Hardware via Google News](https://news.google.com/rss/articles/CBMizAJBVV95cUxQcmhNQ1l1dndwVTc5LTZIVFY1S3dUTDE5eVl5TTNRMldpYXZFU0RYcTUzU2pTTnRwR1A2VC1NWUhIVG1xbDRuXy14MXRMUzd6amxNbGxfeERWZERsY3laWFVEU1F5eDhRR0RCRmJGNDNkeW1kQnYxVXlLUkhwVGd3STEyeTNKZUl0Um5DY0lKdnZCZjNqcWVySlVZYkZwdzE2SUZEWm9UeUU0WTFBMXNGX2ZYbkd0cDVYTkNnZC1MbElsS3g0WU1Ea3FscUxOR0wtYm1HN2JxUF9DU1UtZzJoY0E1Mmdsa3htSU5xSWI3cndDc3lFOU1wNFlLME95OTBNeXFnbDJZMF9ZbzBST3hhWjdLc3o0N2lPRkxlTktERlFpRDlzbFl6WHd3a1puUTZTRVdKQ2dVMHZLWndvcTJaUUJWblotc0ZCTzliRA))
- **BlackRock $12.3B bond — soft demand → rally, the exact 07-24 angle
  asked for.** Timeline: launched/priced **2026-07-24** at **$12.3B** for
  a new Meta Texas (El Paso) data center vehicle, **yields reportedly
  topping 7%**; Business Times ran **"BlackRock gets soft demand for bond
  sale after AI debt sell-off"** on **2026-07-25**, the direct hit for
  the soft-demand angle. The deal was **not** downsized — by
  **2026-07-27** Bloomberg/Yahoo Finance reported it **rallied** and the
  final raise **upsized to $12.5B**. BlackRock reportedly holds an 80%
  stake in the financing vehicle (Business Model Analyst, 07-20, thin).
  Broader framing: two separate outlets (The Globe and Mail 07-22,
  Bloomberg Tax 07-21) call these off-balance-sheet AI-debt SPVs an
  "Enron-echo" / "$420B hidden debt" pattern across Big Tech — context,
  not Meta-specific confirmation.
  ([Business Times via Google News — soft demand](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNczRZV3BqaWcxRjlmRDRTYnNiZEhpUzFUQTRFZmtpYjdDcEVBcjVhTjhfZzFMN1VCNFRkQWstakFMd2tNSENSZ19JZ3U5UkFJTDVKUkZMQnBBV19CamU1ZWNyeU9sX1V0a0JTTms2S3BYeUtPblhRZmpOSXRjVnlCdUlFV2ZtbGtmVVpXSzdCbXhhcEdzZGExZWRhVlk1c3dNdFk1Mmt5RjVzZw)) ·
  ([Bloomberg via Google News — rally](https://news.google.com/rss/articles/CBMitAFBVV95cUxPVzhQWmhER3FyVGh2YWFNWFVxclRiWm1RTndTQ0UxSTU1UXRHbGt1aFlqTG1ndXg1dVRwWGl4OEQ1RVdIQ3luUDk1XzFYMmlqME90QVZvY3Jza3N2MFJVdU5pS2tjNERNTFVnc3NUd0tTMmd3anFnTEtKMWlwNzZhdm14eDc1WUlZMUt3TDVwbDBMa0JLdy0xdmh3YnFmWlozd3hFYXBxdlhMUGx0UmtTQ2ZSOTU))

## 2. SILICON — MTIA vs. Nvidia vs. Broadcom

- **MTIA — active roadmap, next chip due September 2026.** Meta unveiled
  **4 new MTIA inference-chip generations** in March 2026 on a **6-month
  cadence** (multi-outlet: CNBC, Tom's Hardware, ServeTheHome, The
  Register, all 2026-03-11/13). A Reuters exclusive (2026-07-13) reported
  a next chip, reportedly codenamed **"Iris,"** entering production
  **September 2026** to **double compute capacity** — well-corroborated
  secondhand (4+ outlets citing the same Reuters exclusive) but not
  primary-verified, since Reuters' own body text didn't resolve.
  ([Reuters exclusive via Google News](https://news.google.com/rss/articles/CBMizAFBVV95cUxOQmJUcmlIQzJ4M0Vmd1QxQno5ajZPWnFqRHMtQkNMSzVRMHlnOXBqZDN4cjVuRU1XR3IyajdHekZJRkNpeXA2UjRBaXdiaDlnbkxVa1VXb1hwY3BDMUE1am9uX0o3OUxYTWVkeUMyemFUQ0JkMlVpX1RWSTBLVzI3bC1uaTVGelVXd1pSdEY4RHpreUQySmhOUjZMemVGQ3k4YTREY3VxN3k5alhELVdJa1hGeGYxbUltMV9mVUtHZWM4SmQ1eGNqRkk0RUk))
- **Nvidia "600K H100-equivalents" — stale, superseded twice.** Origin:
  Data Center Dynamics / CNBC, 2024-01-18, Zuckerberg's "600,000 H100
  GPU equivalents by year-end" claim. **First supersession:** PCMag,
  2025-01-24, Zuckerberg targeting **1.3 million** GPUs. **Second
  supersession:** CNBC/Axios, 2026-02-17, **"Meta expands Nvidia deal to
  use millions of AI chips... including standalone CPUs"** — no precise
  new count found in this pull; treat any current use of "600K" in the
  thread as outdated.
  ([Data Center Dynamics, origin, via Google News](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQT3hqcWJubkdxUzE4cUQxZXRBdk9TNjg5TjVzTzJSSXE5TzAyRjJQak91VzJkTzF0dWhpLVdocmk1QnVKeFpwLWF3Y0FscWszbWZ0VDRYQUlob0dMSTg0U2FqSFl2U0VNNlV4UVdZR2w3OVNocFpqWTlHczNJMnVQSTloSGR4dUdGMGFz)) ·
  ([CNBC, Feb 2026 expansion, via Google News](https://news.google.com/rss/articles/CBMif0FVX3lxTFBiLXZYX1ZjaTRaenZCcmpJT0FZTksxVFpNOWhYOXBHenZDUjlKLXBoTDJuOHluYzRiSWx0YVV6Slljb3NBem9CLVlJUHlTR1FIQk15ODZGRm4yaXduckZ6YW9DNTJoYkZveDFwS3Y1amFOTkRiSi1lNDYxZlQwMFU))
- **Broadcom — extended April 14 2026, through 2029, 1GW+.** CNBC,
  Reuters, and Broadcom's own release (GlobeNewswire) all confirm the
  same day: Meta commits to **1GW+ of custom chips** with Broadcom
  ("multiple generations" of MTIA), the deal extended **through 2029** —
  announced the same day Broadcom CEO **Hock Tan stepped down from
  Meta's board.** Still the live figure as of 2026-07-24 (Mshale
  re-confirms the 2029 term, no further extension since). A **$35B**
  dollar figure for the extension (tech-insider.org, 04-22) appears in
  only one lower-tier outlet — **not corroborated**, do not treat as
  confirmed.
  ([CNBC via Google News](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQU3JRUzgyMGZsQ08tLVgyTzNfZE1PZUdJaDBIVFZJUmlfM1daVEVFSEhvOTNXV1Y1UTRKQ1hPRk90UWExbjl1MGpjU0NSTVc4aGhXZWV3X242NGFoLUJ3TjJVZXZ2UHY4QjdVOGlqWXd4a1l0SWI3Z2ZnTHdCVmE4cy14alMwOGhUX09YUEtWeGJaYmhXcGxzejd3VHRlaUtHSDdRa04yc09pUklmZk82RG5XdGw0ZGhweDFMZjl5ZVhsOVdPNGRkRQ)) ·
  ([Broadcom official via Google News](https://news.google.com/rss/articles/CBMipgJBVV95cUxORkVKMkdhVWN4WHpSdm9ObFdrX0s3cERiSnFkbnlqUkhkMlN4cHhOdm9wcHNlekp0Mk54TUNpbW50aW0yQlYxaDhJcWM5ZlJ2SWEyRFFSdllGemFvS2FjZTRhSWtjZE1zNWZsbFpibk1KZkprbFhOTmVUVlFjcnhOWGNhTjRFQ0RUNzNWSWotc1JfeTRFWWpLRHNxVEthVHFxOXB2R2NyZlZOVXBzMFFRMTZJblZORHN1UzV5QlN4VmQ3ZzdKTmR5d0ZxVnJFTzVDZGpHU2wyel8tQU9yX0pUeEpLVkVDa2t4dXNfQzlURlZ6QVI3MlJsNUpkYllBcW5ySUVlR1dJTkk3LWpjZHl4SmRIajM5NDRHRG1PUV93eG5VTENiMWc))

## 3. POWER — PPAs, geothermal, nuclear, and the gas pivot

- **PPAs (2025-2026), no single combined total reported.** Largest
  single deal: **Meta–NextEra, 2.3GW solar + 165MW storage** across
  ERCOT/SPP/MISO plus a New Mexico tranche (full text confirmed,
  2025-12-08). Others reported this year: **Meta–DESRI, 850MW new PPAs,
  2.5+GW cumulative partnership across nine states** (2026-05-12);
  **Meta–Constellation, 20-year PPA for the entire Clinton, IL nuclear
  plant** (2025-06-03); smaller solar deals with Enbridge, RWE, Zelestra,
  EDP Renewables, Sabanci, Lightsource bp, and a **Noon Energy** deal for
  up to **1GW/100GWh long-duration storage** (2026-04-21/22). No outlet
  in this pull reported one aggregate figure spanning nuclear + solar +
  geothermal + gas.
  ([ESG Today, NextEra — full text](https://www.esgtoday.com/meta-signs-2-5-gw-of-u-s-clean-energy-deals-with-nextera/)) ⟨2025-12-08⟩
- **Nuclear solicitation — awards Jan 9 2026, up to 6.6GW.** RFP launched
  **2024-12-03/04** (outlets disagree on the original target: Reuters/
  Utility Dive/World Nuclear News say "up to 4GW," Data Center Dynamics
  says "1.4GW" — **unresolved discrepancy, thin**). Awards announced
  **2026-01-09**: **Oklo** (1.2GW, Southern Ohio), **TerraPower** (8×
  Natrium 345MW plants, incl. Cheyenne WY), **Vistra** (expanding Beaver
  Valley, PJM region — exact MW not confirmed). Aggregate figure,
  multi-outlet including Meta's own release: **"up to 6.6 GW."**
  ([Meta Store, official, via Google News](https://news.google.com/rss/articles/CBMilwFBVV95cUxOT2pPa1RyS01SdjVXYmtibWp3MURDbHJuRjhMb3BuUkI4dXZueW5uMzhIUkFKamsxYW55VDZ5Z0RlU1R4M3ZnODRIMXl2SW5xOURoRTFyNlhYbkVlNXVTd3N6N0N5aHB4OXdrc3JKR3hTUG1jNnE4ZnRpdzM5bzRGdDh0S0JzVWZCSG1DN21fSlFqYzdObjJJ)) ⟨2026-01-09⟩
- **Geothermal — two separate 150MW deals, not one program.**
  **Sage Geosystems**: original 150MW PPA (2024-08-26, pre-window but
  foundational); Sage raised **$97M Series B** and announced plans for
  "the world's first commercial pressure geothermal power generation
  facility" (2026-01-21/22, thin — headline-level, capacity/location of
  the new facility not confirmed). **XGS Energy** (a separate partner):
  **150MW** geothermal deal in **New Mexico** (2025-06-13/18, thin —
  headline-level). Do not conflate Sage and XGS totals.
- **The gas pivot — this week's real news.** Meta committed to **seven
  natural gas plants** for Louisiana (Forbes/Engadget/TweakTown,
  2026-03-27/31) and is separately reported operating/building **7.5GW**
  of Louisiana gas capacity in the context of **quitting RE100**
  (MLQ.ai/Electrek, **2026-07-23/24** — the most recent, and arguably
  most consequential, item in this whole crawl: it directly cuts against
  the clean-power-sourcing narrative built by the NextEra/nuclear/
  geothermal deals above). Recommend this become its own line in the
  thread's watch, not buried under "power."
  ([Electrek via Google News](https://news.google.com/rss/articles/CBMihgFBVV95cUxNckllSG9UbFR1QTBNRWtjSVAzVHJKd0MwWFJTTDVGVlZyTXd5am4xRk9QaW1kdnpXbGZqQ25HZGlWaFdBaHBRN082U1ozUS1pcTdkR1k2Qkl1b1BRbGIwTXE1b1VWRGVuYmE3S3V3V3ZYeHRRbUM0ckpNVjhsUndCblN4MFZvZw)) ⟨2026-07-24⟩

## 4. PAYOFF CLAIM — superintelligence, Scale AI, ad-revenue, and the Moody's warning

- **Zuckerberg's "superintelligence" framing.** Launched publicly
  2025-07-30/31 (Reuters/TechRepublic — pledged "hundreds of billions"
  for AI data centers, "superintelligence for everyone... now in
  sight"). Reaffirmed at the **2026-01-28/29 Q4 earnings call** alongside
  the capex raise ("Meta boosts annual capex sharply on superintelligence
  push, shares surge" — Reuters). By **2026-06-14**, CNBC's framing had
  shifted to skepticism: **"A year after Meta tapped Alexandr Wang...
  Zuckerberg has to sell it."** On **2026-07-02**, Business Insider
  reported Zuckerberg telling an internal town hall that AI agent
  progress is moving **"more slowly than expected"** — a real
  moderation of the framing four weeks before earnings. No exact quotes
  independently verified (all headline-level).
  ([Reuters, Jan 2026 earnings, via Google News](https://news.google.com/rss/articles/CBMiswFBVV95cUxQejJlUUhHUzdMNVdYaVp1VUZnOEV4NnByWHdkeFpzUVYzYjN0RWlzTHQxMDV5RTNZN1RQSUREY2ZYUWVMMDNNcHVONktzVDNsSGl1bmFzTXQwQm5kanRxYnVLRVZmZUxkQmY5YXplOWtHN0doSVdUVERBWlNIamRXMlU1c2RCQWZfM0NBMUpiekNad2xSUWowbmpHdG5HLWJULTlqYjI3c2o0cS1Bd041YkFMVQ))
- **TBD Lab / Scale AI ($14.3B stake) — a payoff bet under real strain.**
  Meta invested **$14.3B for ~49% of Scale AI** (2025-06-10/13), hired
  founder Alexandr Wang as Chief AI Officer; the elite research group
  named **"TBD Lab"** (WSJ, 2025-08-11). Since: a fourth AI-org
  restructuring in six months (Aug 2025), ~600 layoffs from
  "Superintelligence Labs" (Oct 2025), chief scientist **Yann LeCun's
  departure** calling LLMs "a dead end" (Nov 2025), a **$200M hire
  (Ruoming Pang) leaving for OpenAI after 7 months** (Feb 2026), and
  continuing "suffocating management"/"soul-crushing" internal-culture
  coverage through June-July 2026 (TechCrunch 06-12; multiple outlets
  07-17→07-25, right up to this week). Meta's first shipped product from
  the org, **Muse Spark**, launched 2026-04-08. No change to the equity
  stake itself found since June 2025.
  ([WSJ, $14.3B deal, via Google News](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcUl5MS1ZV3ZudEdnOGpSVkZ4V0RvdE1xNXJIRGhEaUxLd3VhTFBTeXFiSGxxZFBfQlFVekQyOHpMYVlmN0RheW9IZVJuOGtSMU1yN3pxajBDWUliQzVEaGpRVEtBZFhXUWFyWFNNcTRrXzdWSFlIZVdVSTF1bjV6Sk9xSTVJREZRZmE2QVlYR0dNZ2R1THZ1U3FkX1FJM2NRYjFhRXFIX29sQQ))
- **Ad-revenue attribution — asserted, not shown.** Meta's own investor
  content frames "2026: AI Drives Performance" (2026-01-28), and
  financial-media coverage pairs **33% ad-revenue growth** against the
  **$145B capex** figure repeatedly (TIKR 04-30, AlphaStreet 04-27,
  tastylive 07-27). But no independently-verified direct quote from a
  Meta executive attributing a specific percentage of ad growth to AI was
  found in this pull — every hit is a financial-media aggregator pairing
  two headline numbers, not a sourced attribution claim.
- **Moody's credit warning — confirmed, dated 2026-07-24.** CNBC:
  **"Moody's says 'unprecedented' AI spending threatens credit quality of
  Amazon, Meta, Alphabet and others,"** 2026-07-24 17:37 UTC, corroborated
  same-day/next-day by five other outlets (The Tech Buzz, KuCoin,
  finance.biggo.com ×2, Cryptopolitan, Startup Fortune). Cryptopolitan's
  companion piece frames Meta/Amazon/Alphabet as **lower-severity** risk
  vs. Oracle/CoreWeave flagged as the "weakest credit link." **Not
  confirmed:** whether this was a formal rating action/outlook change or
  general commentary, or any Meta-specific number — body text never
  resolved. Builds on earlier 2026 Moody's warnings (Feb 23/25, Mar 13)
  about hyperscaler capex and data-center accounting broadly, so this is
  an escalation of a running story, not a one-off.
  ([CNBC via Google News](https://news.google.com/rss/articles/CBMilgFBVV95cUxQc3Uzc2dUOF9odGJhRS16SzZrQ1ZYOFNLOWs3dFJ3T3d6ektVZzluX01Gb1haM0V4QzJGY0o1RWRybVN5Qi1OZUg1SEE0U3NTcjBSbGphdUdBZmNqci1zakhGNVliTUZVQWVjZ0hla0ZFOHZQeUZ3U19jelRENHl3TXlJZ1VtYkdpTndKVDJMRWtQQjEtaXfSAZsBQVVfeXFMT3FJRGVjZUV1MFJOaldHYmpwR0VJVG1DalVFeVA1SWw4V0lnM2dSbkoyNGU0aEFhZW1WU2lMWXVQMjdNRUZJSG1NOHV3ODFBQ1dMOUF1T3RfQm1yLVF0TWVsNmYxTlZ6VVkxTFAwbWd4akV5RTZPMTFLWlFYX25kWHlaZTVFamJLWjZsVnlUaE81M0VZNDViUVljQ1U)) ⟨2026-07-24⟩
- **Earnings 2026-07-29 — what to verify.** Confirmed via Meta IR
  (2026-07-14 release). Watch for: **(a)** whether capex guidance climbs
  past $145B again (Q1 2026 already saw a capex-raise-driven selloff);
  **(b)** debt/bond commentary given both the Moody's warning and the
  BlackRock soft-demand episode ("AI-related bond cracks emerge," Crypto
  Briefing, 2026-07-27); **(c)** confirmation (or not) of the separate
  **$10B Anthropic cloud deal talks** reported 2026-07-22 (Motley Fool),
  which would make Meta a fourth major cloud provider; **(d)** any Scale
  AI/TBD Lab organizational update given the sustained negative internal
  coverage through this week; **(e)** the exact ad-revenue framing Meta
  itself uses vs. the media's 33%-growth pairing. **The "$76B TTM"
  figure from the crawl brief could not be corroborated** — a dedicated
  query returned zero results; verify its source before repeating it in
  the thread.

## Open questions (feed the watch)

- **The $76B TTM figure is unconfirmed** — the two numbers that actually
  recur in 2026 coverage are $135B (Jan guidance) and $145B (Apr-Jul
  coverage). Worth checking whether $76B was a stale first-half actual
  spend read, or a different metric entirely, before it's used again.
- **RE100 exit + 7.5GW gas buildout (07-23/24) is the freshest,
  highest-signal item in this crawl** and directly undercuts the
  clean-power PPA narrative — deserves its own watch line, possibly its
  own thread if it develops further at the 07-29 earnings call.
- **BlackRock $12.3B→$12.5B bond (07-20→07-27) is a live, fast-moving
  sub-story** — launched, hit soft demand, then rallied and upsized, all
  within one week. Good candidate for the thread's "last 7 days" block.
- **Nuclear RFP original target (1.4GW vs. 4GW) is an unresolved
  outlet-level discrepancy** — worth a primary-source check (Meta's own
  Dec 2024 RFP announcement) if it matters to the thread.
- **Prometheus (Ohio) has no clean 2026 GW re-statement** the way
  Hyperion does — worth a dedicated follow-up query next crawl.
- **No Meta-sourced, quote-level ad-revenue-to-AI attribution figure**
  was found — every pairing of "33% growth" and "$145B capex" is
  media-constructed, not a company claim. Watch the 07-29 call for
  whether Meta makes this claim directly.
