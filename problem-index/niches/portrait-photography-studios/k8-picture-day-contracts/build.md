# Zero-Touch School Deliverables

**Niche:** [[niches/portrait-photography-studios/k8-picture-day-contracts/profile|K-8 Picture Day Contracts]]
**Industry:** [[industries/portrait-photography-studios|Portrait Photography Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every school deliverable — ID cards, yearbook package, SIS images, the district's licensed library — could come from one reconciled record, and today each is rebuilt by hand per school.
**Tags:** #large-language-models #k-nearest-neighbors #contrastive-learning #evaluation-metrics #data-integration #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to deliver everything a K-8 school asks of picture day — every child photographed, ID cards within days, yearbook and SIS files, free retakes — right the first time and under a privacy agreement the district trusts, and whoever asks least of the school office keeps the contract.

## The Problem
A studio with a few hundred schools runs a few hundred variations of the same data job: a roster export in that school's quirks, a publisher's PSPA variant, an SIS naming rule, an ID template with the district logo, a retake merge, an opt-out list. Coordinators do it in spreadsheets in October, under deadlines of days.

## Why Nobody Has Built This
Ordering platforms handle sorting and a PSPA export, then stop; the deliverables beyond that differ by district and look like custom work. Studios absorb it as seasonal labour.

## What to Build
A deliverables engine: ingest the roster, reconcile captured images using card scans plus within-job face matching that is discarded after delivery, merge retakes and late enrolments, apply opt-outs, and generate every output from a per-school profile (publisher variant, SIS format, ID template, licence scope). It keeps a log of which image went where, ready for the district's privacy review, and a school-office portal that answers "is my class done?" without a phone call.

## Target Customer
Operations directors at regional volume studios serving roughly 100–2,000 schools (estimate); ordering-platform vendors as partners.

## Impact If Built
Deliverables move from weeks of coordinator time to hours, ID cards meet ten-day clauses, yearbook errors drop toward zero, and the studio can show a district exactly how its children's images were handled.
