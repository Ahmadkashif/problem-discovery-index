# The STAT Report Stuck Behind Routine Dictation

**Niche:** [[niches/document-preparation-services/medical-transcription-documentation/profile|Medical Transcription & Healthcare Documentation Editing]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Fix (Pain Point)
**One-liner:** Work queues sort by arrival and by a turnaround category set when the job was created, so an urgent operative note can sit behind a morning's worth of routine letters.
**Tags:** #gradient-boosting #time-series-forecasting #workflow-orchestration #automation #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to return a health system's residual dictation — the reports front-end speech recognition and ambient scribes don't absorb — inside contract turnaround at an AHDI score of 98 or better, and whoever holds turnaround and accuracy at the fewest editor minutes per line takes the account.

## The Problem
Contracts set turnaround by report type: STAT and emergency reports in an hour or two, operative notes and discharge summaries same day, routine letters within a day or more. Queues are configured by job type at creation, and real urgency is often wrong or missing: a discharge summary that blocks a patient leaving, a radiology addendum a surgeon is waiting on. Editors pick up work in the order the queue presents it, and breaches are discovered in the monthly turnaround report.

## Why It's Still Broken
Queue rules are set once per account and rarely revisited. Dictation volume swings by hour and weekday while editor schedules are fixed weeks ahead, and no one forecasts the gap.

## What a Fix Looks Like
Priority recomputed continuously from turnaround clock remaining, report type, the patient's encounter status from the EHR feed (pending discharge, in surgery) and predicted editing time. Add a short-horizon volume forecast that tells the coordinator, hours ahead, which turnaround bands will breach on the current schedule.

## Who Feels the Pain
Clinicians waiting on reports; HIM directors paying for service levels that slip; vendors absorbing service credits; editors pulled off one job to rescue another.

## Impact If Fixed
Fewer turnaround breaches without more editors, and service credits that fall rather than recur every month.
