# The Hot-Shot Driver's Forty Runs

**Industry:** [[auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Worker Life Changing
**One-liner:** The commercial delivery driver gets back a day that is planned instead of shouted across the counter: fewer one-part runs, fewer return trips for wrong parts, and no phone calls at red lights.
**Tags:** #dynamic-programming #markov-decision-processes #optimization-fundamentals #time-series-forecasting #worker-facing #automation

## The Problem
A commercial parts store's delivery driver, often in a compact car or small pickup, runs ~20–50 deliveries a day to repair shops within a few miles (estimate). Each run is triggered at the counter: a part is pulled, a ticket printed, and someone shouts that the shop on Main Street needs it now. The driver goes, often with one part, comes back, and goes again. A wrong part means a second trip to the same shop. A return or a core to collect adds a stop that nobody planned. Shops call the store asking where their part is, the counter calls the driver, and the driver answers while driving. Pay is hourly and near the bottom of the store's scale (QCEW put average pay at the parts-store code at ~$40,600 in 2024 across all roles), turnover is high, and the job is how many counter pros start.

## Why It Matters to the Worker
The driver's day is shaped by other people's urgency and mistakes. Back-to-back single-part runs mean more miles, more traffic and more chances of an accident under time pressure, with no say in the order of stops. The second trip for a wrong part is the driver's wasted hour, even though the error was made at the counter or in the catalog. Being the person a shop yells at when a part is late, and the person the counter calls mid-run, makes a low-paid job stressful in ways that have nothing to do with driving.

## What a Solution Looks Like
A dispatch view on the driver's phone that batches orders by direction and promised time, holds a run for a few minutes when the next order to the same street is likely, and adds core and return pickups to runs already going that way. Shops see live arrival times instead of calling. Wrong-part re-runs are logged against their cause, so the counter and the catalog, not the driver, absorb the blame. The driver interacts with one screen: next stop, what to hand over, what to collect, with voice confirmation so the phone stays in the mount.

## Impact If Solved
If consolidation cut runs by ~15–25% at the same service level (estimate), a driver would drive ~10–20 fewer miles a day, take fewer calls behind the wheel, and spend the saved hour on core pickups that are now missed, which is also money back to the store.
