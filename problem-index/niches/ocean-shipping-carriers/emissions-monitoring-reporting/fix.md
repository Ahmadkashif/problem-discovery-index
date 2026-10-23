# The Bunker Delivery Note That Doesn't Match the Noon Report

**Niche:** [[niches/ocean-shipping-carriers/emissions-monitoring-reporting/profile|Emissions Monitoring, Reporting & Verification]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Fuel delivered, fuel reported burned and fuel remaining on board rarely add up, and the gap is found by the verifier rather than by the ship.
**Tags:** #gaussian-processes #evaluation-metrics #compliance #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a fleet's noon reports and fuel records into emissions figures a verifier accepts before 31 March, and whoever gets the most ships' reports verified with no corrections takes the account.

## The Problem
The bunker delivery note says 1,200 tonnes; the sum of daily consumption since the last stem plus the remaining-on-board figure implies 1,150. The difference may be a measurement error, a sounding taken at a bad trim, or a quantity dispute with the supplier. It surfaces months later as a verifier's query on the emissions report.

## Why It's Still Broken
Nobody reconciles fuel continuously. Each party checks its own figure: the chief engineer the soundings, the office the invoice, the performance team the consumption.

## What a Fix Looks Like
A running fuel balance per ship that reconciles every delivery, daily consumption and sounding, flags gaps above a tolerance the day they appear, and asks the chief engineer a specific question while the evidence is still on board.

## Who Feels the Pain
Chief engineers queried months after the fact, fleet performance managers preparing for verification, and compliance teams facing corrections near 31 March.

## Impact If Fixed
Catching a 50-tonne delivery shortfall (estimate) while it can still be claimed, at ~$600 per tonne of VLSFO (estimate), recovers ~$30,000 per stem and removes a verifier correction later.
