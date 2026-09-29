# Implementation Consultant Migration Grind

**Industry:** [[healthcare-practice-software|Healthcare Practice Software]]
**Type:** Worker Life Changing
**One-liner:** Implementation consultants stop spending their nights hand-mapping a decade of somebody else's database into spreadsheets and start doing the configuration work they were hired for.
**Tags:** #large-language-models #bert #word-embeddings #k-nearest-neighbors #feature-engineering #evaluation-metrics #transfer-learning #worker-facing

## The Problem
When a practice switches EHR vendors, an implementation consultant is assigned to move it. The practice has ten or fifteen years of history in a competitor's system: patients, insurance policies, appointments, problem lists, medications, allergies, immunisations, documents, outstanding balances and open claims. Some of it exports cleanly. Most of it arrives as a flat extract with column names invented by another company, free-text fields carrying meaning that was never in a code, custom fields nobody can explain, and duplicate patients created over a decade of front-desk turnover.

The consultant maps it by hand. Open the extract, open the target schema, work out what a column named PT_STAT_2 means by looking at its values, build a crosswalk in a spreadsheet, run a test load, review the errors, adjust, repeat. Go-live is a fixed date, usually a weekend, and the last two weeks before it run long. Consultants carry three or four of these concurrently.

## Why It Matters to the Worker
This is skilled work being spent on the least skilled part of the job. Implementation consultants are hired for clinical workflow knowledge — configuring a practice so that its actual patterns of care fit the software — and that is the part clients remember and the part that determines whether an account succeeds. Instead the majority of the engagement is data janitorial work performed under deadline pressure.

The failure mode is personal. A migration that drops allergy data or mis-maps balances is discovered on the first clinical day, in front of the client, and the consultant is the person in the room. That risk sits on individuals who had no control over the quality of the source extract, and it is the reason burnout and turnover in implementation teams runs high in a role that takes a year to become good at.

## What a Solution Looks Like
Schema mapping proposed rather than authored. The vendor has performed thousands of migrations from the same twenty source systems; the crosswalks are largely repeats, and a model trained on prior mappings can propose a field-level mapping with a confidence score and let the consultant confirm or correct. Ambiguous columns get inferred from their values, not their names.

Free-text clinical fields get structured rather than dumped — extracting medications, allergies and problems from narrative history into coded entries, flagged for review rather than silently trusted. Duplicate patients get identified probabilistically with the uncertainty shown. Reconciliation reports run continuously through the load rather than as a post-mortem, so a mis-mapped balance surfaces during testing instead of on the first Monday.

## Impact If Solved
Implementation is where accounts are won or lost and where the vendor's most expensive people spend their time on the least valuable task. Giving consultants their expertise back shortens go-live, raises the quality of the configuration clients actually experience, and retains people the vendor spent a year training.
