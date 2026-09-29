# Severity Prediction and Complexity Routing at First Notice

**Niche:** [[niches/insurtech-platforms/claims-core-systems/profile|Claims Core Systems]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The reserve set in the first hours of a claim anchors everything that follows and is set from a table, while the carrier holds decades of first notices paired with what the claims eventually cost.
**Tags:** #gradient-boosting #survival-analysis #bayesian-inference #confidence-intervals #evaluation-metrics #cross-validation #revenue-impact #causal-inference
**Contested on:** Every serious competitor in claims systems is fighting to reserve a claim correctly and route it to the right adjuster at first notice — and whoever improves reserve accuracy and cycle time most takes the account.

## The Problem
A first notice of loss arrives with a description, a date, a policy, a location and a few facts. An initial reserve is set from an average for the claim type. The claim is assigned by workload. Three months later it is apparent that this was a complex claim with an injured third party and a likely litigation path, which a more experienced adjuster would have handled differently from the outset and which needed a reserve several times the one that was set. The signals that distinguished it were present in the first notice — the description, the parties, the jurisdiction, the reported injury, the policy characteristics — and the carrier has thousands of prior claims that began the same way and ended expensively.

## Why Nobody Has Built This
Reserving is an actuarial function performed at portfolio level and claims handling is an operational function performed at claim level, and the two have historically not met — individual claim severity prediction sits between them and belongs to neither. There is also a legitimate concern that a predicted reserve becomes an anchor that biases the adjuster and, worse, that a systematically low prediction suppresses reserves in a way that affects financial reporting. That concern is answerable — the prediction informs rather than sets, calibration is monitored, and the actuarial function retains the portfolio view — but it has been treated as a reason not to start.

## What to Build
A severity distribution and a complexity classification at first notice, from the carrier's own history. Features come from the loss description, the parties involved, the jurisdiction, the policy and coverage, the reported injury or damage, and enrichment on the location and the parties. The output is a distribution rather than a point, because the interesting claims are the tail and a point estimate hides exactly what a claims organisation needs to see — a claim with a modest expected value and a fat tail should be handled differently from one with the same expectation and no tail. Routing follows: predicted complexity matched against adjuster experience and current load, with the reasoning shown. Calibration is monitored continuously and reported, and the actuarial organisation is a first-class consumer rather than an afterthought, since a well-calibrated individual severity model improves portfolio reserving as a by-product.

## Target Customer
Carriers and third-party administrators with claims volume, and the claims system vendors whose intake workflows are excellent and whose triage is a rule.

## Impact If Built
Reserve accuracy affects financial reporting, capital and pricing, and first-notice accuracy is where the error is largest. Complexity routing addresses the other half: claims handled by the wrong adjuster develop worse, and the mismatch is currently determined by who was available. Both are measurable against the carrier's own history before anything is deployed.
