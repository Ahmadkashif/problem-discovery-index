# One Platform, Two Entirely Different Buyers

**Niche:** [[niches/observability-vendors/observability-platforms/profile|Observability Platforms]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Engineering observability and security log analytics have different retention requirements, different query patterns, different economics and different buyers, and are sold as one product with two configurations.
**Tags:** #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to be the place an organisation's telemetry lands and is queried — and that contest is fought twice, for engineering and for security, which is why this niche is not terminal and is decomposed below.

## The Problem
An organisation runs one platform for both. The engineering team needs thirty days of high-resolution telemetry with fast interactive queries and pays for retention they do not want on security logs. The security team needs three years of audit logs for compliance, queried rarely and deeply, and pays interactive-tier prices for data nobody touches for months. Both teams complain about the bill. The vendor sees one account with high ingestion and a cost complaint, and cannot tell that it is two workloads with opposite requirements colliding in one pricing model.

## Why It's Still Broken
Consolidation is genuinely attractive — one pipeline, one agent, one query language — and both vendors and buyers pursued it for good reasons. The economics diverge sharply nonetheless: interactive engineering telemetry and rarely-queried multi-year audit retention have costs that differ by an order of magnitude and are priced identically. Neither buyer sees the other's usage, so neither can make the argument. And vendors report account-level ingestion rather than workload-level, so the collision is invisible in their data too.

## What a Fix Looks Like
Separate the workloads within the platform rather than within the invoice. Classify ingested data by workload — engineering telemetry, security and audit, business events — automatically from source and shape, which is straightforward and is the prerequisite for everything else. Report cost, volume and query activity per workload, so each team sees its own and the collision becomes visible. Apply retention and tier policy per workload, since the correct answers are genuinely different and a global policy is wrong for both. Price accordingly, with a cold tier whose economics reflect rare access, which is what makes multi-year compliance retention affordable and is what drives security teams to separate products. Report query patterns per workload, which will show that the security data is queried in a completely different shape — rare, deep, time-bounded investigations — and justifies a different storage strategy. And give each buyer their own view, because the two teams currently argue about a shared bill neither can decompose.

## Who Feels the Pain
Engineering teams paying for compliance retention; security teams paying interactive prices for cold data; and vendors whose cost complaints are really a workload mismatch they cannot see.

## Impact If Fixed
Workload classification and per-workload reporting are straightforward and immediately decompose a bill that both buyers currently experience as one unexplained number. Tier economics that match access patterns are what stop the security workload leaving for a separate product.
