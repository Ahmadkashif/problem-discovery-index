# SOC 2 Evidence Collection for Agency Delivery

**Niche:** [[niches/software-dev-agencies/fintech-compliance-dev/profile|Fintech & Compliance-Driven Development]]
**Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Vanta and Drata automate SOC 2 compliance for product companies, but dev agencies need to collect and package evidence for their client's SOC 2 audit, not their own — a fundamentally different workflow.
**Tags:** #compliance #workflow-orchestration #data-integration #automation

## The Problem
When a fintech client undergoes a SOC 2 Type II audit, the auditor asks for evidence of security controls operating effectively during the audit period. If the dev agency built and maintains the application, the client asks the agency to provide: code review evidence (who reviewed, when, what was checked), deployment logs (when code was deployed, by whom, with what approvals), access control records (who has access to production systems), and incident response documentation. The agency must retroactively collect this evidence across GitHub, JIRA, AWS CloudTrail, and Slack — a process that takes 40-80 hours per client audit and repeats annually.

## What Already Exists
Vanta and Drata automate evidence collection by integrating with the company's own AWS, GitHub, and HR systems. They pull evidence continuously and present it to auditors. But they are designed for the entity being audited — the product company — not the agency delivering on behalf of that company. An agency cannot install Vanta into its client's infrastructure, and Vanta does not model the multi-client, multi-project evidence collection workflow that agencies need.

## The Customization Gap
The adaptation requires: (1) multi-tenant evidence collection across multiple clients' projects within the agency's own tooling (GitHub org, JIRA projects, AWS accounts), (2) mapping agency development practices to SOC 2 control objectives in the client's audit scope, (3) generating client-specific evidence packages that can be delivered to the client's auditor without exposing other clients' data, (4) continuous evidence collection during the audit period (not retroactive assembly), and (5) templated responses to common auditor requests specific to software development (code review practices, deployment controls, change management).

## Target Customer
Dev agencies serving 3+ fintech clients that undergo annual SOC 2 audits, where a senior engineer or compliance liaison spends 40-80 hours per audit cycle assembling evidence.

## Impact If Solved
Reduces SOC 2 evidence preparation from 40-80 hours to 4-8 hours per client audit. Converts audit preparation from a reactive fire drill to continuous evidence capture. Enables agencies to offer "SOC 2 readiness" as a premium service to clients.
