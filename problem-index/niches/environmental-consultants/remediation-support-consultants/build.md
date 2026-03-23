# Affordable Remediation Data Management and Trend Analysis Platform

**Niche:** [[niches/environmental-consultants/remediation-support-consultants/profile|Remediation Support Consultants]]
**Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A cloud-based platform that replaces the Excel-workbook-per-site approach to remediation data management with a structured database that ingests lab results, compares against regulatory screening levels, generates concentration trend plots, and flags wells approaching or exceeding cleanup criteria — at $200-500/month instead of EQuIS's $15,000+/year.
**Tags:** #time-series-forecasting #anomaly-detection #tabular-ml #data-integration #revenue-impact

## The Problem
Mid-size environmental firms (10-30 people) manage 30-80 active remediation sites with data stored in Excel workbooks — one per site, growing to hundreds of megabytes over multi-year projects. When a new quarterly sampling event occurs, the scientist must: import lab results into the spreadsheet, compare each analyte against the applicable screening level (which varies by state, media type, and land use), update concentration trend charts, check for statistical trends (Mann-Kendall), and identify wells showing increasing or decreasing contaminant concentrations. This quarterly data update takes 4-8 hours per site, multiplied across 50 sites equals 200-400 hours per quarter — nearly a full-time position devoted to spreadsheet maintenance.

## Why Nobody Has Built This
EQuIS owns the large-site market and has no incentive to build a simplified, lower-cost version. Building a competitor requires: (1) flexible lab data import (EDDs come in dozens of formats — TestAmerica/Pace/Eurofins each have different column layouts), (2) a regulatory screening level database covering 50 states with different cleanup standards for soil, groundwater, vapor, and different land uses, and (3) statistical trend analysis (Mann-Kendall, Sen's slope) integrated with visualization. The market of mid-size firms is fragmented — no single customer justifies the build cost — but collectively, 5,000-8,000 firms need this tool.

## What to Build
A SaaS platform with: (1) a universal lab data importer that normalizes EDDs from major labs into a standard schema, (2) a regulatory screening level database updated quarterly covering all 50 states, (3) automatic comparison of each result against applicable screening levels with exceedance flagging, (4) concentration trend plots per well per analyte with Mann-Kendall trend analysis, (5) a dashboard showing which sites have wells exceeding cleanup criteria or trending upward, and (6) export templates for state-specific regulatory reporting formats. Priced at $200-500/month per firm (not per site), making it accessible to 10-person shops.

## Target Customer
Remediation project managers at 10-30 person environmental firms managing 20+ active sites, currently drowning in Excel workbooks and manually comparing results against screening levels.

## Impact If Built
Reduces quarterly data management from 4-8 hours to 1-2 hours per site. For a firm managing 50 sites, this saves 150-300 hours per quarter (600-1,200 hours annually) — equivalent to a full-time position. Catches screening level exceedances immediately instead of during report preparation, enabling faster regulatory response.
