# Jobber Scheduling with Route Intelligence

**Niche:** [[niches/landscaping/residential-maintenance/profile|Residential Maintenance]]
**Industry:** [[industries/landscaping|Landscaping]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Jobber handles scheduling and invoicing for thousands of lawn care companies but shows properties as pins on a map without sequencing them, clustering them by crew capability, or flagging route inefficiencies — leaving the hardest operational decision (daily routing) entirely manual.
**Tags:** #gradient-boosting #automation #data-integration #workflow-orchestration

## The Problem
Jobber is the default platform for residential lawn maintenance companies with 2-15 employees. It manages client records, recurring job scheduling, invoicing, and a basic map view of daily jobs. But the map view is read-only — it shows where today's jobs are without suggesting the order to visit them, which crew should take which cluster, or whether moving three Thursday clients to Wednesday would save 40 minutes of drive time. Every morning, the operations manager opens Jobber, looks at the map, and mentally sequences the day's route — the same cognitive task they'd do with pushpins on a paper map. For companies with 5+ crews hitting 80+ properties daily, this is a 30-60 minute planning session every morning that produces inconsistent results depending on who's doing it.

## What Already Exists
Jobber's scheduling provides recurring job templates, a calendar view, and a map view showing job locations for any given day. The map uses color-coded pins by crew assignment. Jobber also recently added "route optimization" as a feature label, but it only reorders stops for a single pre-assigned crew — it doesn't reassign jobs between crews, account for equipment constraints, or learn from historical completion times. Generic route tools (Google Maps multi-stop, OptimoRoute) can sequence stops but don't integrate with Jobber's scheduling data, requiring manual re-entry.

## The Customization Gap
Three capabilities are missing from Jobber's scheduling for residential maintenance. First, inter-crew route optimization: reassigning properties between crews to maximize geographic density per crew per day, respecting constraints like "this property needs the 60-inch mower that's only on Truck 2." Second, time-per-property prediction: using historical job completion data already in Jobber to estimate actual service time per property (not the uniform 30-minute default), so the system can realistically load-balance crew days to 8 hours instead of having one crew finish at 2pm and another at 6pm. Third, weather-cascade rescheduling: when rain cancels a service day, automatically rebatching those properties into the remaining week with minimal route disruption — a task that currently takes the ops manager 45-90 minutes of manual calendar shuffling and client notification.

## Target Customer
Residential lawn care companies with 3-10 crews already on Jobber ($60-250/month plan), generating $300K-3M in annual revenue, where the owner or operations manager spends 30-60 minutes daily on route planning and 1-2 hours on rain-day rescheduling.

## Impact If Solved
Reduces daily route planning time from 30-60 minutes to under 5 minutes. Eliminates the 1-2 hour rain-day rescheduling task that currently causes client communication gaps and missed properties. Balances crew workloads to within 30 minutes of each other daily, reducing overtime costs by $500-1,500/week during peak season.
