# Continuous Integration and Canary Practice

**Niche:** [[niches/ai-model-evaluation-firms/application-regression-harnesses/profile|Application Regression Harnesses]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Progressive delivery solved shipping a risky change safely with canaries, automated analysis and rollback, and model application teams deploy prompt changes to everybody at once.
**Tags:** #hypothesis-testing #confidence-intervals #automation #workflow-orchestration #evaluation-metrics #change-point-detection #data-integration #quick-win
**Contested on:** Every serious competitor in this sub-niche is fighting to tell a product team whether their change made their own application better, per commit, at a cost that fits a tooling budget — and whoever does that takes the account, because that is the only question an application team is asking.

## The Problem
The deployment discipline already has an answer for a change whose effect cannot be fully determined before release: ship it to a small slice, compare the slice against the baseline automatically on real traffic, and roll back on a bad signal. It is mature, widely implemented and directly applicable to a prompt or model change, whose effect is genuinely hard to establish offline. Teams instead run a two-hundred-item suite and ship to everyone.

## What Already Exists
Progressive delivery and canary release tooling with automated analysis and rollback; feature flag platforms with targeting and instant kill switches; online experimentation with sequential testing; shadow and mirrored traffic evaluation; and service-level objective monitoring with error budgets.

## The Customization Gap
The adaptation is to a change whose quality signal is neither an error rate nor a conversion metric. It requires: (1) canary analysis on output quality rather than on latency and errors, since a prompt change breaks nothing mechanically and degrades the thing nobody is monitoring — this is the gap that makes generic canary tooling useless here; (2) shadow evaluation, running the new configuration against real traffic without serving it, which suits this workload unusually well because the outputs can be graded offline and no user is exposed; (3) implicit quality signals from user behaviour — retries, escalations, edits, abandonment — as the canary metric, since explicit feedback is too sparse to gate on and these are available and underused; (4) cost and latency as co-equal signals, because a change that improves quality at triple the cost per request is a regression by most teams' standards and no evaluation harness reports it; and (5) sequential analysis so a canary can conclude as soon as the evidence supports it, which matters when each observation costs a model call.

## Target Customer
Engineering teams shipping model-based applications, evaluation platform vendors, and the progressive delivery and experimentation vendors for whom output quality is an unserved signal type.

## Impact If Solved
Canary practice is mature and its analysis metrics are the wrong ones for this workload. Grading shadow traffic offline suits model applications unusually well, and implicit behavioural signals are dense enough to gate on where explicit feedback is not.
