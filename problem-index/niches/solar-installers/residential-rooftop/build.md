# Dynamic Savings Projection with Utility Rate Forecasting

**Niche:** [[niches/solar-installers/residential-rooftop/profile|Residential Rooftop Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A savings projection engine that models solar economics using forecasted utility rate changes — including time-of-use rate transitions, net metering policy modifications, demand charge introductions, and rate escalation patterns — replacing the static 3% annual escalation assumption that makes 80% of solar proposals inaccurate by year 5.
**Tags:** #time-series-forecasting #gradient-boosting #revenue-impact #data-integration

## The Problem
Every solar proposal includes a 25-year savings projection: "Your solar system will save you $45,000 over 25 years." This number drives the purchase decision. But the projection is built on assumptions that are almost certainly wrong: a fixed annual utility rate escalation (typically 3-4%), the current net metering policy continuing unchanged, and the current rate structure persisting. In reality, utilities are shifting to time-of-use rates (where solar production value varies by hour), reducing net metering compensation (NEM 3.0 in California reduced export credits by 75%), and introducing demand charges for residential customers. A solar system designed for NEM 2.0 economics in 2024 may produce 30-40% less savings than projected when NEM 3.0 takes effect in 2025. Customers who discover their savings don't match the proposal lose trust in the installer and generate negative reviews — the #1 complaint category for solar companies is "savings didn't meet expectations."

## Why Nobody Has Built This
Utility rate forecasting is genuinely hard. There are 3,000+ electric utilities in the US, each with their own rate structures, regulatory proceedings, and policy timelines. Rate changes are driven by regulatory commissions (PUCs), legislative mandates, utility capital plans, and wholesale market dynamics — not by simple escalation curves. Modeling these requires tracking regulatory filings, rate case outcomes, and legislative actions across all 50 states. The data exists (PUC dockets, tariff databases, EIA data) but is fragmented across hundreds of sources with inconsistent formats. No solar-focused company has built the regulatory intelligence infrastructure needed to produce jurisdiction-specific rate forecasts.

## What to Build
A utility rate intelligence platform that: (1) maintains a continuously updated database of current tariff structures for the top 200 utilities (covering 80%+ of residential solar installations); (2) models rate escalation using historical rate data, pending rate case filings, planned capital investments, and wholesale market trends — producing a probability-weighted rate forecast rather than a single escalation percentage; (3) incorporates known policy changes — NEM transitions, TOU rate introductions, demand charge rollouts — with their effective dates and specific rate impacts; (4) outputs a dynamic 25-year savings projection showing a range (optimistic/expected/pessimistic) rather than a single number; and (5) integrates with Aurora Solar and other design tools via API, replacing the static escalation assumption with the dynamic forecast. The output gives the homeowner a realistic expectation: "Your expected savings are $38K-52K over 25 years, depending on utility rate changes."

## Target Customer
Residential solar installers doing 100+ installations per year who want to differentiate on proposal accuracy and reduce post-installation savings complaints. Solar sales organizations with 5-20 reps who need consistent, defensible financial projections.

## Impact If Built
Reduces "savings didn't meet expectations" complaints by 40-60% through realistic range-based projections. Increases close rates by 10-15% by providing more credible financial analysis than competitors using static assumptions. Protects installer reputation and reduces BBB/Google review complaints — the #1 driver of solar company reputation damage. Could be priced at $200-500/month per installer or $2-5 per proposal.
