# Downsizing the Standby

**Niche:** [[niches/cloud-cost-management/engineering-facing-optimisation/profile|Engineering-Facing Optimisation]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform generates rightsizing recommendations and engineers ignore them, because the second time a tool suggests downsizing a standby that exists precisely to be idle, the feature is dead.
**Tags:** #gradient-boosting #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #cross-validation #worker-facing #revenue-impact
**Contested on:** Every serious competitor here is fighting to produce a recommendation an engineer will actually act on — specific, safe and verifiably right — and whoever does that takes engineering, because after two bad suggestions the feature is dead permanently.

## The Problem
The tool lists forty recommendations. The first suggests downsizing a database replica that is idle because it is a failover standby. The second suggests deleting a volume that holds a quarterly regulatory extract. The third is correct and would save a meaningful amount. The engineer never reaches the third, because they stopped after the second and concluded that the tool does not understand their systems — which is accurate. The tool's recommendations are derived from processor and memory utilisation, and every one of its errors comes from information it does not have and could obtain.

## Why Nobody Has Built This
Recommendations are generated from infrastructure metrics because that is what the billing and monitoring data provides, and application context — what this resource is for, whether it is a standby, what its failure mode is, what its peak looks like — lives elsewhere and has not been integrated. Coverage has also been treated as the goal, so products compete on the number of recommendations rather than on their precision, which is exactly backwards for an asymmetric loss. And nobody measures whether recommendations are acted on, so the failure is invisible in the vendor's own metrics.

## What to Build
Optimise for precision and say so. Incorporate application context before recommending: redundancy role, whether the resource is part of a failover or standby pair, the load pattern over a full business cycle including quarterly and annual peaks, what depends on it, and resources the utilisation metrics do not cover such as network interfaces, connection limits and file descriptors — since almost every wrong recommendation comes from one of these. Attach an explicit confidence and a safety assessment to each recommendation, and withhold the ones that cannot be assessed, because a shorter trustworthy list is a better product than a comprehensive one. Show the evidence, so an engineer can check the reasoning in ten seconds rather than evaluating a conclusion. Capture rejections with a reason and never repeat a rejected recommendation without new evidence, which is the loop every tool currently omits. Verify accepted recommendations afterwards — did the saving materialise, did anything degrade — which builds the record that makes the next one credible. And move beyond instance sizing to the architectural levers where the money actually is: data transfer patterns, storage class and lifecycle, retry and polling behaviour, and idle non-production environments, which are larger and are addressed by almost nobody.

## Target Customer
Platform engineering teams, cost management vendors whose recommendation feature is unread, and the engineering organisations being asked to reduce spend without usable guidance.

## Impact If Built
Trust is the entire binding constraint and it is destroyed by a small number of confidently wrong suggestions. Application context removes most of those errors, and withholding the unassessable ones is what makes the remaining list worth reading.
