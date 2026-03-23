# Post-Treatment Pickup Timing Mismatch

**Niche:** [[niches/non-emergency-medical-transport/dialysis-transport-specialists/profile|Dialysis Transport Specialists]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Fix (Pain Point)
**One-liner:** Dialysis patients wait 30-90 minutes for return rides because NEMT providers schedule pickups at fixed times while treatment completion times vary unpredictably.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #worker-facing

## The Problem
The return trip from dialysis is the most time-sensitive and medically risky leg of the transport cycle. Patients emerge from 3-5 hours of treatment dehydrated, fatigued, and often hypotensive — sitting in a clinic lobby for 45 minutes is not just uncomfortable but clinically inadvisable. Drivers who arrive before the patient is ready wait idle in the parking lot, losing productive time. Drivers who arrive late find an anxious, unwell patient who has been calling dispatch repeatedly. The timing mismatch stems from a fundamental information asymmetry: the NEMT provider schedules pickups hours in advance based on estimated treatment duration, but actual treatment times vary by 30-60 minutes due to access issues, blood pressure complications, and facility scheduling.

## Why It's Still Broken
Treatment completion is inherently variable, and no automated signal currently flows from the dialysis center to the transport provider. Dialysis centers staff their front desks with medical personnel who are not responsible for transportation coordination. Patients are expected to call their ride when they are ready, but many are elderly, fatigued post-treatment, and may not have reliable cell phone access. The NEMT provider's dispatcher monitors 20-50 simultaneous pickups and cannot proactively track each patient's treatment status.

## What a Fix Looks Like
A predictive pickup system that uses each patient's historical treatment duration patterns (most patients stabilize within a 15-minute window after 4-6 treatments) combined with same-day treatment start time confirmation to predict completion within a 10-minute window. The system dispatches the return vehicle to arrive 5 minutes after predicted treatment end, with automatic adjustment if the dialysis center sends a "treatment extended" or "patient ready" notification. For patients with highly variable treatment times, the system positions the vehicle at the facility during the predicted window rather than dispatching from a distant location.

## Who Feels the Pain
Dialysis patients who sit in lobbies post-treatment feeling unwell, drivers who waste 30-45 minutes per shift waiting at dialysis centers, and dispatchers who field 10-20 daily calls from patients asking "where is my ride?"

## Impact If Fixed
Reduces average post-dialysis wait time from 40 minutes to under 10 minutes, recovers 1.5-2.5 driver-hours per day per fleet in eliminated wait time, and reduces patient complaint calls by 60-70% — directly improving the metrics that determine broker contract retention.
