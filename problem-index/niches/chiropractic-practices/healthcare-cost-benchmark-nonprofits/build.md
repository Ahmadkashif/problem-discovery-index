# Benchmark Provenance as a First-Class Product Attribute

**Niche:** [[niches/chiropractic-practices/healthcare-cost-benchmark-nonprofits/profile|Healthcare Cost Benchmark Data Organizations]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A benchmark figure is used to settle an out-of-network payment dispute years after publication, and reconstructing which claims produced it, under which methodology version, is a manual archaeology exercise.
**Tags:** #data-integration #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #compliance #feature-engineering #workflow-orchestration #probability-distributions #revenue-impact

## The Problem
The organization's outputs are cited in payment disputes, arbitration under federal surprise billing rules, regulatory proceedings, and litigation. Every one of those is a demand to explain a number: which claims went into this percentile for this procedure in this geography, under what inclusion rules, computed by which methodology version, on data as of when. The organization can usually reconstruct it, given time, from pipeline code and release notes and someone's memory of what changed. That reconstruction is slow, it is done under adversarial time pressure, and it depends on continuity of staff. For an institution whose entire standing rests on independence and rigour, provenance being a manual exercise rather than a stored property is the wrong exposure to carry.

## Why Nobody Has Built This
The organization was built to produce benchmarks at scale, and the pipeline was optimized for that — computing a release and publishing it, with the inputs treated as an implementation detail. Retaining full lineage across many releases, tens of billions of records, and an evolving methodology is genuinely expensive in storage and engineering terms, and the payoff was invisible until the volume of disputes citing the benchmarks grew. Methodology also evolves for good reasons, and versioning it properly means committing to a discipline that makes every change slower — which is a real cost that has to be argued for before it will be paid.

## What to Build
Provenance as a stored, queryable property of every published figure. Each benchmark carries the exact inclusion criteria, the data vintage, the methodology version, the contributing population characteristics in aggregate, and the sample support behind it, retained for the full period any published figure might be cited. Methodology is versioned as a specification rather than as code, so a change is a reviewable artifact and a prior release remains recomputable exactly as published — which is what "reproducible" has to mean when the audience is an arbitrator. On that base, a provenance response to any external challenge becomes a query returning a defensible account rather than a project. It also enables something the organization currently cannot offer: publishing sample support and uncertainty alongside every figure, so a user knows whether a percentile for an uncommon procedure in a rural geography rests on thousands of claims or on eleven.

## Target Customer
Chief research officers and heads of data products at benchmark organizations, and the arbitrators, regulators, and disputing parties who rely on these figures and currently have no view into what stands behind them.

## Impact If Built
Converts the organization's core vulnerability into its strongest claim. Independence is asserted through governance today; provenance would let it be demonstrated per figure. As federal and state dispute resolution processes increasingly reference these benchmarks by name, the ability to answer a challenge in minutes with a complete account — rather than in weeks with a reconstruction — is the difference between being the reference and being the defendant.
