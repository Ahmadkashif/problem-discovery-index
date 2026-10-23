# The Runner's Note That Never Reaches the Report

**Niche:** [[niches/investigation-and-screening-firms/county-court-record-retrieval/profile|County Court Record Retrieval]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A runner learns that a court has not entered dispositions for the last four months, writes it in a comment field, and the screener reports the search as clear.
**Tags:** #large-language-models #bert #compliance #workflow-orchestration #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to return a county criminal search with the full disposition and the identifiers needed to match it inside the screener's turnaround window, from courts that restrict or refuse online access, and whoever covers the most slow and restricted counties without a re-pull takes the account.

## The Problem
Runners see things the result format has no field for: a clerk who says recent filings are not yet indexed, a terminal that shows only felonies, a case file that lists a disposition the index omits. They type these in free-text notes. The screener's system ingests only the structured result — record found or not — and the note is never read, so a report can be "clear" for a period the court had not yet indexed.

## Why It's Still Broken
The retriever-to-screener exchange format was designed for hits and no-hits. Notes vary in language and arrive in volume, so screeners filter them out rather than read them.

## What a Fix Looks Like
Add structured search-condition fields (index coverage dates, record types searched, identifiers available, known backlogs) to every result, and classify existing free-text notes into those fields with a language model, routing any condition that limits completeness to the screener's compliance review before the report goes out.

## Who Feels the Pain
Screening firms whose §613 "strict procedures" depend on complete results; employers who hire against an incomplete search; candidates whose pending case later appears.

## Impact If Fixed
Completeness limits become visible before delivery rather than after a missed record, at the cost of a few fields per search.
