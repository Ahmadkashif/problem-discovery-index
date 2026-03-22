# Truck Inventory Tracking and Predictive Restocking

**Niche:** [[niches/plumbing-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Plumbers drive back to the supply house 1-3 times per day because nobody tracks what parts are on each truck — a mobile inventory system with predictive restocking based on scheduled job types would eliminate $50-150/day in wasted drive time per technician.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #automation #revenue-impact #worker-facing

## The Problem
A residential service plumber's truck is a rolling warehouse carrying $3,000-8,000 in parts — fittings, valves, supply lines, water heaters, drain parts, and specialty tools. No plumbing FSM platform tracks truck-level inventory. When a plumber arrives at a job and discovers they need a 3/4" SharkBite coupling they don't have, they drive 20-40 minutes round trip to the supply house. This happens 1-3 times per day per tech across the industry. For a 10-truck operation, that's 10-30 unproductive supply house trips per day, each costing $50-150 in lost billable time plus fuel. The plumber's frustration compounds — they know the trip is wasted time, but nobody restocks their truck systematically.

## Why It's Still Broken
Truck restocking is the plumber's personal responsibility, done ad hoc at the end of a long day or during a morning stop at the supply house. Experienced plumbers develop an intuitive sense of what to carry based on the season (more water heaters in winter), the neighborhoods they serve (older homes need different fittings than new construction), and their own job mix. This is tacit inventory knowledge — a 15-year veteran's truck is always stocked right, while a 2-year journeyman makes 3 supply house runs a day. No system captures this institutional knowledge. The parts themselves are cheap ($2-50 each for fittings) so the inventory carrying cost is negligible — the cost is entirely in wasted windshield time when the part isn't there.

## What a Fix Looks Like
A mobile app where the plumber scans or taps to log parts used at each job (integrated with their FSM's job completion workflow). A predictive restocking engine analyzes scheduled jobs for the next day, historical parts usage by job type, and current truck inventory to generate a per-truck restocking list each evening. The list is sent to the supply house for will-call pickup or to a warehouse runner who pre-stages parts. Over time, a gradient-boosted model trained on job type, property age, zip code, and season predicts which parts each job will require with 80-90% accuracy, enabling proactive restocking before the plumber even knows what they'll need.

## Who Feels the Pain
The technician who loses 45-90 minutes of billable time per day on supply house runs, and the owner who watches truck utilization hover at 55-65% when it should be 80%+.

## Impact If Fixed
Eliminating 1-2 supply house trips per tech per day across a 10-truck operation recovers $75K-200K in annual billable time. The predictive restocking model, once trained on 6 months of parts usage data, can maintain 90%+ first-trip parts availability compared to the current 65-70% industry average.
