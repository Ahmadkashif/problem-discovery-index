# Hydro Reservoir Scheduling for Batteries

**Niche:** [[niches/renewable-power-producers/storage-bidding-dispatch/profile|Battery Storage Bidding & Dispatch]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hydro operators have scheduled reservoirs for decades by valuing stored water against future prices; a battery is a small, fast reservoir with a wear cost.
**Tags:** #dynamic-programming #monte-carlo-methods #optimization-fundamentals #time-series-forecasting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to capture the most of a battery's theoretical market revenue, and whoever has the highest capture rate against a perfect-foresight benchmark takes the account.

## The Problem
Battery bidding needs a value for stored energy over the next hours and days, and many optimisers solve one day at a time.

## What Already Exists
Hydro scheduling tools compute a "water value" for each reservoir level by stochastic dynamic programming over inflow and price scenarios, then set generation offers against it; production-cost models used by utilities and traders include storage modules.

## The Customization Gap
The adaptation needs: five-minute and fifteen-minute intervals instead of hourly or daily steps; ancillary service co-optimisation under each ISO's rules (including ERCOT's real-time co-optimisation); state-of-charge limits per ancillary product; degradation cost per cycle in place of spill; and bids generated automatically in each market's format.

## Target Customer
IPPs bringing storage trading in-house rather than paying a revenue share.

## Impact If Solved
Adapting a proven scheduling method could replace a ~10–15% revenue share (estimate) on a 200 MW portfolio earning ~$8M a year with an in-house tool, keeping ~$1M a year.
