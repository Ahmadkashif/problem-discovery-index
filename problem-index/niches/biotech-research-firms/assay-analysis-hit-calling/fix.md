# The Masked Well With No Reason

**Niche:** [[niches/biotech-research-firms/assay-analysis-hit-calling/profile|Plate-Based Assay Analysis & Hit Calling]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A well is excluded from a curve and the potency moves threefold, and nobody can later say who excluded it or why.
**Tags:** #evaluation-metrics #hypothesis-testing #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn plate-reader output into curve fits and hit calls scientists accept without re-checking, with every masking and refit decision recorded, and whoever makes analysis both same-day and auditable takes the account.

## The Problem
Masking is a legitimate scientific decision that changes results. Most tools record that a well was masked but not the reason, so a partner's diligence team or a new scientist cannot tell a justified exclusion from a convenient one.

## Why It's Still Broken
Reason fields are optional and slow to fill, and nothing downstream uses them.

## What a Fix Looks Like
Required reason codes for every mask (edge effect, replicate outlier, precipitation, instrument error), defaulted from automatic QC flags, and a report of masking frequency by assay and scientist.

## Who Feels the Pain
Research associates defending their analysis; discovery heads answering partner questions; anyone trying to reproduce a historical result.

## Impact If Fixed
An auditable analysis record at almost no extra effort.
