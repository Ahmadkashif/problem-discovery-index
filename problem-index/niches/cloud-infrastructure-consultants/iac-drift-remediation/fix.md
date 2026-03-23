# Console-Click Configuration Leakage

**Niche:** [[niches/cloud-infrastructure-consultants/iac-drift-remediation/profile|IaC Drift Remediation]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Engineers bypass IaC to make quick changes in the cloud console during incidents, creating configuration leakage that accumulates into an unreliable IaC state and makes future deployments unpredictable.
**Tags:** #automation #compliance #workflow-orchestration #worker-facing

## The Problem
During incidents, engineers make changes directly in the AWS/Azure/GCP console to resolve issues quickly — modifying security groups, scaling instance sizes, changing RDS parameters. These "console clicks" are rational in the moment but create configuration leakage: the IaC state no longer matches reality. Over months, 10-30% of resources in a typical environment have at least one drifted attribute. Eventually, running `terraform apply` becomes dangerous because it might revert a critical hotfix that was never backported.

## Why It's Still Broken
Console access cannot be fully restricted because engineers need it during incidents when IaC pipelines are too slow. Organizations that try to enforce "no console changes ever" find that engineers work around restrictions during emergencies, creating an adversarial dynamic. The real problem is the lack of a fast, low-friction path from "console change during incident" to "IaC updated to match" — the backporting process is manual, requires context-switching, and gets deprioritized once the incident is resolved.

## What a Fix Looks Like
A lightweight tool that detects console-made changes within minutes (via CloudTrail event stream), captures the exact configuration delta, and auto-generates a Terraform PR that backports the change to IaC. The PR includes the associated incident ticket link, the engineer's identity, and a description of what was changed and why. Engineers review and merge the PR as part of incident postmortem, closing the loop between emergency action and IaC integrity.

## Who Feels the Pain
Platform engineers who inherit months of accumulated console drift and spend entire sprints reconciling IaC state with reality before they can safely deploy new infrastructure.

## Impact If Fixed
Reduces configuration leakage from 20% of resources to under 3%, restores confidence in `terraform apply` for the entire engineering team, and eliminates the quarterly "drift cleanup sprint" that wastes 40-80 engineering hours.
