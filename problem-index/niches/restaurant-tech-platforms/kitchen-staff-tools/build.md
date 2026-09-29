# The Prep List That Computes Itself

**Niche:** [[niches/restaurant-tech-platforms/kitchen-staff-tools/profile|Kitchen Staff & Back-of-House Tools]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tomorrow's prep list is a function of tomorrow's forecast demand, today's inventory and each item's shelf life, and it is written every morning by a sous chef from memory while standing in a walk-in.
**Tags:** #time-series-forecasting #optimization-fundamentals #gradient-boosting #confidence-intervals #evaluation-metrics #dynamic-programming #automation #worker-facing
**Contested on:** Every serious competitor building for the back of house is fighting to get the prep list, the par levels and the station setup to the line in a form usable with wet hands during service — and whoever the cooks actually use takes the kitchen.

## The Problem
A sous chef arrives at nine, walks the walk-in, notes what is low, thinks about what day it is, and writes a prep list. The list is a set of quantity decisions — how much of each sauce, stock, portioned protein and prepped vegetable — each of which is a forecast against a shelf life. Too much and it is thrown out in three days; too little and the line runs out on Saturday. The information that would make these decisions well is available: forecast demand by item, current inventory, recipe yields, shelf lives, and the kitchen's own history of what it prepped versus what it used. None of it is assembled, so the list is a skilled guess repeated every morning for the length of a career.

## Why Nobody Has Built This
The prep list sits downstream of a demand forecast the category does not produce, so it has been unbuildable for the same reason everything else in this industry is unbuilt. It also requires an accurate inventory of prepped items, which almost no kitchen maintains, because counting prepped items is work with no visible payoff. And the interface constraint is severe: whatever is produced has to be usable by a cook with wet hands at six in the morning, which rules out most of what a product team would naturally build and has discouraged serious attempts.

## What to Build
A prep planner that takes the item-level demand forecast, current prepped and raw inventory, recipe yields and shelf lives, and computes a quantity per prep item with the shelf-life constraint handled explicitly — producing more of a long-life item and less of a short-life one at the same demand uncertainty is the whole craft, and it is an optimisation rather than an intuition. Output is a printed or displayed list in the kitchen's own order, by station, in quantities expressed in the units the kitchen works in rather than in decimal pounds. Production is confirmed at the station with a tap, which gives the system the actual-versus-planned data it needs to improve, and which is the only input it should ever ask a cook for. Shortages and over-production are reported to the chef weekly by item, which is the first time most kitchens will have seen that pattern.

## Target Customer
Full-service and high-volume kitchens where prep is a significant daily labour block, restaurant groups standardising back-of-house practice, and the back-office vendors whose recipe data already sits unused for this purpose.

## Impact If Built
Prep is the largest controllable source of food waste in a full-service kitchen and a substantial labour block, and computing it against a forecast rather than a memory improves both. The more durable gain is knowledge transfer: the prep decisions of a departing sous chef currently leave with them, and a computed list with recorded outcomes is the institutional version of that knowledge.
