# Teardown Findings Predicted Before the Vehicle Arrives

**Niche:** [[niches/defense-systems-manufacturers/combat-vehicle-production-reset/profile|Combat Vehicle Production & Depot Reset]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reset line orders parts on average replacement rates and finds out what a vehicle really needs only after it is stripped to the hull.
**Tags:** #gradient-boosting #survival-analysis #random-forests #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to return vehicles from production and reset on the contracted date, and whoever cuts the share of vehicles held for parts discovered only at teardown takes the account.

## The Problem
Every vehicle inducted for reset has a history (operating hours, miles, deployments, battle damage, prior repairs), but the plan treats each the same. Inspectors find hull cracks, worn suspension, corroded harnesses and damaged components at teardown, and the parts and labour they trigger weren't ordered. Vehicles sit waiting for long-lead parts while the line moves around them.

## Why Nobody Has Built This
Findings are recorded on paper checklists or free-text work orders, so there is no labelled history to learn from. Vehicle histories sit in Army systems the contractor sees only in part, and reset volumes are low enough that nobody has treated forecasting findings as a product.

## What to Build
A findings model trained on digitised teardown records: for each inducted vehicle, predict the probability of each major finding and the parts it would need, from usage, deployment, age, configuration and prior repairs. Feed predicted demand into parts ordering before induction, and update the forecast as inspection proceeds.

## Target Customer
Production managers at vehicle plants and Army depots running reset and upgrade lines, and the contractors that supply their parts.

## Impact If Built
Ordering the most likely long-lead parts before induction could cut the share of vehicles waiting on teardown-found parts by a third or more (estimate) and shorten average reset time by weeks.
