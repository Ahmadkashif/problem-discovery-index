# Dialysis Transport Specialists

**Parent Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Category:** High Market Share

## Profile
**Market Size:** $2-3B
**Share of Parent Industry:** ~20-25%
**Digital Adoption:** Medium — Dialysis centers have scheduling systems (DaVita, Fresenius portals), but coordination with NEMT providers is phone/fax-based with no automated scheduling integration
**Target Buyer:** NEMT provider owner / dialysis center transport coordinator
**Automation Potential:** High — Dialysis trips are the most predictable NEMT segment: same patient, same facility, same schedule (typically 3x/week), creating standing orders ideal for automated routing and exception handling

## What Makes This a Distinct Niche
Dialysis transport represents the highest-volume recurring trip type in NEMT — approximately 500,000 Americans receive in-center hemodialysis 3 times per week, generating ~78 million annual NEMT trips. These trips are uniquely time-critical: patients must arrive within a narrow treatment window (missing a session can be life-threatening), and post-treatment patients often experience fatigue, dizziness, and hypotension requiring careful handling during transport. The recurring nature creates standing orders that should be easy to automate, but the reality is complicated by treatment time variability (3-5 hours), patient condition changes post-treatment, facility-side delays, and the fact that 15-20% of dialysis patients use wheelchairs.

## Current Tools & Gaps
Dialysis centers (DaVita, Fresenius, independent centers) have internal scheduling systems for treatment slots but coordinate transportation externally via phone or fax to NEMT brokers or directly to providers. NEMT dispatch software treats dialysis trips as any other trip type, missing the specific requirements: predictable 3x/week scheduling that should auto-generate standing orders, post-treatment pickup timing that depends on actual treatment completion (not a fixed time), and patient condition monitoring that may require upgrading from ambulatory to wheelchair transport mid-route.

## Problems
- [[niches/non-emergency-medical-transport/dialysis-transport-specialists/build|🔨 Build: Dialysis Center-NEMT Real-Time Scheduling Bridge]]
- [[niches/non-emergency-medical-transport/dialysis-transport-specialists/buy|🛒 Buy: Standing Order Route Optimizer for Recurring Trips]]
- [[niches/non-emergency-medical-transport/dialysis-transport-specialists/fix|🔧 Fix: Post-Treatment Pickup Timing Mismatch]]
