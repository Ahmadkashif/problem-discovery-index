# Silent Pipeline Failures

**Niche:** [[niches/data-analytics-consultants/data-pipeline-monitoring/profile|Data Pipeline Monitoring & Alerting]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Pipelines that succeed technically but produce wrong data are the most damaging failure mode — the job ran, no errors were thrown, but the source system returned empty results, stale data, or truncated records, and nobody noticed for days or weeks.
**Tags:** #anomaly-detection #change-point-detection #tabular-ml #quick-win

## The Problem
A client's daily Salesforce-to-Snowflake pipeline runs every night at 2 AM. On Tuesday, Salesforce's API rate limit changed, causing the pipeline to return only 500 records instead of the usual 50,000. The pipeline completed successfully — no errors, no timeouts. The resulting dashboard showed revenue dropping 99%, which the client noticed... three days later, on Friday morning. The consulting firm spent the weekend in emergency mode: reloading data, reconciling three days of bad reports, and explaining to the client why their board received incorrect financial data. Silent failures — pipelines that succeed but produce wrong data — are more damaging than hard failures because they go undetected.

## Why It's Still Broken
Pipeline orchestrators (Airflow, Prefect) monitor job success/failure, not output correctness. Data quality tests (Great Expectations) validate schema and basic rules but require explicit test definitions for each expected behavior. Nobody writes a test for "row count should be within 20% of yesterday's row count" on every table in every pipeline — it is not part of the standard pipeline development checklist. Silent failures require behavioral monitoring (comparing today's output to yesterday's output) rather than rule-based monitoring (checking if column X is not null), and this behavioral monitoring is not standard practice.

## What a Fix Looks Like
An output-comparison monitoring layer that: (1) captures key metrics for every pipeline run (row count per table, null count per column, min/max/mean of numeric columns, distinct count of categorical columns), (2) compares each run's metrics to the trailing 30-day baseline, (3) flags anomalies that exceed configurable thresholds ("row count dropped 95% — expected 50,000, got 500"), (4) distinguishes between expected variation (weekend data is always 40% lower) and unexpected anomalies (Monday data dropped 90% — never seen before), and (5) sends alerts with context ("Pipeline X completed successfully but output row count is 99% below baseline — likely source API issue"). Deploys as a post-pipeline step requiring zero custom test writing.

## Who Feels the Pain
Data engineers who discover silent failures only when clients report incorrect dashboards, and clients who lose trust in analytics when bad data goes undetected for days.

## Impact If Fixed
Catches 90% of silent pipeline failures within 1 hour of occurrence, reducing client-reported data issues by 80%. Prevents the most damaging analytics consulting scenario — "your dashboard showed wrong numbers and we didn't know for 3 days." Deploys in minutes per pipeline, requiring no custom test writing.
