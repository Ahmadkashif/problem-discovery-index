# Nobody Knows Which Spreadsheets Depend on That Column

**Niche:** [[niches/bi-analytics-platforms/spreadsheet-last-mile/profile|The Spreadsheet Last Mile]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A data team renames a column after checking every dashboard, and breaks forty spreadsheets nobody could enumerate, which surfaces one at a time over the following fortnight.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #quick-win #automation
**Contested on:** Every serious competitor here is fighting to make the spreadsheet a governed, refreshable surface on the warehouse rather than a dead export — and whoever does that takes the finance account, because finance will not stop using spreadsheets and every vendor has spent fifteen years pretending otherwise.

## The Problem
A model is refactored and a column is renamed. The data team does the responsible thing: checks lineage, updates the dependent models, verifies the dashboards, announces the change. Two days later finance's weekly pack fails, then a regional sales file, then the commission calculation. Forty spreadsheets pulled from that column through a connector or a scheduled extract, and no lineage tool knows they exist, because lineage stops where the platform's boundary is and the work continues past it.

## Why It's Still Broken
Lineage products model warehouses, transformation code and BI assets, and stop there — the spreadsheet is outside the perimeter by convention. Connections from spreadsheets are frequently made through personal credentials and ad hoc connectors, so they are invisible to central tooling. And the breakage is absorbed by the person whose file broke, who fixes it locally and does not report it, which means the data team never learns the true blast radius of anything they do.

## What a Fix Looks Like
Extend the inventory past the boundary. Log connector and extract activity by source object, which most platforms already record and none surfaces as dependency — that alone produces most of the map. Scan the document estate for workbooks containing warehouse connections and register them, which is a discovery job over shared drives and cloud storage, run periodically. Build the dependency edges from those sheets to the objects they read, and include them in impact analysis so a proposed change lists the affected spreadsheets and their owners alongside the affected dashboards. Notify those owners ahead of a change rather than letting them discover it, which is the entire practical benefit and costs nothing once the map exists. And report the shape of the estate — how many sheets depend on each object, how many are actively refreshed, how many have a single owner who has left — which typically reveals a dependency structure the data team did not know they had.

## Who Feels the Pain
Finance and operations analysts whose files break without warning; data engineers who verified everything they could see and broke things they could not; and organisations whose reporting depends on a dependency graph nobody has drawn.

## Impact If Fixed
The connector logs already exist and surfacing them as dependency is a reporting change rather than a new capability. Notifying spreadsheet owners before a change converts a recurring fortnight of silent breakage into an email, and the estate shape is usually a surprise worth having.
