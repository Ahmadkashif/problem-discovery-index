# Sepsis & Deterioration Prediction Vendors

**Parent Industry:** [[industries/general-hospitals|General Hospitals]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
These vendors sell inpatient early-warning and sepsis prediction models and the surveillance workflows around them. Representative are Epic's own models in the EHR, Bayesian Health (TREWS), Prenosis (its Sepsis ImmunoScore received FDA De Novo marketing authorisation on 3 April 2024, per CNBC) and the developers of nursing-documentation models such as CONCERN (Epic and Bayesian Health named from recall). The Epic Sepsis Model's external validation (AUC 0.63, 67% of sepsis cases missed, alerts on 18% of hospitalisations) and the CONCERN trial (35.6% lower mortality risk) frame the market. Bayesian Health's ML postings on its own board date from December 2024 and October 2025.

## Insight Function
**Size:** ~10-50 data scientists and clinical scientists per vendor (estimate)
**Output:** Model subscriptions, validation studies, regulatory submissions
**Proprietary data:** Client EHR data under business associate agreements; validation cohorts
**Clock:** Hospitals' SEP-1 and VBP performance periods are the client's clock. FDA review timelines apply only to regulated products, so no third party dates the vendor's analysis.
**Buyer:** Chief Medical Officer or Head of Clinical AI at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 3 |
| Q2 Labor mass + repeatable | ×2 | 2 |
| Q3 Proprietary data moat | ×3 | 3 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **32/60** |

**Kill switches:** **HIPAA**, and **FDA computer-system validation**. Training data are client PHI, and models that drive treatment can be regulated as software as a medical device.
**Verdict:** Logged — kill switch. Clinically the most important prediction in the industry and the most regulated, sold as software rather than insight.
