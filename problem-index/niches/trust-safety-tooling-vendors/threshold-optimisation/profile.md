# Threshold Optimisation

**Parent Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Whether the operating point is computed from the score distribution and the stated costs, and maintained as both drift.

## Profile

**Market Size:** ~$240M
**Share of Parent Industry:** ~8%
**Digital Adoption:** Very low — a static number
**Target Buyer:** Trust & safety engineering, vendor product teams
**Automation Potential:** Very high — it is a computation

## What Makes This a Distinct Niche

Given what the two errors cost and how the scores are distributed, where the threshold should sit is a computation with a known answer. This is the tractable half.

It is separable from its sibling in the strongest sense. [[niches/trust-safety-tooling-vendors/error-cost-elicitation/profile|🎯 Error Cost Elicitation]] cannot be computed from anything — it requires a platform to state a values judgement and write it down, which is why it does not exist. Optimisation requires only the costs as an input and produces the threshold as an output, maintainable automatically, testable against outcomes.

The contest is drift. A threshold is set once and the world moves underneath it. Content changes. The model is retrained and its scores are differently distributed. A new type of content enters the platform. The same number is now a different operating point, producing different error rates, and nobody notices because the configuration has not changed.

A vendor that maintained the operating point against the stated costs, recomputing as distributions shift, would be selling something no product in the category offers — and it is achievable today for the customers who have stated any costs at all, and approximately even for those who have not.

## Current Tools & Gaps

Confidence scores and configurable thresholds. Precision-recall curves published by some vendors. Tiered thresholds for auto-action, review and ignore. Occasional manual tuning based on reviewer feedback or queue volume.

The gaps are that nothing is maintained. Thresholds are static while score distributions drift, so the operating point moves silently. Model updates change the score scale and the threshold is frequently carried over unchanged, which is a substantial and largely unremarked failure. Precision-recall curves are computed on the vendor's test set rather than on the customer's live distribution. Nothing monitors the realised error rates at the current threshold. And nothing recomputes when anything changes.

## Problems

- [[niches/trust-safety-tooling-vendors/threshold-optimisation/build|🔨 Build: A Maintained Operating Point]]
- [[niches/trust-safety-tooling-vendors/threshold-optimisation/buy|🛒 Buy: Cost-Sensitive Learning and Model Monitoring]]
- [[niches/trust-safety-tooling-vendors/threshold-optimisation/fix|🔧 Fix: The Model Was Retrained and the Threshold Was Not]]
