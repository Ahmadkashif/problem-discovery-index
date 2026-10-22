# A Covariance Realism Scorecard for Every Data Source

**Niche:** [[niches/satellite-operators/conjunction-assessment/profile|Conjunction Assessment & Collision Avoidance]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A collision probability is only as good as the uncertainty attached to each orbit, and no operator keeps a graded record of how honest each provider's uncertainty has been.
**Tags:** #probability-distributions #maximum-likelihood-estimation #hypothesis-testing #evaluation-metrics #gradient-boosting #automation
**Contested on:** Every serious competitor in this niche is fighting to tell an operator, before the manoeuvre deadline, which of its conjunction warnings are real, and whoever does it with the fewest false alarms and no missed events takes the operator's screening account.

## The Problem
Each conjunction warning carries covariance matrices: the stated uncertainty of each object's position at closest approach. If a provider's covariance is too small, collision probabilities are overstated or understated in unpredictable ways; if too large, every event looks dangerous. Analysts learn by experience which sources and object types to trust and adjust mentally.

## Why Nobody Has Built This
Grading covariance needs later, better tracking of the same objects, joined to the original predictions, which no single operator collects systematically. Providers have little incentive to publish their own calibration. Government screening has historically been free and treated as authoritative.

## What to Build
A scorecard that, for every provider, object class, orbit regime and prediction horizon, compares predicted positions and covariances with later observed positions, tests the statistical consistency of the errors, and outputs correction factors. Each new warning is re-scored with corrected covariance before an analyst sees it.

## Target Customer
Heads of flight dynamics at LEO constellations and their screening providers; regulators assessing screening services.

## Impact If Built
Fewer manoeuvres for phantom risks, fewer missed real ones, and a defensible basis for each decision when the FCC or an insurer asks.
