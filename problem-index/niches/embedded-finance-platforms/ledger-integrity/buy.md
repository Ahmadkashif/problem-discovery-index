# Custody Reconciliation for Pooled Accounts

**Niche:** [[niches/embedded-finance-platforms/ledger-integrity/profile|Ledger Integrity]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Securities custody solved pooled-account beneficial ownership reconciliation decades ago under rules written for it, and embedded finance runs the same structure with spreadsheet-era discipline.
**Tags:** #compliance #data-integration #evaluation-metrics #automation #change-point-detection #hypothesis-testing #confidence-intervals #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to prove continuously that the sub-ledger's record of who owns what matches the money actually held at the bank — and whoever can prove it at any moment rather than at month end wins the accounts where a break means customers lose access to their money.

## The Problem
An omnibus account holding assets for many beneficial owners, reconciled against a sub-ledger that is the sole record of individual entitlement, is the exact structure of securities custody. That industry has segregation rules, daily proof requirements, break management disciplines, independent verification and an examination regime built around them. Embedded finance platforms operate the same structure for customer cash and largely reinvented the practice from first principles.

## What Already Exists
Custody and fund accounting platforms; omnibus and sub-account reconciliation engines; break management workflow with ageing and escalation; segregation and safeguarding rules with daily computation; and independent verification practice.

## The Customization Gap
The adaptation is to cash moving continuously at consumer transaction rates. It requires: (1) continuous rather than end-of-day reconciliation, since custody's daily proof cycle is adequate for securities settlement and inadequate when card authorisations arrive every second — this is the substantive adaptation; (2) card network settlement as a reconciliation counterparty, with its authorisation-to-settlement lag, partial captures and reversals, which has no custody analogue; (3) many programmes in one FBO account, so a break must be localised to a product as well as to a customer; (4) engineering rather than fund accounting as the owning function, which changes what the tooling must look like; and (5) the platform rather than a regulated custodian holding the record, which raises the proof burden rather than lowering it.

## Target Customer
Platform finance operations and engineering, sponsor bank safeguarding functions, and custody and reconciliation vendors for whom this structure is familiar and this tempo is not.

## Impact If Solved
The structure is custody's and the discipline was reinvented without it. Continuous reconciliation at card-network tempo is the real adaptation and is what the daily proof cycle cannot supply.
