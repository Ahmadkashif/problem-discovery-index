# Certification as a Checkable Set

**Niche:** [[niches/game-porting-studios/certification-requirements/profile|Certification & Platform Requirements]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of requirements per platform, published as prose, verified by a person with a spreadsheet.
**Tags:** #compliance #workflow-orchestration #automation #evaluation-metrics #large-language-models #data-integration #sets-and-logic #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to satisfy several platforms' certification regimes from requirement documents written in prose, where a late failure costs a release window — and whoever makes compliance checkable takes the account.

## The Problem
Certification is a large, exacting, repetitive body of work. Each platform publishes hundreds of requirements in prose; a specialist reads them, maps them to the game, tracks implementation, arranges verification, and prepares a submission. Requirements overlap between platforms in ways nobody has formalised, change between document versions in ways nobody diffs, and a failure discovered at submission costs weeks and sometimes a release window.

## Why Nobody Has Built This
The documents are confidential per platform, which discourages shared tooling. Each studio builds its own spreadsheet. Many requirements need judgement rather than a check. And the platform holders have no incentive to make their requirements machine-readable.

## What to Build
Turn the documents into a structured set and automate what is testable. Convert each platform's requirements into a structured, versioned set with a stable identifier per requirement, which is the core and makes everything else possible. Diff requirement sets between document versions so changes are surfaced rather than discovered, since a silently changed requirement is the classic late failure. Map equivalent requirements across platforms, which lets one piece of work satisfy several and is currently done from memory. Automate the mechanically testable requirements — suspend and resume, controller disconnect, storage full, network loss, account state changes — as those are a large fraction and are entirely scriptable. Track implementation and verification status per requirement per platform in one place rather than in a spreadsheet per project. Reuse compliance work across projects on the same engine, which is where the duplication is. Flag requirements historically associated with failures, since the distribution is uneven and known. Generate the submission documentation from the tracked status. Run the automated checks continuously rather than at submission, which is what moves the failure earlier. And keep the specialist's judgement central for the requirements that genuinely need it, which is a smaller set than the current process treats as such.

## Target Customer
Porting and co-development studios, publisher certification teams, platform holders, and compliance tooling vendors.

## Impact If Built
Hundreds of prose requirements per platform, tracked in a spreadsheet, with failures discovered at submission. A structured versioned set with automated checks moves the failure to the week it was caused.
