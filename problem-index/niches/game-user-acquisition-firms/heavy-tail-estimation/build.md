# Finding the Few Who Matter

**Niche:** [[niches/game-user-acquisition-firms/heavy-tail-estimation/profile|Heavy-Tail Estimation]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The players who will produce the revenue are indistinguishable from everyone else on day three.
**Tags:** #probability-distributions #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #maximum-likelihood-estimation #rnns #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to identify, from a few days of behaviour, the small fraction of players who will produce most of a cohort's value — and whoever does it takes the account.

## The Problem
On day three of a cohort's life, the players who will eventually produce most of its revenue have typically spent nothing and behaved much like everyone else. The prediction must nonetheless be made, because bids are set now. This is a rare-event identification problem dressed as a regression problem, and treating it as regression is why the models behave as they do.

## Why Nobody Has Built This
The standard approach works well enough to run a business on. Tail events are rare by definition, so training signal is thin. The behavioural sequence data is available and mostly unused because aggregate features are easier. And nobody has reframed it as a rare-event problem.

## What to Build
Treat it as rare-event identification, not as regression. Model the probability of becoming a high-value player separately from the value conditional on it, which is the core and is what makes the rare event learnable at all. Use the full early behavioural sequence rather than aggregate day-three features, since the order and pacing of early play carries signal that aggregates destroy. Handle extreme class imbalance deliberately with methods designed for it rather than by weighting. Output a distribution per cohort so bidding can reason about upside rather than an expectation. Calibrate the high-value probability, because an uncalibrated rare-event score is worse than a rate. Evaluate on the metrics that matter for rare events — precision at the top, lift in the top percentile — rather than on regression error. Borrow strength across games and sources where the tail behaviour is comparable, which addresses the thin-signal problem. Update predictions as the cohort ages rather than fixing them at day three, since bidding continues. Report which cohorts the model cannot distinguish, which is honest and actionable. And validate against realised long-horizon value continuously, as the tail behaviour drifts with the game.

## Target Customer
UA data science teams and agencies, mobile publishers, bidding platforms, and predictive modelling vendors.

## Impact If Built
This is rare-event identification dressed as regression, and treating it as regression is why the models behave as they do. Separating the become-a-spender event from conditional value makes the rare event learnable.
