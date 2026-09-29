# Rebuilding the Day, Again

**Niche:** [[niches/scheduling-booking-platforms/schedule-coordinator-recovery/profile|Schedule Coordinator Recovery]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A practitioner calls in sick and someone spends ninety minutes reassigning twelve appointments by hand, against constraints the system already holds and an objective it has never been given.
**Tags:** #convex-optimization #dynamic-programming #graph-theory #optimization-fundamentals #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to re-solve the day automatically when something moves and propose the recovery — and whoever does that takes the multi-practitioner operator, because rebuilding the day by hand is the coordinator's entire job.

## The Problem
At 7:40 a physiotherapist calls in sick. Twelve appointments. The coordinator works through them: three can be moved to a colleague today, two clients will only see this practitioner, one needs the room that is now free anyway, four can shift to Thursday, and two will have to be cancelled. Each one is a phone call. It takes the whole morning, during which the front desk is unattended and two more people call to reschedule, and the outcome is worse than it needed to be because nobody could hold twelve simultaneous options in their head. The system knew every constraint and offered a calendar to drag things around on.

## Why Nobody Has Built This
The products model a schedule as a set of events to be edited rather than as a solution to be re-solved, so there is no solver and no objective. The constraints that make a recovery correct — practitioner competency, room and equipment compatibility, client preferences and tolerances — are mostly not represented, which is the same gap the availability niche describes and is why the two capabilities are the same investment. Client tolerance in particular is knowledge held by the coordinator and captured nowhere. And the coordinator's labour is the existing solution, which is expensive but invisible because it is a salary rather than a line item.

## What to Build
Recovery as a proposed solution. On a disruption, re-solve the affected period against the full constraint set and produce two or three complete recovery plans, each with its consequences stated: these four move, these two are reassigned, these two need a call, this one cannot be saved. Optimise for minimum disruption — fewest clients affected, smallest moves, preserved practitioner continuity where it matters — which is the objective the coordinator already uses and which no product encodes. Learn client tolerance from history rather than asking: who has accepted a change before, who cancelled when moved, who always takes the first slot offered, all of which is in the booking record and is exactly the knowledge that currently lives in one person's head. Execute the communications for the accepted plan — the messages, the confirmations, the follow-ups — rather than leaving twelve phone calls. Handle the cascade case, where an over-run pushes everything behind it, as a continuous small re-solve rather than as an event. And let the coordinator override anything, easily, because they know things the model does not and their overrides are the best available training signal.

## Target Customer
Multi-practitioner clinics, salons, studios and service operators; and the vertical platform vendors serving them, for whom this is the capability that justifies a system over a calendar.

## Impact If Built
Disruption recovery happens several times a day in every one of these businesses and consumes a coordinator's working life. The constraints are the same ones availability needs, so the two capabilities compound, and minimum-disruption is an objective the coordinator already has and the product has never been told.
