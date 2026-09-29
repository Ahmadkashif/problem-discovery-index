# Cost-Sensitive Classification Practice

**Niche:** [[niches/payment-processors/fraud-and-chargeback-decisioning/profile|Fraud & Chargeback Decisioning]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine learning has handled asymmetric misclassification costs since its beginnings, and fraud screening optimises one side of the trade-off because the other side has no number.
**Tags:** #loss-functions #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #logistic-regression #optimization-fundamentals #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to block the fraudulent transaction without blocking the customer — and whoever balances that properly stops merchants losing more to declined good orders than to fraud.

## The Problem
Classification with asymmetric costs is elementary. Cost-sensitive learning, threshold selection against an explicit cost matrix, expected-cost minimisation and calibrated probability estimates are all standard and taught everywhere. The method is unambiguous once both costs are known. Fraud screening applies it with one cost populated and the other left at an implicit zero, not because the practitioners do not know better but because nobody has estimated what a false decline costs.

## What Already Exists
Cost-sensitive learning and threshold optimisation; calibrated probability estimation; expected cost minimisation; cost matrix specification; and evaluation under class imbalance.

## The Customization Gap
The adaptation is to a cost that must be estimated experimentally rather than looked up. It requires: (1) the false positive cost being unobservable without deliberate exploration, since a declined order's value and the customer's lifetime response are both counterfactual — designing that exploration is the substantive work and the method is useless without it; (2) costs that vary per merchant, per order and per customer, so the cost matrix is a model rather than a constant; (3) a long-run component, since a declined customer may never return, which makes the cost larger than the order value and is routinely omitted; (4) an adversary who moves in response, so the optimal threshold is not stationary; and (5) the party bearing the cost being the merchant while the threshold is frequently set by a vendor optimising fraud caught.

## Target Customer
Merchant risk teams, fraud vendors, and machine learning practitioners for whom the missing cost estimate is the interesting part of an otherwise standard problem.

## Impact If Solved
The method is elementary once both costs are known and the industry runs it with one cost set to an implicit zero. Designing the exploration that estimates the false decline cost is the substantive work, and the long-run loss of a declined customer is routinely omitted even when it is estimated.
