# Nobody Knows What the Simplification Costs

**Niche:** [[niches/scheduling-booking-platforms/multi-resource-availability/profile|Multi-Resource Availability]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An operator restricts online booking to four of eleven services and pads every slot, and neither they nor the vendor has any idea what that costs, because a slot never offered produces no data.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor here is fighting to let a real business express what it can actually deliver — staff with different skills, constrained rooms and equipment, service-specific buffers and travel — and whoever does that takes the account, because businesses currently simplify their availability and sell less than they could.

## The Problem
A salon's online booking shows a fraction of its true capacity: two stylists rather than five, four services rather than twelve, and thirty-minute padding on everything because the owner once had a double-booking. Customers who cannot find a slot leave the page. Some call; most do not. The owner sees a healthy booking rate on the slots they offer and no evidence at all of the demand they turned away. The platform sees the same thing and reports a well-utilised account.

## Why It's Still Broken
The whole cost class is invisible by construction: abandonment on a booking page with no available slot generates no record in most implementations, and demand for services that are not listed generates nothing anywhere. Vendors report bookings made rather than searches unfulfilled, so the metric does not exist. And operators simplify for a reason — a past double-booking or an over-run — so the padding is defended by a specific memory that no counter-evidence exists to balance.

## What a Fix Looks Like
Measure the demand that finds nothing. Log booking page sessions that end without a booking, with the service and date range sought, which is basic instrumentation nobody does and immediately produces an unmet-demand picture. Report fully-booked searches specifically, distinguishing a customer who found no slot from one who was browsing. Compare declared service duration against actual elapsed time from the appointment record, which tells the operator whether their padding is justified — usually it is for two services and not for the other nine, and that finding is specific enough to act on. Report utilisation against true capacity rather than against offered capacity, which is the number that reveals the gap. Track phone bookings for services not offered online, where they are recorded, since that is the clearest evidence of the simplification's cost. And present the whole thing as an opportunity rather than a criticism, because the operator's simplification was a reasonable response to a system that could not represent their business.

## Who Feels the Pain
Operators leaving capacity unsold with no way to see it; customers who cannot book what the business can obviously do; and vendors whose accounts look healthy while the customer's actual problem is invisible in their data.

## Impact If Fixed
Instrumenting unfulfilled searches is a small change that creates a metric nobody in the category has. The declared-versus-actual duration comparison is a direct query over existing appointment records and usually shows most of the padding to be unnecessary.
