# A Reading-Capacity Forecast Tied to the Scan Schedule

**Niche:** [[niches/diagnostic-imaging-centers/radiologist-reading-capacity/profile|Radiologist Reading Capacity]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Centres book scans weeks ahead but staff reading by the day, so Monday's backlog is a surprise every week.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #workflow-orchestration #automation #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor here is fighting to get every study a centre acquires read and reported. But outsourced reading contracts are won by whoever covers the highest share of a centre's after-hours and overflow studies with major-discrepancy rates under the contract threshold, and reading software is won by whoever raises studies finalised per radiologist hour without more addenda. Different buyers, vendors and costs of failure, so the niche is decomposed into contested sub-niches below.

## The Problem
The scan schedule knows how many brain MRIs, prostate MRIs and chest CTs will be acquired each day next week. The reading roster does not use it. Subspecialty reads (neuro, MSK, breast, body) pile up when the one subspecialist is away, and overflow goes to teleradiology at premium rates decided the same morning.

## Why Nobody Has Built This
Scheduling and reading live in different systems, often run by different companies: the centre and the radiology group. Neither owns both sides of the data.

## What to Build
A forecast of reading demand by subspecialty, licence state and hour, generated from the booked schedule and historical acquisition-to-read lags. It is matched against the group's roster and teleradiology contract terms. It recommends shift changes, overflow pre-bookings and which study types to route outside before the backlog forms.

## Target Customer
Operators that hold their own reading contracts with several groups, and groups reading for multiple centres.

## Impact If Built
Turning same-day overflow into pre-booked coverage would cut turnaround breaches and premium overflow spend. At a mid-size operator that is plausibly 10%–20% of a seven-figure overflow budget (estimate).
