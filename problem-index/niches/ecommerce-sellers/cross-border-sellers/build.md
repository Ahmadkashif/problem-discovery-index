# Automated HS Code Classification and Duty Calculator

**Niche:** [[niches/ecommerce-sellers/cross-border-sellers/profile|Cross-Border & International Sellers]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automatically classifies e-commerce SKUs into correct HS codes across destination countries and calculates landed cost including duties, making every cross-border pricing decision a guess.
**Tags:** #bert #text-classification #nlp #compliance #automation

## The Problem
A seller shipping 200 SKUs to 10 countries needs each SKU classified into the correct Harmonized System (HS) code for each destination — and HS codes are not universal at the 6+ digit level, meaning the same product can have different duty rates depending on the destination country's schedule. Misclassification triggers customs holds (2-5 day delays), fines (up to 4x the underpaid duty), and customer refunds. Most sellers either pay customs brokers $15-30 per classification or guess — and guessing wrong on a high-volume SKU can cost thousands in penalties.

## Why Nobody Has Built This
HS code classification requires understanding product composition, material, function, and end-use — information that lives in product descriptions, spec sheets, and sometimes only in the seller's head. The classification logic is codified in thousands of pages of tariff schedules that vary by country and are updated annually. Building a reliable classifier requires training on millions of product-to-code mappings, which customs authorities don't publish as structured datasets. Companies like Zonos and Avalara have partial solutions but focus on checkout-time duty estimation, not proactive SKU-level classification management.

## What to Build
An NLP-powered HS code classification engine that ingests product descriptions, images, material specs, and category metadata from marketplace listings, maps each SKU to the correct HS code for each destination country, calculates applicable duty rates including any trade agreement preferences (USMCA, EU FTAs), and produces a per-SKU landed cost estimate. The system flags high-risk classifications for human review and automatically updates when tariff schedules change.

## Target Customer
Cross-border sellers on Amazon, Shopify, and eBay shipping 100+ SKUs internationally who currently rely on manual classification or customs broker services.

## Impact If Built
Eliminates $3K-10K/year in customs broker classification fees per seller. Reduces customs holds by 60-80% through accurate pre-classification. Enables accurate landed-cost pricing that prevents margin erosion on international orders — typically recovering 3-8% in under-priced duty exposure.
