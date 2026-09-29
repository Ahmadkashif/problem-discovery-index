# Every Plan Study Is Rebuilt From Scratch and Nothing Accumulates

**Niche:** [[niches/gyms-independent/fitness-benefit-network-analytics/profile|Fitness Benefit Network Analytics]]
**Industry:** [[industries/gyms-independent|Independent Gyms]]
**Type:** Fix (Pain Point)
**One-liner:** The team runs the same analysis for forty health plans a year, forty separate times, and finishes each year knowing no more than it did at the start.
**Tags:** #workflow-orchestration #data-integration #automation #worker-facing

## The Problem
Renewal season means a stack of plan-specific analyses on a fixed deadline. Each one asks nearly the same questions — participation, engagement depth, cohort comparisons, cost trend — against a population defined slightly differently, using an eligibility file with its own quirks, delivered in the plan's preferred format.

So each one gets built by hand. An analyst pulls the eligibility file, reconciles it against check-ins, decides how to handle the members who appear mid-year, picks a comparison group, and writes it up. The next plan's analyst makes the same decisions independently and reaches slightly different ones. Two studies of the same programme, produced by the same team in the same month, are not comparable — and neither is comparable to last year's version, because the analyst who built that one has moved on.

The team is busiest exactly when the work is most repetitive, and the repetition produces nothing that makes next year easier.

## Why It's Still Broken
Deadline pressure is self-reinforcing. Renewal analyses land in a cluster, every one is contractually committed, and the fastest path through any individual study is to copy the last similar notebook and change the filters. Building the shared layer would take a quarter that never exists, because the quarter after renewals is spent on the studies that slipped.

Underneath that is a definitional problem nobody owns. What counts as an active member, how a mid-year enrolee is treated, whether a facility visit and a class booking are the same event — these are answered per study, by whoever is writing it, and the answers were never written down anywhere the next analyst would look. There is no canonical definition because defining it is somebody's job in the abstract and nobody's in particular.

## What a Fix Looks Like
Turn the repeated study into a specified pipeline, and make the definitional choices explicit artefacts rather than analyst habits.

**A metric layer with one definition each.** Active member, engaged member, visit, lapse, cohort — defined once, versioned, and used by every study. Where a plan contractually requires a different definition, that becomes a named variant with the difference recorded, not a silent divergence.

**The standard study as a parameterized pipeline.** Population in, sections out. Ninety percent of a renewal analysis is identical across plans; the plan-specific reasoning is the last ten percent, and that is where the analysts should be spending renewal season.

**A results register.** Every study's headline numbers, method version, and population, stored so they can be compared. Three years of these is a genuine longitudinal picture of what the benefit does across plan types, populations, and designs — the most valuable analytical asset the company could have, currently scattered across individual analysts' notebooks and slide decks.

**Reproducibility as the default.** Any study should rerun from its parameters. Today a question about a study from eighteen months ago starts with finding the person who wrote it.

## Who Feels the Pain
Analysts, who spend renewal season doing work they have done before and cannot point to anything that accumulated. The head of analytics, defending numbers that differ between decks for reasons nobody can reconstruct. And the plan clients, who receive a report that cannot be compared to the one they received last year.

## Impact If Fixed
Renewal season stops consuming the team. More importantly, the studies start compounding: a results register spanning several years and dozens of plans answers questions about programme design that no single study can, and it is built entirely from work the team is already doing and currently discarding.
