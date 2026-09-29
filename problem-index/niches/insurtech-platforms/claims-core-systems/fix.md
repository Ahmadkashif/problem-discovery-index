# Reserve Development Nobody Shows the Adjuster

**Niche:** [[niches/insurtech-platforms/claims-core-systems/profile|Claims Core Systems]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every adjuster sets hundreds of reserves a year and every one of them eventually resolves into a known paid amount, and almost no adjuster is ever shown how their reserves compared to what the claims actually cost.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #survival-analysis #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in claims systems is fighting to reserve a claim correctly and route it to the right adjuster at first notice — and whoever improves reserve accuracy and cycle time most takes the account.

## The Problem
An adjuster has been setting reserves for six years. They have never seen a systematic comparison of their reserves against final paid amounts — whether they are consistently low on a particular claim type, whether they revise too late, whether their estimates are noisier than their colleagues'. Reserve development is analysed by actuaries at portfolio level and discussed in terms adjusters never see. The person making the estimate receives no feedback on the estimate, in a job that consists substantially of making estimates, which is close to the definition of a skill that cannot improve.

## Why It's Still Broken
Development analysis lives with actuaries whose questions are portfolio questions, and nobody has built the adjuster-level view because it has not been anyone's job. There is also a real sensitivity: reserve adequacy is a performance-loaded topic and an individualised report reads as an evaluation, particularly in an organisation where reserve strengthening is a fraught subject. That is a reason to design the feedback carefully — as a learning instrument shown to the adjuster first, with appropriate handling of small samples — rather than to withhold it.

## What a Fix Looks Like
Compute the comparison and show it to the person who made the estimate. For every closed claim, the initial reserve, the revision history and the final paid amount, aggregated per adjuster by claim type, with bias and dispersion separated — a consistently low adjuster needs a different correction from an erratic one. Show revision timing too, since late recognition is a distinct and common failure that costs the carrier more than initial inaccuracy. Handle sample size honestly, because an adjuster with fourteen closed claims of a type does not have a measurable pattern and treating noise as performance is both wrong and corrosive. Deliver it to the adjuster as their own information first and to management as an aggregate, which is what makes it a development tool rather than a surveillance one. Pair it with the specific claims that drove the pattern, since the learning happens on cases rather than on statistics.

## Who Feels the Pain
Adjusters making estimates for years with no feedback loop; claims leadership managing reserve adequacy through general exhortation; and actuaries building portfolio estimates on case reserves of unmeasured quality.

## Impact If Fixed
Estimation is a learnable skill and feedback is the mechanism, and this profession has been estimating without it. The computation is a join between closed claims and their reserve histories — data every claims system holds — and the separation of bias from dispersion is what makes the resulting conversation useful rather than accusatory.
