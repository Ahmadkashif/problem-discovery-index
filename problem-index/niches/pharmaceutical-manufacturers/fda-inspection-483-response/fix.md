# The Back Room Running on a Spreadsheet

**Niche:** [[niches/pharmaceutical-manufacturers/fda-inspection-483-response/profile|FDA Inspection Readiness & Form 483 Response]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** During an inspection, the back room tracks every FDA request in a shared spreadsheet, and a document handed over unreviewed becomes an observation.
**Tags:** #large-language-models #transformers #workflow-orchestration #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to answer an FDA Form 483 so that the agency judges the corrective actions adequate, and whoever closes the highest share of 483s without a warning letter takes the account.

## The Problem
The front room hosts the investigator; the back room finds, reviews and copies documents for each request, logged in a spreadsheet and chased by phone. Requests pile up late in the day, reviewers skim, and a deviation report with an unexplained gap goes across the table.

## Why It's Still Broken
Inspections are infrequent at any one site, so the process is rebuilt each time by whoever is available, and nobody owns a tool for it.

## What a Fix Looks Like
A request log that parses each request, retrieves candidate documents from the QMS and document system, flags open issues in them (unsigned pages, related open deviations) for back-room review, and records what was given and when, ready for the response.

## Who Feels the Pain
QA staff working through the night of an inspection; site heads who learn of a problem document when it appears on the 483.

## Impact If Fixed
Cutting request turnaround and catching problem documents before they reach the investigator could remove one or two observations per inspection (estimate), each of which needs its own response and CAPA.
