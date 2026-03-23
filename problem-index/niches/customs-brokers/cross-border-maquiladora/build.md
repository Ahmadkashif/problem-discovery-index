# IMMEX Temporary Import Reconciliation Platform

**Niche:** [[niches/customs-brokers/cross-border-maquiladora/profile|Cross-Border Maquiladora Operations]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform tracks the full lifecycle of temporary imports under Mexico's IMMEX program — from US export through Mexican assembly to re-export — proving that each imported material was used in manufacturing and re-exported within the required timeframe, which is the core compliance obligation that prevents duty assessment on the temporary imports.
**Tags:** #automation #compliance #data-integration #workflow-orchestration

## The Problem
Under IMMEX, materials imported temporarily into Mexico for manufacturing must be re-exported (as finished products) within 18 months, or duties become payable. A maquiladora importing 500 material SKUs per month must track: which materials were received, when they were consumed in manufacturing, which finished products they went into, and when those finished products were re-exported. This material-to-product-to-export reconciliation is the compliance obligation that maintains the duty-free status. Most maquiladoras track this in spreadsheets or legacy SAP custom modules — neither of which provides the real-time reconciliation visibility needed to identify materials approaching their 18-month deadline.

## Why Nobody Has Built This
IMMEX reconciliation spans three data domains: (1) Mexican customs import records (pedimentos de importacion temporal); (2) manufacturing production records (bill of materials, work orders); (3) Mexican customs export records (pedimentos de exportacion). These data sources are in different systems, different formats, and often managed by different departments (customs team, production team, logistics team). Building a reconciliation platform requires integrating across all three — which no single-domain software vendor has done.

## What to Build
An IMMEX reconciliation platform that: (1) ingests temporary import records (material, quantity, import date, pedimento number); (2) connects to manufacturing records to track material consumption by finished product; (3) ingests export records to confirm re-export of finished products; (4) reconciles the material-to-product-to-export chain, identifying materials that haven't been consumed or whose finished products haven't been exported; (5) alerts when materials are approaching the 18-month deadline without documented consumption/export.

## Target Customer
IMMEX compliance managers at manufacturers operating maquiladora plants in Mexico. Approximately 3,000 active IMMEX programs in Mexico, of which ~1,500 are operated by US manufacturers. Average contract value: $24-48K/year.

## Impact If Built
Preventing duty assessment on unreconciled temporary imports saves $50K-$500K per incident. Automated reconciliation reduces the compliance team's monthly reconciliation from 40-60 hours to 4-8 hours of review.
