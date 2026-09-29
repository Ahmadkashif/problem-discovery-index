# Approval Prediction

**Parent Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to predict which lender approves this borrower and on what terms, from outcomes that are observed only for the borrowers who were already routed — and whoever handles that censoring best predicts approval for everyone else.

## Profile
**Market Size:** ~$1.0B US
**Share of Parent Industry:** ~17% of category revenue
**Digital Adoption:** Very Low — not attempted
**Target Buyer:** Data and product leadership
**Automation Potential:** Very High — inference under censored feedback

## What Makes This a Distinct Niche
This contest is inference. Given a borrower's profile and whatever outcome data exists, predict each lender's decision and terms. The defining difficulty is that outcomes are observed only where the borrower was routed and applied, which is a selected, non-random subset shaped by the marketplace's own past ranking — the classic censored-feedback problem, in a setting where nobody has even framed it as one. It is modelling, not negotiation.

## Current Tools & Gaps
Eligibility rules, credit band heuristics, and funding notifications where lenders send them. The gaps: no approval model; selection bias unaddressed; terms never predicted; no exploration to obtain counterfactual data; and no measure of prediction quality.

## Problems
- [[niches/lending-marketplaces/approval-prediction/build|🔨 Build: Predicting a Decision You Rarely See]]
- [[niches/lending-marketplaces/approval-prediction/buy|🛒 Buy: Reject Inference From Credit Risk]]
- [[niches/lending-marketplaces/approval-prediction/fix|🔧 Fix: The Funding Notifications Nobody Uses]]
