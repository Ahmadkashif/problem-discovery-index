# Point-in-Time Correctness Left to the Pipeline Author

**Niche:** [[niches/mlops-platforms/training-serving-consistency/profile|Training–Serving Consistency]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Training data is assembled by joining feature tables to labels, and unless every join respects what was knowable at the time, the model is trained on the future and evaluates beautifully.
**Tags:** #data-integration #evaluation-metrics #cross-validation #hypothesis-testing #descriptive-statistics #automation #quick-win #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to prove that the feature values a model sees in production are the values it was trained on — and whoever does that takes the account, because it is the most common expensive failure in applied machine learning and nothing currently detects it.

## The Problem
A churn model joins a customer feature table to a churn label. The feature table holds current values — the customer's current plan, their current support ticket count, their current payment status. The label says whether they churned three months ago. The customer's payment status is now failed because they churned. The model learns that failed payment predicts churn with extraordinary accuracy, evaluates at a number that should have been suspicious, deploys, and predicts nothing, because at prediction time that field has not yet turned. The join was one line of SQL and the leak is invisible in every metric that was computed.

## Why It's Still Broken
Doing the join correctly requires every feature source to be versioned by time and the join to be an as-of join at the label's timestamp, which many warehouses make awkward and many feature tables do not support because they store only current state. The wrong join is simple, fast and produces better numbers, which is the worst possible combination of properties. Nobody checks, because there is nothing to check against — the leak is a property of the assembly code rather than of the data. And a suspiciously good evaluation result is celebrated more often than it is investigated.

## What a Fix Looks Like
Make the correct join the easy one and flag the leak when it happens. Require a timestamp on every feature source and make as-of joins the default construct rather than an advanced option, since the failure originates in the correct thing being harder than the incorrect thing. Detect the signature automatically: a single feature with implausibly high individual predictive power, a sharp performance drop between a random split and a temporal split, and a feature whose value distribution differs between label classes in a way no causal story supports — all three are computable on every training run and none are computed. Compare evaluation under a temporal split against a random split as a standing report, because the gap between them is the most reliable leakage detector available and it costs one extra evaluation. Warn when a feature's own update timestamp postdates the label event, which is the direct mechanical test and catches the common case outright. Record the join semantics in the run metadata so a reviewer can see what was done. And treat an unusually good result as a trigger for review rather than a reason to ship, which is a cultural fix that a platform can support by putting the temporal-split comparison in front of the person celebrating.

## Who Feels the Pain
ML engineers who ship a model that evaluated at ninety and delivers nothing; the business functions who planned on the evaluation number; and the reviewers who have no mechanical way to catch a leak in somebody else's join.

## Impact If Fixed
Comparing a temporal split against a random split costs one extra evaluation and is the most reliable leakage detector available. Making as-of joins the default removes the incentive structure in which the wrong answer is the convenient one.
