# Network Upgrade Tables Retyped From Study PDFs

**Niche:** [[niches/renewable-power-producers/interconnection-queue-strategy/profile|Interconnection Queue Strategy & Development Pipeline]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Fix (Pain Point)
**One-liner:** Cluster study results, the upgrade costs that decide whether a position lives, arrive as PDF reports that analysts retype into spreadsheets under a deposit deadline.
**Tags:** #large-language-models #transformers #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to put money only behind queue positions that will survive their network-upgrade assignments, and whoever has the lowest share of queued megawatts withdrawn after the first cluster study takes the account.

## The Problem
Each grid operator publishes cluster study reports in its own layout, with upgrade lists, cost allocations and affected-system notes spread across tables and appendices. Analysts retype them to compare positions before the readiness deposit is due, and errors carry straight into the keep-or-drop decision.

## Why It's Still Broken
Formats differ by operator and change between clusters, reports run to hundreds of pages, and nobody owns the cross-cluster archive that would show how assigned costs moved from study to restudy.

## What a Fix Looks Like
Extraction that reads each report into one schema (request, upgrade, cost share, phase, affected systems), links every number to its page, flags low-confidence cells, and keeps the history so the change in each position's assigned cost between studies is visible.

## Who Feels the Pain
Interconnection analysts working deposit deadlines; development heads deciding on incomplete comparisons; acquirers diligencing portfolios.

## Impact If Fixed
Turning ~3 analyst days of retyping per cluster report into ~2 hours (estimate) frees ~100 days a year at a developer holding 40 positions, and catches transcription errors before ~$3–6M deposits are posted.
