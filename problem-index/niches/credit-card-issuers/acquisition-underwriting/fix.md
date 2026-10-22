# Training on Defaults That Were Fraud

**Niche:** [[niches/credit-card-issuers/acquisition-underwriting/profile|Acquisition & Underwriting Decisioning]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Fix (Pain Point)
**One-liner:** Acquisition models are trained on charge-offs, and a share of those charge-offs were bust-outs and synthetic identities booked as credit loss.
**Tags:** #gradient-boosting #evaluation-metrics #feature-engineering #hypothesis-testing #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to approve, and set the first line for, applicants the bureau file describes poorly — thin files, recent immigrants, near-prime rebuilders — at a loss rate it can predict in advance and explain in an adverse action notice, and whoever does that best takes the account.

## The Problem
The "bad" label in an acquisition model is usually 90+ days delinquent or charged off within 12–24 months. First-party fraud and synthetic identities reach that label through collections, not through the fraud team, so the model learns that some applicant profiles default when in fact they were fraud rings. The profiles most affected — new-to-credit, thin-file, recently arrived — are exactly the segments the issuer wants to grow.

## Why It's Still Broken
Fraud and credit report to different executives and book losses in different lines; collections assigns charge-off reasons for its own purposes; and nobody owns the cross-check.

## What a Fix Looks Like
Before each model rebuild, run the bad-label sample through a first-party-fraud screen — synthetic-identity scores, bust-out signatures, investigator review of a sample — and either exclude confirmed fraud from the credit target or model it separately. Report how many "defaults" changed class.

## Who Feels the Pain
Acquisition modellers whose thin-file models underperform; thin-file applicants declined for a fraud ring's behaviour; fraud teams that never see the losses.

## Impact If Fixed
A cleaner credit target lifts thin-file approval rates at the same true credit loss and gives fraud teams a loss category they can attack.
