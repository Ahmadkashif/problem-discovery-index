# Metric Definition Drift

**Parent Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to guarantee that two things called revenue are the same number, and to detect it from the query logic when they are not — and whoever does that takes the account, because the meeting that reconciles instead of deciding is the category's most visible failure.

## Profile
**Market Size:** ~$3.2B US semantic layer, metrics governance and definition management
**Share of Parent Industry:** ~20% of category revenue
**Digital Adoption:** Medium — semantic layers are widely bought and partially adopted
**Target Buyer:** Heads of data, analytics engineering leads, finance
**Automation Potential:** Very High — every definition exists as query logic the platform already stores

## What Makes This a Distinct Niche
Three dashboards report active users. One counts anyone with a session, one excludes internal accounts, one uses a trailing thirty-day window. Each is defensible, each was built by someone who thought about it, and the meeting that surfaces all three spends its hour reconciling rather than deciding. This is the oldest complaint in business intelligence and the one self-service made worse, since the point of self-service was to let people build their own things and the consequence is that they did. The semantic layer was invented as the answer and is adopted in patches — the governed models cover what someone got round to modelling, and everything else drifts freely in dashboards, saved queries, spreadsheets and notebooks. What makes this a distinct contest is that divergence is detectable without governance: the SQL behind every dashboard is stored, the filters are explicit, and two definitions of the same-named metric differ in ways a comparison can find. The category has the evidence and produces the argument instead.

## Current Tools & Gaps
Semantic layers inside the major platforms, dbt's metrics and model layer, headless metrics stores, certification badges, and data catalogues with business glossaries. The gaps: adoption of any semantic layer is partial by nature and the ungoverned remainder is where the drift lives, so a product that only governs cannot detect; nothing compares definitions to each other, so divergence is discovered in a meeting rather than in a report; the glossary states what a metric should mean and is disconnected from what the queries actually do; and lineage stops at the table rather than reaching the definition, so nobody can answer which assets compute revenue in which of the four ways.

## Problems
- [[niches/bi-analytics-platforms/metric-definition-drift/build|🔨 Build: Three Dashboards, Three Numbers, All Defensible]]
- [[niches/bi-analytics-platforms/metric-definition-drift/buy|🛒 Buy: Program Analysis Applied to the Query Estate]]
- [[niches/bi-analytics-platforms/metric-definition-drift/fix|🔧 Fix: The Glossary Nobody Connected to the Queries]]
