# Call-Off Forecasting That Books Standby Cover Before 5 a.m.

**Niche:** [[niches/skilled-nursing-facilities/internal-scheduling-retention/profile|Internal Scheduling, Float Pools & Retention]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Call-offs follow patterns by day, shift, pay period and person, yet every facility treats each one as a surprise.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #optimization-fundamentals #worker-facing #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to fill the facility's schedule from its own employees and float pool before any outside labour, and whoever cuts agency hours furthest without letting reported hours per resident day fall below the staffing-star cut points takes the account.

## The Problem
The staffing coordinator fills call-offs reactively, starting before dawn. The same shifts go short every week (Sunday days, the shift after payday, holiday weekends), and the same few employees account for a large share of call-offs (estimate). Nothing in the scheduling system anticipates them.

## Why Nobody Has Built This
Scheduling vendors sell schedule building and timekeeping, not prediction. Attendance history sits in timeclock data that is rarely analysed. Facilities fear that predicting individual absences will look punitive.

## What to Build
A model trained on the facility's own timeclock and schedule history (day, shift, unit, pay cycle, weather, local school calendars, recent overtime and individual attendance) that predicts call-off risk for each scheduled shift a week ahead. It books paid standby or float cover for the highest-risk shifts. When a call-off comes, it offers the shift first to the employees most likely to accept, within overtime limits, with one-tap acceptance. Individual risk is shown only to the coordinator, framed as planning, not discipline.

## Target Customer
Directors of nursing and staffing coordinators at facilities with frequent same-day agency bookings; regional operations leaders running float pools.

## Impact If Built
Cutting same-day agency bookings by a quarter (estimate) saves ~$50,000 a year on ~$200,000 of contract nursing spend per facility. That spend estimate comes from contract labour at ~5% of hours (CLA, LTCCC) priced 59–80% above employed staff (ASPE, 2021). Dawn scrambles shrink and reported staffing steadies.
