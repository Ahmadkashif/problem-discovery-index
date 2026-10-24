# Monthly Variance Analysis Written by Hand

**Industry:** [[defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every month each control account over threshold needs a written variance explanation and a re-signed estimate at completion, and on most programmes the narrative is still drafted from scratch in Word and Excel.
**Tags:** #large-language-models #transformers #time-series-forecasting #evaluation-metrics #feature-engineering #compliance #automation

## The Problem
A cost-type development or production contract of $50M or more carries an earned value requirement under DFARS Part 234 (class deviation 2026-O0011, effective 1 February 2026), and the monthly Integrated Program Management Data and Analysis Report goes to the programme office with schedule and cost data plus variance analysis. Each control account whose cost or schedule variance crosses the contract's reporting threshold needs a variance analysis report: the cause, the impact on the estimate at completion, and the corrective action. A large programme can have hundreds of control accounts and dozens of reportable variances a month (estimate).

The control account manager, usually an engineer, writes them in the few days between the accounting close and the report due date. They pull actuals from the cost system, earned value from Cobra or a similar tool, and schedule status from Primavera or Microsoft Project, then write prose that programme control edits for consistency. The same causes recur month after month in slightly different words, and DCMA tests the data for traceability between the narrative, the numbers and the schedule.

## What Already Exists
Earned value engines (Deltek Cobra, Oracle Primavera Unifier, Hexagon's EcoSys) compute variances and indices. Analytics layers such as Empower and in-house Power BI dashboards chart them and flag threshold breaches. Generic LLM writing assistants, where security rules allow them, can draft prose.

## The Customisation Gap
The tools compute the variance but not the explanation. The defence-specific layer is: the contract's variance thresholds and data item requirements; the 32 EIA-748 guidelines and DCMA's data tests, which check that a narrative's cause matches the work packages, the schedule's critical path and the estimate's change; the link between this month's variance and last month's corrective action; and the need to run on premises, because programme data is CUI and often classified. A draft that pulls the drivers from cost, schedule and material data, cites the work packages, compares against last month's explanation and flags contradictions would match how programme control already reviews the reports.

## Impact If Solved
Drafting variance analysis from the data instead of from memory could save a control account manager several hours each monthly close (estimate) across hundreds of accounts per programme. It would also make explanations consistent enough that recurring causes become visible to programme managers before they turn into an estimate change.
