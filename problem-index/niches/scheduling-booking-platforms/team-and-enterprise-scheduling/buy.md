# Calendar Constraints as an Optimisation Problem

**Niche:** [[niches/scheduling-booking-platforms/team-and-enterprise-scheduling/profile|Team & Enterprise Scheduling]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Constraint programming and scheduling optimisation are among the most developed areas of operations research, with free solvers that handle far harder problems, and team scheduling intersects free-busy blocks.
**Tags:** #convex-optimization #dynamic-programming #optimization-fundamentals #graph-theory #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to place a meeting that involves more than one busy internal calendar without a human brokering it — and that contest splits by what the meeting is for, which is why this niche is not terminal and is decomposed below.

## The Problem
Placing activities subject to resource availability, precedence, eligibility and preference constraints is the scheduling problem, and operations research has spent sixty years on it. Free solvers handle factory schedules, crew rosters and timetables with thousands of variables. Team meeting scheduling — a handful of people, a few constraints, a week of slots — is a small instance of it, and the products solve it by displaying the intersection of free time and letting a human choose.

## What Already Exists
Constraint programming solvers and mixed-integer solvers, free and mature, that dispatch problems of this size instantly. Employee and crew scheduling literature. Timetabling research, which handles precisely the multi-party, multi-constraint case. Calendar APIs exposing free-busy across the major providers. Preference elicitation and stable matching methods for the assignment half.

## The Customization Gap
The adaptation is to human calendars and soft preferences. It requires: (1) preferences as soft constraints with weights rather than hard rules, since "prefers mornings", "no meetings on Friday afternoons" and "needs thirty minutes between calls" are real and violable, and a solver treating them as hard will return infeasible far too often; (2) uncertainty in the availability data itself, because a free-busy block is not the truth — people hold provisional time, accept meetings they will move, and keep undeclared focus time, which means the optimal solution on paper is frequently declined; (3) latency budgets in the seconds, since the solve happens while a person waits on a booking page and an optimal answer in ninety seconds is worthless; (4) explicability, because an assignment nobody understands is overridden, and the solver must be able to say why this person and this time; and (5) incremental re-solving when something moves, which is the common case and is far more valuable than the initial solve — the repair problem rather than the construction problem.

## Target Customer
Scheduling platform vendors, applicant tracking and customer relationship vendors with scheduling modules, and large organisations with dedicated coordination functions.

## Impact If Solved
An extremely mature optimisation field addresses a problem the category solves by displaying free time. Soft preferences and availability uncertainty are the two adaptations, and incremental re-solve is where most of the practical value is.
