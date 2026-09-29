# Buy: Audit and Governance Tooling Adapted to Employment Decisions

**Niche:** [[niches/recruiting-tech-vendors/compliance-and-records/profile|Compliance, Records & Audit Trail]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Audit logging and AI governance platforms record what systems did; an employment decision record must also capture what a person concluded and why.
**Tags:** #compliance #data-integration #workflow-orchestration #evaluation-metrics #descriptive-statistics #confidence-intervals #automation #hypothesis-testing
**Contested on:** Whether system-oriented governance tooling can capture a mixed human and automated decision.

## The Problem

Audit and governance infrastructure is mature and growing. Immutable audit logs, model registries with versioning, data lineage, policy management, evidence collection and AI governance platforms responding to new regulation are all available.

They are built around systems: what the model was, when it changed, what data it used, who approved it. An employment decision is frequently a hybrid — an automated filter removed a candidate, or a score ranked them low and a human reviewer acting on that ranking rejected them — and reconstructing it requires the system record and the human basis together. The governance platforms capture the first and have no representation for the second.

## What Already Exists

Immutable audit logging. Model registries and versioning. Data lineage tooling. AI governance platforms addressing new regulatory regimes. Policy and control management. Evidence collection for audit. Records retention management. ATS audit trails of variable depth.

## The Customization Gap

**The decision is hybrid and the tooling models only the automated half.** The record must link the automated output to the human action that followed, including whether the human agreed, overrode or simply accepted the ranking. That linkage is the substance of an explanation and no governance product has it.

**The human basis needs structure, and structure needs the requisition's own criteria.** A generic reason taxonomy is useless as evidence. Reasons tied to the specific requisition's stated requirements are informative and require the governance layer to know about requisitions.

**The subject is an individual with rights.** Governance platforms serve internal oversight. Employment decision regimes increasingly give the candidate rights of disclosure and contestation, which means the record must support producing a candidate-facing explanation — a different output than an auditor's evidence pack.

**Configuration changes are the decision context.** A filter's threshold on a given date is as much part of the decision as the model version. Governance tooling versions models; ATS configurations are typically mutable and unversioned, and closing that gap is where most reconstruction failures originate.

**Retention rules conflict.** Data minimisation and candidate data deletion rights pull against the retention needed to reconstruct a decision. Resolving this requires a deliberate policy — what is retained, in what form, for how long, pseudonymised at what point — that the tooling cannot decide for you.

## Target Customer

ATS vendors building to arriving automated-decision obligations, and employers' compliance functions specifying what they need from vendors. Also the AI governance platform vendors, for whom hiring is the most immediately regulated application of automated decision-making and their system-centric model is incomplete for it.

## Impact If Solved

The immutable logging, versioning, lineage and evidence machinery gets reused, and the hybrid decision linkage, requisition-specific reason structure, candidate-facing explanation, configuration versioning and retention resolution get built. Concretely: a record from which a specific person's rejection can be explained, which is what the regulation is going to ask for.
