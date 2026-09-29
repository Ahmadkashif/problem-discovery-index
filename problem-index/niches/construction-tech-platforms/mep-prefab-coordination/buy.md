# Manufacturing Execution Systems Adapted to the Prefab Shop

**Niche:** [[niches/construction-tech-platforms/mep-prefab-coordination/profile|Mechanical & Electrical — Model-to-Fabrication Chain]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** A prefabrication shop is a job-shop manufacturing operation, manufacturing execution systems have solved job-shop scheduling and tracking for decades, and construction prefab shops run on whiteboards.
**Tags:** #dynamic-programming #optimization-fundamentals #combinatorics-and-counting #time-series-forecasting #evaluation-metrics #workflow-orchestration #automation #data-integration
**Contested on:** Every serious competitor in MEP contractor software is fighting to carry a coordinated model through to a fabricated, delivered, installed and tracked assembly without anyone redrawing it — and whoever closes that chain with the fewest re-entries takes the account.

## The Problem
A prefab shop supports six projects with different schedules, shared machines, shared welders and a finite floor. Sequencing is done by a shop manager with a whiteboard and knowledge of which projects are shouting loudest. When a project's need date moves — which is constantly — the consequences for the other five are worked out in a meeting. Material is ordered per project rather than pooled, so the shop carries inventory it does not need and runs out of what it does. None of this is exotic; it is the standard set of problems that manufacturing solved with production planning.

## What Already Exists
Manufacturing execution systems, finite capacity scheduling and shop floor control are mature categories with dozens of vendors, from full MES suites to lightweight job-shop scheduling products. Nesting and cutting optimisation is standard in the fabrication equipment vendors' own software. Inventory and material requirements planning is available at every price point. The construction prefab market has a handful of specialist products, generally thinner than what manufacturing has had for twenty years.

## The Customization Gap
The adaptation is to a shop whose demand signal is a construction schedule. It requires: (1) taking need dates from the project schedule and treating them as soft, probabilistic dates rather than hard due dates, because a construction need date is a forecast and scheduling a shop as if it were certain produces work that sits in a yard; (2) explicit handling of change — a coordination revision invalidates work in progress, and the scheduler must know what is already cut, which is where the identity layer becomes load-bearing; (3) pooling material and shared resources across projects while preserving per-project cost attribution, since the contractor still has to job-cost; (4) sequencing that accounts for site delivery constraints and laydown capacity, which are the real bottlenecks more often than the shop is; and (5) an honest capacity model that lets the contractor answer whether taking another project is feasible, which is currently answered by instinct.

## Target Customer
Mechanical, electrical and sheet metal contractors operating prefabrication shops of any scale, and the construction fabrication software vendors who could adopt manufacturing planning wholesale rather than reinventing it.

## Impact If Solved
Job-shop scheduling applied to prefab typically raises effective shop throughput without capital expenditure and cuts the work-in-progress sitting in laydown yards. The more valuable change is decision quality: a contractor that can answer whether the shop can absorb another project stops discovering the answer in the middle of it.
