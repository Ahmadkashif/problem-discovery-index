# Medical Debt Collectors

**Parent Industry:** [[industries/collections-agencies|Collections Agencies]]
**Category:** High Market Share

## Profile
**Market Size:** ~$6B in medical debt placed with third-party agencies annually
**Share of Parent Industry:** ~30%
**Digital Adoption:** Medium — collection platforms handle account management, but medical debt-specific workflows (insurance verification, charity care screening, itemized statement compliance) are largely manual
**Target Buyer:** Agency principal or VP of operations at agencies with dedicated healthcare receivables divisions
**Automation Potential:** High — medical debt has unique pre-collection verification requirements (insurance eligibility, charity care screening, No Surprises Act compliance) that follow deterministic rules

## What Makes This a Distinct Niche
Medical debt collection operates under a unique regulatory overlay: the No Surprises Act, state surprise billing laws, charity care requirements, HIPAA constraints on debtor communication, and credit reporting restrictions specific to medical debt (the three bureaus no longer report medical debt under $500 and delay reporting for 365 days). Before a medical debt can be collected, the agency must verify that insurance was properly billed, that the patient was not eligible for charity care, and that the itemized statement matches the original provider records. These pre-collection steps add 15-30 minutes of verification per account that does not exist in other debt categories.

## Current Tools & Gaps
Standard collection platforms (FICO, Latitude, Artiva) handle the collection workflow but do not automate the medical-specific pre-collection verification. Insurance eligibility checking requires accessing separate clearinghouse portals. Charity care screening requires cross-referencing the debtor's income against the provider's charity care policy — data that is rarely transmitted with the placement file. HIPAA-compliant communication templates are maintained manually.

## Problems
- [[niches/collections-agencies/medical-debt-collectors/build|🔨 Build: Pre-Collection Medical Debt Verification Engine]]
- [[niches/collections-agencies/medical-debt-collectors/buy|🛒 Buy: Healthcare Clearinghouse Integration for Insurance Verification]]
- [[niches/collections-agencies/medical-debt-collectors/fix|🔧 Fix: Charity Care Screening Gap Before Collection Attempts]]
