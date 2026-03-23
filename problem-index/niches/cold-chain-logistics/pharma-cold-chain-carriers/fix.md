# Manual MKT Calculation and Compliance Report Assembly

**Niche:** [[niches/cold-chain-logistics/pharma-cold-chain-carriers/profile|Pharmaceutical Cold Chain Carriers]]
**Industry:** [[industries/cold-chain-logistics|Cold Chain Logistics]]
**Type:** Fix (Pain Point)
**One-liner:** Compliance analysts spend 45-90 minutes per shipment manually exporting temperature data, calculating MKT in spreadsheets, and formatting GDP compliance reports — a repeatable process that should be a one-click operation.
**Tags:** #automation #compliance #data-integration #worker-facing

## The Problem
Every pharma cold chain shipment generates a compliance deliverable: a GDP-formatted temperature report with MKT calculation, chain-of-custody documentation, and excursion narrative (if applicable). Compliance analysts currently export raw CSV data from Sensitech or Controlant, import it into an Excel template with MKT formulas, manually verify data completeness across shipment legs, draft any excursion narratives, format the output to the specific pharma customer's template, and route for electronic signature. For a carrier processing 200 pharma shipments per week, this represents 1.5-2 FTEs of dedicated compliance analyst labor.

## Why It's Still Broken
Three factors perpetuate the manual workflow. First, each pharma customer specifies a different report template — there is no GDP report standard format, so every customer relationship requires a custom output. Second, multi-leg shipments (truck to warehouse to truck to final delivery) require stitching temperature data from multiple loggers across handoff points, a reconciliation step that monitoring platforms don't automate. Third, MKT calculation requires the activation energy constant (Ea) specific to each pharmaceutical product, which varies by drug product and is provided in the customer's quality agreement — not in any monitoring platform database.

## What a Fix Looks Like
A middleware layer that connects to Sensitech/Controlant APIs, automatically stitches multi-leg temperature data, calculates MKT using product-specific Ea values stored in a customer configuration database, generates the compliance report in the customer's specified template, and routes for electronic signature with a GxP-compliant audit trail. Exception cases (data gaps, logger failures, excursion events) are flagged for analyst review rather than requiring manual review of every shipment.

## Who Feels the Pain
Compliance analysts and quality coordinators at pharma cold chain carriers — typically 1-3 people per organization who are the bottleneck for shipment closeout. When report generation falls behind, shipments are delivered but documentation is incomplete, creating GDP compliance exposure during customer audits.

## Impact If Fixed
Reduces per-shipment compliance documentation from 45-90 minutes to 5-10 minutes of exception review. For a carrier processing 200 pharma shipments/week, this eliminates 1-1.5 FTEs of compliance labor ($75,000-$110,000/year). More critically, ensures 100% of shipments have audit-ready documentation at delivery rather than the current 2-5 day documentation lag.
