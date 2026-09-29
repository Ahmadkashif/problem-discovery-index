# Workforce Optimisation Solvers From Larger Industries

**Niche:** [[niches/restaurant-tech-platforms/labor-scheduling-availability/profile|Labour Scheduling & Availability]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Nurse rostering and airline crew scheduling are decades-old solved disciplines with mature solvers and a deep literature, and restaurant scheduling — a structurally simpler version of the same problem — is done in a spreadsheet.
**Tags:** #optimization-fundamentals #convex-optimization #dynamic-programming #combinatorics-and-counting #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in restaurant scheduling is fighting to produce a schedule that respects who can genuinely work, so the manager stops spending the week on the phone finding cover — and whoever gets the share of shifts that survive the week highest takes the account.

## The Problem
Restaurant auto-scheduling, where it exists, is typically a greedy assignment: fill the highest-demand shifts first from whoever is available, then work down. It produces schedules that satisfy coverage and violate everything soft — someone closing then opening, an unbalanced distribution of desirable shifts, a senior server given three shifts and a new hire five. Managers then edit heavily, which is the same as building it by hand with extra steps.

## What Already Exists
Employee rostering is one of the most studied problems in operations research, with an extensive literature, standard benchmark instances, and mature open-source and commercial solvers — constraint programming frameworks and MIP solvers handle problems of this size trivially. Nurse rostering in particular addresses nearly the same constraint structure: skills, shift patterns, rest requirements, fairness, and preferences. Predictive scheduling compliance rules are published statute. Nothing needed here has to be invented.

## The Customization Gap
The adaptation is in the objective and the constraint vocabulary rather than the solver. It requires: (1) a demand model at daypart resolution feeding coverage requirements, without which the optimisation is solving the wrong problem precisely; (2) fairness encoded explicitly — distribution of closing shifts, weekend shifts and high-tip shifts — because these are what staff actually complain about and what no greedy assignment handles; (3) predictive scheduling statutes as hard constraints with their notice periods and premium-pay penalties modelled, since in covered jurisdictions a schedule change has a real cost that should be in the objective rather than discovered in payroll; (4) rest and clopening rules as constraints even where not legally required, because they are the largest driver of turnover in the segment and a solver will happily produce them otherwise; and (5) a solve fast enough to re-run interactively, since a manager's real workflow is making a change and seeing the consequences, not generating once.

## Target Customer
Restaurant scheduling vendors, and the multi-unit operators sophisticated enough to build this themselves if nobody sells it.

## Impact If Solved
Adapting a mature rostering solver gets a restaurant vendor a schedule quality that heuristic assignment will never reach, at a fraction of the development cost, with known behaviour on hard instances. The fairness and rest constraints are the part that matters most to staff and cost nothing extra to include once the model is formulated properly.
