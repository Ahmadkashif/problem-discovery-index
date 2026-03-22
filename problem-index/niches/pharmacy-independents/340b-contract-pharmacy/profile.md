# 340B Contract Pharmacy

**Parent Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Category:** Low Digitized

## Profile
**Market Size:** $0.5-1B
**Share of Parent Industry:** ~5%
**Digital Adoption:** Low — 340B program management relies on third-party administrators (TPAs) for claim accumulation, but pharmacies have minimal visibility into per-claim 340B eligibility, margin attribution, and audit compliance status; most documentation is retrospective and TPA-dependent
**Target Buyer:** Independent pharmacy owner with a 340B contract pharmacy arrangement with an FQHC, rural hospital, or other covered entity, or an FQHC pharmacy director managing 340B compliance across multiple contract pharmacy relationships
**Automation Potential:** High — split billing determination (which claims qualify for 340B pricing), HRSA audit preparation, and manufacturer restriction tracking are rule-heavy processes with clear automation pathways

## What Makes This a Distinct Niche
The 340B Drug Pricing Program allows eligible healthcare organizations (FQHCs, disproportionate share hospitals, Ryan White clinics) to purchase outpatient drugs at steep discounts — typically 25-50% below wholesale acquisition cost. These "covered entities" contract with independent pharmacies to dispense medications to their patients, and the pharmacy accesses 340B pricing for those specific claims. The complexity is in determining which prescriptions qualify: the patient must be a registered patient of the covered entity, the prescription must be written by a provider associated with the entity, and the drug must be on the entity's formulary. Split billing — routing eligible claims through 340B purchasing and non-eligible claims through regular wholesale — requires real-time eligibility determination at point of sale. Errors in either direction are costly: over-claiming 340B pricing constitutes program fraud, while under-claiming leaves 340B savings on the table. HRSA audits (which can be triggered randomly or by manufacturer complaints) require the pharmacy to produce documentation proving each 340B claim was for an eligible patient — a documentation burden that most pharmacies cannot meet retrospectively.

## Current Tools & Gaps
340B TPAs (Sentry Data Systems, Macro Helix, Verity Solutions) handle "virtual inventory" models — they retrospectively identify which dispensed claims qualified for 340B pricing and process the replenishment orders. These systems determine 340B eligibility after the fact, not at point of sale. The pharmacy has limited visibility into which claims the TPA identified as 340B-eligible, what the margin delta was on each claim, or whether the eligibility determination would withstand an HRSA audit. The covered entity controls the patient eligibility list, which the pharmacy cannot independently verify. The gap is real-time 340B eligibility determination with per-claim audit documentation and margin visibility — replacing the current model where the pharmacy trusts the TPA's retrospective analysis without independent verification.

## Problems
- [[niches/pharmacy-independents/340b-contract-pharmacy/build|🔨 Build: Real-Time 340B Split Billing and Compliance Audit Platform]]
- [[niches/pharmacy-independents/340b-contract-pharmacy/buy|🛒 Buy: TPA Dashboard with Per-Claim 340B Margin Visibility and Audit Trail]]
- [[niches/pharmacy-independents/340b-contract-pharmacy/fix|🔧 Fix: HRSA Audit Readiness with Continuous Compliance Monitoring]]
