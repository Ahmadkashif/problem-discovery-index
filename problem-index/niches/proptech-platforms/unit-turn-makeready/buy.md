# Project Scheduling Tooling Applied to a Five-Day Project

**Niche:** [[niches/proptech-platforms/unit-turn-makeready/profile|Unit Turn & Make-Ready Sequencing]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Critical path scheduling and resource-constrained project planning are textbook techniques with free implementations, and the rental industry runs tens of thousands of small dependency-constrained projects a year on a notebook.
**Tags:** #dynamic-programming #graph-theory #optimization-fundamentals #combinatorics-and-counting #evaluation-metrics #confidence-intervals #workflow-orchestration #automation
**Contested on:** Every serious competitor in turn operations is fighting to get a vacant unit from move-out to rent-ready in the fewest days across five vendors who do not talk to each other — and whoever cuts days-vacant most takes the account.

## The Problem
A turn has all the properties project scheduling was invented for: tasks with durations, precedence constraints, shared resources across concurrent turns, and a cost of delay. Construction schedules a thousand-task project this way routinely. A property operator running forty simultaneous turns across a portfolio, competing for the same three painters, schedules each one independently by phone and discovers the resource contention when a vendor says he is at another property.

## What Already Exists
Critical path method, resource-constrained project scheduling and the associated solvers are textbook, with free and mature implementations including constraint programming toolkits that handle problems of this size instantly. Workforce and job scheduling products exist at every price point. The methods are taught in every operations course and are older than the software industry.

## The Customization Gap
The adaptation is to a very small project run at very high volume by people who will never open a Gantt chart. It requires: (1) scheduling across concurrent turns rather than per turn, since the binding constraint is almost always a shared vendor's capacity across a portfolio and per-unit scheduling misses it entirely; (2) durations as distributions from the operator's realised history rather than as fixed estimates, because the whole failure mode is a plan built on optimistic point estimates; (3) an interface that is a list of what happens next and who to expect, not a network diagram, since the user is a site manager between two showings; (4) communication with vendors through text and voice confirmation, because this vendor population has no systems to integrate with and any design assuming otherwise will not be adopted; and (5) continuous re-planning on every event, delivered as a notification of what changed rather than a new schedule to interpret.

## Target Customer
Property operators and turn-services companies, and the platform vendors who could embed a solver rather than another checklist.

## Impact If Solved
Portfolio-level scheduling against shared vendor capacity is the part that no manual process can do and that the solver does trivially, and it is where most of the recoverable days are. The tooling is free; the work is in duration modelling and in an interface that a site manager will use in fifteen seconds.
