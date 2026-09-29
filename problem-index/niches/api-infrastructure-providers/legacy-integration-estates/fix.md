# The Partial File Nobody Noticed

**Niche:** [[niches/api-infrastructure-providers/legacy-integration-estates/profile|Legacy Integration Estates]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A transfer is monitored for whether the file arrived, so a file that arrives with two thirds of its records is processed successfully and the missing third is discovered a week later.
**Tags:** #descriptive-statistics #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #data-integration #automation
**Contested on:** Every serious competitor here is fighting to bring visibility and change safety to the file transfers, message queues and SOAP services that still move most enterprise data — and whoever does that takes the integration estate, because nobody can currently see it at all.

## The Problem
The nightly extract normally contains around eighty thousand records. On Tuesday the source system's job was interrupted and the file contains fifty-one thousand. It transferred successfully, passed the arrival check, and was loaded without error. Twenty-nine thousand transactions are simply absent from the downstream system. Nobody notices until a reconciliation the following week, by which point the downstream processing has produced statements, payments and reports based on incomplete data, and unwinding it costs far more than the original incident.

## Why It's Still Broken
Monitoring these flows was set up around the failure mode that was obvious when they were built: the file did not arrive. Partial and malformed content is a subtler failure that requires knowing what normal looks like, and nobody established a baseline. Many of these formats carry a trailer record with a control total precisely for this purpose, and a surprising proportion of implementations do not check it, or check it and log the mismatch without alerting. And the downstream system's job is to load what it is given, so it succeeds.

## What a Fix Looks Like
Check content, not arrival. Verify control totals and record count trailers where the format provides them, which is the cheapest and strongest check available and is frequently already in the file and ignored. Baseline record counts and key aggregate values per flow, accounting for day-of-week, month-end and seasonal patterns, and alert on deviation outside the expected band — which catches the partial file on Tuesday morning rather than the following week. Reconcile end to end: records sent against records loaded, which is the definitive check and requires only that both numbers be reported to the same place. Halt downstream processing on a failed check rather than proceeding, which is the decision that converts a data incident into a delayed batch and is frequently not configurable. Alert the owner of the flow rather than the operator of the transfer server, since the person who can fix a truncated extract is at the source. And report the check coverage across the estate, because the first useful finding is usually how many flows have no content check at all.

## Who Feels the Pain
Operations teams unwinding a week of downstream processing; the business functions whose reports and payments were computed from incomplete data; and the engineers who discover that the format contained a control total nobody was checking.

## Impact If Fixed
Control total verification is nearly free and is already present in most of these formats, and count baselining is elementary statistics over data every transfer log contains. Halting downstream processing on a failed check turns a costly data incident into a delayed batch.
