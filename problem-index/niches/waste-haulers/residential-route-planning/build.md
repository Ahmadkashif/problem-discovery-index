# Routes Planned From Observed Stop Times, Not Averages

**Niche:** [[niches/waste-haulers/residential-route-planning/profile|Residential Route Planning & Rebalancing]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Route optimisers assume a standard service time per home, while lift telemetry already records the real time at every stop, which varies by density, cart placement, set-out rate and season.
**Tags:** #gradient-boosting #time-series-forecasting #dynamic-programming #feature-engineering #automation
**Contested on:** Every serious competitor in this niche is fighting to build residential routes that drivers finish as planned, and whoever leaves the smallest gap between planned and actual route hours takes the account.

## The Problem
A rebalance uses a homes-per-hour assumption by area type. Real time per stop depends on whether carts are at the curb or behind fences, how many households set out each week, parked cars, and the season (yard waste in spring, holiday volume in December). Routes planned on averages run long in some areas and short in others.

## Why Nobody Has Built This
Optimiser vendors sell the solver and leave service-time inputs to the customer; telematics sits in a separate system; and route managers rebalance rarely, so the investment in better inputs is never made.

## What to Build
A stop-time model learned from arm-cycle timestamps and GPS: predicted service and travel time per stop by day of week and season, fed into the optimiser. After go-live, compare actual route hours with plan per route and feed the residuals back. Experienced drivers' actual sequences become candidate solutions.

## Target Customer
Route managers at haulers with 50+ residential routes and lift telemetry.

## Impact If Built
Cutting the planned-versus-actual gap from ~1 hour to ~20 minutes per route-day (estimate) on 100 routes saves ~15,000 overtime hours a year.
