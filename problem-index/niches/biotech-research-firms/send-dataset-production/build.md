# Report-to-Dataset Reconciliation Before Submission

**Niche:** [[niches/biotech-research-firms/send-dataset-production/profile|SEND Dataset Production]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** SEND validators check that a dataset conforms to the standard; nothing checks that it agrees with the study report FDA's reviewer will read beside it.
**Tags:** #large-language-models #transformers #evaluation-metrics #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to produce SEND datasets that pass FDA's technical rejection criteria and match the study report the first time, from whatever system the study ran on, and whoever closes the gap between report and dataset fastest takes the account.

## The Problem
An FDA pharmacology/toxicology reviewer may load the SEND data into analysis tools while reading the report. If incidence counts, mean values or severity grades differ, the reviewer asks why, and the sponsor answers an information request during the 30-day IND review.

## Why Nobody Has Built This
Conformance validation came first because FDA's rejection criteria require it. Reconciliation needs reading report narrative and tables, which rule engines cannot do.

## What to Build
A reconciliation engine that extracts every quantitative statement and table from the final report, recomputes the same values from the SEND domains (BW, LB, MI, MA, OM, CL), and lists discrepancies with locations. It runs on draft versions so mismatches are fixed before signature.

## Target Customer
SEND managers at CROs; regulatory operations at sponsors compiling INDs from several CROs.

## Impact If Built
Fewer reviewer queries and resubmissions, and a dataset that matches its report on the first pass.
