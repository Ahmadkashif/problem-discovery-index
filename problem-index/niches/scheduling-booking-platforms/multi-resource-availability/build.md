# The Business the Configuration Screen Cannot Describe

**Niche:** [[niches/scheduling-booking-platforms/multi-resource-availability/profile|Multi-Resource Availability]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform can express availability and none can express a real business, so operators simplify their bookable offering and quietly sell less than their capacity.
**Tags:** #convex-optimization #dynamic-programming #optimization-fundamentals #graph-theory #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to let a real business express what it can actually deliver — staff with different skills, constrained rooms and equipment, service-specific buffers and travel — and whoever does that takes the account, because businesses currently simplify their availability and sell less than they could.

## The Problem
A clinic has four therapists, three rooms, one specialised machine, and eleven services. Two therapists can deliver all eleven; the others can deliver six between them. Three services need the machine. One needs the large room. Turnaround is ten minutes for most services and twenty-five for two of them. The owner spends an afternoon in the configuration screen, cannot express any of the interactions, and settles on a model where each therapist has a fixed weekly pattern and only four services are bookable online. Everything else goes through the phone, and the online availability shown to customers is a conservative subset of what the clinic could actually deliver on any given day.

## Why Nobody Has Built This
The category grew from the individual scheduling link, where one person's calendar is the whole model, and multi-resource support was added as a second calendar type rather than as a change of model. Solving combinations properly is a constraint problem the products do not have a solver for, and configuration surfaces are forms, which cannot express conditional and interacting rules no matter how many fields are added. Vendors also see no evidence of a problem, because the simplification is invisible in their data — a customer who never sees an available slot does not generate a failed booking.

## What to Build
Availability as a solved query rather than a stored calendar. Model the business as resources with capabilities and constraints: staff with per-service competency and realistic service durations, rooms and equipment with their own availability and their service compatibility, turnaround and setup times that depend on the service pair rather than being fixed, mutual exclusions, and travel time computed from actual locations for mobile work. Compute bookable slots by solving for a feasible assignment of every required resource, which is what makes combinations correct and is the technical heart of it. Keep the latency low enough to answer a booking page, which is achievable by precomputing the near horizon and solving on demand for the rest. Present configuration as questions about the business rather than as a form — how long does this take, who can do it, what does it need, what cannot run alongside it — since the operator knows all of this and cannot translate it into fields. And show the operator what they can now sell that they could not before, in money, because that is the only argument that will make them reconfigure a system that currently works badly but predictably.

## Target Customer
Multi-practitioner clinics, salons, studios, workshops and mobile service businesses; and the vertical platform vendors serving them, for whom availability correctness is the difference between a booking module and a booking system.

## Impact If Built
The unsold capacity is invisible to everyone, including the vendors, because a slot never offered generates no data. Solving for resource combinations rather than storing calendars is the model change, and the recovered-capacity number is what makes an operator willing to migrate.
