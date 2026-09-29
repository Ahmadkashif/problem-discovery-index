# Incrementality From Experimental Economics

**Niche:** [[niches/streaming-video-platforms/title-causal-valuation/profile|Title Causal Valuation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Economics and epidemiology built the toolkit for estimating effects from staggered rollouts and natural variation, and streaming has more of both than either field.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #descriptive-statistics #survival-analysis #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to attribute subscribers acquired and retained to the titles that caused them — and whoever produces a number a chief financial officer will defend changes what the industry spends billions on.

## The Problem
Estimating a treatment effect from staggered adoption across regions, from a policy that switched on at different times in different places, or from a withdrawal, is precisely what difference-in-differences, synthetic control and event study methods were built for. Economists apply them to policy changes with far messier data and far smaller samples. Streaming platforms generate staggered rollouts and withdrawals constantly and analyse none of them this way.

## What Already Exists
Difference-in-differences and staggered adoption estimators; synthetic control methods; event study designs; sensitivity analysis for unmeasured confounding; and standards for reporting observational causal claims.

## The Customization Gap
The adaptation is to an individual-level outcome with an adaptive recommender in the middle. It requires: (1) the platform's own recommendation system mediating exposure, so treatment assignment is endogenous in a way policy adoption is not — this is the substantive complication and must be modelled explicitly; (2) individual-level rather than aggregate outcomes, which is a strength and changes the estimator; (3) many titles releasing simultaneously, so effects overlap and must be separated; (4) an outcome that is a subscription decision made at a monthly boundary rather than a continuous variable; and (5) commercial decisions made on the estimate, which raises the evidentiary bar above academic publication.

## Target Customer
Data and finance leadership, content leadership, academic collaborators, and analytics vendors serving media.

## Impact If Solved
The estimators exist and were built for exactly this structure, on worse data. The genuinely new complication is a recommender mediating exposure, which makes treatment assignment endogenous and must be handled rather than ignored.
