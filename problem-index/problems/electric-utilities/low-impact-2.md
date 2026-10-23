# Storm Cost Recovery From a Shoebox of Crew Invoices

**Industry:** [[electric-utilities|Electric Distribution Utilities]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** After a major storm a utility receives invoices, timesheets, lodging and meal bills from dozens of mutual-assistance utilities and contractors, and must turn them into a cost record that a commission or FEMA will reimburse, mostly by hand over many months.
**Tags:** #large-language-models #transformers #random-forests #descriptive-statistics #compliance #automation #data-integration

## The Problem
When a hurricane or ice storm takes out a large share of a system, the utility brings in hundreds or thousands of line and tree crews from other utilities and contractors through its regional mutual-assistance group. Each crew bills afterwards in its own format: hourly labour by person and day, equipment hours, travel time, overtime multipliers, mobilisation and demobilisation, hotels, meals and fuel. Storms are now the largest single driver of outage time. Major events caused 80% of the 11 hours US customers spent without power in 2024 (EIA), so this paperwork recurs every year in many service territories.

Recovering the money is its own project. An investor-owned utility asks its commission for a storm reserve draw, a deferral or securitisation, and staff and intervenors audit for prudence: were rates reasonable, were crews released promptly, were the hours real? Cooperatives and municipal utilities can apply for FEMA Public Assistance (estimate of eligibility rules, recalled), which has its own categories, documentation standards and audits. Storm accountants reconcile invoices against crew rosters, check rates against mutual-aid terms, and chase missing timesheets, sometimes for a year or more.

## What Already Exists
Accounts-payable automation (Coupa, SAP Concur, Tipalti and OCR invoice capture tools) reads invoices and matches them to purchase orders. Workforce management tools track employee time. Some storm logistics platforms track crew rosters and lodging during an event, and FEMA's grants portal manages Public Assistance applications.

## The Customisation Gap
Storm invoices have no purchase order and no standard format. The industry logic missing from generic AP tools: matching invoices to the crews actually released and checked in during the event; applying the mutual-aid agreement's rate and overtime rules; flagging duplicate or overlapping hours across crews; separating capital replacement from operating restoration cost for accounting; mapping costs to FEMA Public Assistance categories for public power and co-ops, or to the commission's prudence-review schedules for IOUs; and assembling a document package an auditor can follow from the claim back to the timesheet.

## Impact If Solved
Cutting reconciliation from ~6–12 months to ~4–8 weeks (estimate) would bring storm cash back sooner and could cut the share disallowed for weak documentation by a few percentage points (estimate). For a small co-op after a major storm, that can be the difference between recovering the cost and absorbing it into rates.
