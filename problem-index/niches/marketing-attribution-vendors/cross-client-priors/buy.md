# Hierarchical Modelling Practice

**Niche:** [[niches/marketing-attribution-vendors/cross-client-priors/profile|Cross-Client Priors]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Partial pooling across related units is standard statistical practice for exactly this situation, and measurement vendors fit every client in isolation.
**Tags:** #bayesian-inference #monte-carlo-methods #confidence-intervals #regularization #hypothesis-testing #evaluation-metrics #probability-distributions #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn a portfolio of clients into estimated priors that replace an analyst's judgement — and whoever does that makes every new engagement start from evidence instead of from an assumption.

## The Problem
When you have many related units each with limited data, partial pooling is the standard answer: estimate a population distribution and shrink each unit's estimate toward it by an amount the data determines. It is taught in every applied Bayesian course, implemented in every probabilistic programming framework, and used throughout education research, clinical trials and sports analytics. Measurement vendors have exactly this structure — many clients, each with a short noisy series — and fit each one independently.

## What Already Exists
Hierarchical and multilevel models with partial pooling; empirical Bayes estimation; shrinkage estimators; probabilistic programming frameworks implementing all of it; and cross-validation for hierarchical structures.

## The Customization Gap
The adaptation is to units that are commercial clients with confidentiality expectations. It requires: (1) pooling across entities that have not consented to being pooled, which is a legal and contractual design problem before it is a statistical one — resolving it through abstraction and contract is the work that makes the method usable; (2) a grouping structure that must be discovered, since which businesses are similar is itself an empirical question and the obvious groupings by vertical are frequently wrong; (3) heterogeneity that is the product, because a client wants to know how they differ from the population as much as what the population does; (4) incremental fitting as new clients arrive rather than a single batch estimation; and (5) an interpretation obligation, since shrinking a client's estimate toward a population they cannot see requires explaining why that is better than their own data alone.

## Target Customer
Measurement vendor science teams, large advertisers with many units, and statistical consultancies for whom portfolio pooling is an unclaimed application.

## Impact If Solved
Partial pooling is the textbook answer to many related units with short noisy series, and vendors fit each client alone. Pooling across entities that have not consented is a contractual design problem before a statistical one, and discovering the right grouping is itself an empirical question.
