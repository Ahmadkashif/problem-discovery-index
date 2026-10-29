# PCS & RSNAT Prior Authorization for Scheduled Transports

**Parent Industry:** [[industries/ambulance-services|Ambulance Services]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to keep each repetitive patient's Medicare transports paid without prepayment review, and whoever has the fewest RSNAT claim lines denied per 1,000 scheduled round trips takes the account.

## Profile
**Market Size:** ~$0.15B a year of PCS specialists, authorization staff, billing-firm fees and fax and portal tooling for scheduled non-emergent transports (estimate)
**Share of Parent Industry:** ~0.7% of 621910 receipts (estimate)
**Digital Adoption:** Low — PCS forms travel by fax between ambulance offices, dialysis units and physicians' offices; requests reach the MAC by fax, portal or esMD
**Target Buyer:** Operator billing director or the ambulance billing firm's client-services lead
**Automation Potential:** High for tracking, packet assembly and completeness checks; the clinician's signature cannot be automated

## What Makes This a Distinct Niche
Medicare's RSNAT prior authorization model applies to independent suppliers (not institution-based ones) that bill A0426 or A0428 for a patient riding three or more round trips in 10 days or weekly for three weeks, most often to dialysis. It went nationwide in waves from 1 December 2021 to 1 August 2022. If no request is made by the fourth round trip in a 30-day period, claims go to prepayment review. Affirmations cover up to 40 round trips over up to 60 days, the MAC decides within 7 calendar days, and the PCS must carry the attending physician's signature and credentials, dated within 60 days (CMS). The model has worked as a spending control: charted RSNAT payments fell from $388M in the second half of FY2014 to $81M in each half of FY2024, and of 14,268 claim lines denied in FY2024 prepayment review, 11,953 had no documentation submitted (CMS statistics). Competitors are operators' PCS staff, ambulance billing firms and the few prior-auth tools that touch Medicare FFS. The nearest profiled contest is [[niches/physician-practices/ordering-practice-prior-authorization/profile|⚡ Prior Authorization at the Ordering Practice]], where the clinician who ordered the service asks a payer from its own chart. Here the supplier asks a MAC, using a PCS and notes written by third-party clinicians it does not employ. Medicaid NEMT trip authorization is a different contest, at [[niches/non-emergency-medical-transport/trip-authorization-verification/profile|⚡ Trip Authorization Verification]].

## Current Tools & Gaps
Fax servers, MAC portals, esMD gateways, billing-system PCS date fields and spreadsheets of renewals. Gaps: no rolling count of round trips against the fourth-trip trigger, no completeness check before submission, and no link from an affirmation number to each scheduled run.

## Problems
- [[niches/ambulance-services/rsnat-pcs-prior-authorization/build|🔨 Build: Round-Trip Trigger and Renewal Tracker for Every Repetitive Patient]]
- [[niches/ambulance-services/rsnat-pcs-prior-authorization/buy|🛒 Buy: Dialysis Referral Platforms Extended to Ambulance PCS]]
- [[niches/ambulance-services/rsnat-pcs-prior-authorization/fix|🔧 Fix: PCS Forms Returned Without Credentials or Dates]]
