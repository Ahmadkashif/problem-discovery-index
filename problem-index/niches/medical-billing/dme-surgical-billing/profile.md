# DME & Surgical Billing

**Parent Industry:** [[industries/medical-billing|Medical Billing]]
**Category:** Underserved

## Profile
**Market Size:** $1-1.5B
**Share of Parent Industry:** ~7%
**Digital Adoption:** Low — many DME companies still use paper-based CMN tracking, fax-based prior authorizations, and manual rental period calculations
**Target Buyer:** DME company billing manager, surgical supply billing specialist, or DME billing company owner
**Automation Potential:** Very High — CMN tracking, rental period calculations, and competitive bidding compliance are rule-based workflows ripe for automation

## What Makes This a Distinct Niche
DME (Durable Medical Equipment) and surgical supply billing is fundamentally different from physician billing. The code set is HCPCS (Healthcare Common Procedure Coding System) Level II, not CPT — codes like E1390 (oxygen concentrator), K0823 (power wheelchair), and L1970 (ankle-foot orthosis). Every DME item requires a Certificate of Medical Necessity (CMN) or Detailed Written Order (DWO) signed by the ordering physician, with specific clinical criteria that vary by product category. Billing follows rental vs. purchase logic — oxygen concentrators follow a 36-month capped rental period after which ownership transfers; wheelchairs may be rented or purchased depending on payer and expected duration of need. Medicare's Competitive Bidding Program sets pricing for certain DME categories in specific geographic areas, overriding standard fee schedules. Advance Beneficiary Notices (ABNs) must be obtained when coverage is uncertain. This is an entirely separate billing discipline that generic PM systems do not support.

## Current Tools & Gaps
DME-specific billing software exists (Brightree, now part of ResMed; TeamHealth DME; NikoHealth) but is designed for large DME suppliers — pricing starts at $500-1,000/month and requires extensive configuration. Small DME companies and surgical supply distributors often use generic PM systems or even spreadsheet-based tracking for CMN dates, rental periods, and reauthorization deadlines. Clearinghouses accept HCPCS claims but don't validate CMN requirements or rental period logic. The gap is affordable DME billing software for small-to-mid-sized suppliers that handles CMN lifecycle tracking, rental period automation, competitive bidding compliance, and ABN management without enterprise-level complexity or cost.

## Problems
- [[niches/medical-billing/dme-surgical-billing/build|🔨 Build: DME Billing & CMN Lifecycle Platform]]
- [[niches/medical-billing/dme-surgical-billing/buy|🛒 Buy: HCPCS Billing Module for Standard PM Systems]]
- [[niches/medical-billing/dme-surgical-billing/fix|🔧 Fix: CMN Expiration Tracking to Prevent Auto-Denials]]
