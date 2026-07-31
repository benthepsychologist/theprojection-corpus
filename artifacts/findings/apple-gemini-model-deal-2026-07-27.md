---
thread: apple-gemini-model-deal
kind: crawl-finding
date: 2026-07-27
bundle: artifacts/bundles/apple-gemini-model-deal-2026-07-27/
method: >
  WebSearch budget exhausted from same-day sweeps (per /week 2026-07-27
  notes). Built via a sonnet subagent's first pass on Google News RSS
  (news.google.com/rss/search) + direct-outlet WebFetch, then spot-verified
  directly against two primary sources (Google's Jan-12 joint statement,
  Apple's Jun-8 WWDC newsroom post) and re-pulled the RSS listings myself
  for the EU/DMA and iOS-27-beta clusters to get real, resolvable citation
  links rather than relaying the subagent's paraphrase.
---

# The Gemini-Siri deal's missed month, reconstructed — backstory finding

**The throughline:** the deal itself was never secret — it broke in five
separate waves from Nov 2025 to today — but kestrel's 29-day blackout
(06-28 → 07-27) missed only one real story during that stretch: the EU
blocking Siri AI at its EU launch over DMA compliance (06-09), plus the
routine iOS 27 public-beta rollout (mid-to-late July). The **"07-21/22
Siri-Gemini cloud-services extension"** the weekly sweep flagged as the
reason to crawl **does not appear to be a real development** — it traces
to a March 2 2026 cloud-hosting report, re-surfaced by MSN's syndication
pipeline and re-dated by Google News's indexer. That's the headline
finding for the map: treat it as a false positive, not a missed story.

## The arc

- **2025-11-05 — first reported.** Bloomberg breaks the ~$1B/year figure:
  Apple nearing a deal to license Google AI for Siri. (medium — RSS-listed
  only, live Bloomberg page not independently re-fetched)
  ([Bloomberg via Google News](https://news.google.com/rss/search?q=Apple+Google+Gemini+Siri+billion&hl=en-US&gl=US&ceid=US:en))
- **2026-01-12 — official joint announcement, terms partially disclosed.**
  Google and Apple confirm a **multi-year** partnership: "the next
  generation of Apple Foundation Models will be based on Google's Gemini
  models and cloud technology," with **"a more personalized Siri coming
  this year"** as one instance of a broader Apple Intelligence
  collaboration. On-device/cloud split stated explicitly: **"Apple
  Intelligence will continue to run on Apple devices and Private Cloud
  Compute."** **No financial terms or exclusivity language in the official
  statement** — the ~$1B/yr figure is reporter-sourced, never confirmed by
  either company. (high — primary source, fetched directly)
  ([Google's joint statement](https://blog.google/company-news/inside-google/company-announcements/joint-statement-google-apple/))
  Same-day coverage: CNBC, TechCrunch ("Google's Gemini to power Apple's
  AI features like Siri"), MacRumors ("Google Gemini Partnership With
  Apple Will Go Beyond Siri Revamp" — the earliest signal the deal is
  broader than Siri alone), Ars Technica, Gadget Hacks.
- **2026-01-17 — a larger aggregate figure surfaces.** thebull.com.au:
  "Apple Cements $5 Billion Google Gemini Partnership" — a multi-year
  total estimate, distinct from (not a correction of) the $1B/yr annual
  figure. (thin — single outlet, methodology not stated)
- **2026-03-02 — the cloud-hosting detail breaks.** Gadget Hacks: "Apple
  Eyes Google Cloud for AI-Powered Siri Upgrade," citing The Information —
  Apple in talks to host the new Siri's compute on Google's cloud rather
  than purely on-device/Apple silicon. **This is the story that later gets
  mis-dated to July** (see below). (medium — RSS-listed)
- **2026-06-04 — hardware specifics.** AppleInsider: "Revamped Siri will
  tap Nvidia chips for fast, private cloud computing" — the Google-cloud
  hosting runs on **Nvidia Blackwell-class GPUs** with confidential-compute
  framing consistent with Apple's Private Cloud Compute privacy posture.
  (medium — RSS-listed)
- **2026-06-08 — WWDC ships it.** Apple's own newsroom post confirms
  Apple Intelligence is "powered by the next generation of Apple
  Foundation Models, **custom-built in collaboration with Google and its
  Gemini models**." (high — primary source, fetched directly)
  ([Apple Newsroom](https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences/))
  Same-day: CNBC ("Apple partnering with Google and Nvidia for most
  advanced AI model"), 9to5Mac ("Craig Federighi details Apple's
  collaboration with Google for Siri AI in iOS 27").
- **2026-06-09 — the real regulatory story: EU blocks the launch.** Apple
  **withholds Siri AI from EU iPhones at iOS 27 launch**, citing Digital
  Markets Act compliance; **EU regulators publicly reject Apple's
  exemption request** ("no tech rule exemption," per the Commission).
  ~450M EU iPhone users affected at launch. Five independent outlets same
  day. (high — multi-outlet convergence)
  ([Reuters via Google News](https://news.google.com/rss/articles/CBMitgFBVV95cUxPVzNjcTNvOF9vcGtjQlkwczJ2Znk2SGllam1yRlZ2OEdOOHVUdGV6dnl2OW1rMk13cEVxcFlXaHIyVW9FV2liTlhmVHdmT1FlZzFodV9qejNlM2ZRREZkLVNublllRTA0WGRHWnVKS3ViWFFaNEFvUm5JbkZUN0I1NC1MOFF6dXNZY2g0cUl1cFJZQVYwS3VVdnFwdmRFV0Y5TE9KVmFyc1NIMlpseDloU3FkRElFUQ?oc=5) ·
  [euractiv.com via Google News](https://news.google.com/rss/articles/CBMijwFBVV95cUxOZVpCSXo2c0tSMjRyV1Bnc1FiTE5mRjllaHROcmZwWllwNVA2WW5tRHhmOXJDRWxFZDVmaUZRalczWEJCSmVPcXlucUhZeFpJOTQwd2poMGhtOGFDRmpjUWl3WWYyNkh5VmdBNm8wV2M5VGtDNjg4MjZHUldoYUR5bG5TNmNiVXJKQ3lKeGd6NA?oc=5) ·
  [The Verge via Google News](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTndNVXAwRmo5Z3NHYzlfbHlpSUFJUUx3S3czX0JkSTdFN3V2Vl80NTdfYjlUQjQxamNXNnhPcXF3LVpfUUU5VWJ1VXExd2YtOWlwVFhvV0JfTDBSYzlNbWI5S0V0ODVGNUlJc1JvTWo0YWd6UlphTXdzWWJ1MHVpVWNPYXhjRV8xVG1F?oc=5))
  Cross-thread note: **not** the same story as Google's own DMA fight —
  the EU separately ordered Google to open Android/Search to AI rivals
  (mid-July, [The Verge](https://news.google.com/rss/articles/CBMilwFBVV95cUxNaWkxdWZzRUwtWTk2TDdhNmRPZ3VTS3ZQNkRNeWVZUnloUlVKN0k0TGRWUE52amVRcEtfamJ1MWNJcTV2WHJwck40a3dEX1cweGk0OTRza2xlTXZWdWZIbERtV0toWnF4UjdTY2kxV0xnaTBxZGZWTzExRGJZRk1mYWxfQWpycVdyUGk3d2h2dzdhQ1Q5bWpF?oc=5)),
  a parallel DMA thread on the same partners, not this deal.
- **2026-07-13→15 — public beta ships Siri AI broadly.** iOS 27 public
  beta opens Siri AI to general testers (US/non-EU); routine, well-covered
  product rollout, not a deal-terms development. (high — multi-outlet,
  consistent dates)
  ([TechCrunch via Google News](https://news.google.com/rss/articles/CBMipAFBVV95cUxNb2RidWstcDVSb1Y5RHV1a0tVRDBvaDl0bTRTUm5WNlFPQ2s5QWd1UFQ1MUplR20wV3RHWF9hUkM1U0ZRa2ZHc3VNemlzQUVDaEQwQkI4Q3NWLXNhcnRXZ0FDTXRQX1BWc2tSZUFRYmRZRXJQaWE5eUR1eHFuNHNKRDZCalF0UXhMU01vNE1XTmxkVGo0Sk94a1RJNTl3cE9adVhVaA?oc=5) ·
  [Engadget via Google News](https://news.google.com/rss/articles/CBMiZEFVX3lxTE81NFo4SUNHaGdnS19ZeU1zMUVMWjVKN3M4VlByWGUxeVlsNDQxY0pwYkZsak5GeEJUa2ExTkxTWVY0MVpaX0Y2M3hSalpRaE5wbVlvUFo1VzRZVHNXcllVdGlyV28?oc=5))
- **2026-07-22 — the flagged item, resolved.** Google News RSS carries
  **"Apple's recent agreement with Google for Siri update might extend to
  cloud services: report"** via **MSN**, timestamped **Jul 22 2026** — this
  is the headline the weekly sweep flagged as an uncovered development.
  Its wording is near-identical to the **2026-03-02** Gadget Hacks
  cloud-hosting story (see above), which cites the same underlying report.
  No independent outlet reported a *new* cloud-services development in the
  07-20→07-22 window; the only confirmed 07-22 items are routine iOS 27
  public-beta-2 rollout coverage. **Assessment: stale MSN
  re-syndication, re-dated by Google News's indexer — not a new
  development.** This is exactly the failure mode a dated-headline sweep
  produces without opening the article body. (the "thin" flag here is on
  the *newness* claim, not on the deal facts themselves, which are
  well-established from March/June)
  ([MSN item via Google News](https://news.google.com/rss/articles/CBMi1gFBVV95cUxOWWIta2dENEtBMEZFRDd3N1JIQUtNN01QTFFReTV6a3ZKVTE3cXg4ZTU5ekZVQ2J3ajNVLXpnTlRtOWFWNEJhc0JIWmo1bVZTZWpSQVhXWHRFbm1pYzNpUkNsbGhhTEM2OEFhQlRxY0lMNzJJMGlJa1Y2SS1QS2NXQ0xyT0szUUp3MXdZc2ZYVlBzaFlmeU9GVUF1VktheTBVekRseG1TTG00bm5yLTlVREVjbjBITUprZG9OVmhmNEJyYjByR2oxYTMxeGZ3TG1zZGZTYUp3?oc=5))

## Open questions (feed the watch)

- **The $1B/yr (or $5B aggregate) figure is still never confirmed by
  either company** — every restated figure since Nov 2025 traces back to
  the same original Bloomberg report, not a fresh disclosure.
- **Whether Apple builds back toward its own frontier model** long-term —
  no dated evidence either way found in this window; the Apple Foundation
  Models remain framed as "custom-built in collaboration with Google,"
  language that avoids saying whether Gemini IS the Apple Foundation
  Model or merely trained/informs it.
- **EU resolution timeline** — as of 07-09, Tech Times reported "EU Court
  Ruling... Blocks Last Legal Defense" for Google's parallel Android/AI
  case; unclear whether/when Apple's Siri AI actually ships in the EU.
  Worth a dedicated check next crawl.
- **US antitrust angle** — no dated US (DOJ/FTC) enforcement action found
  touching this specific deal in the window; only the EU/DMA angle is
  sourced.
