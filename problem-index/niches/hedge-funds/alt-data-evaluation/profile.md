# Alternative Data Evaluation & Onboarding

**Parent Industry:** [[industries/hedge-funds|Hedge Funds]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to prove or disprove, inside the trial window and on the fund's own universe, whether a dataset carries information not already in consensus — and whoever produces a defensible verdict before the trial expires decides which data gets bought.

## Profile
**Market Size:** ~$600M global spend on alternative-data evaluation, onboarding and data engineering at hedge funds (estimate), governing an estimated ~$2.8B of annual dataset spend by investment managers (Neudata, 2025)
**Share of Parent Industry:** ~5% of hedge fund research and data spend (estimate)
**Digital Adoption:** High tooling, low standardisation
**Target Buyer:** Head of Data Strategy, Head of Data Science
**Automation Potential:** Very High — evaluation steps are the same for every dataset

## What Makes This a Distinct Niche
The number of alternative datasets on offer runs into the thousands, and a fund's ability to evaluate them — not its budget — limits what it uses. Each evaluation repeats the same steps: entity mapping, point-in-time reconstruction, KPI and return testing, provenance review. The broker and marketplace side of this exchange is analysed in [[industries/data-marketplace-brokers|Data Marketplace Brokers]] (including its [[niches/data-marketplace-brokers/pre-purchase-evaluation/profile|Pre-Purchase Evaluation]] niche); this niche is the buyer side.

## Current Tools & Gaps
Data platforms (Snowflake, Databricks), data delivery services (Crux), discovery services (Neudata), vendor-supplied backtests, and in-house code. Gaps: entity maps rebuilt per dataset; vintages missing; evaluation not standardised across trials; verdicts informal.

## Problems
- [[niches/hedge-funds/alt-data-evaluation/build|🔨 Build: A Standard Trial Harness With a Written Verdict]]
- [[niches/hedge-funds/alt-data-evaluation/buy|🛒 Buy: Entity Resolution Tuned for Merchants and Tickers]]
- [[niches/hedge-funds/alt-data-evaluation/fix|🔧 Fix: The Backtest Run on Revised History]]
