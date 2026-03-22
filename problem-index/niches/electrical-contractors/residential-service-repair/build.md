# Flat-Rate Pricing Optimizer

**Niche:** [[niches/electrical-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that analyzes historical job data — close rates, margins, seasonality, geographic pricing tolerance — to optimize flat-rate pricebook entries, replacing the annual gut-feel pricebook update with data-driven pricing that maximizes revenue per call.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #time-series-forecasting #revenue-impact #data-integration

## The Problem
Residential electrical service companies price their work from flat-rate pricebooks — a menu of services with fixed prices (e.g., "Install ceiling fan: $385," "Replace 20A breaker: $275"). These pricebooks are typically set by the owner once a year based on material costs plus a labor markup, adjusted by gut feel for "what the market will bear." The problem is that pricing tolerance varies dramatically by service type, geography, season, and customer segment. A panel upgrade in a high-income suburb can close at $4,200 while the same job in a working-class neighborhood closes only at $2,800 — but most shops use one pricebook for all areas. Seasonal demand spikes (summer A/C circuits, holiday lighting) create pricing power that goes unexploited. The result: shops leave 15-25% of potential margin on the table through uniform pricing while simultaneously losing close-rate on price-sensitive services by overpricing relative to local competition.

## Why Nobody Has Built This
The data needed to optimize pricing — job-level close rates by service type, geography, technician, and season — sits inside ServiceTitan or Housecall Pro but is never analyzed at the pricebook-entry level. ServiceTitan's reporting shows aggregate revenue and average ticket but doesn't connect pricing to close rates. Building the optimization requires joining dispatch data (call type, location, time), job outcome data (closed/lost, final invoice amount, line items), and external factors (competitor pricing, median household income by zip code, material cost trends). Most electrical contractors have 500-2,000 completed jobs per year — enough data for a gradient-boosted model but only after 12-18 months of clean data collection. The behavioral barrier is also real: owners treat their pricebook as proprietary and are reluctant to change prices that "have been working."

## What to Build
A pricing analytics platform that ingests job history from ServiceTitan/Housecall Pro via API, enriches it with geographic and demographic data (Census ACS median income by zip, county permit data for competitor activity), and builds a gradient-boosted model predicting close probability as a function of price, service type, geography, season, technician, and lead source. The optimizer then recommends pricebook adjustments: "Increase ceiling fan install from $385 to $425 in zip codes 90210-90215 (predicted close rate drop: 2%, margin increase: 12%)" or "Decrease panel upgrade from $4,200 to $3,800 in zip codes 30301-30315 (predicted close rate increase: 18%, margin decrease: 8%, net revenue increase: $45K/year)." Updates are pushed quarterly with A/B testing capability — half the techs use the new price, half use the old, measure actual close rates.

## Target Customer
Residential electrical service companies with 5-20 technicians and 1,000+ completed jobs per year in ServiceTitan, generating $2-8M in annual revenue. These shops have enough data for meaningful pricing analysis and enough call volume to measure the impact of price changes within a quarter.

## Impact If Built
Increases average gross margin per job by 8-15% through precision pricing — worth $200K-600K annually for a 10-truck residential electrical shop. Reduces close-rate losses on price-sensitive services by 10-20% through geographic and seasonal adjustments, adding another $100K-200K in recovered revenue.
