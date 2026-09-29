# Buy: Scheduling Infrastructure Adapted to Interchangeable Panels

**Niche:** [[niches/recruiting-tech-vendors/interview-coordination/profile|Interview Scheduling & Coordination]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Scheduling tools find a slot for named people; the panel problem needs a solver over a pool of qualified substitutes nobody has enumerated.
**Tags:** #convex-optimization #graph-theory #dynamic-programming #data-integration #evaluation-metrics #workflow-orchestration #automation #confidence-intervals
**Contested on:** Whether calendar scheduling products can be extended to substitution and constraint solving.

## The Problem

Scheduling software is mature and cheap. Calendar integration, availability negotiation, booking links, round-robin assignment, time zone handling, reminders and rescheduling flows are all standard, and several products handle multi-person scheduling reasonably.

They schedule named people. Round-robin assignment is the closest thing to substitution and it distributes among an undifferentiated pool rather than selecting for a required competency. Nothing in the category solves "find the earliest slot where one qualified assessor for each of these four competencies is simultaneously available, subject to load limits and ordering constraints", which is the actual problem.

## What Already Exists

Calendly, Cal.com and the scheduling category with round-robin and collective availability. ATS-native scheduling modules. Dedicated interview coordination tools. Calendar APIs from the major providers. Constraint solvers — OR-Tools and its peers — which handle the combinatorial core trivially once the problem is specified.

## The Customization Gap

**The interviewer pool by competency has to exist and does not.** This is the data prerequisite and it is an organisational artefact rather than a software feature. Building and maintaining it — who can assess what, calibrated when, at what level — is the substantive work and no scheduling product has a place for it.

**Substitution requires a qualification model, not round-robin.** Round-robin treats a pool as interchangeable. Here interchangeability is conditional on competency and level, and the solver has to respect it.

**The constraints are richer than availability.** Ordering — the hiring manager last, the technical assessment before the design discussion. Load limits per interviewer. Cooling-off between a candidate's sessions. Candidate constraints including a current job and a time zone. Tooling requirements for technical interviews. These are solver constraints and scheduling products express none of them.

**Cancellation should trigger re-solve, not restart.** Every scheduling product treats a cancellation as a return to the beginning. Modelling it as a constraint change with a warm restart is the difference between minutes and days.

**Candidate experience is an objective, not an afterthought.** Minimising elapsed time and session count for the candidate should be in the objective function. Scheduling tools optimise for the organiser, and here the organiser's convenience is what loses the candidate.

## Target Customer

ATS and interview coordination vendors, for whom panel scheduling is a known weakness and a solver is a bounded addition. Also large employers' talent operations teams, who frequently build a partial version internally and would rather not.

## Impact If Solved

The calendar integration, booking, reminder and time zone machinery gets bought, and the competency pool model, qualification-aware substitution, richer constraints, warm-restart re-solve and candidate-centred objective get built. Concretely: a five-person panel scheduled by a solver in a minute rather than by a coordinator over two days.
