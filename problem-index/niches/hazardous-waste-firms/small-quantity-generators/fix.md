# The Pickup That Comes After the Limit

**Niche:** [[niches/hazardous-waste-firms/small-quantity-generators/profile|Small & Very Small Quantity Generators]]
**Industry:** [[industries/hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A small generator's drum sits past its accumulation limit because the route was rescheduled for density, and the shop, not the collector, takes the citation.
**Tags:** #time-series-forecasting #optimization-fundamentals #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a small generator compliant on a scheduled pickup it never has to think about, and whoever keeps the most customer sites free of accumulation-limit citations takes the account.

## The Problem
Route planners merge and stretch routes to fill trucks. A customer on a ~90-day cycle drifts to ~120 days after two reschedules (estimate), and its container passes the limit without anyone noticing.

## Why It's Still Broken
Route software optimises miles and stops; it does not know each customer's limit or when its container started filling.

## What a Fix Looks Like
Add each site's last pickup, container start dates and limit to the route plan as a hard deadline, alert the planner before a reschedule breaks it, and let the customer request an early pickup with one tap.

## Who Feels the Pain
Shop owners facing inspectors; route planners juggling density against service; branch managers losing accounts after a citation.

## Impact If Fixed
Preventing a single citation saves a small shop a penalty that can run to thousands of dollars (estimate); keeping 1% more of 50,000 small accounts (estimate) is ~500 sites retained a year for a large route business.
