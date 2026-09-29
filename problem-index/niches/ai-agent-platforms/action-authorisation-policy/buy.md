# Authorisation Controls and Risk-Based Approval

**Niche:** [[niches/ai-agent-platforms/action-authorisation-policy/profile|Action Authorisation Policy]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Banking, procurement and payments all built risk-based approval hierarchies with delegated authority and maker-checker controls, and agent platforms offer a checkbox.
**Tags:** #compliance #markov-decision-processes #evaluation-metrics #confidence-intervals #descriptive-statistics #revenue-impact #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to place the human approval gate where the evidence says it belongs rather than where a nervous product manager guessed — and whoever does that takes the account, because gate placement determines whether a deployment saves anything.

## The Problem
Deciding which actions need a second pair of eyes, at what threshold, by whom, is a solved organisational problem. Delegated authority matrices set limits by role and value. Maker-checker separation is standard in finance. Risk-based approval routes a transaction by its own characteristics rather than by a flat rule. Payments systems approve, challenge or decline based on a scored risk in milliseconds. Agent platforms offer a list of tools with a checkbox next to each.

## What Already Exists
Delegated authority frameworks with value and role thresholds; maker-checker and segregation of duties controls; risk-based authentication and transaction approval with scored routing; step-up challenge patterns; policy engines evaluating approval rules; and audit trails designed for regulatory review.

## The Customization Gap
The adaptation is to an actor whose error rate is measurable and whose actions vary in reversibility. It requires: (1) the agent's own confidence as a routing input, which is the direct analogue of a transaction risk score and is the piece that makes graduated approval possible rather than categorical; (2) reversibility as an explicit dimension, since financial controls are organised around value and the dominant consideration here is whether a mistake can be undone — a hundred-dollar irreversible action frequently deserves more scrutiny than a thousand-dollar reversible one; (3) approval routed to whoever has the context rather than to whoever has the authority, since the reviewer needs to judge whether the agent is right rather than whether the amount is permitted; (4) step-up patterns adapted so the agent can ask a clarifying question rather than escalate, which is a cheaper intervention with no analogue in transaction approval; and (5) audit trails covering the agent's reasoning as well as the action, since the regulatory question will be why it did that.

## Target Customer
Risk and compliance functions, agent platforms, and the authorisation and payments control communities.

## Impact If Solved
Risk-based approval is mature and organised around value, while the dominant consideration here is reversibility. Using the agent's own confidence as the routing score is the direct analogue of a transaction risk score and is what makes approval graduated rather than categorical.
