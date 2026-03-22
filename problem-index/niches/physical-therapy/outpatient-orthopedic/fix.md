# Patient Dropout Detection and Intervention

**Niche:** [[niches/physical-therapy/outpatient-orthopedic/profile|Outpatient Orthopedic PT Clinics]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Fix (Pain Point)
**One-liner:** Clinics stop losing 20-30% of evaluated patients who vanish after their first visit — automated detection and outreach intervenes before the patient disappears permanently.
**Tags:** #logistic-regression #gradient-boosting #feature-engineering #evaluation-metrics #automation #revenue-impact

## The Problem
A patient completes an initial evaluation — the clinic invests 45-60 minutes of clinician time, verifies insurance, obtains authorization, and builds a treatment plan. Then the patient never returns. Across outpatient orthopedic PT, 20-30% of evaluated patients drop out before their second visit. The clinic has no automated system to detect this in real time. The front desk might notice after a week, or might not notice at all if they are managing 200+ active patients. By the time anyone follows up, the patient has either self-discharged, gone to a competitor, or simply given up on PT entirely. Each lost patient represents $1,500-$4,000 in unrealized revenue from the remaining treatment episode.

## Why It's Still Broken
PT EMRs track scheduled appointments but don't flag the absence of expected appointments. If a patient's treatment plan calls for 2 visits per week and they simply don't schedule the next visit, no alert fires. The EMR sees a completed evaluation — task done. It doesn't model the expected patient journey (eval → follow-up within 3-5 days → 2x/week for 6 weeks) and compare actual behavior against that expectation. Front desk staff are focused on today's schedule, not on patients who should be on the schedule but aren't. The dropout detection problem requires a patient lifecycle model that PT EMRs don't implement.

## What a Fix Looks Like
An automated layer that monitors patient status against expected treatment cadence. When a patient completes an evaluation but has no follow-up scheduled within 48 hours, it triggers: (1) an immediate staff alert so the front desk can call, (2) an automated patient text/email at 48 hours ("We have openings this week — reply to schedule your next visit"), and (3) a 7-day escalation to the treating therapist if the patient hasn't responded. The system tracks dropout reasons when captured (transportation, cost, felt better, went elsewhere) to build a practice-level understanding of why patients leave. Over time, it can predict dropout risk at the point of evaluation based on patient demographics, payer type, diagnosis, and scheduling behavior.

## Who Feels the Pain
Clinic owners who watch revenue projections evaporate when evaluated patients don't return. Treating therapists who invest time in evaluations and treatment plans that are never executed. Front desk coordinators who bear the burden of manual follow-up when they notice a patient hasn't returned — if they notice at all.

## Impact If Fixed
Recovering even 30% of dropout patients adds $150K-$500K annually to a mid-sized outpatient orthopedic PT clinic. Reduces wasted evaluation time (each dropout wastes 45-60 minutes of clinician time plus authorization effort). Improves patient outcomes by re-engaging patients who would otherwise abandon treatment prematurely.
