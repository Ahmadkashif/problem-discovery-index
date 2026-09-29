# The Expert Review That Is the Real Acceptance Test

**Niche:** [[niches/synthetic-data-providers/regulated-domain-generation/profile|Regulated Domain Generation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Every regulated-domain deal is decided by a clinician or an underwriter reading a handful of records, and no vendor runs that test before the customer does.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #tacit-knowledge-ml #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to produce records a domain expert cannot tell are impossible — and whoever does that takes the account, because in a regulated domain a single implausible record ends the evaluation.

## The Problem
The acceptance test in these domains is not the vendor's report. It is a domain expert, in a room, reading fifteen records and forming a judgement in a few minutes. Everyone involved knows this. The vendor prepares a fidelity deck and the customer's clinician reads record four, finds something that could not happen, and stops. The test that decides the outcome is never run by the party who could act on the result, and the vendor learns about the failure as a lost deal rather than as a defect report.

## Why It's Still Broken
Expert review costs expert time, which vendors price as a services burden rather than as quality assurance. It produces findings that are uncomfortable and specific, where a distribution comparison produces a number that is comfortable and vague. There is no established protocol for it, so each review is improvised and the results are not comparable across runs. And nobody has framed the implausibility rate as a metric, which means it is not tracked, not targeted, and not improved between releases.

## What a Fix Looks Like
Run the test internally, on a protocol, before the customer does. Establish a structured review: a stratified sample, a rubric covering the known impossibility classes, independent reviewers, and a recorded verdict per record with the reason — which makes the result a comparable number rather than an anecdote. Report the implausibility rate with a confidence interval as a headline metric alongside fidelity, since it is the number the buyer's decision actually turns on. Feed every finding back into the constraint set, which is how the review compounds into product rather than repeating as a cost. Sample deliberately from the boundary regions where generative interpolation is most likely to produce impossible combinations, rather than uniformly, because uniform sampling of a mostly-plausible dataset wastes expert time on the easy cases. Build an automated pre-screen from the accumulated findings so experts see only what the screen could not settle, which is what makes the review affordable at frequency. Publish the protocol and let the customer run it themselves. And run it as a release gate, so a version with a rising implausibility rate does not ship.

## Who Feels the Pain
Clinicians and underwriters spending their time finding defects that a protocol would have caught; vendor solutions engineers losing deals at record four; and the customers who conclude that synthetic data does not work in their domain, having tested one vendor's unscreened output.

## Impact If Fixed
The review decides the deal and the vendor never runs it. Turning it into a protocol with a reported rate makes it a tracked metric, and feeding findings back into the constraint set is what converts a recurring services cost into a compounding product asset.
