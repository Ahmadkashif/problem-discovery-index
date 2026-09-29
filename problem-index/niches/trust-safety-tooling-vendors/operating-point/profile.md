# Operating Point & Threshold Setting

**Parent Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Category:** High Market Share
**Contested on:** Whether the number that decides how much harm is missed and how much legitimate speech is removed is chosen with a framework, or typed into a configuration field.

## Profile

**Market Size:** ~$600M
**Share of Parent Industry:** ~20%
**Digital Adoption:** Very low — a confidence score and a field
**Target Buyer:** Policy and trust & safety leadership, regulators
**Automation Potential:** High for the optimisation, none for the values

## What Makes This a Distinct Niche

A classifier produces a score. Somewhere a number is chosen, and above it content is actioned and below it it is not.

That number is where the consequences live. Set it low and more harmful content is caught and more legitimate posts are removed. Set it high and the reverse. The two errors are not comparable — a missed child safety violation and a wrongly removed political criticism are harms of different kinds — and the balance differs by category, by platform, by community and by jurisdiction.

The product ships a score and a configuration field. The choice is made by the customer, frequently by an engineer, sometimes by whoever set it up, and is then rarely revisited.

So the single most consequential decision in automated moderation is made without a framework, by whoever happened to configure the system, and neither the vendor nor the customer records what considerations went into it.

### Contested sub-niches

- [[niches/trust-safety-tooling-vendors/error-cost-elicitation/profile|🎯 Error Cost Elicitation]]
- [[niches/trust-safety-tooling-vendors/threshold-optimisation/profile|🎯 Threshold Optimisation]]

## Current Tools & Gaps

Confidence scores per classification, configurable thresholds per category, and in better products a tiered arrangement — auto-action above one threshold, human review between, ignore below. Some vendors publish precision-recall curves. Some customers tune thresholds based on reviewer feedback.

The gaps are that nothing supports the decision. No framework exists for stating what the two errors cost, so the threshold is set by feel or by whatever produces a tolerable review volume. Review capacity frequently determines the threshold rather than harm considerations, which means the operating point is an operations constraint wearing a policy costume. Score distributions drift and thresholds do not move. Nothing records why a threshold was set where it was. And the resulting error rates in each direction are rarely measured, so nobody knows where the operating point actually landed.

## Problems

- [[niches/trust-safety-tooling-vendors/operating-point/build|🔨 Build: A Decision, Not a Configuration Field]]
- [[niches/trust-safety-tooling-vendors/operating-point/buy|🛒 Buy: Decision Analysis and Screening Practice]]
- [[niches/trust-safety-tooling-vendors/operating-point/fix|🔧 Fix: The Threshold Is Set by Review Capacity]]
