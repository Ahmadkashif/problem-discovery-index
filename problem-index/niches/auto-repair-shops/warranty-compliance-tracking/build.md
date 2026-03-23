# Automatic Parts Warranty Tracker with Claim Filing

**Niche:** [[niches/auto-repair-shops/warranty-compliance-tracking/profile|Warranty & Recall Compliance Tracking]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system tracks aftermarket parts warranty periods and automatically initiates claims with suppliers when a warrantied part fails — shops eat $5,000-$15,000/year in unclaimed parts warranties.
**Tags:** #automation #data-integration #workflow-orchestration #revenue-impact

## The Problem
When a shop installs aftermarket brake pads, a water pump, or an alternator, the part carries a manufacturer warranty (typically 12-36 months or a mileage limit). If the part fails within warranty, the shop should get a free replacement from the supplier — but this requires knowing the original install date, the warranty terms for that specific brand/part, and filing a claim through the supplier's process. Most shops don't track any of this. The technician installs the part, the warranty sticker goes in a drawer, and 14 months later when the part fails, nobody remembers it's still under warranty. The shop buys another part at full price.

## Why Nobody Has Built This
Parts warranty terms vary by manufacturer, product line, and even individual SKU — there's no standardized warranty database. Claim filing processes differ across hundreds of parts suppliers (some require photos, some require the old part returned, some have online portals, some require phone calls). Building a comprehensive system requires aggregating warranty terms across thousands of SKUs and integrating with dozens of supplier claim workflows.

## What to Build
A warranty tracking layer that automatically logs every part installed (from the repair order), records the warranty period (from a maintained database of parts warranties by manufacturer/SKU), monitors vehicle mileage and calendar time, and alerts the service advisor when a vehicle returns with a symptom matching a still-warrantied component. When a warranty claim is confirmed, the system pre-fills the supplier's claim form with the required information (original invoice, part number, install date, failure description).

## Target Customer
Shop owners installing 50+ aftermarket parts per week who currently have no systematic warranty tracking and estimate they miss 30-50% of valid warranty claims.

## Impact If Built
Recovers $5,000-$15,000 per year per shop in previously unclaimed parts warranties. For a 5-technician shop installing 200+ parts per month, even a 50% warranty claim capture rate represents $8,000-$12,000 in annual savings.
