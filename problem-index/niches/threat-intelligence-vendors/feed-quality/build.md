# Build: The Feed Scorecard

**Niche:** Feed Quality Measurement
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A published scorecard per feed — match rate, precision, uniqueness, timeliness and decay — computed across a large installed base and segmented by the kind of organisation buying it.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #logistic-regression #bayesian-inference #survival-analysis #data-integration #compliance
**Contested on:** Whether a feed's value can be stated as a number, or remains a matter of collection breadth and analyst reputation.

## The Problem

A security leader choosing between threat intelligence vendors compares collection narratives. One has underground forum access. Another has incident response telemetry from a large practice. A third has malware analysis at scale. Each publishes indicator volumes and source counts.

None of it answers the question. Which of these feeds will actually match something in my environment, and when it does, will it be real?

The customer cannot answer it either, though they could. They hold the telemetry. Measuring how often each feed's indicators matched, and how those matches were adjudicated, is a query against data they already collect. Almost nobody does it, so renewal decisions are made on whether the reporting felt useful.

The vendors with endpoint telemetry are in a far better position. They see matches across tens of thousands of organisations. They could state, with real statistical weight, how often their indicators fire and against what. And they do not, because publishing a match rate invites comparison and the honest number for a large feed is uncomfortable — much of any large indicator feed has never matched anything anywhere.

## Why Nobody Has Built This

**The honest number is bad for the seller.** A feed of five million indicators where a small fraction has ever matched is a normal feed and a poor advertisement. The first vendor to publish takes the reputational cost alone.

**Volume is the only comparable attribute today.** Procurement compares indicator counts and source lists because nothing else is comparable, which means volume is what gets optimised and quality is not.

**Precision needs ground truth that is scarce.** Match rate is computable from telemetry. Whether a match was genuinely malicious requires adjudicated outcomes, which is the harder half described in [[niches/threat-intelligence-vendors/precision-verification/profile|🎯 Precision Verification]].

**Customer segmentation matters and complicates the message.** A feed excellent for financial services may be irrelevant to manufacturing. A single headline number would be misleading, and segmented numbers are harder to sell.

**Telemetry access is uneven.** Only vendors bundled with endpoint or network products see matches at scale. Pure-play intelligence vendors do not, which means the measurement can only be produced by a subset of the market — and that subset competes with the rest.

**Nobody is asking loudly enough.** Buyers accept collection narratives. Until procurement asks for a match rate, no vendor has to supply one.

## What to Build

**Start with match rate, which needs only telemetry.** For each indicator: did it ever match, at how many organisations, over what period, against what volume. Aggregate to a feed-level match rate and a distribution. This is computable now by anyone with telemetry at scale and is the single most informative number in the category.

**Segment by organisation shape.** Sector, size, geography, technology stack. A feed's value is highly dependent on whether the adversaries it tracks target organisations like the buyer, and an unsegmented number hides exactly that.

**Measure uniqueness across feeds.** Which indicators appear in this feed and not in others, and how those unique indicators perform. A customer buying four feeds is frequently paying four times for substantially overlapping content, and the academic work that has looked at this found low overlap and high disagreement — which cuts both ways and is worth knowing.

**Measure timeliness.** How long before or after first observation elsewhere an indicator appears in this feed. Being early is the core claim of the category and is directly measurable against a reference.

**Model decay.** How an indicator's match quality changes with age, so a feed can be assessed on whether it retires indicators appropriately rather than accumulating them.

**Add precision where ground truth exists.** Where adjudicated outcomes are available, report precision with honest uncertainty and state the sample. Partial precision data with stated limits is far better than none.

**Publish and invite challenge.** The measure's value is in being believed. Open methodology, external validation and a willingness to publish unflattering numbers about one's own feed is what would establish it, and is also what makes it a durable position — a vendor that publishes first defines the metric everyone else must report against.

## Target Customer

Vendors bundled with endpoint or network telemetry — the intelligence arms of the large security platforms — who can compute this across an installed base no pure-play competitor can match. For them the measurement is a structural advantage.

Security operations buyers as the demand side, who should be computing their own match rates from their own telemetry regardless of what vendors publish.

Procurement and independent evaluators as the eventual forcing function, since a published methodology makes comparison possible and comparison is what changes what gets optimised.

## Impact If Built

The category acquires a quality measure. Every assurance business in this cluster competes on reputation because quality is unobservable, and here two observable proxies have been sitting unused.

A published match rate would immediately reveal how much of a large feed is inert, which is the finding that would reprice the market away from volume.

And segmentation by organisation shape would let a buyer choose a feed on whether it tracks adversaries who target them, which is the actual purchasing question and is currently answered by a sales narrative.
