# Policy as Code and Change Management

**Niche:** [[niches/payment-fraud-vendors/rules-and-policy-operations/profile|Rules & Policy Operations]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering solved managing accumulated logic with version control, testing, staged rollout and deprecation, and fraud rules are edited in a console.
**Tags:** #workflow-orchestration #evaluation-metrics #automation #compliance #hypothesis-testing #confidence-intervals #descriptive-statistics #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to manage a rule layer that grows after every incident and is never pruned — and whoever measures what each rule actually does takes back the decisions the model should be making.

## The Problem
A fraud rule set is a large, long-lived body of logic edited by multiple people over years under time pressure. Software engineering has mature practice for exactly this: version control, code review, automated testing, staged rollout, feature flags, observability per code path, deprecation processes and technical debt management. Rule consoles offer an edit box and a save button.

## What Already Exists
Version control and review workflow; automated testing and regression suites; staged rollout and feature flagging; per-path observability; and deprecation and debt management practice.

## The Customization Gap
The adaptation is to logic whose correctness is statistical. It requires: (1) tests that are statistical evaluations against historical traffic rather than assertions, since a rule is not right or wrong but has a cost and a benefit — this is the substantive difference; (2) rollout measured on business outcomes with delayed feedback, so a canary must run long enough for chargebacks to arrive; (3) authorship by risk strategists rather than engineers, so the tooling must fit non-engineers; (4) an adversary who probes the rules, which makes exposing rule logic a security consideration; and (5) deprecation decisions that require evidence rather than judgement about dead code.

## Target Customer
Risk strategy and engineering leadership, risk strategists authoring rules, and decision platform vendors whose rule management is a console.

## Impact If Solved
Engineering solved managing accumulated logic and the fraud version has none of it. The adaptation is tests that are statistical evaluations rather than assertions, which is what makes a rule safe to remove.
