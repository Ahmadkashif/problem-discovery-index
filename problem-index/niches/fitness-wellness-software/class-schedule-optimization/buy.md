# Constrained Scheduling Solvers for the Weekly Grid

**Niche:** [[niches/fitness-wellness-software/class-schedule-optimization/profile|Class Schedule Optimisation]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Timetabling under staff, room and preference constraints is a textbook optimisation problem with free solvers and a large literature, and a studio grid is built by dragging blocks around a calendar.
**Tags:** #optimization-fundamentals #combinatorics-and-counting #dynamic-programming #convex-optimization #evaluation-metrics #confidence-intervals #workflow-orchestration #automation
**Contested on:** Every serious competitor in studio scheduling is fighting to build a grid from measured demand rather than from instructor availability and habit — and whoever raises revenue per class hour most takes the account.

## The Problem
Building a grid means satisfying instructor availability and qualifications, room and equipment capacity, format spacing so similar classes do not compete with each other, staffing costs, and the demand pattern — simultaneously. An owner does it by moving blocks on a calendar until nothing obviously conflicts, which finds a feasible schedule and never a good one. The problem is a timetabling problem, which is among the most studied in operations research, and the studio is solving it by hand at a scale where a solver would return an answer instantly.

## What Already Exists
University and school timetabling has produced decades of literature, standard benchmark problems and mature open-source solvers. Constraint programming toolkits handle problems of this size in seconds. Staff rostering methods, as used in the restaurant and healthcare examples elsewhere in this vault, apply directly. Nothing in the required machinery is expensive or unproven.

## The Customization Gap
The adaptation is to the studio's objective and its social constraints. It requires: (1) demand rather than feasibility as the objective, since any grid that satisfies the constraints is feasible and the studio needs the one that earns most — which means the demand model is the precondition and the solver is the easy part; (2) instructor preferences as weighted rather than hard constraints, with the cost of honouring each one visible, because the current practice treats availability as absolute and the owner should at least see what that costs; (3) cannibalisation between similar formats at nearby times modelled explicitly, since a solver that ignores it will happily schedule two competing classes an hour apart; (4) incremental change as the output format, because a studio will not adopt a wholly new grid and will consider three specific moves — this is a product decision that determines whether any of it is used; and (5) member impact considered, since moving a class that a group of long-standing members organise their week around has a retention cost that does not appear in the revenue calculation and should be surfaced.

## Target Customer
Studio platform vendors, multi-location operators building grids across sites, and the programming leads at larger studios.

## Impact If Solved
The solver is free and the literature is mature; the value is entirely in the objective function and in presenting the output as three changes rather than a new timetable. Making the cost of each instructor preference visible is the quietly important part, because it converts an unexamined constraint into a deliberate choice.
