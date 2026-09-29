# Seeing Both Sides Before Moving

**Niche:** [[niches/payment-fraud-vendors/the-risk-strategist/profile|The Risk Strategist]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The strategist changes the number that decides millions of transactions and can see the consequence in only one direction.
**Tags:** #causal-inference #monte-carlo-methods #evaluation-metrics #confidence-intervals #revenue-impact #worker-facing #hypothesis-testing #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to let a strategist see both sides of a threshold move before they make it — and whoever gives them that turns a reactive craft into a measured discipline.

## The Problem
A merchant complains about declines, so the strategist loosens. Losses rise, so they tighten. Each move is a guess about a trade-off whose two sides are measured with wildly different precision: fraud losses arrive as chargebacks with a name and a number, while the revenue given up by declining appears nowhere at all. The role is therefore structurally biased toward tightening, and the person doing it knows it and has no evidence to argue otherwise.

## Why Nobody Has Built This
Half the outcome data does not exist, so the tooling was built around the half that does — and a dashboard can only show what is measured, which makes the bias architectural rather than attitudinal. Simulation requires counterfactual estimation nobody attempted. The strategist's work is treated as a craft rather than as a discipline needing instrumentation. And the merchant complaint is the loudest signal in the room.

## What to Build
Give the role a simulator and a cost model. Simulate a proposed threshold or rule change against historical traffic and project both approvals gained and fraud admitted, which is the core and converts a guess into an estimate. Use the randomised approval sample to calibrate the decline side, since that is what makes the projection honest rather than assumed. State an explicit cost per false decline and per fraud loss, because a trade-off cannot be optimised without prices and the prices are currently implicit and asymmetric. Show the merchant's own revenue at stake, as the strategist currently argues fraud rates with someone who cares about revenue. Track every change against its realised outcome, so the role accumulates evidence rather than experience. Model the delay before chargebacks confirm a change, since the feedback lag is what makes rapid iteration misleading. Provide segment-level views, because a global threshold is almost always wrong for some part of the traffic. Support planned policy work rather than only reactive changes, as the calendar is currently set by incidents. Show the distribution of scores near the threshold, which makes the sensitivity of a move visible. And report the portfolio effect of all changes over a period, since individual moves are tracked and their aggregate is not.

## Target Customer
Risk leadership and strategists, merchants negotiating policy, guarantee underwriters, and decision platform vendors whose tooling stops at a threshold control.

## Impact If Built
A dashboard can only show what is measured, which makes the tightening bias architectural rather than attitudinal. Simulation calibrated on a randomised sample gives the role its first view of the side it has never been able to see.
