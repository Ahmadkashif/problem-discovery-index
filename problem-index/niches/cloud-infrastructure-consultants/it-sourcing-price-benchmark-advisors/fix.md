# Comparability Judgments Live in the Analyst, Not the Database

**Niche:** [[niches/cloud-infrastructure-consultants/it-sourcing-price-benchmark-advisors/profile|IT Sourcing & Price Benchmark Advisors]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Deciding which prior deals are comparable to the client's situation is the entire analytical act, it is made from memory by whoever is assigned, and the database records only the answer.
**Tags:** #tacit-knowledge-ml #k-nearest-neighbors #feature-engineering #contrastive-learning #evaluation-metrics #descriptive-statistics #confidence-intervals #data-integration #worker-facing #workflow-orchestration

## The Problem
A benchmark is a comparable set plus adjustments, and building it is where the expertise lives. An analyst decides which prior transactions resemble this client's situation — similar enough in product configuration, volume, term, industry, geography, and negotiating posture — and how to adjust for the differences that remain. The decisions are consequential and undocumented. The deliverable records the resulting number and a description of methodology; it does not record which transactions were included, which were considered and rejected, or why. So the firm cannot measure whether two analysts given the same brief would produce the same benchmark, cannot explain a benchmark when a vendor disputes it, and cannot transfer the judgment to anyone new except by apprenticeship. Senior analysts are the product, and the firm's capacity is bounded by how many of them exist.

## Why It's Still Broken
The work is done under engagement deadlines where documentation reads as overhead, and the deliverable the client pays for does not require the comparable set to be disclosed — indeed contributor confidentiality often argues against disclosing it. Comparability is also treated as craft rather than as method, which has been broadly true and has therefore gone unexamined. And the database schema reflects its origin as a repository of transactions rather than of analyses, so there is nowhere for a comparable set to be recorded even if someone wanted to record it.

## What a Fix Looks Like
The comparable set as a stored, structured object attached to every benchmark. Which transactions were included, which were considered and rejected with the reason, which adjustments were applied and on what basis, and the analyst's confidence in the result. Capture happens as the analysis is built rather than after, so the cost is close to zero. Once benchmarks carry their comparable sets, several things become possible for the first time. Consistency between analysts is measurable — the same brief can be independently constructed and the sets compared, which is the quality control the firm has never had. Recurring comparability patterns become visible and promotable into house method, so judgment applied consistently by seniors stops being personal and becomes institutional. A disputed benchmark can be explained in terms of its actual basis, under confidentiality, rather than defended by methodology description. And a new analyst learns from a corpus of worked comparability decisions rather than from sitting beside someone for two years.

## Who Feels the Pain
Analysts reconstructing comparability reasoning that colleagues have already worked through; the practice leader whose capacity is capped by senior headcount and who cannot measure consistency; clients receiving benchmarks whose basis they must take on trust; and the firm, whose core method is undocumented and walks out with every departure.

## Impact If Fixed
Converts the firm's differentiating expertise from personal to institutional, which is the constraint on both quality and growth. It also makes everything else tractable — outcome validation is meaningless without knowing which comparables produced the benchmark being validated, so this is the fix the others depend on.
