# Menu Planning as the Constrained Optimisation It Is

**Niche:** [[niches/restaurant-tech-platforms/non-commercial-foodservice/profile|Non-Commercial Foodservice]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Institutional menu planning is a textbook constrained optimisation — nutrient bounds, cost ceiling, commodity allocations, variety rules, allergen exclusions — and it is performed by a dietitian dragging items around a spreadsheet until the checker stops complaining.
**Tags:** #convex-optimization #optimization-fundamentals #lagrange-multipliers #combinatorics-and-counting #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in institutional foodservice software is fighting to produce a cycle menu that satisfies the nutrition regulation, the allergen safety requirement and the per-meal budget simultaneously — and whoever generates a compliant menu people will actually eat takes the account.

## The Problem
A school foodservice director builds a four-week cycle menu. It must hit calorie, sodium, saturated fat, whole grain, fruit, vegetable subgroup and protein requirements across weekly averages, fit inside a per-meal cost that the reimbursement rate dictates, use the USDA commodity entitlement the district has been allocated, avoid repeating the same entrée too often, work with the equipment each school kitchen actually has, and be acceptable to children. She builds it by hand over several days, runs the nutrient analysis, finds the vegetable subgroups are short in week three, adjusts, re-runs, and repeats. This is the standard practice across the country and it is a solved class of problem being done manually.

## Why Nobody Has Built This
The vendors grew up as compliance documentation products — the regulatory requirement is to prove the menu met the standard, so the software was built to check and to produce the record. Generating rather than checking requires encoding the rules as constraints, which is more work and creates the risk that the vendor's interpretation of a regulation is wrong in a way that a district gets audited for. The acceptability constraint is also genuinely hard and is the reason a naive optimiser fails: a menu that is nutritionally perfect, cheap and uneaten is worse than the hand-built one, and until recently nobody had the participation and plate-waste data to model acceptability at all.

## What to Build
A menu generator that treats the regulation as constraints and acceptability as the objective. Nutrient bounds, cost ceilings, commodity allocations, variety and repetition rules, equipment capability per site and allergen exclusions all enter as constraints; the objective is predicted consumption, estimated from the district's own participation and plate-waste history by item and by grade band. The output is a set of candidate cycle menus rather than one, so the director chooses among genuinely feasible options instead of negotiating with a checker. Infeasibility is reported usefully — which constraint is binding and what relaxation would resolve it — because a menu planner's real question when the vegetable subgroups will not fit is what to trade. The same engine serves healthcare and senior living with therapeutic and texture constraints substituted in.

## Target Customer
School district foodservice directors and the K-12 nutrition vendors, hospital and senior living nutrition services, and the contract caterers running menus at scale across sites.

## Impact If Built
Days of a director's time per cycle, recovered, is the visible gain. The larger one is that optimising for predicted consumption rather than for passing the checker attacks the actual problem in institutional foodservice — food that meets the standard and is thrown away meets neither the budget nor the nutritional purpose, and no current product even measures that, let alone plans against it.
