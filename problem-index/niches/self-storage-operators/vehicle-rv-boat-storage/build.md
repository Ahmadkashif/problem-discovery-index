# Space Assignment and Pricing by Vehicle Length and Season

**Niche:** [[niches/self-storage-operators/vehicle-rv-boat-storage/profile|Vehicle, RV & Boat Storage Lots]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** RV and boat lots sell spaces by a size code, so a 25-foot trailer sits in a 45-foot space while a 42-foot coach waits on a list.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #bayesian-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to fill outdoor and covered vehicle spaces with the vehicles that pay most for the space they take, and whoever earns the most rental income per acre takes the account.

## The Problem
A vehicle lot's revenue depends on fitting the right vehicles into the right spaces: long rigs in pull-through rows, boats in covered bays, vans near the gate. Spaces are rented first come, first served, at one price per size code, and move-outs leave gaps nobody re-packs. Seasonal demand is predictable, but prices do not follow it.

## Why Nobody Has Built This
Storage software treats parking as another unit type. Parking software prices hours, not seasons. The lots are mostly owned by independents and small portfolios, too small for a pricing team, and the space map lives in the manager's head.

## What to Build
A space planner with three parts. A site model records each space's length, width, clearance, cover and access. An assignment optimiser places new and waitlisted vehicles to maximise revenue per acre, proposing occasional moves at renewal when re-packing frees a premium space. A seasonal demand forecast by vehicle type sets prices for open, covered and enclosed spaces and charges the waitlist where demand exceeds supply. Gate events, and plate reads only from consented captures or synthetic test images with plates deleted after matching, confirm which vehicles are actually on site.

## Target Customer
Owners of dedicated RV and boat storage facilities; storage operators with large parking areas.

## Impact If Built
If better assignment fills ~5–10% more of a lot's linear footage (estimate) and seasonal pricing adds ~3–5%, a lot earning ~$400,000 a year gains ~$30,000–60,000.
