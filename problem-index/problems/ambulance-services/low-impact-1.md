# RSNAT Prior Authorization on Generic Prior-Auth Tools

**Industry:** [[ambulance-services|Ambulance Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Prior-authorization software is built for a physician's office asking a payer to approve a scan or a drug; an ambulance company asking a MAC to affirm 40 dialysis round trips needs a PCS it does not write, from a clinician it does not employ, before the fourth round trip.
**Tags:** #large-language-models #transformers #logistic-regression #workflow-orchestration #compliance #automation #data-integration

## The Problem
A patient on dialysis three times a week who cannot sit in a wheelchair rides a stretcher ambulance six times a week. Under Medicare's RSNAT model, which went nationwide in waves from 1 December 2021 to 1 August 2022, that patient's transports (A0428 basic or A0426 advanced non-emergency) need a provisional affirmation from the MAC. Otherwise the claims go to prepayment review once the fourth round trip in a 30-day period has passed without a request. The request must carry a physician certification statement signed by the attending physician, with credentials, dated within 60 days of the start date. It must also carry medical documentation from the patient's own clinician that shows why the patient cannot travel by other means. An affirmation covers up to 40 round trips over up to 60 days (CMS MLN6805343, January 2026).

The PCS specialist at the ambulance company or its billing firm does not control any of those documents. She faxes a blank PCS to a dialysis social worker, calls the nephrologist's office, receives a form with the credential line blank, and sends it back. Since 9 January 2025 the MAC answers within 7 calendar days, but only once the packet is complete. Every 60 days the cycle repeats for every patient. In FY2024, 27.6% of the 28,836 completed requests were not provisionally affirmed. Of the 14,268 claim lines denied in prepayment review, 11,953 were denied because no documentation was submitted (CMS FY2024 statistics).

## What Already Exists
Prior-authorization platforms and payer portals (Availity, payer utilization management portals, ePA tools for imaging and pharmacy), MAC portals and esMD gateways, fax servers, and the billing modules of ambulance billing systems that track PCS dates. Shared vendors are profiled at [[niches/physician-practices/ordering-practice-prior-authorization/profile|⚡ Prior Authorization at the Ordering Practice]] and [[niches/general-hospitals/patient-access-auth-estimates/profile|⚡ Patient Access: Prior Authorization, Eligibility & Estimates]].

## The Customisation Gap
Generic prior-auth tools assume the requester is the ordering clinician and holds the chart. RSNAT reverses that. The supplier requests, and every supporting document comes from a third party. The ambulance-specific logic is the repetitive-transport definition (three round trips in 10 days or weekly for three weeks) and the fourth-round-trip trigger counted per beneficiary over a rolling 30 days. On top of that sit the PCS completeness rules (signature, credentials, 60-day date window), the 40-trip and 60-day affirmation window, matching each scheduled run to an affirmation number, and the bed-confinement and "other means contraindicated" criteria of 42 CFR 410.40. A tool also has to read clinician notes that were never written for an ambulance claim, and flag which ones will not support "cannot be transported by other means" before the packet goes to the MAC.

## Impact If Solved
A PCS tracker with these rules would turn a fax chase into a queue of known gaps: missing credential, PCS expiring in 9 days, round trip four due Thursday. For an operator running 300 dialysis patients, that is roughly 1,800 renewals a year (an estimate) handled by exception. It would also cut the prepayment denials caused by documents that never arrived, which were 84% of RSNAT prepayment denials in FY2024.
