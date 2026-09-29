# Analogue Selection Is the Whole Judgment and Is Recorded as a Curve

**Niche:** [[niches/oil-gas-field-services/reserve-engineering-firms/profile|Reserve Engineering Firms]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Fix (Pain Point)
**One-liner:** An engineer decides which wells a future location will resemble, and the report shows the resulting type curve.
**Tags:** #tacit-knowledge-ml #graph-ml #tabular-ml #worker-facing #evaluation-metrics

## The Problem
Most of the value in a reserve report sits in undeveloped locations, and an undeveloped location has no production history. Its estimate comes from analogues: the engineer picks producing wells they judge comparable and builds a type curve from them.

That selection is the estimate. An engineer who has covered a basin for fifteen years knows which wells are genuinely comparable and which look similar and are not — that an operator's early wells used a completion design nobody would repeat, that a section produces differently because of a structural feature, that a neighbouring operator over-reports early rates.

The report shows the type curve and the wells behind it. Why those wells, what was excluded and why, and how confident the engineer was is not recorded in any structured form. So the same basin is re-reasoned each cycle, two engineers reach different estimates for adjacent acreage, and when a senior engineer retires the firm's judgment in that basin degrades with no mechanism to replace it.

## Why It's Still Broken
The report is the deliverable and it is written for an auditor and a lender. It documents method and inputs, and professional standards emphasize that the estimate is the engineer's judgment — which has been taken to mean the judgment need not be decomposed.

Deadline pressure does the rest. Year-end and redetermination seasons are the firm's capacity constraint, and documenting reasoning is time that does not close a file.

And the knowledge is a personal asset. Basin expertise is what makes a senior engineer valuable, and nothing rewards making it portable.

## What a Fix Looks Like
Make analogue selection an explicit, reusable, testable artefact.

**Structured analogue records.** The wells selected, the wells considered and excluded, the reason for each exclusion, and the engineer's confidence — attached to the location, the acreage, and the basin rather than only to the engagement.

**Basin knowledge notes.** Completion vintages that should not be used as analogues, structural features that separate populations, operators whose early reporting is unreliable. This is what two years of basin experience produces and it is written nowhere.

**Retrieval at evaluation.** An engineer working acreage should see the firm's prior analogue reasoning for the area, not rebuild it.

**Test the selections.** When an undeveloped location is eventually drilled, its actual production can be compared to the analogue-based forecast. The firm has decades of these pairs unexamined, and they are the only evidence about whose analogue judgment is good.

**Show dispersion in the report.** An analogue set with wide dispersion and one with tight dispersion produce the same point estimate today, and they are not the same claim.

## Who Feels the Pain
Junior engineers, learning basins by apprenticeship over years. Senior engineers, who are the firm's capacity ceiling and cannot be replicated. Practice leaders, watching basin expertise approach retirement. And every lender and investor relying on an estimate whose central judgment nobody can inspect.

## Impact If Fixed
Analogue selection is where reserve estimates are actually made, and it is undocumented in a profession with an ageing workforce and hard seasonal deadlines. Structuring it compresses the years it takes to develop a basin engineer, makes estimates consistent across a firm, and creates the only feedback loop the discipline has ever had.
