# The Missing Trial Summary File

**Niche:** [[niches/biotech-research-firms/send-dataset-production/profile|SEND Dataset Production]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Fix (Pain Point)
**One-liner:** FDA's own figures show that most nonclinical studies rejected under rule 1734 failed for one missing file, which a pre-submission checklist would catch.
**Tags:** #evaluation-metrics #compliance #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to produce SEND datasets that pass FDA's technical rejection criteria and match the study report the first time, from whatever system the study ran on, and whoever closes the gap between report and dataset fastest takes the account.

## The Problem
Between 15 September 2021 and 15 February 2023, 453 IND, NDA and BLA nonclinical studies failed FDA rule 1734; 329 of them (73%) because the ts.xpt trial summary file was missing. Many were studies started before SEND applied, for which FDA only wants a simplified trial summary.

## Why It's Still Broken
Submission assembly happens in regulatory operations, far from the SEND team, and the rule for older studies is a detail nobody owns.

## What a Fix Looks Like
A gate in the submission build that lists every study in Module 4, determines from its start date whether full SEND or a simplified ts.xpt is required, and blocks publication until each is present and valid.

## Who Feels the Pain
Regulatory operations staff; sponsors whose submission is rejected on a technicality before review starts.

## Impact If Fixed
The commonest nonclinical rejection eliminated at almost no cost.
