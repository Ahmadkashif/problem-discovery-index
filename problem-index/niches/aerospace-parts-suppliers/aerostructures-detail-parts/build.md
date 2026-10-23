# A Rate-Break Capacity Model From the Routing

**Niche:** [[niches/aerospace-parts-suppliers/aerostructures-detail-parts/profile|Aerostructures & Airframe Detail Parts]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Suppliers answer a prime's "can you hold the next rate?" with a spreadsheet of standard hours; nobody builds the answer from actual machine, programmer and inspection data.
**Tags:** #linear-regression #monte-carlo-methods #time-series-forecasting #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show a prime that a supplier can hold the next rate break, and whoever builds a capacity plan from the shop's own routings and machine data that survives the prime's rate-readiness review takes the account.

## The Problem
A tier-2 shop making ~300 part numbers for a fuselage programme must show its customer that it can move from 42 to 47 shipsets a month and on to the next step Boeing is planning. Its planners multiply standard hours by rate and compare against machine counts. Standard hours are years old, five-axis machines are shared across programmes, CMM and FAI capacity is ignored, and outside processing is a fixed number of days. The prime knows this and discounts the answer.

## Why Nobody Has Built This
APS vendors sell scheduling, not rate scenarios; the data (actual cycle times from machine monitoring, inspection queues, processor turn times) sits in four systems; and each prime asks for a different template.

## What to Build
A model that learns actual hours per operation from machine monitoring and job history, adds inspection, FAI and outside-processing capacity, and simulates each rate step with uncertainty (Monte Carlo over cycle-time and scrap variation). It names the binding constraint by month (a machine, a programmer, a CMM, a processor) and costs the fix, and it exports the prime's rate-readiness template from the same model.

## Target Customer
VP Operations and programme managers at structures and detail-part suppliers facing 2026–2027 rate breaks.

## Impact If Built
A credible plan wins share at re-sourcing and avoids the ~$0.5–2M a year (estimate) of expedite premiums, overtime and late-delivery penalties a mid-size supplier carries when it overcommits.
