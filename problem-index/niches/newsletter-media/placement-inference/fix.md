# Thirty Seed Mailboxes and a Hundred Thousand Subscribers

**Niche:** [[niches/newsletter-media/placement-inference/profile|Placement Inference]]
**Industry:** [[industries/newsletter-media|Newsletter Media]]
**Type:** Fix (Pain Point)
**One-liner:** The deliverability report is based on accounts that exist only to receive test mail, and it is read as though it described the real list.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to estimate where a send actually landed, per provider and per segment, from behaviour rather than from a seed test — and whoever does it replaces a few dozen synthetic mailboxes with the publisher's own hundred thousand.

## The Problem
The seed test reports that the send reached the inbox at one provider and the promotions tab at another. Those accounts receive nothing but test mail, have never clicked anything, have no sending history with the publisher, and do not resemble any real subscriber in any way a provider's filter would care about. The result is presented as a percentage, with no interval, and is used to make decisions about content, sending schedule and list management.

## Why It's Still Broken
The seed test is the only thing available, so its limitations are tolerated rather than addressed — a flawed measurement with no alternative becomes the measurement. Its output looks precise, which is worse than an honest range. Vendors have no incentive to state the sample's weakness. And publishers lack the statistical background to interrogate it.

## What a Fix Looks Like
Use it correctly and supplement it. State the sample size and the uncertainty on every seed result, which is the fix and immediately changes how the number is read. Check the seed result against the publisher's own engagement pattern for the same providers, since a disagreement is informative and nobody makes the comparison. Track the seed result over time rather than treating each as a verdict, because the trend survives the sample's weakness better than the level does. Report by provider rather than as a blended figure, as the blended number conceals the only actionable detail. Note that seed accounts have no engagement history, which is the single most important caveat and is never stated. Use real subscriber segments as an additional signal wherever the platform allows. Correlate placement changes with sending changes, since attribution is the point and a bare percentage provides none. Keep a log of what was changed and what the result was, as deliverability work is currently a sequence of unrecorded experiments. Ask the vendor for the methodology, because most publishers have never asked and the answers would change their reading. And stop making content decisions from a thirty-mailbox sample, which is the concrete harm.

## Who Feels the Pain
Publishers making decisions from an unrepresentative sample; growth teams chasing phantom problems; advertisers told about placement nobody measured; and vendors whose product is better than the way it is read.

## Impact If Fixed
A flawed measurement with no alternative becomes the measurement, and this one looks precise. Stating the sample size, reporting by provider and checking against the publisher's own engagement is free and changes what the number can be used for.
