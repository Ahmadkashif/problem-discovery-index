# Experimental Design and Sequential Testing

**Niche:** [[niches/mlops-platforms/classical-ml-experimentation/profile|Classical ML Experimentation]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistics has two centuries of experimental design and the online experimentation industry has mature sequential testing, and machine learning experimentation uses random search and eyeballing.
**Tags:** #hypothesis-testing #confidence-intervals #bayesian-optimization #gaussian-processes #monte-carlo-methods #evaluation-metrics #cross-validation #probability-distributions
**Contested on:** Every serious competitor in this sub-niche is fighting to make a large population of cheap runs genuinely comparable — so that a team can say what changed, what it was worth, and where the next run should go — and whoever does that takes the account, because comparability is the only thing a tracking tool is bought for at this scale.

## The Problem
The problem of learning the most from a fixed budget of expensive trials is the founding problem of experimental design, with factorial designs, blocking, replication and analysis of variance all built for exactly it. The problem of stopping a trial early without invalidating the inference is solved by sequential testing, deployed at scale by every serious online experimentation platform. Machine learning teams run random search, look at the top of a sorted table, and stop when they are out of time.

## What Already Exists
Factorial and fractional factorial designs with variance decomposition; response surface methodology; sequential and group-sequential testing with valid early stopping; multi-armed bandit allocation; Bayesian optimisation with acquisition functions and multi-fidelity variants; and the experimentation platforms that productised sequential inference for online tests.

## The Customization Gap
The adaptation is to trials whose outcome is noisy for reasons other than sampling. It requires: (1) treating seed variance as a first-class noise source, since the same configuration rerun gives a different number and most ML comparison ignores this entirely — which is where the classical machinery most directly applies and is least used; (2) designs over mixed discrete, continuous and structural factors, because a feature set is not a level on a continuous axis and standard designs assume it is; (3) sequential stopping adapted to a learning curve rather than an accumulating sample, since early stopping in training is a different inference than early stopping in an A/B test and conflating them is a common error; (4) analysing an observational population after the fact, because teams will not run designed experiments and the tooling has to be useful on the runs that actually happened; and (5) reporting effects with intervals rather than rankings, which is a presentation change that would prevent a large share of the wrong conclusions drawn at this scale.

## Target Customer
Data science organisations, tracking and sweep vendors, and the experimentation platform industry for whom this is an adjacent application.

## Impact If Solved
Experimental design was built for exactly this problem and machine learning uses almost none of it. Treating seed variance as a noise source and reporting intervals instead of rankings are both cheap and would prevent most of the wrong conclusions at this scale.
