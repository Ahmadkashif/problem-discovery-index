# The Re-Segmentation Nobody Noticed

**Niche:** [[niches/sell-side-equity-research/model-maintenance/profile|Model Maintenance]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Fix (Pain Point)
**One-liner:** A company changes its segment reporting and the model keeps filling the old rows with numbers that no longer mean the same thing.
**Tags:** #change-point-detection #evaluation-metrics #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to get reported numbers into each analyst's own model layout — correct, sourced and with presentation changes flagged — within minutes of the release.

## The Problem
Re-segmentations, restatements and KPI redefinitions are announced in footnotes; the model fill does not notice.

## Why It's Still Broken
Nobody compares this quarter's presentation to last quarter's systematically.

## What a Fix Looks Like
A presentation diff on every release — segment names, definitions, restated history — routed to the analyst before the fill.

## Who Feels the Pain
Analysts and associates whose estimates are later shown to be on a stale basis.

## Impact If Fixed
Fewer silent model errors in published estimates.
