# Error Cost Elicitation

**Parent Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Whether a platform will state what it costs to miss a piece of harmful content against what it costs to remove a legitimate one.

## Profile

**Market Size:** ~$360M
**Share of Parent Industry:** ~12%
**Digital Adoption:** Very low — the judgement is never made explicit
**Target Buyer:** Platform policy leadership, regulators, civil society
**Automation Potential:** Low — this is a values judgement

## What Makes This a Distinct Niche

Every threshold encodes an exchange rate between two harms. Leaving harassment up costs something to the person targeted. Removing a post that was not harassment costs something to the person who wrote it. Those costs are of different kinds and the exchange rate between them is a values judgement.

Nobody states it. The judgement is made implicitly, by whoever sets a number, and is never recorded — which means the platform's position on the relative weight of over-removal and under-removal exists only as a configuration value.

This is what separates it from its sibling. [[niches/trust-safety-tooling-vendors/threshold-optimisation/profile|🎯 Threshold Optimisation]] is a computation: given the costs and the score distribution, the optimal cut-off follows, and it can be maintained automatically. Elicitation cannot be computed from anything. It requires a platform to decide, explicitly, how much legitimate speech it accepts removing in order to catch a given amount of harm — and to write it down.

The contest is whether anyone will. The methods for eliciting preferences over incommensurable outcomes are mature and borrowed from decision analysis. The obstacle is that the output is a document stating a platform's values in a form that can be quoted, which is exactly why it does not exist.

## Current Tools & Gaps

Policy documents stating principles in qualitative terms. Category-level severity classifications. Escalation rules for the most serious categories. Regulatory submissions describing a moderation approach. None of it produces a stated exchange rate.

The gaps are total. No platform states the relative cost of the two errors for any category. The affected populations — those harmed by missed content and those wrongly removed — are not consulted. The false positive harm has no measured magnitude, so half the trade has no quantity. Costs are not differentiated by community, though the harm of over-removal falls very unevenly across communities. And nothing records the judgement, so a threshold cannot be reviewed against the values it was supposed to implement.

## Problems

- [[niches/trust-safety-tooling-vendors/error-cost-elicitation/build|🔨 Build: A Stated Exchange Rate]]
- [[niches/trust-safety-tooling-vendors/error-cost-elicitation/buy|🛒 Buy: Preference Elicitation From Decision Science]]
- [[niches/trust-safety-tooling-vendors/error-cost-elicitation/fix|🔧 Fix: Nobody Measures What Over-Removal Costs]]
