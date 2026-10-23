# Storm Stock Sized From Weather and Outage History

**Niche:** [[niches/electrical-distributors/utility-grid-supply/profile|Utility & Grid Supply]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Storm stock is sized by memory of the last bad season, and the alliance is lost or kept in the week the stock runs out.
**Tags:** #time-series-forecasting #gradient-boosting #monte-carlo-methods #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep a utility's or co-op's transformers, cable, meters and line hardware on the shelf under an alliance agreement through storms and multi-year lead times, and whoever posts the highest fill rate when the storm hits takes the account.

## The Problem
A distributor serving coastal or ice-belt utilities holds storm inventory — transformers, cutouts, arresters, conductor, connectors — that sits for months and then empties in days. How much to hold, where, and of which ratings is decided by experienced utility salespeople and the utility's materials manager, with no model of what a storm of a given size consumes.

## Why Nobody Has Built This
Storm consumption data is split between the utility (outage and restoration records) and the distributor (sales during events), and nobody joins them. Events are rare, so each distributor sees few examples.

## What to Build
A model that joins historical storm tracks, wind and ice severity, outage counts and restoration material consumption by item, then simulates consumption for each utility territory under seasonal storm scenarios. It recommends stock levels by item and location against the alliance's fill-rate terms and the lead time to replenish, and updates as forecasts firm up before landfall.

## Target Customer
Utility sales leaders at distributors with alliance agreements in storm-exposed regions; utility materials managers as co-owners.

## Impact If Built
If storm-week fill rates rise from ~80% to ~95% (estimate) while quiet-year dead stock falls ~10–20% (estimate), the distributor protects alliance renewals worth tens of millions of dollars a year (estimate) in the week that decides them.
