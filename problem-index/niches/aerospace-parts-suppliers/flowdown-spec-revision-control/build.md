# A Clause-to-Router Checker

**Niche:** [[niches/aerospace-parts-suppliers/flowdown-spec-revision-control/profile|Customer Flowdown & Specification Revision Control]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Contract review is a person reading a PO's clause list against memory; no tool turns the clauses into requirements on the router and checks them before release.
**Tags:** #large-language-models #transformers #bert #feature-engineering #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn each purchase order's quality clauses and specification revisions into checked requirements on the router before a job is released, and whoever catches the most clause and revision mismatches before parts are made takes the account.

## The Problem
In a typical case (illustrative), a PO from a tier-1 lists ~25 quality clause codes, four process specs with revisions and a note that the prime's approved-process-source list applies. The contracts or quality person skims it, recognises most clauses, signs contract review, and releases the job. The plating spec revision on the PO is newer than the shop's procedure, and the source inspection clause is missed. Both surface at FAI or at the customer.

## Why Nobody Has Built This
Clause libraries are customer-specific and change; specifications are licensed documents; and contract review sits between sales, quality and planning, so no single buyer feels it.

## What to Build
A checker that extracts every clause code and referenced document from the PO, resolves each against the customer's current clause library and the specification's current revision, and compares the result with the shop's procedures, approved processors and the job's router. It produces a requirement list on the traveller (source inspection, FAI, special processes, record retention, specialty metals) and blocks release on any mismatch until resolved. Every resolution is kept, so the next PO from the same customer starts checked.

## Target Customer
Quality and contracts managers at suppliers handling hundreds of aerospace POs a month across several primes.

## Impact If Built
Catching revision and clause mismatches at release instead of at FAI or customer audit avoids rework and SCARs that cost ~1–3 weeks each (estimate) and halves contract-review time (estimate).
