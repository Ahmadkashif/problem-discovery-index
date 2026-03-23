# Per-Customer Profitability and LTV Attribution Engine

**Niche:** [[niches/ecommerce-sellers/shopify-dtc-brands/profile|Shopify DTC Brand Operators]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool shows a DTC brand the true profit per customer after acquisition cost, returns, fulfillment, and support tickets — making it impossible to know which acquisition channels produce profitable customers vs. money-losing ones.
**Tags:** #gradient-boosting #regression #tabular-ml #data-integration #revenue-impact

## The Problem
A DTC brand spending $50K/month on Meta and Google ads can see which campaigns drive purchases, but cannot see which campaigns drive profitable customers after factoring in return rates (25-40% in apparel), support ticket costs ($5-15 per ticket via Gorgias), fulfillment costs, and repeat purchase behavior. A campaign that generates $30 AOV customers who return 40% of orders and never repurchase is destroying value, but current tools report it as "profitable" based on first-order ROAS.

## Why Nobody Has Built This
Building per-customer profitability requires stitching together data from Shopify (orders, refunds), the ad platform (attribution), Gorgias or Zendesk (support costs), the 3PL or ShipBob (fulfillment costs), and Loop/Returnly (return disposition). Each system uses a different customer identifier, and matching them at the individual customer level requires probabilistic identity resolution. The attribution layer itself is contested territory — Meta, Google, and Triple Whale each claim different credit for the same conversion.

## What to Build
A customer-level data platform that ingests events from Shopify, ad platforms, support tools, returns platforms, and fulfillment providers, resolves them to a single customer identity, and computes per-customer lifetime profitability. Roll up to the acquisition channel/campaign level to show: "Meta Lookalike Campaign #7 acquires customers with an average 12-month LTV of $85 after all costs, while TikTok Spark Ads acquire customers with a $12 average 12-month LTV." This data feeds directly into ad budget allocation decisions.

## Target Customer
DTC founders and growth leads spending $20K+/month on paid acquisition who are currently optimizing on ROAS or blended CAC without visibility into post-acquisition economics.

## Impact If Built
Enables reallocation of 15-30% of ad spend from unprofitable to profitable channels, typically improving blended contribution margin by 8-15 percentage points. Identifies and suppresses acquisition of chronic returners before they enter the funnel.
