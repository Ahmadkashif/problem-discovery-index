# Faire-Style Reorder Suggestions Extended to Non-Faire Vendors

**Niche:** [[niches/independent-retailers/vendor-reorder-automation/profile|Vendor Reorder Automation]]
**Industry:** [[industries/independent-retailers|Independent Retailers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Faire provides smart reorder suggestions for products purchased on their marketplace, but 50-70% of an independent retailer's inventory comes from non-Faire vendors (direct accounts, trade shows, local makers) — the reorder intelligence should cover the entire catalog, not just one procurement channel.
**Tags:** #data-integration #time-series-forecasting #automation #quick-win

## The Problem
Faire's reorder notification feature ("You ordered this product 90 days ago and it's selling well — reorder now") is one of the best inventory management features available to independent retailers. But it only works for products purchased through Faire. A typical gift shop sources 30-50% of inventory from Faire and the rest from direct wholesale accounts, trade show purchases, local artisans, and other channels. The Faire-sourced products get smart reorder suggestions; everything else gets the owner-walking-the-store-and-guessing approach. This creates a two-tier inventory management system where the owner unconsciously under-manages non-Faire inventory because there are no prompts.

## What Already Exists
Faire ($0 — commission-based) provides reorder alerts, sales analytics, and wholesale marketplace for products on their platform. Shopify's Stocky provides purchase order management and demand forecasting within the Shopify ecosystem. Neither extends reorder intelligence to products sourced outside their respective platforms.

## The Customization Gap
The gap is extending Faire-quality reorder intelligence to the entire product catalog regardless of source. This requires: (1) a product database that includes both Faire-sourced and non-Faire products (populated from POS data, not from a marketplace), (2) sales velocity tracking from POS data for all products, (3) reorder point calculation using POS-derived sales velocity and user-entered vendor lead times, (4) reorder notifications that cover the entire catalog ("Reorder ceramic mugs from Local Potter Sue — lead time is 2 weeks, current stock is 5 days' supply"), and (5) purchase order generation for non-Faire vendors (email-based PO with the vendor's contact information). The tool should integrate with Faire for Faire-sourced products (using their reorder flow) and provide equivalent functionality for everything else.

## Target Customer
Independent retailers who love Faire's reorder suggestions but wish they worked for their entire inventory, not just the 30-50% sourced through Faire.

## Impact If Solved
Extends intelligent reorder management from 30-50% of inventory (Faire-sourced) to 100%, reducing stockouts on non-Faire products by 40-60%. Reduces the time spent on manual reorder decisions for non-Faire vendors from 3-5 hours/week to 30 minutes of review.
