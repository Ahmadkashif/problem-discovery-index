# Measuring What It Should Have Done

**Niche:** [[niches/payment-fraud-vendors/fraud-decisioning/profile|Fraud Decisioning]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every accuracy number in this industry describes a population the model itself selected.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #monte-carlo-methods #revenue-impact #expectation-maximization
**Contested on:** Every serious competitor in this niche is fighting to approve the good transaction and decline the bad one — and the contest splits cleanly enough that it is not terminal.

## The Problem
A transaction is declined. No outcome follows: the merchant never learns whether that customer would have paid, whether they bought elsewhere, or whether they were the fraudster the model believed. Labels arrive only for approvals and only as chargebacks, which are themselves lagged, noisy and partly adversarial. The models are trained on that and evaluated on that, and the dominant commercial error — false declines, estimated to exceed fraud losses across card-not-present commerce — is invisible to every metric the industry reports.

## Why Nobody Has Built This
The fix requires deliberately approving some transactions the model would decline, and that cost is visible, immediate and attributable, while the bias it corrects is invisible and permanent — which is an asymmetry no risk executive is rewarded for accepting. Chargebacks are what merchants contract on, so the incentives point at the measurable half. Nobody wants to publish a false decline rate. And the industry's competitive claims all rest on the biased number.

## What to Build
Buy the evidence and then model on it. Run a small randomised approval allowance on transactions the model would decline, which is the core and is the only way to obtain unbiased labels in the region where the model is weakest. Size the allowance so the cost is bounded and the statistical power is adequate, since the objection is cost and the answer is that a fraction of a percent suffices. Model well on whatever labels exist, which is the other half and is the conventional contest. Estimate the false decline rate directly from the randomised sample, because it is the number the industry has never had and the one merchants most need. Report accuracy on the unbiased sample rather than on the selected population, as that is the claim no competitor can contradict or match. Decompose chargebacks into genuine fraud and other causes, since treating a forgotten subscription as fraud corrupts the label. Use the randomised evidence to recalibrate thresholds, which is where the commercial gain lands. Separate the merchant's loss from the vendor's guarantee exposure, because the optimal threshold differs and the conflict is undisclosed. Offer the experiment as a merchant-level product, since some merchants will gladly pay for the answer. And publish the methodology, because credibility here is the durable asset.

## Target Customer
Risk and data leadership, merchants losing revenue they cannot see, guarantee underwriters pricing exposure, and every competitor whose accuracy claim rests on a selected population.

## Impact If Built
The cost of the experiment is visible and attributable while the bias it corrects is invisible and permanent, which is an asymmetry no risk executive is rewarded for accepting. A small randomised approval allowance is inexpensive and produces the only honest accuracy estimate in the category.
