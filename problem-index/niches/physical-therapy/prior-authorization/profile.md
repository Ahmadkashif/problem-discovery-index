# Prior Authorization & Concurrent Review

**Parent Industry:** [[industries/physical-therapy|Physical Therapy]]
**Category:** Highly Automatable

## Profile
**Market Size:** $2-4B (embedded across all insured PT)
**Share of Parent Industry:** Touches all insurance-billed PT — cross-cutting operational function
**Digital Adoption:** Low-Medium — authorization tracking is done in spreadsheets, sticky notes, and EMR free-text fields despite being the highest-risk administrative process in PT
**Target Buyer:** Authorization specialist, front desk coordinator, billing manager
**Automation Potential:** Very High — authorization tracking, extension requests, and medical necessity narratives are all structured, rule-based processes with high error cost

## What Makes This a Distinct Niche
Most payers require PT authorization every 10-12 visits. Tracking where each patient stands in their authorization cycle, requesting extensions before visits run out, and documenting medical necessity for each extension request is a manual process that touches every insured PT patient. Different payers use different utilization management (UM) vendors — EviCore, Cohere Health, Carelon — each with their own portal, criteria, and submission workflows. When authorization tracking fails, the clinic delivers unauthorized visits and absorbs the cost ($100-200 per visit). This is not a clinical problem but an operational one — yet it directly impacts revenue, compliance, and patient care continuity. A single authorization lapse can cost a clinic $1,000-$2,000 in unreimbursed visits.

## Current Tools & Gaps
PT EMRs (WebPT, Clinicient/Prompt) have basic authorization tracking fields — a place to enter the authorization number, start date, end date, and approved visit count. But they don't pull data from payer portals, don't proactively alert when authorization is expiring, don't auto-populate extension request forms with clinical data, and don't track the status of pending extension requests. The front desk manages authorization on spreadsheets or in their heads, checking each patient's remaining visits manually. UM vendor portals (EviCore, Cohere Health) each require separate logins and different submission workflows, with no aggregation across payers.

## Problems
- [[niches/physical-therapy/prior-authorization/build|🔨 Build: Universal PT Authorization Tracker]]
- [[niches/physical-therapy/prior-authorization/buy|🛒 Buy: Proactive Authorization Management for PT EMRs]]
- [[niches/physical-therapy/prior-authorization/fix|🔧 Fix: Auto-Generated Medical Necessity Narratives]]
