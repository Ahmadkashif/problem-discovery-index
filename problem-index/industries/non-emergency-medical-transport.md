# Non-Emergency Medical Transport

## Profile
**Category:** Transportation
**Market Size:** ~$12B US (Medicaid-funded + private pay); growing 7-8% annually as aging population and chronic disease prevalence increase ride volume
**Tech Maturity:** Low-Medium — TripMaster, RouteGenie, and CTS Software handle basic dispatch and GPS tracking, but most operators still rely on manual scheduling spreadsheets, phone-based coordination, and paper trip logs for Medicaid billing reconciliation
**Workforce:** Drivers (often W-2 and 1099 mixed fleets), dispatchers juggling real-time scheduling boards, scheduling coordinators managing broker relationships, billing specialists handling Medicaid claim submissions and denial rework

## Key Pain Themes
Dispatchers manually assess each trip request by reading patient profiles, appointment types, and facility locations to determine vehicle type (wheelchair van, stretcher, ambulatory sedan), estimated load/unload time, and whether an attendant is required — a judgment call that experienced dispatchers make in seconds but new hires get wrong 30-40% of the time, causing late pickups and compliance violations. Multi-stop route optimization across a mixed fleet with varying vehicle capacities, patient mobility levels, and narrow appointment windows is solved manually or with basic routing tools that ignore patient-specific constraints. Medicaid billing requires matching every trip to an authorization, capturing exact pickup/dropoff times and odometer readings, and surviving audits where a single documentation gap can trigger recoupment of thousands in claims. Driver turnover exceeds 60% annually because the job combines physically demanding patient assistance with unpredictable schedules, low pay, and emotional fatigue from transporting medically fragile individuals.

## Current Tech Landscape
TripMaster and CTS Software provide dispatch boards, GPS tracking, and basic Medicaid billing integration, but their routing engines treat patients as interchangeable cargo and ignore mobility-specific time requirements. Broker platforms like Modivcare and LogistiCare assign trips to providers but offer no tools for intra-fleet optimization. Most operators under 50 vehicles still use whiteboards, phone trees, and Excel for daily scheduling, with billing staff manually keying trip data into state Medicaid portals.

## Problems
- [[problems/non-emergency-medical-transport/high-impact|🔴 High Impact: Multi-Constraint Trip Scheduling and Route Optimization]]
- [[problems/non-emergency-medical-transport/low-impact-1|🟡 Low Impact: Medicaid Trip Billing and Verification Automation]]
- [[problems/non-emergency-medical-transport/low-impact-2|🟡 Low Impact: Mixed Fleet Preventive Maintenance Scheduling]]
- [[problems/non-emergency-medical-transport/worker-life-1|🟢 Worker Life: Driver Patient Interaction and Documentation Burden]]
- [[problems/non-emergency-medical-transport/worker-life-2|🟢 Worker Life: Dispatcher Real-Time Rerouting on No-Shows and Cancellations]]
- [[problems/non-emergency-medical-transport/ml-opportunity|🔵 ML Opportunities]]
- [[problems/non-emergency-medical-transport/ai-agents-platforms|🤖 AI Agents & Platforms]]
