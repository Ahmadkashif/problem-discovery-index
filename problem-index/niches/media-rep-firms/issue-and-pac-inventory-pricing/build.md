# A Station-Week Political Demand Forecast

**Niche:** [[niches/media-rep-firms/issue-and-pac-inventory-pricing/profile|Issue & PAC Inventory Pricing]]
**Industry:** [[industries/media-rep-firms|Media Representative Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Political trackers forecast spending by race and market; nobody forecasts it by station and week, which is the level at which a rep sets issue rates and decides what to hold back.
**Tags:** #time-series-forecasting #bayesian-inference #gaussian-processes #feature-engineering #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to price non-candidate issue and PAC spots as close as possible to what the market will clear in the final weeks before an election, while deciding which regular advertisers to displace, and whoever forecasts that demand best books the most political revenue per spot.

## The Problem
In August the desk must decide what to charge issue buyers for October inventory on each station. Price too low and the late money arrives to find the inventory sold at a fraction of what it would have paid. Price too high and the spots go to regular advertisers at regular rates.

## Why Nobody Has Built This
Training data arrives once every two years and differs by race map. Rep firms hold the richest station-level political order history but use it for commissions, not forecasting.

## What to Build
A hierarchical forecast of non-candidate demand per station and week. It is built from the rep's political orders across past cycles and pooled across markets, with race ratings, fundraising, ballot measures and current bookings as covariates, and it updates weekly as bookings arrive. It recommends an issue rate and a hold-back level per station-week, with the displacement cost of each.

## Target Customer
Heads of political sales at rep firms and station group pricing leads.

## Impact If Built
More revenue per political spot in the weeks that decide a station's year. In the 2024 cycle broadcast TV took $5.3B, so small pricing improvements are large in dollars.
