# Harvest Labour Scheduling From Workforce Optimisation

**Niche:** [[niches/agtech-platforms/specialty-permanent-crops/profile|Specialty & Permanent Crops]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Harvest is the largest cost in specialty crops and the hardest scheduling problem on the farm, and workforce optimisation — which solves exactly this shape of problem in every other industry — is not used at all.
**Tags:** #optimization-fundamentals #dynamic-programming #combinatorics-and-counting #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in specialty crop software is fighting to manage a permanent planting at the block and the tree rather than at the field — and whoever makes per-block economics and harvest labour legible takes the operation.

## The Problem
Nine blocks reach harvest readiness across a three-week window that overlaps unpredictably with the weather. Crews of varying size and skill must be allocated across blocks, each of which has a different yield, a different picking rate and a different quality penalty for being picked early or late. Bins, trucks and packing house slots are all constrained. The harvest manager plans it on a whiteboard each morning, adjusts constantly, and the cost of getting it wrong is fruit picked at the wrong maturity or left on the tree.

## What Already Exists
Workforce scheduling and resource-constrained allocation are mature disciplines with free solvers, as the restaurant, construction and field service examples elsewhere in this vault describe. Crop maturity modelling from degree-day accumulation is established agronomy. Weather forecasting is commodity. Yield estimation from imagery and from sampling is an active and reasonably developed area. Every component exists.

## The Customization Gap
The adaptation is to a perishable window and a variable workforce. It requires: (1) block readiness modelled as a window with a quality penalty curve rather than a date, since the real decision is a trade-off between picking a block slightly early and leaving another slightly late; (2) crew productivity estimated per crew per block from the operation's own history, because picking rates vary enormously with block characteristics and crew composition and a uniform assumption produces a plan that fails on day one; (3) weather integrated as a constraint and a risk, since rain closes a window and a plan that ignores the forecast is replanned every morning anyway; (4) downstream capacity — bins, transport, packing house slots — as hard constraints, because harvesting more than can be moved and packed is a common and expensive failure; and (5) replanning presented as the minimal change from this morning's plan rather than as a new plan, since the crews are already deployed and a wholesale reshuffle is not executable.

## Target Customer
Orchard, vineyard and vegetable operations with substantial harvest labour, harvest labour contractors, and the packing and marketing organisations whose capacity planning depends on the same information.

## Impact If Solved
Harvest cost and harvest timing together determine most of a specialty operation's margin, and the planning is done on a whiteboard against a perishable clock. Crew productivity estimation is the specific adaptation that makes the plan realistic and is derivable from records the operation already keeps for payroll.
