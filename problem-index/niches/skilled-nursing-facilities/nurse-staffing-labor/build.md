# One Labour Ledger Across Every Source of Hours

**Niche:** [[niches/skilled-nursing-facilities/nurse-staffing-labor/profile|Nurse Staffing & Labour Supply]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A facility buys nursing hours from four sources (employees, its float pool, marketplaces and agencies) and cannot see their combined cost and coverage on any one screen.
**Tags:** #time-series-forecasting #linear-regression #feature-engineering #data-integration #revenue-impact #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor here is fighting to staff each shift at the hours residents need with the least premium labour. That is two contests with different winners: keeping the facility's own employees and float pool on the schedule, which workforce-management and scheduling vendors win, and supplying a credentialed clinician for a same-day hole, which marketplaces and agencies win. Decomposed into contested sub-niches below.

## The Problem
Employee hours live in payroll and the timeclock, float-pool hours in a regional spreadsheet, marketplace shifts in each vendor's portal and agency hours on monthly invoices. The administrator sees the overrun only at month end, after the hours have been worked. The director of nursing cannot compare what a marketplace shift costs against overtime for her own aide, at the moment she has to choose.

## Why Nobody Has Built This
Each vendor shows its own slice and has little interest in showing a competitor's prices beside its own. Payroll vendors stop at employees. Chains build spreadsheets at the regional level, and independents have no analyst to build anything.

## What to Build
A ledger that pulls hours and cost from payroll, timeclock, marketplace APIs and parsed agency invoices into one shift-level record. It shows, for each open shift, the effective cost of each option (overtime, float, marketplace, agency) and its effect on the day's hours per resident day by role. Add a monthly forecast of premium-labour spend from census and call-off history, and the same data shaped for PBJ.

## Target Customer
Chief operating officers and regional directors of operations at chains of 5–100 buildings, where premium labour is a board-level line.

## Impact If Built
Shift decisions are made on full cost. Moving ~10% of agency hours to overtime or float cover (estimate) saves ~$10,000–20,000 a year on ~$200,000 of contract nursing spend per facility (estimate, from ~5% contract hours and the ASPE premium), and the PBJ file matches the hours actually bought.
