# Integration Fit & Compatibility

**Parent Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Category:** 🔵 High Market Share
**Contested on:** Every serious competitor in this niche is fighting to answer, before purchase, whether an asset will work in the buyer's engine version, render pipeline and performance budget — and whoever answers it takes the account.

## Profile
**Market Size:** ~$400M US
**Share of Parent Industry:** ~27% of category revenue
**Digital Adoption:** Very low — screenshots
**Target Buyer:** Marketplace product leadership
**Automation Potential:** Very high — static analysis of the files

## What Makes This a Distinct Niche
The listing shows a rendered screenshot and a price. The cost that decides whether the purchase was worthwhile is the integration work, and nothing in the marketplace describes it. An asset that does not match the buyer's engine version, render pipeline, physics setup or platform target costs hours or is discarded. Every fact needed to answer this is computable from the files the marketplace already stores, and the category answers it by letting the buyer find out.

## Current Tools & Gaps
A thumbnail, a description, a supported-versions field the creator typed, and a refund policy. The gaps: no computed polygon and texture budgets; no render pipeline dependency detection; no engine version compatibility testing; no platform feasibility assessment; and no integration effort estimate.

## Problems
- [[niches/game-asset-marketplaces/integration-fit/build|🔨 Build: Reading the Asset Instead of the Listing]]
- [[niches/game-asset-marketplaces/integration-fit/buy|🛒 Buy: Dependency Compatibility From Package Registries]]
- [[niches/game-asset-marketplaces/integration-fit/fix|🔧 Fix: The Asset That Does Not Compile in This Pipeline]]
