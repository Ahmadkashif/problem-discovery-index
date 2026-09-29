# Survey Methodology and Psychometrics

**Niche:** [[niches/ai-model-evaluation-firms/human-preference-operations/profile|Human Preference Operations]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Survey research has a century of work on order effects, question framing and sampling, and preference collection reinvented the field's oldest known mistakes.
**Tags:** #hypothesis-testing #confidence-intervals #bayesian-inference #descriptive-statistics #evaluation-metrics #probability-distributions #logistic-regression #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to collect preference ratings that measure the model rather than the presentation — and whoever does that takes the account, because the current ratings are substantially a measurement of length and formatting.

## The Problem
Order effects, acquiescence bias, framing, satisficing and non-representative sampling are the founding subject matter of survey methodology, with established detection and correction procedures and a professional literature. Psychometrics adds validated instrument construction, reliability estimation and differential item functioning. Preference collection at scale rediscovered several of these effects empirically, named them freshly, and adopted few of the remedies.

## What Already Exists
Survey methodology with randomisation and counterbalancing designs, response bias detection, and weighting for non-representative samples; psychometric instrument validation with reliability and validity frameworks; item response theory including models for pairwise comparison; differential item functioning for detecting when a measure behaves differently across subgroups; and paired comparison models with a long statistical history.

## The Customization Gap
The adaptation is to comparisons between long-form generated text at very large volume. It requires: (1) covariate adjustment in the paired comparison model for length and formatting, which is a direct extension of the standard model and is the specific technical fix — the machinery exists and the extension is modest; (2) rater ability and bias modelled jointly with model strength, since raters vary and the standard aggregation treats them as interchangeable; (3) sampling weights toward the population the customer cares about, because the volunteer rater pool is not the user base and nothing currently bridges that; (4) differential functioning analysis to detect where a model is preferred by one subgroup and not another, which is currently invisible and matters enormously for deployment decisions; and (5) satisficing detection adapted to a task where the correct answer is unknown, which is harder than in surveys and where response time and behavioural signals substitute for the usual checks.

## Target Customer
Preference collection operators, leaderboard maintainers, labs, and the survey and psychometrics professions for whom this is a large unclaimed application.

## Impact If Solved
The effects degrading these measurements are survey research's founding subject matter. Covariate adjustment for length and formatting inside the paired comparison model is a modest extension of existing machinery and would change published rankings.
