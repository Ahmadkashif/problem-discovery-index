# The Sync That Has Been Failing Since Tuesday

**Niche:** [[niches/revops-consultancies/revenue-systems-sync/profile|Revenue Systems Sync]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Fix (Pain Point)
**One-liner:** A connector has been silently dropping a subset of records for three weeks and the first sign was a number that looked wrong.
**Tags:** #quick-win #automation #data-integration #change-point-detection #evaluation-metrics #workflow-orchestration #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to keep CRM, marketing automation, quoting and finance in agreement about the same accounts and deals, and whoever automates that reconciliation takes the account.

## The Problem
Integrations fail partially and quietly. A validation rule changes and a subset of records stops syncing; an API limit is hit and a batch is skipped; a field mapping breaks and values arrive empty. The job reports success because most records went through. Nobody notices until a report looks wrong, by which time weeks of records are missing and reconstructing what happened is archaeology.

## Why It's Still Broken
Monitoring watches jobs rather than records — an integration that succeeds on ninety-eight percent of records reports success, and the two percent are invisible until they matter. Error logs are not read. Nobody owns sync health. And the discrepancy is absorbed during reporting.

## What a Fix Looks Like
Count records on both sides, which is the simplest possible check. Compare record counts between systems daily and alert on divergence, which is the fix and takes an afternoon. Report failed records with the reason rather than a job status, since the reason is usually specific and fixable. Alert on a sudden change in sync volume, as that is the signature of a partial failure. Check key fields for emptiness after sync, which catches broken mappings that counts do not. Assign an owner for sync health with the alerts routed to them. Retry and queue failed records rather than dropping them, which many connectors do not do by default. Keep a log of failures so recurring causes are visible. Reconcile fully on a schedule rather than only when something looks wrong. Test integrations after any platform release, since that is when mappings break. And surface sync health where the analyst assembling reports can see it, so an odd number has an explanation available.

## Who Feels the Pain
Analysts reconciling differences with no cause available; leaders acting on reports missing weeks of records; administrators doing archaeology on a three-week-old failure; and everyone's confidence in the numbers.

## Impact If Fixed
An integration that succeeds on ninety-eight percent of records reports success, and the two percent are invisible until they matter. A daily record count comparison is an afternoon of work against weeks of silent loss.
