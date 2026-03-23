# Trip Authorization Verification

**Parent Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Category:** Highly Automatable

## Profile
**Market Size:** Embedded across $12B industry (estimated $600M-900M in labor costs for manual verification)
**Share of Parent Industry:** Cross-cutting scheduling function affecting all Medicaid-funded providers
**Digital Adoption:** Low — Schedulers manually verify each trip against broker authorization databases via phone calls or portal lookups, one trip at a time
**Target Buyer:** Scheduling coordinator / compliance officer / operations manager
**Automation Potential:** High — Authorization verification is a deterministic matching problem: does this trip match an active authorization in the broker's system? Binary yes/no with structured inputs and outputs

## What Makes This a Distinct Niche
Before an NEMT provider can dispatch a vehicle for a Medicaid-covered trip, the scheduler must verify that an active authorization exists in the transportation broker's system — confirming the patient is eligible, the trip dates fall within the authorization period, the authorized service level matches the vehicle type being dispatched, the pickup and dropoff locations match the authorization, and any special requirements (attendant, wheelchair, stretcher) are covered. This verification process consumes 3-5 minutes per trip and represents 30-40% of a scheduler's daily workload. For a provider handling 200 trips per day, that is 10-17 person-hours daily spent on verification alone. Trips dispatched without proper authorization are denied at billing, creating irrecoverable revenue losses.

## Current Tools & Gaps
Transportation broker portals allow individual trip authorization lookups, but each lookup requires navigating to the portal, entering patient and trip details, and interpreting the result — a process that cannot be batched or automated through current portal interfaces. TripMaster and CTS Software store authorization numbers but do not automatically verify them against broker systems. No tool performs batch authorization verification, identifies trips that lack current authorizations, or flags authorization changes (cancellations, modifications) that occurred after the trip was scheduled.

## Problems
- [[niches/non-emergency-medical-transport/trip-authorization-verification/build|🔨 Build: Automated Batch Authorization Verification]]
- [[niches/non-emergency-medical-transport/trip-authorization-verification/buy|🛒 Buy: Authorization-to-Dispatch Compliance Gate]]
- [[niches/non-emergency-medical-transport/trip-authorization-verification/fix|🔧 Fix: Post-Schedule Authorization Changes]]
