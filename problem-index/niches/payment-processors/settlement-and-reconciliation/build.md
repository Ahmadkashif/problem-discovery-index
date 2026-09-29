# Proving the Totals Agree, by Hand

**Niche:** [[niches/payment-processors/settlement-and-reconciliation/profile|Settlement & Reconciliation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Money moves through networks, currencies, fee schedules and settlement timetables that each report differently, and the work of proving the totals agree is done by people with spreadsheets.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #compliance #descriptive-statistics #graph-theory #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to prove that money moved across networks, currencies and fee schedules adds up — and whoever does that automatically removes the largest manual finance function in payments.

## The Problem
The processor's own ledger says one thing. The network's settlement file says another, using different identifiers and a different cut-off. The bank statement shows a net amount covering many transactions with fees deducted according to a schedule with dozens of qualification conditions. The currency conversion happened at a rate applied by somebody else. Somebody must establish that these describe the same money. They do it in spreadsheets, every day, at every processor, and the differences that cannot be explained are written off below a threshold that nobody has justified.

## Why Nobody Has Built This
Reconciliation crosses counterparty boundaries where identifiers and conventions are set by other people, which makes it feel bespoke per counterparty — the external heterogeneity is real and it obscures that the matching logic is the same everywhere. It is a finance function inside an engineering company and receives finance function tooling. Breaks are individually small. And the manual process works, which is the condition under which nothing gets built.

## What to Build
Automate the matching and investigate the residual. Build a canonical transaction model that every source maps into, which is the foundation and turns a set of pairwise reconciliations into one comparison. Match automatically with tolerance for timing and fee differences, since most breaks are timing or fee-calculation artefacts rather than missing money and separating them is most of the work. Recompute fees independently from the published schedules, which catches the genuine errors and is the part most often skipped because the schedules are complicated. Attribute every break to a cause rather than to an amount, since the causes are few and recurring and naming them turns investigation into classification. Investigate automatically where the cause is known, escalating only the novel ones. Handle currency conversion explicitly with the applied rate and timing, which is a common and hard-to-see source of difference. Report the unexplained residual as a standing metric, since a write-off threshold with no justification is a policy nobody has examined. Reconcile continuously rather than daily, so a systematic problem is caught in hours rather than at the next cycle. Give merchants their own reconciliation, since they have the same problem one level down and mostly cannot do it. And measure the function's headcount and the residual together, because that pair describes both the cost and the risk of the current arrangement.

## Target Customer
Finance operations at processors and platform acquirers, large merchants reconciling their own settlements, and the reconciliation vendors serving the segment.

## Impact If Built
External heterogeneity is real and it obscures that the matching logic is identical everywhere, which is why this is rebuilt per counterparty and done by hand. A canonical model with cause-attributed breaks turns pairwise spreadsheet work into classification and makes the unexplained residual a managed number.
