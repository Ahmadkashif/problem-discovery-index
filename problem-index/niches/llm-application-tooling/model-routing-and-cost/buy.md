# Cascade and Cost-Sensitive Classification

**Niche:** [[niches/llm-application-tooling/model-routing-and-cost/profile|Model Routing & Cost]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cascade classifiers and cost-sensitive learning solved spending more computation only where it is needed, decades ago, and this category runs the expensive model on everything.
**Tags:** #gradient-boosting #logistic-regression #convex-optimization #evaluation-metrics #confidence-intervals #cross-validation #hypothesis-testing #bias-variance-tradeoff
**Contested on:** Every serious competitor in this niche is fighting to send each request to the cheapest model that will answer it well enough — and whoever does that takes the account, because the spread across models is an order of magnitude and the current rule is to ignore it.

## The Problem
Spending cheap computation on easy cases and expensive computation only on hard ones is a classic pattern with a long history — cascades in detection, coarse-to-fine search, anytime algorithms, cost-sensitive learning with explicit misclassification costs. The theory is well developed and the engineering is well understood. This category routes every request through the most capable available model and treats the resulting bill as a fact of nature.

## What Already Exists
Cascade architectures with early exit on confident decisions; cost-sensitive learning with asymmetric error costs; anytime algorithms that improve with more computation; confidence-based abstention and deferral frameworks; and the model selection literature on accuracy-cost trade-offs.

## The Customization Gap
The adaptation is to a cascade whose stages are whole models with no shared confidence scale. It requires: (1) a verification step that decides whether the cheap answer is good enough, since the cheap model's own confidence is poorly calibrated and cannot gate the cascade — designing that check is the central technical problem here and it can frequently be a cheap structural test rather than another model call; (2) cost accounting that includes the wasted cheap call when escalation happens, since a cascade that escalates half the time may cost more than going straight to the expensive model; (3) quality measured per cluster rather than overall, because the cheap model is adequate on some request types and not others and that is exactly the routing signal; (4) latency treated alongside cost, since a cascade adds a round trip and for interactive paths that can outweigh the saving; and (5) continuous re-evaluation, because the models change frequently and a cascade tuned at one point is wrong after the next release.

## Target Customer
Gateway vendors, application teams, and the cost-sensitive learning community for whom this is a large unclaimed application.

## Impact If Solved
Cascades are a decades-old pattern and this category runs the expensive model on everything. The verification step deciding whether a cheap answer suffices is the central design problem, and it is frequently a cheap structural check rather than another model call.
