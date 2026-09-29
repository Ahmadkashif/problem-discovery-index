# Downloads as the Headline Metric

**Niche:** [[niches/open-source-commercial-vendors/adoption-visibility/profile|Adoption Visibility]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Every open-source company reports downloads to its board, everyone involved knows the number is close to meaningless, and nothing else is reported because nothing else has been constructed.
**Tags:** #descriptive-statistics #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to tell an open-source vendor who is actually running their software and how — and whoever does that takes the commercial function, because every decision it makes is currently based on download counts.

## The Problem
The monthly report leads with downloads, stars and contributors. Everyone in the room knows downloads are dominated by automated pipelines, that stars measure attention at a moment years ago, and that contributor count is a proxy for project activity rather than for adoption. The numbers are reported anyway, because they are available and because no alternative has been assembled. Decisions are then made against them: a growth slowdown in downloads prompts a marketing response to a phenomenon that may be a change in a continuous integration cache policy.

## Why It's Still Broken
The metrics are supplied free by the registries and require no work, which is why they became the standard. Constructing anything better requires deduplication, classification and inference, which is a project nobody has owned. The numbers also flatter, which removes the pressure to replace them. And the board expects a growth number, so producing a smaller and more honest one is a conversation nobody wants to start without an alternative ready.

## What a Fix Looks Like
Construct a defensible set and report it alongside the old one for a period. Deduplicate downloads by source where the registry permits, separating automated infrastructure from plausible human or deployment activity, which is achievable from the request patterns and immediately produces a number an order of magnitude smaller and far more meaningful. Report distinct organisations rather than events wherever the signal supports it, since the commercial question is about organisations. Separate evaluation from sustained use by looking at repeat behaviour over time rather than at single events. Report version distribution, which is both operationally useful — who is on an unsupported version — and a genuine adoption signal. Track the public signals as a distinct series: dependent public repositories, job postings, conference mentions, which are noisy individually and informative as trends. Connect each candidate metric to commercial outcomes retrospectively, which establishes which ones actually predict anything and is the analysis that justifies replacing the old set. And state the limitations of every number in the report, because a category whose headline metric is known to be meaningless will not be fixed by a new number with the same problem.

## Who Feels the Pain
Commercial teams making decisions from a metric they know is noise; boards reading growth numbers that reflect cache behaviour; and product teams prioritising against issue volume because nothing better exists.

## Impact If Fixed
Deduplication and repeat-behaviour analysis over registry data produce a much smaller and far more meaningful number without any new instrumentation. Connecting candidate metrics to commercial outcomes is what establishes which ones deserve to be in the report at all.
