# Indications Rebuilt Every Time the Model Version Changes

**Niche:** [[niches/property-casualty-insurers/homeowners-cat-load-rate-adequacy/profile|Homeowners Catastrophe Loads & Rate Adequacy]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Fix (Pain Point)
**One-liner:** A new catastrophe model version moves average annual loss by territory, and the carrier spends weeks rebuilding indications and explaining the swing to its own executives before it can explain it to a regulator.
**Tags:** #descriptive-statistics #hypothesis-testing #monte-carlo-methods #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get a modelled catastrophe load and the cost of reinsurance accepted in a rate filing for a high-hazard state, and whoever wins approval for an adequate rate without committing to write more than it can carry takes the account.

## The Problem
Model vendors release new versions with updated hazard, vulnerability and exposure assumptions. Territory-level losses can shift sharply. The pricing team reruns the book, rebuilds indications and must explain which changes came from the science, which from the carrier's exposure data, and which from the vendor's software, before deciding whether to file.

## Why It's Still Broken
Version change analysis is done ad hoc in spreadsheets, and the decomposition of a change into its drivers depends on a modeller's time and memory.

## What a Fix Looks Like
An automated version-change report: rerun the same exposure snapshot on both versions, decompose differences by peril component, region and construction, flag exposure-data artefacts, and draft the indication change with an explanation the filing can reuse.

## Who Feels the Pain
Catastrophe modellers and pricing actuaries, and product heads deciding whether to file.

## Impact If Fixed
Model updates become a routine, explained input to pricing rather than a fire drill.
