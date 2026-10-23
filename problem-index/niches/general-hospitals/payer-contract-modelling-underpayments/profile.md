# Payer Contract Modelling & Underpayment Recovery

**Parent Industry:** [[industries/general-hospitals|General Hospitals]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to compute, for every remittance line, what each payer's contract says the hospital should have been paid, and whoever catches the most underpaid dollars inside the contract's dispute window takes the account.

## Profile
**Market Size:** ~$3B a year of contract-management software, managed-care analysts and contingency underpayment recovery (estimate)
**Share of Parent Industry:** ~0.2% of general hospital revenue (estimate)
**Digital Adoption:** Medium — expected-reimbursement engines exist, but contract terms are keyed in by hand from PDFs and go stale with amendments
**Target Buyer:** VP Managed Care / Director of Patient Financial Services
**Automation Potential:** High — contract extraction and variance detection are mechanical once terms are structured

## What Makes This a Distinct Niche
The claim was approved, just paid short. Commercial contracts mix DRG rates, per diems, percent-of-charges, Medicare-percentage clauses, implant carve-outs, outlier thresholds and lesser-of provisions, all amended over time. The work is reconciliation, not medicine. Since 1 April 2026 hospitals must publish median and percentile allowed amounts from their own remittances (CMS-1834-FC), and payers publish negotiated rates under Transparency in Coverage. Both give contract modellers a public benchmark, and the same files feed the normalisers profiled in [[niches/medical-billing/price-transparency-data-vendors/profile|🔍 Healthcare Price Transparency Data]].

## Current Tools & Gaps
Epic and Oracle expected-reimbursement modules; FinThrive, Experian and MedeAnalytics contract management (recalled); contingency recovery firms; Turquoise Health and Serif Health rate data for negotiation. Gaps: terms keyed by analysts and rarely re-verified after amendments; rule versions (IPPS/OPPS updates) applied late; variances under a threshold ignored; dispute windows tracked in spreadsheets.

## Problems
- [[niches/general-hospitals/payer-contract-modelling-underpayments/build|🔨 Build: Contracts Read Straight Into the Pricing Engine]]
- [[niches/general-hospitals/payer-contract-modelling-underpayments/buy|🛒 Buy: Price Transparency Rate Data Adapted to Underpayment Detection]]
- [[niches/general-hospitals/payer-contract-modelling-underpayments/fix|🔧 Fix: The Variance Threshold That Hides Systematic Underpayment]]
