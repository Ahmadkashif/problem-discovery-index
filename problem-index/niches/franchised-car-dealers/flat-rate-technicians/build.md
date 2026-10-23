# A Bay-Side Queue That Ends the Walk to the Counter

**Niche:** [[niches/franchised-car-dealers/flat-rate-technicians/profile|Flat-Rate Technicians]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A flat-rate technician loses unpaid time walking to the parts counter and the advisor's desk; nothing measures it or removes it.
**Tags:** #time-series-forecasting #gradient-boosting #workflow-orchestration #worker-facing #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to cut the unpaid minutes between jobs — waiting for parts, approvals and repair information — and whoever raises technicians' flagged hours per clocked hour takes the account.

## The Problem
Between flagging one job and starting the next, a technician requests parts, waits for an advisor to get approval, looks up a procedure, waits for an alignment rack. Each step is a walk or a wait, unpaid, and invisible in reports that show only flagged and clocked hours.

## Why Nobody Has Built This
Technicians are not the buyer; managers buy dispatch tools that assign work, not tools that remove friction from the bay.

## What to Build
A bay-side app tied to the DMS: parts requested from the bay with a pick-up time, approval status pushed when the customer approves, the next job pre-staged with parts and procedure before the current one ends, and a log of wait time by cause for the service manager.

## Target Customer
Service managers at stores where technician turnover and capacity limit car count.

## Impact If Built
Recovering ~20 minutes of waiting per technician per day (estimate) is roughly 7 flagged hours a month each; for 15 technicians, ~100 billable hours a month.
