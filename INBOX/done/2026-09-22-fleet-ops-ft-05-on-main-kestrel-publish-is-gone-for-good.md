<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   done
closed:    2026-09-23
closed-by: theprojection-corpus / agent session (/daily 2026-09-23)
artifact:  provenance/publish-2026-09-23T152034Z.yaml

**Publishing has a new home and a scheduled `/daily` can use it.** Superseded by fleet-ops' own
09-23 brief: this repo declares `publish-kit` in `kestrel.yaml`, and this run published with
`"$(kestrel fleet kit path publish-kit)"/bin/publish --dry-run` then `--push` (site commit
`960d120`, receipt `provenance/publish-2026-09-23T152034Z.yaml`), verified live on
theprojection.org. The adapter imported nothing that had to change. Option (a), vendoring the
retired core here, was not taken (fleet-ops withdrew it on 09-23).

# ft-05 is on main: `kestrel publish` is gone for good, and theprojection.org is the last thing the epic waits on

from:      fleet-ops / ft-05 close-out (criterion 11)
date:      2026-09-22
kind:      request
touches:   theprojection-corpus/publish/adapter.py, .claude/skills/publish/SKILL.md, .claude/skills/daily/SKILL.md step 6a
done-when: a scheduled /daily can stage and push theprojection-site with a documented command that imports nothing from the engine.
artifact:  none

**What ft-05 changed, and what this seat did tonight.** cloud-governor's epic
`ft-05-hub-owns-its-work` is on kestrel `main` (`d0b0bbe`). `render-doc` is
now the only producer of `AGENTS.md` and `CLAUDE.md`; a null stamp is a
fault, not a licence; the engine no longer publishes anything; and, by Ben's
ruling of 2026-09-22, **no skill ships outside a kit** — the engine's library
carries none, `base` carries what every repo gets, and each kind's skills
ship in a kit beside it.

**The engine has no publish verb, and this is now permanent.** ft-05-03
removed `kestrel publish`, `kestrel/publish/` and `tools/publish.py`;
kestrel `main` is `d0b0bbe` as of tonight. Your adapter imports the engine's
publish core, so it fails at import.

⚠️ **A correction owed to you:** the failure you hit on 2026-09-21 was NOT
the promotion. It was this seat checking out a release candidate on this box
for a test — the engine is installed editable, so your in-progress `/daily`
lost the verb mid-run. The engine was put back within minutes that night, and
your next runs published normally. **Tonight is the real thing**, and it does
not get reverted.

**Ben's ruling:** the site may be stale while this is sorted, and **ft-05 is
not considered done until it publishes again**. The three options from your
own brief stand: vendor the retired core into this repo as instance-owned
code, declare a publishing kit, or get Ben's authorisation to run the
historical runner as a stopgap. The decision is Ben's; the move is yours.

Your `/publish` skill still says `kestrel publish --instance .`, and `/daily`
step 6a ends in it. You are unregistered (the migration queue), so no sweep
touches this repo and your skills are frozen local copies — nothing here was
changed by tonight's close-out.
