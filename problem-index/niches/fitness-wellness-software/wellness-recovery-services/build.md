# Utilisation Scheduling Across Practitioners, Rooms and Equipment

**Niche:** [[niches/fitness-wellness-software/wellness-recovery-services/profile|Wellness & Recovery Services]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A recovery business's cost is practitioner hours and room rent, its revenue is appointments of varying duration, and its scheduling software treats every booking as a slot on a grid.
**Tags:** #optimization-fundamentals #dynamic-programming #combinatorics-and-counting #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in recovery and wellness software is fighting to keep practitioners and rooms utilised when service durations vary and no-shows are costly — and whoever raises utilisation per available practitioner hour takes the account.

## The Problem
A studio has four treatment rooms, two saunas, a cold plunge and six practitioners on varying shifts. A client books a ninety-minute massage followed by a sauna. Another books two fifty-minute services back to back with different practitioners. The booking system places these on a calendar grid, which cannot represent that the massage occupies a practitioner and a room for ninety minutes plus fifteen for turnover, and that the sauna occupies a different resource for thirty. Conflicts are discovered on the day. Gaps open between appointments that a different placement would have avoided. The owner looks at a half-empty afternoon and a fully booked evening and concludes they need more staff.

## Why Nobody Has Built This
The category grew out of fitness software, where capacity is a class with a headcount and the resource model is trivial, and the products extended booking rather than rebuilding scheduling. Doing it properly means modelling practitioners, rooms and equipment as separate constrained resources with service-specific requirements and turnover times, which is a real data model change under the busiest screen in the product. And the businesses themselves are small and growing fast, so they tolerate the friction as a growth problem rather than identifying it as a software one.

## What to Build
A resource-constrained scheduler. Each service specifies which resources it consumes, for how long, with what turnover, and which practitioners are qualified to deliver it. Booking becomes an allocation against those constraints rather than a placement on a grid, so double-booking becomes impossible and the system can offer the client the times that actually exist. Duration is estimated per service per practitioner from history rather than taken from a configuration field, since the variance is real and is what makes grid-based scheduling fail. Multi-service visits are sequenced automatically with the transitions handled. Offered times are chosen to consolidate rather than to fragment, in the same way the in-person trainer niche describes. And the owner gets the measurement they have never had: utilisation by practitioner, by room and by hour, which is what tells them whether they need more staff or better placement.

## Target Customer
Independent recovery and wellness studios, massage practices, multi-modality wellness businesses, and the platform vendors serving them with class-based scheduling.

## Impact If Built
Utilisation is the entire economics of a business paying for practitioners and rooms, and grid scheduling leaves a substantial share of it on the floor through fragmentation and conflict. The utilisation measurement alone usually redirects an owner's hiring decision, which is the most expensive decision they make.
