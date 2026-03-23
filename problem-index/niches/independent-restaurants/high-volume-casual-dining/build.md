# Real-Time Food Cost Dashboard with Automatic Invoice-to-Recipe Mapping

**Niche:** [[niches/independent-restaurants/high-volume-casual-dining/profile|High-Volume Casual Dining Independents]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product today connects invoice OCR, POS sales mix, and recipe decomposition into a live per-dish margin dashboard without requiring ongoing manual recipe maintenance.
**Tags:** #ocr #gradient-boosting #regression #tabular-ml #data-integration #revenue-impact

## The Problem
High-volume casual restaurants buy $15K-$60K/month in ingredients but cannot tell you the actual contribution margin of any single dish. Invoices arrive as PDFs or paper from 3-5 distributors, recipes exist in the chef's head or a binder that was last updated two years ago, and POS sales mix data sits in a separate system. The result: owners discover they are underwater on a dish only when they notice they are losing money overall — months after the problem started.

## Why Nobody Has Built This
The technical challenge is the automatic mapping layer: recognizing that a Sysco invoice line for "CHKN BRST BLS 6OZ CS/40" corresponds to the chicken breast ingredient in 7 different recipes at varying quantities. This requires a product-catalog normalization engine specific to foodservice distributors, combined with anomaly detection that flags when purchasing patterns diverge from expected recipe usage (indicating waste, theft, or recipe drift). Existing tools require the operator to build and maintain this mapping manually, which is why adoption collapses.

## What to Build
An invoice ingestion system (photo capture or distributor API) that auto-maps line items to a normalized ingredient database, connects to POS sales data via Toast/Square API, and maintains recipe decompositions through a combination of one-time entry and ongoing anomaly detection. The output is a per-dish margin dashboard updated after every invoice, with alerts when a dish's food cost crosses a threshold.

## Target Customer
Owner-operators or GMs of independent restaurants doing $1M-$5M revenue with 20+ menu items and 3+ distributors, who currently have no per-dish cost visibility.

## Impact If Built
A 2-3 point food cost reduction on $2M revenue translates to $40K-$60K in recovered annual profit — often the difference between a viable business and one that closes within 18 months.
