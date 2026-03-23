# Scope Change Impact Calculator

**Niche:** [[niches/software-dev-agencies/client-change-order-mgmt/profile|Client Change-Order Management]]
**Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** JIRA and Linear track task dependencies, but they cannot calculate the cascading cost and timeline impact of a scope change across dependent features, milestones, and resource allocations in real time.
**Tags:** #automation #workflow-orchestration #data-integration #quick-win

## The Problem
When a client requests adding "multi-language support" to a web application mid-project, the PM must figure out: which existing features are affected (every user-facing screen, email templates, PDF reports), how many additional hours are needed for each affected feature, whether the current sprint plan can absorb the work or must be reorganized, whether the milestone dates shift and by how much, and whether any downstream dependencies (QA testing, client review, launch date) are impacted. This analysis takes 2-4 hours per change request, requires pulling data from JIRA (task dependencies), the estimate (original effort per feature), and the resource plan (who is available when). Most PMs do a rough mental estimate instead, leading to inaccurate impact assessments.

## What Already Exists
JIRA and Linear model task dependencies and can show critical path impact when tasks are added. Microsoft Project and Smartsheet offer more sophisticated dependency and resource modeling. But none of these calculate the cost impact (what does the change cost the client?), integrate with the contract terms (does this push past a milestone payment trigger?), or present the impact in client-friendly terms. They show task-level shifts, not business-level impact.

## The Customization Gap
The tool needs to: (1) model the project at the feature level (not just task level) with effort estimates per feature, (2) calculate cascading impact when a new feature or modification is added — which features are affected, how many hours are added, which milestones shift, (3) translate the impact into cost terms using the project's rate card, (4) present the impact in a client-readable format ("adding multi-language support affects 8 features, adds 120 hours, costs $18,000, and delays launch by 2 weeks"), and (5) generate a change order document from the impact assessment with one click.

## Target Customer
Project managers at dev agencies handling 5+ concurrent projects with 3-5 change requests per project, spending 2-4 hours per change request on manual impact analysis.

## Impact If Solved
Reduces change impact assessment from 2-4 hours to 15-30 minutes per request. Improves impact accuracy by 30-40% through systematic dependency analysis. Enables PMs to respond to client change requests same-day instead of waiting 2-3 days for analysis.
