# Intent-Aware Drift Classification

**Niche:** [[niches/cloud-infrastructure-consultants/iac-drift-remediation/profile|IaC Drift Remediation]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can determine whether infrastructure drift was intentional (a hotfix that should be backported to IaC) or accidental (a misconfigured automation that should be reverted), forcing consultants to investigate every drift event manually.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml #automation

## The Problem
When drift detection tools find that the actual state differs from the IaC state, there are two possible responses: revert the change (if accidental) or update the IaC to match the new state (if intentional). Making the wrong choice is dangerous — reverting an intentional hotfix causes an outage; accepting accidental drift erodes IaC integrity. Experienced platform engineers can usually tell the difference by looking at who made the change, when, and what was modified — but this judgment is tacit knowledge that junior engineers lack.

## Why Nobody Has Built This
Intent classification requires correlating drift events with CloudTrail/audit logs (who made the change), incident tickets (was there an active incident when the change was made), change management records (was this change approved), and temporal patterns (changes at 3 AM during an incident are likely hotfixes; changes at 2 PM on Tuesday are likely accidental). No single tool has access to all these data sources, and the classification rules vary by organization.

## What to Build
A drift classification engine that ingests drift events from Terraform/CloudFormation, correlates them with audit logs and incident management systems (PagerDuty, Jira), and classifies each drift event as "intentional — backport to IaC" or "accidental — revert to declared state." The system learns from engineer feedback on classification accuracy and builds organization-specific patterns over time. For intentional changes, it auto-generates the IaC update (Terraform PR) needed to reconcile.

## Target Customer
Platform engineering teams at organizations with 200+ IaC-managed resources experiencing 10-50 drift events per week, currently spending 5-10 hours/week on manual drift investigation.

## Impact If Built
Automates 70% of drift remediation decisions, reduces drift investigation time from 10 hours/week to 2 hours/week, and prevents the 2-3 outages per year caused by incorrectly reverting intentional changes.
