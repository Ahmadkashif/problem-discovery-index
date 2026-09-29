# The Managed Services Engineer Inheriting the Org

**Industry:** [[saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Worker Life Changing
**One-liner:** After go-live, someone has to support a configuration built by people who have left, documented in a slide deck, with no explanation of why any of it is the way it is.
**Tags:** #graph-neural-networks #large-language-models #bert #gradient-boosting #change-point-detection #evaluation-metrics #worker-facing #tacit-knowledge-ml

## The Problem
Managed services engineers support configured platforms after implementation, usually across several customers. What they inherit is a tenant containing hundreds of automations, validation rules, custom objects, integrations and interface modifications, built over months by a team that has moved on, with documentation that describes what was built and almost never why.

The why is what matters. A validation rule exists because of a compliance requirement or because one stakeholder in 2022 wanted it, and those have completely different implications for whether it can be changed. An approval chain routes a certain way for a reason nobody wrote down. A field that looks redundant feeds an integration that fails silently if it is removed.

So every change request begins with archaeology. Trace the dependencies, work out what touches what, form a theory about intent, and make a change with incomplete confidence. The risk falls on the engineer: a change that breaks something in production is attributable to them, regardless of whether the original design was knowable.

Ticket volume runs continuously alongside this, with service level commitments, across multiple customers with different configurations — so the engineer is context-switching between unfamiliar environments under a clock.

## Why It Matters to the Worker
This is accountability for other people's undocumented decisions, which is a poor and permanent position. The engineer did not build it, cannot find out why it is the way it is, and owns the consequence of touching it.

The fear of breaking things has an effect on the work. Engineers become conservative — avoiding changes, layering new configuration on top of old rather than cleaning up, deferring anything risky — and the tenant accumulates complexity, which makes the next change harder. Everyone involved can see the accumulation and nobody has the confidence or the budget to reverse it.

And the knowledge problem repeats at every handover. The engineer who has spent two years learning why a tenant is the way it is becomes the single point of failure, and when they leave, the next person starts the archaeology again.

## What a Solution Looks Like
Make the dependency graph explicit and queryable. What a field, rule, automation or integration touches, and what touches it, is derivable from configuration metadata, and having it answerable in seconds removes most of the archaeology and most of the risk of an unforeseen consequence.

Reconstruct intent where it can be reconstructed. Requirements documents, change requests, ticket history and project correspondence contain the reasons, scattered and unindexed. Linking a configuration element to the discussion that created it turns the most important missing question — why is this here — from unanswerable into retrievable.

Detect the accumulation. Unused fields, automations that never fire, rules that no longer match any record, and duplicated logic are all measurable in a live tenant, and presenting them as a ranked cleanup list with evidence gives an engineer the case for remediation they currently cannot make.

Flag the blast radius before the change. A proposed modification should carry an automatic statement of what depends on it and which of those dependencies is exercised in production, which turns a nervous change into an assessed one.

## Impact If Solved
Managed services is where enterprise SaaS implementations actually live out their lives, supported by people with the least information and the most exposure. A queryable dependency graph and reconstructed intent remove the archaeology that precedes every change; accumulation detection gives the evidence for the cleanup everyone knows is needed. Together they address the long decay that turns a successful go-live into an unmaintainable tenant three years later.
