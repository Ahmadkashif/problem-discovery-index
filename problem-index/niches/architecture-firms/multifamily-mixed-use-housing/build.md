# Feasibility Studies That Carry Their Own Cost Model

**Niche:** [[niches/architecture-firms/multifamily-mixed-use-housing/profile|Multifamily & Mixed-Use Housing]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Site yield tools count units in minutes; whether those units pencil depends on a cost per unit nobody estimates until weeks later.
**Tags:** #gradient-boosting #gaussian-processes #bayesian-optimization #feature-engineering #revenue-impact #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to fit the most rentable units onto a site under zoning and code at a construction cost per unit that makes the developer's pro forma pencil, and whoever proves yield and cost fastest at feasibility takes the account.

## The Problem
A developer has a site under option for a few weeks and asks two or three architects for test fits. The architect shows unit counts and massing; the developer's estimator or a contractor prices it later. Schemes that maximise units often do so with expensive moves — deeper excavation, a taller podium, a construction type change — that erase the margin, and the developer learns this after the option money is spent.

## Why Nobody Has Built This
Yield tools are geometry engines; cost lives with contractors and estimators who price from drawings, not from massing. Architects hold their own past projects' unit counts and construction types but rarely the final costs, which sit with the developer and contractor.

## What to Build
A feasibility engine that pairs every yield option with a cost-per-unit range from a model trained on completed projects (structure type, podium levels, parking ratio, unit mix, enclosure ratio, region), searches the option space for the best margin rather than the most units, and exports straight into the developer's pro forma format.

## Target Customer
Housing studio principals at firms doing repeat developer work, and development directors at regional multifamily developers.

## Impact If Built
Better go/no-go decisions on land at the point they are cheapest, and an architect whose feasibility work the developer cannot get elsewhere.
