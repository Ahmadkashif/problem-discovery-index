# Support for the Weekly Investigation

**Niche:** [[niches/game-analytics-vendors/the-analyst-asked-why/profile|The Analyst Asked Why by Thursday]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A causal question, descriptive data, and two days.
**Tags:** #worker-facing #causal-inference #workflow-orchestration #evaluation-metrics #confidence-intervals #large-language-models #data-integration #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to let the person asked why a metric moved answer it properly within the deadline they were given — and whoever equips them takes the account.

## The Problem
The analyst receives a question — why did this move — with a deadline measured in days. They form hypotheses from experience, write queries to test each, and stop when they find something that fits and the deadline arrives. The process is undocumented, unrepeatable, and depends entirely on which hypotheses occurred to them. It repeats weekly, frequently on similar questions, and nothing accumulates between investigations.

## Why Nobody Has Built This
Analytics tooling is built for exploration and reporting rather than for investigation. The analyst's process is regarded as craft. Nobody has treated the weekly why-question as a recurring workflow. And the analyst absorbs the difficulty invisibly.

## What to Build
Give the investigation a structure, a memory and a standard opening. Provide an investigation workflow that enumerates candidate causes, tests each, and records what was ruled out, which is the core and turns a search into a method. Pre-compute the standard opening moves — change point, segment decomposition, change timeline overlay, seasonality comparison — so the first two hours are done before the analyst starts. Keep a library of past investigations so a recurring question starts from the previous answer. Make the analysis reusable as a template rather than as a one-off query, since the same question recurs monthly. Record the conclusion and revisit it when more data arrives, which is how the analyst learns whether their judgement is good. Surface what the data cannot distinguish, so the analyst has a defensible way to say the question is unanswerable. Generate the write-up from the investigation record, which is a meaningful share of the time. Track how long investigations take and which questions recur, as that is the case for fixing the underlying instrumentation. Share investigations across the team rather than leaving them in individual notebooks. And protect the analyst from being the only place the organisation's causal reasoning happens, which is the real fix.

## Target Customer
Studio analytics teams, game analytics vendors, publishers with analytics functions, and analytics workflow tooling providers.

## Impact If Built
The answer depends entirely on which hypotheses occurred to the analyst before the deadline, and nothing accumulates between investigations. A structured workflow with pre-computed opening moves and a library of past answers changes both.
