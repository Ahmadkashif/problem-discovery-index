# The Holiday Override Nobody Scores

**Niche:** [[niches/armored-car-services/atm-cash-forecasting-replenishment/profile|ATM Cash Forecasting & Replenishment]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Fix (Pain Point)
**One-liner:** Before every long weekend a cash manager adds a margin to dozens of machines on instinct, and nobody checks afterwards whether the instinct was right.
**Tags:** #tacit-knowledge-ml #time-series-forecasting #evaluation-metrics #hypothesis-testing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep each ATM between a cash-out and idle cash with the fewest unscheduled visits, and whoever holds the least cash in machines at the contracted cash-out rate takes the account.

## The Problem
Experienced cash managers know things the model does not: a festival in town, a factory payday moved, a competitor's machine down the street out of service. They override the forecast, usually upwards. Some overrides prevent cash-outs; many just add idle cash. Without a record, the good instincts cannot be taught and the bad ones cannot be dropped.

## Why It's Still Broken
Overrides are typed into an order field with no reason and no later comparison. Forecast accuracy is reported on the model, not on the human adjustment.

## What a Fix Looks Like
Require a reason code with every override, score each override against what the machine actually dispensed, and report each planner's override value monthly. The reasons with a record of paying off become forecast features; the rest are retired.

## Who Feels the Pain
Cash managers whose judgement goes unrecognised; owners paying for idle cash; forecasters whose models are blamed for overrides.

## Impact If Fixed
A few months of logging through one holiday season turns tacit knowledge into measured inputs, and typically shows which override habits cost more cash than they save (estimate).
