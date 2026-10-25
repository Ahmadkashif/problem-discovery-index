# A Virtual Head Sensor From Pump Run-Times

**Niche:** [[niches/landfill-operators/leachate-pfas-management/profile|Leachate Management & PFAS]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The number that matters — how much leachate sits on each cell's liner — is measured occasionally in a few sumps, while pump cycles, flows and rainfall that could estimate it continuously go unused.
**Tags:** #time-series-forecasting #gaussian-processes #lstms-and-grus #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to keep leachate moving off the liner as treatment plants tighten PFAS acceptance, and whoever has the fewest days with leachate head above the 30 cm design limit takes the account.

## The Problem
Head on the liner rises when inflow outruns pumping or when an outlet stops taking loads. Operators see sump levels, not head across the cell, and find problems from seeps or a regulator's inspection.

## Why Nobody Has Built This
Level transducers in sumps and riser pipes are sparse and drift; pump run-time and flow logs sit in SCADA historians nobody models; and the link to rainfall and cell geometry needs hydrology as well as data work.

## What to Build
A per-cell model that estimates head from pump starts and run-times, measured flows, sump levels, rainfall and the cell's drainage geometry, calibrated against periodic manual measurements, with a 7-to-14-day forecast under the rain outlook and the booked outlet capacity, and alerts before the 30 cm limit is approached.

## Target Customer
Environmental managers at landfills with multiple lined cells and constrained outlets.

## Impact If Built
At a site that logs ~20 days a year above the head limit after storms (estimate), forecasting that books outlets a week earlier could cut that to a handful, avoiding seep repairs and enforcement that can run ~$100K per event (estimate).
