# Buying the Missing Half

**Niche:** [[niches/payment-fraud-vendors/counterfactual-labels/profile|Counterfactual Label Acquisition]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A fraction of a percent of deliberately approved declines would produce the only unbiased fraud labels in existence, and essentially nobody runs it.
**Tags:** #causal-inference #hypothesis-testing #monte-carlo-methods #confidence-intervals #evaluation-metrics #revenue-impact #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to obtain honest outcomes for the transactions the model declines — and whoever pays the visible short-term cost of that experiment first can say something about its own accuracy that no competitor can contradict or match.

## The Problem
The decline region has no labels, and no amount of modelling ingenuity creates them. The only way to learn what would have happened is to let some of those transactions through and observe. Every participant in the industry knows this. Almost nobody does it, because approving transactions the model called fraudulent produces losses that appear in a report next month with a name attached, while the bias it removes has never appeared in any report at all.

## Why Nobody Has Built This
The cost is attributable and the benefit is diffuse, which is the structural reason and it is an organisational problem rather than a technical one — nobody is promoted for deliberately approving fraud. Guarantee contracts make the vendor liable for the losses, sharpening the disincentive. Merchants would need to consent. And the absence of any competitor doing it removes the comparison that would force the issue.

## What to Build
Design the experiment so the objection dissolves. Run a continuous randomised approval allowance stratified by score band, which is the core and yields unbiased outcomes exactly where the model is blind. Size it from the statistical power required rather than from intuition, since the volume in this industry means a very small rate suffices and the cost is far lower than anyone assumes. Bound the exposure explicitly by transaction value and merchant, so the downside is known in advance and the objection becomes quantified rather than feared. Share the cost with merchants who want the answer, because many will pay for an honest false decline estimate and that converts a cost centre into a product. Estimate the false decline rate and its confidence interval, which is the deliverable and does not exist anywhere today. Use the labels to retrain in the decline region, as that is where model improvement has been impossible. Recalibrate thresholds on unbiased evidence, which is where the commercial return lands. Run continuously rather than as a one-off, since the adversary moves and a stale estimate misleads. Publish the methodology and the result, because the credibility is the point and cannot be copied quickly. And report the experiment's cost alongside the revenue it recovered, so the asymmetry that blocked it is resolved with numbers.

## Target Customer
Risk executive leadership willing to make a strategic bet, merchants who want to know their lost revenue, guarantee underwriters, and boards evaluating competing vendor claims.

## Impact If Built
The cost is attributable and the benefit is diffuse, so nobody is promoted for deliberately approving fraud. Bounding the exposure and sharing the cost with merchants who want the answer turns the blocked experiment into a product.
