# Classification From What the Requester Can Actually Say

**Niche:** [[niches/procurement-spend-platforms/intake-and-orchestration/profile|Intake & Orchestration]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Intake forms ask an employee for a commodity code, a risk classification and a contract type, which are procurement's vocabulary rather than theirs, and the gap is filled by an analyst acting as a help desk.
**Tags:** #large-language-models #bert #transformers #gradient-boosting #evaluation-metrics #confidence-intervals #workflow-orchestration #automation
**Contested on:** Every serious competitor in procurement intake is fighting to take a request from someone who does not know what procurement needs and route it correctly without a human help desk — and whoever routes most requests unassisted takes the account.

## The Problem
A marketing manager needs a tool that analyses customer survey responses. The intake form asks for a commodity code, whether the purchase involves personal data, whether it requires a security review, the contract type, the budget line and the expected term. She knows what she wants and none of the answers. She either guesses, which produces a misrouted request that a reviewer bounces back three days later, or she contacts the procurement analyst, who asks her three questions in plain language, determines the answers in ninety seconds, and enters them. That analyst's job is substantially translation between the employee's description and procurement's schema.

## Why Nobody Has Built This
The form was designed backwards from what the downstream processes require, which is the natural way to build it and produces a form only procurement can complete. Inferring the classification from a plain-language description was not reliably achievable until recently, so the help desk was the rational answer. And the analyst role exists and functions, which removes the urgency — the cost is an FTE and a three-day delay per misrouted request, both of which are absorbed rather than measured.

## What to Build
Intake that asks what the requester knows and infers the rest. The employee describes what they need in their own words and answers a small number of adaptive questions chosen for information gain — is any customer data involved, will this connect to our systems, roughly how much and for how long — rather than a fixed form of everything. From that, the classification is inferred: commodity category, whether personal data is implicated, whether a security assessment is warranted, the likely contract type and the applicable approval path, each with a confidence. High-confidence determinations route automatically; the uncertain ones go to the analyst with the inference and the reasoning attached, so their job becomes confirming rather than eliciting. Prior requests for the same thing are surfaced, since a substantial share of intake is somebody asking for a tool the organisation already has — which is the highest-value single output and is currently discovered by accident. Every analyst correction is a label, so the inference improves on this organisation's own vocabulary.

## Target Customer
Procurement intake vendors, the suites building intake layers, and procurement operations teams staffing an analyst as a help desk.

## Impact If Built
The help desk role exists because the form speaks the wrong language, and inference removes most of it while also removing the three-day round trips from misrouted requests. Surfacing existing entitlements — you already have this tool, here is who owns it — is the by-product with the most direct financial value and requires only that the request be classified well enough to match.
