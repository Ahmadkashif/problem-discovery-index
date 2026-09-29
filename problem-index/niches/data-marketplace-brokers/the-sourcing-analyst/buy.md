# Benchmark Harnesses and Notebook Automation

**Niche:** [[niches/data-marketplace-brokers/the-sourcing-analyst/profile|The Sourcing Analyst]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Parameterised notebooks, data profiling libraries and comparison reporting all exist as mature open tooling, and the analyst writes the same notebook by hand every time.
**Tags:** #descriptive-statistics #evaluation-metrics #automation #workflow-orchestration #data-integration #hypothesis-testing #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to give the analyst a reusable evaluation harness instead of a quarter spent rebuilding one — and whoever does that takes the account, because the same comparison is being constructed from scratch in every firm in the market.

## The Problem
Running the same analysis over a new input and producing a formatted report is solved by parameterised notebook execution. Profiling a dataset's completeness and distributions is solved by profiling libraries. Comparing two datasets' distributions is solved by drift and comparison tooling. Every component of the analyst's three weeks exists as a mature open library, and the assembly into a workflow they can point at a new provider does not exist anywhere.

## What Already Exists
Parameterised notebook execution with report generation; data profiling libraries producing completeness and distribution summaries automatically; drift and distribution comparison tooling; record linkage libraries for overlap measurement; schema inference and mapping tools; and report templating with comparison layouts.

## The Customization Gap
The adaptation is to an evaluation whose reference is the buyer's own data and whose subject is a commercial decision. It requires: (1) overlap against a private reference as the central measurement, since profiling libraries characterise one dataset and the decisive question here is a two-dataset comparison the buyer must run themselves; (2) schema mapping as the parameterised input, which is the piece that makes the rest generic and is where the assembly currently fails; (3) evaluation criteria weighted to a decision rather than presented as statistics, since the analyst has to produce a recommendation and a wall of profiling output is not one; (4) execution entirely within the buyer's environment, because the reference data is the buyer's own customer base and cannot go anywhere; and (5) a persistent store of evaluations, since the tooling is built for one-off analysis and the value compounds only if results accumulate.

## Target Customer
Data sourcing teams, the analysts running evaluations, and the data tooling ecosystem for whom dataset procurement is an unserved workflow.

## Impact If Solved
Every component exists as a mature library and the assembly does not. Schema mapping as the parameterised input is the piece that makes everything else generic, and a persistent evaluation store is what makes the work compound instead of repeat.
