# Accelerated Underwriting Evidence & Mortality Score Vendors

**Parent Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
Vendors that sell carriers the non-medical and medical evidence behind accelerated underwriting, each with a mortality score on top. Milliman IntelliScript sells prescription histories, up to seven years of medical claims and EHR data with its Irix risk scores. ExamOne sells Rx checks and labs, LexisNexis Risk Solutions and TransUnion sell public-record and credit-based mortality scores, and EHR networks retrieve clinical records. Carriers pay per hit, and the vendors' data science teams build and validate the scores against mortality.

## Insight Function
**Size:** 30-150 data scientists, actuaries and medical staff per vendor (estimate)
**Output:** Per-applicant reports and risk scores; validation studies; rules libraries
**Proprietary data:** Prescription and medical-claims histories licensed from pharmacy benefit managers and clearinghouses, compiled public records and credit data, and years of scores joined to applicants' subsequent deaths
**Clock:** Carriers' annual fairness-testing and governance obligations (New York Circular Letter No. 7; Colorado attestations from 1 December 2024), which land on the vendor's client and come back as evidence requests
**Buyer:** Chief Data Science Officer / Head of Insurance Analytics

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 2 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **43/60** |

**Kill switches:** **compliance gate** — the reports are consumer reports under FCRA, built from health data released under applicants' HIPAA authorisations and licensed from PBMs and clearinghouses with use restrictions. Procurement of anything touching the pipeline runs through FCRA, HIPAA and source-licence review.
**Verdict:** Logged — kill switch. A deep, outcome-labelled corpus whose product is scored per hit by machines rather than produced by analysts, behind the industry's heaviest data-use gates.
