# Five Things Moved and One of Them Was Yours

**Niche:** [[niches/llm-application-tooling/the-applied-ai-engineer/profile|The Applied AI Engineer]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An applied AI engineer investigating why answers got worse must separate their own prompt changes from a provider's silent model update, a retrieval change, a data change and ordinary sampling noise, with no reliable baseline anywhere.
**Tags:** #causal-inference #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to tell an engineer which of five simultaneously-moving things caused a quality change — and whoever does that takes the account, because that attribution is most of the job and nothing supports it.

## The Problem
Users report worse answers. In the relevant fortnight: the prompt was edited twice, the provider updated the model behind an unchanged identifier, the knowledge base was re-indexed with a different chunking, a data refresh added a new document category, and the traffic mix shifted after a marketing campaign. The engineer samples inputs, re-runs them, gets different results each time, and cannot tell whether a two-point difference is real. Four days later they have a hypothesis and no proof. The information to resolve it in an hour existed and was never assembled.

## Why Nobody Has Built This
The five moving parts live in five systems owned by different people, two of them outside the company. A continuous baseline requires running a fixed evaluation set on a schedule, which costs model calls nobody budgeted. Provider-side changes are undisclosed and unversioned, so detecting them requires deliberate probing nobody set up. And the engineer's four days are invisible in any metric.

## What to Build
Assemble the moving parts and measure against a standing baseline. Version every component together — prompt, model identifier and observed behaviour fingerprint, retrieval index version, data snapshot, application version — and stamp every production response with the full tuple, which is the structural precondition and is a small amount of plumbing. Run a fixed evaluation set continuously on a schedule, so a baseline exists that predates the incident rather than being reconstructed after it — this standing measurement is what turns a four-day investigation into a lookup and its cost is trivial next to the time it saves. Detect provider model changes with a canary probe, which the fix note develops. Attribute a quality change by re-running the baseline set under each historical configuration, which is a designed comparison rather than a manual bisect and parallelises. Report quality with uncertainty so that differences inside the noise are not investigated at all, which removes a large share of these investigations outright. Diff the configuration tuple between any two points in time and show what changed. Track the traffic mix as a component, since a shift in what users ask changes quality without anything in the system changing. And report the time spent on attribution, because it is currently a large hidden cost that nobody has named.

## Target Customer
Applied AI engineering teams, their leads, and the tooling vendors whose customers spend days on this repeatedly.

## Impact If Built
A standing baseline measured on a schedule costs very little and turns a four-day investigation into a lookup. Versioning all five components into one tuple stamped on every response is the small plumbing change that makes attribution possible at all.
