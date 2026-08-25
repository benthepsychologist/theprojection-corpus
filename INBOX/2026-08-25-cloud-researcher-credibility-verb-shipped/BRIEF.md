# `cloud-researcher credibility` now exists — your `sources/build_outlet_credibility.py` has a shared twin

from:      cloud-researcher / kestrel-ops session
date:      2026-08-25
kind:      fyi
touches:   sources/build_outlet_credibility.py (this repo's local builder)
           sources/outlet-credibility.yaml (this repo's output)
done-when: you've read this and decided whether/when to switch — not a
           request with a deadline, and nothing here was applied to your
           repo.
artifact:  outlet-classification.yaml (see below)

## What landed

`kestrel` issue #5 (filed 2026-08-07, "the builder should still move
engine-side if this pattern spreads") is closed: `cloud-researcher` has a
new verb, `credibility`, that does what your `sources/
build_outlet_credibility.py` does — same three-layer design (pc1 ensemble,
Wikipedia RSP, `class: primary-source`), same universe logic
(cited-domains ∪ buffer(gdelt+rss, n30d>=3)), same output shape. Run:

    cloud-researcher credibility --corpus . [--dry-run]

**Verified against your own real data**, not assumed: a dry-run against
this repo's live `buffer/` + your site's `data/stories.json` produced 627
domains (385 cited, 318 buffer), 86% citation coverage with your own
own-channel list loaded. Numbers are higher than your file's last-recorded
77%/400 domains because more time has passed and the pc1/rsp sources were
fetched live, not because anything behaves differently.

## What moved out of the shared tool, and why it's not automatic

Your `PRIMARY_OWN_CHANNEL` list (36 domains — OpenAI, Anthropic, the
various `newsroom.`/`ir.` corporate channels, the three 2026-08-11 evening
additions) is **this repo's own curated data**, not something a shared
tool should hardcode or guess at for every consumer. The shared tool reads
it from `sources/outlet-classification.yaml` if that file exists in the
corpus it's pointed at — **your repo doesn't have one yet**, which is why
a dry run with only the shared tool's built-in rules (`_is_gov` +
universal journal/registry platforms) undercounts your `primary-source`
domains (45 instead of 75).

**Attached**: `outlet-classification.yaml` — your own 36-domain list,
extracted verbatim from `build_outlet_credibility.py`'s
`PRIMARY_OWN_CHANNEL`/`OWN_CHANNEL_PREFIX` constants, in the shape the
shared tool reads. This is evidence of shape, not a patch — read it,
re-derive it into your own `sources/outlet-classification.yaml` yourselves
if you decide to switch (per the read-never-apply-directly rule).

## Not done here, on purpose

Nothing in this repo was touched — no file added, removed, or rewritten.
Whether/when to retire your local `build_outlet_credibility.py` in favor
of the shared verb is entirely your call, on your own schedule. If you do
switch: the shared tool's contact-email requirement is
`$KESTREL_CONTACT_EMAIL` (same convention every other collector in
`cloud-researcher` already uses), and `--site PATH` is optional — it
falls back to this repo's own `kestrel.yaml` `outputs.site` if declared.

## Also worth knowing, unrelated to the switch decision

`mhinbrief-corpus` (standing-kind) was the second named consumer in the
original 2026-08-07 ask ("we're going to want the same for
therapybulletin-corpus," Ben's words) — the shared tool was built kind-
agnostic specifically so it works there too, not just for attention-kind
corpora. Not this repo's concern, just context for why the tool isn't
attention-shaped internally.
