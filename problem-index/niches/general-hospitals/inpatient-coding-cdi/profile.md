# Inpatient Coding & Clinical Documentation Integrity

**Parent Industry:** [[industries/general-hospitals|General Hospitals]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to assign the DRG the documentation truly supports before the claim drops, and whoever captures the most legitimate severity with DRG shifts that survive payer audit takes the account.

## Profile
**Market Size:** ~$5B a year of CDI specialists, inpatient coders, outsourced coding and CDI/coding software (estimate)
**Share of Parent Industry:** ~0.4% of revenue (estimate)
**Digital Adoption:** Medium-High — computer-assisted coding and CDI worklists are standard, but every inpatient chart is still read by a coder and many by a CDI nurse
**Target Buyer:** VP Revenue Integrity / Director of HIM and CDI
**Automation Potential:** Very High for outpatient and simpler inpatient cases; high for CDI query targeting; human sign-off persists for complex DRGs

## What Makes This a Distinct Niche
Inpatient payment is set by MS-DRG, and one documented complication or major complication (CC/MCC) can move a case to a tier paying thousands of dollars more. CDI specialists review open charts and send compliant queries to physicians. Coders assign ICD-10-CM/PCS codes after discharge. Payers then audit the result and downgrade DRGs, a fight profiled from the payer side at [[niches/health-insurance-carriers/payment-integrity-vendors/profile|🔍 Outsourced Payment Integrity Vendors]] (51, kill switch). DRG weights reset every 1 October in the IPPS final rule. The FY2027 rule, issued 31 July 2026, recalibrated them on ~6.9M FY2025 discharges and cut the MS-DRG count from 772 to 768 (HFMA and McDermott+ summaries). The same documentation also sets risk-adjusted mortality, PSI and readmission measures, so CDI affects quality scores as well as payment.

## Current Tools & Gaps
Solventum 360 Encompass (formerly 3M), Microsoft/Nuance CDE, Iodine Software, Epic's CDI and coding modules, AKASA, Smarter Technologies (SmarterDx pre-bill review), Fathom, CodaMetrix and Nym for autonomous coding (recalled); code sets and guidelines from [[niches/medical-billing/medical-coding-content-publishers/profile|🔍 Medical Coding Content Publishers]]. Gaps: query targeting tuned to dollars rather than audit survival; no learning from which DRG shifts payers reverse; autonomous coding limited to simpler encounter types. The office-visit version of this contest is [[niches/physician-practices/ambient-documentation-visit-coding/profile|Ambient Documentation & Office Visit Coding]]. There the code is a same-day E/M level and HCC capture closed at the visit. Here it is a DRG built from a multi-day record before the claim drops, and payers audit it months later.

## Problems
- [[niches/general-hospitals/inpatient-coding-cdi/build|🔨 Build: CDI Queries Ranked by Audit Survival, Not Just Dollars]]
- [[niches/general-hospitals/inpatient-coding-cdi/buy|🛒 Buy: Outpatient Autonomous Coding Extended to Inpatient DRGs]]
- [[niches/general-hospitals/inpatient-coding-cdi/fix|🔧 Fix: The Query Nobody Answers Before Discharge]]
