# Stale Rightsizing Recommendations

**Niche:** [[niches/cloud-infrastructure-consultants/multi-cloud-cost-optimizers/profile|Multi-Cloud Cost Optimizers]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Rightsizing reports generated monthly become outdated within days as workload patterns shift, leaving 60% of recommendations unactioned by the time the next review cycle begins.
**Tags:** #time-series-forecasting #anomaly-detection #tabular-ml #quick-win #automation

## The Problem
Consultants generate rightsizing reports showing oversized or undersized instances, typically on a monthly cadence. But cloud workloads change weekly — new deployments, traffic spikes, application refactoring — so by the time a client's engineering team reviews the report, many recommendations are no longer valid. Engineers lose trust in the reports and stop acting on them, undermining the consultant's value proposition.

## Why It's Still Broken
Rightsizing analysis requires combining CPU, memory, network, and disk utilization data over multiple time horizons, then comparing against the provider's current instance catalog (which also changes). Most consultants use point-in-time snapshots rather than continuous monitoring because the data pipeline to process utilization metrics in near-real-time across thousands of instances is expensive to build and maintain. The economics of monthly engagements don't justify the infrastructure investment.

## What a Fix Looks Like
A continuous rightsizing engine that processes utilization telemetry in near-real-time, detects when a recommendation's underlying data has changed, and auto-expires stale recommendations while surfacing new ones. Recommendations are delivered as a living dashboard with confidence scores that decay over time, rather than as a static PDF report. Engineers see only actionable, current recommendations.

## Who Feels the Pain
Cloud engineers who receive monthly PDFs with 200 rightsizing recommendations, knowing that 40% are already irrelevant but having no way to tell which ones.

## Impact If Fixed
Increases recommendation adoption rate from 25% to 65%, delivering an additional 10-15% cost savings per client and reducing consultant time spent on stale-data cleanup by 8 hours/month.
