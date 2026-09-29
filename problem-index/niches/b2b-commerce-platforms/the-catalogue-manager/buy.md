# Data Quality Management Practice

**Niche:** [[niches/b2b-commerce-platforms/the-catalogue-manager/profile|The Catalogue Manager]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data quality management is a mature discipline with profiling, rule-based validation and remediation workflow, and product catalogue quality is still measured as a completeness percentage.
**Tags:** #evaluation-metrics #descriptive-statistics #workflow-orchestration #compliance #automation #data-integration #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell the catalogue manager which gaps are costing sales — and whoever ranks the work by revenue at risk turns an endless backlog into a finite prioritised queue.

## The Problem
Enterprise data quality management has a well-developed practice: profile the data, express expectations as rules, score against dimensions, route exceptions to owners with workflow, and track remediation over time. It is applied seriously to financial, customer and regulatory data. Product catalogue data — which is larger, changes constantly, arrives from thousands of external parties and directly determines whether a customer can find something to buy — is managed with a completeness percentage and a spreadsheet.

## What Already Exists
Data quality platforms with profiling and rule engines; anomaly detection on value distributions; stewardship workflow with ownership and escalation; lineage tracking; and quality scorecards with trend reporting.

## The Customization Gap
The adaptation is from correctness to commercial usefulness. It requires: (1) scoring quality by revenue consequence rather than by rule violation count, which is the central change and is the one thing generic data quality tooling structurally cannot express; (2) rules generated from the category's own value distributions rather than authored by hand, since nobody will write validation rules for ten thousand attribute types across two hundred categories; (3) supplier-level scoring and feedback, because most catalogue defects originate outside the business and the remediation that matters is upstream; (4) handling attributes that are legitimately absent for some products and required for others, which breaks simple completeness rules and is why the percentage is misleading; and (5) integration with the storefront's search behaviour, which is the evidence generic tooling has no access to.

## Target Customer
Product information and catalogue teams, distributors with large technical catalogues, and data quality vendors for whom product data is an unserved application.

## Impact If Solved
The mature data quality discipline scores by rule violation, which cannot express commercial consequence. Generating rules from the category's own value distributions is the only way to cover ten thousand attribute types, and supplier-level feedback moves remediation upstream where the defects originate.
