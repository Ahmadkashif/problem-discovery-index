# Rate Setting & Yield Pricing

**Parent Industry:** [[industries/parking-operators|Parking Operators]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to price every hour and every event at the rate that fills the facility without turning cars away, and whoever earns the highest revenue per available space against comparable nearby facilities takes the account.

## Profile
**Market Size:** ~$300M a year in pricing staff time, revenue-management software and rate-distribution tools across operators (estimate)
**Share of Parent Industry:** ~3% of operator receipts (estimate), steering a far larger share of gross collections
**Digital Adoption:** Medium — rates are published digitally to PARCS, apps and marketplaces, but chosen by hand
**Target Buyer:** Operator VP of revenue or pricing; area managers; owners' asset managers who approve rates
**Automation Potential:** High — forecasting, rate rules and multi-channel publication are mechanical once data is clean

## What Makes This a Distinct Niche
This is the daily mechanism behind the industry's high-impact problem: transient steps, daily maximums, early-bird and evening rates, event pricing and marketplace rates, set per facility. Cities show it can be run by rule. SFMTA moves each block's meter rate $0.25 about every quarter, raising it above 80% occupancy and lowering it below 60% (latest change 2026-07-13), and Seattle targets 70–85% (search summary). Owners now report revenue per available stall. The analogues elsewhere in the vault are hotel revenue management at [[niches/hotels-boutique/rms-vendor-data-science/profile|Revenue Management System Data Science]] and apartment pricing at [[niches/property-management/revenue-management-rent-pricing/profile|Revenue Management & Rent Pricing Systems]]. Parking differs in three ways: hourly inventory, a monthly base underneath it, and contract limits on rate changes.

## Current Tools & Gaps
PARCS rate tables, marketplace operator portals (SpotHero, ParkWhiz, ParkMobile), event-pricing spreadsheets and, at Metropolis, pricing inside its own platform. SpotHero was hiring a Senior Data Engineer I in Chicago (first posted 2026-09-18). Gaps: no hourly forecast per facility at most operators; rates not checked against comparable facilities; elasticity unknown; channel prices out of step.

## Problems
- [[niches/parking-operators/rate-setting-yield-pricing/build|🔨 Build: An Hourly Occupancy Forecast and Rate Recommender]]
- [[niches/parking-operators/rate-setting-yield-pricing/buy|🛒 Buy: Hotel Revenue Management Adapted to Garages]]
- [[niches/parking-operators/rate-setting-yield-pricing/fix|🔧 Fix: Three Channels, Three Prices]]
