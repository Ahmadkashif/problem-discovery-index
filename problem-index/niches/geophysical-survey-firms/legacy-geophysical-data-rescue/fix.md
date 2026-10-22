# The Tape Whose Header Doesn't Match the Map

**Niche:** [[niches/geophysical-survey-firms/legacy-geophysical-data-rescue/profile|Legacy Geophysical Data Rescue]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A transcribed field tape claims to be one line, its shot-point range fits another, and the mismatch is found only when the reprocessed section refuses to tie.
**Tags:** #k-nearest-neighbors #descriptive-statistics #evaluation-metrics #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn decades of paper sections, field tapes and observer logs into correctly navigated, loadable digital data with clean licence title, and whoever does it at the lowest cost per line-kilometre without navigation errors wins the archive.

## The Problem
Legacy data comes in pieces — tapes, sections, maps, observer reports — that were separated over decades of mergers and warehouse moves. Labels are wrong, lines were renamed, and extensions were shot years apart under the same name. Rescue firms reconcile them line by line, and mistakes surface late, after reprocessing money has been spent.

## Why It's Still Broken
Each source is processed by a different step and person; nobody runs a consistency check across all of a line's pieces before work starts.

## What a Fix Looks Like
A reconciliation pass at intake that compares, for every line, the shot-point ranges, dates, contractor and geometry implied by the tape headers, section labels, maps and reports; scores matches; proposes the right pairing where pieces conflict; and blocks a line from reprocessing until conflicts are resolved.

## Who Feels the Pain
Rescue technicians, processors handed mismatched inputs, and library sales staff who license a line that turns out to be in the wrong place.

## Impact If Fixed
Conflicts resolved at intake for minutes of review rather than after weeks of processing.
