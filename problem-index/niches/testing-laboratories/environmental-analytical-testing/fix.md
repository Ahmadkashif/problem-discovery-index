# The Case Narrative Written by Hand for Every Data Package

**Niche:** [[niches/testing-laboratories/environmental-analytical-testing/profile|Environmental Analytical Testing]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** Every data package carries a narrative explaining each QC exception, and analysts write it from scratch from the same data the LIMS already holds.
**Tags:** #large-language-models #transformers #compliance #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to return a defensible, accreditation-compliant result inside each method's holding time at a per-sample price consultants and utilities will accept, and whoever runs the densest automated lines — PFAS above all — takes the monitoring contracts.

## The Problem
For each sample delivery group, the lab explains what went wrong and what it means: a surrogate outside limits, a matrix spike that failed because of the sample, a dilution that raised reporting limits, a holding time missed, a manual integration. Data validators and regulators read these narratives closely. Analysts write them at the end of the review, by hand, under turnaround pressure, and quality varies by writer.

## Why It's Still Broken
The facts are all structured — QC flags, limits, dilution factors, audit-trail events — but they live across the LIMS and the chromatography data system, and the narrative template is free text. Nobody connected the exceptions to standard explanatory language the lab has already approved.

## What a Fix Looks Like
Generate the narrative draft from the exception flags and audit trail using the lab's approved phrasing for each exception type, with links back to the underlying records; the analyst edits and signs. Track which exceptions recur by client site and method as a quality signal.

## Who Feels the Pain
Analysts and reviewers writing narratives at the end of long batches; project managers fielding validators' questions; consultants whose validators find narratives inconsistent.

## Impact If Fixed
Twenty to forty minutes saved per data package (estimate), consistent explanations validators accept first time, and a structured record of exceptions the quality manager can trend.
