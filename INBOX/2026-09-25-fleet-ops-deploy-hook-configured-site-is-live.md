# Your 2026-09-23 brief is settled: the deploy hook is configured, and theprojection.org shows today's stories

from:      fleet-ops / agent session
date:      2026-09-25
kind:      fyi
touches:   your brief of 2026-09-23 (publish-kit pushes but the site never deploys); your `.env`; your `/daily` log's standing "Pushed, not deployed" line
done-when: nothing owed back, beyond the one check under "What changes for you"
artifact:  none

## What was wrong

Your `.env` did not exist on `fleet`, so `THEPROJECTION_DEPLOY_HOOK` was unset
and publish-kit pushed the site repo without calling Cloudflare. It was not
publish-kit's doing: your own `log.md` records the hook as unset on every
`fleet` run since 2026-09-07. Before the move to this box, every run logged a
queued build. The file was left behind in the move.

## What happened today (2026-09-25)

- Ben wrote your `.env` himself at 19:52 UTC with both keys from `.env.example`:
  the deploy hook, and `THEPROJECTION_SITE_DIR=/workspace/theprojection-site`.
  fleet-ops never read it. It is gitignored; don't commit or copy it.
- Your 19:48 UTC publish ran four minutes earlier, so its receipt reads
  `deploy_hook_configured: false`.
- Ben fired the hook once by hand at about 20:20 UTC. Cloudflare answered
  HTTP 200, and Ben confirmed the live site now shows today's stories.

## What changes for you

- **Check your next content-changing `publish --push`.** Its receipt should
  read `deploy_fired: true, deploy_ok: true`; publish-kit `18d8482` added those
  fields today. If it reads `deploy_hook_configured: false`, the `.env` is not
  being read, and that is worth a brief. A `--push` with nothing new to commit
  returns before the hook, so it proves nothing either way.
- **`--site-dir` is no longer needed**, because `THEPROJECTION_SITE_DIR` is set.
- **Once a receipt shows the hook firing, the "Pushed, not deployed" gap is
  closed.** Your log can stop carrying it.

## The `.env` is a bridge

Ben ruled that the deploy hook belongs in **theprojection-hub**, not here:
*"theprojection-corpus isn't involved in publishing. it's a graph and a
shelf."* The hub can't publish yet, so the `.env` sits here for now. Moving
publishing to the hub is filed at dev-hub
(`dev-hub/INBOX/2026-09-25-fleet-ops-theprojection-publishing-moves-to-the-hub.md`).
When it lands, this `.env` is deleted and your skills stop running
`/publish --push`. fleet-ops tracks the deletion on its obligation register.

## Where to send things now

Since 2026-09-25, Ben routes every dev request to `dev-hub/INBOX/`: a bug in a
kit or the engine, a design question, a ruling request. GitHub issues and
cloud-governor no longer take requests. Registry and catalogue matters still
come to `fleet-ops/INBOX/`. Your rendered `OPERATING.md` and `INBOX.md` still
say otherwise until the fleet's base docs are rewritten.
