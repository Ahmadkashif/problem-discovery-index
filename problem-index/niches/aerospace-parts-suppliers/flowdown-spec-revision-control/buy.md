# QMS Document Control Linked to the Purchase Order

**Niche:** [[niches/aerospace-parts-suppliers/flowdown-spec-revision-control/profile|Customer Flowdown & Specification Revision Control]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** QMS document control already tracks the shop's procedures and revisions; it never sees the revisions customers call out on each PO.
**Tags:** #data-integration #large-language-models #compliance #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn each purchase order's quality clauses and specification revisions into checked requirements on the router before a job is released, and whoever catches the most clause and revision mismatches before parts are made takes the account.

## The Problem
The shop controls its own procedures well, because AS9100 auditors check document control. The customer's documents (clause libraries, process specs at stated revisions) arrive on POs and live outside the system.

## What Already Exists
QMS platforms (ETQ, MasterControl, Uniphi, Qualio) with document control and contract-review checklists; specification subscription services; ERP sales-order entry.

## The Customization Gap
A connector that reads each PO's referenced documents and revisions into the QMS, maps them to the shop's controlled procedures, flags where the customer's revision is newer than the procedure, and opens a change task. Contract review then becomes a recorded comparison rather than a signature, with customer clause libraries version-controlled alongside the shop's own documents.

## Target Customer
AS9100 suppliers already running a QMS document-control module.

## Impact If Solved
Linking customer revisions to internal procedures turns a recurring audit finding into an automatic task and cuts contract review per PO from ~20–30 minutes to ~5 (estimate).
