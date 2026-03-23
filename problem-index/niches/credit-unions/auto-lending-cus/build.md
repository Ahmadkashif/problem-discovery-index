# Local Used Vehicle Market Pricing Intelligence

**Niche:** [[niches/credit-unions/auto-lending-cus/profile|Auto Lending CUs]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** National vehicle valuation guides (Black Book, JD Power) give a single wholesale value for a 2021 Toyota Camry — but the actual resale value in Boise versus Miami varies by $2,000-$4,000, and CUs setting LTV limits from national values are either over-lending or missing good deals.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
CUs use national vehicle valuation guides to set maximum loan amounts (typically 100-120% of book value). But used vehicle prices vary significantly by local market — a 4WD truck commands a premium in Montana that it doesn't carry in Florida, and a convertible depreciates faster in Minnesota than in California. A CU using national book values in a market where actual resale values are 10-15% higher is unnecessarily limiting loan amounts and losing deals to competitors who lend more aggressively. Conversely, a CU using national values where local prices are depressed is over-lending and absorbing collateral shortfall risk on repossessions.

## Why Nobody Has Built This
Vehicle valuation companies (Black Book, JD Power, Kelley Blue Book) provide national and regional values but don't offer hyper-local pricing calibrated to a specific CU's geographic footprint. Building local market models requires scraping or licensing dealer listing data, auction results, and transaction prices at the zip-code level — data that is available but fragmented across multiple sources and not aggregated for CU lending use cases. CU technology vendors focus on LOS and core banking integration, not collateral valuation intelligence.

## What to Build
A used vehicle pricing model that combines national valuation baselines with local market adjustment factors derived from: dealer listing prices within the CU's service area, recent auction results at regional auctions (Manheim, ADESA), CU's own repossession recovery history, and seasonal/economic adjustments. The model outputs a local market value (not just book value) for each vehicle at loan decision time, with a confidence interval. Integration with the CU's LOS automatically adjusts maximum LTV based on local market value rather than national book value.

## Target Customer
VP of Lending and auto lending managers at CUs with $100M+ in auto loan portfolios who make 500+ auto lending decisions per month and want collateral valuation that reflects their actual market, not a national average.

## Impact If Built
Reduces collateral shortfall on repossessions by 15-25% through accurate local valuation. Increases competitive loan approvals by 5-10% in markets where actual values exceed national book values. Provides a data-driven justification for LTV decisions during NCUA examination.
