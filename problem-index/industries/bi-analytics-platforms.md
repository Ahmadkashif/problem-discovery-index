# BI & Analytics Platforms

## Profile
**Category:** Horizontal SaaS
**Market Size:** ~$16B US business intelligence and analytics software
**Tech Maturity:** Mature and structurally unresolved — Power BI, Tableau, Looker, Sigma, ThoughtSpot and Omni have made visualisation and self-service ubiquitous. Every organisation that adopted them has arrived at the same place: many dashboards, several definitions of revenue, and an analyst answering questions in Slack because nobody trusts the dashboards.
**Workforce:** Analytics engineers, BI developers, data analysts, semantic layer owners, data platform engineers, implementation consultants

## Key Pain Themes
Self-service analytics created a definition problem it has never solved. Three dashboards report active users and give three numbers, each defensible, each computed slightly differently, and the meeting that discovers this spends its time reconciling rather than deciding. The semantic layer was invented to fix it and is adopted partially, so the drift continues in the parts nobody governed. Alongside it sits dashboard sprawl — thousands of assets, most unopened for a year, none deletable because someone might use them — and data quality alerting that either fires constantly or not at all, because thresholds are set by hand on pipelines whose normal behaviour nobody characterised. The analysts are the release valve for all of it: they answer ad hoc questions all day precisely because the self-service tooling did not deliver self-service, and the data engineers spend their nights on pipeline pages that repeat.

## Current Tech Landscape
Power BI dominates by distribution through Microsoft's estate; Tableau retains the analyst loyalty it earned; Looker's semantic modelling was influential and is now widely imitated; Sigma and Omni compete on warehouse-native interaction. dbt reshaped transformation and brought definitions into version control, which is the most substantive progress the space has made. Data observability vendors (Monte Carlo, Bigeye, Metaplane) emerged specifically because pipelines fail silently. Natural language querying has been promised for a decade and is now genuinely arriving, which raises the definition problem rather than resolving it.

## Problems
- [[problems/bi-analytics-platforms/high-impact|🔴 High Impact: Metric Definition Drift]]
- [[problems/bi-analytics-platforms/low-impact-1|🟡 Low Impact: Dashboard Sprawl and Certification]]
- [[problems/bi-analytics-platforms/low-impact-2|🟡 Low Impact: Data Quality Alerting]]
- [[problems/bi-analytics-platforms/worker-life-1|🟢 Worker Life: Analyst Ad Hoc Request Queue]]
- [[problems/bi-analytics-platforms/worker-life-2|🟢 Worker Life: Data Engineer on the Pipeline Page]]
- [[problems/bi-analytics-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/bi-analytics-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms hold the complete record of how an organisation asks questions about itself: every query, every dashboard, every filter, every drill-down, by whom and how often. That is a map of what the business actually cares about and where its understanding is confused — the same question asked eleven ways, the metric that four teams compute differently, the dashboard that everyone opens and nobody trusts. The category renders charts and never analyses the asking, which is the one dataset it uniquely holds.
