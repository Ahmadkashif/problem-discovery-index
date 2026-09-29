# Build: Exposure Management for Labelling

**Niche:** The Annotation Workforce
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Bring exposure measurement, presentation controls and rotation into the labelling interface, where exposure is more concentrated than in moderation and the protections have not arrived at all.
**Tags:** #cnns #evaluation-metrics #confidence-intervals #markov-decision-processes #compliance #worker-facing #automation #survival-analysis
**Contested on:** Whether the people who look at harmful material so a classifier can learn from it are visible to anyone.

## The Problem

An annotation task for a harm category is, by construction, a concentrated stream of that harm. A moderation queue contains a mix of mostly ordinary content; a training set for violent content is violent content, item after item, for a shift.

So the exposure profile is worse than moderation's in the dimension that matters most, and the protections that have developed for moderation — wellness provision, break structures, clinical support, and the public and legal attention that produced them — have not reached this layer.

The annotation platform is built for labelling quality. It measures agreement between annotators, tracks throughput, manages task assignment and enforces quality controls. It does not measure what the annotator has been exposed to, does not offer fidelity controls, does not rotate people off severe categories, and does not track cumulative exposure across a project.

Meanwhile the technical interventions that would help are the same ones available in moderation and are easier here, because the labelling task frequently does not require full fidelity. A category judgement can often be made from a reduced-fidelity rendering, a short segment or a still frame, and the interface presents the full item because that is the default.

## Why Nobody Has Built This

**The workforce is two relationships away.** The platform contracts the vendor, the vendor contracts a labelling supplier, and the supplier employs the people. Nobody in the chain owns the conditions.

**Annotation platforms optimise label quality.** Their metrics are agreement and throughput, and the labeller's exposure is not a variable in the product.

**Full fidelity is assumed necessary for accurate labels.** Reduced fidelity might reduce label accuracy, which is a real concern and is untested — the trade has never been measured.

**Labelling projects are concentrated pushes.** A training set is produced in a burst, which makes rotation harder than in a continuous moderation operation.

**The workforce has no visibility.** They are not named in any vendor's product description, are not covered by the reporting that applies to moderation, and have no channel to anyone.

**Measurement would create an obligation.** The same dynamic as in moderation: measuring exposure produces a record, and the record creates responsibility.

## What to Build

**Measure exposure in the labelling interface.** Items viewed, by severity category, at what fidelity, over what period. This is the ledger that every other intervention depends on and the platform is the natural place for it.

**Apply presentation controls by default.** Greyscale, audio suppression, reduced resolution, frame sampling and segment isolation as the default rendering, with escalation to full fidelity when the label genuinely requires it.

**Test the fidelity-accuracy trade.** Measure label accuracy at reduced fidelity against full fidelity. If a category judgement survives greyscale and frame sampling, which it frequently will, that is a free reduction in harm and nobody has checked.

**Rotate and cap.** Cumulative severe-category exposure capped per shift and per project, with automatic routing to lower-intensity tasks. Harder in a concentrated project than in continuous moderation and not impossible.

**Design the task to minimise exposure.** Ordering items so severe ones are spread rather than clustered, and using model pre-labelling so annotators confirm rather than view everything, reduce exposure substantially for the same labelled output.

**Make conditions a procurement requirement.** The platform buying the classifier can require exposure management of the vendor, who requires it of the supplier. This is the only mechanism that reaches through the chain.

**Report it.** A vendor stating how its training data is produced and under what conditions is making a claim no competitor makes and is disclosing something buyers are increasingly asked about.

## Target Customer

Annotation platform vendors, for whom exposure management is a genuine differentiator in a category competing on quality tooling and throughput.

Trust and safety vendors, who are increasingly asked by platform buyers about their supply chain and currently have little to say about it.

Platform procurement, which is the only party with leverage that reaches through the chain and is the mechanism by which anything here would change.

## Impact If Built

The protections that have partially reached content moderation extend to a workforce with a more concentrated exposure profile and no visibility at all.

Testing the fidelity-accuracy trade is cheap and would very likely show that many category judgements survive substantial fidelity reduction, which is a free reduction in harm nobody has checked for.

And model pre-labelling with human confirmation reduces exposure for the same labelled output, which is a task design change that improves both the harm profile and the throughput.
