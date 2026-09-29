# Predicting a Decision You Rarely See

**Niche:** [[niches/lending-marketplaces/approval-prediction/profile|Approval Prediction]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Outcomes come back only for the borrowers the marketplace already chose to route, which is exactly the data that cannot be modelled naively.
**Tags:** #gradient-boosting #causal-inference #logistic-regression #confidence-intervals #evaluation-metrics #hypothesis-testing #expectation-maximization #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to predict which lender approves this borrower and on what terms, from outcomes that are observed only for the borrowers who were already routed — and whoever handles that censoring best predicts approval for everyone else.

## The Problem
The marketplace wants to know, for a given borrower, which lenders will approve and at what rate. It observes outcomes only where it routed the borrower and the borrower applied, and that routing was done by a model optimising clicks. So the training data is a biased sample twice over, and the naive model learns the past ranking policy rather than the lenders' underwriting. Nobody has framed this as a censored-feedback problem, which means the standard remedies have not been considered.

## Why Nobody Has Built This
The problem was never posed, because approval prediction was assumed impossible without the lender's criteria — the missing data looked like a wall rather than a modelling condition. Selection bias requires an explicit treatment that the data teams, staffed for ranking and acquisition, were not built for. Exploration costs revenue in the short run. And lenders regard their criteria as proprietary, which discourages even asking.

## What to Build
Treat the censoring as the central modelling problem. Model approval per lender per borrower profile with the selection mechanism represented explicitly, which is the core and is the difference between learning underwriting and learning the old ranking. Apply reject inference methods from credit risk, since the discipline solved a structurally identical problem decades ago and the transfer is direct. Introduce deliberate exploration in routing to obtain counterfactual data, because without it the biased sample never improves and the cost is small relative to the information. Predict terms as well as the binary decision, as rate and amount are what determine whether the borrower accepts and are what lenders actually differ on. Use the borrower's return to the marketplace as a weak outcome signal, since reappearing shortly afterward implies the previous route failed. Infer eligibility boundaries empirically rather than relying on published criteria, because the published rules are incomplete and the observed decisions reveal the real ones. Quantify prediction uncertainty, since a confident wrong prediction sends a borrower to a wasted inquiry. Validate against the lenders willing to share, which gives a ground-truth subset to calibrate the rest. Detect when a lender's criteria change, as they do frequently and silently. And report prediction accuracy as the function's metric, which does not currently exist in any form.

## Target Customer
Data and product leadership, lenders receiving better-matched applicants, borrowers whose inquiries are currently wasted, and credit risk vendors whose methods apply directly here.

## Impact If Built
The missing data looked like a wall rather than a modelling condition, so the problem was never posed. Reject inference and deliberate exploration are established remedies for exactly this censoring and have not been tried in this category.
