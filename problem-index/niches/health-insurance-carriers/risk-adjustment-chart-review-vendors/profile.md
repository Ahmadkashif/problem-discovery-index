# Risk Adjustment Chart Review & Coding Vendors

**Parent Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Firms that retrieve members' medical records and code them for risk adjustment, for MA plans and for ACA issuers' HHS risk adjustment data validation: Datavant, Episource, Reveleer, Cotiviti and Optum are representative (named from recall). They run retrospective chart reviews, prospective suspecting, NLP-assisted coding and RADV audit defence. Since CMS announced in May 2025 that it would audit every eligible MA contract each year, demand has shifted from adding codes toward validating and deleting them.

## Insight Function
**Size:** 20-150 data scientists, NLP engineers and clinical analytics staff per vendor (estimate); the certified coders are production staff
**Output:** Coded chart findings (adds and deletes), suspect lists, RADV submission packages
**Proprietary data:** Coding outcomes and audit results across many plans' members; the records belong to providers and the findings to client plans
**Clock:** CMS's final risk adjustment submission deadline and RADV record submission windows (five months under CMS's January 2026 memo)
**Buyer:** Chief Product Officer / VP of Analytics

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 3 |
| Q4 External clock | ×2 | 5 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **43/60** |

**Kill switches:** **HIPAA**, and **data isn't theirs** — the work is reading identified members' medical records on behalf of client plans. Scored consistently with [[niches/medical-billing/coding-audit-compliance-firms/profile|🔍 Coding Audit & Compliance Firms]] (46, kill switch).
**Verdict:** Logged — kill switch. Volume grows with coders rather than analysts, and the corpus is protected health information the vendor holds for its clients.
