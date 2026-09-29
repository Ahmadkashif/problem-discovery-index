# Catching the Change That Passes Every Check

**Niche:** [[niches/data-platform-integrators/semantic-data-quality/profile|Semantic Data Quality]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The rows arrived on time, in the expected volume, and mean something different.
**Tags:** #change-point-detection #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #automation #hypothesis-testing #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to catch the data failures that matter — a field whose meaning changed — when the monitoring watches freshness and volume against thresholds somebody set at deployment.

## The Problem
The expensive data failures are semantic. An upstream team adds a status value, changes how a field is populated, alters a currency convention, or reuses a code for a new purpose. Nothing technical breaks: rows arrive, counts are normal, nulls are within tolerance. The transformation layer processes it faithfully, every downstream number shifts, and the discovery comes weeks later when somebody notices a figure that looks wrong.

## Why Nobody Has Built This
Observability tooling monitors the properties that are easy to define — freshness, volume, nulls — and semantic meaning is not one of them. Thresholds are set once and never revisited. Source teams change things without telling anyone. And the failure is attributed to the data team.

## What to Build
Monitor distributions and category sets rather than counts and timestamps. Monitor the distribution of every meaningful field and alert on a change in shape, which is the core — a semantic change is a distribution change and is invisible to any count-based check. Detect new and disappearing category values, since an added status code is the commonest semantic break and is trivially detectable. Track relationships between fields, as many semantic changes show up as a broken relationship rather than a changed field. Baseline automatically and adapt to legitimate seasonality rather than using a fixed threshold. Assess downstream impact when a change is detected, so the alert states which reports are affected. Establish contracts with source systems covering meaning as well as schema, which is the upstream fix and the harder one. Alert with the evidence — the before and after distribution — rather than a threshold breach, which is what makes an alert actionable. Quarantine or flag the affected downstream outputs rather than publishing quietly. Record every confirmed semantic change with its cause, so the pattern becomes known. And direct the alert to the source team as well as the data team, because that is where the fix is.

## Target Customer
Data platform teams and integrators, data engineering leadership, observability and quality vendors, and platform providers.

## Impact If Built
A semantic change is a distribution change and is invisible to any count-based check, which is what every monitor watches. Distribution and category monitoring with downstream impact catches the failures that actually cost money.
