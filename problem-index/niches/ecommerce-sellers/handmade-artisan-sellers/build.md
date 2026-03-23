# Production Capacity Planning for Maker Businesses

**Niche:** [[niches/ecommerce-sellers/handmade-artisan-sellers/profile|Handmade & Artisan Sellers]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool helps handmade sellers plan production runs based on demand forecasts, material availability, and their own labor capacity — leaving makers either overcommitted or idle.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #workflow-orchestration #worker-facing

## The Problem
A ceramicist who sells 200 mugs/month on Etsy and 50 wholesale units to Faire accounts cannot answer: "How many mugs should I throw this week to fulfill expected demand in 3 weeks, given my kiln capacity, clay inventory, and the glaze I'm waiting on?" Production decisions are made by gut feel, leading to either missed deadlines (Etsy shop goes into "vacation mode" during peak season) or overproduction (inventory sits unsold, tying up materials cost). Wholesale orders compound the problem because they have fixed delivery dates that must be planned around retail demand.

## Why Nobody Has Built This
The maker market is fragmented across thousands of craft types, each with different production processes (kiln firing vs. sewing vs. casting vs. woodworking), and the per-user revenue is low ($30-80/month willingness to pay). Standard manufacturing planning tools (MRP systems) are designed for factories, not a solo ceramicist with one kiln. The unit economics of building for this market have discouraged SaaS investment.

## What to Build
A lightweight production planning tool that ingests demand signals from Etsy, Faire, and Shopify, models the maker's production process (labor hours per unit, equipment capacity constraints, material requirements per item), and generates weekly production schedules that balance retail demand, wholesale commitments, and material availability. Visual calendar view showing: "This week: throw 80 mugs, trim Tuesday-Wednesday, bisque fire Thursday, glaze next Monday."

## Target Customer
Handmade sellers doing $50K-500K/year in revenue across Etsy, Faire, and/or Shopify who have outgrown "make to order" and need to plan production runs but cannot justify MRP software.

## Impact If Built
Reduces order fulfillment delays by 40-60% during peak seasons (Q4 holiday rush). Prevents overproduction waste on slow-moving items, recovering 10-15% of materials cost. Enables makers to confidently take wholesale orders by planning production around delivery dates.
