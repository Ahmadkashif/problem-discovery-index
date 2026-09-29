# Build: The Match Rate, Published

**Niche:** Match Rate Measurement
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compute and publish, per feed, what proportion of its indicators ever matched real telemetry — across an installed base, segmented by organisation shape, with the distribution not just the mean.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #survival-analysis #k-means-clustering #data-integration #automation #compliance
**Contested on:** Whether anyone will publish how often a feed's indicators actually fire against real telemetry.

## The Problem

A feed contains several million indicators. Some fraction of them corresponds to infrastructure that will ever touch any customer's network. The rest are observations from collection — malware configurations, forum posts, sinkholed domains, addresses seen in someone else's incident — that are true, well sourced, and will never match anything in an enterprise environment.

Nobody knows what that fraction is. The vendor has not published it. The customer has not computed it. And the feed is priced and compared on the total.

The computation is a join. Take the feed, take the telemetry, count matches. A vendor with endpoint visibility can do it across tens of thousands of organisations in a batch job. A customer can do it against their own logs in an afternoon with a script.

What makes it interesting is not the headline number but the distribution. Indicators that matched at many organisations are describing widely-encountered infrastructure. Indicators that matched at exactly one are the interesting ones, potentially describing a targeted campaign. Indicators that matched nowhere are the bulk. Those three populations have completely different value and are shipped, priced and reported as one.

## Why Nobody Has Built This

**Only some vendors can compute it.** Pure-play intelligence vendors have no telemetry. The ones bundled with endpoint or network products do, and publishing it would advantage them against competitors who cannot answer — which is an argument for building it rather than against, and has still not happened.

**The number embarrasses the seller.** A large feed with a low match rate is a normal feed and a bad headline, and the first vendor to say so absorbs the comparison alone.

**Match is not the same as value.** A vendor could reasonably argue that an indicator which never matched still had value as context, or that its absence from telemetry means the defence worked upstream. These arguments are partly fair and are also exactly what an unfalsifiable product sounds like.

**Customer telemetry raises privacy questions.** Computing matches across an installed base means processing customer telemetry for a vendor's product analytics, which requires clear contractual basis.

**Segmentation is where the effort is.** A single number is misleading and easy; useful segmentation by sector, size, geography and stack is more work and is what a buyer actually needs.

**Nobody is asking.** Procurement has never required it, so no vendor has had to produce it.

## What to Build

**Compute the match rate and the distribution.** Per feed and per indicator: matched never, matched at one organisation, matched at many. Report the distribution rather than a mean, because the three populations mean different things and the mean conceals them.

**Segment by organisation shape.** Sector, size, geography, technology stack. A feed's match rate for organisations like the buyer is the number that matters, and it is the one that would let a mid-sized manufacturer see that a feed optimised for financial services will not fire for them.

**Distinguish what was matched.** An indicator matching high-volume ordinary traffic is different from one matching a single rare connection. Reporting the volume and rarity of what matched adds most of the interpretive value at little cost.

**Track match latency.** How long after an indicator is published before it first matches, and whether it matched before or after the vendor published it — which is a direct measure of whether the feed is ahead of the threat or describing it afterwards.

**Report indicator lifetime.** How long an indicator continues matching, and when it stops. This feeds directly into decay modelling and into knowing when to retire content.

**Publish methodology openly and invite replication.** The measure's value is in being trusted and compared. A published methodology that a competitor or a customer can replicate is what makes it a metric rather than a marketing claim.

**Give customers their own version.** A per-customer match rate report, so each buyer sees how the feed performed in their environment. This is straightforward, immediately useful, and would make the vendor's own honesty a selling point rather than a risk.

## Target Customer

Vendors bundled with endpoint or network telemetry — the intelligence arms of the large security platforms — for whom this is a structural advantage no pure-play competitor can match.

Security operations buyers, who should be receiving a per-environment match rate as a standard part of any subscription and currently receive none.

Procurement teams, for whom a required match rate disclosure would make comparison possible for the first time.

## Impact If Built

The category's first real product measurement, computable today, from data that already exists, requiring no adjudication or ground truth.

The distribution would separate three populations currently sold as one — widely-matched infrastructure, singleton matches that may indicate targeting, and inert content — which is the most useful analytical cut available.

And a per-customer match rate would turn a renewal conversation based on feeling into one based on whether the feed fired in that environment, which is the question the buyer is actually trying to answer.
