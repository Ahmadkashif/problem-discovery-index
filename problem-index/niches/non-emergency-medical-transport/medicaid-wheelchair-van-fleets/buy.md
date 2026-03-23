# Wheelchair Trip Dwell Time Prediction

**Niche:** [[niches/non-emergency-medical-transport/medicaid-wheelchair-van-fleets/profile|Medicaid Wheelchair Van Fleets]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Route optimization tools use static dwell time estimates for all wheelchair pickups, but actual loading times vary 5x depending on patient mobility, wheelchair type, facility layout, and weather.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #workflow-orchestration

## The Problem
Dispatchers build routes using a flat dwell time assumption — typically 15 minutes for every wheelchair pickup. In reality, loading a self-propelling manual wheelchair patient at a ground-floor facility takes 5 minutes, while loading a bariatric power wheelchair patient at a facility with a narrow hallway and no ramp takes 25 minutes. When routes are built with 15-minute estimates, 40% of wheelchair trips run over time, cascading delays to every subsequent patient on the route. Experienced dispatchers mentally adjust for specific patients and facilities — "Mrs. Johnson at Oak Street Dialysis always takes 20 minutes because the elevator is slow" — but this knowledge is not captured in any system.

## What Already Exists
TripMaster and CTS Software allow configuring default dwell times by trip type (wheelchair, stretcher, ambulatory), but these are fleet-wide static values. Google Maps and routing APIs estimate drive times between points but have no concept of patient loading time. Route optimization tools (RouteGenie, RoutingBox) use these static dwell inputs without questioning their accuracy.

## The Customization Gap
Wheelchair trip routing needs a dwell time prediction model that learns from historical GPS data — specifically, the time between "arrived at pickup" and "departed pickup" for each patient-facility combination. The model should account for: patient mobility level (self-propelling vs. attendant-pushed vs. power chair), facility characteristics (floor level, ramp vs. lift vs. stairs, hallway width, parking proximity), weather conditions (rain and snow add 3-8 minutes to outdoor loading), and time of day (facility elevator wait times peak at 8-9am). These predictions feed directly into route optimization, producing realistic schedules that prevent cascading delays.

## Target Customer
NEMT dispatchers building daily routes for fleets of 15+ wheelchair vans who currently under-estimate dwell times on 40% of wheelchair trips, causing chronic late arrivals.

## Impact If Solved
Improves on-time performance for wheelchair trips from 70-75% to 90%+ by replacing static dwell time estimates with patient-facility-specific predictions. For a 30-vehicle fleet, this prevents 15-25 late arrivals per day, protecting broker contracts and reducing patient complaints by 40-50%.
