# Wave Planning Optimization

**Niche:** [[niches/cloud-infrastructure-consultants/enterprise-migration-partners/profile|Enterprise Migration Partners]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Project management tools like Jira and Smartsheet can track migration tasks but cannot optimize wave sequencing based on dependency graphs, business criticality, and resource constraints.
**Tags:** #reinforcement-learning #ranking #workflow-orchestration #data-integration

## The Problem
Wave planning — deciding which groups of applications to migrate in what order — is a constraint satisfaction problem that consultants currently solve in spreadsheets. A typical 500-workload migration has 8-12 waves over 6-9 months, and each wave must respect dependency ordering, change-freeze windows, team capacity, and business criticality. Getting wave order wrong causes rollbacks costing $50K-$200K per incident.

## What Already Exists
Smartsheet and Microsoft Project handle task sequencing, and tools like Flexera and Cloudamize provide workload assessment data. However, none of these tools can ingest a dependency graph and automatically generate wave plans that satisfy multiple simultaneous constraints — consultants manually build wave plans in Excel, iterating through 3-5 revisions per engagement.

## The Customization Gap
The missing layer is a constraint-aware scheduling engine that takes dependency maps, business calendars, team capacity, and risk tolerances as inputs and outputs optimized wave sequences. This requires domain-specific constraints that generic project management tools don't model: database-before-application ordering, shared-service migration timing, and rollback window requirements.

## Target Customer
Senior migration architects at firms managing 5+ concurrent enterprise migration programs, each with $2M+ in consulting fees.

## Impact If Solved
Eliminates 2-3 weeks of manual wave planning iteration per engagement, reduces wave-related rollbacks by 40%, and improves overall migration timeline predictability from ±30% to ±10%.
