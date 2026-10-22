# Boilerplate Requirements Copied From the Last File

**Niche:** [[niches/title-and-settlement-offices/search-exam-production/profile|Title Search & Examination Production]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Fix (Pain Point)
**One-liner:** Commitments carry requirements that do not apply to the file because the examiner started from the last one, and the escrow officer chases them anyway.
**Tags:** #large-language-models #bert #evaluation-metrics #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a clean chain into an underwriter-acceptable commitment in minutes and send only the genuinely defective chains to an examiner, and whoever draws that line most accurately takes the lender channel's refinance and purchase volume.

## The Problem
Examiners build commitments fast from templates or prior files. A spousal joinder requirement on an unmarried seller, an estate requirement already satisfied of record, a survey requirement on a condominium unit — each sends the escrow team chasing something that does not exist and delays clear-to-close.

## Why It's Still Broken
Production systems do not check requirements against the facts in the search package, and nobody measures how many raised requirements were later waived as inapplicable.

## What a Fix Looks Like
Check each requirement against the vesting deed, marital status, property type and recorded instruments before the commitment is issued, and flag those with no supporting fact; report the waiver rate by requirement type and examiner.

## Who Feels the Pain
Escrow officers and processors; agents and buyers waiting on clear-to-close.

## Impact If Fixed
Fewer phantom requirements, faster clear-to-close, and a measure of commitment quality.
