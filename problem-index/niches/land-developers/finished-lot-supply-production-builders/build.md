# Lot Delivery Forecast Tied to the Takedown Schedule

**Niche:** [[niches/land-developers/finished-lot-supply-production-builders/profile|Finished-Lot Supply to Production Builders]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Developers promise builders delivery dates from a superintendent's judgement, when the record of how long each city, inspector and utility actually took on past phases could predict them.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver finished lots into each builder's takedown schedule, phase by phase, and whoever delivers the highest share of contracted lots by the contract delivery date takes the account.

## The Problem
A phase becomes deliverable lots only after a chain of events the developer partly controls: grading complete, utilities installed and tested, paving, city inspection and acceptance of public improvements (or a bond posted), plat recorded, and electric, gas and fibre service installed. The takedown contract fixes the date the builder expects. The superintendent's estimate of when each link will finish is experience; the developer's management sees a date, not a distribution, and finds out a phase is late when the builder calls.

## Why Nobody Has Built This
Horizontal development is a small software market next to vertical construction, and each developer's data sits in different places: drone scans with one vendor, inspections on a city portal, utility work orders in emails, the takedown schedule in a spreadsheet. Builders who care most about the date do not own the developer's records. Nobody has joined them.

## What to Build
A delivery model at lot or block level. It ingests progress from drone scans and grade checks, subcontractor reports, city inspection results and utility work-order status, plus the takedown schedule. It learns durations per jurisdiction, inspection type and utility provider from the developer's past phases, using survival models that handle phases still in progress. It outputs a predicted delivery date with an interval for each lot, the critical waits, and the takedown quantities at risk per quarter. Every forecast is logged and graded against actual delivery.

## Target Customer
VPs of land development and division presidents at lot developers delivering a few thousand lots a year to several builders, and land-banking platforms that need their developers' delivery risk.

## Impact If Built
A developer that sees a late phase two months early can re-sequence crews, push a utility or post a bond, and keep the builder's takedown. A quarter's slip on 200 lots defers ~$21.7M of lot revenue at Forestar's average of $108,400 a lot and adds ~$0.5M of carry at ~10% a year on that value (estimate), before any damage to the builder's next contract.
