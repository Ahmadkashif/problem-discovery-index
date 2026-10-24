# The Ramp Plan That Assumes the Motors Arrive

**Niche:** [[niches/defense-systems-manufacturers/missile-interceptor-production-ramps/profile|Missile & Interceptor Production Ramps]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** Ramp plans are built top-down from contracted quantities and treat sub-tier deliveries as promised, so the shortfall surfaces at final assembly.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #data-integration #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to raise delivered rounds per month on a qualified missile line, but the shortage that caps the rate sits in two places with different winners — sub-tier motors and their energetic ingredients, where whoever delivers qualified motors at rate wins, and the prime's own final assembly and acceptance test, where whoever raises first-pass yield wins. Decomposed into contested sub-niches below.

## The Problem
A ramp plan starts with the contract's delivery schedule and works backward, taking supplier commitments at face value. Motor, nozzle and igniter suppliers are themselves ramping (Breaking Defense reported nozzle lead times of seven to ten months and new igniter makers still needed in January 2026), so promised dates slip and the plan is revised only when parts fail to arrive.

## Why It's Still Broken
Supplier promise dates are the only data the plan is fed. Nobody scores each supplier's history of promise versus delivery, so a supplier that has missed every date for a year carries the same weight as one that never has.

## What a Fix Looks Like
Score every open purchase order by the supplier's own record: historical promise-date slippage by part family, current lead-time trend and the supplier's own ramp status. Replace promised dates in the plan with predicted dates and their ranges, and show programme managers the gap between contracted and predicted deliveries each week.

## Who Feels the Pain
Programme directors explaining missed deliveries, final-assembly supervisors with idle crews, and buyers expediting by phone.

## Impact If Fixed
Planning on predicted rather than promised dates exposes a motor or nozzle shortfall one to two quarters earlier (estimate), early enough to fund a second source or re-sequence the line instead of missing a delivery lot.
