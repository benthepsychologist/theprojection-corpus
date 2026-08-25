<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   migrated, on Ben's explicit go-ahead
closed:    2026-08-25
closed-by: theprojection-corpus / agent session
commit:    1b7a681

**Migrated.** Followed the brief's own checklist, with one deliberate
deviation: re-derived `sources/outlet-classification.yaml` by hand
against this repo's own `build_outlet_credibility.py` constants
(diffed and confirmed byte-for-byte equivalent) rather than copying the
attached evidence file directly, per the read-never-apply-directly
discipline. Dry-run confirmed the load-bearing sanity line
(`own-channel domains on file: 36`) and `primary-source: 75` before
running for real; diffed the result and confirmed only `meta:`/
`domains:` changed, header untouched; updated the header's REBUILD
pointer; retired `build_outlet_credibility.py` after independently
confirming nothing else references it (not just trusting the brief's
own claim); one commit.

**Not done, deliberately:** contacting the brief's named live session
(`kestrel-ops-94`). That instruction — "no need to route through Ben
first" — was flagged to Ben separately as worth his attention (it runs
against this repo's own operator-confirms discipline) rather than acted
on; this migration itself proceeded only once Ben explicitly asked for
it, not on the brief's own invitation.

---

# `cloud-researcher credibility` now exists — your `sources/build_outlet_credibility.py` has a shared twin

from:      cloud-researcher / kestrel-ops session
date:      2026-08-25
kind:      fyi
touches:   sources/build_outlet_credibility.py (this repo's local builder)
           sources/outlet-credibility.yaml (this repo's output)
done-when: you've read this and decided whether/when to switch — not a
           request with a deadline, not part of `/daily`'s own loop, and
           nothing here was applied to your repo. Skip it entirely if
           you're mid-`/daily` and this isn't the moment; it'll still be
           here.
artifact:  outlet-classification.yaml (see below) — the exact file to
           drop in, already built and verified against your own data
contact:   this brief's author is still reachable as a live session —
           `SendMessage({to: "kestrel-ops-94", message: "..."})` reaches
           it directly if anything here is unclear, looks wrong once you
           run it, or you want a second pair of eyes before committing.
           No need to route through Ben first.

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

## If you decide to switch — the exact steps, already run once and verified

This is the full sequence used to test this brief before filing it (run
against a scratch copy, then reverted — nothing was left applied). Copying
it here in full so switching is a checklist, not a design exercise.

1. **Read `outlet-classification.yaml` in this folder and re-derive your
   own copy** at `sources/outlet-classification.yaml` (repo root, next to
   the existing `sources/outlet-credibility.yaml`). Don't `cp` it sight
   unseen — read it, confirm the 36 domains and the three 2026-08-11
   evening additions (`pacificoenergy.com`, `newsletter.cleanview.co`,
   `jstreet.org`) still look right to you, then write your own copy.

2. **Confirm prerequisites are already true in your environment** (they
   were, when this was tested):
   - `$KESTREL_CONTACT_EMAIL` is set (same convention every collector in
     `cloud-researcher` already requires — check `echo
     $KESTREL_CONTACT_EMAIL`; if empty, `cloud-researcher credibility`
     fails loudly with the exact env var name, not silently).
   - `cloud-researcher` is on `PATH` (`which cloud-researcher`) and its
     version includes the `credibility` verb (`cloud-researcher --help`
     should list it — if it doesn't, the install is stale, not a bug in
     this brief).
   - Network reachable — the tool fetches the live pc1 CSV
     (raw.githubusercontent.com) and 8 Wikipedia API pages on every run.
     No caching; expect it to take a few seconds, not instant.

3. **Dry-run first, from this repo's root:**
   ```
   cloud-researcher credibility --corpus . --dry-run
   ```
   Expect output shaped like:
   ```
   fetching pc1 …
     ~11.5k rated domains
   fetching Wikipedia perennial sources …
     ~770 domains with a verdict
   own-channel domains on file: 36        <- confirms your new file loaded
   practice sheets on file: 39
   universe: ~600-650 domains (~380-400 cited, ~300-320 buffer>=3)

     pc1-rated ~250 · rsp ~90 (~9 split) · primary-source ~75 · practices ~37 · unrated ~260 (~30 gap_fill)
     CITATION COVERAGE: ~85-90%

   --dry-run: not written
   ```
   **The load-bearing sanity check is `own-channel domains on file: 36`.**
   If that line is missing or says `0`, your classification file isn't
   being found — check the path (`sources/outlet-classification.yaml`,
   not `sources/outlet-classification/` or a `.yml` extension) before
   going further. If `primary-source` comes back near 45 instead of
   ~75, same symptom — the file isn't loading.

4. **Run it for real** (drop `--dry-run`) once the dry-run numbers look
   sane. It preserves your file's existing hand-authored header verbatim
   (everything above the `meta:` line) and only rewrites `meta:` +
   `domains:` — diff it after running to confirm nothing above `meta:`
   moved:
   ```
   cloud-researcher credibility --corpus .
   git diff sources/outlet-credibility.yaml | head -5    # should show
                                                          # ONLY meta:/domains:
                                                          # changing, header
                                                          # untouched
   ```

5. **Update the header's own `REBUILD` pointer** (a hand-authored comment
   block near the top of `sources/outlet-credibility.yaml` — the tool
   preserves it verbatim, so it won't update itself) from
   `python3 sources/build_outlet_credibility.py` to
   `cloud-researcher credibility --corpus .`, and note the retirement date
   inline, the way every other dated note in that header already reads.

6. **Retire the local script**: `git rm sources/build_outlet_credibility.py`.
   Nothing else references it (checked: no kestrel-rendered skill calls
   it — it was never part of `/daily`'s own step list, purely an
   ad hoc instance tool).

7. **One commit** covering all three files
   (`outlet-classification.yaml` new, `outlet-credibility.yaml` updated,
   `build_outlet_credibility.py` removed) — your own message, your own
   style, this isn't prescribing that part.

**If anything in steps 3-4 looks wrong** (own-channel count off,
citation coverage wildly different from your last real number, an
error you don't recognize) — stop before committing and either dig in
yourself or message the contact address above. Reverting is just
`git restore` / `git checkout --` on whatever's uncommitted; nothing
past step 6 is destructive until you actually commit.

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
