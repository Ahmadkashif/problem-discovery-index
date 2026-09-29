# A Return Policy Meets a Payment Schedule

**Niche:** [[niches/bnpl-providers/returns-and-instalment-reconciliation/profile|Returns & Instalment Reconciliation]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The provider sits between a merchant's return policy and a consumer's instalment schedule, and must reconcile two systems that were never designed to talk.
**Tags:** #workflow-orchestration #data-integration #automation #compliance #evaluation-metrics #descriptive-statistics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to reconcile a merchant's return policy with a consumer's instalment schedule — and whoever does that removes the most common and most infuriating failure in the product.

## The Problem
A consumer buys three items on one plan, returns one, and has already made two of four payments. What should happen to the schedule is determinable — the plan reduces, the payments already made partly apply to the returned item, a refund is due or the remaining payments shrink — but the merchant's system issues a refund against an order, the provider's system holds a payment schedule, and neither knows how to express the other's concept. Somebody works it out manually, or the consumer keeps being charged and calls to complain, which is the most common version.

## Why Nobody Has Built This
The merchant's order management system and the provider's instalment ledger were built independently and neither models the other's object — an order line and a payment instalment have no relationship either system can express, and the integration passes a refund amount and a reference. Partial returns are treated as an edge case despite being common. The reconciliation falls on support. And the consumer's complaint is handled as a service issue rather than as a systems gap.

## What to Build
Model the relationship between the order and the schedule. Map instalments to order lines explicitly at plan creation, which is the foundation and is what makes every subsequent adjustment determinable rather than manual. Handle partial returns as a first-class case with a stated rule for how the schedule adjusts, since it is the common case and is currently improvised per instance. Receive refunds at line level from the merchant, which requires an integration change and is the practical enabler. Adjust the schedule automatically and tell the consumer what changed, which is where the complaint currently originates. Handle the timing, since a return processed after a payment was taken requires a refund and one processed before requires a schedule change, and the two are different operations. Model exchanges, which are neither a return nor a purchase and are currently handled as both. Deal with the post-completion return, where the plan has finished and a refund must go somewhere. Reconcile the merchant's settlement against the plan adjustments, since the money has to balance between three parties and currently does so by hand. Define the policy with the merchant at integration, because different merchants will want different treatment and the ambiguity is currently resolved case by case. And measure the return-related contact rate, since it is a large share of support volume and is entirely a systems problem.

## Target Customer
Operations leadership at instalment providers, merchants whose returns create support volume for both parties, and the commerce platforms whose refund model is the constraint.

## Impact If Built
An order line and a payment instalment have no relationship either system can express, so the integration passes an amount and the reconciliation falls on a person. Mapping instalments to order lines at plan creation makes every subsequent adjustment determinable.
