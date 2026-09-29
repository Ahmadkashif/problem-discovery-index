# Cohort Analysis Adapted to Anthropometric Shape

**Niche:** [[niches/alterations-tailoring/body-scan-fit-standards/profile|Body Scan & Fit Standard Consultancies]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical and BI tooling handles cohorts defined by columns; a fit cohort is defined by a shape, and there is no column for "bodies whose shoulder slope exceeds the grading assumption."
**Tags:** #pca #dimensionality-reduction #manifold-learning #gaussian-mixture-models #k-means-clustering #descriptive-statistics #confidence-intervals #evaluation-metrics #automation #workflow-orchestration

## The Problem
The recurring analytical job is to characterize a client's target consumer and show where the client's current size chart fails them. That means defining a population, cutting it by demographics and geometry, comparing it to the client's declared target body, and quantifying the mismatch garment region by garment region. The analysis is genuinely repetitive in structure and completely bespoke in execution: each engagement is built in a statistical script by an analyst, from scratch, with the geometric definitions re-implemented every time. Two analysts asked to define "petite with a full bust" in the same market will produce different populations, and neither definition is recorded anywhere the next engagement can find.

## What Already Exists
The analytical toolkit is mature and cheap. R and Python with the standard scientific stack handle every statistical operation involved; Hex, Deepnote, and Posit Connect provide parameterized, shareable notebooks with scheduled execution; Tableau and Power BI cover client-facing presentation. For scalar cohort definition, BI semantic layers already do the job well.

## The Customization Gap
The mismatch is in what a cohort is. Every one of these tools expresses a cohort as a predicate over columns, which covers demographics and single measurements and stops exactly where this work starts. The cohorts that matter here are geometric — defined by relationships between measurements, by posture, by shape components rather than girths — and expressing them in a column-based tool means an analyst hand-coding the geometry each time, which is why nothing is reusable. The adaptation needed is a cohort layer whose primitives are anthropometric: named, versioned shape definitions that can be composed, applied across capture waves, and cited in a deliverable. Alongside it, a fit-gap primitive that takes a cohort and a size chart and returns per-region coverage — the calculation at the centre of every engagement, currently rewritten every time. Deliverable generation then draws from the same definitions, so the chart in the client report and the analysis behind it cannot drift apart.

## Target Customer
Analytics leads and senior consultants running fit standard engagements, and the technical design teams at client brands who receive these analyses and cannot currently reproduce or interrogate them.

## Impact If Solved
Engagement delivery compresses toward the interpretive work, and the firm gains something it does not have: a house definition of every commonly used body shape, versioned and consistent across clients and years. That consistency is directly commercial — a brand that bought a fit standard three years ago and wants to know what changed can be given a real answer rather than a fresh study built on incomparable definitions.
