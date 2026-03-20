# Delivery Scheduling with Patient Mobility and Access Constraints

**Industry:** [[medical-supply-retail|Medical Supply Retail]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Standard route optimization tools treat every delivery stop as equivalent, but delivering a bariatric hospital bed to a third-floor walkup requires a two-person crew, a stair-climbing dolly, and 45 minutes on-site — while dropping off a box of wound care supplies takes 5 minutes at the front door — and no delivery scheduling platform accounts for these patient-specific access and setup variables.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #cross-validation #evaluation-metrics #optimization-fundamentals #workflow-orchestration

## The Problem
DME delivery is not standard parcel delivery. Equipment ranges from a 2-pound bag of CPAP supplies (doorstep drop) to a 400-pound bariatric bed (requires disassembly, room-by-room navigation, reassembly, and patient fitting). Patient homes present access challenges that standard logistics tools ignore: narrow hallways, stairs without elevators, hoarding conditions, rural addresses with unpaved access roads, and patients who cannot open the door and require a caregiver to be present. Delivery windows must accommodate patients who may have home health aide schedules, dialysis appointments, or limited mobility that makes certain times of day impossible. Current scheduling is done manually by dispatchers who hold all of this contextual knowledge in their heads or in free-text notes attached to each order — and when the dispatcher is out sick, deliveries go sideways.

## What Already Exists
Route optimization platforms (Route4Me, OptimoRoute, Routific) solve the traveling salesman problem for standard delivery fleets — minimizing drive time and fuel cost across a set of stops. Brightree includes a basic delivery scheduling module that assigns orders to drivers based on zip code zones. Google Maps and similar tools provide drive-time estimates. General-purpose field service management tools (ServiceTitan, Housecall Pro) handle appointment scheduling for service businesses.

## The Customisation Gap
None of these tools model the per-stop service time as a function of equipment type, patient mobility, home access characteristics, and crew requirements. A delivery scheduler for DME needs to know that Order #4521 (power wheelchair, patient lives in a second-floor apartment with a narrow staircase, patient weighs 280 lbs) requires a two-person crew, a stair-climbing track system, and a 60-minute delivery window — and cannot be combined on the same route with Order #4525 (hospital bed delivery, also two-person) because the single two-person crew can only handle one heavy delivery per morning. The customization requires a regression model trained on historical delivery data (equipment type, home characteristics, actual time on-site) to predict per-stop service duration, which then feeds into a constraint-aware route optimizer that respects crew capacity, equipment-specific vehicle requirements (some items only fit in the box truck, not the van), and patient availability windows.

## Impact If Solved
Reduces failed deliveries (patient not home, wrong equipment for access conditions, insufficient crew) from the current 10–15% rate to under 3%, saves 1–2 hours per driver per day in idle time caused by misestimated stop durations, and improves patient satisfaction scores by providing accurate delivery windows instead of the current "sometime between 8am and 5pm" experience.
