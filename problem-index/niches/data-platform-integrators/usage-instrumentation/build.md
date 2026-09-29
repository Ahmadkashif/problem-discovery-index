# A Standing Account of What Is Used

**Niche:** [[niches/data-platform-integrators/usage-instrumentation/profile|Usage Instrumentation]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform records every access and nobody has turned that into a report about the estate.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #graph-theory #automation #revenue-impact #confidence-intervals #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn query logs, lineage and cost data into a standing account of what each asset is worth — and whoever produces that takes the account.

## The Problem
Every modern data platform logs queries in detail: which object, by whom, from which tool, how often, at what cost. Lineage links objects to what depends on them. None of it is assembled into an account of the estate. So questions that should be routine — is this dashboard used, does anyone read this table, what does this model cost relative to its use — are answered by asking around.

## Why Nobody Has Built This
The logs are technical artefacts used for troubleshooting and billing rather than for asset management. Joining them requires modest work nobody has scheduled. The catalogue vendors sell discovery rather than utilisation. And no one function owns the estate's health.

## What to Build
Assemble the standing report and keep it current. Join query history, lineage and cost into an asset-level utilisation view refreshed continuously, which is the core and is the product. Separate human queries from pipeline reads, since an asset read only by a downstream model has a derived rather than direct value. Report the consumer distribution per asset, as breadth of use is a better signal than count. Attribute cost per asset including the cost of everything it depends on, which is the true figure and is never computed. Show the trend, since an asset whose use is declining is a different case from one that never had any. Cover dashboards and downstream tools as first-class assets, which is where proliferation is worst. Identify assets with high cost and low use explicitly, which is the actionable list. Highlight assets with no owner, since ownership is the prerequisite for any later decision. Make it a standing report with a cadence rather than a one-off analysis. And publish it to asset owners rather than only to leadership, which is where the behaviour changes.

## Target Customer
Data platform teams and leadership, integrators and analytics consultancies, catalogue and observability vendors, and platform providers.

## Impact If Built
The platform logs every access and nothing assembles it into an account of the estate, so routine questions are answered by asking around. A joined, standing utilisation view is the product the logs have always supported.
