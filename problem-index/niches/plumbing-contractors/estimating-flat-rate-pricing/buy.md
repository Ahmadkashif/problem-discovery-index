# ServiceTitan Pricebook Auto-Updater with Material Cost Feeds

**Niche:** [[niches/plumbing-contractors/estimating-flat-rate-pricing/profile|Estimating & Flat-Rate Pricing]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ServiceTitan's pricebook module stores flat-rate task pricing but has no connection to actual material costs — a plugin that feeds live distributor pricing into the pricebook and flags tasks where material cost changes have eroded margins would prevent the slow profit bleed of stale pricing.
**Tags:** #data-integration #time-series-forecasting #automation #revenue-impact #quick-win

## The Problem
ServiceTitan's pricebook is the largest deployed flat-rate pricing system in residential plumbing. It stores tasks with labor time, material costs, overhead allocation, and target margin. But the material costs are static — entered once during pricebook setup and never automatically updated. When the company's supplier changes prices (which happens quarterly for most materials and monthly for volatile items like copper and water heaters), the pricebook doesn't know. The service manager is supposed to review and update material costs manually, but this requires logging into distributor portals, comparing line-by-line, and updating hundreds of tasks in ServiceTitan — a 10-20 hour quarterly project that almost nobody actually does. The result: margin erosion that the owner doesn't notice until the P&L shows shrinking profits 3-6 months later.

## What Already Exists
ServiceTitan's pricebook module handles task storage, pricing presentation to homeowners, and basic task analytics. ServiceTitan's open API allows reading and writing pricebook data. Plumbing distributors (Ferguson, Hajoca, Winsupply) provide account-specific pricing via online portals and in some cases EDI/API feeds. Material cost tracking services (RSMeans, BNi Building News) publish construction cost data but at a broad industry level, not tied to specific distributor accounts or specific pricebook tasks.

## The Customization Gap
A ServiceTitan pricebook auto-updater needs: (1) integration with major plumbing distributor pricing — pulling the company's account-specific material costs from Ferguson, Hajoca, Winsupply, and local distributors via API, EDI, or scheduled scraping of account portals, (2) a material-to-task mapping layer that knows which materials appear in which pricebook tasks (e.g., "replace water heater 50 gal gas" includes: one water heater, two flex connectors, one gas connector, two SharkBite couplings, one expansion tank, one T&P drain), (3) automated margin impact calculation when material costs change — flagging tasks where the cost increase has pushed the effective margin below the company's target, and (4) a one-click price update that recalculates the flat-rate price at the target margin for all affected tasks, with a review-and-approve workflow before prices go live. Built as a ServiceTitan Certified App. Priced at $79-149/month, saving the company $10K-50K annually in hidden margin erosion.

## Target Customer
Residential plumbing companies on ServiceTitan with 500+ task pricebooks that haven't been comprehensively updated for material costs in 6+ months, experiencing unexplained margin compression that they attribute to "everything costs more" but haven't quantified or addressed task-by-task.

## Impact If Solved
Eliminates material cost-driven margin erosion, which typically represents 2-5% of revenue for companies with stale pricebooks. For a $2M/year operation, that's $40K-100K in recovered margin. Reduces the quarterly pricebook update from a 10-20 hour manual project (that usually doesn't happen) to a 30-minute review-and-approve session. Gives the service manager real-time visibility into which tasks are profitable and which are losing money.
