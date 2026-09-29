# Truckload — Coverage and ETA Accuracy

**Parent Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in truckload visibility is fighting to get location from a fragmented carrier base and turn it into an arrival time a dock will plan against — and whoever holds tracked-shipment share and ETA accuracy highest takes the account.

## Profile
**Market Size:** ~$1.4B US domestic truckload visibility
**Share of Parent Industry:** ~18% of freight technology revenue
**Digital Adoption:** High — electronic logging device mandates put a telematics device in essentially every truck
**Target Buyer:** Shipper supply chain leaders and brokerage operations directors
**Automation Potential:** Very High — location is available and the prediction on top of it is barely attempted

## What Makes This a Distinct Niche
Domestic truckload is the mode where the raw data problem is already solved by regulation. Electronic logging device requirements mean essentially every truck carries a telematics device reporting location continuously, and the telematics providers have integration relationships with the visibility platforms. The contest is therefore not whether the data exists but two things downstream of it. First, coverage across a carrier base where most capacity sits in fleets of fewer than twenty trucks, each of which must individually agree to connect — which is a distribution and incentive problem rather than a technical one. Second, turning a stream of positions into an arrival time accurate enough to plan a dock against, which is where the category has consistently underdelivered. Both are measurable, both are comparable across vendors, and neither is published.

## Current Tools & Gaps
project44 and FourKites lead, with the telematics providers, load board operators and brokerage platforms supplying or competing at the edges. Integration breadth with telematics providers is genuinely extensive. Coverage on large fleets is high and coverage on small carriers is materially worse, which matters because that is where most of the capacity is and where the visibility gap is therefore concentrated. On the prediction side, ETAs are generally computed from distance and estimated driving time with limited allowance for hours of service, facility dwell, or the carrier's own behaviour — the three factors that dominate real arrival variance. Detention, which is the industry's most argued-about cost and is entirely a timestamp problem, is measured from disputed manual records rather than from the geofence data the platform already holds.

## Problems
- [[niches/freight-tech-platforms/truckload-eta-accuracy/build|🔨 Build: Arrival Prediction That Models Hours, Dwell and Carrier Behaviour]]
- [[niches/freight-tech-platforms/truckload-eta-accuracy/buy|🛒 Buy: Geofencing Turned Into an Evidentiary Detention Record]]
- [[niches/freight-tech-platforms/truckload-eta-accuracy/fix|🔧 Fix: Small Carriers Are Where the Coverage Isn't]]
