# The Client Before the Call Connects

**Niche:** [[niches/robo-advisors/the-licensed-associate/profile|The Licensed Associate]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform knows everything about this client's behaviour and the associate answering their call knows their name and balance.
**Tags:** #large-language-models #gradient-boosting #worker-facing #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to put a client's full history in front of a licensed associate before the call connects — and whoever does it turns the worst days of a decade from an endurance test into the moment the product proves itself.

## The Problem
The call is the highest-leverage interaction the platform ever has. A client who is about to liquidate is on the line, and what the associate says in the next four minutes may determine a material part of that person's retirement. The associate has an account screen. They do not have, assembled and in front of them, what this client said about risk at signup, what they did in the last two drawdowns, whether their contributions have paused, what their goal was, what they were told in their last conversation, or what this decline actually means for their plan.

## Why Nobody Has Built This
Service was scoped as account support, so the tooling is a CRM record rather than an advice workstation — the function was defined by the tickets it answers rather than by the decisions it influences. The behavioural data sits in analytics systems the service platform does not touch. Calls are measured on handle time. And the days that matter are rare enough that the tooling is never built for them.

## What to Build
Assemble the client and the argument before the call connects. Build a pre-call brief from the platform's own data — stated tolerance, prior drawdown behaviour, contribution history, goal and funded status, prior conversations, current unrealised position — which is the core and is pure assembly of data already held. Compute what selling now would cost this client specifically, since a concrete personal number is the most persuasive thing available and the associate currently has a general argument. Flag the client's behavioural risk from the measurement work, so the associate knows whether they are talking to someone who has held through two declines or someone who sold in both. Recall what was said in prior conversations, because clients notice when they have to re-explain themselves and it undermines everything. Suggest the framing that has worked for similar clients, connecting to the intervention evidence. Route calls by risk rather than by queue order, since the client about to sell should not wait behind a password reset. Capture the outcome of every call in a structured form, which is the data the whole function needs and currently produces nothing of. Measure whether the call changed behaviour, as handle time is measuring the wrong thing on the day that matters. Prepare surge capacity and brief the team with real data rather than talking points. And give the associate the client's whole position where it is known, since advice about one account in a crisis is unconvincing.

## Target Customer
Client service leadership, the licensed associates themselves, investment leadership accountable for client outcomes, and advice platform vendors whose service tooling is a CRM.

## Impact If Built
Service was defined by the tickets it answers rather than by the decisions it influences, so the tooling is a record rather than a workstation. The brief is pure assembly of data already held, delivered at the only moment it matters.
