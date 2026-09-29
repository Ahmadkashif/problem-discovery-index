# Routing Optimisation That Includes the Constraints Dispatchers Use

**Niche:** [[niches/field-service-software/residential-trades-platforms/profile|Residential Trades Platforms]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every field service platform ships route optimisation built on commodity solvers, and dispatchers override it every day because it optimises drive time while they are optimising for whether the job gets done.
**Tags:** #dynamic-programming #optimization-fundamentals #combinatorics-and-counting #gradient-boosting #evaluation-metrics #confidence-intervals #workflow-orchestration #automation
**Contested on:** Every serious competitor in residential trades software is fighting to predict what the job actually is before the truck leaves, and to match the technician and the parts to it — and whoever moves first-time fix rate most takes the account.

## The Problem
The optimiser proposes a route that saves forty minutes of driving. The dispatcher rejects it, because the second job is a commercial customer who only accepts one particular technician, the fourth is on a street where the truck with the ladder rack cannot park, and the fifth is a diagnosis that this technician will take two hours over and the other will fix in forty minutes. None of those constraints is in the model. So the optimisation runs, gets overridden, and the vendor records low adoption of a feature that works correctly on the wrong problem.

## What Already Exists
Vehicle routing with time windows is one of the most commoditised optimisation problems in software, available through Google's OR-Tools, commercial solvers, and routing APIs with live traffic. Every field service platform already has one. Skills-based assignment exists in most of them. The solver is not the gap — the constraint model is.

## The Customization Gap
The adaptation is to model what dispatchers actually optimise. It requires: (1) expected job duration predicted per technician per job type rather than taken from a flat-rate book, since duration variance between technicians on the same job dwarfs drive-time differences and is the single largest omission; (2) parts availability on each truck as a hard constraint, which requires truck inventory to be real, and is the difference between a route that completes and one that generates a return visit; (3) customer-technician affinity and continuity as a soft objective, because the trades run on relationships and a routing engine will trade them away for eight minutes; (4) probability of first-time fix as the objective alongside drive time, which changes the answer in most cases and is computable once the diagnosis prediction exists; and (5) continuous re-optimisation as the day degrades, proposing the minimal change rather than a new plan, since the dispatcher's real job is reacting to disruption and a full re-plan at eleven o'clock is unusable.

## Target Customer
Field service platforms whose routing features are shipped and unadopted, and dispatch-heavy residential contractors running six or more trucks.

## Impact If Solved
Optimising for completed jobs rather than for drive time is what makes a dispatcher accept a proposal, and acceptance is the entire value — an unused optimiser saves nothing. Minimal-change re-optimisation addresses the dispatcher's actual day, which is continuous re-planning, and is the feature most likely to be used hourly rather than once each morning.
