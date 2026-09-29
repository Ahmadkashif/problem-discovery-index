# Experimentation Platform Practice

**Niche:** [[niches/programmatic-ad-platforms/incrementality-and-budget-allocation/profile|Incrementality & Budget Allocation]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product organisations run thousands of properly powered experiments a year on mature platforms, and advertising runs a lift study when someone asks for one.
**Tags:** #hypothesis-testing #causal-inference #confidence-intervals #evaluation-metrics #monte-carlo-methods #bayesian-inference #descriptive-statistics #automation
**Contested on:** Every serious competitor in this niche is fighting to tell an advertiser what their spend actually caused rather than what it was credited with — and whoever does that decides where the category's budget goes.

## The Problem
Online experimentation is an industrialised discipline. Large product organisations run experiments continuously on platforms that handle assignment, power analysis, sequential testing, variance reduction, interference detection and automated readouts, with statistical guardrails that prevent the common errors. The methods are documented and the tooling is available. Advertising, where the stakes per decision are frequently larger, runs occasional bespoke lift studies designed by whoever is available and often powered to detect nothing.

## What Already Exists
Experimentation platforms with assignment and randomisation; power analysis and sample size planning; sequential testing with valid stopping rules; variance reduction techniques; and interference and network effect detection.

## The Customization Gap
The adaptation is from a product surface the experimenter controls to a media market they do not. It requires: (1) randomisation at geography or audience level rather than at user level, since identity is partial and exposure is not controlled — which weakens power dramatically and makes design far harder than the product case; (2) the treatment being spend rather than a feature, so the dose is continuous and compliance is imperfect, requiring instrumental rather than simple comparisons; (3) outcomes measured in the advertiser's systems with delay, which connects to the outcome feedback niche and rules out the fast readouts product experimentation relies on; (4) interference across channels as the normal case, since a holdout audience still sees the brand elsewhere and the clean isolation product experiments assume does not exist; and (5) a counterparty with an interest in the result, which product experimentation never faces and which makes independence a design requirement rather than a nicety.

## Target Customer
Advertiser measurement teams, independent measurement vendors, demand-side platforms differentiating on honesty, and experimentation vendors for whom media measurement is unserved.

## Impact If Solved
Product experimentation assumes controlled exposure, user-level randomisation and fast readouts, and media has none of the three. Geo-level design with imperfect compliance and cross-channel interference is a harder statistical problem than the one the mature platforms solve.
