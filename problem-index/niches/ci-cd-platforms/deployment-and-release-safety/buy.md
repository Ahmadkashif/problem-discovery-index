# Sequential Testing for the Canary Decision

**Niche:** [[niches/ci-cd-platforms/deployment-and-release-safety/profile|Deployment & Release Safety]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Online experimentation solved the problem of deciding as early as possible whether a variant is worse, with sequential methods and proper controls, and canary analysis uses a threshold on an error rate.
**Tags:** #hypothesis-testing #confidence-intervals #bayesian-inference #causal-inference #evaluation-metrics #cross-validation #monte-carlo-methods #automation
**Contested on:** Every serious competitor here is fighting to make a bad release stop itself before most users see it — and whoever does that takes the release account, because the alternative is that a human notices and reacts, which is what happens almost everywhere.

## The Problem
Deciding whether a treatment is worse than a control, as early as possible, while controlling error rates under continuous monitoring, is exactly what sequential experimentation methods were built for, and consumer software companies run thousands of such tests. Canary analysis asks an identical question — is this version worse than the previous one — and is typically answered by comparing an error rate to a fixed number.

## What Already Exists
Sequential and always-valid testing methods that permit continuous monitoring without inflating false positive rates; experimentation platforms with assignment, exposure logging and analysis; variance reduction using pre-period covariates; multiple testing corrections; and canary analysis services from a few large operators with published descriptions of their approach.

## The Customization Gap
The adaptation is to a deployment rather than a product experiment. It requires: (1) traffic assignment that is deployment-aware, since the unit is a request or a session routed to an infrastructure version rather than a user assigned to a variant, and the assignment must be stable enough to avoid mixing versions within a session; (2) a metric set weighted toward harm rather than improvement, because the decision is asymmetric — the cost of shipping a bad release far exceeds the cost of delaying a good one, and the test should be powered accordingly; (3) very short horizons, since the value is in deciding within minutes, which limits sample size and makes variance reduction genuinely important rather than a refinement; (4) multiple metrics with correction, because monitoring twelve signals with independent thresholds produces constant false alarms and is why automatic promotion is distrusted; and (5) an explicit no-decision outcome, since with limited exposure the honest answer is frequently that there is not yet evidence either way, and a system that must choose will choose badly.

## Target Customer
Deployment and progressive delivery vendors, feature flag platforms, site reliability teams, and the experimentation vendors for whom this is an adjacent application.

## Impact If Solved
The statistical machinery for exactly this decision is mature and widely deployed one department over, and release tooling uses a threshold. Asymmetric power and multiple-metric correction are the two adaptations that determine whether teams trust automatic promotion.
