# Backward crawl — the other three "Big Four" passive managers, AI-investment angle (2026-08-04)

**Trigger:** a board-pass audit found State Street, Vanguard, and Fidelity —
BlackRock's Big Four peers, all already on `board.yaml` (kingdom / capital
pocket / US sphere) — with zero thread coverage, while BlackRock alone
carries `asset-managers-build-ai` (opened 2026-07-28; GIP's $40B Aligned
Data Centers buy, the $12.5B El Paso bond, KKR's $10B Helix venture — direct
equity/infrastructure positions in the AI buildout, not passive index
holding). This crawl asks the same question of each of the three: does it
have a matching story, a different-but-real story, or genuinely nothing.

Method: WebSearch (available all session) + WebFetch on primary/near-primary
pages. GDELT's DOC API was rate-limited on every attempt this session
("please limit requests to one every 5 seconds" persisted past three
retries with backoff) — abandoned in favor of WebSearch, which covered the
May–August 2026 window adequately for all three companies.

---

## State Street — genuinely quiet on AI investment

No evidence of any direct AI-infrastructure or AI-company equity position,
despite a targeted check of State Street's own alternatives/infrastructure
arm (the one part of its business structurally capable of a GIP-style
move, per the board gloss's "constrained — fiduciary; Big-Three index /
SPDR"). Its SSGA alternatives platform advertises capability across
"private credit, real assets, infrastructure, private equity" and
digital-infrastructure/data-center themes generally
([ssga.com/alternatives](https://www.ssga.com/us/en/institutional/capabilities/alternatives)),
but no dated 2026 deal, fund closing, or named acquisition surfaced —
only general capability marketing and thought-leadership commentary on the
AI capex cycle as a market theme
([ssga.com — "Why the AI CapEx cycle may have more staying power than you
think"](https://www.ssga.com/us/en/institutional/insights/ai-capex-cycle-may-have-more-staying-power)).

The only concrete AI story at State Street in 2026 is **internal/product,
not investment**: State Street Alpha (its Aladdin-competing platform,
built on the Charles River Development acquisition + an Axioma risk-model
partnership, $25T+ AUM riding the platform) is building generative-AI
features for client workflow — conversational access to portfolio data,
trade status, and documentation — and State Street cites "400 AI
practitioners" and "six recently won patents" on the effort
([statestreet.com/alpha/insights/artificial-intelligence-investing](https://www.statestreet.com/alpha/insights/artificial-intelligence-investing);
[ssga.com — "How AI is transforming investment management: State Street's
strategic approach"](https://www.ssga.com/us/en/intermediary/insights/how-ai-is-transforming-investment-management-state-street-strategic-approach)).
This is State Street **using** AI to sell portfolio-management software,
the same genre as BlackRock's Aladdin — not State Street **investing in**
AI infrastructure or AI companies. Noted as the weaker, different-in-kind
story the crawl brief asked to flag rather than inflate.

**Verdict: genuinely quiet.** No thread entry, no entity tag.

---

## Vanguard — genuinely quiet on AI investment

Confirms the board's own framing of Vanguard as the most extreme
passive/no-discretionary-capital case ("client-owned at-cost mutual...
no free corporate capital to redeploy"). Every AI-adjacent hit is either
(a) a passive index/ETF product that happens to hold AI or data-center
stocks at market weight — e.g. Vanguard Growth ETF (VUG, $352B AUM, 160+
holdings) or the Vanguard Real Estate ETF's data-center-REIT exposure —
which is index tracking, not a discretionary bet, or (b) internal tooling.

The one dated, real item is **Expert Insights**, an AI-enabled portfolio
analysis tool for financial advisors, announced **2026-04-09**
([corporate.vanguard.com press
release](https://corporate.vanguard.com/content/corporatesite/us/en/corp/who-we-are/pressroom/press-release-vanguard-launches-expert-insights-equipping-advisors-with-ai-powered-portfolio-analysis-expertise-04092026.html)).
It combines "Vanguard's portfolio expertise with generative AI" so
advisors can get instant, personalized portfolio analysis (stress
testing, healthcare-cost projections, Social Security optimization) at
scale without adding headcount — it was in pilot as of the announcement,
with broader rollout later in 2026. This is explicitly **internal tooling
for advisors, not investment in AI infrastructure or AI companies** — the
same weaker-story caveat as State Street, and for the same reason: an
at-cost mutual with no free corporate capital has nothing to deploy into
GIP-style positions even if it wanted to.

**Verdict: genuinely quiet.** No thread entry, no entity tag. This is the
board's discipline working as intended — "inclusive surfacing, selective
promotion" — Vanguard was surfaced and checked, and the honest finding is
nothing.

---

## Fidelity — a real, distinct AI-capital story: direct equity in the AI labs themselves

Fidelity is the one board hypothesis that pays off, but the shape of the
story is **not** BlackRock's shape. BlackRock/GIP buys physical
infrastructure (data centers, hyperscaler bonds). Fidelity is instead
taking **primary-market equity stakes directly in the frontier AI labs**
— OpenAI and Anthropic — through its own mutual-fund complex (Fidelity
Management & Research Company, "FMR"), which is a different mechanism:
retail/institutional fund money buying into private AI-company cap
tables, not data-center ownership.

**Anthropic — three rounds, growing position:**
- Fidelity Management & Research Co. **co-led Anthropic's Series F**,
  September 2025: $13B raised at a $183B post-money valuation.
- Fidelity was named among investors in Anthropic's **Series G**,
  February 2026: $30B raised (GIC/Coatue-led) at a $380B valuation.
- Fidelity was named a **"significant investor" in Anthropic's Series H**,
  **2026-05-28**: $65B raised at a **$965B post-money valuation** —
  co-leads were Capital Group, Coatue, D1 Capital, GIC, ICONIQ, and XN;
  Fidelity sat in the significant-investor tier alongside Blackstone,
  Brookfield, T. Rowe Price, and Temasek, with Micron/Samsung/SK hynix
  as strategic hardware partners
  ([Anthropic's own release, anthropic.com/news/series-h](https://www.anthropic.com/news/series-h)).
  Notably, this Series H is the same round the board's `pif` node's
  AI run-rate math doesn't yet capture — a candidate for a later axes
  refresh, out of scope here.

**OpenAI — smaller but real, and dated:**
- Fidelity holds **~$1.09B in OpenAI shares across 33 separate fund
  vehicles** as of Q1 2026 — the **third-largest fund sponsor** by OpenAI
  exposure, behind Capital Group (~$1.29B) and T. Rowe Price, and with
  "the broadest distribution of any sponsor" (i.e., spread across the most
  individual funds)
  ([leveragedposition.com — "These 66 Funds hold OpenAI
  Shares"](https://leveragedposition.com/blog/funds-that-hold-openai/),
  sourced from SEC N-CSR filings).
- Fidelity Management & Research Company participated as an **additional
  investor in OpenAI's March 31, 2026 round**: $122B in committed capital
  at an **$852B post-money valuation** — the largest single private-market
  round on record at the time.

**Context that bears on how to read this:** both labs are IPO-adjacent —
Anthropic's bankers began investor roadshow meetings mid-July 2026, and
OpenAI was reported in late June 2026 to be leaning toward waiting until
2027 rather than list in 2026 below a $1T valuation. That makes Fidelity's
position a **live, marked-to-model stake in two pre-IPO companies whose
valuations have been resetting every few months** ($183B → $380B → $965B
for Anthropic alone inside eight months) — a genuinely different kind of
watchable risk/story than BlackRock's physical-asset position, and one
that touches Fidelity's own retail fund-holders more directly (they own
this exposure inside ordinary mutual funds, not via a dedicated
alternatives vehicle).

**Verdict: deserves distinct coverage of its own**, not folding into
`asset-managers-build-ai`. Reasoning: that thread's own watch language is
specifically about physical-infrastructure buildout ("who buys the next
hyperscaler asset... locked capital sliding into physical infra") and its
terms list ("GIP data center," "KKR Helix") is infra-specific. Fidelity's
story is capital flowing into AI-lab **equity**, not infrastructure — a
related but mechanically distinct genre within the same broader
capital-flow lens. This is a judgment call, not a bright line — the
alternative (tag Fidelity onto the existing thread and broaden its frame)
is defensible and noted below for the main session to weigh.
