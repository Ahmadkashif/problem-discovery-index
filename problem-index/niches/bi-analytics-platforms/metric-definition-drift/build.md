# Three Dashboards, Three Numbers, All Defensible

**Niche:** [[niches/bi-analytics-platforms/metric-definition-drift/profile|Metric Definition Drift]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Divergent metric definitions are discovered in the meeting they ruin, and the query logic that differs is sitting in the platform's own metadata, comparable automatically.
**Tags:** #graph-theory #word-embeddings #bert #k-means-clustering #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to guarantee that two things called revenue are the same number, and to detect it from the query logic when they are not — and whoever does that takes the account, because the meeting that reconciles instead of deciding is the category's most visible failure.

## The Problem
A quarterly review opens with three slides showing active users. The numbers differ by eleven percent. Forty minutes go to establishing which is right, which ends inconclusively because all three are right under their own definition. The underlying facts — that one excludes internal domains, one counts sessions rather than users, one uses a different window — are three lines of SQL apart, stored in the same platform, and were never compared because nothing compares them. The same discovery is made again the following quarter by different people.

## Why Nobody Has Built This
Platforms treat each asset as independent: a dashboard is a document, and nobody asked what a library of documents says collectively. The semantic layer approach took the opposite and more ambitious route — govern everything so drift cannot occur — which works for what it covers and leaves the rest untouched, and the rest is most of it. Detection also requires parsing and normalising SQL across dialects and comparing the resulting logic semantically rather than textually, which is more work than a dashboard feature justifies but far less than it appears, given mature parsing tooling. And the problem is experienced by executives in meetings rather than by the platform's users, so it never enters the product backlog through the usual door.

## What to Build
Definition comparison across the whole estate, governed or not. Parse every query behind every dashboard, saved report and scheduled extract into a normalised representation — the source tables, the joins, the filters, the aggregation, the time grain. Group assets that claim to compute the same business concept, using the metric names, the column aliases and the surrounding text, since the name is the claim being made. Compare the normalised logic within each group and report the differences in business terms rather than as a SQL diff: this one excludes internal accounts and that one does not; this one is monthly and that one is trailing thirty days. Rank by consequence — divergence in a metric on an executive dashboard matters more than in an analyst's scratch report — because a report of four hundred divergences is ignored and a report of the nine that reach leadership is acted on. Then track drift over time, so a definition that changes in one asset and not in its siblings is flagged when it happens rather than in the next quarterly review. Where a semantic layer exists, use it as the reference definition and report deviation from it; where it does not, the comparison still works, which is the point.

## Target Customer
Heads of data and analytics engineering leads at organisations past the first few hundred assets, finance functions who carry the consequence of divergence, and the BI vendors themselves, for whom this is a defensible differentiator in a category competing on visualisation.

## Impact If Built
This is the industry's most recognisable failure and the evidence for it is fully present in every platform's own metadata. Detection works without governance, which is what makes it deliverable to the ninety percent of the estate a semantic layer will never cover.
