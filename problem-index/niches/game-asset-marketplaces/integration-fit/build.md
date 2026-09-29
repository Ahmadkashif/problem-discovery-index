# Reading the Asset Instead of the Listing

**Niche:** [[niches/game-asset-marketplaces/integration-fit/profile|Integration Fit & Compatibility]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Everything the buyer needs to know is in the file and the marketplace reads only the title.
**Tags:** #data-integration #automation #evaluation-metrics #graph-theory #descriptive-statistics #confidence-intervals #feature-engineering #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to answer, before purchase, whether an asset will work in the buyer's engine version, render pipeline and performance budget — and whoever answers it takes the account.

## The Problem
A buyer wants to know whether an asset will work in their project: the engine version they are on, the render pipeline they use, the platform they ship to, the performance budget they have. The marketplace shows a screenshot. The answers are all present in the uploaded files — polygon counts, texture resolutions and formats, shader and pipeline dependencies, referenced plugins, script API usage — and none of them are extracted. The buyer pays, downloads, imports, and discovers.

## Why Nobody Has Built This
Marketplaces were built as storefronts and storefronts read metadata, not payloads. Parsing many asset formats across several engines is real work with no obvious revenue attached. Creators supply compatibility claims for free, which is good enough to ship. And refunds absorb the failures cheaply enough that nobody has costed the abandonment.

## What to Build
Extract the facts from the files and put them on the listing. Parse every uploaded asset for its technical profile — geometry and texture budgets, material and shader dependencies, plugin and API references, platform-incompatible features — which is the core and is a one-time engineering investment against every listing in the catalogue. Test import against the major engine versions automatically rather than trusting a declared field, since the declaration is the least reliable data on the page. Detect render pipeline dependency specifically, as that is the commonest and most expensive mismatch. Estimate integration effort with a stated basis, because the buyer's real question is cost rather than compatibility. Assess platform feasibility against mobile, console and desktop budgets, which the buyer currently computes by hand if at all. Flag assets that will break on engine upgrade, which is the recurring failure that erodes trust in the whole category. Let the buyer filter by their own project profile rather than by keyword, which is the product this analysis makes possible. Show the technical profile alongside the screenshot rather than behind a tab. Re-run the analysis when a new engine version ships, so compatibility is current rather than historical. And give creators the same report so they can fix problems before buyers find them.

## Target Customer
Asset marketplaces and storefronts, game studios buying at volume, engine vendors, and asset pipeline tooling providers.

## Impact If Built
Every fact the buyer needs is in the file, and the storefront reads only the metadata. Extracting the technical profile and testing import against real engine versions replaces a declared field with an answer.
