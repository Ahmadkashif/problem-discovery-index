# Interview Scheduling and Coordination

**Industry:** [[recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Arranging a five-person panel across three time zones takes a coordinator two days of messages, and one cancellation restarts it.
**Tags:** #convex-optimization #gradient-boosting #time-series-forecasting #confidence-intervals #optimization-fundamentals #evaluation-metrics #automation #workflow-orchestration

## The Problem
Interview coordination is the operational heart of recruiting and is close to pure logistics. A panel requires several interviewers with specific skills, availability across calendars that are already full, sequencing constraints, room or video arrangements, and a candidate whose availability is constrained by their current job — which usually means early morning, lunchtime or evening.

It is solved by messaging. A coordinator proposes slots, collects responses, discovers a conflict, proposes again. For a senior role with a multi-stage process across time zones this consumes days, and every day of delay measurably increases the probability that the candidate accepts another offer.

Cancellations are the compounding problem. An interviewer drops out the day before and the coordinator must find a qualified replacement in hours or reschedule the whole panel, which pushes the process back a week.

Interviewer load is managed by whoever the coordinator remembers to ask, so a few willing people carry a disproportionate share and burn out on it, while others interview rarely and stay unpractised.

## What Already Exists
Scheduling automation is a mature feature in modern applicant tracking systems — Ashby, Greenhouse and Lever all offer calendar integration, availability matching and self-scheduling. Standalone tools like GoodTime specialise in interview logistics with load balancing and constraint handling. Calendar integration with major providers is standard. Video conferencing is automatically provisioned. Interview scorecards and structured feedback collection are built in.

## The Customisation Gap
The constrained optimisation is well-shaped and is generally solved greedily rather than properly. Assigning interviewers to panels subject to skill coverage, availability, load balance, diversity of panel composition, sequencing and candidate constraints is a scheduling problem with a known form, and doing it as an optimisation rather than as a first-fit search produces materially better schedules — particularly under the tight availability that senior processes involve.

Robustness is the gap that matters most. Schedules should be built to survive a cancellation: knowing in advance which interviewers could substitute for each slot, and preferring schedules with more substitution options, turns a day-before dropout from a crisis into a swap. That is a design choice nobody makes.

Load management should be a standing objective rather than a coordinator's memory. Interview hours per person per month, tracked and balanced against a stated capacity, protects the people who always say yes and spreads the practice that makes interviewers competent.

And speed should be measured as a conversion driver. Time from application to offer is one of the strongest predictors of whether a candidate accepts, and coordination delay is the largest controllable component — measuring it per stage tells an organisation where the days actually go, which is usually not where they think.

## Impact If Solved
Coordination delay costs candidates directly through offers lost to faster competitors, and costs a substantial share of a coordinator's week. Proper constrained scheduling with substitution robustness removes the cancellation crisis, load balancing protects the interviewers who carry the burden, and measuring stage-level delay identifies where a process is actually slow rather than where everyone assumes it is.
