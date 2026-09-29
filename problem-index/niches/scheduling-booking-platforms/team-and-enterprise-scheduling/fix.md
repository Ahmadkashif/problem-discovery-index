# Rescheduling Starts From Scratch

**Niche:** [[niches/scheduling-booking-platforms/team-and-enterprise-scheduling/profile|Team & Enterprise Scheduling]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** One person moves one meeting and the product offers a fresh booking link, discarding everything already known about who else was involved and what constraints applied.
**Tags:** #graph-theory #dynamic-programming #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to place a meeting that involves more than one busy internal calendar without a human brokering it — and that contest splits by what the meeting is for, which is why this niche is not terminal and is decomposed below.

## The Problem
A four-person meeting is scheduled for Thursday. On Tuesday one participant has a conflict. The product's response is to cancel and offer a new link, which restarts the entire negotiation: four calendars, the same constraints, the same preferences, none of it retained. In practice a coordinator takes over and does it by hand, or the meeting slips a week. The system knew the constraint set two days ago and discarded it the moment the booking was confirmed.

## Why It's Still Broken
Bookings are modelled as events rather than as solutions to a constraint problem, so the constraints are inputs that are thrown away once an event exists. Rescheduling was implemented as cancel-and-rebook because that is the simplest path through an event-shaped data model. And the cost falls on whoever is coordinating, which in most organisations is nobody's measured responsibility, so it has never been prioritised.

## What a Fix Looks Like
Retain the constraints and treat rescheduling as repair. Store what produced the booking — participants, eligibility, preferences, buffers, sequence requirements — alongside the event, which is a data model change and the precondition for everything else. On a conflict, re-solve against the retained constraints and propose two or three alternatives that satisfy everyone, rather than reopening the negotiation. Minimise disruption explicitly, preferring solutions that move one meeting over solutions that move three, which is the objective a coordinator uses instinctively and no system encodes. Handle the cascade, since moving one meeting frequently invalidates another and the products treat each in isolation. Offer a substitution path where someone else is eligible, which is often better than moving the time and is never suggested. And measure the reschedule rate and its causes, which tells an operator whether their availability model is wrong — repeated conflicts in the same window usually mean declared availability that is not real.

## Who Feels the Pain
Coordinators rebuilding negotiations by hand; participants whose meetings slip a week for a one-hour conflict; and organisations whose meeting time is consumed by the arrangement of meetings.

## Impact If Fixed
Retaining the constraint set is a modest data model change that converts rescheduling from a restart into a repair. Minimising disruption is the objective coordinators already use, and the reschedule-cause report usually reveals an availability model that was wrong from the start.
