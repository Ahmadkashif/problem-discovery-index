# Resource-Constrained Scheduling, Off the Shelf

**Niche:** [[niches/scheduling-booking-platforms/multi-resource-availability/profile|Multi-Resource Availability]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Resource-constrained project scheduling and job-shop scheduling are foundational operations research with free solvers, and appointment availability is computed by intersecting calendars.
**Tags:** #convex-optimization #dynamic-programming #optimization-fundamentals #graph-theory #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to let a real business express what it can actually deliver — staff with different skills, constrained rooms and equipment, service-specific buffers and travel — and whoever does that takes the account, because businesses currently simplify their availability and sell less than they could.

## The Problem
Scheduling jobs that require particular machines and particular operators, with setup times depending on sequence and with resources that cannot be shared, is the job-shop and resource-constrained scheduling problem. It is among the most studied problems in operations research, with free solvers that handle industrial instances. A six-person clinic with three rooms is an instance so small that the solver would answer before the page finished loading, and the category computes availability by intersecting free-busy blocks.

## What Already Exists
Constraint programming and mixed-integer solvers with dedicated scheduling constructs for cumulative resources, sequence-dependent setup and no-overlap; the resource-constrained project scheduling literature; vehicle routing solvers for the mobile-services travel component, which is a well-solved problem in its own right; and routing and distance services for travel times. All free and all mature.

## The Customization Gap
The adaptation is to a booking page rather than a production plan. It requires: (1) inverting the question, since production scheduling asks when a known set of jobs can run and a booking page asks which start times are feasible for a new job given everything already committed — a feasibility enumeration rather than a single optimisation, and this reframing is the central piece of work; (2) latency suitable for an interactive page, which means precomputing the near horizon, caching aggressively and invalidating on booking, since a solve per page load will not do; (3) configuration elicited in the operator's language rather than as a model, because the person configuring this runs a salon and the constraint model must be inferred from questions they can answer; (4) stability of offered slots, since availability that shifts between page load and confirmation is worse than a conservative model and the solver must commit to what it displays; and (5) graceful degradation, because an over-constrained model that returns nothing is a business emergency and the system must relax soft constraints and say what it relaxed.

## Target Customer
Scheduling platform vendors, vertical software vendors in health, beauty, fitness and field service, and field service management vendors for whom the travel component is already core.

## Impact If Solved
The solving technology is decades mature and free, and the entire gap is the reframing to interactive feasibility plus a configuration surface an operator can use. Latency and slot stability are the engineering constraints, and neither is hard at this scale.
