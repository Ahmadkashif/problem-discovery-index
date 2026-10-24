# Outpatient Prior Authorization & Gold-Carding

**Parent Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to turn an outpatient authorization request into a determination inside the 72-hour and seven-day clocks without a fax or a phone call, and whoever auto-approves the largest share of requests a nurse would have approved, with no rise in overturned denials or later-audited approvals, takes the account.

## Profile
**Market Size:** ~$7B a year in outpatient authorization staff, specialty benefit manager programmes and submission and decision platforms (estimate)
**Share of Parent Industry:** ~5% of carrier administrative spend (estimate)
**Digital Adoption:** Medium — portals and electronic submission are common, but attachments are still documents read by people
**Target Buyer:** VP of Utilization Management / Head of Specialty Benefit Programmes
**Automation Potential:** High — most requests are approved, and most of the review is matching documented facts to written criteria

## What Makes This a Distinct Niche
Outpatient requests (advanced imaging, elective surgery, specialty drugs under the medical benefit, therapy visits, durable equipment) are high-volume, mostly approved and decided once, before the service. More than 90% of MA determinations in 2024 were fully favourable (KFF). The contest is throughput: deciding fast, with evidence, without a nurse touching what a nurse would approve anyway. The CMS-0057-F API due in January 2027 and state gold-card laws, which exempt providers with high approval rates (Texas's 2021 law first, recalled), both push toward deciding from data rather than documents. On the provider side, a freestanding imaging centre re-checks the approval against the exam it performs: see [[niches/diagnostic-imaging-centers/order-intake-auth-verification/profile|Referral Order Intake & Authorization Verification]].

## Current Tools & Gaps
Specialty benefit managers (Evolent, Carelon, EviCore), submission and decision vendors (Cohere, Availity), payer portals and fax intake with OCR. The gaps are a criterion-level evidence layer in the plan's own system, gold-card lists computed from real approval history rather than by hand, and auto-approval rules that are audited after the fact.

## Problems
- [[niches/health-insurance-carriers/outpatient-prior-authorization/build|🔨 Build: Approve-on-Sight for Outpatient Requests]]
- [[niches/health-insurance-carriers/outpatient-prior-authorization/buy|🛒 Buy: Gold-Card Lists Built From Provider Approval History]]
- [[niches/health-insurance-carriers/outpatient-prior-authorization/fix|🔧 Fix: The Missing Note That Restarts the Clock]]
