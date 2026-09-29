# Early Lifetime Value Modelling From Subscription

**Niche:** [[niches/mobile-game-publishers/early-signal-modelling/profile|Early Signal Modelling]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Subscription businesses built rigorous early-signal lifetime value models because they had to underwrite acquisition, and publishers use a day-one figure.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #confidence-intervals #bayesian-inference #evaluation-metrics #revenue-impact #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to predict a game's 180-day outcome from its first three days of player behaviour, and whoever makes that prediction reliable enough to act on takes the account.

## The Problem
Subscription and consumer internet businesses solved a close version of this: predicting a cohort's long-run value from its first days, because acquisition spend has to be committed before the value is realised. The methods are mature — hazard models for churn, cohort curve extrapolation with uncertainty, early engagement features, calibration against realised cohorts. Mobile publishers face the identical structure at the concept level and use a single retention percentage.

## What Already Exists
Survival and hazard modelling of churn; cohort curve extrapolation; early engagement feature engineering; predicted lifetime value with intervals; and calibration against realised cohorts.

## The Customization Gap
The adaptation is from predicting a cohort inside a known product to predicting a product from one cohort. It requires: (1) the unit of prediction being the game rather than the user, so there are few labelled examples rather than millions — this inverts the data situation entirely and is the substantive difference; (2) a three-day window rather than a first month, which is far shorter than subscription practice assumes; (3) genre conditioning in place of a single product's known base rates; (4) a paid test audience that is not the eventual audience, which subscription models rarely have to handle; and (5) survivorship in the training set, since the outcomes only exist for concepts that were allowed to continue.

## Target Customer
Mobile publishers, games data science teams, publishing partners, and lifetime value modelling vendors.

## Impact If Solved
Subscription businesses had to underwrite acquisition before value arrived, so they built the models. Predicting the game rather than the user inverts the data situation, and survivorship in the training set is the constraint the borrowed method does not carry.
