# Dispatcher Real-Time Rerouting on No-Shows and Cancellations

**Industry:** [[non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Worker Life Changing
**One-liner:** Dispatchers stop playing a frantic mental chess game every time a patient no-shows, and instead get a system that instantly recommends the best reroute for every affected vehicle.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #optimization-fundamentals #bias-variance-tradeoff #worker-facing

## The Problem
NEMT patient no-show rates run 15-20% industry-wide. Every no-show triggers a cascade: the assigned driver is now ahead of schedule with a gap, other patients on shared rides may be affected, and there may be an add-on trip request that could fill the slot — but only if the dispatcher can identify the match within minutes. Dispatchers managing 20-50 active vehicles juggle this mentally, flipping between GPS screens, trip boards, and phone calls to drivers, trying to minimize wasted miles while keeping every other patient's appointment window intact. On a heavy day, dispatchers handle 30-50 no-show/cancellation events and must re-sequence routes under time pressure while simultaneously answering incoming trip requests and driver calls. The cognitive load is extreme — dispatchers describe the job as "air traffic control without the radar."

## Why It Matters to the Worker
Dispatchers burn out within 12-18 months at most NEMT operators. The job requires holding a mental model of every vehicle's position, every patient's mobility level and time sensitivity, and every open slot — then re-computing that model dozens of times per day as no-shows cascade. Mistakes are immediately visible: a late pickup generates a patient complaint, a broker penalty, and a driver who is now behind for the rest of the day. Dispatchers internalize the stress of knowing that their rerouting decisions directly affect whether a 74-year-old dialysis patient waits 45 minutes in a lobby or gets home on time. The emotional weight of these decisions, repeated 50 times a day, is the primary driver of dispatcher turnover.

## What a Solution Looks Like
When a no-show is confirmed (driver marks it in-app or the system detects the vehicle has been stationary at the pickup location beyond a threshold), the system instantly generates 2-3 reroute options ranked by impact: which add-on trips can fill the gap, how to re-sequence the remaining route to recover time, and whether any other vehicle is better positioned to absorb displaced patients. The dispatcher reviews and approves with a single click rather than mentally computing from scratch. The system factors in patient mobility (a wheelchair patient can't be reassigned to a sedan), facility parking constraints, and broker-specific shared-ride rules.

## Impact If Solved
Dispatcher decision time per no-show event drops from 5-10 minutes of frantic coordination to 30 seconds of review-and-confirm. Dead miles from no-shows decrease 30-40% as the system finds optimal backfills. Dispatchers report dramatically lower stress when the rerouting burden shifts from mental computation to system-assisted decision-making — similar to how GPS navigation reduced the cognitive load of driving in unfamiliar areas.
