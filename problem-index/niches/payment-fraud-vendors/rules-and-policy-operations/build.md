# Knowing What Each Rule Does

**Niche:** [[niches/payment-fraud-vendors/rules-and-policy-operations/profile|Rules & Policy Operations]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of rules sit over the model and nobody can say what any individual one contributes.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #causal-inference #automation #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to manage a rule layer that grows after every incident and is never pruned — and whoever measures what each rule actually does takes back the decisions the model should be making.

## The Problem
A rule was written after an attack three years ago. The attack ended, the model improved, the merchant's business changed, and the rule remains — declining transactions that the model would now approve correctly. There are hundreds like it. Their combined effect on approval rate, fraud rate and false declines is not decomposable by anything in the platform, and the only evidence about any of them is that removing one feels risky.

## Why Nobody Has Built This
Rules are an escape hatch for urgency, so they are written under pressure and nothing in that moment creates an expiry or a measurement — and an artefact created to solve an emergency inherits none of the discipline a planned feature would get. Removing a rule risks a loss with a name attached while keeping it costs invisible revenue. Attribution across overlapping rules is genuinely non-trivial. And nobody reports the layer's aggregate effect.

## What to Build
Measure the layer and give rules a lifecycle. Attribute decisions to individual rules and report each one's volume, override rate against the model, and outcome, which is the core and makes the invisible visible. Identify rules that only ever decline transactions the model would also decline, since they are pure redundancy and can be removed with no risk at all. Identify rules that override the model and produce no fraud prevention, as those are pure false-decline cost. Simulate a rule change against historical traffic before deploying it, which turns a fearful decision into an evidenced one. Require an expiry and a rationale on every new rule, because the discipline has to be imposed at creation or never. Detect overlapping and contradictory rules, which accumulate silently and produce behaviour nobody intended. Report the rule layer's aggregate contribution separately from the model's, so the two can be managed independently. Trial removal on a traffic slice rather than all at once, as a safe test removes the main objection. Version and review the layer on a cadence with an owner, since nothing currently forces a look. And feed the persistently useful rules back as model features, because a rule that genuinely adds signal belongs in the model.

## Target Customer
Risk strategy leadership, data science teams whose model is overridden, merchants whose approval rate is shaped by forgotten rules, and decision platform vendors with no rule analytics.

## Impact If Built
An artefact created to solve an emergency inherits none of the discipline a planned feature gets, so rules arrive with no expiry and no measurement. Per-rule attribution identifies the redundant and the purely costly ones immediately.
