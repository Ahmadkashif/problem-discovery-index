# Dialysis Center-NEMT Real-Time Scheduling Bridge

**Niche:** [[niches/non-emergency-medical-transport/dialysis-transport-specialists/profile|Dialysis Transport Specialists]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system connects dialysis center treatment completion signals to NEMT dispatch for real-time return trip coordination, leaving patients waiting 30-90 minutes post-treatment.
**Tags:** #data-integration #workflow-orchestration #automation #ai-platform

## The Problem
A dialysis patient's treatment typically runs 3-5 hours, but the actual completion time varies by 30-60 minutes based on treatment adjustments, access complications, or facility delays. The NEMT provider schedules the return pickup at a fixed time (e.g., "pickup at 2pm"), but the patient may finish treatment at 1:30pm or 2:45pm. If the driver arrives at 2pm and the patient is not ready until 2:45pm, the driver waits 45 minutes — time that could serve other patients. If the patient finishes at 1:30pm and the driver arrives at 2pm, the post-dialysis patient sits in the lobby for 30 minutes, fatigued and potentially hypotensive, without transportation home.

## Why Nobody Has Built This
Dialysis centers run proprietary treatment management systems (DaVita's Falcon, Fresenius's FMCNA platforms) that do not expose patient completion status to external systems. NEMT dispatch software has no mechanism to receive real-time treatment status updates. Building a bridge requires API integration with dialysis center systems (which have historically been closed) or a lightweight manual interface where dialysis staff notify the NEMT provider when a patient is coming off the machine. The coordination happens across two separate organizations with no shared technology stack.

## What to Build
A lightweight integration platform that receives a "treatment completing in 15 minutes" signal from the dialysis center (via API integration, nurse tablet notification, or automated EHR trigger) and pushes this signal to the NEMT dispatch system, which then dispatches the return trip vehicle with optimal timing. For centers without API access, a simple tablet-based interface allows dialysis nurses to tap "patient coming off" for each patient, triggering the dispatch. The system learns each patient's typical treatment-to-ready time (including post-treatment recovery, vitals check, and wheelchair transfer) and adjusts dispatch timing accordingly.

## Target Customer
NEMT providers specializing in dialysis transport (typically 30-60% of their trip volume), and dialysis center administrators seeking to reduce lobby congestion and patient complaints about wait times.

## Impact If Built
Reduces average post-treatment patient wait time from 45 minutes to under 15 minutes, recovers 2-3 hours of driver time per day per fleet by eliminating facility wait time, and improves patient satisfaction scores that affect Medicaid Managed Care Organization (MCO) contract retention.
