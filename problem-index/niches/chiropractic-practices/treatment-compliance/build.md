# Treatment Plan Compliance Dashboard with Automated Interventions

**Niche:** [[niches/chiropractic-practices/treatment-compliance/profile|Treatment Plan Compliance Tracking]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product tracks real-time patient compliance against the prescribed treatment plan and automatically triggers stage-appropriate interventions (reminders, re-engagement, plan modification) when compliance drops below target.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #automation #revenue-impact

## The Problem
A chiropractor prescribes a 24-visit treatment plan over 12 weeks. By week 4, the patient has attended 8 of 12 recommended visits (67% compliance). By week 8, they've attended 12 of 20 recommended visits (60% compliance). By week 12, they've attended 14 of 24 (58%). The DC discovers the patient's declining compliance only if they manually count visits — which they don't because they're seeing 30+ patients per day. The front desk notices missed appointments individually but doesn't calculate compliance rates. By the time anyone notices the pattern, the patient has disengaged.

## Why Nobody Has Built This
Treatment plans in chiropractic EHRs are stored as static text, not structured data. "3x/week for 4 weeks" is a narrative recommendation, not a machine-readable schedule that the system can track against actual appointments. Building a compliance tracker requires parsing treatment plans into structured schedules, calculating compliance rates against actual visit patterns, and defining intervention triggers — none of which exists in current EHR data models.

## What to Build
A compliance dashboard that parses the treatment plan into a structured visit schedule, calculates real-time compliance rate for each patient, and triggers automated interventions at defined thresholds: 80% compliance = green (on track); 60-79% = yellow (automated text reminder emphasizing plan importance); below 60% = red (staff call scheduled, plan modification recommended). Dashboard shows all patients by compliance status, sorted by risk of plan abandonment. Predicts which patients will complete their plan based on early compliance patterns, enabling proactive intervention on the most at-risk patients.

## Target Customer
Chiropractic practices with 200+ active treatment plan patients, experiencing 40-50% average plan completion rates.

## Impact If Built
Increases treatment plan completion rates from 45% to 65-70% through early intervention on non-compliant patients. For a practice with 200 active plan patients at $2,400 average plan value, improving completion by 20 percentage points adds $96K in annual revenue from plans that would otherwise be abandoned.
