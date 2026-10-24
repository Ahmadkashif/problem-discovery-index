# A Season Forecast That Books February

**Niche:** [[niches/powersports-and-boat-dealers/seasonal-service-capacity/profile|Spring Commissioning & Seasonal Service Capacity]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Service managers know the spring wall is coming and still meet it unbooked, because nothing turns last year's repair orders and this year's storage contracts into a plan.
**Tags:** #time-series-forecasting #exponential-smoothing #temporal-fusion-transformers #gradient-boosting #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to fill the service department's technician hours through the spring commissioning peak and the winter trough, and whoever bills the most technician hours per technician across the year takes the account.

## The Problem
Every spring the backlog runs to weeks, customers miss their first lake weekend, some take their boats elsewhere, and technicians work ~55-hour weeks (estimate). Every January the same technicians are short of hours. The demand is largely predictable: the dealer holds the storage and winterization contracts, last year's repair orders and the list of units sold last season.

## Why Nobody Has Built This
DMS schedulers work day by day. Forecasting needs repair lines classified by job type, which are free text, and weather and calendar data no dealer system holds.

## What to Build
A weekly demand forecast by job type and skill from storage contracts, prior repair orders (classified by a text model), last season's sales, weather, ice-out and holiday calendars. A pre-booking engine offers stored-unit customers February and March commissioning slots with an incentive, books parts ahead, and shows the service manager projected backlog by week as bookings come in.

## Target Customer
Service managers at marine dealers with storage contracts and at high-volume powersports stores.

## Impact If Built
Moving 15–20% of commissioning into the shoulder months (estimate) adds 80–150 billed hours a technician a year and cuts the peak backlog by a week or more.
