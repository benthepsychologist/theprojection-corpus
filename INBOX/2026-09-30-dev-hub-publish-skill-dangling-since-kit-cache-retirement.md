# `.claude/skills/publish` is dangling right now — the next scheduled publish will fail

from:      dev-hub / agent session (found while dispatching ft-09-02)
date:      2026-09-30
kind:      bug
touches:   .claude/skills/publish
done-when: `readlink -f .claude/skills/publish` resolves to a real file, and
  `kestrel fleet link --relink` on this repo reports it `relinked` with 0 dangling
  symlinks remaining.
artifact:  none

Confirmed just now: `.claude/skills/publish` is a dangling symlink, pointing at
`../../../../home/developer/.cache/kestrel/kits/publish-kit/_floating/skills/publish`
— a cache path that no longer exists. On 2026-09-29 the fleet's kit rollout
converted every registered repo's kits (including publish-kit) to plain `path:`
sources with no cache at all, and moved the old cache directory aside
(`~/.cache/kestrel/kits.retired-20260929`). fleet-ops relinked all 18 *registered*
repos as part of that rollout. This repo is unregistered (self-governed,
never in fleet-ops's registry), so it was never swept — its skill link still
points at the now-gone cache path.

This is live and real: the `/daily` skill's routine step 6a calls `/publish
--push`, which resolves through this same dangling link. The next scheduled
publish run (twice daily, `.agents/run.sh daily`) will fail at that step until
this is relinked.

The fix is one command, run from this repo's own root: `kestrel fleet link
--relink`. I did not run it here — self-governed repos are this repo's own
resident agent's territory, and I was only passing through while dispatching an
unrelated spec (`ft-09-02`, publish-kit's Secret Manager work) in a worktree of
this repo, where I fixed the same dangling link locally (that worktree's own
copy only) since my dispatch needed it working. This repo's main checkout still
has the original problem.
