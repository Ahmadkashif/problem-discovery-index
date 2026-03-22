# Crew Efficiency Tracking Per Property

**Niche:** [[niches/landscaping/residential-maintenance/profile|Residential Maintenance]]
**Industry:** [[industries/landscaping|Landscaping]]
**Type:** Fix (Pain Point)
**One-liner:** Lawn care companies know their total daily revenue and crew hours but cannot tell which individual properties are profitable and which are money-losers — because no tool connects per-property service time to per-property revenue at scale.
**Tags:** #gradient-boosting #data-integration #revenue-impact #worker-facing

## The Problem
A residential lawn care company with 400 properties on monthly contracts has no idea which 50 properties are actually losing money. Monthly contracts are priced by estimated lot size and service level, but actual service time varies dramatically based on factors invisible at quoting time: terrain slope, obstacle density (flower beds, swing sets, garden borders requiring trimmer work), grass type and growth rate, gate access delays, and client-specific requests that accumulate over time ("can you also blow off my driveway?" becomes an unpaid 5-minute task on every visit). Companies track total crew hours per day and total daily revenue, but the ratio of crew-time-to-revenue at the individual property level is completely opaque. The result: unprofitable properties subsidized by profitable ones, and no data to support price increase conversations with clients whose properties have become more complex over time.

## Why It's Still Broken
Per-property time tracking requires either manual clock-in/clock-out at each stop (which crew members forget or fake, adding 30 seconds of friction 25 times per day) or automated GPS geofence detection (which struggles with adjacent properties in dense suburban neighborhoods where three clients may be within 200 feet of each other). Jobber and LMN both offer job-level time tracking, but for recurring maintenance the "job" is often a route of 20 properties entered as a single job, making per-property extraction impossible without restructuring the entire schedule. Even companies that have tried per-property tracking find the data noisy — a crew's time at property #12 is inflated by the 5-minute equipment refueling that happened to occur there, or deflated because the crew blew off Property #12's clippings while finishing Property #11 next door.

## What a Fix Looks Like
A lightweight time-tracking layer that uses phone GPS geofencing calibrated to individual property boundaries (using parcel data from county GIS), automatically logging arrival and departure at each property without crew intervention. Machine learning smooths the noise — a gradient-boosted model trained on 8-12 weeks of GPS data learns the typical time-per-property adjusted for visit sequence effects (first property of the day takes longer due to unloading, adjacent properties share setup time). Weekly reports show per-property profitability: revenue per visit vs. allocated crew cost per visit, ranked from most to least profitable. Properties below breakeven are flagged with a recommended price increase amount and a one-click email template to send the client.

## Who Feels the Pain
Company owners who see tight margins but can't identify which properties to reprice, operations managers who suspect certain routes are less productive but have no data to prove it, and crew leaders who know that the "easy" route finishes at 2pm while the "hard" route runs until 6pm but can't quantify the imbalance to management.

## Impact If Fixed
Identifies the bottom 10-15% of properties by profitability, enabling targeted price increases or service level adjustments worth $30K-80K in annual margin recovery for a 400-property company. Balances crew workloads by revealing actual time-per-property rather than estimated, reducing overtime costs and crew turnover driven by perceived unfair route assignments.
