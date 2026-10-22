# Route Optimisation Pointed at the Delivery Van

**Niche:** [[niches/libraries-and-archives/public-ils-and-consortium-circulation/profile|Public Library ILS & Consortium Circulation]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Delivery route software optimises stops and miles; a library's van problem is which crates to carry and when, set by the holds queue.
**Tags:** #optimization-fundamentals #graph-theory #time-series-forecasting #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to fill a patron's hold from any shelf in a shared consortium catalogue in the fewest days, without losing a hold or a patron record when the system changes, and whoever makes daily holds delivery and the migration least risky takes the consortium's shared contract.

## The Problem
Consortium delivery runs on fixed routes drawn years ago, sized by crate counts from the last busy season. Volumes swing with holds and floating collections.

## What Already Exists
Route optimisation software for field service and delivery fleets (OptimoRoute, Route4Me, Routific) and the routing tools inside courier contracts.

## The Customization Gap
The library version needs crate forecasts per branch pair from ILS holds and transit data, branch opening hours and staff sorting windows, and a link back to holds routing so that which copy is paged and which van carries it are decided together. Off-the-shelf tools take stops and demand as given.

## Target Customer
Delivery coordinators at consortia and regional library systems that run their own vans or contract couriers.

## Impact If Solved
Routes sized to forecast volume reduce overflow days and idle runs, cutting delivery cost and hold wait times together.
