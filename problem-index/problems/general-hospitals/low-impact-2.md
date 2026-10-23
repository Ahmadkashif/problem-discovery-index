# Case Durations Taken From the Surgeon's Guess

**Industry:** [[general-hospitals|General Hospitals]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every OR scheduling system already books cases, but it books them at the surgeon's own estimate or a historical average, so the day runs over or ends early and released block time is filled too late to use.
**Tags:** #gradient-boosting #bayesian-inference #monte-carlo-methods #optimization-fundamentals #evaluation-metrics #automation #revenue-impact

## The Problem
An operating room suite is scheduled in blocks: Dr A has Room 4 every Tuesday, the orthopaedic group has Rooms 6–8 on Mondays. When a case is booked, the scheduler enters a duration. That is usually the surgeon's preference-card estimate or the system's average for that surgeon and procedure code. Neither knows that this patient has a BMI of 46, that this is a revision rather than a primary, or that the second resident is new this month. The day runs long, staff go into overtime, and the last case is cancelled. Or it ends at 1 p.m. and a staffed room sits empty. Separately, surgeons release block time they will not use, often only days before. The released minutes are offered first-come-first-served and mostly go unfilled. OR time costs roughly $36–$37 a minute in a widely cited California study (recalled), so a single unused room-afternoon can cost ~$8,000–$9,000 (estimate).

## What Already Exists
Epic OpTime and Oracle's surgical modules handle booking, preference cards and block rules. LeanTaaS iQueue for Operating Rooms, Qventus Perioperative Solution and Opmed.ai sell block-utilisation analytics, release nudges and duration prediction. Generic forecasting and scheduling software, and every data team's notebook, can fit a duration model.

## The Customisation Gap
The hospital-specific logic is what generic models miss.

- **Durations.** They must be predicted per surgeon, procedure combination, patient and team, with a full distribution rather than a point. Scheduling against the 80th percentile changes overtime, while scheduling against the mean only changes the average.
- **Block rules.** Each hospital's block policy is a negotiated, political document: release deadlines by service, protected time for trauma, utilisation thresholds that trigger block reallocation. A tool has to encode these rules rather than one vendor's defaults.
- **Back-fill.** Released time needs matching to the add-on and waitlist cases that could actually use it, given equipment, anaesthesia and implant-vendor availability.

Opmed.ai reports that work with Mayo Clinic cut case-duration error substantially (company figures, not checked). The point is that the gain came from tuning to one institution's data and rules.

## Impact If Solved
Duration predictions within ~15–20 minutes for most cases (estimate), plus earlier and better-matched release, let a 20-room suite run ~2–5 more cases a week. That is worth ~$1M+ a year in contribution margin (estimate). It also cuts overtime and the cancellations that send a fasting patient home.
