# Public Prior Authorization Metrics From the Plan's Own Records

**Niche:** [[niches/health-insurance-carriers/utilization-management/profile|Utilization Management & Prior Authorization]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every plan already owns business intelligence tools; what it lacks is a defensible way to compute the prior authorization metrics CMS now makes it publish, from records spread across its own UM platform and its delegated vendors.
**Tags:** #descriptive-statistics #evaluation-metrics #data-integration #compliance #automation #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to decide authorization requests inside the CMS-0057-F clocks with determinations that survive appeal. But outpatient prior authorization and inpatient and post-acute concurrent review are won on different inputs, clocks, vendors and outcomes, so the niche is decomposed into contested sub-niches below.

## The Problem
CMS-0057-F requires impacted payers to publish prior authorization metrics each year. The first, covering 2025, were due by 31 March 2026: approval and denial rates, approvals after appeal, extensions, and average decision times for standard and expedited requests. A plan's requests are split across its own UM system and several specialty benefit managers, each with its own definition of a "request", a "decision" and a "day".

## What Already Exists
Enterprise BI and data warehouse tools (Tableau, Power BI, Snowflake), the reporting modules of UM platforms, and vendor-supplied delegate reports.

## The Customization Gap
The plan needs a common request-level model across all delegates. It needs CMS's metric definitions encoded once, including how to count pended-for-information time, partial approvals, withdrawn requests and Part B drugs, which keep separate 24- and 72-hour clocks. It also needs reconciliation to the universes a CMS program audit would pull, and a monthly internal view of the same metrics, so the published figure is never the first time anyone has seen it.

## Target Customer
UM operations and compliance leaders at MA and Medicaid plans with two or more delegated UM vendors.

## Impact If Solved
A defensible published metric, an internal early-warning view of decision-time slippage before it becomes an audit finding, and one definition of a request across every delegate.
