# Data Reconciliation Practice

**Niche:** [[niches/programmatic-ad-platforms/the-ad-operations-specialist/profile|The Ad Operations Specialist]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data engineering has reconciliation frameworks, freshness checks and automated break analysis as standard practice, and ad operations compares spreadsheets.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #automation #workflow-orchestration #hypothesis-testing #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to explain the discrepancy between three systems automatically instead of having a person derive it every month — and whoever does that removes the most repeated unproductive task in the category.

## The Problem
Reconciling counts between systems that disagree is ordinary data engineering. Frameworks exist for expressing expectations, comparing source and target, surfacing breaks with diagnostics, monitoring freshness and alerting on drift. Any competent data platform team deploys this as infrastructure. Ad operations performs the same reconciliation between three or four systems, monthly, at every agency and publisher in the industry, using exported spreadsheets and personal expertise.

## What Already Exists
Data quality and expectation frameworks; source-to-target reconciliation tooling; break detection with root cause diagnostics; freshness and completeness monitoring; and lineage tracking across pipelines.

## The Customization Gap
The adaptation is to systems owned by counterparties with different and undocumented definitions. It requires: (1) reconciliation across organisational boundaries where the schemas, definitions and counting points are not merely different but undisclosed, which is the substantive difference — internal reconciliation assumes you can read both systems' code and here you cannot; (2) a domain-specific cause library, since the diagnostics that matter are advertising-specific and no generic framework will ever contain them; (3) legitimate rather than erroneous discrepancy as the normal case, which inverts the usual assumption that a break means a defect and changes what the tool should say; (4) output aimed at a client conversation rather than at an engineer, since the consumer is a commercial relationship; and (5) deployment by teams with no data engineering capability, which rules out anything requiring a pipeline to be written.

## Target Customer
Ad operations teams at agencies, publishers and advertisers, ad tech vendors reducing their support load, and data quality vendors for whom cross-organisational reconciliation is unserved.

## Impact If Solved
Internal reconciliation assumes you can read both systems, and here the definitions are undisclosed and owned by a counterparty. An advertising-specific cause library and an output aimed at a client conversation are what a generic framework will never supply.
