# Daily Rates From a Vacancy Forecast, Not Last Month's Survey

**Niche:** [[niches/self-storage-operators/street-rate-pricing/profile|Street-Rate Pricing & Move-In Promotions]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Outside the REITs, web rates move when someone notices a competitor changed theirs, not when the store's own 10x10s are about to run out or sit empty.
**Tags:** #time-series-forecasting #bayesian-inference #exponential-smoothing #large-language-models #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each vacant unit type's web rate and promotion every day against nearby competitors, and whoever earns the most rental revenue per available square foot takes the account.

## The Problem
A regional operator's revenue manager adjusts rates for 80 stores from a weekly competitor survey and an occupancy report. A unit type at 97% occupancy keeps its promotion for another week. One at 70% gets cut to match a competitor whose "first month free" was misread as a lower rate. Each mistake shows up in move-ins within days, but the cause is never traced.

## Why Nobody Has Built This
Vendors sell rate recommendations driven by occupancy thresholds and competitor rates. Forecasting vacancy by unit type at each store needs move-in, move-out and reservation history joined across stores, and small unit types have too few events to forecast alone.

## What to Build
A forecast-led pricing engine. A hierarchical forecast of move-ins and move-outs by unit type and store pools small unit types toward the store and region. It uses seasonality, reservations, web traffic and expected move-outs from scheduled increases. Competitor rates are normalised daily from public rate pages, with a language model parsing promotions into effective rent over a typical stay. A pricing rule then sets each unit type's web rate and promotion to hit a target vacancy path, with guardrails for floor rates and promotion budgets. Every change logs its reason.

## Target Customer
Revenue managers at regional operators and third-party managers with 20–500 stores.

## Impact If Built
If forecast-led pricing lifts revenue per available square foot by ~1–2% (estimate), a 100-store portfolio collecting ~$70M a year earns ~$0.7–1.4M more. Revenue managers stop spending Mondays on the survey.
