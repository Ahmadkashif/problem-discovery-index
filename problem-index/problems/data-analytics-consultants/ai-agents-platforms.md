# AI Agents & Platform Opportunities — Data Analytics Consultants

**Industry:** [[data-analytics-consultants|Data Analytics Consultants]]

---

## 1. Data Quality Agent
#ai-agent #anomaly-detection #automation #data-integration

**Concept:** An autonomous agent that connects to a client's data warehouse at engagement kickoff, runs a comprehensive profiling and quality assessment, and produces an annotated data quality report within hours — not the days or weeks it currently takes an analyst to do manually. The agent profiles every table and column, tests join relationships for fan-outs and data loss, identifies columns with implicit business logic (e.g., encoded status codes, overloaded fields), detects stale or orphaned tables, and ranks all findings by likely impact on downstream analysis. It operates continuously during the engagement, monitoring for data drift or upstream changes that could invalidate the consultant's work.

**Inputs:** Database connection credentials (read-only), optional context on the engagement scope (e.g., "we are analyzing customer churn for a SaaS company"), previous engagement profiles if the firm has worked with this client before.

**Outputs / Actions:** A structured data quality report with: per-column quality scores and issue descriptions, join relationship map with risk annotations, a prioritized investigation checklist for the analyst, automated dbt test suggestions for critical quality checks, and ongoing alerts if data distributions shift during the engagement. The report is generated in Markdown for Notion/Confluence and as an interactive notebook for Jupyter/Hex.

**Why now:** LLMs can now parse schema metadata and generate natural-language explanations of data quality issues that are genuinely useful (not just restating statistics). Cheap inference means profiling can run iteratively — the agent can form hypotheses about data issues and test them by running sample queries, mimicking how a human analyst investigates. Vector databases enable the agent to learn from prior engagements and recognize patterns across clients.

**Market:** Every analytics consulting firm with 10+ analysts ($5-15K/year per seat). Secondary market: in-house analytics teams at mid-market companies. Estimated addressable market of $500M-$1B given the hours currently burned on manual data profiling.

---

## 2. Dashboard Builder Agent
#ai-agent #llm #text-generation #automation

**Concept:** An agent that takes a natural-language description of the desired analytical view (e.g., "monthly recurring revenue by customer segment with churn overlay and cohort retention curves"), connects to the client's data warehouse, identifies the relevant tables and columns, writes the necessary SQL transformations, and generates a complete, interactive dashboard in the client's BI platform of choice (Tableau, Looker, Power BI, Metabase). The agent handles the semantic mapping between analytical concepts and the client's specific schema, applies appropriate aggregation logic, and configures cross-filtering and drill-down behavior.

**Inputs:** Natural-language dashboard specification from the consultant, database connection, target BI platform and version, optional style/branding guidelines (colors, fonts, logo), and optional reference dashboards from previous engagements.

**Outputs / Actions:** A fully functional dashboard definition file (Tableau .twb, LookML files, Power BI .pbix, or Metabase API payload) with all data connections configured, filters wired, and visualizations styled. The agent also generates a brief documentation page explaining the dashboard's data sources, transformation logic, and refresh schedule. If the agent encounters ambiguity (e.g., multiple possible "revenue" columns), it asks the consultant for clarification before proceeding.

**Why now:** LLMs with large context windows can process full schema definitions and generate syntactically correct SQL, LookML, and Tableau calculations. BI platforms have increasingly robust APIs (Tableau REST API, Looker API, Power BI REST API) that allow programmatic dashboard creation. The combination means an agent can go from intent to deployed dashboard without the consultant manually configuring widgets.

**Market:** Analytics consulting firms and freelance analysts who build 5-20 dashboards per month. Pricing at $200-500/month per seat targets the 50,000+ analytics consultants in the US. Adjacent market: internal BI teams at companies with 100-1,000 employees who lack dedicated dashboard developers.

---

## 3. Project Scoping Agent
#ai-agent #ai-platform #revenue-impact #workflow-orchestration

**Concept:** An agent that assists principals and account managers in scoping new analytics engagements by analyzing the prospective client's data environment, comparing it to historical engagements, and generating a detailed scope document with effort estimates, risk factors, and recommended team composition. The agent conducts a preliminary data assessment (with client permission), maps the requested deliverables to its knowledge of similar past projects, identifies potential scope risks (e.g., "their data warehouse has 47 tables with no documentation — expect 2x the usual data profiling effort"), and produces a draft SOW with phase-by-phase timelines and confidence intervals.

**Inputs:** Client RFP or meeting notes describing the engagement objectives, access to the client's data warehouse (or a schema export if direct access is not yet available), the consulting firm's historical engagement database (anonymized), and the firm's current staffing availability and skill matrix.

**Outputs / Actions:** A draft Statement of Work (SOW) including: engagement phases with hour estimates and confidence intervals, recommended team composition (by role and seniority), identified risks with mitigation strategies, data readiness assessment, and a proposed timeline. The agent also generates a "scope risk score" that flags engagements likely to overrun and explains why. For proposals, it generates a client-facing executive summary that translates the technical scope into business terms.

**Why now:** LLMs can now parse unstructured RFPs and meeting notes to extract analytical requirements with high accuracy. Historical engagement data, when structured, provides a rich training set for effort estimation that was previously locked in principals' heads. The agent's ability to perform a preliminary data assessment (even from a schema export) adds a data-driven rigor to scoping that was previously impossible before the engagement started.

**Market:** Analytics consulting firms with $5M+ annual revenue where principals spend 10-20 hours per week on scoping and proposals. Pricing as a platform ($1,000-3,000/month per firm) targeting the estimated 5,000-10,000 analytics consulting firms in the US with 10+ employees. The ROI is immediate: a single engagement scoped more accurately pays for a year of the platform.
