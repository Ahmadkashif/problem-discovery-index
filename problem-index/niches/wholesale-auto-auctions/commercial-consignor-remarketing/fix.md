# The Floor Set From Last Month's MMR

**Niche:** [[niches/wholesale-auto-auctions/commercial-consignor-remarketing/profile|Commercial Consignor Remarketing]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Fix (Pain Point)
**One-liner:** A floor typed as a fixed share of MMR when the car was checked in is still the floor three weeks later, after the market has moved and the car has failed to sell twice.
**Tags:** #time-series-forecasting #linear-regression #automation #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to sell a commercial consignor's off-lease, rental, fleet and repossessed units for the most money after fees and transport, and whoever returns the highest net proceeds as a share of MMR takes the account.

## The Problem
Commercial floors are often set once, at check-in, from MMR and a standing instruction ("95% of MMR, adjusted for grade"). MMR moves weekly. The Manheim index fell 1.1% in September 2026 alone and conversion slipped to 55.2%. A floor that was realistic at check-in becomes a no-sale two runs later, and each rerun adds fees, transport between sites and depreciation.

## Why It's Still Broken
Floors belong to the consignor, and changing one needs the consignor's remarketing desk to approve it. That desk is handling thousands of units and reviews exceptions weekly. The auction can see the floor is stale but has no standing authority to move it.

## What a Fix Looks Like
A standing floor rule expressed as a formula the consignor approves once: MMR at sale time, adjusted for grade and days since check-in, with a stop-loss. The floor recomputes before every run and the reason is shown. Units whose floor sits far above the live bid history are flagged to the consignor before the run, not after the no-sale.

## Who Feels the Pain
Consignor remarketing analysts approving reruns; auction account managers explaining no-sales; and the consignor's finance team, which books the extra depreciation.

## Impact If Fixed
If 10% of commercial units rerun because of stale floors and each rerun costs ~$150–300 (estimate), recomputing floors before each run saves $15–30 a unit across the book. At OPENLANE's 2025 commercial volume of 762,000 units that is $11–23M a year.
