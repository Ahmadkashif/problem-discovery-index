# Payment Posting & Reconciliation

**Parent Industry:** [[industries/medical-billing|Medical Billing]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1-1.5B (embedded across all billing operations)
**Share of Parent Industry:** Touches all segments
**Digital Adoption:** Medium — ERA/835 electronic remittances are standard, but interpreting complex adjustment reason codes and verifying contractual rates against fee schedules remain manual
**Target Buyer:** Payment posting specialist, billing manager, AR reconciliation lead
**Automation Potential:** Very High — payment posting is high-volume, rules-based, and error-prone when done manually, making it an ideal automation target

## What Makes This a Distinct Niche
Payment posting is the process of matching incoming payments (from payers and patients) to the correct claims, applying the correct adjustment reason codes, calculating patient responsibility, and posting to the correct patient account in the PM system. A single ERA (Electronic Remittance Advice, ANSI 835 format) from a large payer can contain 200+ line items across dozens of patients, each with multiple adjustment reason codes (contractual obligation, deductible, coinsurance, non-covered charges, bundling adjustments). The posting specialist must interpret each adjustment, verify it against the provider's contracted rate with that payer, identify underpayments, and flag discrepancies. When a payer pays $85 for a procedure with a contracted rate of $95, the specialist must determine whether the $10 difference is a legitimate patient deductible or a payer underpayment — this determination requires knowing the patient's specific plan, remaining deductible, and the provider's fee schedule for that payer. At scale, a billing company processing 5,000-10,000 claims per month spends 40-80 hours on payment posting alone.

## Current Tools & Gaps
PM systems have auto-posting features that can read ERA/835 files and apply payments, but they handle only the simplest cases — single payment to single claim with standard adjustment codes. When adjustments are complex (multiple CARC codes per line, takeback/reversal scenarios, bundled payment across multiple claims), auto-posting fails and creates exceptions that require manual review. No PM system verifies that the paid amount matches the contracted rate — this requires cross-referencing the payer's fee schedule, which is stored in a separate contract document (often a PDF or spreadsheet). The gap is intelligent auto-posting that handles complex adjustment logic, verifies contractual rate compliance, flags underpayments automatically, and reduces the exception queue to only genuinely ambiguous cases.

## Problems
- [[niches/medical-billing/payment-posting-reconciliation/build|🔨 Build: Intelligent Auto-Posting with Contractual Rate Verification]]
- [[niches/medical-billing/payment-posting-reconciliation/buy|🛒 Buy: ERA Auto-Posting Enhancement for PM Systems]]
- [[niches/medical-billing/payment-posting-reconciliation/fix|🔧 Fix: Contractual Adjustment Verification to Catch Underpayments]]
