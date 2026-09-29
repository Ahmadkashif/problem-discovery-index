# Decline Recovery

**Parent Industry:** [[industries/payment-processors|Payment Processors]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to know which declines are worth retrying, from which issuer, on what schedule — and whoever learns that from settlement outcomes recovers revenue everyone else abandons.

## Profile
**Market Size:** ~$20B US
**Share of Parent Industry:** ~17% of category revenue
**Digital Adoption:** Low — schedules and folklore
**Target Buyer:** Payments product and merchant revenue leadership
**Automation Potential:** Very High — abundant labelled outcomes

## What Makes This a Distinct Niche
Once an issuer has declined, the question is purely about recovery: retry or not, when, how many times, whether to refresh the credential first, whether to change anything about the attempt. This is a prediction problem with abundant labelled data — every retry ever made has a settlement outcome — and it is currently answered by a schedule. It requires no network relationships, no routing infrastructure and no partnership, which is what separates it entirely from preventing the decline in the first place.

## Current Tools & Gaps
Fixed retry schedules, dunning configurations for subscriptions, account updater services, and decline code rules. The gaps: schedules chosen by convention; no per-issuer timing; credential refresh applied indiscriminately or not at all; no learning from settlement outcomes; and retry budgets spent on declines that will never succeed.

## Problems
- [[niches/payment-processors/decline-recovery/build|🔨 Build: Retrying on a Schedule Somebody Chose]]
- [[niches/payment-processors/decline-recovery/buy|🛒 Buy: Collections Timing Practice]]
- [[niches/payment-processors/decline-recovery/fix|🔧 Fix: The Retry That Was Never Going to Work]]
