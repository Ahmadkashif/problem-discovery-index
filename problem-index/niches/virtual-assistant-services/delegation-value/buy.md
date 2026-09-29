# Buy: Productivity Analytics Adapted to a Delegated Relationship

**Niche:** [[niches/virtual-assistant-services/delegation-value/profile|Delegation Value Measurement]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Workplace analytics products measure how an organisation spends its time; the question here is whether one person's time was freed by another person's work, across a company boundary.
**Tags:** #descriptive-statistics #causal-inference #confidence-intervals #evaluation-metrics #data-integration #compliance #hypothesis-testing #automation
**Contested on:** Whether organisational productivity analytics can measure a two-person relationship spanning two companies.

## The Problem

Workplace productivity analytics is an established category. Products derived from calendar and communication metadata report meeting load, focus time, collaboration patterns and after-hours work, and organisations use them for workload and effectiveness analysis.

They measure an organisation's own employees inside its own tenant. Here the question concerns one executive inside the client's tenant and one assistant who is a contractor of a different company, frequently operating through the executive's own shared logins, and the quantity of interest is the interaction between them. The analytics have no way to see one side, no way to attribute across the boundary, and no concept of delegation as a unit.

## What Already Exists

Microsoft Viva Insights, Worklytics, Time Is Ltd and the workplace analytics category. Calendar and email metadata analysis. Time tracking products on the assistant's side. Task management systems with cycle time reporting. Meeting analytics. Focus time measurement.

## The Customization Gap

**The two parties are in different tenants and sometimes the same account.** Attribution requires distinguishing assistant actions from executive actions, which is hard when the assistant operates through a shared login — a common and unexamined feature of this industry. Solving attribution is prerequisite to any measurement and is mostly an access-architecture problem.

**Delegation is the unit and no product has it.** The object is a task handed over, with a briefing cost, a delivery, a review cost and possibly a rework cost. Constructing that object from messages, documents and task systems is the core work and does not exist in any analytics product.

**The consumed side is what matters and is what nobody counts.** Productivity analytics measure a person's time allocation. Here the question is specifically how much of the executive's time the delegation consumed, which requires identifying the briefing and review interactions and pricing them — a narrower and different measurement.

**There is no baseline and no control.** Organisational analytics compare periods or teams. Here there is one executive and no counterfactual, so the design has to lean on pre-engagement baselines, task-type comparisons within the engagement and improvement curves over time, none of which the products support.

**The privacy posture is entirely different.** Workplace analytics operate under an employer's relationship with its employees, usually aggregated and with works-council-style safeguards. Here an agency would be analysing an individual executive's calendar and messages — a much more sensitive proposition requiring explicit executive consent, narrow scope, and the executive's own visibility as the default rather than a concession.

## Target Customer

Agencies building a value measurement capability, who will evaluate workplace analytics and find they cannot see across the boundary. Also the workplace analytics vendors, for whom the executive-assistant dyad is a well-defined and unserved measurement problem, and chief-of-staff and executive effectiveness consultancies.

## Impact If Solved

The calendar and communication metadata infrastructure gets reused, and the cross-boundary attribution, the delegation object, the consumed-time measurement, the baseline design and the individual-level privacy posture get built. Concretely: a number for whether the delegation worked, in a market that currently sells the claim and measures the hours.
