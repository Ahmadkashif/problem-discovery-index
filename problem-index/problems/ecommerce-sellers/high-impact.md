# True Profitability Tracking per SKU Across Channels

**Industry:** [[ecommerce-sellers|E-Commerce Sellers]]
**Type:** High Impact
**One-liner:** Sellers finally know which of their 500 SKUs actually make money after every fee, ad dollar, return, and storage charge is allocated — and kill the losers within days instead of months.
**Tags:** #gradient-boosting #regression #tabular-ml #data-integration #revenue-impact

## The Problem
A mid-size e-commerce seller running 200-500 SKUs across Amazon, Shopify, and Walmart cannot answer the basic question: "Which products are profitable?" Revenue is visible, but true profit requires combining COGS (which changes with each supplier PO), marketplace fees (Amazon referral fees, FBA pick-and-pack, storage, Shopify transaction fees), advertising cost allocated per SKU (not per campaign), return rates with associated restocking and shipping costs, and inbound freight amortized across units. Most sellers discover a product was unprofitable only after 3-6 months of selling it, by which time they've reordered inventory twice.

## Why It's Unsolved
The data lives in 6-10 disconnected systems: Amazon Seller Central reports, Shopify admin, ad platform dashboards, supplier invoices (often PDFs or emails), 3PL billing, and shipping carrier invoices. Fee structures change frequently — Amazon updates FBA fees annually and storage fees quarterly. Allocating shared costs (a single PPC campaign driving traffic to 15 ASINs, a single freight shipment containing 40 SKUs) requires attribution models that no off-the-shelf accounting tool handles. Existing tools like Sellerboard and Inventory Lab cover Amazon-only and require extensive manual COGS entry.

## What a Solution Looks Like
A system that ingests API data from Amazon, Shopify, Walmart, and ad platforms automatically; uses OCR and structured extraction on supplier invoices and freight bills to capture COGS; applies attribution models to allocate shared advertising and logistics costs to individual SKUs; and produces a real-time profit-per-unit dashboard with trend lines, margin alerts, and automated recommendations to discontinue, reprice, or double-down on specific products.

## Impact If Solved
Sellers running 200+ SKUs typically discover 15-25% of their catalog is margin-negative once all costs are allocated. Eliminating those products and reallocating ad spend to profitable SKUs can increase net margin by 8-15 percentage points — the difference between a struggling operation and a sustainable business.
