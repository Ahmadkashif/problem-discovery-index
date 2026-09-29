# Who the Meeting Should Be With

**Niche:** [[niches/scheduling-booking-platforms/team-and-enterprise-scheduling/profile|Team & Enterprise Scheduling]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Team scheduling products answer when a meeting can happen and treat who it should be with as a round-robin, which is the decision that actually determines whether the meeting is worth having.
**Tags:** #convex-optimization #dynamic-programming #gradient-boosting #graph-theory #evaluation-metrics #confidence-intervals #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to place a meeting that involves more than one busy internal calendar without a human brokering it — and that contest splits by what the meeting is for, which is why this niche is not terminal and is decomposed below.

## The Problem
A team booking page distributes meetings evenly across five people. Even distribution is a fairness property, not a business one. The prospect who should have gone to the specialist goes to whoever was next in rotation; the panel interview is assembled from whoever happened to be free rather than from who should assess this candidate; the follow-up meeting goes to a different person from the first one. The platform optimised for a balanced calendar, which nobody asked for, over a correct match, which is the entire value of the meeting.

## Why Nobody Has Built This
Round-robin is simple, explicable and obviously fair, which made it the natural first answer and a hard one to displace without a clear alternative. Deciding who a meeting should be with requires context the scheduling tool does not hold — account ownership, territory, specialisation, language, relationship history, interview eligibility — which lives in other systems. And the category's origin is the individual scheduling link, where the question does not arise, so the product architecture has no concept of a matching decision.

## What to Build
The common layer both sub-niches need: assignment as an explicit optimisation rather than a rotation. A model of who is eligible for a given meeting, drawn from the systems that hold it — ownership and territory rules, specialisation, language, seniority, prior relationship, and hard exclusions such as a conflict of interest — evaluated as constraints rather than preferences. An objective that reflects what the meeting is for, which differs by use case and is where the two sub-niches diverge, but shares the property of being about outcome rather than about even distribution. Load balancing retained as a secondary objective rather than the primary one, since capacity genuinely matters and should not be the thing being maximised. Latency as a first-class constraint, because in several of these cases the value of the meeting decays by the minute. And measurement of the assignment rather than of the booking: did meetings assigned this way convert, complete, or produce a decision — which is the only way anyone finds out whether the matching is any good and which no product currently reports.

## Target Customer
Revenue operations and talent acquisition functions, scheduling platform vendors moving up-market, and the customer relationship and applicant tracking vendors whose scheduling modules compete here.

## Impact If Built
Round-robin optimises a property nobody cares about over the one that determines the meeting's value. Making assignment an explicit constrained decision is the shared foundation, and the objective that sits on top of it is what the two sub-niches below define.
