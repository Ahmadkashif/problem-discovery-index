# Virtual Patient Engagement & Disengagement Detection

**Niche:** [[niches/behavioral-health-clinics/teletherapy-only-practices/profile|Teletherapy-Only Practices]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Fix (Pain Point)
**One-liner:** Teletherapy patients ghost at 15-25% higher rates than in-person patients, and practices have no early-warning system to detect disengagement before the patient disappears.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #time-series-forecasting #change-point-detection #cross-validation #evaluation-metrics #worker-facing

## The Problem
In teletherapy, the barrier to dropping out is a single click — no awkward front-desk cancellation, no physical no-show where someone notices. Patients disengage gradually: session frequency declines, cancellations increase, cameras turn off, sessions end early. By the time the therapist notices the pattern, the patient has already ghosted. Practices lose 20-30% of active patients annually to silent attrition, and each lost patient represents $3,000-$8,000 in annual revenue. More importantly, these are patients who needed care and didn't get it.

## Why It's Still Broken
Teletherapy platforms track session attendance but don't surface engagement trends. Therapists manage 25-35 active patients and can't manually monitor disengagement signals across their caseload. EHRs report on no-shows after the fact but don't predict them. The teletherapy-specific signals that indicate disengagement — camera-off frequency, session duration shortening, rescheduling-to-cancellation ratio, gap-between-sessions lengthening — aren't captured as structured data by any current platform. They exist in session metadata that nobody aggregates or analyzes.

## What a Fix Looks Like
An engagement monitoring dashboard that ingests teletherapy session metadata (attendance, duration, camera status, cancellation/reschedule history, time-between-sessions) and computes a per-patient engagement score using a trained classifier. When the score crosses a disengagement threshold — calibrated to flag patients 2-3 weeks before they would typically ghost — the system triggers automated outreach: a personalized check-in message, a rescheduling prompt, or an alert to the therapist to address retention in the next session. The dashboard gives practice owners a caseload-wide view of engagement health.

## Who Feels the Pain
Therapists who lose patients they could have retained if they'd caught the disengagement early, and practice owners who see revenue erosion from silent attrition they can't measure or prevent.

## Impact If Fixed
Reducing silent attrition by even 30% recovers $15,000-$40,000 per year for a 5-therapist practice. Therapists spend less emotional energy wondering why patients disappeared and more time on clinical work. Patients who would have dropped out get a second chance at continuity of care.
