# Missing Data Practice

**Niche:** [[niches/marketing-attribution-vendors/path-based-attribution/profile|Path-Based Attribution]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistics has a well-developed theory of missing data and what happens when it is missing for a reason, and attribution drops the unobserved touchpoints and divides what remains.
**Tags:** #expectation-maximization #bayesian-inference #confidence-intervals #monte-carlo-methods #hypothesis-testing #evaluation-metrics #probability-distributions #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to say something defensible about journeys that are now mostly unobservable — and whoever handles the missing paths honestly replaces a method that survives on familiarity.

## The Problem
Missing data theory is settled. The distinction between data missing at random and missing for reasons related to what you are measuring is foundational, the consequences of ignoring the difference are well documented, and the methods — multiple imputation, likelihood approaches, selection models, sensitivity analysis over missingness assumptions — are standard and implemented everywhere. Attribution has data that is missing for reasons systematically related to channel, and handles it by analysing complete cases.

## What Already Exists
Multiple imputation with proper uncertainty propagation; likelihood and expectation maximisation approaches; selection models for non-random missingness; sensitivity analysis across missingness assumptions; and complete-case bias diagnostics.

## The Customization Gap
The adaptation is to missingness that is a majority of the data and is caused by adversarial privacy mechanisms. It requires: (1) missingness driven by browser and platform policy rather than by respondent behaviour, so the mechanism is knowable in structure but not in detail — modelling it requires understanding the privacy landscape, which is a domain input the statistical methods do not supply; (2) a missing fraction that is the majority rather than a minority, where imputation becomes extrapolation and bounds are more honest than point estimates; (3) the missing touchpoints correlating with the channels being compared, which is the worst case for complete-case analysis and the reason the current output is systematically rather than randomly wrong; (4) auxiliary information from aggregate methods and experiments, which is unusually strong here and should anchor the imputation; and (5) outputs consumed as point estimates by people who will not accept an interval, which is a presentation constraint rather than a statistical one.

## Target Customer
Measurement vendors, client analytics functions, and statistical practitioners for whom majority-missing behavioural data is an unaddressed application.

## Impact If Solved
The theory is settled and attribution analyses complete cases on data missing for reasons correlated with the channels being compared — the worst case. A majority missing fraction makes bounds more honest than imputation, and aggregate methods provide unusually strong auxiliary anchoring.
