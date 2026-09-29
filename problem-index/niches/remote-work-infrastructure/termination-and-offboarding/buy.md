# Buy: Case and Workflow Tooling Adapted to a Statutory Process

**Niche:** [[niches/remote-work-infrastructure/termination-and-offboarding/profile|Termination & Offboarding]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Workflow and case management tools run processes people define; a statutory termination process is defined by law and cannot be edited by the administrator.
**Tags:** #compliance #workflow-orchestration #data-integration #evaluation-metrics #confidence-intervals #descriptive-statistics #automation #worker-facing
**Contested on:** Whether configurable workflow tooling can enforce a process the configuration must not be allowed to change.

## The Problem

Workflow and case management software is abundant. Process definition, task assignment, approvals, SLAs, document management, audit trails and escalation are standard, and an HR or legal operations team can model a termination process in an afternoon.

The tooling assumes the process is the organisation's own. Administrators configure it, managers override it, and exceptions are granted when business need requires. A statutory termination process is none of those things: it is imposed, the steps are mandatory, the waiting periods cannot be shortened, and an override is not an exception but a breach.

## What Already Exists

Workflow engines and case management platforms. HR service delivery tools with offboarding workflows. Document generation and e-signature. Task and approval management. Audit logging. Matter management from the legal world, which is closer in shape.

## The Customization Gap

**The process is law and must not be configurable by the user.** A gate that a manager can override is not a gate. The process definitions need to be owned by compliance, versioned with the rule base, and locked against the operational users who run terminations under pressure.

**The timeline runs from statutory requirements, not from a target date.** Workflow tools compute dates from SLAs the organisation sets. Here the dates come from notice periods and waiting requirements that depend on the worker's tenure, contract and jurisdiction, and the earliest lawful completion is an output rather than an input.

**Eligibility checks have to reach into other systems.** Protected category status depends on leave records, medical absence, parental leave, union role and complaint history held across payroll, leave and case systems. A workflow that asks the user to confirm no protected category applies is worthless; it must check.

**Sixty process definitions, versioned, with effective dates.** Every jurisdiction has its own, they change, and a termination initiated under one version follows it through. Workflow tools version a process definition and do not generally handle in-flight cases spanning a version change in a legally meaningful way.

**The output is an evidence file.** Not a completed workflow but a bundle a tribunal could examine — steps, dates, documents, communications, calculations — assembled in a defensible form. Case management produces a record; this needs a record built to be read adversarially.

## Target Customer

Platform legal and operations teams building termination workflows on generic tooling and finding the overrides are the problem. Also the HR service delivery and legal matter management vendors, for whom statutory process enforcement across jurisdictions is a distinct requirement their configurable products do not meet.

## Impact If Solved

The process engine, task management, document generation and audit machinery get bought, and the non-configurable gates, statutory timeline computation, cross-system eligibility checks, versioned jurisdictional definitions and adversarial evidence file get built. Concretely: a termination that cannot skip the step that makes it lawful.
