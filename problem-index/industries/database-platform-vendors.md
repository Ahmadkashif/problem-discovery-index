# Database Platform Vendors

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$25B US database software and managed database services
**Tech Maturity:** Extremely high engineering, extremely low operability — PostgreSQL, MySQL, MongoDB, Snowflake, Databricks, Neon, PlanetScale and the hyperscalers' managed services have made storage and query engines remarkable. Operating one well still requires a specialist most organisations cannot hire.
**Workforce:** Database engineers, support and escalation engineers, performance specialists, solutions architects, migration consultants, storage and query engine developers

## Key Pain Themes
The category's defining gap is that databases fail slowly and visibly only at the end. A query plan flips because statistics drifted, a table's growth crosses a threshold, an index stops being used, connection pooling saturates under a traffic pattern — each degrades gradually and then breaks at the worst moment, usually during a load event. The engines expose enormous diagnostic detail and almost no interpretation, so the knowledge to read it belongs to a shrinking population of specialists. Around that sit two chronic burdens: schema migration on live systems, where the safe procedure is well known and the execution is bespoke and terrifying every time; and connection and resource management, where defaults are wrong for almost every workload and tuning requires understanding the internals. Support engineers spend their days reconstructing what happened from logs, and application developers write queries against a system whose performance behaviour they have no way to predict.

## Current Tech Landscape
PostgreSQL has become the default choice and its ecosystem is enormous; MySQL retains vast installed base; MongoDB serves document workloads; the analytical side is dominated by Snowflake, Databricks and BigQuery. Serverless and branching database products (Neon, PlanetScale) have changed developer expectations about provisioning. Query performance tooling exists (pganalyze, SolarWinds, native performance insights) and is used mainly by specialists. Online schema change tools are mature and require expertise to operate. Vector search capability has been added to nearly every engine.

## Problems
- [[problems/database-platform-vendors/high-impact|🔴 High Impact: Degradation That Is Only Visible at the End]]
- [[problems/database-platform-vendors/low-impact-1|🟡 Low Impact: Schema Migration on Live Systems]]
- [[problems/database-platform-vendors/low-impact-2|🟡 Low Impact: Connection and Resource Configuration]]
- [[problems/database-platform-vendors/worker-life-1|🟢 Worker Life: Support Engineer Reconstructing the Incident]]
- [[problems/database-platform-vendors/worker-life-2|🟢 Worker Life: The Developer Writing Queries Blind]]
- [[problems/database-platform-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/database-platform-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Managed database vendors observe query workloads, schemas, access patterns and failures across enormous numbers of production systems. The same anti-patterns recur constantly — the query that will not scale past a data volume, the index that stops being selective, the migration that will lock a large table, the connection pattern that exhausts a pool — and each customer discovers them independently, usually during an outage. The corpus that would let a vendor warn before rather than diagnose after exists in the fleet and is used for capacity planning.
