# Bids That Price Every Cycle's Wear

**Niche:** [[niches/renewable-power-producers/storage-bidding-dispatch/profile|Battery Storage Bidding & Dispatch]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Optimisers chase each interval's spread and treat battery wear as a fixed cycle cap, so a battery can earn this year's revenue by spending next decade's capacity.
**Tags:** #markov-decision-processes #dynamic-programming #model-based-rl #time-series-forecasting #optimization-fundamentals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to capture the most of a battery's theoretical market revenue, and whoever has the highest capture rate against a perfect-foresight benchmark takes the account.

## The Problem
Warranty terms cap cycles or throughput, and degradation depends on depth of discharge, temperature and rate. Bidding against a simple cap either leaves money on the table on high-spread days or burns cycles on thin ones.

## Why Nobody Has Built This
Degradation models come from cell makers and integrators and are rarely shared; revenue-share contracts reward the optimiser for revenue, not for asset life; and the benchmark everyone quotes ignores wear.

## What to Build
A stochastic bidder that values each cycle by its marginal degradation cost from a cell-level model fitted to the asset's own capacity tests, plans across day-ahead, real-time and ancillary markets with price scenarios, and reports capture rate both gross and net of degradation.

## Target Customer
Storage trading heads at IPPs with 500 MWh or more of merchant storage, and integrators offering long-term service agreements.

## Impact If Built
On a 250 MW / 1,000 MWh portfolio earning ~$40/kW-year (~$10M), lifting net capture rate from ~70% to ~78% (estimate) adds ~$1.1M a year while keeping cycle use within warranty.
