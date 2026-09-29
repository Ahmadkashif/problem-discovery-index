# eDiscovery Platforms Adapted to Financial Reconstruction
**Niche:** [[niches/accounting-firms-smb/forensic-litigation-support/profile|Forensic Accounting & Litigation Support]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** eDiscovery platforms are built to find responsive documents; forensic accountants need to rebuild a ledger from them, which is a different problem the tools do not model.
**Tags:** #bert #transformers #large-language-models #transfer-learning #data-integration #workflow-orchestration #automation #evaluation-metrics

## The Problem
A forensic engagement typically starts with a production of bank statements, invoices, emails, and accounting exports in mixed formats and inconsistent quality. The accountant must reconstruct transaction flows — tracing funds across accounts and entities, matching invoices to payments, identifying what is missing. This is done by exporting to spreadsheets and building the reconstruction by hand over weeks, and it restarts substantially whenever a supplemental production arrives.

## What Already Exists
Relativity, Everlaw, and DISCO handle large productions with strong search, deduplication, threading, and review workflow. Analytics for concept clustering and near-duplicate detection are mature. They are excellent at their designed purpose.

## The Customization Gap
Their unit of analysis is the document; the forensic unit of analysis is the transaction. The adaptation needed sits on top: extract transactions from heterogeneous financial documents into a normalised ledger, resolve entities and accounts across sources, reconcile flows and flag gaps, and — the part that matters most in practice — absorb a supplemental production incrementally rather than forcing a rebuild. The review platform stays as bought; what is missing is the financial reconstruction layer above it.

## Target Customer
Forensic accountants performing reconstruction and the engagement managers who scope these matters against fixed court schedules.

## Impact If Solved
Removes the largest and least predictable block of hours in a forensic engagement, and makes supplemental productions a routine update instead of a schedule risk.
