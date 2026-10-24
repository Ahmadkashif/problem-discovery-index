# Stability-Window Routing for Lab Couriers

**Niche:** [[niches/clinical-laboratories/specimen-logistics-courier-networks/profile|Specimen Logistics & Courier Networks]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Courier routes are planned around miles and habit, while the thing that matters is how long each specimen has been out of the patient.
**Tags:** #time-series-forecasting #exponential-smoothing #optimization-fundamentals #monte-carlo-methods #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get specimens from practices and patient service centres to the bench inside their stability windows, and whoever delivers the lowest rate of rejected or recollected specimens per thousand picked up takes the account.

## The Problem
A regional lab runs dozens of routes a day, each a loop of 20–40 stops planned once and adjusted by drivers. Practices draw at different times, and some of their specimens need to reach the lab within hours or be spun on site. The lab cannot see which specimens are waiting where, or how old they are, until they arrive.

## Why Nobody Has Built This
Generic route optimisers minimise distance or time with delivery windows; they do not model specimens ageing at each stop, practice draw patterns or the test-specific stability limits that decide whether a pickup is worth an extra loop. Lab IT owns the LIS, not the fleet.

## What to Build
Forecast specimens and readiness per stop and hour from history, practice schedules and electronic orders placed that day. Solve routes that minimise expected out-of-window specimens subject to driver hours, with stochastic travel times. Re-plan intraday when a practice places a time-critical order. Close the loop by joining each rejection or stability-related comment to its route, pickup time and transit minutes.

## Target Customer
Logistics directors at regional and outreach labs running 20–200 routes a day.

## Impact If Built
Cutting stability-related rejections by a third on a lab rejecting 2 per 1,000 specimens out of 15,000 a day avoids ~2,500 recollections a year (estimate), each a patient recalled and a delayed result.
