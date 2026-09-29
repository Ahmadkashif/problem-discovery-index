# Nobody Can Tell the Customer When It Will Be Ready

**Niche:** [[niches/field-service-software/equipment-dealer-service/profile|Equipment Dealer Service Departments]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** The only question an equipment customer asks is when their machine will be back, and the dealership's answer is a guess delivered by whoever picks up the phone, revised each time they call.
**Tags:** #survival-analysis #time-series-forecasting #confidence-intervals #evaluation-metrics #descriptive-statistics #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in dealer service software is fighting to get a machine back into the field inside the window the customer's season allows — and whoever cuts downtime during the narrow weeks that matter takes the dealership.

## The Problem
A farmer's machine is in the shop during a window when every day matters. He calls on Tuesday and is told Thursday. He calls Thursday and is told a part is coming Monday. He calls Monday and gets a different person who does not know. Each call takes a service advisor away from the counter, each answer is worse than the last, and the customer's experience of the dealership — which will determine where he buys his next machine — is formed entirely in this sequence. The information needed to answer properly exists somewhere: the job's remaining work, the technician's queue, the part's actual shipping status.

## Why It's Still Broken
There is no schedule to derive a date from, so the estimate comes from a person's impression of the shop. Parts status lives in the manufacturer's ordering system and is not surfaced to whoever answers the phone. And there is a defensive habit: giving an optimistic date avoids a difficult conversation today at the cost of a worse one on Thursday, and under pressure most people take that trade. The result is that the dealership's most important customer interaction is conducted on information nobody has.

## What a Fix Looks Like
Produce an estimate from the actual state and tell the customer without being asked. Remaining work, technician queue position, and parts arrival — with a real expectation from the supplier rather than a nominal lead time — combine into a completion estimate with an interval, which is honest in a way a single date is not: "Thursday, probably, but it depends on a part due Wednesday" is both more accurate and better received than a date that slips. Push status proactively on any change, so the customer stops calling and the service advisor stops being interrupted. Track promised versus actual completion as a standing metric, because no dealership currently measures whether it keeps its promises and the number is the fastest route to improving them. Where a machine is down in a season window, flag it for priority explicitly rather than leaving it to whoever shouts.

## Who Feels the Pain
Service advisors giving answers they know are unreliable; customers losing days in a season on a machine whose status nobody can state; and technicians interrupted to answer status questions about their own jobs.

## Impact If Fixed
Proactive, honest status removes most inbound status calls, which is a measurable recovery of service advisor time, and it changes the customer's experience of the dealership more than any improvement in turnaround time would. Measuring promise attainment is free and is the metric the department has never had, in a business where the promise is the product.
