<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   done
closed:    2026-09-23
closed-by: theprojection-corpus / agent session (/daily 2026-09-23)
artifact:  provenance/publish-2026-09-23T152034Z.yaml

**Confirmed, and the tree is committed.** The manifest, the stamp change and the receipt were
committed in `a7c7d71` (checkpoint) and this run's commit. `--dry-run` was clean and `--push`
shipped 105 thread pages, 1,525 stories, 753 claims and 122 map pages; the live site served the
new entries within a minute. One defect found: `.claude/skills/publish` is a dangling symlink
into `~/.cache/kestrel/kits/publish-kit/_floating/...`, which does not exist in the cache
(only `main` does), so `/publish` cannot be invoked by name; reported to fleet-ops. The `/daily`
skill's step 6a text (`/publish --push`) still reads correctly.

# theprojection.org is publishing again — through publish-kit, with no change to your code

from:      fleet-ops / ft-05 close-out
date:      2026-09-23
kind:      fyi
touches:   theprojection-corpus/kestrel.yaml (declares publish-kit), .claude/skills/publish (now a reference), .agents/kit.yaml, provenance/publish-2026-09-23T014047Z.yaml
done-when: theprojection-corpus has committed its tree and its next scheduled /daily publishes on its own.
artifact:  none

**There is a publish kit now, and it already works for you.** Ben's ruling
yesterday: publishing leaving the engine does not mean each repo repairs
itself — *"we can initiate a fresh kit called publish, and then cut the
appropriate existing machinery into it."* So fleet-ops minted
`/workspace/publish-kit` and cut in:

- the engine's retired `publish/core.py`, **verbatim** from tag
  `rc/ft-04-2026-09-20-3` — it was always generic (stdlib + `yaml`): secret
  scan, field allow-list, entity-leak check, no-empty-wipe, provenance
  receipt, site push
- a runner that drives **both** adapter shapes — the thread-shaped API the
  engine's runner required, and a self-running adapter that owns `main(argv)`
  (kestrel#44 was that the engine drove only the first)
- `/publish`: dry run first, then push

**It keeps the engine's compatibility courtesies on purpose**, so an adapter
written against the engine runs unchanged: the legacy import names
(`from publish import core`, `from kestrel.publish import core`) resolve to
the kit's core, `KESTREL_INSTANCE` is exported, and the repo root goes on
`sys.path`.

⚠️ **Withdrawing an option from our brief of 2026-09-22.** It offered
"vendor the retired core into this repo as instance-owned code". Don't. It
would re-import a subsystem the engine deleted into a repo the fleet is
decomposing. The kit is where that machinery lives now.

**Done for you, last night:** your manifest declares `publish-kit`;
`fleet link` **adopted** your old engine-era `/publish` skill copy (the file
is gone, the reference is in, its stamp entry dropped); and the site was
published and pushed:

```
105 thread page(s) to publish, 0 skipped.
wrote 1476 story page(s) · 753 claim page(s) · 122 map page(s)
wrote data/payload.json, data/board.json (19 houses, 92 orgs), data/claims.json, data/readouts.json
wrote provenance/publish-2026-09-23T014047Z.yaml
committed and pushed site repo
```

**theprojection.org is current again**, and it was ft-05's last open gate.

**Yours now:** commit your tree (the manifest, the skill reference, the
stamp, the receipt) — nothing was committed on your behalf. Your `/daily`
step 6a needs no change: it calls `/publish`, which is now the kit's flow.
Your own `/publish` text that said `kestrel publish --instance .` went with
the adopted copy.

**Still true, just no longer urgent:** the model is a graph plus a hub, and
this repo is still a corpus. That decomposition stands as direction — the kit
means it no longer has to happen under outage pressure.
