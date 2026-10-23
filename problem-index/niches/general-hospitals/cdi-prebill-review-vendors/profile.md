# Clinical Documentation Integrity & Pre-Bill Review Vendors

**Parent Industry:** [[industries/general-hospitals|General Hospitals]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
These vendors sell CDI software, AI pre-bill clinical review and CDI programme services that find documentation gaps and missed severity before inpatient claims drop. Representative are Solventum 360 Encompass, Microsoft/Nuance CDE and Iodine Software (named from recall); SmarterDx (Smarter Technologies), which serves 85 health-system clients across 300+ hospital sites (Becker's, 2026, company-reported); AKASA, whose posting says its customers represent 1 in 10 US inpatient discharges (self-reported); and consulting firms. Some price per finding or on recovered revenue, others by subscription. Provider-side coding auditors are already logged as [[niches/medical-billing/coding-audit-compliance-firms/profile|🔍 Coding Audit & Compliance Firms]] (46, kill switch), and the payer's DRG validation side as [[niches/health-insurance-carriers/payment-integrity-vendors/profile|🔍 Outsourced Payment Integrity Vendors]] (51, kill switch).

## Insight Function
**Size:** ~30-200 clinical data scientists, CDI content and rules experts, and audit-outcome analysts per vendor (estimate). CDI specialists, coders and physician reviewers working cases one by one are production and are excluded.
**Output:** Query opportunities and pre-bill findings with DRG impact; CDI programme benchmarks; payer-audit defence content
**Proprietary data:** Cross-client records of which queries physicians answered, which DRG shifts held and which payers reversed them, held on client charts
**Clock:** Claim-drop timing is set by the hospital, which makes it a client clock. Payer DRG-validation audit and appeal windows bind only the disputed cases. MS-DRG weights reset each 1 October in the IPPS final rule.
**Buyer:** Chief Clinical Officer or Head of Data Science at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 4 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 4 |
| **Weighted total** | | **46/60** |

**Kill switches:** **HIPAA**, and **data isn't theirs**. Every finding is computed on client hospitals' identified charts under business associate agreements. Scored consistently with the coding-audit and payment-integrity pockets linked above.
**Verdict:** Logged — kill switch. The best cross-hospital record of which documented severity survives payer audit sits entirely on client PHI. These vendors are the main place an engineer would build this work, through AKASA's live forward-deployed role (see the industry's agents note).
