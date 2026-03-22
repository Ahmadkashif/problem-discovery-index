# Plan Version Control & Change Tracking

**Niche:** [[niches/estate-planning/document-assembly/profile|Document Assembly & Plan Packaging]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Fix (Pain Point)
**One-liner:** When a client updates their estate plan, attorneys stop manually comparing the old and new versions of 6-8 documents to figure out what actually changed — and start seeing a clear change log across the entire plan package.
**Tags:** #bert #large-language-models #feature-engineering #evaluation-metrics #data-integration #automation

## The Problem
Estate plans are updated throughout a client's lifetime — after marriages, divorces, births, deaths, moves, and asset changes. Each update may affect some or all of the 6-8 documents in the plan package. Currently, when a client returns for an update, the attorney or paralegal must: pull the prior plan from the file, determine which documents need updating, generate new versions, and manually compare old and new versions to verify that only the intended changes were made and no unintended changes were introduced. There is no redline, change log, or version comparison across the plan package. For long-term clients with 3-4 plan updates over 20 years, the full history of what changed and why is lost — reconstructing the planning rationale requires reading through years of correspondence and file notes.

## Why It's Still Broken
Estate planning document assembly tools treat each document generation as a standalone event. When an attorney generates a new trust in WealthDocx, the system doesn't know that this replaces a trust generated 5 years ago — it has no concept of document lineage or version history. Document management systems (NetDocuments, iManage) store versions of files but don't understand estate planning document structure well enough to produce meaningful change summaries ("Article 4 changed the successor trustee from John to Sarah" rather than "23 lines were modified in trust.docx"). The combination of document-level assembly and file-level storage means that plan-level version control doesn't exist anywhere in the current toolchain.

## What a Fix Looks Like
A plan-level version control system that maintains a structured representation of each plan version: all fiduciary appointments, beneficiary designations, distribution provisions, and special provisions, linked to the specific document language implementing each element. When a plan is updated, the system produces a plan-level change log: "Version 3 (2026-03-20) — Changes: Successor Trustee changed from John Smith to Sarah Smith (affects Trust Art. 5, Will Art. 3, Financial POA Sec. 2). Healthcare Agent changed from Mary Smith to David Smith (affects Healthcare POA Sec. 1, Trust Art. 7 incapacity provisions). No changes to distribution provisions, asset schedule, or guardianship appointments." The attorney reviews the change log to verify that all intended changes were captured and no unintended changes were introduced. For long-term clients, the full change history serves as a planning narrative: why each change was made, what triggered it, and how the plan evolved over decades.

## Who Feels the Pain
Paralegals who spend 30-60 minutes per update manually comparing old and new plan documents across 6-8 files. Attorneys who review updated plans without a clear summary of what changed and must read entire documents to verify accuracy. Successor attorneys who inherit a client file and must reconstruct 20 years of planning history from document versions and file notes.

## Impact If Fixed
Reduces per-update review time by 30-45 minutes for both paralegal and attorney. Eliminates the risk of unintended changes introduced during plan updates — a category of error that can produce estate distribution outcomes the client never authorized. Creates a documented planning history that supports continuity when clients change attorneys or when the original attorney retires.
