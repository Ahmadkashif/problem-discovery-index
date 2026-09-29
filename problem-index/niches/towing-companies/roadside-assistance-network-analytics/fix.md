# Provider Scorecards Built From Whatever the Provider Typed

**Niche:** [[niches/towing-companies/roadside-assistance-network-analytics/profile|Roadside Assistance Network Analytics]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Providers are ranked, paid and dropped on performance data most of them enter themselves, after the fact, with an obvious incentive.
**Tags:** #change-point-detection #evaluation-metrics #automation #data-integration #worker-facing

## The Problem
The network's central operational asset is its judgment about which providers are good. That judgment drives dispatch priority, rates, and whether an operator stays on the network at all — and for an independent tow company, network work is most of the revenue.

The data behind it is largely self-reported. Arrival and completion times are frequently entered by the provider or their dispatcher, sometimes hours later, from memory or from a paper log. Larger operators integrate through software and report automatically; the long tail of small operators does not. So the performance record is a mixture of measured and asserted times, and the mixture correlates with operator size rather than with operator quality.

The incentive is obvious and does not require dishonesty to distort things. A provider entering their own arrival time, after a shift, on a job they know was scored against a service level, will round in a predictable direction.

Two further gaps compound it. Customer feedback is collected on a small and self-selecting fraction of events, so it is noisy exactly where volume is thin — which is the rural and overnight coverage the network most needs to understand. And the network typically does not know what happened after the tow: whether the vehicle arrived undamaged, whether the customer disputed the charge, whether the repair shop found the diagnosis was wrong.

The result is that the most consequential decision the network makes about its supply base is made on data of unmeasured and uneven quality.

## Why It's Still Broken
The provider network is deliberately asset-light and enormously fragmented. Requiring telematics or a mobile application from every operator is a real barrier to network coverage, and coverage is the product — a network that cannot serve a rural county at two in the morning has a bigger problem than a noisy scorecard.

Self-reported timestamps also arrive already integrated with billing, which is the workflow that actually has to happen. Nobody built a second, independent measurement path because the first one was free.

And the measurement gap is uncomfortable rather than urgent. Scorecards work well enough to identify the worst providers; the cost of the noise falls mostly on mid-ranked operators who lose dispatch priority for reasons nobody can substantiate.

## What a Fix Looks Like
**Capture position passively where possible.** A lightweight mobile check-in, or an integration with the operator's own dispatch software, gives a measured timestamp without requiring hardware. Adoption will be partial; that is fine, because partial adoption is what makes the next step possible.

**Model the bias in self-reported times.** With a subset of providers measured directly, the distribution of self-reported error is estimable — by provider, by market, by time of day — and can be corrected rather than ignored. This is the single highest-value analysis available here and it needs no new data collection beyond the subset.

**Score data quality alongside performance.** A provider's scorecard should carry how much of it is measured and how much asserted. A network that cannot distinguish a well-evidenced good provider from an unverified one is guessing about its own supply base.

**Detect implausible reporting.** Arrival times that are impossible given the dispatch time and distance, or that cluster suspiciously just inside a threshold, are visible in the data and are not looked for.

**Close the loop past the tow.** Damage claims, customer disputes and repair shop outcomes exist and are usually held by a different function. Joining them to the provider record turns a timeliness scorecard into a quality one.

**Give providers their own numbers.** Operators generally cannot see how they are scored or why they lost priority. A transparent scorecard with the measurement basis shown is both fairer and a strong retention argument in a market where operators can choose which networks to accept work from.

## Who Feels the Pain
Independent tow operators whose livelihoods depend on a score computed from mixed-quality data they cannot see; the network's own dispatch algorithms, optimising against noisy quality signals; and customers, who are routed to providers ranked partly on how diligently they fill in a form.

## Impact If Fixed
Provider quality is the network's core asset and the basis of every dispatch decision it makes. Measuring it honestly — correcting self-report bias rather than pretending it is absent, and reporting the evidence behind each score — improves dispatch immediately, and it is the precondition for the arrival time modelling above, which cannot be trained on timestamps nobody has validated.
