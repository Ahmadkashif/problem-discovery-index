# Routed on Cost, Judged on Approval

**Niche:** [[niches/payment-processors/routing-and-network-optimisation/profile|Routing & Network Optimisation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The route, network, token and authentication path all change whether a transaction is approved, and they are chosen by cost rules and integration defaults.
**Tags:** #graph-theory #gradient-boosting #convex-optimization #evaluation-metrics #confidence-intervals #revenue-impact #optimization-fundamentals #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to present the transaction in the way most likely to be approved — route, network, token, authentication, data — and whoever does that prevents the declines everybody else is busy retrying.

## The Problem
A transaction can be presented several ways. Routed through a local acquiring entity in the cardholder's country it may approve at a substantially higher rate than the same transaction presented cross-border. Presented with a network token rather than a card number it may approve better and be immune to a credential change. Sent with additional data fields the issuer's model uses, it may clear a risk check it would otherwise fail. These choices are typically made by a least-cost routing rule that optimises the interchange and processing fee, on a transaction where a point of approval rate is worth many times the fee difference.

## Why Nobody Has Built This
Routing was built to manage cost because cost was the historical basis of competition, and the rules never changed when approval performance became the basis instead — the optimisation objective is a decade out of date. Measuring which route approves better requires the settlement join and a willingness to route experimentally. Local acquiring and network agreements are expensive and slow to establish, so the routing options themselves are constrained. And merchants see the fee and not the forgone approval.

## What to Build
Optimise for net value rather than for cost. Model approval probability per available route, network, token status and authentication path for each transaction, which is the core and makes the routing decision a prediction rather than a rule. Compare routes on expected net revenue — approval probability times value minus cost — since the fee difference is usually small relative to a point of approval rate and optimising the smaller term is the error. Randomise deliberately to measure route performance causally, which the processor can do at scale and which is the only way to know rather than infer. Drive token adoption where it demonstrably helps, since the benefit varies and the migration effort should go where the evidence is. Apply authentication selectively by predicted benefit rather than by a blunt threshold, because authentication both improves some approvals and adds friction that loses others. Send the optional data fields that issuers actually use, which is the fix note's subject and is close to free. Invest in local acquiring where the measured approval difference justifies the licence and the operation, which turns a strategic guess into a business case. Report route performance to merchants, since they are judging the processor on the number and cannot currently see what drives it. Maintain the issuer-level view of what works, connecting to the network intelligence niche. And measure the approval rate uplift of the routing layer, since that is the claim and is what a merchant will switch for.

## Target Customer
Processors and platform acquirers competing on approval rate, large cross-border merchants, and the orchestration vendors routing across multiple acquirers.

## Impact If Built
The optimisation objective is a decade out of date — routing manages cost while merchants judge approval, and a point of approval rate outweighs the fee difference many times over. Predicting approval per route and randomising to measure it turns a rule into a demonstrable advantage.
