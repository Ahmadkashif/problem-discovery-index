# A Traceable Statistical Pipeline From Agent to Exhibit

**Niche:** [[niches/title-insurance-carriers/statistical-reporting-rate-filings/profile|Title Statistical Reporting & Rate Filings]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Title rate cases turn on agent-level premium, expense and loss data that is rebuilt by hand for each cycle and cannot be traced to source when opposing actuaries challenge it.
**Tags:** #descriptive-statistics #linear-regression #confidence-intervals #large-language-models #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn thousands of agents' production records into statistical-plan submissions and rate-filing exhibits that trace to source, and whoever's numbers the regulator and the opposing actuaries cannot impeach at the hearing takes the account.

## The Problem
For each rate cycle, statistical staff collect premium, transaction counts by rate bracket, escrow fees and agent expense data from thousands of agents' systems. They code each item to the statistical plan, reconcile the totals to statutory statements and build the exhibits. When TLTA appealed the February 2025 Texas order, the dispute was about which years of data the commissioner had used. The data's provenance had become the argument.

## Why Nobody Has Built This
The buyers are few: a few dozen underwriters, a handful of associations and bureaus. The work peaks once every cycle, and consulting actuaries rebuild it in spreadsheets each time.

## What to Build
A pipeline that ingests agents' production extracts and maps fee and charge codes to each state's statistical plan, using an LLM-assisted mapper with human confirmation. It validates against remittances and statutory statements and keeps the lineage of every figure. It produces standard exhibits with sensitivity analysis and confidence intervals on the indications, and lets any exhibit cell be traced back to the agent records behind it.

## Target Customer
Chief actuaries and regulatory affairs leads at underwriters, state land title associations, and rating bureaus.

## Impact If Built
Each rate cycle becomes a refresh rather than a rebuild, and the underwriter arrives at a contested hearing with numbers the other side cannot impeach on provenance.
