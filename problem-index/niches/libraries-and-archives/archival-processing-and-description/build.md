# First-Pass Finding Aids From Scanned Boxes

**Niche:** [[niches/libraries-and-archives/archival-processing-and-description/profile|Archival Processing & Finding Aids]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An archivist reads every folder of a collection to write a description that a model could draft from quick scans in a fraction of the time.
**Tags:** #tacit-knowledge-ml #transformers #cnns #large-language-models #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn unprocessed boxes into a searchable, privacy-screened finding aid at a cost per linear foot a grant or budget line can carry, and whoever makes processing fastest without exposing restricted material takes the archive's processing budget.

## The Problem
Processing a collection of a few dozen boxes means opening every folder, noting dates, correspondents and subjects, deciding the arrangement, and writing scope notes, folder lists and restrictions. The archivist's judgement — what a series is about, what matters to researchers, what must be closed — is the valuable part; most of the hours go to reading and typing.

## Why Nobody Has Built This
Archives are a small, grant-funded market, and until recently models could not read mixed handwriting, typescript and photographs well enough to describe them. Archival software vendors build systems of record, not description engines.

## What to Build
A pipeline that takes rapid, low-resolution capture of each folder (a phone or overhead scanner at a few seconds a page), recognises text and document types, clusters folders into candidate series, drafts folder titles, date ranges, correspondents and subject terms, flags pages with personal or restricted information, and outputs a draft finding aid in the archive's own DACS and EAD conventions for the archivist to edit. Edits are logged so the archive's description style is learned over time.

## Target Customer
University special collections and state archives with processing backlogs, and processing grant programmes that fund them.

## Impact If Built
If processing rates rise from an estimated few linear feet to tens of linear feet per archivist-week for routine collections (estimate), backlogs measured in decades become years, and the archivist's time goes to appraisal and arrangement.
