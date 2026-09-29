# Losing More to Declines Than to Fraud

**Niche:** [[niches/payment-processors/fraud-and-chargeback-decisioning/profile|Fraud & Chargeback Decisioning]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Merchants routinely lose more revenue to declined legitimate orders than to fraud, and only one of the two appears as a loss anywhere in their reporting.
**Tags:** #gradient-boosting #loss-functions #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #causal-inference #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to block the fraudulent transaction without blocking the customer — and whoever balances that properly stops merchants losing more to declined good orders than to fraud.

## The Problem
A merchant's fraud screening declines a percentage of orders. Some were fraudulent. Many were legitimate customers whose order looked unusual — a gift to a different address, a first purchase at an unusual hour, a travelling cardholder. The fraud loss is a number on a report. The declined legitimate revenue is not a number anywhere, because a declined order produces no record of what it would have been worth and no complaint the merchant hears. The screening is therefore tuned against one visible cost and one invisible one, which produces exactly the behaviour that optimisation predicts.

## Why Nobody Has Built This
Fraud loss is measurable and false declines are not, so the objective is written in terms of the measurable one — the asymmetry in visibility produces an asymmetry in the loss function and nobody corrects for it. Merchants are charged back for fraud and are not charged for caution. Screening vendors are judged on fraud caught. And the declined customer simply goes elsewhere.

## What to Build
Balance the two errors with evidence. Estimate the false decline rate and its value, by approving a sample of borderline orders and observing the outcome, which is the fix and is the only way to make the invisible cost visible — it costs a small amount of deliberate fraud exposure and is worth many times that. Write the objective in net revenue rather than in fraud loss, which changes where every threshold should sit and is the reformulation the whole niche turns on. Report both errors to the merchant with their values, since a merchant who sees only their fraud rate will keep tightening. Use the network view, since a cardholder unfamiliar to this merchant may be well known across the processor's book and that is exactly the information that prevents a false decline. Predict chargeback probability rather than fraud in the abstract, because the merchant's actual exposure is the chargeback and the two are not the same. Distinguish the dispute types, since a friendly-fraud chargeback and a stolen-card chargeback need entirely different responses and screening cannot address the first. Feed chargeback outcomes back into screening, which is the labelled data and is frequently not connected. Decide representment from evidence of what wins, which is the fix note's subject. Support graduated responses — step-up authentication, hold for review, partial fulfilment — rather than approve or decline, since the middle is where most of the value is. And report net fraud cost including declines, because a merchant managing one number is not managing the problem.

## Target Customer
Merchant risk teams, processors and fraud vendors competing on net outcome rather than fraud rate, and the customers declined for buying something unusual.

## Impact If Built
The asymmetry in visibility produces an asymmetry in the loss function, and nobody corrects for it. Approving a sample of borderline orders makes the invisible cost measurable, and rewriting the objective in net revenue moves every threshold.
