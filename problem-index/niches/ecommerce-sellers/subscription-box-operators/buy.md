# Subscription-Aware Inventory and Box Curation Planning

**Niche:** [[niches/ecommerce-sellers/subscription-box-operators/profile|Subscription Box Operators]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Inventory planning tools exist for standard e-commerce, but none handle the subscription box model where demand is partially known (active subscribers) but product selection changes every month.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #workflow-orchestration #revenue-impact

## The Problem
Each month, a subscription box operator must curate which products go into the box, procure the right quantities, and manage variants (size, flavor, dietary preference). The demand signal is partially deterministic (active subscriber count) but uncertain (new sign-ups, cancellations before ship date, skip requests, gift conversions). Ordering too much product wastes margin on unsold inventory; ordering too little means some subscribers don't get the promised items. This planning cycle repeats monthly with different products each time — a cadence that standard inventory tools don't support.

## What Already Exists
SoStocked and RestockPro handle Amazon inventory replenishment for consistent SKUs. Shopify's inventory management assumes a stable catalog. Cratejoy offers basic subscriber counts but no procurement planning. Operators use spreadsheets that multiply active subscriber count by a safety buffer and hope for the best.

## The Customization Gap
The missing layer is a monthly curation planning tool that connects subscriber forecast (predicted active count on ship date, accounting for churn, new sign-ups, skips, and gift expirations) to product procurement (MOQs per supplier, lead times, variant distributions from subscriber preference surveys). It must handle the unique planning constraint that next month's products are different from this month's — there's no steady-state reorder model, just a recurring planning cycle with different inputs each time.

## Target Customer
Subscription box operators curating 3-8 products per box for 500+ subscribers who currently plan procurement in spreadsheets with manual subscriber count estimates.

## Impact If Solved
Reduces overstock waste by 15-25% per box cycle (typically $2-5 per box in wasted product across 2,000+ boxes = $4K-10K/month). Eliminates subscriber fulfillment shortfalls that currently trigger 2-5% of subscribers to cancel due to missing or substituted items.
