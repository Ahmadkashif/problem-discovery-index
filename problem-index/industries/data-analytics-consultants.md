# Data Analytics Consultants

## Profile
**Category:** Technology
**Market Size:** ~$30B US data analytics consulting and services
**Tech Maturity:** High on tooling (Snowflake, dbt, Tableau, Looker, Power BI, BigQuery), Low on project operations — most firms still scope engagements on gut feel, track utilization in spreadsheets, and hand off deliverables as static slide decks or ad-hoc notebooks.
**Workforce:** Data analysts, data engineers, visualization specialists, project managers, account managers, principals

## Key Pain Themes
The defining bottleneck is not analysis — it is everything surrounding analysis. Consultants spend 60-80% of engagement hours cleaning data, debugging joins, reverse-engineering undocumented schemas, and reconciling conflicting source-of-truth tables before a single insight is produced. Client data arrives in wildly inconsistent formats: CSV dumps with mixed encodings, API exports missing fields, warehouse tables with implicit business logic baked into column names only the original engineer understood. Once analysis is complete, the handoff problem begins — dashboards built for one client's Looker instance cannot be reused for the next client's Tableau setup, documentation is written retroactively (if at all), and institutional knowledge about data quality gotchas walks out the door when an analyst rolls off a project. Utilization tracking, project scoping, and engagement health monitoring remain manual processes that principals manage through weekly status calls and gut instinct.

## Current Tech Landscape
The analytics toolchain itself is mature — Snowflake/BigQuery for warehousing, dbt for transformation, Tableau/Looker/Power BI for visualization, Python/R for statistical work. What is missing is the operational layer: most firms use a patchwork of Harvest/Toggl for time tracking, Google Sheets for project planning, Slack threads for data quality issue tracking, and tribal knowledge for scoping new engagements. Tools like Monte Carlo and Great Expectations address data observability but require dedicated setup per client environment and are rarely deployed on short consulting engagements. No tool exists that learns from a consultant's pattern of data investigation and accelerates the next engagement.

## Problems
- [[problems/data-analytics-consultants/high-impact|🔴 High Impact: Data Quality Assessment Autopilot]]
- [[problems/data-analytics-consultants/low-impact-1|🟡 Low Impact: Client Dashboard Templating]]
- [[problems/data-analytics-consultants/low-impact-2|🟡 Low Impact: Data Lineage Documentation Generator]]
- [[problems/data-analytics-consultants/worker-life-1|🟢 Worker Life: SQL/Python Debugging on Messy Data]]
- [[problems/data-analytics-consultants/worker-life-2|🟢 Worker Life: Utilization Pressure and Bench Anxiety]]
- [[problems/data-analytics-consultants/ml-opportunity|🔵 ML Opportunities]]
- [[problems/data-analytics-consultants/ai-agents-platforms|🤖 AI Agents & Platforms]]
