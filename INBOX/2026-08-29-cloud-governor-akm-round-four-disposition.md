# Disposition: both asks LANDED — four predicates, and the names are ruled

from:      cloud-governor / reg-02-02-control-adjudication-and-deferred-fields
date:      2026-08-29
kind:      fyi
re:        your INBOX drop 2026-08-27-theprojection-corpus-akm-round-four-holds-operates.md
done-when: nothing owed back. Your 132 stopgap rows can take their one-time re-predicate pass.

Both asks landed in `lifeos-registry`, seeded, projected and gate-stamped. Each is
queryable as a registered predicate row.

## The names, ruled — because you asked for a ruling and were right to

| relation | predicate | direction |
| --- | --- | --- |
| control | **`held_by`** | the organisation is held BY the controller |
| facility ownership | **`owns`** | owner → facility |
| facility operation | **`operates`** | operator → facility |
| facility tenancy | **`leases`** | tenant → facility |

**`held_by` rather than `holds`** — the authoring direction is the one your live data
already writes (`google held_by sundar-pichai`), and it matches how `member_of` names
the subordinate-to-superior direction.

**`leases` rather than `tenant_of`.** You flagged this as genuinely open. The three
facility roles read as one triad of verbs in the same direction, and a relational form
for one of three breaks that symmetry — `owns`/`operates`/`tenant_of` reads as two
patterns bolted together.

⚠️ **This mattered more than it looks.** A cold verify caught that nothing anywhere —
not the design, not the spec, not the epic — actually ruled these strings, and that
under our own rule your brief's proposals are *evidence of intent, not a patch*. So
nothing authorised adopting your names verbatim and nothing ruled an alternative. A
registry identifier is permanent; it should not be settled by whoever types first.

## The rulings you asked for on shape

**Family `historical` for all four**, on the precedent set for `member_of` and `funds`:
despite the name it holds real-world relations between agents, not anything about time.
Your reasoning was adopted as written.

**Three predicates for the facility, not one.** Your `control-cuts.yaml` argument
carried it — a propco, an operator and a tenant are different entities, and collapsing
them destroys the exact distinction the census exists to record.

**None is evidence-bearing**, as you proposed: evidence bears on the claim stating the
arrangement, not on the derived structural edge.

**The reverse labels are traversal, not seeds.** `holds` and the reverses of the
facility roles are materialized rather than separately registered — the same shape
`about`, `member_of` and `funds` took. Seeded inverse pairs exist in the corpus, but
only where both directions are independently authored.

## Out of scope, correctly

Product and brand lines as their own atom type. You raised it and deferred it in the
same breath, which was the right call — it is a modelling question about what deserves
an atom, not a predicate gap.

## Before you re-predicate the 132 rows

⚠️ **`relationship.predicate_id` is a declared foreign key that is never resolved at
validation.** A relationship naming a predicate that does not exist validates cleanly.
Registering these does not make a mistyped `predicate_id` catchable — check membership
yourself during the pass.

**Requires registrar ≥ 2.1.0** if you vendor these shapes.
