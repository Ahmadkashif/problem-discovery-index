# Implementation Specialist Matter Migration

**Industry:** [[legal-practice-software|Legal Practice Software]]
**Type:** Worker Life Changing
**One-liner:** Implementation specialists stop reconstructing a decade of matter history out of folder names and email exports, and get back to configuring the workflows that decide whether the firm actually adopts the software.
**Tags:** #large-language-models #bert #word-embeddings #k-nearest-neighbors #feature-engineering #evaluation-metrics #transfer-learning #worker-facing

## The Problem
A firm switching practice management systems brings a decade of matters. In a well-run firm that is a structured export from a competitor's database. In most firms it is a structured export for the billing data plus a network drive organised by whatever convention prevailed at the time, a mail archive, and a set of paper files somebody scanned in 2016.

The implementation specialist reconciles this into matters, clients, contacts, documents, time entries, trust ledgers and open balances. Which of these forty thousand files belongs to which matter is often only recoverable from the folder path, and the folder path changed three times. Client names appear in five spellings. Trust balances must reconcile exactly, because they are client money.

Go-live is a fixed date. The specialist carries several of these at once.

## Why It Matters to the Worker
Implementation specialists in legal software are hired for practice workflow knowledge — knowing how a plaintiff-side personal injury firm actually runs, and configuring the system so that its intake, treatment tracking, lien handling and settlement workflow match. That configuration is what determines adoption, and adoption is what determines whether the account renews.

They spend most of their time on file reconciliation instead. It is unstructured, deadline-bound, and carries a specific dread: trust accounting must reconcile to the cent, and a discrepancy discovered after go-live is not an inconvenience but a potential bar issue for the client firm. The specialist owns that risk without owning the data quality that creates it.

The role also has no memory. The fortieth migration from the same competitor system repeats the work of the first, because nothing captured what was learned.

## What a Solution Looks Like
Document-to-matter assignment proposed automatically from filename, path, content and the dates and parties involved, with confidence attached and the ambiguous cases queued rather than guessed. Client and contact deduplication run probabilistically with the evidence shown. Field mapping from the competitor's schema proposed from prior migrations off the same system, since the vendor has done many.

Trust reconciliation run continuously from the first test load, reconciling to the source system's own ledger totals at every stage, so a discrepancy appears in week one rather than on the Monday after go-live.

And a memory: every confirmed mapping and every correction feeds the next migration from that source system, so the fortieth is faster than the first.

## Impact If Solved
Implementation determines whether a firm ever really uses what it bought. Moving the specialist's time from file archaeology to workflow configuration improves the outcome the vendor is actually paid for, and removes the single most stressful part of a job the vendor spends a year training people to do.
