# Settlement Reconciliation From Payments

**Niche:** [[niches/music-distribution-platforms/royalty-accounting-and-reconciliation/profile|Royalty Accounting & Reconciliation]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payments built reconciliation as a discipline with invariants, break detection and lineage, and royalty accounting reconciles by spreadsheet at month end.
**Tags:** #data-integration #evaluation-metrics #change-point-detection #automation #compliance #confidence-intervals #descriptive-statistics #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn dozens of incompatible statement formats into a payment an artist can trace back to a stream — and whoever makes a royalty statement explainable takes the trust the whole category runs on.

## The Problem
Payments and financial operations treat reconciliation as a first-class discipline: invariants that must hold continuously, automated break detection with classification, lineage from a transaction to a settlement, and an expectation that any figure can be decomposed on demand. Royalty accounting handles comparable complexity with less rigour, on a monthly cycle, with breaks investigated manually if they are noticed.

## What Already Exists
Reconciliation invariants and continuous checking; break detection and classification; transaction-to-settlement lineage; exception workflow with ageing; and audit-ready decomposition of any figure.

## The Customization Gap
The adaptation is to a counterparty statement rather than a ledger. It requires: (1) the incoming data being another party's report rather than a shared ledger, so there is no independent record to reconcile against and the expected value must be modelled from stream counts — this is the substantive difference; (2) formats that change without notice and differ per service, where payments has standards; (3) allocation across a catalogue and splits among rights holders, adding two layers payments does not have; (4) rates that are computed pro-rata from a pool and are not knowable in advance; and (5) a payee with no ability to audit, which shifts the burden of demonstrable correctness entirely onto the distributor.

## Target Customer
Royalty operations and finance leadership, artists and rights holders, auditors, and reconciliation platform vendors.

## Impact If Solved
Payments made reconciliation continuous and decomposable and royalty accounting does it monthly by spreadsheet. Modelling expected revenue from stream counts is what substitutes for the shared ledger this domain does not have.
