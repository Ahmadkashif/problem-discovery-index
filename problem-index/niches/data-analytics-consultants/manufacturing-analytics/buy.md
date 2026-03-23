# Pre-Built OEE and Quality Analytics Templates

**Niche:** [[niches/data-analytics-consultants/manufacturing-analytics/profile|Manufacturing Analytics & Industry 4.0]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Tableau and Power BI offer manufacturing dashboard templates, but they assume clean, structured data — not the raw historian exports with missing timestamps, variable sampling rates, and undefined downtime categories that consultants actually receive from factories.
**Tags:** #automation #data-integration #quick-win #tabular-ml

## The Problem
Every manufacturing analytics engagement includes the same core deliverables: OEE (Overall Equipment Effectiveness) dashboard, downtime Pareto analysis, quality metrics (first-pass yield, scrap rate, defect distribution), and cycle time analysis. Consultants rebuild these analytics from scratch for every client because the input data format varies by factory. But the underlying calculations are standardized — OEE = Availability x Performance x Quality. The variation is in how "availability," "performance," and "quality" are measured with the client's specific data (which fields represent downtime? How is planned vs. unplanned downtime distinguished? What constitutes a "defect"?). Templating these analytics with parameterizable data mappings would eliminate 60-70% of the rebuild effort.

## What Already Exists
Tableau Server offers pre-built manufacturing dashboards through its Exchange. Power BI has manufacturing-specific content packs. Seeq provides OEE analytics for historian data. But these templates assume the data is already clean, structured, and mapped to standard fields. In reality, consultant data arrives as: raw historian extracts with 5,000 unlabeled tag columns, ERP exports with factory-specific downtime codes, and MES data with custom batch record structures. The gap between template expectations and actual data renders pre-built dashboards useless without significant customization.

## The Customization Gap
The templates need: (1) a data mapping interface where the consultant maps client-specific fields to standard manufacturing KPI inputs ("column X = machine state, value 'R' = running, value 'D' = down, value 'M' = maintenance"), (2) data quality preprocessing (handle missing timestamps, interpolate gaps, detect sensor flatlines), (3) parameterizable KPI definitions (OEE calculation that adapts to the client's definition of "ideal cycle time" and "planned downtime"), (4) drill-down from KPI to raw sensor data for root cause investigation, and (5) exportable deliverables (PDF reports, presentation-ready charts) that consultants can brand and include in their final deliverables.

## Target Customer
Manufacturing analytics consultants delivering 5+ factory analytics engagements per year, where OEE and quality dashboards are standard deliverables.

## Impact If Solved
Reduces core manufacturing dashboard development from 3-4 weeks to 3-5 days per engagement. Ensures analytical consistency across engagements (same OEE calculation methodology, same visualization standards). Enables junior consultants to deliver manufacturing analytics previously requiring senior expertise.
