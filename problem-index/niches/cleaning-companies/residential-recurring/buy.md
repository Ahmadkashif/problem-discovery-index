# Route-Optimized Scheduling for Dense Markets

**Niche:** [[niches/cleaning-companies/residential-recurring/profile|Residential Recurring Services]]
**Industry:** [[industries/cleaning-companies|Cleaning Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic route optimization tools solve for delivery stops, not for 2-4 hour cleaning appointments with cleaner-specific constraints.
**Tags:** #reinforcement-learning #automation #workflow-orchestration

## The Problem
Residential cleaning margins depend on route density — every minute a cleaner spends driving between homes is unpaid time. But scheduling isn't a simple routing problem: homes have preferred time windows, specific cleaner assignments, variable job durations based on home size, and recurring patterns (every Tuesday, biweekly Thursdays). A new booking or cancellation cascades through the entire week's schedule.

## What Already Exists
Route optimization tools like OptimoRoute, Routific, and Google OR-Tools handle delivery routing well. Cleaning-specific platforms like ZenMaid and Launch27 offer basic scheduling but no route optimization. Neither category handles the specific constraints of residential cleaning: multi-hour appointments, cleaner-client loyalty, recurring weekly patterns, and dynamic rescheduling when a cleaner calls in sick.

## The Customization Gap
The optimization engine needs to balance travel time against cleaner-client preferences (Mrs. Johnson only wants Maria), time window constraints (no arrivals before 9am), job duration variability (a 3-bedroom takes 2.5 hours, a studio takes 1 hour), and recurring schedule stability (don't shuffle everyone's day every week). It also needs a real-time rebooking mode for same-day callouts.

## Target Customer
Cleaning company operators in dense metro areas with 15+ cleaners whose daily drive time exceeds 20% of work hours.

## Impact If Solved
Reducing average daily drive time by 25% adds roughly one extra job per cleaner per day — at $150/job, that's $750/week per cleaner in recovered capacity.
