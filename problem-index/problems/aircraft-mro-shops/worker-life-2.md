# The Hangar Planner Promising a Return-to-Service Date

**Industry:** [[aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Worker Life Changing
**One-liner:** A heavy-check planner commits to a redelivery date before anyone has opened the aircraft, then spends the check explaining to an angry customer why the non-routine findings, the parts waits and the missing inspectors moved it.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #worker-facing #workflow-orchestration #revenue-impact

## The Problem
A heavy airframe check (a C-check on a narrowbody, a major inspection on a business jet) is quoted and slotted months ahead from the routine work package: the task cards the maintenance programme calls for, with standard hours. The planner who owns the check knows the routine package is only half the story. Once panels come off, inspectors raise non-routine cards for corrosion, cracks, worn bushings and chafed wiring. On an older aircraft those can equal or exceed the routine hours (recalled industry range). Each non-routine card may need an engineering disposition, an approved repair, a part with a lead time of weeks, or an inspector with a specific authorisation who is already booked on another aircraft.

The planner rebuilds the schedule every morning in a spreadsheet beside the maintenance system: which cards are blocked on parts, which on engineering, which on manpower. Then they decide what to tell the customer. The customer's own clock is fixed. The aircraft is in their summer schedule, a lease return date, or a charter booked for the following week. Every day late carries a penalty clause or a lost revenue argument, and every change order for the extra non-routine work turns into a negotiation.

## Why It Matters to the Worker
The planner carries a promise they had no data to make and no authority to keep. When the date slips they are the one on the morning call with the airline's representative, defending numbers produced by findings nobody could have seen at quote time. They spend the day as a dispatcher and a negotiator instead of a planner. Experienced planners carry a private sense of how much non-routine work a given tail number, operator or aircraft age will produce, and that sense leaves with them.

At smaller shops the planner is often also the quoting estimator, so their own guess at quote time becomes the stick they are beaten with a month later.

## What a Solution Looks Like
At quote time, a forecast of non-routine labour and parts by zone and ATA chapter, built from the shop's own past checks on the same type, age and operator. Each figure would come with a range, not a single date. During the check, a daily forecast of the remaining critical path that updates as cards are raised, showing which blocked cards (parts, engineering, inspector) actually drive the end date. Then a customer update that drafts itself from that state, with the change orders attached and justified by finding.

## Impact If Solved
A planner managing four or five concurrent checks could get back ~1–2 hours a day of manual re-planning and status reporting (estimate). Quoting with a realistic non-routine allowance, plus earlier warning of slips, could cut late redeliveries and the penalty disputes that follow by a third or more (estimate). That is worth tens of thousands of dollars a day of slot time on a widebody (estimate).
