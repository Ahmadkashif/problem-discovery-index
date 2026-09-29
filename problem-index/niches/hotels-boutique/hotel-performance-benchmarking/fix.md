# The Analysts Know Which Submissions Are Wrong and Fix Them by Hand

**Niche:** [[niches/hotels-boutique/hotel-performance-benchmarking/profile|Hotel Performance Benchmarking & Demand Data]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Fix (Pain Point)
**One-liner:** Data quality is the product's foundation and it is maintained by people who recognize a bad number when they see it.
**Tags:** #anomaly-detection #tacit-knowledge-ml #data-integration #worker-facing #automation

## The Problem
Hundreds of thousands of properties submit daily performance data, and a meaningful share of it is wrong. A hotel reports rooms sold including comps one month and excluding them the next. A property under renovation reports against its full room count. A management company changes accounting systems and revenue arrives net of tax where it used to be gross. A submission is duplicated, or missed and back-filled as a lump.

Analysts catch these. They know that this market's numbers always look strange in the first week of the month because of one contributor's reporting calendar, that this brand's properties report revenue differently after a system migration, that a particular submitter's data needs checking every quarter. The knowledge is specific, accurate, and stored in the analysts.

The automated checks are ranges and thresholds — occupancy above 100%, revenue outside a band — which catch the obvious and miss almost everything an analyst would notice.

## Why It's Still Broken
Quality work is invisible when it succeeds. There is no line item for corrections prevented, so the function is staffed to keep up rather than to improve, and improvement means building something rather than clearing the queue.

The corrections themselves are not recorded as data. An analyst fixes a submission, or contacts a contributor, and the outcome is a corrected number. What was wrong, how they recognized it, and what the underlying cause turned out to be is not captured in any form a system could learn from. Years of expert anomaly detection have produced no training set.

And contributor relationships make it delicate. Telling a hotel its data is wrong is a conversation, and the reciprocity model depends on those relationships staying good. That has made the function conservative about anything automated that might generate an unnecessary one.

## What a Fix Looks Like
Record what the analysts already do, and let the panel check itself.

**Corrections as structured records.** Every intervention becomes a labelled example: what was submitted, what was wrong, what class of problem it was, what caused it, how it was resolved. This is a training set the business has been generating for years and discarding at every step.

**Contributor-specific expectations.** A property's plausible range is not a global threshold; it is its own history, its market's pattern, and its own reporting behaviour. A property that has never reported above 85% occupancy submitting 97% is an alert even though 97% breaks no rule.

**Cross-property consistency.** The panel's real advantage is that properties in the same market move together. A single property reporting a strong night in a flat market is checkable in a way that no single-property rule can be, and it catches the errors that sit comfortably inside every range.

**Analyst knowledge as durable annotations.** Contributor quirks — reporting calendars, system migrations, chronic definitional confusion — attached to the contributor, dated, and visible to whoever handles that account next. Today they live in the analyst who has covered that region for six years.

**Alerts ranked by consequence.** An error in a small market with few contributors moves the published index; an identical error in a large market does not. Prioritizing by effect on the output rather than by size of the discrepancy focuses limited attention where it changes the product.

## Who Feels the Pain
Analysts, doing skilled work that leaves no trace and cannot be handed over. The head of data quality, whose function's capability is a set of tenures. Contributors, who occasionally get asked about data that was fine and occasionally do not get asked about data that was not. And every subscriber, whose index moved for a reason that was somebody's spreadsheet.

## Impact If Fixed
This is a business whose entire value is that its numbers are trusted. Quality currently rests on individuals recognizing patterns they cannot articulate, at a scale that grows every year. Turning that recognition into a system that learns from it is the difference between a function that keeps up and one that improves — and it is the cheapest available improvement to the accuracy of a benchmark the whole industry is measured against.
