# Incident Response Practice From Site Reliability

**Niche:** [[niches/mlops-platforms/the-on-call-ml-engineer/profile|The On-Call ML Engineer]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Site reliability engineering worked out how to run a humane on-call rota with alert budgets, runbooks and blameless review, and ML teams page each other with none of it.
**Tags:** #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #worker-facing #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make the page arrive with a diagnosis instead of a log file — and whoever does that takes the account, because the platform already recorded everything needed to produce one.

## The Problem
The operations discipline has a well-developed answer to this. Alerts must be actionable or they are deleted. Every page has a runbook. Toil is measured and capped. Incidents get blameless reviews that produce changes. On-call load is a tracked metric with an explicit ceiling. ML teams inherited the pager without any of the surrounding practice, because their pipelines became production systems without anyone deciding they had.

## What Already Exists
Incident response platforms with escalation, scheduling and load reporting; runbook tooling with executable steps; alert quality practice including actionability criteria and alert budgets; blameless post-incident review methodology; error budgets and reliability targets; and toil measurement frameworks with published guidance on acceptable proportions.

## The Customization Gap
The adaptation is to a system whose failures are frequently data-caused and whose degradation is silent. It requires: (1) reliability targets expressed over data and model outcomes — freshness, completeness, prediction quality — rather than over uptime, since an ML pipeline that runs successfully on wrong data has met every conventional target and failed completely; (2) upstream data readiness as a first-class dependency, because the most common ML pipeline failure is a dependency being late or empty and no conventional alerting models that; (3) runbooks that account for correctness, since rerunning a training job is not always safe and the generic retry advice is wrong here; (4) severity that accounts for silent degradation, which has no analogue in service reliability where failures announce themselves; and (5) the on-call rota sized for a team that is not an operations team, where the same load falls on fewer people with less tooling and the standard guidance on acceptable toil proportions is being exceeded without anyone measuring it.

## Target Customer
ML engineering leaders, platform teams, incident response vendors, and the reliability community for whom ML pipelines are an unaddressed workload.

## Impact If Solved
The humane on-call practice exists and ML teams inherited only the pager. Expressing reliability targets over data freshness and prediction quality rather than uptime is the adaptation that makes the practice fit a system whose failures are silent.
