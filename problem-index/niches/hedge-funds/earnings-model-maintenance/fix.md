# The Hardcoded Number Nobody Can Trace

**Niche:** [[niches/hedge-funds/earnings-model-maintenance/profile|Earnings Model Maintenance]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Fix (Pain Point)
**One-liner:** A typed-in actual in a model has no source, and when it is wrong nobody can tell where it came from.
**Tags:** #evaluation-metrics #feature-engineering #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to get a reported quarter into the analyst's own model template, correctly mapped and source-linked, before the conference call starts — and whoever does it in the analyst's template rather than a vendor's takes the account.

## The Problem
Analysts type actuals into models under time pressure. A transposed digit or a figure from the wrong period flows through to estimates and to the PM's view, and the cell carries no record of its source.

## Why It's Still Broken
Excel does not record provenance and analysts have no time to annotate.

## What a Fix Looks Like
Source links for every populated actual, and a reconciliation pass that checks hand-entered figures against the filing and flags mismatches before the model is shared.

## Who Feels the Pain
Analysts whose errors become visible at the worst moment; PMs sizing on wrong numbers.

## Impact If Fixed
Model errors caught before they drive decisions, at almost no cost to the analyst.
