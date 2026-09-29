# Finding the Data Problems in Week One

**Niche:** [[niches/saas-implementation-partners/data-migration/profile|Data Migration]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The source data is always worse than promised and that is always discovered late.
**Tags:** #data-integration #automation #evaluation-metrics #descriptive-statistics #workflow-orchestration #k-nearest-neighbors #compliance #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to move a client's data into a new platform without discovering its quality problems during cutover weekend — and whoever automates that takes the account.

## The Problem
Migration is planned as a mechanical exercise and turns out to be a data quality project. Duplicates, missing mandatory values, inconsistent formats, orphaned references and twenty years of accumulated mess surface when the first load fails, which is typically late in the engagement. The plan then compresses, the cutover slips, and the client's view of the whole implementation is shaped by a weekend that went badly.

## Why Nobody Has Built This
Source access is often granted late, so profiling happens late. Migration is scoped as a task rather than as a quality project. Each source system is different enough to feel unique. And the discovery late in the project is normalised as how migrations go.

## What to Build
Profile first, map from patterns, and rehearse properly. Profile the source data in the first week of the engagement rather than at the first load, which is the core and moves every unpleasant discovery to when there is time to handle it. Quantify the quality problems and their remediation effort as a stated scope item, so the client decides rather than the project absorbs. Reuse mappings per source system, since the same legacy products appear repeatedly and their models do not change. Match and deduplicate records with proper methods rather than by exact keys, which is the commonest and most consequential quality issue. Automate reconciliation between source and target as a standard output rather than a spreadsheet someone builds. Rehearse the full load repeatedly against a realistic environment, which is the practice that makes cutover uneventful. Time the load and extrapolate honestly, as cutover windows are routinely underestimated. Produce a remediation workflow the client can run on their own data, which is where much of the fix has to happen. Record what went wrong per source system so the next engagement starts informed. And treat the profile as a deliverable in its own right, which several clients would value independently.

## Target Customer
Implementation partners and systems integrators, migration specialists, enterprise clients, and data quality and migration tooling vendors.

## Impact If Built
Migration is planned as mechanical and turns out to be a data quality project, discovered at the first load. Profiling in week one moves every unpleasant discovery to when there is still time and scope to handle it.
