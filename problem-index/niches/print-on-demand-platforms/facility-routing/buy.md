# Assignment Optimisation and Supplier Scorecards

**Niche:** [[niches/print-on-demand-platforms/facility-routing/profile|Facility Routing]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Operations research solved multi-objective assignment and procurement built supplier scorecards that drive allocation, and this routing uses distance.
**Tags:** #convex-optimization #optimization-fundamentals #evaluation-metrics #confidence-intervals #descriptive-statistics #revenue-impact #dynamic-programming #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to send each order to the facility that will produce it well rather than the one that is nearest — and whoever does that takes the quality, because quality is the variable the routing decision currently omits.

## The Problem
Assigning jobs to resources under multiple objectives and constraints is one of the oldest solved problems in operations research, with exact and heuristic methods for every scale. Procurement built the complementary practice: supplier scorecards combining quality, delivery and cost, with allocation driven by the score so that good suppliers gain volume and poor ones lose it. This routing uses distance and a capacity check, and allocates volume by proximity regardless of performance.

## What Already Exists
Assignment and transportation problem formulations with multi-objective extensions; real-time dispatch optimisation from logistics; supplier scorecard methodology with weighted performance dimensions; allocation mechanisms tying volume to score; and capacity-aware scheduling with load balancing.

## The Customization Gap
The adaptation is to a quality dimension that depends on the specific job. It requires: (1) supplier quality scored per work type rather than overall, since a facility's competence varies enormously by decoration method and substrate and a single score would route as badly as distance does — this granularity is the specific adaptation; (2) the objective expressed as expected total cost including reprint and delay, which makes the multi-objective problem a single-objective one and is the modelling simplification that makes it tractable at volume; (3) exploration built into the allocation, since a scorecard that only rewards the current leader never learns about anybody else; (4) decisions made in milliseconds at high volume, which rules out exact optimisation per order and argues for a learned policy; and (5) contractual allocation commitments respected, since partner agreements frequently guarantee volume and the optimisation must work within them.

## Target Customer
Network operations, partner management, and the operations research and procurement communities whose methods transfer with a per-work-type quality dimension.

## Impact If Solved
Multi-objective assignment is solved and supplier scorecards drive allocation everywhere else, and this routing uses distance. Scoring quality per work type rather than overall is the specific adaptation, and expressing everything as expected total cost makes the problem tractable at volume.
