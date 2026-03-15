# DIR Fee Exposure Prediction and PBM Contract Optimization

**Industry:** [[pharmacy-independents|Independent Pharmacies]]
**Type:** High Impact
**One-liner:** A pharmacy that can predict its DIR fee exposure by prescription, plan, and quarter — before filling — can make informed decisions about which PBM contracts to accept, which drugs to stock, and when to counsel patients toward cash-pay alternatives that are actually cheaper for the pharmacy.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
DIR fees are the most financially destructive and operationally confusing problem in independent pharmacy today. A pharmacy fills a brand-name prescription, receives an initial reimbursement that appears profitable, and then months later receives a reconciliation statement from the PBM clawing back 6-15% of that reimbursement based on performance metrics the pharmacy has limited control over (patient adherence rates, star ratings, network tiers). The cumulative impact of DIR fees has turned entire PBM network contracts from profitable to loss-generating for many independent pharmacies — but the fees come retroactively, making it impossible to see the problem in real time. Pharmacies are effectively filling prescriptions at an unknown final margin.

## Why It's Unsolved
DIR fees are deliberately opaque — PBMs publish their performance metrics and calculation methodologies only in general terms, not prescription-by-prescription. The retroactive timing means the data needed to build a predictive model (original reimbursement, final net reimbursement after DIR, contributing metrics) exists only in aggregate year-end statements, not in a machine-readable format per claim. Building a model requires assembling this data retrospectively and reverse-engineering the PBM's calculation — which most independent pharmacies lack the technical capacity to do. No PMS vendor has built this because their customer base doesn't have data engineers.

## What a Solution Looks Like
A model trained on a pharmacy's historical claims data — original adjudicated amount, PBM-identified DIR fee per reconciliation period, patient adherence record, plan type, formulary tier, drug category — that predicts the expected net reimbursement per new prescription at fill time, including DIR fee exposure. The output is embedded in the PMS fill workflow: "Expected net margin for this claim: $2.40 (before DIR) → $1.10 (estimated post-DIR). Consider counseling on cash pay alternative: GoodRx cash price = $18, cost to pharmacy = $14, net margin = $4.00." At the contract level, the model aggregates claim-level predictions to show which PBM network contracts are net-loss after DIR — enabling contract renegotiation or termination with data.

## Impact If Solved
Independent pharmacies losing $50,000-200,000 annually to DIR fees they can't see or manage could recapture 20-40% of that through better contract decisions and cash-pay substitution for DIR-vulnerable claims. At scale across 19,000 independent pharmacies, this addresses a $1B+ annual wealth transfer from pharmacies to PBMs.
