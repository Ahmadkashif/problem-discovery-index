# Data Pipeline Monitoring & Alerting

**Parent Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1.8B (internal spend)
**Share of Parent Industry:** N/A (operational cost, not revenue)
**Digital Adoption:** Medium — Consultants build pipelines with Airflow, dbt, and Fivetran but monitor them through manual checks, Slack alerts for failures, and periodic "is the dashboard still updating?" reviews.
**Target Buyer:** Data engineers and pipeline operations leads at analytics consulting firms who maintain client data pipelines post-deployment.
**Automation Potential:** Very High — Pipeline health monitoring follows deterministic patterns: did the job run? Did it complete? Did the output data meet quality thresholds? Did row counts change within expected ranges?

## What Makes This a Distinct Niche
Analytics consultants build data pipelines for clients, then maintain them under support contracts. A mid-size consulting firm maintains 50-100 active client pipelines simultaneously, each with different schedules, data sources, quality expectations, and failure modes. When a pipeline breaks (source API changed, data volume spike exceeded memory, upstream system pushed bad data), the consultant discovers it through: the client calling to report stale dashboards (worst case), a Slack alert from Airflow (better case), or a morning check of pipeline status across all clients (common case). Proactive, intelligent monitoring across all client pipelines — detecting not just failures but anomalies, data quality degradation, and performance trends — would prevent 80% of client-reported issues.

## Current Tools & Gaps
Airflow and dbt provide job-level monitoring (pass/fail, run duration). Monte Carlo, Great Expectations, and Soda provide data quality monitoring. But these tools are designed for single-organization deployment — they do not support the multi-client, multi-pipeline portfolio management workflow of a consulting firm. No tool provides a unified view across 50+ client pipelines with client-specific SLAs, quality thresholds, and escalation rules.

## Problems
- [[niches/data-analytics-consultants/data-pipeline-monitoring/build|🔨 Build: Multi-Client Pipeline Health Dashboard for Consulting Firms]]
- [[niches/data-analytics-consultants/data-pipeline-monitoring/buy|🛒 Buy: Data Quality Monitoring Across Client Portfolios]]
- [[niches/data-analytics-consultants/data-pipeline-monitoring/fix|🔧 Fix: Silent Pipeline Failures]]
