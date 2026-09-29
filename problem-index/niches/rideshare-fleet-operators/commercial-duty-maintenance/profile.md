# Maintenance for Commercial-Duty Vehicles

**Parent Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Category:** Low Digitized
**Contested on:** Whether a vehicle doing forty thousand city miles a year is maintained on a schedule derived from how it is actually used.

## Profile
**Market Size:** ~$900M — 15% of US rideshare fleet services
**Share of Parent Industry:** ~15%
**Digital Adoption:** Low — consumer service intervals, a spreadsheet and a local garage
**Target Buyer:** Fleet maintenance coordinators and owners
**Automation Potential:** High — telematics supports condition-based scheduling and mostly is not used for it

## What Makes This a Distinct Niche

Vehicles doing forty thousand miles a year in stop-start city service are maintained on schedules designed for private owners doing ten. The manufacturer's interval assumes a duty cycle that bears no resemblance to rideshare use: constant idling, continuous stop-start braking, short trips that never reach operating temperature, high passenger loads, and a driver who is not the owner and has no stake in the vehicle's long-term condition.

The niche is distinct because the economics invert the usual maintenance trade-off. For a private owner, deferring service risks a repair. For a fleet, deferring service risks a breakdown that idles the asset and terminates the driver's earnings — and the idle days frequently cost more than the repair. Conversely, servicing too early wastes parts and idle days. Getting the interval right is worth real money in both directions, and nobody computes it.

## Current Tools & Gaps

Telematics provides odometer, diagnostic trouble codes, engine hours, idle time and driving behaviour. Fleet management software schedules maintenance by mileage or date. Most operators use an independent garage or a small in-house shop, with a spreadsheet tracking what is due.

The gaps are duty-cycle awareness and failure prediction. Intervals are set by mileage, which ignores that fifteen thousand city miles with heavy idling is harder on a vehicle than thirty thousand highway miles. Diagnostic codes arrive and are triaged by whoever sees them, with no model of which predict an imminent failure. And failure history across the fleet — which is a genuine dataset after a few years — is not analysed, so the operator relearns each vehicle model's weak points by experiencing them.

## Problems
- [[niches/rideshare-fleet-operators/commercial-duty-maintenance/build|🔨 Build: Duty-Cycle Maintenance Intervals and Failure Prediction]]
- [[niches/rideshare-fleet-operators/commercial-duty-maintenance/buy|🛒 Buy: Fleet Maintenance Software Adapted to a Renter Who Is Not the Owner]]
- [[niches/rideshare-fleet-operators/commercial-duty-maintenance/fix|🔧 Fix: The Driver Who Reports Nothing Until It Stops]]
