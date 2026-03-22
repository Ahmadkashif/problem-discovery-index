# Internal Referral Leakage Tracking

**Niche:** [[niches/physical-therapy/hospital-based-outpatient/profile|Hospital-Based Outpatient PT]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Fix (Pain Point)
**One-liner:** Hospital rehab departments stop losing patients to external PT providers by tracking which system surgeons refer out and why — turning invisible referral leakage into actionable retention data.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #data-integration #revenue-impact

## The Problem
Hospital-based PT departments depend on internal referrals from system surgeons — an orthopedic surgeon employed by the health system should be sending post-surgical patients to the system's own rehab department. But many don't, or they send only some patients. A system surgeon who performs 200 total knee replacements per year might refer 120 to the hospital's PT department and 80 to external clinics — because the external clinic is closer to the patient's home, has shorter wait times, or because the surgeon has a personal relationship with an outside PT. The rehab department has no visibility into this leakage. They know how many patients they receive, but not how many they should be receiving. The data exists in the hospital's surgical records and referral orders, but nobody connects it.

## Why It's Still Broken
Internal referral tracking requires joining surgical case data (which lives in the OR system) with PT referral and scheduling data (which lives in the rehab module) and comparing against the total surgical volume of each system surgeon. This cross-departmental data join is technically possible within Epic or Cerner but requires custom report development that IT departments deprioritize — rehab is a cost center, not a revenue priority for most health systems. Additionally, surgeons have autonomy over referral patterns, and rehab department directors lack the data to have evidence-based conversations about referral retention. Without quantified leakage, the problem remains invisible.

## What a Fix Looks Like
A dashboard that connects surgeon surgical volume to PT referral volume within the health system. For each system surgeon: total procedures performed, number of PT referrals to in-system rehab, number of PT referrals to external providers (captured from referral orders), and the resulting capture rate. Trending shows whether capture rates are improving or declining. Drill-down reveals which procedures have the highest leakage rates and which external competitors receive the leaked referrals. The rehab director uses this data to approach surgeons with specific numbers: "Dr. Chen, we captured 62% of your total knees this quarter, down from 78% last quarter — the patients going to ABC Physical Therapy cite wait times as the reason. We've added Thursday evening availability to address this."

## Who Feels the Pain
Rehab department directors who are responsible for department revenue but cannot quantify or address referral leakage. Hospital administrators who invest in surgical programs but don't capture the downstream rehabilitation revenue. System surgeons who would prefer to keep referrals internal if the rehab department addressed the friction points driving patients out.

## Impact If Fixed
Recovering 10-20% of leaked internal referrals adds $500K-$2M annually to a hospital rehab department's revenue. Provides rehab directors with data to justify capacity investments (evening hours, satellite locations) that address the root causes of leakage. Strengthens the system-wide value proposition by demonstrating end-to-end surgical-to-rehab care coordination.
