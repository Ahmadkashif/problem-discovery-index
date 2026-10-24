# Patient Access: Prior Authorization, Eligibility & Estimates

**Parent Industry:** [[industries/general-hospitals|General Hospitals]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to get every scheduled service verified, authorised and priced before the patient arrives, and whoever clears the most scheduled cases with no human touch and no downstream authorisation denial takes the account.

## Profile
**Market Size:** ~$4B a year of patient access staff, eligibility and authorisation software and outsourced pre-service work at general hospitals (estimate)
**Share of Parent Industry:** ~0.3% of revenue (estimate)
**Digital Adoption:** Medium — eligibility checks are electronic (270/271), but authorisations still run through payer portals, phone and fax, and estimates are built from chargemaster and contract tables of uneven quality
**Target Buyer:** Director of Patient Access / VP Revenue Cycle
**Automation Potential:** Very High — rule lookup, portal submission and status checking are mechanical, and federal API mandates are arriving

## What Makes This a Distinct Niche
Scheduled hospital services (surgery, infusions, advanced imaging, inpatient elective admissions) need eligibility checked, authorisation obtained against each payer's rules, and, for self-pay and shoppable services, a good-faith estimate. A missing authorisation becomes a technical denial that is hard to overturn. CMS-0057-F requires impacted payers to stand up FHIR prior-authorisation APIs by 1 January 2027 (recalled; checked under [[industries/health-insurance-carriers|Health Insurance Carriers]]). Since April 2026, hospital price files must carry median and percentile allowed amounts drawn from remittances (CMS-1834-FC), which links the price file to what patients are actually quoted. Obtaining the authorisation for an order belongs to the practice that placed it: see [[niches/physician-practices/ordering-practice-prior-authorization/profile|Prior Authorization at the Ordering Practice]] and [[niches/physician-practices/imaging-procedure-authorization/profile|Imaging & Procedure Authorization]] under [[industries/physician-practices|Physician Practices]]. This niche keeps the hospital's side. It checks at scheduling that a valid authorisation exists and matches the service, and it obtains authorisations only where the hospital itself is the requesting provider. A freestanding imaging centre's own re-check of the approval against the exam actually performed sits under [[niches/diagnostic-imaging-centers/order-intake-auth-verification/profile|Referral Order Intake & Authorization Verification]] ([[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]).

## Current Tools & Gaps
Epic Prelude and Cadence with Epic's payer platform; Experian, Waystar and Availity for eligibility and authorisation; AKASA and Commure authorisation automation; Infinitus and other voice agents calling payers; estimate tools built on chargemasters and contract models. Gaps: payer rule libraries maintained by hand; portal-by-portal submission; estimates that miss the patient's actual allowed amount; no link from authorisation status to the scheduling decision.

## Problems
- [[niches/general-hospitals/patient-access-auth-estimates/build|🔨 Build: Authorization Requirement Prediction From the Order Itself]]
- [[niches/general-hospitals/patient-access-auth-estimates/buy|🛒 Buy: Payer FHIR Prior-Auth APIs Wrapped for Hospital Schedulers]]
- [[niches/general-hospitals/patient-access-auth-estimates/fix|🔧 Fix: Estimates That Disagree With the Hospital's Own Price File]]
