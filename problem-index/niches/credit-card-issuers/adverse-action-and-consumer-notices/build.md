# Reason Codes Tested for Fidelity to the Model

**Niche:** [[niches/credit-card-issuers/adverse-action-and-consumer-notices/profile|Adverse Action & Regulatory Notices]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Reason codes are mapped to a model when it launches and are never checked again, although retraining, new features and strategy overlays change which factors actually drive a decline.
**Tags:** #gradient-boosting #feature-engineering #hypothesis-testing #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn each model-driven decline, line decrease or rate increase into a notice whose stated reasons are the model's actual reasons and which goes out inside the Reg B and Reg Z clocks, and whoever makes reasons both faithful to the model and defensible to an examiner takes the account.

## The Problem
An adverse action notice lists the top reasons for a decision. With a gradient-boosted model, a strategy overlay and a fraud screen all contributing, the listed reasons can drift from the real drivers without anyone noticing.

## Why Nobody Has Built This
Explainability tools compute attributions; nobody owns the continuous test that compares them with the reasons actually printed, and model risk validates at launch rather than monthly.

## What to Build
A monitor that recomputes attributions for a sample of each month's adverse actions — across the score, strategy rules and overlays — compares them with the reasons sent, flags mismatches and unstable reasons, tests whether reasons are consistent for similar applicants across protected groups, and produces the evidence pack for examiners.

## Target Customer
Model risk and consumer compliance leaders at issuers using machine-learning underwriting or line models.

## Impact If Built
Reasons that stay accurate as models change, with proof on file.
