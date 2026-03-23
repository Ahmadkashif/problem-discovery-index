# Non-QM & Specialty Lending Brokers

**Parent Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Category:** High Market Share

## Profile
**Market Size:** $50-80B in annual origination volume
**Share of Parent Industry:** ~15% of broker originations, growing 20%+ annually
**Digital Adoption:** Low-Medium — Non-QM lender guidelines are distributed as PDF overlays updated weekly; no LOS natively models non-QM product matrices; rate sheets are manual lookups across 10-20 specialty lenders with different structures
**Target Buyer:** Brokerage owner or non-QM specialist loan officer
**Automation Potential:** High — Non-QM product matching is a complex rule-matching problem across dozens of lender guidelines, but the rules are explicit (published overlays) and the matching logic is deterministic

## What Makes This a Distinct Niche
Non-QM (Non-Qualified Mortgage) lending — bank statement loans, DSCR investor loans, asset depletion loans, foreign national loans — is the fastest-growing segment of mortgage brokerage. These products serve borrowers who don't fit conventional underwriting guidelines: self-employed individuals, real estate investors, high-net-worth individuals with complex income, and foreign nationals. The lender landscape is fragmented (20+ non-QM wholesale lenders with different products, overlays, and pricing), product matrices are complex (each lender offers 5-15 non-QM programs with different eligibility criteria), and guidelines change weekly. The broker's value is knowing which of 100+ possible lender-product combinations fits a specific borrower — knowledge that is even more tacit than conventional lender selection.

## Current Tools & Gaps
Encompass and Byte handle conventional loan processing but don't model non-QM product structures (bank statement income calculation methodologies, DSCR ratios, asset depletion formulas). Pricing engines (Optimal Blue) are expanding non-QM coverage but don't capture the full overlay matrix. Lender guidelines are distributed as PDFs updated weekly — loan officers maintain personal cheat sheets comparing lenders. No tool systematically compares non-QM products across lenders for a specific borrower profile.

## Problems
- [[niches/mortgage-brokers/non-qm-specialty-brokers/build|🔨 Build: Non-QM Product Matrix Matching Engine]]
- [[niches/mortgage-brokers/non-qm-specialty-brokers/buy|🛒 Buy: Bank Statement Income Calculation Automation]]
- [[niches/mortgage-brokers/non-qm-specialty-brokers/fix|🔧 Fix: Weekly Lender Guideline Change Tracking]]
