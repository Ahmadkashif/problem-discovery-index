# Crew-to-Move Assignment Optimization

**Niche:** [[niches/moving-companies/estimation-crew-scheduling/profile|Move Estimation & Crew Scheduling Optimization]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Workforce scheduling and route optimization tools exist for field services but don't account for moving-specific constraints — variable job duration by cubic footage, crew skill matching to move complexity, and truck capacity as a binding constraint alongside labor.
**Tags:** #reinforcement-learning #regression #tabular-ml #automation #workflow-orchestration

## The Problem
A dispatcher managing 15 moves per day across 6 crews must solve a combinatorial problem every morning: which crew goes to which move, in what order if a crew has two moves, which truck(s) each crew takes, and how to handle the inevitable mid-day disruptions (a move running 2 hours long, a crew member calling out, a customer rescheduling). The dispatcher makes these decisions from memory and gut feel — they know crew A handles piano moves well, crew B is fast but rough with fragile items, and truck #3 has a lift gate needed for the commercial job. This tacit knowledge produces decent schedules but can't optimize across 15 simultaneous constraints the way an algorithm can.

## What Already Exists
Field service management platforms (ServiceTitan, Jobber, Housecall Pro) handle technician scheduling with route optimization. Workforce management tools (Deputy, When I Work) handle shift scheduling. Route optimization engines (Route4Me, OptimoRoute) minimize drive time across multiple stops. All three categories solve parts of the dispatcher's problem, but none combines labor scheduling, route optimization, and capacity planning (truck cubic footage) into one decision.

## The Customization Gap
The scheduling engine needs moving-specific inputs: estimated cubic footage per move (determines truck selection), estimated labor-hours (determines whether a crew can do one or two moves per day), crew skill profiles (piano handling, stair work, commercial experience), truck specifications (cubic footage, lift gate, number of dollies), and real-time duration updates from crews in the field. The optimizer must jointly solve crew assignment, truck assignment, and route sequencing — not treat them as independent problems. It must also handle re-optimization when a morning move runs long and the afternoon schedule needs reshuffling.

## Target Customer
Dispatchers at moving companies running 8-30 moves per day who currently build the daily schedule manually in 60-90 minutes each morning and spend another 2-3 hours adjusting it throughout the day.

## Impact If Solved
Reduces average drive time between moves by 15-20% (saving fuel and labor), improves crew utilization from 75% to 85-90% (more billable hours per crew per day), and cuts dispatcher schedule-building time from 90 minutes to 15 minutes. Net impact: $3,000-8,000/month in labor and fuel savings for a 10-crew operation.
