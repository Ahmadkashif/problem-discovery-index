# Custom Study Production Adapted to a Standing Panel

**Niche:** [[niches/acupuncture-practices/natural-products-market-data/profile|Natural Products Channel Data Vendors]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** BI and analytics notebooks assume the data model changes and the questions repeat; custom insight studies are the reverse — the panel is stable and every question is new — and no product is built for that shape.
**Tags:** #feature-engineering #descriptive-statistics #time-series-forecasting #k-means-clustering #dimensionality-reduction #evaluation-metrics #automation #workflow-orchestration #data-integration

## The Problem
Alongside syndicated reports, these vendors sell custom studies: a manufacturer wants to know how a botanical category is performing in a specific channel among a specific shopper cohort over a defined window. An analyst pulls from the panel, builds the cuts, checks them against known benchmarks, and assembles a deck. The work is genuinely analytical, but a large share of every study is reconstruction — re-deriving the same category rollups, the same seasonality adjustments, the same store-level projection weights that a colleague derived last month for a different client. Studies live as finished decks and one-off notebooks. Nothing accumulates, so the tenth study on a category costs roughly what the first one did, and delivery time is what gets squeezed when the client's category review date is fixed.

## What Already Exists
The analytics tooling market is saturated and capable. Databricks and Snowflake handle the panel at scale; dbt gives versioned, tested transformation logic; Hex, Deepnote, and Observable provide collaborative notebooks with parameterization and scheduled runs; Looker and Power BI cover semantic layers and self-service reporting. Every individual capability the workflow needs exists in a mature product.

## The Customization Gap
The mismatch is in what these tools assume is stable. BI semantic layers are built for recurring questions over an evolving model — define the metric once, answer it forever. Custom insight work inverts that: the panel and its projection methodology are the stable part, while every engagement asks something structurally new. So the semantic layer captures the trivial half and none of the expensive half, and analysts drop into raw notebooks the moment a question deviates, which is always. The adaptation needed is a study-shaped abstraction sitting above the panel: a library of parameterized analytical patterns — category share over a window, cohort penetration, distribution-driven versus rate-driven decomposition, seasonality-adjusted trend — each carrying its own validation rules and each recording where it has been used and what it produced. A new study is composed from patterns rather than written from the raw feed, and any genuinely novel analysis an analyst builds becomes a candidate pattern for the library. Panel-specific projection and weighting logic lives in the patterns rather than being re-implemented per study.

## Target Customer
Directors of custom insights and analytics managers running study delivery teams, and the senior analysts who currently absorb the reconstruction cost on every engagement.

## Impact If Solved
Study delivery time compresses toward the analytical part of the work, which is what the client is actually paying for and the only part that differentiates the vendor. Margin on custom work improves as the library deepens, changing the economics of a line of business that is usually run at thin margin to protect the syndicated relationship. And methodological consistency stops depending on which analyst was assigned — the pattern library is the house method, made executable.
