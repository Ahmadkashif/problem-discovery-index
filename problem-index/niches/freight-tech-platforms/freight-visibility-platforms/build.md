# ETA as a Distribution With a Published Track Record

**Niche:** [[niches/freight-tech-platforms/freight-visibility-platforms/profile|Freight Visibility Platforms]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Visibility platforms present an arrival time as a single confident number, every user knows it is often wrong, and nobody publishes how wrong — so the product's central output cannot be used for any decision that depends on it.
**Tags:** #time-series-forecasting #gradient-boosting #confidence-intervals #evaluation-metrics #survival-analysis #cross-validation #revenue-impact #automation
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A receiving facility is told a truck will arrive at 14:20. Whether that means "between 14:00 and 14:40 with high confidence" or "sometime this afternoon, probably" changes everything the facility would do with it — whether to hold a dock door, whether to keep a crew, whether to reschedule the next appointment. The platform does not say, so the facility treats every ETA the same way, which in practice means treating them all as unreliable and planning as if there were no ETA at all. The product delivers a number that is precise, unqualified, and therefore inert.

## Why Nobody Has Built This
Point estimates demo better than intervals, and a platform that publishes its own uncertainty has published its own limitations in a competitive market where nobody else does. There is also a real modelling difficulty: arrival time uncertainty is dominated by events that are not in the data — how long the facility ahead of this one takes to unload, whether the driver has hours available, whether the appointment will be honoured — so an honest interval is wide, and a wide interval is commercially unattractive to present. The correct response is to narrow it by modelling those factors, which requires facility-level and carrier-level data the platforms have and have not used this way.

## What to Build
An arrival forecast expressed as a distribution, conditioned on the things that actually drive variance: remaining distance and route, current hours of service position, the destination facility's own historical dwell and appointment adherence, the carrier's own punctuality history, time of day, day of week and weather. Facility-level effects are the largest untapped source of accuracy and the platforms are uniquely positioned to estimate them, because they observe every carrier's experience at every facility. The output is a probability of arrival within each window, which is directly actionable — a facility can decide whether to hold a door on a 70% chance, and cannot decide anything on a bare timestamp. Accuracy is measured continuously and published inside the product, per lane and per facility, because a probabilistic forecast without a calibration record is worse than a point estimate.

## Target Customer
Visibility platforms, shippers whose operations depend on arrival planning, and the receiving facilities whose labour scheduling is the largest downstream consumer of an ETA.

## Impact If Built
A calibrated arrival distribution is the difference between a tracking product and a planning input, and the downstream value is in facility labour, dock utilisation and detention — all of which are large and none of which can be managed from a point estimate. Facility-level dwell modelling is also the industry's most valuable unpublished dataset and belongs to the visibility platforms alone.
