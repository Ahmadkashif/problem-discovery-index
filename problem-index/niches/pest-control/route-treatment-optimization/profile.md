# Route & Treatment Optimization

**Parent Industry:** [[industries/pest-control|Pest Control]]
**Category:** Highly Automatable

## Profile
**Market Size:** $2B
**Share of Parent Industry:** ~10%
**Digital Adoption:** Medium — Basic routing exists in pest CRMs, but optimization considering treatment time variability, product loading, and service-type sequencing is absent.
**Target Buyer:** Multi-route pest control companies with 10+ technicians seeking to maximize daily job completion and minimize windshield time.
**Automation Potential:** High — Daily route construction, product truck loading, and service time estimation follow optimizable patterns.

## What Makes This a Distinct Niche
Pest control routing is more complex than typical field service routing because of treatment variability. A termite inspection takes 45-90 minutes; a quarterly residential spray takes 15-20 minutes; a commercial restaurant service takes 30-60 minutes. Products and equipment differ by service type — a termite treatment truck carries different chemicals and tools than a general pest truck. Route optimization must balance travel time, service duration variability, product/equipment matching, and customer time windows. Most pest companies still build routes manually — the dispatcher arranges pins on a map or sorts by zip code.

## Current Tools & Gaps
FieldRoutes and PestPac include basic routing (nearest-neighbor algorithms). Generic route optimization tools (OptimoRoute, Routific) optimize for travel time but don't model pest-specific constraints: variable service durations by type, product compatibility on the truck, regulatory requirements (some pesticides require specific PPE transitions between services), and service sequencing preferences (do rodent work last because of odor).

## Problems
- [[niches/pest-control/route-treatment-optimization/build|🔨 Build: Service-Aware Route Optimization Engine]]
- [[niches/pest-control/route-treatment-optimization/buy|🛒 Buy: Truck Loading Optimization by Route]]
- [[niches/pest-control/route-treatment-optimization/fix|🔧 Fix: Service Time Estimation Guesswork]]
