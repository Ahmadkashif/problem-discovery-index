# Multi-Resource Availability Logic

**Industry:** [[scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every platform can express availability, and expressing a real business — several staff with different skills, rooms and equipment that are also constrained, service-specific buffers and travel time — defeats the configuration interface, so businesses simplify and sell less.
**Tags:** #optimization-fundamentals #convex-optimization #gradient-boosting #dynamic-programming #evaluation-metrics #workflow-orchestration #revenue-impact

## The Problem
Booking looks like finding a free hour on a calendar and rarely is. A salon appointment requires a stylist qualified for that service, a chair, and possibly a shampoo station for part of the time. A clinic appointment requires a clinician licensed for the procedure, a room configured for it, and equipment shared across rooms. A field service appointment requires a technician with the right certification, the part on the van, and travel time from wherever they were before.

Platforms express availability well for one person with one calendar. Multi-resource constraints are supported partially, with an interface that requires the business owner to reason about the interaction between staff skills, room capacity, equipment and buffers.

Most owners cannot, and reasonably do not want to. So they simplify: pretend the equipment is not constrained, add a generic buffer to everything, or block off time defensively. Each simplification costs capacity, and none of them is visible as a loss — the business simply sells less than it could and never sees the counterfactual.

The scheduling that would maximise capacity is a combinatorial problem, and the interface asks a small business owner to solve it by hand.

## What Already Exists
Availability rules, working hours, buffers and lead times are standard everywhere. Resource booking is offered by Acuity, Square Appointments and most vertical platforms. Round-robin and pooled team availability handle simple cases. Calendar integration prevents the most obvious double-bookings. Vertical platforms in health and beauty have deeper resource models than the horizontal players.

## The Customisation Gap
Constraint expression is the wrong interface for the problem. The business owner knows the rules in operational terms — this service needs a colourist and a chair, and the chair is free after the processing time starts — and must translate that into resource types and buffer settings. That translation is where it breaks.

Slot generation as an optimisation rather than a lookup is the substantive gap. What should be offered to a customer is the set of start times for which a feasible assignment of all required resources exists, and choosing which of those to offer should account for how each booking fragments the remaining day. Offering a two o'clock that strands an unusable forty-five minutes is a real cost that no platform models.

Travel time for mobile services is a specific and common failure. It is knowable and is usually handled with a fixed buffer that is too generous in dense areas and too tight in sparse ones.

Capacity diagnosis is the third gap: which resource is actually the binding constraint on this business's revenue, which the platform could compute and which every owner guesses at.

## Impact If Solved
Availability determines what can be sold, and small businesses are simplifying their availability because the configuration is harder than the business. Treating slot generation as a constrained optimisation rather than a calendar lookup recovers capacity that is currently lost invisibly.
