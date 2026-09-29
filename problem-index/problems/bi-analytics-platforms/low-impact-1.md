# Dashboard Sprawl and Certification

**Industry:** [[bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Certification badges, folders and workspace governance ship in every platform, and organisations still have eleven thousand dashboards of which four hundred are opened in a month and none can be deleted.
**Tags:** #bert #word-embeddings #dbscan #k-means-clustering #gradient-boosting #evaluation-metrics #automation

## The Problem
Self-service analytics succeeded at its stated goal: anyone can build a dashboard. The consequence is that everyone did, for years, and nothing was ever removed.

A mature deployment holds thousands of dashboards and tens of thousands of underlying queries. Most are opened rarely or never. Many are near-duplicates built because someone could not find an existing one. A significant number are broken — pointing at deprecated tables, filtered to a date range that ended two years ago, or silently returning zero rows.

Nobody deletes anything. The reason is entirely rational: deleting something someone depends on is a visible failure, and keeping it costs nothing visible. So the estate grows monotonically, discovery becomes impossible, and the impossibility of discovery causes more duplicates.

Certification was the category's answer — mark the trustworthy ones. It requires someone to certify, certification goes stale, and the uncertified majority remains, which means a user searching still cannot tell what to trust.

## What Already Exists
Certification and endorsement features exist in Power BI, Tableau and Looker. Workspace and folder governance is standard. Usage analytics are available in every platform, showing views by asset. Lineage tools trace dependencies. Data catalogues (Alation, Collibra, Atlan) provide discovery and documentation layers.

## The Customisation Gap
Usage data exists and is not acted upon. The platforms report views per dashboard and never propose the obvious consequence — that an asset unopened in twelve months, with no downstream dependency, is a deletion candidate. Automating the identification, with a reversible archive rather than a delete, removes the risk that keeps everything alive.

Duplicate detection is absent and is straightforward. Dashboards computing the same fields over the same tables with the same filters are near-identical, and clustering by query semantics reveals them immediately.

Brokenness detection is the third and most valuable gap. An asset that silently returns zero rows, or whose underlying table was deprecated, is actively harmful because someone may still be reading it. This is mechanically detectable and no platform reports it.

Certification should follow evidence rather than volunteers. An asset that is widely used, built on governed sources, consistent with the canonical metric definitions and not broken has earned a provisional trust badge that no human had to award — and the ones that fail those checks are exactly the list a governance team should work.

## Impact If Solved
Dashboard sprawl is why self-service analytics degrades into a search problem, and the fear of deleting is why it is monotonic. Evidence-based archival, duplicate detection and brokenness checks make the estate manageable using telemetry every platform already collects.
