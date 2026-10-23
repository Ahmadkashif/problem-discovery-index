# Automotive Incentive Data Services

**Parent Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
Firms that compile every OEM consumer and dealer incentive programme, by region, model, trim and eligibility rule, into data feeds licensed to desking and DMS vendors, listing marketplaces, OEM and dealer websites and lenders, so that quoted payments reflect the current programmes. J.D. Power's Chrome-branded rebates-and-incentives, VIN-decode and configuration data, which came with its December 2019 merger with Autodata Solutions (Thoma Bravo release), is the best-known source. Incentive spend averaged $3,359 a vehicle in September 2026 (Kelley Blue Book), so a wrong or late programme load misprices quotes market-wide.

## Insight Function
**Size:** The analysts who read each OEM bulletin and load its rules are production, one programme at a time; methodology and data-product staff are under ~10 per vendor (estimate)
**Output:** Licensed programme and incentive data feeds and APIs
**Proprietary data:** A structured archive of programme rules and amounts by region and VIN pattern, compiled from OEM bulletins distributed to dealers
**Clock:** OEM programme effective dates, which change monthly and mid-month, set by a third party
**Buyer:** VP Data Products / Head of Automotive Data Licensing

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | — |
| Q2 Labor mass + repeatable | ×2 | — |
| Q3 Proprietary data moat | ×3 | — |
| Q4 External clock | ×2 | — |
| Q5 Buyer + market | ×2 | — |
| **Weighted total** | | **—/60** |

**Kill switches:** none — the bulletins are distributed to every dealer of the brand and the structured feed is the firm's own product
**Verdict:** Logged — fails gate (bulletin loaders are production, and the methodology team is under 10). The feed is the product and the OEM sets the clock, but the inputs are bulletins every dealer receives. The dealer-side use of the same rules is the Pass 1 niche [[niches/franchised-car-dealers/oem-incentive-reconciliation/profile|OEM Incentive & Stair-Step Reconciliation]].
