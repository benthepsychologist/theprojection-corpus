# Epoch AI — AI Data Centers dataset (diffable-source snapshot)

source:   https://epoch.ai/data/data-centers
files:    data_centers.csv · data_center_timelines.csv
          (also published: data_center_chillers.csv, data_center_cooling_towers.csv — not snapshotted here)
license:  CC-BY (Creative Commons Attribution) — confirmed on the hub 2026-08-03
fetched:  2026-08-03 (curl, verified cell-by-cell — see INBOX/sotg synthesis)
snapshot: data_centers.2026-08-03.csv (75 facilities, 12,048 MW, 12.87M H100e, 15 owners)
          data_center_timelines.2026-08-03.csv (433 quarterly records)

why here: this is the AI-datacenter census q3 was going to build from
scratch; the state-of-the-game sweep (2026-08-03) found it already IS
~80% of that census, free. Adopted as a `diffable` source per the repo's
perishability rule — snapshot kept for deltas, re-fetch on demand; NEVER
canonicalized (AGENTS.md discipline 1). Owner/user fields carry inline
`#confident`/`#likely` tags that map onto the reliability model; the
timelines give thrust-as-derivative; the published uncertainty bands are
the R-20 error-bar reporting style.

⚠️ import as a source to VERIFY and reconcile, never as truth to copy —
same discipline as the step-0 audit. The value this repo adds is the
owner/operator/propco/tenant attribution and the control cuts Epoch does
NOT model, not the facility list Epoch already maintains.
