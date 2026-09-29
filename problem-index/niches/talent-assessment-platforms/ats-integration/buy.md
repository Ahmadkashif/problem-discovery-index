# Buy: HR Integration Platforms Adapted to a Decision Artefact

**Niche:** [[niches/talent-assessment-platforms/ats-integration/profile|ATS Integration & Score Plumbing]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** HR integration platforms move data between systems competently; an assessment score is a decision artefact with an evidentiary life, not a field to synchronise.
**Tags:** #data-integration #compliance #workflow-orchestration #evaluation-metrics #confidence-intervals #automation #descriptive-statistics #worker-facing
**Contested on:** Whether general HR integration tooling can carry an artefact with legal and interpretive requirements.

## The Problem

HR system integration is well served. Unified API providers, iPaaS platforms, prebuilt connectors between the major applicant tracking systems and the surrounding vendors, and partial data standards all exist, and an assessment vendor can integrate with a dozen ATS products without building each one.

They move fields. An assessment score is a field and it is also a record of a decision about a person, subject to challenge, requiring interpretation context, carrying a version, and needing to survive into a different system years later for a validation that has not been commissioned yet. Integration platforms have no concept of any of that.

## What Already Exists

Merge, Finch and the unified HR API providers. iPaaS platforms with HR connectors. Prebuilt ATS integrations from the major assessment vendors. HR-Open and similar data standards. Webhook and event infrastructure. The plumbing is genuinely good.

## The Customization Gap

**The payload is a decision record, not a value.** Score, error, version, range, quality and accommodation status travel together and are meaningless separately. Integration platforms model fields; this needs a composite object with integrity, and the unified API abstractions flatten exactly that.

**The receiving system must render it, not just store it.** Carrying an interval into a field the ATS displays as a number achieves nothing. The value is realised in the presentation layer, which means the integration project is partly an ATS product change — outside what an integration platform can deliver.

**Retention outlives the systems.** A validation runs eighteen months later, possibly after an ATS migration. The score's survival into the HRIS and its longevity there is a data lifecycle requirement, and integration platforms move data rather than governing its life.

**Versioning is essential and unusual.** Instrument and configuration versions must travel with the score and be immutable afterwards, so that a later analysis knows what produced it. Most HR integrations overwrite.

**Consent and purpose limitation follow the data.** Candidate assessment data carries purpose restrictions that should constrain its use in the destination system — not visible to hiring managers post-hire, not used in performance management. Propagating a purpose limitation across a system boundary is not something integration tooling models.

## Target Customer

Assessment vendors building their integration layer, and the unified HR API providers, for whom assessment is a category they connect and whose requirements exceed a field mapping. Also employers' HR technology teams specifying integrations they will later depend on for validation.

## Impact If Solved

The connector coverage, authentication and event infrastructure gets bought, and the composite decision record, receiving-side rendering, long retention, immutable versioning and travelling purpose limitation get built. Concretely: a score that arrives interpretable and survives long enough to be validated.
