# Process Knowledge Transfer for New Shell Lines

**Niche:** [[niches/defense-systems-manufacturers/artillery-ordnance-lap-plants/profile|Artillery & Ordnance Metal Parts and Load-Assemble-Pack Plants]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A new projectile line gets the drawings and the specification but not the process windows the old plant learned over decades, so it spends a year or more finding them by scrap.
**Tags:** #tacit-knowledge-ml #gradient-boosting #cnns #feature-engineering #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn new and modernised artillery lines into accepted lots, and whoever raises the share of projectile bodies and loaded lots accepted on first submission takes the account.

## The Problem
A 155mm projectile body passes through a sequence of metalworking steps and inspections. Each step has qualified windows that experienced operators manage from the plant's records and the last lot's results. The DoD IG found that the Mesquite line could not make metal parts to specification and that it had adapted tooling built for the older M107 rather than the M795. A new line's engineers start without the history that tells them which knobs matter.

## Why Nobody Has Built This
Older plants keep process records on paper or chart recorders, if at all. Process knowledge sits with operators and engineers who never wrote it down, and the plants are government-owned with contractor operators who change by contract award, so nobody owns the long-run record.

## What to Build
A process record per projectile lot at the qualified plants (the plant's process records, inspection results and lot acceptance outcomes), captured digitally with operator adjustments and reasons. Models learn which recorded patterns preceded rejected lots, and the new line's engineers get a library of past lots that looked like theirs, with how they ended.

## Target Customer
Army ammunition programme offices funding new lines, contractor operators of ammunition plants, and the new metal-parts suppliers entering the programme.

## Impact If Built
Each month a new line reaches accepted output sooner adds thousands of projectiles toward a 100,000-a-month goal the Army has already missed (estimate of per-line rates).
