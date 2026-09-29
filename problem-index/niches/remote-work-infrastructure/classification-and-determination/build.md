# Build: A Determination That Carries Its Own Evidence

**Niche:** [[niches/remote-work-infrastructure/classification-and-determination/profile|Classification & Compliance Determination]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Make every compliance determination a structured record — the facts, the rule, the source, the date, the reasoning and the confidence — rather than a status indicator.
**Tags:** #compliance #large-language-models #confidence-intervals #evaluation-metrics #workflow-orchestration #data-integration #hypothesis-testing #descriptive-statistics
**Contested on:** Whether a platform will make its central product claim auditable.

## The Problem

The platforms hold the information that would make compliance auditable: the facts of each engagement, the rule that was applied, the date the rule was last verified, and the outcomes of the disputes they have handled. None of it is surfaced, and the customer receives a status.

The consequence is that the customer cannot evaluate what they bought. They cannot tell a determination made last week from one inherited from a note written three years ago. They cannot see which facts mattered or check that the facts were right. They cannot compare providers on anything except price and country coverage. And they carry the residual risk of all of it.

Surfacing it would convert a green tick into evidence, and it is resisted for the same reason it is valuable — an auditable determination is a contestable one.

## Why Nobody Has Built This

The product's proposition is that the customer does not have to think about this. An auditable determination invites them to, which is a harder sale and a slower onboarding.

It also creates a written record of reasoning that can be wrong. A status indicator that turns out to be mistaken is a product failure; a documented determination that turns out to be mistaken is a document in someone's evidence bundle. The legal calculus around creating that artefact is not obvious.

And the determinations are currently not structured enough to surface. They exist as a specialist's judgement recorded as an outcome, with the reasoning in an email or nowhere, so making them auditable means first making them structured — which is real work.

## What to Build

A determination record, versioned and evidenced.

**Structure the facts.** The engagement's actual characteristics as a fixed schema: duration, exclusivity, control, equipment, integration into the client's organisation, remuneration structure, substitution rights, place of work. These are the inputs to every classification test in every jurisdiction and they are currently collected as a questionnaire and discarded.

**Version the rule base.** Each jurisdiction's rules as identified, sourced artefacts with an effective date, a last-verified date, and a citation to the statute, case or guidance behind them. This is the internal knowledge work in the first sub-niche and it is the foundation.

**Record the determination as a joined object.** Facts applied to rule version, with the reasoning, the specialist, the date and a stated confidence. Generative assistance can draft the reasoning from the facts and the rule for specialist review, which is what makes this affordable across dozens of jurisdictions.

**Express confidence honestly.** Some determinations are settled and some are genuinely uncertain — a borderline classification, an evolving test, a jurisdiction with inconsistent enforcement. A single green tick across both is the misrepresentation, and a three-level confidence with the reason for uncertainty is both truthful and more useful.

**Re-evaluate on change.** When a rule version changes, every determination that relied on it is flagged for re-review. Today a rule change means someone remembering which customers are affected.

**Learn from the disputes.** Every authority challenge the platform has handled, with the facts, the determination and the outcome, as a structured corpus. This is the only real validation evidence in the industry and it sits in case files.

**Give the customer the record.** The facts, the rule, the date, the reasoning and the confidence, on demand. That is what converts a purchased assertion into a defensible position, and it is what a sophisticated buyer will eventually require.

## Target Customer

Clients' legal and tax functions at larger enterprises, who carry the residual risk and are increasingly unwilling to accept a status indicator as the basis for it. Also platforms competing on trust rather than price, for whom auditability is the only differentiation available in a market where every competitor shows a green tick.

## Impact If Built

The customer can evaluate what they bought, which is the condition for this market to compete on quality at all. Rule changes propagate to affected determinations automatically. Uncertainty gets expressed as uncertainty. And the dispute history becomes the validation evidence the industry has never assembled.
