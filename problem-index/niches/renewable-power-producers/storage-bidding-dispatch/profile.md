# Battery Storage Bidding & Dispatch

**Parent Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to capture the most of a battery's theoretical market revenue, and whoever has the highest capture rate against a perfect-foresight benchmark takes the account.

## Profile
**Market Size:** ~$300M a year of optimisation fees and trading-desk cost on ~$3B of merchant storage revenue (estimate)
**Share of Parent Industry:** ~1% of wind and solar energy revenue (estimate)
**Digital Adoption:** High — bids, telemetry and settlement are electronic; strategy changes still run through a few traders
**Target Buyer:** Head of Storage Trading or Commercial Optimisation at an IPP
**Automation Potential:** Very high — bidding is algorithmic every interval, with humans setting risk limits

## What Makes This a Distinct Niche
Batteries are the fastest-growing part of the fleet: a record 15 GW was added in 2025 and 24 GW was planned for 2026 (EIA). A battery earns only what it is bid to earn across day-ahead energy, real-time energy and ancillary services, within state-of-charge, cycle and warranty limits. Revenue is shrinking where batteries crowd in: Modo Energy's ERCOT index put 2025 earnings to the end of November at ~$26/kW against $54.1/kW a year earlier, as ancillary markets saturated (search summary). The contest is a single number, capture rate against perfect foresight, which optimisers publish and owners compare. Competitors are Tesla's Autobidder, Fluence's Mosaic, Ascend Analytics' SmartBidder, Habitat Energy, GridBeyond, Gridmatic and owners' in-house desks (named from recall); Tyba sells storage revenue modelling and operations software. The optimiser layer as an insight pocket is logged in Pass 2.

## Current Tools & Gaps
Optimiser platforms on revenue-share or fixed-fee terms, price forecasting services, battery management systems and ISO market interfaces. Gaps: degradation cost is rarely priced into each bid, capture-rate claims use different benchmarks, and owners cannot audit a black-box optimiser against an independent counterfactual.

## Problems
- [[niches/renewable-power-producers/storage-bidding-dispatch/build|🔨 Build: Bids That Price Every Cycle's Wear]]
- [[niches/renewable-power-producers/storage-bidding-dispatch/buy|🛒 Buy: Hydro Reservoir Scheduling for Batteries]]
- [[niches/renewable-power-producers/storage-bidding-dispatch/fix|🔧 Fix: Optimiser Claims Nobody Can Audit]]
