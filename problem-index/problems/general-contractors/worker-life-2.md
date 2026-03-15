# Schedule Delay Cascade Prediction

**Industry:** [[general-contractors|General Contractors]]
**Type:** Worker Life Changing
**One-liner:** Project managers who currently discover schedule problems only after they've cascaded across multiple dependent trades — when recovery is expensive and the owner is already notified — get an early-warning system that flags delay risks 2-3 weeks before they materialize, while recovery options still exist.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #worker-facing

## The Problem
Construction schedules are dependency networks: drywall can't start until rough-in is complete; flooring can't start until drywall is painted; millwork installation depends on flooring. When a trade falls behind, the delay propagates through all dependent activities in a cascade that the project manager must manually trace and resequence. The problem is timing: project managers typically discover that a trade is running behind when the trade is significantly behind — when the crew is already 5-7 days late and the downstream trades are already being impacted. At that point, recovery options are limited and expensive: overtime, crew acceleration, activity resequencing all cost money. If the delay had been identified when it was 1-2 days behind schedule, recovery would have been straightforward and inexpensive.

## Why It Matters to the Worker
Project managers on large projects manage 15-30 active subcontractors simultaneously across multiple work areas. The cognitive load of tracking each trade's progress, comparing it against the schedule, and identifying developing delays is immense — and it's impossible to do with precision when the superintendent's day is dominated by problem-solving rather than schedule monitoring. Project managers who consistently deliver on schedule and budget command premium compensation and career advancement; those who let delays cascade report feeling perpetually behind, constantly apologizing to owners, and firefighting rather than managing. The difference between the two outcomes often comes down to delay detection timing.

## What a Solution Looks Like
A schedule analytics model that ingests daily progress updates (from DFRs, inspector logs, or superintendent check-ins), compares actual percent-complete by activity against the scheduled percent-complete, identifies activities with negative float trends, and models the cascade impact of current delays on all downstream activities — producing a 2-3 week lookahead alert: "Framing in Building A north wing is currently 4 days behind schedule; at current crew velocity, this will delay MEP rough-in by 6 days and push drywall start by 8 days. Impact on substantial completion: 6-12 days." The project manager receives this alert when there's still time to accelerate framing rather than after MEP is already delayed.

## Impact If Solved
Reduces unrecovered schedule delays by an estimated 30-50% — the difference between catching a 4-day delay when it's 1-2 days and when it's 7+ days. On a project where each week of delay costs $20,000-100,000 in owner penalties or general condition costs, an early-warning system pays for itself in a single prevented cascade event.
