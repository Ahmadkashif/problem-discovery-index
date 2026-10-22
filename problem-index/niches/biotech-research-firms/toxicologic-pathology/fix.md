# Peer-Review Changes Carried Through the Report by Hand

**Niche:** [[niches/biotech-research-firms/toxicologic-pathology/profile|Toxicologic Pathology & Histopathology Reads]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Fix (Pain Point)
**One-liner:** When a peer-reviewing pathologist disagrees, the agreed changes are reconciled in spreadsheets and meetings, then re-keyed into the study system, tables and SEND.
**Tags:** #large-language-models #evaluation-metrics #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to deliver a pathology read that survives peer review and FDA scrutiny on the study's timeline despite a thin bench of board-certified toxicologic pathologists, and whoever multiplies each pathologist's throughput without weakening the diagnosis takes the account.

## The Problem
Peer review samples slides from the study, compares the reviewer's findings to the study pathologist's, and resolves differences. Each agreed change must be propagated to the pathology data, incidence tables, narrative and SEND. Missed propagation is a common source of report inconsistencies and late QA findings.

## Why It's Still Broken
Peer review is often done by a different organisation from the original read, on a different system, with the record of disagreements kept as a memo. Nothing captures disagreement as structured data, so the same differences recur.

## What a Fix Looks Like
A structured peer-review record per slide — original finding, reviewer finding, resolution — that drives automatic updates to the study data and flags every downstream table and dataset affected. Over time it also shows which lesion types the two pathologists most often disagree on.

## Who Feels the Pain
Study pathologists and peer reviewers; study directors chasing consistency; QA.

## Impact If Fixed
Days removed from the end of every study, at the bottleneck the niche competes on.
