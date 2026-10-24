# The Portfolio Model That Forgets Why a Molecule Was Chosen

**Niche:** [[niches/pharmaceutical-manufacturers/generic-oral-solid-dose-portfolios/profile|Generic Oral Solid Dose Portfolios]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** The spreadsheet that justified a filing is overwritten each quarter, so when a molecule disappoints nobody can see which assumption failed.
**Tags:** #large-language-models #descriptive-statistics #evaluation-metrics #data-integration #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to earn money on a molecule after the brand's exclusivity ends, but first-to-file launches and mature-molecule supply reward different things: a launch is won by whoever is first lawfully on the market with exclusivity, a mature molecule by whoever keeps shipping an awarded contract at an eroded price without a failure-to-supply penalty. Decomposed into contested sub-niches below.

## The Problem
Portfolio forecasts live in one workbook per molecule or one giant model, updated as entry dates and competitor counts change. The original assumptions behind the decision to file are overwritten.

## Why It's Still Broken
Nothing in the workflow asks for the decision record to be frozen, and the people who made the call are rarely around when the outcome is known.

## What a Fix Looks Like
Snapshot every forecast at each decision gate (select, file, launch) with its key assumptions in a structured record, and compare automatically with actuals each quarter, so variances are attributed to entry timing, entrant count, price or cost.

## Who Feels the Pain
Portfolio heads defending selection to the board; finance teams explaining write-downs; analysts inheriting molecules chosen by predecessors.

## Impact If Fixed
A frozen decision record costs about 15 minutes per decision gate and turns every disappointing launch, perhaps a third of a portfolio's launches, into a lesson the next selection can use (both estimates).
