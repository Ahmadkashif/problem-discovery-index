# Reject Inference From Credit Risk

**Niche:** [[niches/lending-marketplaces/approval-prediction/profile|Approval Prediction]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credit risk modelling solved learning from approved-only outcomes decades ago, and the marketplace sitting one step upstream has never applied any of it.
**Tags:** #logistic-regression #causal-inference #expectation-maximization #confidence-intervals #evaluation-metrics #hypothesis-testing #gradient-boosting #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to predict which lender approves this borrower and on what terms, from outcomes that are observed only for the borrowers who were already routed — and whoever handles that censoring best predicts approval for everyone else.

## The Problem
Lenders face this exact problem: performance is observed only for applicants they approved, so a naive model trained on that population misestimates risk for everyone else. The discipline developed reject inference, augmentation, parcelling, controlled exploration with deliberately approved marginal applicants, and validation practices around all of it. The marketplace has the identical structure one step upstream and has imported none of it.

## What Already Exists
Reject inference methodologies; through-the-door population modelling; champion-challenger and controlled exploration frameworks; scorecard development with population stability monitoring; and model validation practice for censored outcomes.

## The Customization Gap
The adaptation is to predicting another firm's decision rather than one's own performance. It requires: (1) the target being a counterparty's decision, which changes what auxiliary information is available and is the substantive difference; (2) many lenders with different and changing criteria rather than one policy, so the model is multi-target and the criteria drift independently; (3) the selection mechanism being the marketplace's own ranking rather than an underwriting cutoff, which is at least fully known internally; (4) exploration that costs lead revenue rather than credit losses, changing the economics of acquiring counterfactuals; and (5) fair lending implications when predicting approval probability, which must be designed for rather than discovered.

## Target Customer
Data and product leadership, lender risk teams, compliance functions assessing fair lending, and credit risk vendors for whom the marketplace layer is unentered.

## Impact If Solved
The censoring problem is identical and the remedies are fifty years old. The only genuinely new part is that the target is a counterparty's decision across many changing policies rather than one's own loss experience.
