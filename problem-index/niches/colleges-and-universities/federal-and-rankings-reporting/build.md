# One Census Snapshot Feeding Every Survey

**Niche:** [[niches/colleges-and-universities/federal-and-rankings-reporting/profile|Federal & Rankings Survey Reporting (IPEDS, Common Data Set, Rankings)]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An IR office answers IPEDS, the Common Data Set, rankings and state surveys from separate extracts, then spends weeks reconciling numbers that should have come from one place.
**Tags:** #large-language-models #data-integration #workflow-orchestration #automation #compliance #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to produce an institution's IPEDS, Common Data Set and rankings submissions from one reconciled data snapshot, and whoever produces them with the fewest post-submission revisions takes the account.

## The Problem
Each survey asks for headcounts, completions, retention, admissions and finance figures with its own definitions and cohort dates. The IR office pulls data separately for each, often from different extracts, and finds discrepancies when an accreditor or rankings editor compares them.

## Why Nobody Has Built This
Survey definitions change annually and live in instruction documents, not data models. Reporting tools provide warehouses and dashboards but leave the mapping from definitions to queries to each office.

## What to Build
A frozen census snapshot per term plus a definitions layer that reads each survey's instructions, maps every item to queries on the snapshot, and generates draft submissions with item-level lineage. It explains year-over-year changes and checks consistency across IPEDS, the Common Data Set, rankings and state reports before anything is submitted. A public demo can start from IPEDS survey instructions and published Common Data Sets.

## Target Customer
Directors of institutional research at colleges with one to five IR staff.

## Impact If Built
Every external number traces to one snapshot and one definition. Cutting reconciliation and drafting time by half gives a two-person IR office back ~400–600 hours a year (estimate).
