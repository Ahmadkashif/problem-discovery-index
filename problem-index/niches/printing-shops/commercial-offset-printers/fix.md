# Makeready Time Unpredictability

**Niche:** [[niches/printing-shops/commercial-offset-printers/profile|Commercial Offset Printers]]
**Industry:** [[industries/printing-shops|Printing Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Makeready time varies 15-45 minutes per job with no way to predict which jobs will be quick and which will be long — wrecking production schedules and causing missed ship dates 2-3 times per week at a typical mid-size shop.
**Tags:** #workflow-orchestration #revenue-impact #worker-facing

## The Problem
The production scheduler allocates makeready time per job based on a standard allowance (e.g., 30 minutes for a 4-color job). Actual makeready varies from 15 minutes (repeat job, same substrate as previous job, pressman knows the color profile) to 45+ minutes (new job, difficult-to-match PMS color, substrate change, pressman unfamiliar with the job). The scheduler has no way to predict which jobs will be fast and which will be slow, so the schedule is inaccurate by 1-3 hours per shift. When makeready runs long, subsequent jobs are delayed, overtime is required, or ship dates are missed. The pressman cannot tell the scheduler in advance how long makeready will take because the pressman does not know until they are on press.

## Why It's Still Broken
Makeready time depends on variables that interact in complex ways: substrate change (same stock as previous job = fast, different stock = slow), ink change (same ink set = fast, PMS custom mix = slow), job complexity (solid coverage = fast to match, fine gradients = slow), pressman familiarity (repeat job = fast, new job = slow), and press condition (recently cleaned = predictable, end-of-shift = variable). No scheduling system models these interactions. Shops track actual makeready time in the MIS but do not use historical data to predict future makeready.

## What a Fix Looks Like
A makeready time prediction module that connects to the MIS job history (actual makeready time per job with substrate, ink, job complexity, press, and operator attributes) and the production schedule (which job follows which on which press). For each scheduled job, it predicts makeready time based on the job's characteristics and the preceding job's characteristics (changeover complexity). The scheduler sees predicted makeready per job rather than a flat standard allowance, enabling more accurate scheduling. Predicted total shift time becomes accurate to within 15-30 minutes instead of 1-3 hours.

## Who Feels the Pain
Production schedulers whose schedules are unreliable by mid-shift. Pressmen who are blamed for "slow" makeready when the job was inherently difficult. Shop owners who approve overtime to catch up on delayed schedules. Customer service reps who must call customers to report delayed ship dates.

## Impact If Fixed
Schedule accuracy improves from +/-3 hours to +/-30 minutes per shift. Overtime from schedule overruns decreases by 30-50%. Missed ship dates decrease by 40-60%. The shop can take on 5-10% more work per shift by scheduling more accurately to available time.
