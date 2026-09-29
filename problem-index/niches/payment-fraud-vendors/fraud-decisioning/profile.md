# Fraud Decisioning

**Parent Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Category:** 🔵 High Market Share
**Contested on:** Every serious competitor in this niche is fighting to approve the good transaction and decline the bad one — and the contest splits cleanly enough that it is not terminal.

## Profile
**Market Size:** ~$2.4B US
**Share of Parent Industry:** ~34% of category revenue
**Digital Adoption:** High — sophisticated models, biased evidence
**Target Buyer:** Risk and data leadership
**Automation Potential:** Very High — one half is modelling, the other is evidence

## What Makes This a Distinct Niche
This is the product: decide, in milliseconds, whether to approve a transaction. The modelling is genuinely sophisticated — large ensembles over device fingerprints, behavioural biometrics, network graphs and consortium signals. The evidence it learns from is chargebacks, which exist only for approvals, so the model never sees an outcome for the decisions it was least sure about. The category's largest contest is therefore two: acquiring honest evidence where there is none, and modelling well on whatever evidence exists.

### Contested sub-niches
- [[niches/payment-fraud-vendors/counterfactual-labels/profile|🎯 Counterfactual Label Acquisition]]
- [[niches/payment-fraud-vendors/decision-modelling/profile|🎯 Decision Modelling]]

## Current Tools & Gaps
Ensemble scoring, device and behavioural signals, consortium networks, rules overlays and thresholds. The gaps: no labels in the decline region; accuracy reported on a self-selected population; false declines unmeasured; no experimentation; and evaluation metrics that cannot detect the dominant error.

## Problems
- [[niches/payment-fraud-vendors/fraud-decisioning/build|🔨 Build: Measuring What It Should Have Done]]
- [[niches/payment-fraud-vendors/fraud-decisioning/buy|🛒 Buy: Credit Decisioning's Reject Inference]]
- [[niches/payment-fraud-vendors/fraud-decisioning/fix|🔧 Fix: Accuracy on a Population We Chose]]
