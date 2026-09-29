# The Corpus That Would Constrain the Claims

**Niche:** [[niches/synthetic-data-providers/generation-corpus-intelligence/profile|Generation Corpus Intelligence]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The category holds thousands of generation runs paired with fidelity and privacy outcomes — the empirical basis for the certification standard it lacks — and nobody has assembled it because the findings would limit what everyone can claim.
**Tags:** #bayesian-optimization #gaussian-processes #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #transfer-learning #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn the accumulated record of generation runs and their outcomes into a certification standard the field lacks — and whoever assembles it defines how the category is judged, which is worth more than any individual product in it.

## The Problem
The question the whole category cannot answer — what utility is actually achievable at what privacy level, for data of this shape — is empirically answerable from data the vendors already hold. Every run logged a configuration, a source profile and a set of evaluation outcomes. Pooled across thousands of runs, that is the frontier: where the trade-off really sits, how it varies by schema shape and column type, which privacy parameters correspond to which measured leakage in practice rather than in the worst case. Nobody has computed it. Each customer is instead told that the trade-off is manageable, on the basis of nothing but the vendor's experience of a handful of similar accounts.

## Why Nobody Has Built This
Publishing the empirical frontier means publishing where your own product sits on it, which is a disclosure no vendor wants to make first. The findings would almost certainly show that meaningful privacy costs more utility than the category's marketing implies, which is uncomfortable for everyone and for the buyers who have already approved releases. Pooling across vendors requires a neutral convener that does not exist. Within a single vendor the run logs are scattered across customer deployments, many of which are on customer infrastructure and contractually out of reach. And nobody's quarterly target depends on it.

## What to Build
Assemble the corpus and publish the picture. Start within one vendor, where the logs are reachable and the value is immediate — the configuration-to-outcome mapping alone improves every future run and is the fix note's subject. Characterise the achievable frontier by data shape, since a customer's most useful question is what is achievable for data like theirs and the corpus answers it directly. Report empirical leakage against formal parameter, which is the single most valuable finding available, because the gap between the theoretical bound and what attacks actually recover is large, well known informally, and never quantified at scale. Build a source-profile-to-configuration recommender, so a new dataset starts near a good operating point rather than after a week of tuning. Track which configurations fail on which structures — relational depth, high cardinality, extreme skew, temporal density — since failure modes are more informative than successes and are currently folklore. Publish as a standard reference and invite contribution, which is the move that makes it a field asset rather than a marketing claim, and which the first mover gets credit for. And accept that the results will constrain the claims, since that is the point: a category whose claims are constrained by evidence is one whose claims can be believed.

## Target Customer
Generation vendors, standards and assurance bodies, regulators developing guidance, and enterprise buyers who currently have no reference for what is achievable.

## Impact If Built
The empirical frontier is computable from logs that already exist and would answer the category's central question. Quantifying the gap between formal privacy parameters and measured leakage is the most valuable finding available, and it is the one nobody wants to publish first.
