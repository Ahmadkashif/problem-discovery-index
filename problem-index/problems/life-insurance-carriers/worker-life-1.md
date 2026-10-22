# The Valuation Actuary Through Quarter Close

**Industry:** [[life-insurance-carriers|Life Insurance Carriers]]
**Type:** Worker Life Changing
**One-liner:** Four times a year a valuation actuary spends two weeks rerunning stochastic models overnight and explaining every movement in reserves to finance, auditors and the CFO, and almost none of that time goes to judging whether the numbers are right.
**Tags:** #large-language-models #feature-engineering #monte-carlo-methods #evaluation-metrics #worker-facing #automation #workflow-orchestration

## The Problem
Quarter close for a life and annuity carrier means producing statutory reserves, GAAP liabilities under LDTI (with market risk benefits for variable and indexed products) and often a Bermuda or IFRS 17 view as well. A valuation actuary receives the in-force extract, checks it against last quarter, loads economic scenarios, runs the projection models and gets results back the next morning. If the extract had a problem, or an assumption table was the wrong version, the run is redone. Then comes the part that consumes the close: the analysis of change. Every movement in every reserve line must be split into new business, expected release, actual-to-expected experience, assumption updates, market movements and model changes. It must be explained in a memo for the controller, the auditors and the CFO, and reconciled to the general ledger. Under VM-20, and VM-22 from 2026, stochastic reserves need hundreds or thousands of scenarios (estimate), so a rerun is not quick.

## Why It Matters to the Worker
The hours land in fixed, predictable bursts: ten to fifteen working days after each quarter end, plus the year-end statutory filing season (estimate). They run late into the night because the model runs are overnight and the deadlines are not negotiable. The work is high-stakes and thankless. A misexplained movement becomes an audit finding or a restatement, and a correctly explained one goes unnoticed. Credentialed actuaries spend their most stressful weeks of the year doing spreadsheet reconciliation and repeated explanation of the same kinds of variance. The judgement they trained for gets the least time: is this assumption still right, and is the model doing what we think?

## What a Solution Looks Like
Pre-run checks that compare the in-force extract and assumption tables against last quarter and flag anomalies before the overnight run, not after. An attribution engine that steps the model through each driver automatically and produces the waterfall without manual reruns. A drafting assistant that writes the first version of the analysis-of-change memo from the attribution and last quarter's memo, linking each sentence to the numbers. And a queryable record of prior quarters' explanations, so the same variance is not re-explained from scratch each time.

## Impact If Solved
Removing the mechanical half of quarter close gives each valuation actuary back an estimated 40–80 hours a quarter, cuts the rerun cycles that cause the latest nights, and moves attention to assumption and model risk, where the expensive errors start.
