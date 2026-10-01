# The Formula That Broke When the Field Changed

**Niche:** [[niches/financial-data-vendors/terminal-desktop-workflow/profile|Terminal & Desktop Workflow]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A vendor changes a field definition, a template or a methodology, and every client model referencing it silently returns a different number with no warning.
**Tags:** #evaluation-metrics #descriptive-statistics #data-integration #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to be the surface where the analyst's model actually gets built — the Excel add-in, the API pull and the screen that feeds the memo — and whoever is embedded in that workflow keeps the seat when the client's market data office comes looking for cuts.

## The Problem
Vendors revise standardised field definitions, retire mnemonics, change how a fiscal period is aligned or restate a history under a new policy. Each is announced in release notes few users read. Client models referencing those fields refresh and return different values with no error. The analyst notices when an output moves for no reason, or does not notice and a number in a published report or pitch book is wrong.

## Why It's Still Broken
The vendor knows what changed but not who depends on it; the client depends on it but does not know it changed. Release notes are written for the product team, not for the model owner. And a silent value change is not a bug in either system, so nobody owns it.

## What a Fix Looks Like
Treat a definition change as a breaking API change. Publish a machine-readable change log keyed to fields. Have the add-in check each workbook's referenced fields against it on refresh and show, cell by cell, which values changed because of a definition change rather than new data, with the before and after. Offer a pinned-definition mode for models that must reproduce a past number. Report to the vendor, in aggregate, how many workbooks a planned change would touch, before shipping it.

## Who Feels the Pain
Analysts and associates whose models move for reasons they cannot see, the compliance teams who must reproduce numbers in published documents, and the vendor's support desk, which fields the resulting questions.

## Impact If Fixed
Silent definition changes are a recurring source of wrong numbers in client deliverables and of support tickets. Flagging them at refresh time is a small engineering change with an outsized effect on trust.
