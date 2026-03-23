# CRE-Specific Pipeline Forecasting from Deal Stage Data

**Niche:** [[niches/commercial-real-estate/deal-pipeline-and-commission-tracking/profile|Deal Pipeline & Commission Tracking]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Salesforce and HubSpot provide pipeline forecasting for SaaS and B2B sales, but CRE deal stages (prospecting → listing → marketing → LOI → due diligence → closing) have radically different conversion rates, timelines, and revenue structures that generic sales forecasting models get wrong by 40-60%.
**Tags:** #gradient-boosting #automation #revenue-impact #data-integration

## The Problem
A CRE managing broker needs to forecast quarterly revenue from the firm's active deal pipeline. Investment sales deals take 6-18 months to close with unpredictable timing; leasing deals close in 3-6 months but commission varies by lease term. The managing broker currently estimates revenue by asking each broker for their "expected closings this quarter" — a process that systematically overestimates by 30-50% because brokers are optimistic about deal timing and underestimate fallout rates. Accurate pipeline forecasting is essential for draw management (if pipeline revenue is overestimated, draws exceed actual commissions, creating cash flow crises).

## What Already Exists
Salesforce provides general pipeline forecasting with customizable stages. Buildout and ClientLook track CRE deal stages but provide no forecasting models. Reonomy provides some predictive analytics but focuses on property data, not deal pipeline forecasting.

## The Customization Gap
CRE pipeline forecasting needs: (1) deal-type-specific conversion rates by stage (leasing deals convert at different rates than investment sales at the LOI stage); (2) timeline distributions by asset type and deal size (a $2M retail sale closes faster than a $20M office building); (3) commission estimation that accounts for co-brokerage, overrides, and split tiers (not just gross revenue); (4) draw balance integration (projected net income after draw repayment). The model must learn from the firm's historical deal data, not generic sales benchmarks.

## Target Customer
Managing brokers and CFOs at mid-size CRE firms with 15+ active deals in pipeline at any time — approximately 5,000-8,000 firms nationally.

## Impact If Solved
Pipeline forecast accuracy improves from +/- 40-50% to +/- 15-20%, enabling accurate draw management and preventing quarter-end cash flow surprises. Managing brokers identify stalled deals 30-60 days earlier, enabling intervention before the deal dies.
