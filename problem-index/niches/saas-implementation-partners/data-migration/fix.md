# Discovering the Duplicates at Cutover

**Niche:** [[niches/saas-implementation-partners/data-migration/profile|Data Migration]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Fix (Pain Point)
**One-liner:** The load fails on cutover weekend because the source has thousands of duplicate records nobody profiled.
**Tags:** #quick-win #data-integration #descriptive-statistics #evaluation-metrics #automation #k-nearest-neighbors #workflow-orchestration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to move a client's data into a new platform without discovering its quality problems during cutover weekend — and whoever automates that takes the account.

## The Problem
Cutover weekend is when the data's real state becomes apparent. Duplicates that the source system tolerated, mandatory fields that are empty in a third of records, references pointing at records that no longer exist. The load fails or completes with errors, and a team that planned a weekend spends it triaging data quality with the client's business waiting to resume on Monday.

## Why It's Still Broken
Nobody profiled the source early — a data quality problem that is only discovered when the load runs will always be discovered at the worst possible moment, because the load is deliberately scheduled last. Source access arrives late. Profiling is not a scoped task. And the client believes their data is fine.

## What a Fix Looks Like
Profile early, rehearse fully and stop discovering at cutover. Profile the source in the first weeks and report the findings to the client, which is the fix and is a day's work with commodity tooling. Count duplicates, empty mandatory fields and broken references specifically, since those three account for most cutover failures. Agree who remediates what, and when, as a scoped item rather than an assumption. Run a full-volume rehearsal load rather than a sample, because problems scale non-linearly and a sample hides them. Rehearse more than once, with the errors fixed between runs. Time the rehearsal and plan the window from it rather than from an estimate. Reconcile automatically after each rehearsal so the checks are proven before they matter. Freeze the source earlier than feels necessary, which removes a whole class of last-minute divergence. Keep a rollback plan that has actually been tested. And publish the data quality findings to the client early, which converts a project failure into a shared task.

## Who Feels the Pain
Delivery teams triaging data on a weekend; clients whose business cannot resume on Monday; consultants blamed for the state of data they did not create; and the go-live date.

## Impact If Fixed
A data quality problem discovered only when the load runs will always be discovered at the worst possible moment, because the load is scheduled last. A day of profiling in week one moves it to where it can be scoped and remediated.
