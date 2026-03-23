# Geographic Arbitrage Detection Engine

**Niche:** [[niches/auto-dealers-independent/wholesale-auction-flippers/profile|Wholesale & Auction Flippers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool systematically identifies geographic pricing arbitrage — vehicles that are underpriced at one auction market relative to retail demand in another — across the national auction network.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A 4WD truck in Miami might sell at wholesale for $14K but retail for $22K in Denver where demand for 4WD is high. An experienced wholesale buyer knows these geographic spreads from years of buying across regions, but this knowledge is entirely tacit and disappears when the buyer retires or changes employers. New buyers overpay in strong markets and miss opportunities in weak ones because they can't see the national price surface for a given vehicle configuration. The arbitrage window is narrow — other buyers with the same knowledge compete for the same vehicles — making speed of identification critical.

## Why Nobody Has Built This
Building this requires real-time pricing data from multiple auction platforms (Manheim, ADESA, ACV, BacklotCars), retail pricing data by geography (from listing platforms and DMV transaction records), transport cost modeling between any two points, and reconditioning cost estimates. The data is commercially available but expensive, and the customer base (wholesale dealers) has low willingness to pay for SaaS tools compared to their revenue. Additionally, publishing arbitrage opportunities too broadly would eliminate the spreads, creating a strategic tension between tool adoption and opportunity persistence.

## What to Build
A real-time arbitrage scanner that monitors upcoming auction inventory across all major platforms, computes the expected retail price in the buyer's target market (adjusted for local demand, seasonality, and inventory supply), subtracts estimated transport cost, reconditioning, and holding cost, and surfaces the top 20 arbitrage opportunities for the buyer's next auction day. Alerts fire when a vehicle matching high-arbitrage criteria enters an auction run list.

## Target Customer
Wholesale dealers and high-volume buyers purchasing 20+ vehicles per month at auction who want to expand their buying range beyond familiar auction lanes.

## Impact If Built
Identifying 3-5 additional arbitrage opportunities per month at $1,000+ spread per vehicle adds $36K-60K in annual gross profit. Enables geographic expansion — a buyer who operates at 2 auction houses can now identify opportunities at 20+ locations and bid digitally, expanding deal flow without travel.
