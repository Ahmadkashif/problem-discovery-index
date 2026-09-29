# Learning the Approval

**Niche:** [[niches/spend-management-platforms/exception-judgement/profile|Exception Judgement]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A perfectly labelled corpus of human judgement about business spend, growing by thousands of examples a month, used as an audit log.
**Tags:** #gradient-boosting #large-language-models #evaluation-metrics #confidence-intervals #cross-validation #automation #worker-facing #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to turn thousands of recorded approve-or-deny judgements a month into automated judgement that a controller trusts — and whoever does it takes the approval queue out of the product entirely.

## The Problem
Machine learning problems are usually constrained by labels. Here the labels are abundant, clean, timestamped, attached to rich context, and free — a manager saying yes or no to a specific purchase by a specific employee against a specific budget, with a merchant, an amount, a category and often a justification in text. The platform has millions of these across its customer base and has never trained anything on them, so the same routine exception is routed to a human every single month.

## Why Nobody Has Built This
The audit trail's purpose is evidentiary, so nobody looked at it as training data — a log built to prove a process happened is not a place anyone goes looking for a dataset. Automating approvals conflicts with the product's control narrative. The labels are per customer and vary in meaning, which makes the problem look harder than it is. And no team owns approval quality as a metric.

## What to Build
Model the judgement and earn the trust. Train on the exception corpus with transaction context, employee history, budget position and merchant, which is the core and is a conventional problem with exceptional data. Use the approver's free-text justification, since it is rich, unread and explains the reasoning the label alone omits. Model per customer with a shared base, because policy meaning varies by company and a pooled model with customer-specific adaptation is the right structure. Calibrate confidence carefully, as auto-approving must be reserved for cases where the model is genuinely certain and a single bad automatic approval will end the feature. Start by ranking rather than deciding, so the controller sees the likely-fine cases grouped and the unusual ones surfaced, which delivers most of the value with none of the risk. Measure approver consistency, since different managers decide the same case differently and nobody knows the spread. Detect the decision that contradicts the customer's own history, which is the case actually worth a human. Explain every prediction, because a controller will not delegate judgement to something that cannot say why. Keep a full audit trail of automated decisions, as the control must remain defensible. Let the customer set their own automation threshold, since risk appetite differs. And report how many approvals were saved and how many automated decisions were later reversed, which is the honest scorecard.

## Target Customer
Product and data leadership, controllers and managers buried in approvals, auditors assessing automated controls, and workflow vendors routing exceptions without learning from them.

## Impact If Built
A log built to prove a process happened is not where anyone looks for a dataset. Millions of clean, contextual, free labels about business judgement are sitting in the audit trail, and the same routine exception is routed to a human every month.
