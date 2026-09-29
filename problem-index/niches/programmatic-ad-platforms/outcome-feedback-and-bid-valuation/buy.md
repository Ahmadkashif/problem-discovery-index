# Delayed Feedback Practice

**Niche:** [[niches/programmatic-ad-platforms/outcome-feedback-and-bid-valuation/profile|Outcome Feedback & Bid Valuation]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Delayed and censored outcomes are a solved statistical problem with a literature stretching back a century, and programmatic responded by picking a label that arrives immediately.
**Tags:** #survival-analysis #maximum-likelihood-estimation #bayesian-inference #loss-functions #confidence-intervals #evaluation-metrics #gradient-boosting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to join the sale back to the impression that caused it and price the bid against that rather than against a click — and whoever closes that loop changes what every impression in the market is worth.

## The Problem
Outcomes that arrive late, and observations still waiting when you must decide, are the subject of survival analysis — a mature field with well-understood estimators for censoring, competing risks and time-varying covariates, used routinely in clinical trials, credit risk and equipment reliability. Conversion after an impression is textbook right-censored data. Programmatic largely sidestepped the field by changing the question to one whose answer arrives in seconds, and then spent a decade compensating for the substitution.

## What Already Exists
Survival and time-to-event models with censoring; competing risks frameworks; delayed feedback models from the conversion literature; hazard modelling with time-varying covariates; and importance weighting for biased observation windows.

## The Customization Gap
The adaptation is to bid-time inference at auction latency on partial, third-party outcome data. It requires: (1) inference inside a single-digit millisecond budget, which rules out anything requiring a fit at request time and forces the survival structure into a precomputed scoring form — this is the engineering constraint that makes the transfer non-trivial; (2) outcomes observed by a different party at partial coverage, so the model must handle a label that is missing for structural rather than random reasons, which the clinical setting never faces; (3) the decision being a price rather than a prognosis, meaning the quantity needed is an expected discounted value rather than a survival curve; (4) competing risks that are other advertisements, since a conversion may be caused by a different exposure entirely and this is the industry's oldest unresolved confound; and (5) continuous retraining under distribution shift, where the clinical practice assumes a fixed cohort.

## Target Customer
Demand-side platforms and bidder teams, advertiser measurement functions, and the measurement vendors whose attribution products are built on convention rather than estimation.

## Impact If Solved
Conversion after an impression is textbook right-censored data, and the industry changed the question instead of using the method. Pushing survival structure into a precomputed scoring form is the engineering work that makes a century-old literature usable at auction latency.
