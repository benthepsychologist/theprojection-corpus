# research/PRINCIPLES.md — durable schema-design principles

This file holds standing design principles for every schema under `research/`
(q1, q2, q3, and anything added later) — the kind of rule that should govern
future field design, not just fix one past mistake. It is separate from
`INBOX/2026-08-03-q1-skeleton-v3.md`'s rulings register (R-01–R-20): that
file is a frozen historical record of a specific design review and is not
edited going forward (see `research/README.md`). This file is the living
home for principles distilled FROM rulings, numbered independently (P-01,
P-02, ...) so it can keep growing as this program does.

A ruling (R-nn) records a specific decision Ben made, with its own date and
context. A principle (P-nn) is the general rule a ruling revealed —
something any future schema change in this program should check itself
against, not just the one field that prompted it.

---

## P-01 — a schema field must match the real-world cardinality of what it represents

**The rule:** never force a single-value field onto something that can
genuinely have multiple values in the world — co-leads, joint owners, shared
credit, multiple lenders, whatever the real structure is. When a schema
field turns out to be too narrow for a real case, extend the field's
cardinality (make it a list, add a repeatable sub-record, etc.); never pick
one value and silently drop the rest to make the record fit the field as
originally written.

**Why this is a principle and not just a bug fix:** a schema is a claim
about the shape of the world. When the world produces a case the schema
can't represent, the world is right and the schema is wrong — the fix is
always to widen the schema, never to distort the fact to fit it. Silently
picking one value out of several loses information permanently unless
someone happens to remember to go back and check; recording the narrowing
explicitly (as pass 2 did) at least flags the loss, but flagging a known
defect is still worse than not having the defect.

**Where this was ruled (worked example):** q1's round-node schema
(`research/q1-flows/nodes.yaml`, `kind: round`) originally gave each
financing round exactly one `lead` field — a single nullable investor-node
id. Cohere's 2025 round was reported as co-led by Radical Ventures AND
Inovia. The single-slot field couldn't hold both, so pass 2 picked Radical
Ventures (listed first in the source) as `lead` and recorded Inovia as a
demoted `participant` — a judgment call, explicitly flagged for Ben rather
than silently made, but still a real loss of a real fact (Inovia was
reported as a co-lead, not a lesser participant). The same defect recurred
independently in the same pass on Together AI's 2025 Series B round
(General Catalyst AND Prosperity7, both reported as co-leads).

Ben's ruling (2026-08-10, verbatim): *"The schema shouldn't have 1 lead
slot then. schemas can't conflict with the world. Add that in as a
principle somewhere."*

**The fix applied:** `lead` (nullable, single id) became `leads` (a list —
empty when no lead is disclosed, one entry for an ordinary single-lead
round, two or more for a genuine co-lead). `memberships.yaml`'s `role`
field changed to match: any number of `is_member_of` rows may carry
`role: lead` on the same round, one per name a source actually calls a
lead — never capped at one to satisfy the old field shape. Both flagged
cases (Cohere 2025, Together AI 2025 Series B) were corrected to record
every named co-lead as `role: lead`.

**How to apply this principle going forward:** before shipping any new
schema field anywhere in `research/` (q1, q2, q3, or later), ask whether
the real-world thing it represents can legitimately have more than one of
whatever the field holds — co-owners, joint operators, shared attribution,
multiple simultaneous values of any kind. If yes, the field's cardinality
must accommodate that from the start; retrofitting it later (as happened
here) is strictly worse than designing it right the first time, because
every record written under the too-narrow version has already silently
lost information by the time the retrofit happens.
