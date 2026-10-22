# Commercial Screening Wired to the Operator's Manoeuvre Planner

**Niche:** [[niches/satellite-operators/conjunction-assessment/profile|Conjunction Assessment & Collision Avoidance]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Screening services check the whole catalogue against the operator's last published orbit; the operator needs them to check its planned orbit, including the burns it has already scheduled.
**Tags:** #monte-carlo-methods #convex-optimization #automation #workflow-orchestration #data-integration
**Contested on:** Every serious competitor in this niche is fighting to tell an operator, before the manoeuvre deadline, which of its conjunction warnings are real, and whoever does it with the fewest false alarms and no missed events takes the operator's screening account.

## The Problem
An operator raising orbit or station-keeping gets warnings computed on a trajectory it will not fly, and misses warnings on the one it will. Analysts re-screen by hand after every planning change.

## What Already Exists
Catalogue-wide screening services from Space-Track, TraCSS and commercial providers (LeoLabs, Slingshot, COMSPOC), which accept operator ephemerides but treat them as one-off uploads.

## The Customization Gap
The adaptation needs: continuous ingestion of the operator's planned ephemerides from its manoeuvre planner, so every plan change triggers a re-screen; candidate-manoeuvre screening that tests several avoidance options against the catalogue at once; operator-specific thresholds, propellant and payload-outage constraints; and de-duplication across providers into one event record.

## Target Customer
Flight dynamics teams at mid-size LEO constellations without Starlink-style in-house autonomy.

## Impact If Solved
Warnings reflect the orbit the satellite will actually fly, avoidance options are pre-screened, and the analyst's time goes to the few real events.
