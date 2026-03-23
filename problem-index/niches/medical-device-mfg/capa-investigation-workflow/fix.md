# CAPA Effectiveness Verification Tracking

**Niche:** [[niches/medical-device-mfg/capa-investigation-workflow/profile|CAPA Investigation Workflow]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** After a CAPA corrective action is implemented, FDA requires verification that the action was effective — but effectiveness checks are scheduled 60-180 days in the future, fall off people's radar, and are the most commonly missed CAPA step, directly triggering FDA 483 observations.
**Tags:** #automation #compliance #workflow-orchestration

## The Problem
CAPA effectiveness verification — confirming that the corrective action actually prevented recurrence of the problem — must occur after a defined waiting period (typically 60-180 days post-implementation) to allow enough time and production volume to observe whether the problem recurs. QMS platforms schedule the effectiveness check, but the actual verification requires the quality engineer to query complaint data, production yield data, and nonconformance data for the relevant period to determine if the problem has recurred. This query is manual, and because the effectiveness check comes months after the investigation was completed, the quality engineer has moved on to other priorities. Result: 20-35% of CAPAs have overdue effectiveness verifications at any given time at typical device manufacturers, and "inadequate CAPA effectiveness verification" is a top-5 FDA 483 citation.

## Why It's Still Broken
QMS platforms send reminder emails for overdue effectiveness checks, but the quality engineer still must manually gather the verification data (complaint recurrence, yield trends, nonconformance counts for the affected product/process). The time investment to gather this data for each verification is 2-4 hours, multiplied by 10-30 verifications coming due per month, creating a chronic backlog. The reminders generate alert fatigue. The fundamental problem is that the data needed for verification exists in other systems, but no automation pulls it and evaluates it against the CAPA's success criteria.

## What a Fix Looks Like
An automated effectiveness verification engine that, at the scheduled verification date, automatically queries complaint data, production yield, and nonconformance data for the product/process affected by the CAPA, compares the post-action data against the pre-action baseline and the CAPA's defined success criteria, and generates a verification report: "Complaint rate for Device X decreased from 2.3% to 0.4% post-action — effectiveness criterion of <1% complaint rate MET." The quality engineer reviews the auto-generated report and signs off rather than performing the data gathering manually.

## Who Feels the Pain
Quality engineers who carry chronic backlogs of overdue effectiveness verifications. Quality directors who report overdue CAPA metrics to management and face FDA scrutiny. Regulatory affairs professionals who must explain overdue effectiveness verifications to FDA inspectors.

## Impact If Fixed
Overdue effectiveness verification rate drops from 20-35% to under 5%. Time per effectiveness verification drops from 2-4 hours to 15-30 minutes of review. FDA 483 citations for inadequate CAPA effectiveness verification are largely eliminated.
