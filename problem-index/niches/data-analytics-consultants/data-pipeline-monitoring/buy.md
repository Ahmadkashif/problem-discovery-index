# Data Quality Monitoring Across Client Portfolios

**Niche:** [[niches/data-analytics-consultants/data-pipeline-monitoring/profile|Data Pipeline Monitoring & Alerting]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Great Expectations and Monte Carlo monitor data quality within a single organization's warehouse, but analytics consultants need to monitor quality across 30+ client warehouses with client-specific quality rules and thresholds without deploying a separate instance per client.
**Tags:** #anomaly-detection #tabular-ml #data-integration #automation

## The Problem
A consulting firm delivers a data warehouse to a client, deploys Great Expectations data quality tests, and moves on. Six months later, the quality tests start failing because: a source system changed its date format, a new product category was added that breaks a validation rule, or data volume grew beyond what the quality thresholds expected. The consulting firm discovers this when the client reports: "our dashboard numbers look wrong." The firm has 30 such clients, each with their own Great Expectations deployment, and no way to monitor quality test results across all of them. The firm's data engineers would need to log into 30 separate quality monitoring interfaces daily.

## What Already Exists
Great Expectations provides data quality testing with customizable expectations (column not null, value within range, referential integrity). Monte Carlo provides anomaly detection for data observability. Soda provides data quality checks as a service. All of these are designed for single-organization deployment — one instance per data warehouse. None provide a multi-tenant view where a consulting firm can monitor quality results across all client deployments from a single interface.

## The Customization Gap
The tool needs: (1) a multi-tenant quality monitoring layer that ingests test results from multiple Great Expectations/Soda/dbt test deployments across client environments, (2) client-specific quality thresholds (Client A tolerates 2% null rate in email fields, Client B requires 0%), (3) quality trend analysis across time (is this client's data quality degrading gradually, or was this a sudden break?), (4) cross-client quality pattern detection ("3 clients using the same Salesforce connector all showed increased null rates this week — probable connector issue"), and (5) client-facing quality scorecards that the consulting firm can share as part of their ongoing support service.

## Target Customer
Analytics consulting firms maintaining data warehouse quality for 15+ clients under ongoing support contracts, using Great Expectations, Soda, or dbt tests for quality validation.

## Impact If Solved
Catches data quality issues 2-5 days before clients report them. Reduces quality-related emergency troubleshooting by 70%. Enables consulting firms to offer proactive data quality monitoring as a premium ongoing service ($1K-$3K/month per client). Identifies cross-client quality patterns that reveal systemic issues (shared source system problems, connector bugs).
