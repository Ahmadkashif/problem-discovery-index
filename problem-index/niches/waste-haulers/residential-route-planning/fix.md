# The Rebalance Nobody Checks After Go-Live

**Niche:** [[niches/waste-haulers/residential-route-planning/profile|Residential Route Planning & Rebalancing]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Fix (Pain Point)
**One-liner:** A route rebalance is planned for weeks, launched in a day, and never measured, so drivers quietly fix the plan by running their own sequences and the next rebalance starts from the same wrong assumptions.
**Tags:** #descriptive-statistics #time-series-forecasting #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to build residential routes that drivers finish as planned, and whoever leaves the smallest gap between planned and actual route hours takes the account.

## The Problem
After a rebalance, some routes run long and drivers trade stops or reorder them; the plan in the system and the route on the street diverge within weeks.

## Why It's Still Broken
Planning is a project with an end date; nobody owns the comparison of plan and actual, and telematics reports are read for exceptions, not for plan quality.

## What a Fix Looks Like
An automatic planned-versus-actual report per route for the 8 weeks after go-live: hours, sequence divergence, missed stops and overtime, with suggested adjustments.

## Who Feels the Pain
Drivers working the long routes; route managers fielding complaints; dispatchers covering overtime.

## Impact If Fixed
Catching the worst-planned tenth of routes in the first month (estimate) removes most of the overtime a rebalance creates, often ~1–2 hours per affected route-day.
