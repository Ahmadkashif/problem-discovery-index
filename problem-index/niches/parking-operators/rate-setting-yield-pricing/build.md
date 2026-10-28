# An Hourly Occupancy Forecast and Rate Recommender

**Niche:** [[niches/parking-operators/rate-setting-yield-pricing/profile|Rate Setting & Yield Pricing]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most facilities have no forecast of when they will fill and no measured price response, so every rate is a guess checked by driving past.
**Tags:** #time-series-forecasting #temporal-fusion-transformers #gradient-boosting #causal-inference #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price every hour and every event at the rate that fills the facility without turning cars away, and whoever earns the highest revenue per available space against comparable nearby facilities takes the account.

## The Problem
An operator's facilities fill at different hours for different reasons, and the rate board changes a few times a year. Event rates are set the week before by feel. Nobody knows how many drivers a $5 increase loses.

## Why Nobody Has Built This
Operator data is fragmented across PARCS vendors and channels, owners must consent to its use at managed sites, and price experiments need owner approval. Small operators lack the data to train on.

## What to Build
This is the two-week MVP, built on public data first. Ingest Seattle's per-minute paid-occupancy feed (13.4 million rows for the last 30 days on 2026-10-28) and its transaction feed, then train hourly forecasts per blockface (LightGBM baseline, temporal fusion transformer). Estimate price response from SFMTA's scheduled block-level rate changes with difference-in-differences. Wrap both in the city's own band rules to recommend each block's next rate. A small open-source plate-reader demo on consented images shows how gate events become sessions, so the same pipeline runs on a garage's entry and exit data. Version two swaps meters for one operator's PARCS history, adds events and competitor rates from marketplace listings, and enforces contract rate caps.

## Target Customer
Regional operators without pricing teams; owners who approve rates; marketplaces that want better rates from their operators.

## Impact If Built
A 3–5% RevPAS lift (estimate) on a 1,000-space garage earning $3M a year is ~$90–150K a year, most of it the owner's. That lift is what the operator's renewal depends on.
