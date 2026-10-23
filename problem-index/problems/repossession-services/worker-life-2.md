# The Camera Car Driver Paid Only on Recovery

**Industry:** [[repossession-services|Repossession Agencies]]
**Type:** Worker Life Changing
**One-liner:** The driver who spends eight hours a night scanning apartment lots with licence-plate cameras is commonly paid by the hit or the recovery, not the hour, and plans the route by habit — so a slow night is an unpaid night and nobody can tell them which streets would have paid.
**Tags:** #time-series-forecasting #optimization-fundamentals #markov-decision-processes #gradient-boosting #worker-facing #revenue-impact #automation

## The Problem
Licence-plate recognition changed how cars are found. A camera car — sometimes a marked truck, often an ordinary car with cameras behind the windows — drives through apartment complexes, employer lots, shopping centres and side streets, and every plate it reads is checked against the hot list of cars up for repossession. A match pings the driver, who confirms the make, model and colour by eye before marking it located; the reporting shows alerts rejected because the car did not match. The agency then sends a truck, or the driver recovers it if they are also the agent.

Many agencies pay camera drivers per confirmed hit or per resulting recovery rather than by the hour (estimate; pay practices were not surveyed). The driver often supplies the car, pays for fuel, and drives from evening into the small hours. Which complexes to work, in what order and at what hour is decided by experience and habit: the lots that paid last month, the neighbourhoods where hot-list cars cluster. The scans the driver collects build the camera network's database, but the driver sees only their own hits, not where scans are thin or where hot-list density is rising.

## Why It Matters to the Worker
Income is lumpy and outside the driver's control. A night of thousands of scans and no confirmed hits earns nothing, while the fuel and the hours are gone. The work is solitary, sedentary and nocturnal, done in places where residents increasingly notice and object to cameras, and it is easy to get wrong: a hurried confirmation sends a truck after the wrong car. Drivers stay in the job while their personal map of good lots pays, and leave when it stops.

## What a Solution Looks Like
A shift planner that forecasts hot-list density and likely hits by area and hour from the agency's open assignments and the driver's past scan and hit history, proposes a route that covers the highest-yield lots at the hours cars are home, and re-plans when a hit is confirmed and the truck is dispatched. Hit confirmation is assisted — the app compares the camera image's make, model and colour with the assignment and asks the driver only when it is unsure. At the end of the shift the driver sees scans, hits, confirmed recoveries and pay in one place, and how tonight's route compared with the plan.

## Impact If Solved
A planner that lifts confirmed hits per driving hour by ~20–30% (estimate) turns the same eight-hour shift into steadier pay and cuts the share of zero-hit nights, fewer false confirmations protect the agency and the borrower, and a driver who can see what each route earns can decide for themselves whether the night is worth working.
