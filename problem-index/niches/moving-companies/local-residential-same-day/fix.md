# Chronic Afternoon Schedule Overruns

**Niche:** [[niches/moving-companies/local-residential-same-day/profile|Local Residential Same-Day Movers]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Morning moves run long, afternoon customers wait 2+ hours past their window, crews work overtime, and the company pays the price in complaints, reviews, and labor cost.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #worker-facing #revenue-impact

## The Problem
Local moving schedules are optimistic by construction: the dispatcher assumes the 8am move will take 4 hours (done by noon), travel time to the next job is 30 minutes (arriving 12:30), and the 1pm move starts on time. In reality, the 8am move takes 5.5 hours (done at 1:30 because the customer had more stuff than described), travel takes 45 minutes (arriving 2:15), and the 1pm customer has been waiting since 12:45. The afternoon move now runs until 7:30pm instead of 5pm — 2.5 hours of overtime at time-and-a-half. This pattern repeats 3-5 days per week. The root cause: estimation error on the morning move cascades through the entire day, and the schedule has no buffer to absorb it.

## Why It's Still Broken
The dispatcher builds the schedule based on estimated durations, but estimates have systematic error: customers understate their inventory ("just a few boxes" turns out to be 40 boxes), access complications aren't discovered until arrival (the elevator is broken, the parking spot is 200 feet from the door), and packing isn't done even though the customer confirmed it would be. The schedule treats these estimates as certain, with no buffer for the 60-70% of moves that run over. Adding buffer "wastes" crew idle time between jobs, so the dispatcher maximizes utilization — which works on paper but fails daily in practice.

## What a Fix Looks Like
A scheduling model that uses historical move duration data (actual vs. estimated, by customer description type) to build realistic duration distributions rather than point estimates. When scheduling, the system allocates jobs with stochastic awareness: "If we schedule the morning move with a 75th-percentile duration estimate (5 hours instead of 4), we have an 85% probability of starting the afternoon move on time." Shows the dispatcher the trade-off: maximize utilization (risk overruns) vs. maximize on-time arrival (accept some crew idle time). Alerts when a morning job is running over and re-estimates downstream arrival times in real time.

## Who Feels the Pain
The afternoon customer who took time off work for a 1pm move and is still waiting at 3pm; the crew that started at 7am and won't get home until 8pm; and the owner who sees 1-star Google reviews mentioning "showed up 2 hours late" on jobs that were actually completed well once they started.

## Impact If Fixed
Reducing afternoon late arrivals from 35-40% to 10-15% prevents 2-3 negative reviews per month (each costing $1,000-$3,000 in future lost bookings) and 3-5 overtime incidents per month ($500-$1,500 each). Total impact: $3,000-$10,000/month for a 5-10 truck operation.
