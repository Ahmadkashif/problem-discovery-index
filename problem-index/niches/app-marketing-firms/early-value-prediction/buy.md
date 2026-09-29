# Time-to-Event Practice

**Niche:** [[niches/app-marketing-firms/early-value-prediction/profile|Early Value Prediction]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Predicting an eventual outcome from early signals under censoring is a solved statistical problem, and app marketing solves it again per team with a gradient booster.
**Tags:** #survival-analysis #maximum-likelihood-estimation #bayesian-inference #confidence-intervals #monte-carlo-methods #evaluation-metrics #gradient-boosting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to predict six-month value from a delayed, coarsened and partly suppressed early signal — and whoever does that accurately bids on better information than everyone else in the auction.

## The Problem
Predicting a long-run outcome from early observations, with censoring and delayed reporting, is standard statistical territory. Survival and time-to-event methods, cumulative incidence estimation, joint models of longitudinal measurements and outcomes, and dynamic prediction that updates as new observations arrive are all established and implemented. Clinical prognosis does exactly this. App marketing frequently approaches the same problem by fitting a regression to whatever features exist and accepting the result.

## What Already Exists
Survival and cumulative incidence models; joint longitudinal-outcome models; dynamic prediction updated with new observations; landmark analysis at fixed horizons; and calibration assessment for time-to-event predictions.

## The Customization Gap
The adaptation is to a cohort-level signal used for a real-time bid. It requires: (1) prediction at cohort rather than individual level, since the signal is aggregated and the unit of decision is a campaign — which changes the estimand and rules out most individual-level survival tooling; (2) an observation that is a coarsened encoding rather than a measurement, so the likelihood must account for the quantisation the schema imposes; (3) suppression dependent on cohort size, which makes the missingness informative and non-ignorable; (4) prediction consumed by a bidding system in near real time, where clinical prediction has a consultation's worth of latency; and (5) a value distribution dominated by a small tail, which makes calibration in the tail far more important than average accuracy and is where standard calibration measures mislead.

## Target Customer
User acquisition data science teams, measurement vendors, and biostatistical practitioners for whom this is an unusually close analogue in an unexpected domain.

## Impact If Solved
Clinical prognosis solves this exact shape and app marketing refits a regression per team. Cohort-level estimands, a quantised observation, and a value distribution dominated by the tail are what the standard toolkit needs adapted.
