# Buy: Case Management Tooling Adapted to Cross-Organisation Chasing

**Niche:** [[niches/telehealth-platforms/the-care-coordinator/profile|The Care Coordinator]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Case management systems track work inside an organisation; a coordinator's work is entirely outside it, against counterparties with no system to integrate with.
**Tags:** #workflow-orchestration #data-integration #compliance #large-language-models #evaluation-metrics #automation #descriptive-statistics #confidence-intervals
**Contested on:** Whether internal case management tooling can manage work whose counterparties are phone lines, portals and fax machines.

## The Problem

Case management software is abundant. Healthcare-specific care management platforms, general workflow and ticketing systems, and CRM-derived products all handle task assignment, SLAs, escalation, audit trails and reporting competently.

They model work as things people in the organisation do. A coordinator's work is almost entirely things people outside the organisation must do — a payer must approve, a specialist office must call back, a pharmacy must stock something, a patient must attend. The task system records that the coordinator called; it has no representation of the external state it was trying to change, and the external state is the actual object.

## What Already Exists

Care management platforms serving health plans and providers, general workflow tools, healthcare CRM products, prior authorisation automation vendors, clearinghouse APIs for eligibility and claim status, fax-to-digital services, and robotic process automation platforms for portal work. Contact centre tooling for outbound calling and logging.

## The Customization Gap

**The tracked object is external state, not internal task.** The system needs to model "authorisation pending at this payer since this date" as a first-class entity with its own lifecycle, sources of truth and closure conditions — distinct from "coordinator to check authorisation", which is what task systems represent. This is the core adaptation.

**Counterparties have no APIs.** Payer portals, specialist offices and pharmacies are reached by portal login, phone and fax. Integrating means clearinghouse APIs where available, RPA where not, and structured telephony and fax handling for the rest. Case management products assume integration; here integration is the project.

**Inbound fax is a primary channel and is unstructured.** A large share of what arrives — authorisation decisions, specialist letters, records — comes as faxed images. Parsing them into structured records and attaching them to the right patient and the right open item is high-value, entirely absent from case tooling, and now technically routine.

**Prioritisation should be predictive, not SLA-based.** Case systems escalate on elapsed time. What a coordinator needs is a ranking by probability of failure times clinical consequence, which requires a model the workflow product does not contain.

**The patient is the counterparty who is easiest to reach and most underused.** Care management tools treat patient outreach as an assigned task. Here well-timed automated patient messaging closes a large fraction of open items without any coordinator involvement, and it should be a default pathway rather than a task.

## Target Customer

Platform operations teams selecting care management or workflow tooling and finding it models their coordinators' work incorrectly. Also the care management vendors, for whom out-of-network episodic coordination is a distinct pattern, and the prior authorisation automation vendors, for whom telehealth platforms are a natural adjacent market.

## Impact If Solved

The task, audit, SLA and reporting machinery gets bought, and the external-state model, the portal and fax integration, the predictive prioritisation and the patient-as-default-channel get built. Concretely: a coordinator sees what the payer and the specialist actually did, rather than a list of things they themselves once tried.
