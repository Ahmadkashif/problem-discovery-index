# Core-System Cash Ordering Adapted to Stop Consolidation

**Niche:** [[niches/armored-car-services/thin-route-rural-institutions/profile|Rural Banks & Credit Unions on Thin Routes]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Small banks' core systems already track teller and vault cash; they do not plan orders to minimise the number of truck stops a thin route can afford.
**Tags:** #time-series-forecasting #exponential-smoothing #optimization-fundamentals #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep serving rural branches profitably as stops thin out, and whoever packs the most bank, retail and ATM stops onto one rural route takes the account.

## The Problem
A small bank with six rural branches orders cash for each one separately, sometimes on different days, so the carrier makes more stops than needed. When the carrier cuts frequency, branches overstock to compensate.

## What Already Exists
Teller and vault cash modules in community bank cores from Fiserv and Jack Henry track drawer and vault balances, and some offer order suggestions.

## The Customization Gap
The adaptation is to plan for the route rather than the branch: forecast each branch's needs by denomination over a longer horizon, consolidate orders to the carrier's actual service days, move cash between nearby branches where it is cheaper than a stop, account for the Fed's recirculation fee on fit notes, and respect the bank's insurance limits for cash held in each branch. The output is a weekly order plan the carrier can serve in the fewest stops.

## Target Customer
Branch operations officers at [[industries/community-banks|community banks]] and [[industries/credit-unions|credit unions]] with rural branches.

## Impact If Solved
Fewer, larger and predictable stops make a rural account cheaper for the carrier to keep and give the bank a credible basis to negotiate frequency rather than accept a price rise.
