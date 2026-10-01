# Risk-Ranked Clearance for Every Research Input

**Niche:** [[niches/hedge-funds/research-compliance-mnpi/profile|Research Compliance & MNPI Control]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compliance reviews research inputs in arrival order when a small fraction carry nearly all the MNPI risk.
**Tags:** #bert #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to clear a research input — an expert call, a dataset, a management meeting — in minutes with a record an SEC examiner will accept, and whoever makes clearance both fast and defensible takes the account.

## The Problem
A compliance team at a fundamental fund may handle hundreds of expert-call requests a month, plus transcripts, channel-check notes, conference meetings and dataset onboarding. Each gets roughly the same treatment. Yet the risk is concentrated: a current employee of a supplier to a holding in the week before earnings is different from a retired industry consultant discussing a sector trend. Treating them alike slows research and dilutes attention.

## Why Nobody Has Built This
Surveillance vendors sell to the trade side and to broker-dealers, where volume is higher; research clearance at buy-side funds is a smaller, more judgement-heavy market. Compliance officers are cautious about automation in a domain where a miss is an enforcement matter.

## What to Build
A triage layer that scores every input by risk using the expert's employment and relationship to holdings, timing relative to corporate events and earnings, the restricted and watch lists, and — after the call — passage-level classification of the transcript by MNPI risk type. Low-risk inputs within policy are approved with the reasoning recorded; high-risk ones are routed with the specific concern highlighted. Every decision is logged for examination.

## Target Customer
Chief compliance officers at fundamental and event-driven funds with active expert-network and alternative-data use.

## Impact If Built
Compliance attention follows risk, research inputs clear in minutes rather than days, and the fund gains a consistent, documented process to show examiners.
