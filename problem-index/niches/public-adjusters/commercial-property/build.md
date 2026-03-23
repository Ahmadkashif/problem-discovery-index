# Business Interruption Loss Calculator

**Niche:** [[niches/public-adjusters/commercial-property/profile|Commercial Property Claims]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product exists that connects a business's financial data to its insurance policy's BI provisions and generates a defensible loss calculation with methodology documentation for carrier negotiation.
**Tags:** #linear-regression #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
Business interruption claims require calculating the income a business would have earned but for the loss — a counterfactual that depends on historical revenue trends, seasonal patterns, industry conditions, and mitigation efforts. PAs and forensic accountants build these calculations manually in Excel, pulling data from QuickBooks/Sage, applying seasonal adjustments, projecting the "but for" revenue, and subtracting actual revenue during the restoration period. A single BI calculation takes 20-40 hours of forensic accounting work and costs the PA $5,000-$15,000 in expert fees, which comes out of the client's settlement.

## Why Nobody Has Built This
BI calculations are part art, part science — the methodology must be defensible against carrier scrutiny, which means it must account for industry trends, local market conditions, and business-specific factors that a simple trend projection misses. Building a tool requires understanding both the financial modeling (time-series projection with seasonality) and the insurance policy provisions (waiting periods, period of restoration definitions, extended period of indemnity, coinsurance clauses) that constrain the calculation. The combination of financial and insurance expertise in one product team is rare.

## What to Build
A BI loss calculator that ingests the business's financial data (QuickBooks/Xero export), applies time-series modeling to project "but for" revenue, overlays policy-specific parameters (BI coverage limits, waiting period, ordinary payroll exclusion, period of restoration), and outputs a formatted BI claim package with methodology narrative, supporting schedules, and sensitivity analysis. The PA reviews and adjusts assumptions rather than building from a blank spreadsheet.

## Target Customer
Mid-size PA firms handling 10-30 commercial claims per year with BI components, currently outsourcing forensic accounting at $5,000-$15,000 per claim.

## Impact If Built
Reduces BI calculation time from 30 hours to 5-8 hours and eliminates $5,000-$15,000 in forensic accounting fees per claim. For a firm handling 20 BI claims per year, saves $100K-$300K annually. Faster BI claim submission accelerates settlement by 30-60 days.
