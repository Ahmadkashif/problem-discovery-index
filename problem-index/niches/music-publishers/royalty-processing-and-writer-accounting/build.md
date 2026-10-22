# Statement Ingestion That Learns Every Match

**Niche:** [[niches/music-publishers/royalty-processing-and-writer-accounting/profile|Royalty Processing & Writer Accounting]]
**Industry:** [[industries/music-publishers|Music Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every new statement layout is a developer ticket and every unmatched title is a person's afternoon, at every publisher, every period.
**Tags:** #large-language-models #k-nearest-neighbors #gradient-boosting #feature-engineering #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every incoming statement line into the right writer's account by the contractual statement date, with each figure traceable to its source so that a writer's audit finds nothing, and whoever does that at volume becomes the royalty department's system of record.

## The Problem
Statements change layout without warning, sub-publishers use local titles and codes, and a few percent of lines never match automatically. Those lines decide whether the department meets its deadline.

## Why Nobody Has Built This
Royalty systems were built as ledgers with fixed importers. The matching knowledge, such as which local title is which song and which society code maps where, lives in analysts' heads and spreadsheets.

## What to Build
An ingestion layer that infers a statement's schema from a sample. It matches lines to works using writer names, IPI numbers, ISWC, title variants, performer, duration and the source's history, with calibrated confidence, and turns every manual match into a rule. It also flags amounts that look wrong for the work and source, and posts traceable entries into the existing system of record.

## Target Customer
Royalty heads at independent publishers and administrators running Vistex, Curve or in-house systems.

## Impact If Built
Suspense cleared in days, deadlines met without overtime and an audit trail for every line.
