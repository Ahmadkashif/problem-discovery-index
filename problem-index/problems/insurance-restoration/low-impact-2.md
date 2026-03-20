# Equipment Tracking and Deployment Optimization

**Industry:** [[insurance-restoration|Insurance Restoration]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Asset tracking tools can tell you where a dehumidifier is, but they can't tell you that pulling it from Job A (which is 80% dry) to rush-deploy on Job B (a new Category 3 loss) will extend Job A's drying time by 2 days and trigger a carrier SLA violation — while leaving Job C's air scrubber running 3 days past when it was needed.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #optimization-fundamentals #linear-regression #probability-distributions #workflow-orchestration

## The Problem
A mid-size restoration company manages 200-500 pieces of drying equipment (dehumidifiers, air movers, air scrubbers, HEPA vacuums, moisture meters) across 15-40 concurrent jobs. Equipment is the company's largest capital investment after labor. Every piece sitting in the warehouse loses money. Every piece running past necessity on a job wastes energy costs and delays deployment to new jobs. But removing equipment too early extends drying time, risks mold growth, and can result in failed clearance testing. Equipment managers make constant allocation trade-offs with incomplete information — they don't know real-time drying progress on every job, so they either over-deploy (safe but capital-inefficient) or under-deploy (risky and potentially job-extending).

## What Already Exists
GPS and Bluetooth asset trackers (Tile, AirTag, dedicated fleet trackers) provide location. Job management platforms track which equipment is assigned to which job. Drying equipment manufacturers (Dri-Eaz, Phoenix, Legend Brands) offer smart controllers with data logging on some models. No system connects equipment location, job drying progress, and new job requirements into an optimization model.

## The Customisation Gap
A restoration equipment optimization system needs to: (1) track real-time drying progress on each job using moisture readings and equipment runtime data, (2) predict remaining drying time per job based on current conditions, equipment deployed, and building characteristics, (3) recommend optimal equipment allocation across concurrent jobs when new losses arrive — including which existing jobs can safely release equipment earliest, (4) alert when equipment has been running past the point of diminishing returns, and (5) factor in carrier SLA deadlines and clearance testing schedules when recommending equipment moves.

## Impact If Solved
Reduces average equipment idle time from 20-30% to under 10%, effectively increasing fleet capacity by 15-20% without capital expenditure. Eliminates 3-5 unnecessary equipment days per job (at $50-$150/day per unit billing to carrier). Prevents the 10-15% of jobs where premature equipment removal causes drying failures and re-mobilization costs of $2,000-$5,000 per incident.
