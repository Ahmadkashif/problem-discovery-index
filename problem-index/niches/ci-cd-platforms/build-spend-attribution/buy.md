# Cloud Cost Allocation, One Layer Down

**Niche:** [[niches/ci-cd-platforms/build-spend-attribution/profile|Build Spend Attribution]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cloud cost management built showback, chargeback, anomaly detection and rightsizing into a whole product category, and build spend is reported as minutes per repository.
**Tags:** #descriptive-statistics #change-point-detection #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to say where build spend actually goes in units somebody can act on — and whoever does that takes the cost conversation, because minutes by repository is not a unit anyone can act on.

## The Problem
Cloud cost management is an established category with a mature practice: allocate spend to the teams and workloads that caused it, detect anomalies and attribute them, recommend rightsizing, and forecast. It is applied to infrastructure and stops at the boundary of the build system, which is frequently a substantial share of an engineering organisation's compute spend and is reported by a separate dashboard with none of the discipline.

## What Already Exists
Cloud cost management platforms with allocation, anomaly detection and rightsizing; the practitioner discipline around cost visibility and accountability; tagging and allocation methodology; anomaly detection with change-point methods; and forecasting. All mature and operating one system over.

## The Customization Gap
The adaptation is to build workloads with a natural unit of output. It requires: (1) a cost-per-outcome unit rather than cost-per-resource, since build spend has a natural denominator — changes delivered — that infrastructure cost management lacks, and it is by far the most useful framing available here; (2) attribution to configuration rather than to infrastructure, because the actionable object is a pipeline step or a test rather than an instance type, which is a different attribution hierarchy; (3) waste categories specific to this workload — re-runs, redundant uncached work, scheduled jobs nobody consumes, queue time — which have no analogue in infrastructure cost management and are where most of the recoverable spend is; (4) change attribution to commits, since a build cost increase is caused by a configuration change with an author, which is a stronger and more actionable attribution than cloud cost management can usually achieve; and (5) forward projection at merge time, so a pipeline change carries its cost estimate into review, which is a control point that does not exist for infrastructure.

## Target Customer
Cloud cost management vendors with an unserved adjacent workload, CI vendors, and platform engineering teams accountable for build spend.

## Impact If Solved
A mature cost discipline stops at the build system, which is a large and rising share of engineering compute. Cost per change delivered and workload-specific waste categories are the two adaptations, and commit-level attribution is a stronger result than the parent discipline usually achieves.
