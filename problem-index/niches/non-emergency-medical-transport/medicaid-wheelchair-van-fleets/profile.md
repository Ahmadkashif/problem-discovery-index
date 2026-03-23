# Medicaid Wheelchair Van Fleets

**Parent Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Category:** High Market Share

## Profile
**Market Size:** $4-5B
**Share of Parent Industry:** ~35-40%
**Digital Adoption:** Low-Medium — TripMaster and CTS handle basic dispatch, but wheelchair-specific scheduling constraints (lift time, securement verification, ADA compliance) are managed manually
**Target Buyer:** Fleet owner / operations manager
**Automation Potential:** High — Wheelchair van trips have predictable dwell times per patient mobility category, recurring patient routes, and standardized vehicle configurations that lend themselves to optimization

## What Makes This a Distinct Niche
Wheelchair van transport is the largest NEMT segment by volume and the most operationally complex. Every trip requires matching the patient's wheelchair type and weight to vehicle lift capacity, scheduling 10-20 minutes of load/unload time (versus 2 minutes for ambulatory patients), verifying driver training on wheelchair securement systems (WTORS compliance), and documenting proper securement with photos or attestation for Medicaid audit purposes. These constraints transform what would be a simple pickup-dropoff into a specialized logistics operation where a single misconfigured vehicle assignment can strand a patient. Fleet owners operate 15-100+ wheelchair-accessible vehicles with higher purchase ($60-80K vs. $35K for sedans) and maintenance costs, making utilization optimization critical to profitability.

## Current Tools & Gaps
TripMaster and RouteGenie provide dispatch boards but treat wheelchair trips as a vehicle-type filter rather than a distinct workflow. No tool automatically matches patient wheelchair specifications to specific vehicle lift and floor configurations. Driver WTORS certification tracking is managed in separate HR files, not linked to trip assignment. The dwell-time predictions that dispatchers use to build routes are static estimates that do not learn from actual wheelchair loading times at specific facilities.

## Problems
- [[niches/non-emergency-medical-transport/medicaid-wheelchair-van-fleets/build|🔨 Build: Wheelchair-Patient-Vehicle Configuration Matcher]]
- [[niches/non-emergency-medical-transport/medicaid-wheelchair-van-fleets/buy|🛒 Buy: Wheelchair Trip Dwell Time Prediction]]
- [[niches/non-emergency-medical-transport/medicaid-wheelchair-van-fleets/fix|🔧 Fix: Securement Documentation for Medicaid Audits]]
