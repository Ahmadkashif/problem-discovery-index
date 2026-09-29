# Proving the Network Effect

**Niche:** [[niches/payment-fraud-vendors/consortium-signal-sharing/profile|Consortium Signal Sharing]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every vendor's central claim is the network, and none of them can tell a merchant what the network is worth to them specifically.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #causal-inference #hypothesis-testing #revenue-impact #gradient-boosting #compliance
**Contested on:** Every serious competitor in this niche is fighting to make the network signal worth more than the sum of its members' own data — and whoever proves the consortium's marginal contribution can charge for it instead of asserting it.

## The Problem
The pitch is that the consortium sees a fraudster who has hit forty other merchants and stops them at the forty-first. Sometimes that happens. How often, for which merchants, worth how much, and how much faster than the merchant's own data would have caught it are all unmeasured. A merchant choosing between vendors is comparing unquantified network claims, and a vendor investing in the network cannot tell where the return is.

## Why Nobody Has Built This
The network effect is a marketing claim, so measuring it risks producing a number smaller than the claim — and a vendor whose positioning rests on an assertion has a reason not to test it. Marginal contribution requires an ablation nobody runs. Propagation latency is not instrumented. And merchants have no way to demand the measurement because they cannot construct it themselves.

## What to Build
Measure the marginal contribution and speed up propagation. Ablate the consortium features and measure the decision quality difference per merchant segment, which is the core and produces the number the entire category asserts without evidence. Measure propagation latency from first observation at one merchant to protection at the rest, since that is the network's actual mechanism and nobody knows its speed. Report per-merchant network value, because merchants differ enormously in how much they benefit and pricing currently ignores that. Improve propagation deliberately, as reducing the lag from hours to minutes is a concrete product improvement with a measurable effect. Weight contributions by quality, since a merchant contributing noisy labels degrades the network and there is currently no incentive structure. Expire negative signals on a schedule, because a stale blocklist entry is a permanent false decline for a real person. Establish the privacy and consent basis properly, as sharing identity signals across merchants is exactly the practice that attracts scrutiny. Share attack patterns rather than only identifiers, which generalises better and is harder for an attacker to evade. Detect the coordinated campaign across merchants, since that is visible only at the network and is the strongest form of the claim. And publish the methodology, because a proven network effect is the most defensible position in this market.

## Target Customer
Network and data leadership, merchants comparing unquantified claims, consortium participants, and threat intelligence vendors adjacent to the same problem.

## Impact If Built
A vendor whose positioning rests on an assertion has a reason not to test it, so the central claim of the category is unmeasured. An ablation per merchant segment produces the number, and propagation latency turns the claim into an improvable mechanism.
