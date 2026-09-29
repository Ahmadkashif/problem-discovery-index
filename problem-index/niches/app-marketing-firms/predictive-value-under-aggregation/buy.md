# Censored Data Practice

**Niche:** [[niches/app-marketing-firms/predictive-value-under-aggregation/profile|Predictive Value Under Aggregation]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Survival analysis has handled censored, delayed and coarsened observations for a century, and app measurement rebuilt the problem from scratch in 2021.
**Tags:** #survival-analysis #maximum-likelihood-estimation #bayesian-inference #confidence-intervals #monte-carlo-methods #evaluation-metrics #probability-distributions #hypothesis-testing
**Contested on:** This niche is not terminal — designing what the bits encode and predicting value from them are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Observations that are delayed, coarsened into intervals, or censored because a threshold was not met are exactly what survival analysis and related statistical practice were built for. Interval censoring, competing risks, delayed entry and truncation all have established estimators, and the field has a century of experience with data that arrives incomplete for structural reasons. App measurement encountered precisely this in 2021 and largely approached it as a new engineering problem.

## What Already Exists
Interval-censored estimation; delayed entry and truncation handling; competing risks models; likelihood-based inference under coarsening; and established diagnostics for censoring assumptions.

## The Customization Gap
The adaptation is to censoring designed by an adversarial platform and a decision that must be made in hours. It requires: (1) a coarsening scheme the analyst chooses rather than one imposed by nature, which is unique — the practice assumes the coarsening is given and here it is a design variable, which is the first sub-niche and has no statistical precedent; (2) suppression that depends on the campaign's own volume, making the missingness dependent on the very quantity being estimated and therefore not ignorable; (3) deliberate randomised delay, which is known in distribution and can be modelled precisely rather than treated as noise; (4) bidding decisions needed within hours where the practice expects a study; and (5) platform rules that change, so the censoring mechanism itself is non-stationary.

## Target Customer
User acquisition data teams, mobile measurement vendors, and statistical practitioners for whom platform-imposed censoring is an unclaimed application.

## Impact If Solved
A century of practice handles censored and coarsened data and the discipline rebuilt it from scratch. The coarsening being a design variable rather than a given has no statistical precedent, and volume-dependent suppression makes the missingness non-ignorable in exactly the campaigns that matter.
