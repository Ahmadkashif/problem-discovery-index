# Self-Healing From Site Reliability Engineering

**Niche:** [[niches/data-platform-integrators/the-oncall-pipeline-engineer/profile|The On-Call Pipeline Engineer]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Site reliability engineering automated the recurring recovery and paged only for novelty, and data on-call reruns jobs by hand.
**Tags:** #automation #workflow-orchestration #worker-facing #evaluation-metrics #change-point-detection #compliance #data-integration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to stop one engineer rerunning, backfilling and explaining overnight failures before the morning reports go out — and whoever automates that recovery takes the account.

## The Problem
Site reliability engineering established that a human should not be woken for a problem with a known remedy. Automated remediation handles the recurring failures, runbooks are executable rather than documents, alerts are required to be actionable, and toil is measured and driven down as an explicit objective. The practice is mature and the principle — that repeated manual recovery is a defect in the system rather than a duty of the operator — is well established. Data pipeline on-call reruns jobs.

## What Already Exists
Automated remediation for known failure modes; executable runbooks; actionability requirements for every alert; toil measurement and reduction targets; and blameless review driving systemic fixes.

## The Customization Gap
The adaptation is to batch data pipelines with stateful correctness requirements. It requires: (1) recovery that must produce correct data rather than a restored service, so a naive retry can silently duplicate or omit records — this is the substantive difference and makes idempotency the central concern; (2) backfill windows that must be reasoned about rather than simply restarted; (3) failures caused by upstream systems the team does not control and cannot page; (4) impact measured in wrong numbers in reports rather than in unavailability; and (5) a consumer notification step with no service-availability equivalent.

## Target Customer
Data platform teams and integrators, platform operations leadership, orchestration and observability vendors, and managed services providers.

## Impact If Solved
Reliability engineering established that repeated manual recovery is a system defect rather than an operator's duty, and automated it. Recovery that must produce correct data rather than a restored service is what makes idempotency the central concern here.
