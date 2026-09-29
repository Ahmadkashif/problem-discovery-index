# Disruption Recovery From Airline Operations

**Niche:** [[niches/scheduling-booking-platforms/schedule-coordinator-recovery/profile|Schedule Coordinator Recovery]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines have solved disruption recovery — rerouting aircraft, crew and passengers after a cancellation, under hard constraints, in minutes — and a clinic reassigns twelve appointments by hand.
**Tags:** #convex-optimization #dynamic-programming #optimization-fundamentals #graph-theory #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor that takes this seriously is fighting to re-solve the day automatically when something moves and propose the recovery — and whoever does that takes the multi-practitioner operator, because rebuilding the day by hand is the coordinator's entire job.

## The Problem
Recovering a schedule after a disruption — reassigning resources, minimising the number of affected customers, respecting hard constraints, and doing it fast enough to matter — is a problem airlines and railways have invested in for decades, with published research, commercial systems and measurable results. A clinic faces a structurally identical and far smaller problem several times a day and solves it with a coordinator and a telephone.

## What Already Exists
Airline disruption management and recovery literature, covering aircraft, crew and passenger recovery; vehicle routing with disruption handling; constraint and mixed-integer solvers, free and fast at this scale; rolling-horizon re-optimisation patterns; and preference and tolerance modelling from revenue management. All published and all available.

## The Customization Gap
The adaptation is to a small business with personal relationships. It requires: (1) an objective centred on client relationships rather than on cost, since a salon's recovery is judged by who was inconvenienced and how they feel about it, which is a different weighting from an airline's; (2) learned per-client tolerance rather than a fare-class rule, because the relevant distinction is which individual will accept a change and that is learnable from their own history; (3) solve times in seconds on modest infrastructure, since these businesses will not run an operations centre and the coordinator is waiting; (4) proposals rather than decisions, because the coordinator knows things no model does — a client's circumstances, a practitioner's mood — and a system that reassigns without asking will be turned off within the week; and (5) the communication half as part of the product, since executing a recovery plan is a dozen conversations and the plan without the messages is half a solution.

## Target Customer
Vertical platform vendors in health, beauty, fitness and field service; scheduling platform vendors moving up-market; and larger multi-site operators with dedicated coordination staff.

## Impact If Solved
A mature operations discipline addresses a far smaller version of the same problem, and the transfer has not been made because the buyer is a clinic rather than an airline. Client-relationship objectives and learned tolerance are the adaptations, and proposing rather than deciding is what makes it adoptable.
