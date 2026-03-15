# Audit Evidence Collection Coordination

**Industry:** [[compliance-consulting|Compliance Consulting Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic project management tools track tasks but don't encode the compliance-specific evidence request logic — which artifact is required for which control, which client department holds it, and what format the auditor will require — making evidence collection a manual, ad hoc coordination burden rather than a systematic workflow.
**Tags:** #automation #workflow-orchestration #data-integration #compliance

## The Problem
Audit preparation requires assembling evidence for every audited control — screenshots of system configurations, policy documents, training records, access logs, vendor contracts, incident reports, change management records. Each piece of evidence must: exist, be current (within the audit period), be in a format the auditor will accept, and be mapped to the specific control it supports. Coordinating the evidence collection across IT, HR, legal, and operations at a client site — getting the right person to pull the right artifact in the right format by the audit deadline — is a project management problem that compliance consultants solve with spreadsheets and email. The result is a months-long coordination effort with constant follow-up, last-minute fire drills when evidence is missing, and no systematic status visibility.

## What Already Exists
Vanta and Drata automate evidence collection for SOC 2 by connecting directly to cloud infrastructure APIs — pulling logs and configurations automatically. Tugboat Logic, Sprinto, and similar tools apply the same model to ISO 27001. These tools work when the client has cloud-native infrastructure and the evidence is computable from system APIs. For non-tech compliance domains (FDA manufacturing, OSHA, HIPAA for non-SaaS organizations), the evidence is human-generated documents, physical records, and manual process artifacts — nothing that an API can collect.

## The Customisation Gap
For non-tech compliance domains, the gap is a structured evidence request and tracking system that: knows which evidence items are required for each regulatory framework and control; knows which client role typically holds each evidence type (IT admin for access logs, HR for training records, quality manager for CAPA records); generates pre-formatted evidence requests to the right client contacts; tracks submission status per evidence item; validates submitted evidence for format and date range correctness; and organizes validated evidence in the audit-ready file structure the auditor expects. This workflow automation requires regulatory-specific knowledge of what evidence is required — knowledge that lives in the consultant's head today.

## Impact If Solved
Reduces consultant time spent on evidence coordination by 40-60% per engagement. More importantly, reduces last-minute audit deficiencies — the most stressful and reputation-damaging aspect of audit preparation — by making evidence gaps visible weeks before the audit rather than days before.
