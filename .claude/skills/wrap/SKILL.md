<!-- kit: attention/wrap@2026-08-21.4 — canonical: kestrel/library/skills/attention/wrap/SKILL.md.tmpl — provenance only. A local edit is fine; kit.py sync will flag drift. Route a wanted template change to the engine's issue tracker (dev) or its ops inbox (anything naming a live repo), never a direct edit. -->

---
name: wrap
description: Checkpoint the session's work — sanity-gate the pipeline state, refresh STATUS.md without rot, append the log.md close entry, commit both zone repos with provenance receipts, push, and verify the push actually landed. Safe to run several times a day; never reads as "session over."
disable-model-invocation: true
---

# /wrap — persist the session, verified

**This is a CHECKPOINT, not a closer** (borrowed verbatim from pm's wrap,
because the usage pattern is identical): Ben runs `/wrap` as the save
button, possibly several times a day, mid-flow. Never append end-of-day
framing to its report, and never treat a wrap as permission to stop
watching the pipeline.

**Scope — what this skill writes, and what it does not** (the
cloud-governor discipline): it writes `STATUS.md`, `log.md`, git commits
and pushes in the two zone repos (this repo + the site sibling), and at
most one brief into `kestrel-ops/INBOX/`. It does
**NOT** write digest content or frontmatter (that's `/daily`'s state
machine), `attention/` steering files (that's `/steer`/`/daily`), or
publish content (that's `/publish`). A wrap that finds those needing work
*names* the need in its report; it doesn't do the work.

## Dispatch map (the global rule, specialized)

- **One sonnet pipeline agent** may run steps 3–5 sequentially (commit →
  site-repo check → push + verify), quoting `git` output verbatim —
  scoped adds, never `-a` blind. One committing agent at a time.
- **Frontier keeps** step 1's content judgment (what STATUS.md's top note
  says), step 2's log entry (it's the session's interpretive record), and
  the step-6 report.
- Steps 0 and 5's checks are haiku-grade reads if dispatched; fine inline
  too — they're single commands.

## Steps

### 0 — sanity gate (read-only; the cheap version of cg's health gate)

Run before writing anything — a wrap that snapshots state on top of a
known-bad tree writes a confident summary over a lie:

- **YAML guardrail:** `yaml.safe_load` every `attention/*.yaml` this
  session touched (the standing LLM-edit rule, enforced at the exit).
- **Digest frontmatter coherence:** no file with `status: final` and
  `coverage: pending`; no `building` day older than ~5h past its close
  without the report saying so (it means a finalize is owed, not that
  wrap should do it).
- **Stranded receipts:** `git status --short -- provenance/` — the
  publisher writes manifests AFTER the work is committed (AGENTS.md
  §Session close), so untracked `provenance/*.yaml` at wrap time is the
  norm, not an anomaly; they go in step 3's commit. An untracked manifest
  *plus nothing else to commit* means a publish ran after the last commit
  — commit the receipt anyway.
- If anything here fails in a way the session can't explain, **stop and
  report** — don't wrap over it.

### 1 — STATUS.md refresh (anti-rot, the pm/cg rule verbatim)

Only if repo state actually moved this session; a read-only session skips
this and says so.

- **Rewrite the top note from scratch** — read git log since STATUS.md's
  own "As of" date plus today's log.md entries, then write the new top
  note fresh. **Never patch a line inside an existing note**; prior dated
  notes below it are history and stay untouched (this repo's top-note
  stack IS its log rotation).
- **Assert nothing a command computes.** Thread/org/entry counts come
  from `yaml.safe_load(...)` run now, not from memory or the old note.
  Unpushed state is `git log @{u}..`'s job, not a sentence's.
- Update the "*As of YYYY-MM-DD*" line to today.

### 2 — log.md append (AGENTS.md §Session close, step 1)

One dated entry, append-only, in the file's own prose register: what ran,
what surfaced, what changed in `attention/` (with provenance tags), the
friction worth remembering, and **where to pick up** — the pick-up line
is the part the next session's `/start` actually reads, write it for that
reader.

### 3 — commit this repo, receipts included

One commit (or a few scoped ones if the session had distinct arcs),
repo-style message, Co-Authored-By line. The specific trap this step
exists for: **provenance manifests are easy to strand** (⛔ this used to
also name `artifacts/read/index.html` — that internal-read-page output is
retired as of 2026-08-25, see AGENTS.md discipline 8) because they're
written by tools after the "real" work was already committed.
`git status --short` must be empty after this step, except deliberate
proposals (e.g. an uncommitted local skill draft awaiting Ben's word —
name those in the report).

### 4 — site repo state, BEFORE any push decision

Check the site sibling's (`theprojection-site`) working tree. Two different
situations, never conflated:

- **Hand-authored edits** (layouts, css, hand-written content like
  `methodology.md`) → their **own commit with a real message, now**.
  `publish.py --push` commits the whole site tree under an anonymous
  thread-list message — hand-authored work must never ride that commit,
  it becomes unfindable in history.
- **Publish-staged content** (`content/threads/`, `data/*.json`) →
  leave for `/publish`; wrap doesn't publish. If content is staged but
  no publish ran, say so in the report ("staged, unpublished") rather
  than pushing a half-state.

### 5 — push + verify (the load-bearing step; the 17-commit incident is why)

- `git push origin main` on this repo.
- **Verify, never assume:** `git log @{u}..` must print **nothing** on
  BOTH this repo and `theprojection-site`. A clean `git status` is not
  evidence — only the upstream check is (AGENTS.md §Session close).
- **Engine repo (`kestrel`): read-only check, flag-never-push.**
  `git -C kestrel log @{u}..` — unpushed commits there mean its
  resident session missed a push; that's a report flag addressed to Ben,
  and pushing it from here is a write-zone violation even though it
  would "help."
- ⏱ **Timing caveat (root-caused 2026-08-07, from a real incident):**
  `hugo` runs ~2 min and `publish.py --push` ~1–2 min. A chained command
  on the default 120s Bash timeout **got its tail silently killed** — the
  build succeeded and the push never ran, leaving a committed-but-unpushed
  site that looked done. Long site commands get explicit timeouts (≥300s)
  and their own invocation, never the tail of a chain.

### 6 — cross-repo hand-offs, then the report

- If `AGENTS.md`/`CLAUDE.md`/kit-tracked skills changed this session and
  the change should reach the canonical template: **one uncommitted
  brief into `kestrel-ops/INBOX/`** (the `/life:handoff` protocol; dev-shaped
  requests go to the engine's issue tracker instead) —
  write the file, commit it there, touch nothing else.
- **The report** — the wrap card, house style: one-line verdict; a table
  of lanes (daily state · map counts with deltas · publishes today with
  build ids · push state ×3 repos); what's waiting on Ben (unanswered
  candidates, open decisions — each a self-contained ask, never a bare
  label); the obvious next move (`/daily` finalizable at HH:MM, `/week`
  due, etc.); flags (engine repo unpushed, `kit.py sync` dirty — expected
  and correct, say so — dead feeds). Report only — fix nothing from inside
  the report.

## Do not

- Do not push, commit, build, or lint in the **engine repo**
  (`kestrel`) — flag, never fix (write zone, Ben 2026-08-04). The
  brief is the one sanctioned write, and it no longer goes there at all:
  ops briefs go to `kestrel-ops/INBOX/` and **are committed** (that repo is a
  filing cabinet, and an uncommitted brief is a dirty tree the next
  operation may lose); dev-shaped requests go to the issue tracker.
- Do not flip digest frontmatter, edit `attention/` steering files, or
  run a publish from here — name the need, leave it to `/daily`,
  `/steer`, `/publish`.
- Do not patch STATUS.md's top note in place, and do not let counts
  appear in it that a command didn't just compute.
- Do not let hand-authored site edits ride a `publish.py` commit.
- Do not shortcut step 5's `@{u}` checks — a printed "pushed" or a clean
  `git status` is never sufficient proof, on either repo.
- Do not read a wrap as "session over," and never write one that says so.
