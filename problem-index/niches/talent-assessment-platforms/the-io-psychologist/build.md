# Build: Scientific Guardrails in the Configuration Path

**Niche:** [[niches/talent-assessment-platforms/the-io-psychologist/profile|The I-O Psychologist]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Encode the instrument's validated range as constraints in the configuration system, so a scientifically unsupported deployment requires an explicit, recorded override.
**Tags:** #compliance #workflow-orchestration #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #worker-facing #automation
**Contested on:** Whether a vendor will build a system that can refuse a client's configuration.

## The Problem

An instrument is validated for a defined range: job families, seniority levels, populations, a way of combining scales, a range of cut scores. That range is in the technical documentation and exists nowhere in the software.

So a client configures the instrument for a role outside the validated families, with a cut score above anything the validation supports, combining scales in a way the norms do not cover, and the configuration system accepts all of it without comment. The psychologist, if consulted, objects in a meeting. The implementation consultant explains the client's requirement. The configuration ships.

The knowledge required to prevent this is written down. It is simply not in the path where the decision is made.

## Why Nobody Has Built This

A configuration system that refuses a client request is a commercial problem. Implementation teams are measured on time to deployment and client satisfaction, and a blocking constraint is friction in a competitive sale.

The validated range is also frequently not written down precisely enough to encode. Technical documentation describes what was studied, not what is permitted, and turning one into the other requires the science team to make explicit judgements they have been able to leave implicit.

And the psychologist's objection has always been a professional communication rather than a system constraint, which is how the profession works and how it is routinely overridden.

## What to Build

Constraints, warnings and recorded overrides in the configuration path.

**Encode the validated range explicitly.** Per instrument: job families, seniority, populations, supported score combinations, cut score ranges, minimum sample requirements, and language and locale coverage. This is a specification the science team writes once and maintains, and writing it is itself clarifying.

**Warn at configuration.** When a setting falls outside the range, a specific message at the moment of configuration — this instrument was validated on these job families and this role is not among them; this cut score exceeds the validated range. In the interface, not in a document.

**Require an override with a reason and a signature.** Configurations outside the range proceed only with an explicit override, a stated rationale, and a named person accepting it. This is the whole mechanism: it does not prevent the deployment, and it makes the decision visible and attributable.

**Record every override.** A register of out-of-range configurations, by client, by instrument, by reason. This is the artefact the psychologist currently lacks — the pattern of overrides is the evidence that the profession's advice is being systematically disregarded, and nobody can see it because nothing is recorded.

**Escalate the severe cases.** Some configurations are not merely unwise but indefensible — a feature with no construct justification, an instrument applied to a protected characteristic proxy, a cut score with no rational basis. A defined escalation to a science authority with the power to refuse, on a narrow and published set of criteria, is what gives the role any teeth.

**Report the register to leadership.** Monthly, with counts and patterns. An override count rising in one client or one product is a governance finding, and it is currently invisible to everyone.

## Target Customer

Vendors' science functions and general counsel, for whom the override register is both a professional and a legal risk instrument. Also employers' assessment functions facing the same dynamic internally, and the professional bodies, for whom an enforceable configuration standard would give their guidance effect for the first time.

## Impact If Built

The instrument's validated range moves from a document nobody reads into the path where decisions are made. Out-of-range deployments still happen and become explicit, attributed and counted. And the psychologist's objection acquires a record, which is the difference between a professional opinion and an accountability mechanism.
