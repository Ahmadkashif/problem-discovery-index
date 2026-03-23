# Mechanical Integrity Test Scheduling and Documentation

**Niche:** [[niches/oil-gas-field-services/regulatory-reporting-automation/profile|Regulatory Reporting Automation]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Fix (Pain Point)
**One-liner:** Mechanical integrity tests (MITs) are required on fixed schedules by state commissions, but operators track deadlines in spreadsheets and lose test documentation in paper files, resulting in violations and well shut-in orders.
**Tags:** #workflow-orchestration #compliance #automation #quick-win

## The Problem
State oil and gas commissions require periodic mechanical integrity tests on injection wells (Class II UIC wells) and certain production wells — typically every 5 years for annular pressure tests and casing inspections. An operator with 200 wells may have 40+ MIT obligations per year, each requiring scheduling a contractor, performing the test, documenting results in the state-prescribed format, and filing within a compliance window. Operators track these deadlines in spreadsheets that are updated annually (if at all), test results are filed as paper or PDF documents in per-well folders, and the connection between the test record and the regulatory filing is not maintained systematically. When a state inspector requests MIT documentation, the compliance manager may spend hours locating the correct test report, pressure chart, and filing receipt.

## Why It's Still Broken
MIT scheduling falls between two systems: the production accounting system (which tracks wells and their attributes) and the maintenance management system (which tracks work orders). Neither owns the regulatory compliance calendar. Test results come from third-party contractors in inconsistent formats (paper pressure charts, PDF reports, raw data files) and are filed by whoever happens to receive them. There is no triggering mechanism that connects the 5-year MIT cycle to the actual scheduling of the test — it relies on someone remembering to check the spreadsheet.

## What a Fix Looks Like
A compliance calendar module that ingests the well list and state MIT requirements, calculates the next test due date for each well based on the last completed test, auto-generates work orders for the testing contractor 90/60/30 days before the deadline, accepts test results in any format (photo of pressure chart, PDF report, digital data file), associates them with the well and the regulatory obligation, generates the state-specific filing form, and marks the obligation complete when the filing is confirmed. Dashboard shows upcoming MIT deadlines, overdue wells, and filing status.

## Who Feels the Pain
Field supervisors and compliance managers at independent operators who personally bear responsibility for MIT compliance but manage it as a side task alongside production optimization and safety management, and who face well shut-in orders (losing $5,000-$20,000/day in production per well) when tests are missed.

## Impact If Fixed
Eliminates missed MIT deadlines that currently result in 5-10% of an operator's UIC wells being flagged for non-compliance annually, prevents well shut-in orders that cost $5,000-$20,000/day per well, and reduces the time spent locating test documentation from hours to seconds during regulatory inspections.
