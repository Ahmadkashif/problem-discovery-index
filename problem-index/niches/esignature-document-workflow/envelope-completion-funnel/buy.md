# Survival Analysis Applied to the Agreement Funnel

**Niche:** [[niches/esignature-document-workflow/envelope-completion-funnel/profile|Envelope Completion Funnel]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Time-to-event modelling with censoring is standard statistics with free implementations, and an envelope that has been outstanding for nine days is exactly the object it was built for.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #confidence-intervals #hypothesis-testing #evaluation-metrics #cross-validation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to know why an envelope has stalled while it can still be saved and to act on that reason automatically — and whoever raises completion rate takes the account, because completion is the number the buyer already reports.

## The Problem
The operational question is not whether an envelope will ever complete but whether it will complete in time, and how much probability mass is left given that it has already been outstanding for nine days. That is a hazard question with right-censored observations, which is the canonical setting for survival analysis. The category answers it with a fixed reminder cadence set by a product manager.

## What Already Exists
Survival analysis is mature: proportional hazards models, accelerated failure time models, discrete-time hazard formulations, and survival-aware gradient boosting all have free, well-tested implementations. Competing risks frameworks handle the case where an envelope can complete, be voided, or expire — three distinct terminal events that a binary model conflates. Concordance and time-dependent calibration metrics are standard. Marketing and subscription analytics have used all of this for decades on structurally identical data.

## The Customization Gap
The adaptation is to multi-party sequential events rather than to a single subject. It requires: (1) competing risks rather than a single event, since completion, void and expiry have different drivers and collapsing them loses the distinction that matters; (2) multi-signer structure, because an envelope with four sequential signers is four nested time-to-event problems and the hazard belongs to the current stage rather than to the envelope; (3) time-varying covariates for opens, forwards, reminders and comment activity, which is where the predictive signal actually lives and which a fixed-covariate model discards; (4) calibration as the primary metric rather than discrimination, because the output drives an intervention with a cost — contacting a counterparty — and a poorly calibrated risk score produces either nagging or silence; and (5) intervention effect estimation, since the whole point is to act, and a model that predicts stalls without ever measuring whether the intervention helped will be trusted for a quarter and then ignored.

## Target Customer
Signature platform vendors, revenue operations teams building on platform APIs, and the contract lifecycle vendors whose products sit either side of execution.

## Impact If Solved
The statistical machinery is decades old and free, the data is complete and clean inside every platform, and the application has not been made. Competing risks and time-varying covariates are the two adaptations that separate a useful model from a dashboard, and neither is difficult.
