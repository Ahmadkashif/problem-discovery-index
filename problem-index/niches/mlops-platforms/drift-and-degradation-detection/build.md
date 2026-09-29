# The Business Metric Moves Weeks Later

**Niche:** [[niches/mlops-platforms/drift-and-degradation-detection/profile|Drift & Degradation Detection]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A model degrades and the first reliable signal is a business metric moving weeks later, because the thing that matters — whether its decisions are still good — cannot be measured until outcomes arrive.
**Tags:** #change-point-detection #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #survival-analysis #time-series-forecasting #entropy-cross-entropy-kl-divergence
**Contested on:** Every serious competitor in this niche is fighting to tell a model owner that their model has stopped working before a business metric does — and whoever does that takes the account, because that is the question the whole category was bought to answer.

## The Problem
A credit model's outcomes are known at ninety days. A churn model's at thirty. A recommendation model's within hours but only for the items it chose to show. For most of the window in which a model can quietly stop working, the ground truth does not exist. Monitoring products fill the gap with input drift, which fires often and means little, and the organisation learns that the model degraded when someone asks why approvals are down. The measurement everyone wants is unavailable at the time they need it, and the field has largely stopped trying.

## Why Nobody Has Built This
Estimating performance without labels is a genuinely hard research problem and the available methods carry real assumptions that can fail, which makes vendors reluctant to ship an estimate they might have to defend. Drift is easy to compute, always available, and superficially satisfying, so it occupies the space. Outcome data lives in the business systems rather than in the ML platform, and joining it back is an integration nobody owns. And the feedback loop problem — that the model determined which outcomes are observable at all — is well known, statistically awkward, and almost universally ignored.

## What to Build
Estimate performance before the labels arrive and be explicit about the assumptions. Implement label-free performance estimation using confidence-based and distribution-reweighting methods, report the estimate with an interval, and state plainly what it assumes and when it breaks — an honest estimate with stated assumptions is worth far more than a drift chart, and the reluctance to ship one is the reason this space is empty. Reconcile estimates against actual performance as labels arrive, which both calibrates the estimator and demonstrates its trustworthiness over time, and is the thing that earns the model owner's confidence. Handle the feedback loop explicitly: a model that declines an application never learns what would have happened, so the observed outcomes are a biased sample and naive performance monitoring on them is systematically wrong — acknowledging this and correcting for it where possible is a differentiator nobody claims. Distinguish covariate shift from a genuine change in the input-outcome relationship, because the first is frequently harmless and the second always matters, and conflating them is the root of the alert fatigue. Connect back to the training distribution, so the question becomes whether current inputs are inside what the model was fitted on rather than whether they moved. Attribute degradation to specific segments, since aggregate performance holding while a segment collapses is the common and consequential case. And recommend an action — retrain, investigate upstream, accept — with the evidence, because a degradation alert with no next step becomes noise.

## Target Customer
Model owners, the business functions depending on model decisions, monitoring vendors, and the risk functions in regulated industries who must evidence ongoing model performance.

## Impact If Built
The question the category exists for is unanswerable for most of the window in which it matters, and the field substituted an easier one. A label-free estimate with stated assumptions, reconciled against outcomes as they arrive, is the missing product — and handling the feedback loop is the part nobody attempts.
