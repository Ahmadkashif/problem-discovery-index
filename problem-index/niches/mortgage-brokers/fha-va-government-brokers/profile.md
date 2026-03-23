# FHA/VA Government Lending Brokers

**Parent Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Category:** Low Digitized

## Profile
**Market Size:** $80-120B in annual origination volume
**Share of Parent Industry:** ~16-24% of broker-originated volume
**Digital Adoption:** Low-Medium — government loan programs have the most complex compliance requirements but the least tooling specifically designed for their unique appraisal, eligibility, and documentation rules
**Target Buyer:** Loan officer / compliance specialist at government lending-focused brokerages
**Automation Potential:** High — FHA/VA eligibility, MIP/funding fee calculation, and appraisal compliance checks follow deterministic rules that are poorly implemented in current LOS platforms

## What Makes This a Distinct Niche
FHA and VA loans operate under entirely different rule sets than conventional lending — FHA has manual underwriting pathways, minimum property standards (MPS) enforced through appraisals, upfront and annual MIP calculations that vary by LTV and term, and county-specific loan limits. VA loans add Certificate of Eligibility (COE) verification, entitlement calculations (full vs. partial vs. bonus entitlement), VA-specific appraisal requirements (Tidewater/reconsideration of value processes), and funding fee exemption rules. Brokers who specialize in government lending must navigate these overlapping rule sets while also managing wholesale lender overlays that further restrict what the agencies allow. A conventional broker cannot easily pivot to government lending without deep domain expertise.

## Current Tools & Gaps
LOS platforms handle FHA/VA loan types but treat them as templates rather than intelligent workflows — they don't flag when a property might fail MPS inspection, don't calculate partial entitlement automatically, and don't warn when a borrower's scenario would qualify better under manual underwriting vs. AUS. FHA's Technology Open to Approved Lenders (TOTAL) scorecard is a black box, and brokers have no way to pre-screen scenarios before submission. VA's WebLGY system for COE retrieval works but doesn't integrate with entitlement calculation logic in the LOS.

## Problems
- [[niches/mortgage-brokers/fha-va-government-brokers/build|🔨 Build: Government Loan Scenario Pre-Qualification Engine]]
- [[niches/mortgage-brokers/fha-va-government-brokers/buy|🛒 Buy: Appraisal Compliance Checker Adapted for FHA/VA MPS]]
- [[niches/mortgage-brokers/fha-va-government-brokers/fix|🔧 Fix: VA Entitlement Calculation Errors]]
