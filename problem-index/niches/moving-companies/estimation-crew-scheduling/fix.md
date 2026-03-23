# Dispatcher Overload from Manual Schedule Juggling

**Niche:** [[niches/moving-companies/estimation-crew-scheduling/profile|Move Estimation & Crew Scheduling Optimization]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Dispatchers spend 60% of their day reactively reshuffling schedules via phone calls and texts because no system propagates the downstream impact of a single move running over time.
**Tags:** #workflow-orchestration #automation #worker-facing #time-series-forecasting #tabular-ml

## The Problem
Moving schedules break every day. A 4-hour move takes 6 hours. A customer isn't ready when the crew arrives. A truck breaks down. Each disruption triggers a cascade: the crew's second move of the day starts late, the customer for that move is upset, the crew may need to work overtime, or a different crew must be redirected. The dispatcher manages this entirely through phone calls and text messages — calling the delayed crew for an ETA, calling the affected customer to reset expectations, calling backup crews to see who can cover, texting the driver with a new address. A dispatcher handling 12-15 daily moves makes 40-60 reactive calls per day, each one a context switch that increases the chance of a scheduling error or a forgotten customer callback.

## Why It's Still Broken
Moving CRMs and dispatch tools show the planned schedule as a static calendar. When reality deviates, there's no propagation engine — the system doesn't know that crew A running 90 minutes late on move #1 means move #2 starts late, which means the customer's elevator reservation at the destination building may need to be pushed, which means the dock slot conflicts with another mover. The dispatcher holds all these dependencies in their head. Building a propagation engine requires real-time crew location and status data that most movers don't capture (crews report via phone call, not GPS check-in).

## What a Fix Looks Like
A real-time dispatch board where crews update status via a simple mobile app (arrived, loading, in transit, unloading, complete). When a move's actual duration exceeds the estimate by a configurable threshold (e.g., 30 minutes), the system automatically recalculates downstream ETAs for that crew's remaining moves, sends updated arrival windows to affected customers via automated text/email, flags scheduling conflicts (elevator reservations, dock slots) that need manual intervention, and suggests reassignment options if another crew can absorb a move. The dispatcher shifts from making 40-60 reactive calls to managing 5-10 exception alerts.

## Who Feels the Pain
Dispatchers who describe their job as "professional firefighter" — the constant reactive communication creates burnout, and the best dispatchers quit within 18-24 months. Company owners who lose their most operationally critical employee to stress.

## Impact If Fixed
Reduces dispatcher reactive communication from 40-60 calls/day to 10-15, cuts customer complaints about late arrivals by 50-60% (the issue isn't the delay — it's not being told about the delay), and extends average dispatcher tenure from 18 months to 3+ years by reducing the role's cognitive overload.
