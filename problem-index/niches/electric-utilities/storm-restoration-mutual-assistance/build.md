# Pre-Landfall Crew Sizing With Uncertainty

**Niche:** [[niches/electric-utilities/storm-restoration-mutual-assistance/profile|Storm Restoration & Mutual Assistance]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The number of mutual-assistance crews a utility requests before a storm is decided by experience on a conference call, and it is never graded against what the storm needed.
**Tags:** #gradient-boosting #random-forests #time-series-forecasting #monte-carlo-methods #evaluation-metrics #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to restore the last customer sooner with fewer crew-days, and whoever stages the right number of crews in the right places before the storm arrives takes the account.

## The Problem
Two to three days before landfall, the storm boss decides how many line and tree crews to request and where to stage them. Request too few and restoration drags for days under public and regulatory pressure. Request too many and the utility pays for idle crews, then faces prudence questions in cost recovery. Neighbouring utilities compete for the same crews, so late requests go unfilled.

## Why Nobody Has Built This
Each utility sees only a few major storms a year, outage prediction research rarely reaches the crew-request decision, and the decision's outcome (crew-days actually used per area) is buried in invoices.

## What to Build
A model that converts weather forecast ensembles, vegetation and asset data into damage and crew-hour distributions per area. It is trained on the utility's storm history plus public cross-utility outage data such as ORNL's EAGLE-I. It recommends a crew request at a chosen risk level, recommends staging sites, updates as forecasts change, and records the final request and actual crew-days so every storm grades the model and the storm boss.

## Target Customer
Emergency preparedness and storm restoration leaders at utilities in hurricane, ice and derecho territory.

## Impact If Built
Restoration ~0.5–1 day faster in a major event for the same cost, or ~10%–20% fewer idle crew-days for the same restoration (estimate), with a documented basis for the request that holds up in prudence review.
