# Support Staff After a Bad Action

**Industry:** [[ai-agent-platforms|AI Agent Platforms]]
**Type:** Worker Life Changing
**One-liner:** When an agent does something wrong on a customer's behalf, a human support agent inherits an angry customer, an action they did not take and cannot explain, and no clear path to undo it.
**Tags:** #large-language-models #evaluation-metrics #confidence-intervals #change-point-detection #gradient-boosting #workflow-orchestration #automation #worker-facing

## The Problem
An agent handled a customer's request and got it wrong. It cancelled the wrong subscription, applied a discount that should not have applied, gave an incorrect policy answer the customer relied on, or escalated something it should have resolved and closed something it should have escalated.

The customer contacts support. A human picks it up and inherits a situation with three problems.

They must reconstruct what happened. The agent's trajectory exists in a trace designed for engineers — tool calls, intermediate state, model outputs — not a narrative a support agent can read in ninety seconds while a customer waits.

They must undo it, and reversal is frequently not built. The agent could issue a refund and there is no equivalent path to unwind one cleanly. The support agent improvises, sometimes creating a second inconsistency.

And they must explain it. The customer wants to know why, and the honest answer — the system made a mistake for reasons nobody can articulate quickly — is not something a support agent is empowered to say.

## Why It Matters to the Worker
Support agents in these deployments have already had the routine work removed by the agent. What remains is the difficult, the ambiguous and the failures, so the average interaction is far harder than before automation and the emotional load is higher.

Inheriting an action they did not take is the specific indignity. The support agent is accountable to the customer for a decision made by a system they do not control, cannot inspect easily and cannot fully explain.

The customer is angrier than they would be about a human error. There is a well-documented asymmetry in how people react to automated mistakes, and the support agent absorbs that difference directly.

And their observations go nowhere. A support agent who sees the same agent failure ten times has identified a pattern more valuable than any individual resolution, and there is usually no channel from the support queue back to whoever tunes the agent.

## What a Solution Looks Like
Readable trajectory summaries. The trace exists; converting it into a plain narrative of what the agent understood, what it did and why is a summarisation task, and it is the difference between a support agent reading for ninety seconds and escalating to engineering.

Reversal as a first-class design requirement. Every action an agent can take should have a defined undo path, or should require approval precisely because it does not. This is a design principle the category has largely skipped and it is the single biggest determinant of how bad a failure becomes.

Proactive detection. Many bad actions are detectable before the customer notices — an anomalous trajectory, an action inconsistent with the request, a downstream contradiction — and reaching the customer first changes the interaction entirely.

A feedback channel from support to agent tuning, with failures categorised and counted, so that the tenth instance of a pattern is visible as a pattern.

Clear disclosure about what the customer was interacting with, which is increasingly a legal requirement in several jurisdictions and which materially affects how the failure conversation goes.

## Impact If Solved
Automated failures land on human support agents who did not cause them, cannot explain them and often cannot undo them, in a queue already concentrated into the hardest cases. Readable traces, designed reversal and a real feedback channel address all three, and the feedback channel is the only route by which production failures reliably reach the people who could prevent the next one.
