# This repo's agent is still told to file ops briefs to kestrel-ops, which is retired and unread

from:      booklet-hub / agent session
date:      2026-09-19
kind:      bug
touches:   ~/.claude/projects/-workspace-theprojection-corpus/memory/project-repo-scope.md (lines 3, 25-61) and its MEMORY.md index line; .claude/skills/wrap/SKILL.md:20,131,148 (rendered)
done-when: This repo's agent, and its unattended /wrap, send an ops brief somewhere that is actually read, never to kestrel-ops. Its project memory no longer instructs it to route there.
artifact:  none

**What changed.** kestrel-ops, the fleet's old operational seat, is
retired. kestrel's own docs (commit `132daa2`, 2026-09-12) call it "the
retired `kestrel-ops` seat" and say never to recreate it as an intake path,
and Ben confirmed the retirement on 2026-09-19. **Nobody reads its inbox.**
Right now it holds 12 unanswered briefs, and 6 of them are from this repo,
filed between 2026-09-03 and 2026-09-11: the news-lane time budget, the RSS
feeds path, cloud-researcher never cloned, GDELT mislens, the world-news
lens unregistered, and the pack news cap dropping sev=major items. fleet-ops has been asked to move every one
of them to its right home, so they are not lost, but they have not been
acted on.

**Why briefs kept going there.** Two things tell this repo's agent to
route there:

1. **Its project memory**, `project-repo-scope.md`, lives outside the repo
   in `~/.claude/projects/-workspace-theprojection-corpus/memory/`. It says
   ops briefs go to `/workspace/kestrel-ops/INBOX/<date>-theprojection-<slug>.md`,
   "committed", and quotes Ben's earlier ruling: *"a mis-directed brief to
   the INBOX in kestrel-ops can get rerouted, so if it's borderline, send it
   there, and kestrel-ops will figure it out."* That ruling rested on
   kestrel-ops having a resident agent. It no longer does. The `MEMORY.md`
   index line repeats it.
2. **The rendered `/wrap` skill** (`.claude/skills/wrap/SKILL.md` lines 20,
   131 and 148) tells the wrap to drop an ops brief into `kestrel-ops/INBOX/`
   and commit it. That text comes from the engine's attention-kind
   template, and cloud-governor has a brief to fix it at the source. **This
   repo is not in the fleet registry, though, so no `fleet sync` will
   re-render it here.** Until someone does, the rendered copy stays wrong,
   and the memory is what keeps the wrap from following it.

**Where briefs go now,** per kestrel's `AGENTS.md` (~line 84):
- operational work goes to the affected repo's own `INBOX/`, or through
  `fleet mail` if it is off-box;
- fleet-wide registry or catalogue work goes to `fleet-ops/INBOX/`;
- a concrete engine bug starts as a kestrel GitHub issue, with the
  implementation landing through cloud-governor.

Several of the stranded briefs describe this repo's own collectors, so some
may simply belong in this repo's own backlog.

**Not in scope:** historical mentions (`log.md`, `STATUS.md` history,
`INBOX/done/`, daily digests) are accurate as history and can stay. The
rendered `OPERATING.md:172` routing row is engine-owned and will be fixed
with the template.
