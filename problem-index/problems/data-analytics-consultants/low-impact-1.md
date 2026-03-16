# Client Dashboard Templating Engine

**Industry:** [[data-analytics-consultants|Data Analytics Consultants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Dashboard creation tools exist for every BI platform, but none can take a consultant's analytical intent and a client's specific schema and auto-generate a working, styled, filterable dashboard without hours of manual widget configuration.
**Tags:** #llm #text-generation #nlp #automation

## The Problem
Analytics consultants build dashboards for every engagement — executive KPI views, operational monitoring panels, ad-hoc exploration interfaces. Each dashboard requires mapping the client's specific column names to visual components, configuring filters and drill-downs for the client's organizational hierarchy, applying the client's branding, and wiring up cross-filtering logic between charts. A consultant who built a nearly identical churn analysis dashboard for three SaaS clients last quarter still starts from scratch each time because the underlying schemas, naming conventions, and BI platform versions differ just enough to prevent direct reuse.

## What Already Exists
Tableau, Looker, Power BI, and Metabase all provide template and theming capabilities. Looker's LookML allows parameterized models. Tableau has starter workbooks. Power BI offers template apps. These tools handle visual formatting and layout reuse, but they do not solve the semantic mapping problem: given a new client's schema, they cannot automatically determine that `cust_churn_dt` maps to the "Churn Date" dimension in the template, or that the client's fiscal year starts in April and all YTD calculations need adjustment.

## The Customisation Gap
The missing layer is a schema-aware semantic mapper that understands analytical intent. A consultant should be able to say "build a churn analysis dashboard" and have the system: (1) identify which tables and columns in the client's warehouse correspond to the required metrics, (2) infer the correct aggregation logic and time grains, (3) handle client-specific naming and organizational hierarchies, and (4) generate the dashboard definition in the target BI platform's native format. This requires NLP understanding of both the analytical template and the client's data dictionary, plus code generation for the specific BI platform's API or definition language.

## Impact If Solved
Dashboard creation time drops from 8-20 hours per engagement to 1-3 hours of review and refinement, freeing consultants to focus on insight generation rather than widget configuration. Firms can serve more clients simultaneously without adding headcount to the visualization team.
