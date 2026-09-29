# Predicting the Number That Matters

**Niche:** [[niches/game-user-acquisition-firms/lifetime-value-prediction/profile|Lifetime Value Prediction]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Billions are bid against a prediction whose mass sits in a tail the prediction cannot see.
**Tags:** #survival-analysis #probability-distributions #gradient-boosting #confidence-intervals #evaluation-metrics #bayesian-inference #revenue-impact #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to predict a cohort's lifetime value from a few days of behaviour when most of that value comes from players who have not spent anything yet — and whoever predicts it better takes the account.

## The Problem
Games revenue is extraordinarily concentrated, and within the top fraction it is concentrated again. Predicted lifetime value is therefore a prediction about a heavy tail, made from a few days of behaviour, for cohorts whose decisive players have done nothing distinguishing yet. Models are trained and evaluated on average error, which rewards predicting the bulk well. The bulk is nearly worthless. The tail is the business, and it is exactly where the model is weakest and nobody measures it.

## Why Nobody Has Built This
Standard modelling practice optimises average error and nobody has re-specified the objective. Tail accuracy is hard to measure with few observations by definition. The models appear to work because bidding systems adapt around them. And the content dependency means even a perfect player model is incomplete.

## What to Build
Predict the distribution rather than the mean, and evaluate on the part that matters. Model the full value distribution per cohort rather than a point expectation, which is the core — the decision depends on the tail and a mean is the one summary that discards it. Evaluate on tail accuracy explicitly, since a model with excellent average error and poor tail behaviour is worse than useless for bidding. Separate the probability of becoming a high-value player from the expected value conditional on it, as those are different problems with different signals. Attach uncertainty to every cohort prediction, because cohort sizes vary enormously and a small cohort's estimate is nearly noise. Calibrate per acquisition source, since sources differ in tail composition far more than in mean. Use the full early behavioural record rather than a handful of aggregate features. Validate against realised long-horizon value continuously rather than at model build. Report where the model is unreliable so bidding can widen its margin there. Incorporate the content dependency explicitly rather than treating it as noise. And make the tail metric the headline the team is measured on, which is the change that reorients everything else.

## Target Customer
Game user acquisition teams and agencies, mobile publishers, attribution and measurement vendors, and bidding platform providers.

## Impact If Built
The decision depends on the tail and the mean is the one summary that discards it, which is what every model is trained to produce. Modelling the distribution and evaluating on tail accuracy reorients the whole optimisation.
