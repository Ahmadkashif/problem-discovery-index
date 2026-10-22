# The Tolerance Column Left Blank

**Niche:** [[niches/specialty-design-studios/grading-and-spec-sheet-production/profile|Grading & Spec Sheet Production]]
**Industry:** [[industries/specialty-design-studios|Specialty Design Studios]]
**Type:** Fix (Pain Point)
**One-liner:** A spec goes to the factory with points of measure that have no tolerance, and the factory decides what "in spec" means.
**Tags:** #logistic-regression #bert #quick-win #automation #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to produce a complete, graded, tolerance-correct spec and bill of materials from a sketch and a base block in minutes rather than hours, and whoever gets round-one factory questions closest to zero takes the account.

## The Problem
Missing tolerances, unspecified trims and ambiguous callouts are among the most-cited causes of re-samples. They are mechanical omissions in documents assembled under time pressure.

## Why It's Still Broken
Nobody checks a pack line by line before it ships; PLM templates allow blank fields.

## What a Fix Looks Like
A pre-send check that flags blank tolerances, trims with no supplier reference, callouts that a classifier trained on past factory questions marks as ambiguous, and labelling fields left empty, before the pack can be released.

## Who Feels the Pain
Technical designers answering avoidable factory questions; factories guessing; brands paying for the round.

## Impact If Fixed
A whole category of factory question and avoidable round removed for minutes of checking.
