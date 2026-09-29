# Data Platform Integrators

## Profile
**Category:** Digital Professional Services
**Market Size:** ~$18B US in data platform implementation, migration and analytics engineering services around Snowflake, Databricks, BigQuery and the tooling ecosystem surrounding them
**Tech Maturity:** Strong engineering discipline, no usage feedback. These firms have adopted software practices — version control, testing, CI, modular transformation — more thoroughly than most of the analytics world. What they have not adopted is any measurement of whether the assets they build are used, because consumption data lives in the client's platform after the engagement ends.
**Workforce:** Analytics engineers, data platform and infrastructure engineers, data architects, migration specialists, BI developers, delivery leads

## Key Pain Themes
The deliverable is a platform and a model layer, and the measure of success is whether people get answers from it. That measure is not taken. A firm delivers three hundred transformation models and forty dashboards, the engagement closes, and nobody establishes how many of those are ever queried. Practitioners' own experience is that the proportion is low — a small number of assets carry nearly all the use and the rest is inventory — but no firm has quantified it across engagements, so every project keeps building at the same rate.

The second theme is that these platforms decay in a characteristic way. Models accumulate because deleting one requires knowing nothing depends on it; dashboards proliferate because building a new one is faster than finding the existing one; and the model layer's complexity grows until change becomes risky. This is the same accumulation problem that afflicts configured enterprise systems and it arrives faster here.

The third is cost, which in consumption-priced platforms is a direct and visible consequence of how the models are written. A poorly structured transformation layer costs real money every day it runs, and the client discovers it on a bill rather than during delivery.

## Current Tech Landscape
Snowflake, Databricks and BigQuery hold the platform layer, with dbt as the near-universal transformation framework and increasing competition from SQLMesh and platform-native alternatives. Ingestion runs on Fivetran, Airbyte, Stitch or custom pipelines. Orchestration on Airflow, Dagster or Prefect. Observability from Monte Carlo, Bigeye, Elementary and dbt's own tests. Semantic layers from dbt, Cube and the BI vendors. Reverse ETL from Hightouch and Census. Cost management is served by platform-native tooling and specialists like Select and Keebo. Lineage is available in catalogues from Atlan, Alation and Collibra, and is used more for compliance than for pruning.

## Problems
- [[problems/data-platform-integrators/high-impact|🔴 High Impact: Three Hundred Models Delivered and Nobody Counts Which Are Queried]]
- [[problems/data-platform-integrators/low-impact-1|🟡 Low Impact: Pipeline Reliability and Data Quality Monitoring]]
- [[problems/data-platform-integrators/low-impact-2|🟡 Low Impact: Legacy Warehouse and BI Migration]]
- [[problems/data-platform-integrators/worker-life-1|🟢 Worker Life: The Analytics Engineer in the Ticket Queue]]
- [[problems/data-platform-integrators/worker-life-2|🟢 Worker Life: The Platform Engineer on Pipeline Call]]
- [[problems/data-platform-integrators/ml-opportunity|🧠 ML Opportunities]]
- [[problems/data-platform-integrators/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These firms build the systems that other functions use to measure things, and they do not measure their own output. Query logs record every access to every table and dashboard; lineage records what depends on what; cost attribution records what each model costs to run. Joining those three answers the question that governs the whole discipline — which of what we built earns its keep — and it is a report nobody produces. The reason is partly that the data belongs to the client and partly that the answer would show a firm billing to build assets that are never opened, which is uncomfortable for a business model priced by delivery volume. It is also the single most useful thing an integrator could offer, because every mature data platform owner knows their estate is mostly inventory and cannot prove which part.
