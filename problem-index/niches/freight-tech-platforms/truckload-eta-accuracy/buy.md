# Geofencing Turned Into an Evidentiary Detention Record

**Niche:** [[niches/freight-tech-platforms/truckload-eta-accuracy/profile|Truckload — Coverage and ETA Accuracy]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Geofencing is a commodity capability every visibility platform already runs, detention is the freight industry's most argued-about cost, and detention claims are still settled from a driver's handwritten arrival and departure times.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #compliance #revenue-impact #worker-facing
**Contested on:** Every serious competitor in truckload visibility is fighting to get location from a fragmented carrier base and turn it into an arrival time a dock will plan against — and whoever holds tracked-shipment share and ETA accuracy highest takes the account.

## The Problem
A driver arrives at 09:40, waits, is loaded, and leaves at 15:10. The carrier bills detention for the hours beyond the free time. The shipper disputes the arrival time, citing its own gate log which shows 11:15 because that is when the guard processed the paperwork. The dispute is settled by negotiation, usually in favour of the party with more leverage, which is not the small carrier. Meanwhile the truck's telematics recorded its position continuously throughout, the visibility platform ran a geofence around the facility, and both parties' claims could have been settled to the minute by data that already existed.

## What Already Exists
Geofencing is trivial and universally implemented. Telematics position data is continuous and timestamped. Visibility platforms already generate arrival and departure events from geofences for their own status updates. Detention rules are written into carrier contracts and rate confirmations in a limited number of standard forms. Yard management systems at large facilities produce their own timestamps. Everything needed to settle a detention claim mechanically is already deployed.

## The Customization Gap
The adaptation is to make the record evidentiary rather than informational. It requires: (1) geofence definitions that both parties agree to in advance — the perimeter, whether a queueing area outside the gate counts as arrival, and what constitutes departure — since most detention disputes are definitional rather than factual; (2) an immutable, timestamped record with the position trace attached, so the claim carries its own evidence rather than an assertion; (3) contractual detention terms encoded per shipper so the calculation is automatic from the timestamps rather than performed by a billing clerk; (4) automatic claim generation and submission, because a substantial share of detention is never billed at all by small carriers who lack the administrative capacity to pursue it; and (5) facility-level dwell reporting back to the shipper, which is the constructive use — a receiver that can see which shifts and which doors generate its detention can fix it, and fixing it is better for both parties than arguing about the bill.

## Target Customer
Carriers of all sizes, brokerages managing accessorial disputes, visibility platforms holding the geofence data, and shippers who would rather reduce detention than dispute it.

## Impact If Solved
Detention is a large, contested and mostly avoidable cost, and settling it from telematics rather than from handwritten times removes the dispute entirely. The asymmetry matters: the party currently losing these arguments is the small carrier with the least administrative capacity, and an automatic evidentiary record is worth disproportionately more to them.
