# Fix: Nobody Measures What Over-Removal Costs

**Niche:** Error Cost Elicitation
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Half the trade-off has a measured magnitude and the other half has an appeals queue, so the threshold is set on one side of a balance.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #descriptive-statistics #hypothesis-testing
**Contested on:** Whether a platform will state what it costs to miss a piece of harmful content against what it costs to remove a legitimate one.

## The Problem

Missed harm is measurable and measured, imperfectly. Reports arrive, incidents occur, journalists investigate, regulators ask. A platform has some sense of what it is failing to catch.

Over-removal produces an appeal. The user submits it into a process, waits, and either has their content restored or does not. The event is recorded as an appeal handled. What it cost — a creator losing income, an activist losing reach during a campaign, a small business losing a listing, a community losing a space — is not captured anywhere.

So one side of the trade has magnitude and the other has a ticket count.

The consequence is predictable. A trade-off where one cost is visible and the other is not will be resolved toward the visible one, consistently, by people acting reasonably. Every incident of missed harm produces pressure to lower the threshold. No equivalent pressure exists from the other direction, because the harm is dispersed across individuals who appeal alone into a process.

And the distribution matters. Over-removal is documented to fall unevenly — reclaimed language, minority-language content, discussion of harm rather than harm itself, and marginalised communities' speech are affected disproportionately — which means the unmeasured cost is concentrated on populations with the least ability to make it visible.

## Why It's Still Broken

**The appeal is the only channel and it measures process, not harm.** An appeal handled is a workflow event, and the underlying cost to the person is not asked about.

**The harmed party is dispersed.** One removal affects one user, who has no way to aggregate with others, where a missed-harm incident frequently produces coordinated attention.

**Measuring it invites the finding.** A platform that quantified over-removal harm would have a number it must then weigh against safety, which is an uncomfortable position.

**Restoration is treated as resolution.** Content restored after four days is treated as an error corrected, and the four days are not counted.

**Disaggregation is politically charged.** Measuring which communities bear the over-removal cost produces findings that are uncomfortable and are exactly the ones most worth having.

**No regulator asks about it.** Regulatory attention has focused substantially on harmful content remaining up, which is legitimate and one-sided.

## What a Fix Looks Like

**Measure the false positive rate directly.** Sample actioned content and review it properly with full context. The proportion wrongly removed is measurable and almost nobody measures it.

**Ask the affected user what it cost.** A short question on appeal about the consequence — reach lost, income lost, time lost. Voluntary, simple, and it gives the harm a magnitude for the first time.

**Count restoration time as harm.** Content restored after four days was unavailable for four days, and treating restoration as a clean correction ignores the interval.

**Disaggregate by community and language.** Over-removal rates by language, by content type and by community. The evidence consistently suggests the distribution is uneven, and reporting it is what would make the harm visible to the people who set thresholds.

**Report both error rates together, always.** Missed harm and wrongful removal in the same report, so the trade is visible whenever the threshold is discussed.

**Give the over-removal side a channel with weight.** Aggregate appeal outcomes into a reported metric that reaches the same people as the missed-harm incidents, so the pressure is symmetric.

**Publish it.** A platform reporting its own over-removal rate alongside its harm metrics would be the first, and would establish a standard the rest would have to answer.

## Who Feels the Pain

The wrongly removed user — the creator, the activist, the small business, the community — whose loss is recorded as a ticket and whose experience of appeal is that it was handled.

Communities whose speech is disproportionately affected, who have the least ability to make the pattern visible and are the ones the aggregate most obscures.

The policy team, setting a threshold with one side of the balance measured and the other represented by an appeals queue.

And the platform, which believes its moderation reflects a considered balance and has been resolving toward the visible cost for years.

## Impact If Fixed

Measuring the false positive rate by sampled review with full context is straightforward and would give half the trade-off a magnitude for the first time.

Asking the appealing user what the removal cost them is one question and converts an unmeasured harm into something with a size.

And disaggregating by community and language would reveal the uneven distribution that the aggregate conceals — which is where the documented harm in content moderation concentrates and where the measurement is most conspicuously absent.
