# Material-to-Product Conversion Documentation

**Niche:** [[niches/customs-brokers/cross-border-maquiladora/profile|Cross-Border Maquiladora Operations]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** IMMEX audits require documentation proving that temporarily imported materials were actually used in manufacturing — a bill-of-materials-to-production-record linkage that maquiladoras maintain in spreadsheets, leading to audit findings when the documentation trail is incomplete or inconsistent.
**Tags:** #automation #compliance #data-integration #quick-win

## The Problem
Mexican customs (SAT) audits IMMEX programs to verify that temporarily imported materials were used in manufacturing and not diverted for domestic sale (which would require duty payment). The audit requires: (1) showing which temporarily imported materials went into which finished products (bill of materials linkage); (2) showing production records proving those finished products were manufactured (work orders, production logs); (3) showing export records proving those finished products were re-exported (pedimentos de exportacion). The maquiladora must produce this documentation for every material imported in the audit period — potentially thousands of line items. Most maquiladoras piece this documentation together from SAP production records, Excel spreadsheets, and paper filing cabinets. Missing a single linkage for a single material triggers a finding.

## Why It's Still Broken
The three data domains (customs import, production, customs export) are managed by three different teams in three different systems. The customs team tracks import pedimentos; the production team tracks work orders and bills of materials; the logistics team tracks export pedimentos. No one system links all three for IMMEX reconciliation purposes. The linkage is typically constructed during audit prep — retroactively assembling a documentation trail that should have been maintained continuously.

## What a Fix Looks Like
A continuous documentation system that: (1) links each temporary import pedimento to the bill of materials that consumes the imported material; (2) links the production work order to the finished product; (3) links the finished product to the export pedimento; (4) maintains this three-way linkage in real time as each transaction occurs (not retroactively during audit prep); (5) generates audit-ready documentation packages on demand.

## Who Feels the Pain
IMMEX compliance managers who spend 2-4 weeks preparing for SAT audits — reconstructing documentation trails that should have been maintained continuously. And maquiladora controllers who face duty assessments of $100K-$1M when audit documentation is incomplete.

## Impact If Fixed
Eliminating audit prep time saves 80-160 hours per annual audit. Preventing duty assessments from documentation gaps (not from actual non-compliance, but from inability to prove compliance) avoids $100K-$1M in preventable penalties per audit cycle.
