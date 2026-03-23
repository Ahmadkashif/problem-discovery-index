# Portfolio-Level Inventory Planning

**Niche:** [[niches/ecommerce-sellers/amazon-fba-aggregators/profile|Amazon FBA Aggregators & Multi-Brand Operators]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Demand forecasting tools exist for single-brand sellers, but none handle the portfolio-level inventory capital allocation problem that aggregators face across 20+ brands sharing a finite cash reserve.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact #data-integration

## The Problem
Aggregators must decide how to allocate limited working capital across inventory replenishment for 20-50 brands simultaneously. Reordering too much for one brand ties up cash that another brand needs to avoid a stockout. Standard inventory planning tools (SoStocked, RestockPro) forecast demand per SKU within a single account — they have no concept of cross-brand capital constraints, portfolio-level cash flow optimization, or opportunity cost of inventory investment in Brand A vs. Brand B.

## What Already Exists
SoStocked, RestockPro, and Forecastly provide single-account Amazon inventory planning with demand forecasting and reorder alerts. These tools assume unlimited capital and optimize each brand independently. Enterprise supply chain planning tools (Oracle, Kinaxis) handle multi-brand inventory but are designed for manufacturers, not marketplace sellers, and cost $500K+ annually.

## The Customization Gap
The missing layer is a capital-constrained portfolio optimizer: given total available cash, supplier lead times per brand, FBA storage fee schedules, and demand forecasts per SKU, compute the capital allocation across brands that maximizes portfolio-level margin. This requires integrating cash flow modeling (when each PO is due, when each brand's revenue deposits clear) with demand forecasting — a cross-brand optimization that single-account tools structurally cannot perform.

## Target Customer
Finance and operations leaders at aggregators who currently manage inventory capital allocation in spreadsheets, often making reorder decisions brand-by-brand without visibility into portfolio-level cash impact.

## Impact If Solved
Reduces stockout events by 25-40% across the portfolio by prioritizing inventory replenishment for high-velocity, high-margin brands. Cuts FBA long-term storage fees by 15-30% by avoiding over-ordering on slow-moving brands. Improves portfolio cash cycle by 5-10 days through optimized PO timing.
