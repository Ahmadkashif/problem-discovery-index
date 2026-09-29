# Buy: Programme Management for a Function of One

**Niche:** The Compliance Manager
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Project and programme management tooling handles portfolios, dependencies, cross-team coordination and deadline forecasting, and the compliance manager runs four programmes from four dashboards and a spreadsheet.
**Tags:** #evaluation-metrics #time-series-forecasting #confidence-intervals #workflow-orchestration #worker-facing #data-integration #automation
**Contested on:** Whether one person running several certification programmes has any leverage over the organisation whose cooperation the whole thing depends on.

## The Problem

Running several concurrent programmes with hard external deadlines, shared dependencies and work executed by teams that do not report to you is a well-understood management problem with mature tooling. Programme management software handles portfolios, cross-project dependencies, resource contention, milestone tracking, risk registers and delivery forecasting.

A compliance manager has exactly that job and does not use any of it. Their tooling is compliance platforms, which model framework readiness rather than programme delivery. A platform tells them which controls are passing; it does not tell them whether the ISO audit in eleven weeks is achievable given that the same three engineers are also needed for the SOC 2 evidence and are currently on a product deadline.

The mismatch is straightforward. The platforms were built to produce audit artefacts, which they do well. The manager's problem is coordinating people across an organisation against several deadlines, which is a different discipline entirely and has its own tools.

## What Already Exists

Programme and portfolio management: Monday, Asana, Smartsheet, Wrike and the enterprise portfolio tools, with cross-project views, dependency tracking, resource allocation, milestone forecasting and risk registers.

Project delivery practice: critical path analysis, burndown forecasting, dependency management and the general apparatus of predicting whether a deadline will be met.

Engineering delivery: Jira and Linear, where the engineering work actually happens and where compliance items land as foreign objects.

Professional services automation: portfolio views across concurrent client engagements, which is structurally similar.

Compliance platforms themselves: framework readiness, evidence collection and audit artefacts, with little programme management on top.

## The Customization Gap

**Framework readiness is not delivery status.** A control at ninety per cent readiness says nothing about whether the remaining work is a day or a quarter, who is blocked on what, or whether the deadline holds. Translating readiness into a delivery plan with estimates and dependencies is the adaptation.

**Cross-framework dependencies are unmodelled.** One evidence item may unblock requirements in three frameworks. Programme tools handle shared dependencies natively; compliance platforms treat each framework as separate.

**The resources are not the manager's.** Programme management assumes some control over assigned resources. Here the work is done by teams with other priorities and no reporting line, which means the tooling needs influence support — escalation paths, visible commitments, agreed capacity — rather than allocation.

**Deadlines are external and immovable.** Audit dates are set by auditors and contracts. Forecasting against a fixed date with uncertain completion is exactly what delivery forecasting does and is not applied here at all.

**The manager runs it alone.** Programme tools assume a programme manager with a delivery team. This is one person coordinating across an organisation, which puts a premium on automation of the coordination itself rather than on planning features.

**Integration is the whole practical problem.** The work lives in engineering's tracker, the status lives in the compliance platform, and the plan would live in a programme tool. Three systems, no joins, which is why the manager's spreadsheet exists.

## Target Customer

The compliance platforms, who should be adding programme management on top of readiness rather than leaving their primary user to assemble it externally.

Programme management vendors are unlikely to build compliance-specific capability, which makes this a lesson for the platforms rather than a product to buy — though Smartsheet and similar are what managers actually improvise with today.

Compliance leadership at multi-framework organisations, who would recognise the framing immediately because they are already doing programme management by hand.

## Impact If Solved

The manager's actual job gets tooling. They are running a portfolio of programmes and their software models certification readiness, which is a description of the output rather than of the work.

Delivery forecasting against fixed audit dates would replace the current method, which is experienced judgement and anxiety, with something that can be shown to a leadership team.

And modelling cross-framework dependencies would surface the highest-leverage work automatically, which is the single biggest improvement available to a person whose constraint is their own time.
