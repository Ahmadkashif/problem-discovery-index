# Multi-Client Pipeline Health Dashboard for Consulting Firms

**Niche:** [[niches/data-analytics-consultants/data-pipeline-monitoring/profile|Data Pipeline Monitoring & Alerting]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product gives analytics consulting firms a unified view of pipeline health, data freshness, and SLA compliance across all client environments — so data engineers start each day checking 50+ pipelines individually.
**Tags:** #anomaly-detection #tabular-ml #automation #data-integration #ai-platform

## The Problem
A data engineering team at an analytics consulting firm maintains pipelines for 40 clients. Each client has 3-10 pipelines (ETL jobs, dbt models, API ingestions) running on different schedules (hourly, daily, weekly) in different environments (client's AWS, shared Snowflake, on-premises SQL Server). The morning health check requires: logging into each client's Airflow/dbt Cloud/Fivetran dashboard, checking for failed or delayed jobs, verifying data freshness (did yesterday's data load?), and reviewing any anomalies. This takes 1-2 hours daily for an experienced engineer who knows each client's expected patterns. When that engineer is on vacation, the substitute misses issues because they do not know client-specific patterns ("Client X's pipeline always fails on Mondays because their source system runs batch processing — that's normal").

## Why Nobody Has Built This
Monitoring tools are designed for single-tenant deployment. Monte Carlo monitors one organization's data ecosystem. Airflow's UI shows one Airflow instance. Building a multi-client monitoring dashboard requires: connecting to monitoring endpoints across different client environments (different clouds, different tools, different access credentials), normalizing pipeline health signals across different orchestration platforms, and encoding client-specific "normal" patterns that distinguish real failures from expected behaviors.

## What to Build
A consulting firm pipeline operations dashboard that: (1) aggregates pipeline health signals from multiple orchestration platforms (Airflow, dbt Cloud, Fivetran, Prefect) across all client environments via API, (2) displays unified health status with client-specific SLA tracking (Client A requires data freshness within 2 hours, Client B within 24 hours), (3) learns client-specific normal patterns and suppresses known-acceptable behaviors (Monday failures at Client X), (4) escalates based on severity and SLA impact (pipeline delay affecting a C-suite dashboard vs. a rarely-viewed report), and (5) provides on-call routing to the assigned data engineer per client. Replaces the 1-2 hour morning health check with a glanceable dashboard.

## Target Customer
Analytics consulting firms maintaining 20+ active client data pipelines under support contracts, with 2+ data engineers sharing pipeline operations responsibilities.

## Impact If Built
Reduces daily health check from 1-2 hours to 5 minutes. Catches 90% of pipeline issues before the client reports them. Enables consulting firms to scale pipeline support from 20 clients to 50+ clients without adding operations staff. Preserves institutional knowledge about client-specific pipeline behaviors when engineers rotate.
