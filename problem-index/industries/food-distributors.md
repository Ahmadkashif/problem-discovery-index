# Food Distributors

## Profile
**Category:** Agriculture & Food
**Market Size:** ~$350B annually in US foodservice and retail food distribution
**Tech Maturity:** Medium — WMS platforms (Manhattan Associates, Blue Yonder) and route optimization (Roadnet, Descartes) are widespread, but AI-driven demand forecasting and dynamic pricing remain rare outside the top 10 national distributors
**Workforce:** Warehouse selectors/pickers, delivery drivers (CDL-B typically), buyers/merchandisers, sales reps, warehouse managers, quality assurance staff

## Key Pain Themes
Perishable inventory management is the central challenge: distributors carry 2,000-10,000 SKUs with shelf lives ranging from 3 days (fresh-cut produce) to 14 days (dairy), and spoilage waste runs 2-5% of revenue — $7M-$17M annually for a mid-size distributor doing $350M. Demand forecasting is complicated by weather, seasonal menus, promotional calendars, and substitution patterns that vary by customer segment (restaurants vs. schools vs. hospitals). Route planning must account for multi-temperature compartments (frozen at -10F, chill at 34F, dry ambient), strict delivery windows (restaurants need product before 6 AM service prep), and product-specific handling (no stacking soft fruit, FIFO rotation at the dock). Supplier invoice reconciliation is uniquely complex because catch-weight pricing (per-pound charges on variable-weight cases), grade adjustments, short-ship credits, and promotional allowances create thousands of line-item discrepancies per week that AP teams resolve manually.

## Current Tech Landscape
Most mid-size distributors run an ERP (often SAP Business One, NetSuite, or industry-specific platforms like Produce Pro or Edible Software) paired with a standalone WMS. Route optimization is handled by Roadnet/Omnitracs or Descartes, but these tools treat all cargo as identical and lack multi-temperature compartment logic. Demand forecasting, where it exists, is spreadsheet-based or uses simple moving averages inside the ERP — no ML, no external signal ingestion (weather, event calendars), no substitution modeling.

## Problems
- [[problems/food-distributors/high-impact|🔴 High Impact: Perishable Demand Forecasting and Inventory Optimization]]
- [[problems/food-distributors/low-impact-1|🟡 Low Impact: Route Optimization for Multi-Temperature Delivery]]
- [[problems/food-distributors/low-impact-2|🟡 Low Impact: Supplier Invoice Reconciliation Against PO and Receiving]]
- [[problems/food-distributors/worker-life-1|🟢 Worker Life: Warehouse Selector Productivity Pressure in Cold Environments]]
- [[problems/food-distributors/worker-life-2|🟢 Worker Life: Delivery Driver Customer Dispute Resolution]]
- [[problems/food-distributors/ml-opportunity|🔵 ML Opportunities]]
- [[problems/food-distributors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Food distribution sits at the intersection of thin margins (1-3% net) and high perishability, making inventory accuracy existential rather than incremental. The industry's fragmented middle market — roughly 3,000 distributors between $50M and $500M revenue — is underserved by enterprise AI vendors who target Sysco/US Foods scale. This creates a clear opening for vertical AI products that integrate with existing ERP/WMS stacks and deliver ROI through spoilage reduction (the single largest controllable cost) and route efficiency (fuel and labor are 60% of delivery cost).
