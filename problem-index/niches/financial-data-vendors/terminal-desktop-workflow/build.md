# The Model the Add-In Cannot See

**Niche:** [[niches/financial-data-vendors/terminal-desktop-workflow/profile|Terminal & Desktop Workflow]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The vendor's Excel add-in feeds thousands of client models every day and has no idea what any of them compute, so it cannot tell an analyst which of their assumptions just went stale.
**Tags:** #large-language-models #graph-theory #feature-engineering #evaluation-metrics #worker-facing #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to be the surface where the analyst's model actually gets built — the Excel add-in, the API pull and the screen that feeds the memo — and whoever is embedded in that workflow keeps the seat when the client's market data office comes looking for cuts.

## The Problem
An equity analyst's model is a workbook of several thousand cells, a few hundred of which are pulled from the vendor by formula and the rest of which are the analyst's own assumptions. When the company reports, the add-in refreshes the historical cells. Nothing tells the analyst that their revenue growth assumption for the next year is now inconsistent with the guidance just given on the call, that a segment they model was redefined in the filing, or that a peer's margin they benchmark against was restated. The analyst finds out by re-reading everything, which is what earnings night consists of.

## Why Nobody Has Built This
The vendor sees the formula calls, not the workbook, and clients would be uneasy about a vendor reading their models. The add-in was built as a data pipe and is owned by a delivery team, while the content that would make it intelligent — guidance, segment definitions, restatements — is owned by different teams. And the commercial value of depth of embedding is real but shows up only at renewal, two budget cycles after the build.

## What to Build
A model-aware layer that runs locally in the client's workbook. Map the dependency graph of the model so the add-in knows which assumptions drive which outputs. Link vendor-sourced cells to events — new guidance, segment redefinition, restatement, consensus moves — and flag the assumptions those events touch, with the source passage. Diff a refreshed model against its prior state and summarise what changed and why. Keep the workbook on the client's machine so nothing proprietary leaves it; the vendor ships the event stream, the client's environment does the matching. Instrument, with consent, whether vendor data reached the model's outputs, which is the usage metric that actually predicts renewal.

## Target Customer
Desktop and Office-integration product leadership at terminal vendors, and the smaller model-data specialists whose entire proposition is the Excel workflow.

## Impact If Built
Earnings night is spent re-reading because the tool feeding the model cannot see it. A model-aware add-in turns the vendor from a number supplier into the system that tells the analyst what to revisit, which is the deepest form of embedding available and the hardest seat to cut.
