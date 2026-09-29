# Farm Office Record Reconciliation

**Industry:** [[agtech-platforms|Agtech Platforms]]
**Type:** Worker Life Changing
**One-liner:** The person keeping the farm's records stops spending the winter reconciling machine files, input invoices, custom operator paperwork and landlord statements into one story about what happened on each field.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #data-integration #worker-facing

## The Problem
Every farm has someone who keeps the records, and on most family operations it is a spouse, a parent or a part-time bookkeeper working alongside the field operation. The job is to produce, for each field, an accurate account of what was applied, what was harvested, what it cost and who is owed what.

The inputs arrive from everywhere and agree about nothing. Machine data in several brands' formats with inconsistent field names. Input invoices from two or three retailers with product names that do not match the plan or the machine record. Custom applicator tickets on paper. Grain tickets from the elevator with splits between landlords. Crop insurance acreage reports with their own field designations. Landlord agreements with share arrangements that vary by field.

Reconciling this is winter work. Field by field, invoice by invoice, matching a product on a ticket to a product in a machine record to a line on a bill, allocating costs across fields that were sprayed in one pass, and splitting proceeds with landlords under different arrangements.

## Why It Matters to the Worker
This is one of the least visible jobs in agriculture and one of the most consequential. The records determine crop insurance claims, landlord settlements, lender reporting, tax position and every cost-per-acre number the operation uses to decide anything.

It is done under time pressure in winter, by one person, often without a formal accounting background, on a set of documents that were never designed to reconcile. Errors are discovered at the worst moments — during a claim, at a landlord settlement, in an audit.

It is also isolating and unacknowledged. The field operation is visible and celebrated; the reconciliation happens at a kitchen table in January. When the person doing it is unavailable, nobody else on the operation can do it, and that dependency is rarely acknowledged until it becomes a problem.

## What a Solution Looks Like
Automatic matching across sources. Invoice lines to products to machine application records is entity resolution with strong signal — the chemistry, the rate, the date and the acres all constrain the match — and it is the single largest piece of the work.

Field identity resolved once across every system, so the machine record, the insurance acreage report, the landlord agreement and the invoice all refer to the same field without anyone maintaining a translation table in their head.

Cost allocation applied automatically for multi-field passes and for shared inputs, under rules the operation states once rather than reapplies each season.

Landlord settlements generated from the reconciled record with the share arrangement applied, which is the most delicate output the office produces and the one most damaged by an error.

And gaps surfaced during the season rather than in January: this field has no planting record, this invoice has not been matched, this application has no product.

## Impact If Solved
The farm record is the basis for insurance, landlord relationships, lending and every management decision, and it is assembled once a year by one person from documents that do not reconcile. Doing it continuously and automatically removes a winter of work and makes the numbers the operation manages by trustworthy for the first time.
