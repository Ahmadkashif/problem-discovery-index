# The Rating Variable Nobody Can Defend in Rate Review

**Niche:** [[niches/property-casualty-insurers/personal-auto-segmentation-rating/profile|Personal Auto Segmentation & Telematics Rating]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Fix (Pain Point)
**One-liner:** A gradient-boosted factor improves the model's lift, then the rate reviewer asks why it rises and falls the way it does, and nobody can say.
**Tags:** #gradient-boosting #regularization #causal-inference #hypothesis-testing #compliance #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to rank drivers by expected loss more finely than the carrier quoting next to them and get that segmentation through state rate review, and whoever keeps its best risks after a rate change without a regulator disapproval takes the account.

## The Problem
Pricing teams increasingly derive rating factors from machine-learned models. The factors can be non-monotonic, depend on interactions and correlate with protected characteristics through geography or credit. Rate reviewers ask for the rationale. Under the NAIC's 2023 AI bulletin and the states that adopted it, they increasingly ask for governance and testing records too.

## Why It's Still Broken
Model documentation is written after the model is built, by people other than its builders, and to the carrier's internal standard rather than a reviewer's questions. Disparate-impact testing, where it exists, is a separate project run late.

## What a Fix Looks Like
Constrain models at build time (monotonicity where intuition demands it, interaction limits), generate factor rationales and stability evidence automatically, run protected-class proxy tests on every candidate variable before it is filed, and keep a ledger of which variables each state has questioned before.

## Who Feels the Pain
Pricing actuaries answering objections, compliance officers facing AI governance exams, and product heads whose rate changes are delayed.

## Impact If Fixed
Fewer disapproved or stripped-down filings, and rating plans whose every variable can be explained when the reviewer asks.
