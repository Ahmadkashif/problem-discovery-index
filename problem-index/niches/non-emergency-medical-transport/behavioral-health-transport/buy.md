# De-Escalation Trained Driver Matching

**Niche:** [[niches/non-emergency-medical-transport/behavioral-health-transport/profile|Behavioral Health Transport]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** NEMT dispatch systems assign drivers by proximity and availability, not by training level — sending untrained drivers to behavioral health pickups that require de-escalation skills.
**Tags:** #automation #workflow-orchestration #worker-facing #compliance

## The Problem
A behavioral health patient leaving a partial hospitalization program needs transport home. The dispatch system assigns the nearest available driver — who has no de-escalation training, no experience with behavioral health patients, and no preparation for the pickup. The patient, already anxious about the transition from a safe clinical environment, encounters a driver who is visibly uncomfortable. The interaction goes poorly. Alternatively, the provider has 3 drivers with de-escalation training out of 25 total, but the dispatch system has no mechanism to preferentially assign those trained drivers to behavioral health trips. The trained drivers end up on standard ambulatory trips while untrained drivers are assigned to high-risk behavioral health pickups.

## What Already Exists
NEMT dispatch platforms (TripMaster, CTS, RouteGenie) assign trips based on vehicle type, driver availability, and geographic proximity. HR systems and training management platforms (Relias, KnowBe4) track driver certifications and training completion. Crisis intervention training programs (CPI, MANDT) certify drivers in de-escalation techniques. These systems do not talk to each other — training records do not flow into dispatch assignment logic.

## The Customization Gap
Behavioral health trip dispatch needs a training-aware assignment layer: when a trip is tagged as behavioral health (by the referring facility or the booking broker), the dispatch system filters available drivers to those with current de-escalation training certification, behavioral health transport experience (measured by completed trips), and positive behavioral health trip ratings. If no trained driver is available, the system alerts the dispatcher rather than silently assigning an untrained driver. The training tracking must be integrated with the certification provider to auto-update when credentials expire or are renewed.

## Target Customer
NEMT dispatchers managing fleets where 10-25% of daily trips serve behavioral health patients, and operations managers responsible for driver training and trip quality.

## Impact If Solved
Ensures 100% of behavioral health trips are served by trained drivers (versus the current estimated 30-40%), reducing transport incidents by 40-60% and driver refusal/turnover on behavioral health routes by 50%. Trained driver matching also improves patient experience scores, supporting behavioral health MCO contract performance.
