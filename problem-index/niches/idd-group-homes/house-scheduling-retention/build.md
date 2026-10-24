# Standby Cover Booked Before the Call-Off Comes

**Niche:** [[niches/idd-group-homes/house-scheduling-retention/profile|House Scheduling, Overtime & First-Year Retention]]
**Industry:** [[industries/idd-group-homes|IDD Group Homes]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Call-offs cluster by day, house and tenure, yet every one is handled as a surprise that ends with someone forced to stay.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #optimization-fundamentals #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to cover every house's shifts from the agency's own trained DSPs without forcing anyone to stay, and whoever cuts mandated overtime shifts per house furthest takes the account.

## The Problem
The same shifts go short every week: weekend evenings, the shift after payday, a new hire's fourth week (estimate). House managers fill them by text at the last minute, and when nobody answers, the DSP on shift is mandated.

## Why Nobody Has Built This
Scheduling modules build rosters and record hours; they do not predict. Timeclock history is rarely analysed, and per-resident qualifications live in training records the scheduler cannot see.

## What to Build
A forecaster trained on the agency's own schedule and timeclock history that scores call-off risk per shift a week ahead. It books paid standby from DSPs qualified for that house's residents for the riskiest shifts. When a call-off comes, it offers the shift to qualified staff in order of likely acceptance, within overtime limits. It ranks mandated overtime by person and stops anyone being forced twice in a fortnight.

## Target Customer
Directors of residential services at agencies with 20+ homes, and record-system vendors adding scheduling intelligence.

## Impact If Built
Cutting mandated doubles by ~50% (estimate) gives the most reliable DSPs back their days off and removes the first-year experience most associated with leaving. Overtime premium falls as standby replaces doubles.
