# Outsourced Payment Integrity Vendors

**Parent Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Firms that find claims a plan should not have paid, or should not pay: Cotiviti, Optum's payment integrity business, Zelis, Machinify, Performant and Gainwell's HMS unit are representative (named from recall). They develop audit "concepts" (clinical and coding logic that identifies overpayment patterns), run pre-payment clinical and coding edits, DRG and itemised-bill reviews, coordination-of-benefits and subrogation recovery, and post-payment data-mining audits. Plans usually pay a contingency share of savings, ~10%–30% (estimate). The plan's in-house payment integrity and medical policy function is already logged as [[niches/medical-billing/payer-claims-adjudication/profile|🔍 Payer Claims Adjudication & Policy]] (51, kill switch).

## Insight Function
**Size:** 50-400 concept developers, data scientists, clinical policy analysts and audit strategists per major vendor (estimate), excluding coders and nurse auditors, who are production staff
**Output:** Overpayment findings and pre-pay edit decisions billed as contingency savings; new audit concepts; provider dispute files
**Proprietary data:** A library of audit concepts with their hit and sustain rates across many plans, and provider dispute outcomes. The claims and medical records belong to each client plan
**Clock:** Prompt-pay statutes for pre-payment review, and contractual and state look-back limits on retroactive recovery
**Buyer:** Chief Analytics Officer / Head of Concept Development

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 5 |
| Q2 Labor mass + repeatable | ×2 | 4 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 4 |
| Q5 Buyer + market | ×2 | 4 |
| **Weighted total** | | **51/60** |

**Kill switches:** **HIPAA**, and **data isn't theirs** — every finding is computed on client plans' identified claims and medical records under business associate agreements. Scored consistently with [[niches/insurance-tpa/medical-bill-review-networks/profile|🔍 Medical Bill Review & Repricing Networks]] (55, kill switch) and [[niches/self-insured-benefit-pools/rbp-claim-repricing-vendors/profile|🔍 Reference-Based Pricing & Claim Repricing Vendors]] (47, kill switch).
**Verdict:** Logged — kill switch. The highest score in this sweep: the finding is literally the invoice, and the vendor holds the only cross-plan record of which audit concepts survive provider dispute. All of it sits on protected health information the plans own.
