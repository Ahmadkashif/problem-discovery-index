# Benchmarks That Reward the Wrong Property

**Niche:** [[niches/synthetic-data-providers/generation-platforms/profile|Generation Platforms]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The category is evaluated on statistical similarity to the source, which is easy to score well on and frequently unrelated to whether the data works.
**Tags:** #evaluation-metrics #hypothesis-testing #cross-validation #descriptive-statistics #probability-distributions #confidence-intervals #quick-win
**Contested on:** Not terminal — the contest differs by data modality, and the decomposition is recorded in the profile.

## The Problem
A generator is scored by comparing marginal distributions, pairwise correlations and a discriminator's ability to separate real from synthetic. A model can score well on all three and still produce data on which a downstream model performs badly — because the task depends on a conditional relationship the aggregate comparisons do not test, or on the tail the comparison averages away, or on a constraint that holds in every real record and is violated in a third of the synthetic ones. The metric the field optimises is not the property the buyer needs, and the mismatch is known and unaddressed.

## Why It's Still Broken
Statistical similarity is cheap, universal and comparable across datasets, which is what a benchmark needs to be. Downstream task performance requires a task, which is customer-specific and cannot be standardised into a leaderboard. And the incumbent metrics flatter the category — scores are high, which supports the marketing, and switching to task performance would produce numbers that are worse and honest.

## What a Fix Looks Like
Evaluate on what the data is for. Make train-on-synthetic, test-on-real the headline measure wherever a task can be specified, since it directly answers the buyer's question and the gap between it and the statistical score is the most informative number available. Report conditional and tail fidelity rather than marginal only, because the marginals are the easy part and the failures live in interactions and in the rare regions that carry the signal. Check constraint satisfaction explicitly — rates, dates that must order, totals that must sum — and report the violation rate as a first-class number, since it is trivially computable and is the most common reason a synthetic dataset is unusable in practice. Report per-subgroup utility, because aggregate fidelity routinely conceals that minority segments were smoothed away, which matters for fairness and for the model that has to serve them. Publish the evaluation protocol and let customers run it on their own task. And report the gap between the statistical score and the task score as a standing metric, which is the honest summary of how much the conventional benchmark is telling you.

## Who Feels the Pain
Buyers who adopted a dataset on a good fidelity score and discovered it downstream; the modelling teams who inherit the result; and the vendors whose genuinely better generators cannot differentiate on a metric everyone saturates.

## Impact If Fixed
Constraint violation rates and per-subgroup utility are trivially computable and almost never reported, and both explain failures that the standard fidelity scores rate as successes.
