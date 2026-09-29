# The Same Component Assessed Forty Times

**Niche:** [[niches/software-supply-chain-security/security-engineer-triage/profile|The Security Engineer]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Fix (Pain Point)
**One-liner:** A vulnerability in a common library produces a finding in every service that uses it, and the same determination is made independently for each one.
**Tags:** #graph-theory #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to stop an application security engineer establishing that findings do not apply, one at a time, in a queue the scanner regenerates nightly — and whoever does that takes the function, because that is currently the job.

## The Problem
A vulnerability is published in a logging library used by ninety of the organisation's services. Ninety findings appear. The determination is the same for most of them — the vulnerable feature is not enabled in the standard configuration the platform generates — and it is made ninety times, by several engineers, over two weeks, each opening a different service and reaching the same conclusion. Three of the ninety use a different configuration and are genuinely affected, and identifying those three is the entire useful content of two weeks of work.

## Why It's Still Broken
The queue is organised by service because that is how findings are generated and how ownership is assigned, so the component-level structure is invisible in the workflow. Grouping by component is trivially available — the finding names it — and no product presents the queue that way. The configuration that determines applicability is frequently identical across services because the platform generated it, which makes the determination genuinely common, and nothing knows that. And the work is distributed across engineers, so no individual sees the repetition clearly.

## What a Fix Looks Like
Group the queue by determination rather than by instance. Present findings clustered by component and version, so the ninety appear as one item with ninety affected services, which is the single change that collapses two weeks into an afternoon. Detect configuration commonality across the affected services, since a platform-generated configuration is identical and the determination applies to all of them at once — with the exceptions identified explicitly, which is the valuable output. Apply a determination to the whole cluster with the exceptions handled individually, which matches how the work should be done and how the tooling prevents. Identify the outliers first, since those three services are the entire risk and the current ordering buries them among ninety. Report the fan-out per component, which tells the platform team which shared dependencies produce the most triage load and is an argument for consolidating them. And record the determination against the component and configuration so the next version's findings inherit it, which connects to the reuse mechanism in the build note.

## Who Feels the Pain
Security engineers making the same determination repeatedly; teams receiving findings that were assessed as inapplicable elsewhere in the organisation; and functions whose capacity is consumed by fan-out rather than by risk.

## Impact If Fixed
Grouping by component is available from the finding itself and collapses the dominant repetition immediately. Identifying the configuration outliers first surfaces the actual risk that the instance-ordered queue currently buries.
