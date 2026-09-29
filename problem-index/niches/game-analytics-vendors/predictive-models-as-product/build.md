# Scores That Are True of These Players

**Niche:** [[niches/game-analytics-vendors/predictive-models-as-product/profile|Predictive Models as Product]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A generic model's output, in a product interface, with no uncertainty attached, becomes a fact.
**Tags:** #logistic-regression #gradient-boosting #cross-validation #confidence-intervals #evaluation-metrics #survival-analysis #transfer-learning #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to ship churn and lifetime value scores that are actually true of a given studio's players, when the models are fitted generically across a whole customer base — and whoever makes them trustworthy takes the account.

## The Problem
Predictive features are shipped as standard: a churn probability, a predicted lifetime value, a propensity score. They are fitted across a heterogeneous customer base because per-customer fitting is operationally harder. A studio sees a number in a column and uses it to target interventions and to forecast revenue. Nothing in the interface indicates that the model may be poorly calibrated for their game, and nobody has checked whether it is.

## Why Nobody Has Built This
Per-customer model fitting is an infrastructure problem the vendor has not taken on. Uncertainty in a product interface looks like weakness next to a competitor's confident number. Validation against realised outcomes requires a discipline nobody has established. And customers have not asked, because they do not know to.

## What to Build
Fit per customer, calibrate, and show the uncertainty. Fit or fine-tune models per game rather than shipping one model across the customer base, which is the core — a game's mechanics and monetisation determine what predicts churn, and a shared model is wrong in game-specific ways. Calibrate probabilities so a score of eighty percent means eighty percent, since uncalibrated scores are actively misleading when used for targeting. Show uncertainty alongside every score, because a number without it will be treated as a measurement. Validate continuously against realised outcomes and publish the accuracy, which is the only honest basis for a customer to rely on it. Use the cross-customer corpus as a prior for games with thin history, which is where the vendor's position genuinely helps. State plainly what the model was trained on and where it should not be used. Retrain on a schedule as the game changes, since a model fitted at launch is wrong by the second season. Warn when a game's population has drifted from what the model was fitted on. Provide guidance on appropriate use rather than only a column. And degrade gracefully to no score rather than a bad one when the data cannot support it.

## Target Customer
Game analytics vendors, studio data teams, publishers using portfolio forecasts, and machine learning platform vendors.

## Impact If Built
A game's mechanics and monetisation determine what predicts churn, and a shared model is wrong in game-specific ways nobody checks. Per-game fitting with calibration and published accuracy is what makes a score usable.
