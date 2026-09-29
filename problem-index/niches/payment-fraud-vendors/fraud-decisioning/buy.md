# Credit Decisioning's Reject Inference

**Niche:** [[niches/payment-fraud-vendors/fraud-decisioning/profile|Fraud Decisioning]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credit lending solved learning from approved-only outcomes decades ago with reject inference and deliberate test approvals, and fraud decisioning never adopted it.
**Tags:** #causal-inference #expectation-maximization #confidence-intervals #evaluation-metrics #hypothesis-testing #logistic-regression #gradient-boosting #compliance
**Contested on:** Every serious competitor in this niche is fighting to approve the good transaction and decline the bad one — and the contest splits cleanly enough that it is not terminal.

## The Problem
Consumer lending faces the identical structure: performance is observed only for approved applicants, so a model trained on them misestimates everyone else. The discipline responded with reject inference, augmentation and parcelling methods, and — crucially — with deliberate approval of a small random sample of marginal applicants to obtain unbiased outcomes. It is standard, documented practice with a regulatory expectation behind it. Fraud decisioning has the same problem and has imported none of it.

## What Already Exists
Reject inference methodologies; through-the-door population modelling; deliberate test-and-learn approval programmes; champion-challenger frameworks; and validation standards for censored outcomes.

## The Customization Gap
The adaptation is to a decision made in milliseconds with an adversary. It requires: (1) an adversary who adapts to the policy, which credit applicants do not do in the same way and which makes a static test sample degrade — this is the substantive difference; (2) outcomes that arrive as chargebacks with a long and variable lag, so the experiment must run continuously rather than as a campaign; (3) the loss falling on the merchant or the guarantor rather than on the modelling party, which means the experiment's cost and benefit sit with different entities; (4) millions of decisions per day, which makes a very small sampling rate statistically sufficient and cheap; and (5) no regulator requiring it, so adoption is a commercial choice rather than a compliance one.

## Target Customer
Risk and data leadership, merchants and guarantors bearing the cost, and credit risk vendors whose methods transfer directly.

## Impact If Solved
The censoring problem is identical and lending's remedies are fifty years old. The only genuinely new complications are an adapting adversary and a cost borne by a different party from the beneficiary.
