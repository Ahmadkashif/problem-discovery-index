# Data Lineage Practice

**Niche:** [[niches/customer-data-platforms/downstream-impact-tracing/profile|Downstream Impact Tracing]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lineage and impact analysis are established data governance capabilities, and they stop at the warehouse edge where the customer-facing systems begin.
**Tags:** #graph-theory #data-integration #workflow-orchestration #automation #compliance #evaluation-metrics #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to say what breaks when something changes, before it changes — and whoever builds that lineage across the customer data stack makes every other failure in the category preventable.

## The Problem
Data lineage is a mature governance capability. Catalogues parse transformation code to build column-level dependency graphs, impact analysis shows what a change affects, and teams use it before refactoring. It is standard in any organisation with a serious data platform. Its coverage ends at the analytical boundary: dashboards and models are nodes, and the segments, journeys, activations and campaigns that consume the same data are not, which is where the customer-facing consequences of a change actually occur.

## What Already Exists
Column-level lineage parsed from transformation code; impact analysis before change; catalogue integration with ownership metadata; automated lineage refresh; and cross-system lineage across warehouse tooling.

## The Customization Gap
The adaptation is to nodes that are marketing objects and destinations outside the organisation. It requires: (1) parsing segment logic, journey conditions and activation mappings rather than transformation code, which is a different set of definition languages and is the substantive parsing work; (2) external destinations as terminal nodes, so the graph ends in an advertising platform rather than in a dashboard, which no lineage tool models; (3) consequence classification, since a broken report and a broken suppression list are not comparable and the graph should say which is which; (4) consumers who are marketers, so the impact view must be legible without data vocabulary; and (5) definitions that change constantly and are edited through interfaces rather than committed as code, which makes automated refresh essential rather than nightly.

## Target Customer
Data platform and governance teams, customer data platform vendors, and catalogue vendors for whom the activation layer is unmapped.

## Impact If Solved
Lineage is mature and stops at the analytical boundary, which is one layer above where the consequences happen. Parsing segment and journey definitions, and modelling external destinations as terminal nodes, is what extends it across the boundary.
