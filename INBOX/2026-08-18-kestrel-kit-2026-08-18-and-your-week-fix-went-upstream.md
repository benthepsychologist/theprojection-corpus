# Your `/week` fix is now the fleet's — plus the new base AGENTS layer

from:      kestrel / engine session
date:      2026-08-18
kind:      fyi
touches:   `AGENTS.md` (429 -> 661 lines), `.claude/skills/week/SKILL.md`, `INBOX/`, 16 kit files
done-when: You have read this and decided what to do about `STATUS.md`.
artifact:  none

---

## 🎉 Your `/week` hot-fix was adopted upstream, and it closed a tracked issue

The local edit sitting in your `.claude/skills/week/SKILL.md` since
2026-08-14 — decay review reframed as a **staleness report** rather than a
retirement queue — has been **adopted into kestrel's library verbatim** and
now ships to every attention instance. It closed **kestrel issue #20**,
which had been filed independently describing exactly this defect.

It was adopted rather than re-derived precisely because your version was
better: it carries Ben's own words (*"I don't understand why we would ever
retire a thread"*), the mechanical reason (`resolved`/`retired` threads
drop out of `/daily`'s collector sweep, so retiring is a decision to **stop
watching**, not to stop displaying), and the evidence — **27 stale threads
reviewed that run, 26 came back "keep."**

Your file no longer reports as drift. It is the template now.

**This is the local-extension protocol working in the direction it is
supposed to work.** A local improvement was kept, noticed, and graduated
up rather than being flattened by a sync.

## What is held back, and why

**`STATUS.md` — untouched.** The base layer now seeds one, and yours is
**1,504 lines** of real hand-written history. Overwriting that with a
skeleton would be vandalism, so it was skipped and reports as drift.

The designed path is a `migrate` verb that reads your file, maps its
headings onto the schema, and proposes a restructured version for review —
never auto-applied. **It is not built yet.** Until it is, the one thing
worth doing by hand is the `*As of YYYY-MM-DD*` line: the schema wants it
alone on its own line, in one spelling, because it is the only automated
freshness check the file has.

## What happened, from scratch

**kestrel** is the engine that renders a versioned set of operating
documents and skills into each repo it administers, hashes what it wrote,
and reports drift. This repo is one of its six targets.

On 2026-08-18 Ben ruled that the **base layer is a schema, not a seed**:
the documents every agent repo has — `AGENTS.md`, `OPERATING.md`,
`INBOX.md`, `STATUS.md` — get an ordered list of sections with an owner
each, and the engine now lints them. Four things landed here as a result.

1. **`AGENTS.md` gained a shared layer.** The base was previously a
   near-empty skeleton; it now carries two engine-owned sections — what a
   kestrel-administered agent repo *is*, and five disciplines the fleet had
   been re-deriving separately in seven different wordings (the operator
   confirms / the agent proposes · provenance travels with the artifact ·
   read `INBOX/` at session start · read-never-run · `yaml.safe_load` or
   revert). Those five were mined from the fleet's own real files, not
   invented. **The operator-confirms rule alone was independently restated
   in four of seven repos**, which is what justified promoting it.

2. **A kind no longer replaces the base.** A kind template is now a
   `.part.tmpl` that *appends*, so a kinded repo gets the shared layer
   **and** its kind's disciplines in one file.

3. **`INBOX/` ships with `INBOX.md`.** Three repos had the contract and no
   queue directory — the file described a hopper that was not there.

4. **`kestrel fleet status` now lints the core docs.** A missing core doc
   is an `alert` with no grace period. Non-conformance is a `warn`, because
   every repo predates the schema — that is migration backlog, not
   breakage. Diverged files report `exempt` and are never flagged.

## Two things about this commit specifically

⚠️ **kestrel committed in your repo, which it normally must not do.**
Discipline 6 says instance repos are tended, not owned, and the commit is
the resident agent's. Ben instructed this one directly — *"do all the
commits and leave notes for each agent so they know what happened."* It is
a one-off on his word, not a new default. Nothing here was authored on your
behalf: every file in the commit is either a rendered kit artifact or this
note.

⚠️ **A bug was found and fixed mid-install, and it touched your stamp.**
`--skip` (meaning "not now") and `--diverge` (meaning "permanently mine")
share one encoding — a null stamp entry *is* diverge. For a file that had
never been stamped, `--skip` wrote that null, silently marking it
permanently yours. Eight files across five repos were affected, and
`kestrel fleet sync` reported all of them as **clean**. Fixed; the entries
were repaired by diffing each stamp against its committed state, which
preserved deliberate divergences. Your held-back files below now correctly
report as drift, which is what "not now" is supposed to look like.
