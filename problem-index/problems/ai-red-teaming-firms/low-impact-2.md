# Regression Testing After Model Updates

**Industry:** [[ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Automated probing tools make re-testing cheap in principle, and in practice a client's model update invalidates an entire assessment with no established way to revalidate short of another engagement.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #large-language-models #transfer-learning #compliance

## The Problem
A firm completes an assessment, delivers findings, and the client remediates. Two months later the client updates their model version, or changes a system prompt, or adds a retrieval source, or modifies a guardrail configuration.

Every finding in the report is now of unknown status. Remediated issues may have regressed. Issues that did not exist may now. The defensive measures validated against the previous model may behave differently.

The client's options are unattractive. Commission another engagement, which is expensive and slow relative to the pace of model updates. Run the automated portion of the previous assessment, which covers the known probes and not the reasoning that produced them. Or accept that the assessment is stale, which is what usually happens.

The mismatch in cadence is the core issue: models update on a timescale of weeks and assurance engagements operate on a timescale of quarters. Regulatory frameworks asking for documented testing do not currently address what happens when the system under test changes, and organisations are quietly carrying assessments that describe a system they no longer run.

## What Already Exists
Automated probing tools and open attack datasets support cheap repeated execution. Guardrail vendors offer continuous monitoring of deployed systems. Evaluation platforms support scheduled runs against fixed test sets. Version tracking for models and prompts is available in most application tooling. Some firms offer retainer arrangements with periodic re-testing.

## The Customisation Gap
The automatable portion is the shallow portion. A red team's value is the reasoning that constructs a novel probe for a specific system, and what gets captured as a reusable test is the resulting prompt — which the model may have been updated specifically to resist, while the underlying reasoning still works with a variation.

Nothing generalises a finding into a test. A discovered vulnerability should become a family of probes exploring the same weakness, not a single string, and that generalisation is the difference between a regression suite that keeps working and one that goes stale immediately.

Change impact assessment is absent. When a client changes model version or configuration, which findings are plausibly affected is estimable — some depend on model behaviour, others on retrieval configuration, others on the guardrail — and a client currently has no way to scope a re-test.

Continuous assurance as a product does not really exist. The engagement model is a project, the risk is continuous, and the gap between them is where clients are exposed.

## Impact If Solved
Assessments describe a system that has since changed, and organisations are relying on them for regulatory and internal assurance. Generalising findings into probe families and scoping re-tests by change impact makes revalidation cheap enough to match the cadence of model updates, which is the only way assurance keeps meaning anything.
