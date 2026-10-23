# Case Management & Post-Acute Placement

**Parent Industry:** [[industries/general-hospitals|General Hospitals]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to get a medically ready patient accepted and authorised for the right post-acute bed on the day they are ready, and whoever removes the most avoidable days per case manager takes the account.

## Profile
**Market Size:** ~$1.5B a year of referral-management, discharge-prediction and placement software and services (estimate), against avoidable inpatient days the DRG does not pay for
**Share of Parent Industry:** ~0.1% of revenue in tools (estimate)
**Digital Adoption:** Low — referral platforms exist, but acceptance still turns on phone calls, faxed packets and Medicare Advantage portals
**Target Buyer:** VP Care Management / Director of Case Management
**Automation Potential:** Medium-High — packet assembly, routing and status chasing are mechanical; level-of-care judgement and family conversations stay human

## What Makes This a Distinct Niche
Under a DRG, every day past medical readiness is unpaid, and the bed is unavailable to the ED patient boarding downstairs. Case managers and social workers plan discharges under the CMS discharge-planning conditions of participation (recalled). They must offer patient choice among post-acute providers, assemble referrals, obtain MA authorisation, and arrange transport and equipment. MA plans deny more than 21% of SNF discharge requests at first submission (Premier, 2025). The first authorisation step, and the continued-stay reviews that follow, are worked from the facility's side in [[niches/skilled-nursing-facilities/ma-authorization-denials/profile|Medicare Advantage Authorisation & Continued-Stay Reviews]]. The receiving admissions desk is [[niches/skilled-nursing-facilities/referral-admissions/profile|Hospital Referral Intake & Admissions]] under [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]. This niche is the hospital's side of that handoff, and this profile is where the referral vendor field is described.

## Current Tools & Gaps
The referral vendor field:
- **CarePort (WellSky)** is the most widely used hospital-side referral network (recalled). Case managers send packets to post-acute providers and track views, accepts and declines in it, and it carries patient-choice lists and Care Compare quality data.
- **Aidin** competes on the same send-and-track workflow, with its own facility network and response analytics.
- **naviHealth (Optum)** sits on the payer side of the same handoff. MA plans use it to authorise and manage post-acute stays, and its length-of-stay predictions have drawn lawsuits over algorithm-assisted denials (recalled).

Around them sit Epic case management modules, discharge-prediction and inpatient-flow products from Qventus and LeanTaaS iQueue for Inpatient Flow, and MCG and InterQual for level-of-care criteria. Gaps: referral packets assembled by hand for each facility; no model of which facility will accept which patient; MA authorisation tracked separately from placement; avoidable days recorded after the fact with vague reason codes.

## Problems
- [[niches/general-hospitals/case-management-post-acute-placement/build|🔨 Build: Acceptance Prediction for Every Post-Acute Referral]]
- [[niches/general-hospitals/case-management-post-acute-placement/buy|🛒 Buy: Freight Load Matching Adapted to Patient Placement]]
- [[niches/general-hospitals/case-management-post-acute-placement/fix|🔧 Fix: Avoidable Days With "Other" as the Reason]]
