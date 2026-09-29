# Documentation That Describes Intent

**Niche:** [[niches/headless-commerce-vendors/the-solutions-architect/profile|The Solutions Architect]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Vendor documentation describes what a service is supposed to do, and the architect needs to know what it does under load, at scale, when a dependency is slow and at the ninety-ninth percentile — none of which is published anywhere.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #compliance #worker-facing #hypothesis-testing #quick-win #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to let an architect find out whether a composition works before the programme commits to it — and whoever does that takes the delivery quality, because the failure modes currently appear in production eighteen months later.

## The Problem
The documentation says the service returns product data with a typical response time in the tens of milliseconds. It does not say what the ninety-ninth percentile is at the architect's expected request rate, how it behaves when its own upstream is slow, what the rate limit is per tenant and what happens at it, how large a catalogue it has been run with, what the consistency window is after a write, or what happens to in-flight requests during their deployments. Every one of those determines whether the composition works, none is published, and the architect finds out in production or by asking a peer who already did.

## Why It's Still Broken
Publishing operating characteristics invites comparison on the dimensions where a vendor is weakest, so nobody publishes first. Documentation is written by developer relations to help somebody get started rather than by engineering to describe behaviour. Procurement asks about features and contractual availability rather than about distributions. And the architect has no standing to demand it during a sales process.

## What a Fix Looks Like
Ask for the characteristics and publish them. Require operating characteristics in the vendor selection — latency distribution at stated request rates, behaviour at the rate limit, consistency window after write, degradation behaviour, deployment impact, tested scale — which is a procurement question a retailer can ask today and which most vendors can answer, and asking it is the fix. Measure them independently during evaluation, since a measured number is worth more than a stated one and the sandbox makes it possible. Publish observed characteristics as an industry resource where a neutral party can, since the collective architects would all benefit and no vendor will go first. Record what was assumed about each service in the architecture decision, so a later failure can be traced to an assumption rather than to a mystery. Contract for the characteristics that matter, since an availability percentage without a latency commitment leaves the property the architecture actually depends on unbound. Test the assumptions in production continuously, which is the fitness function approach and is what catches a vendor's characteristics changing. Share findings between implementations within an integrator, which is the cheapest available improvement and is currently informal. And ask vendors for their degradation behaviour specifically, because that is the least documented and most consequential property in a composed system.

## Who Feels the Pain
Architects designing against documentation of intent; retailers whose compositions fail on properties nobody asked about; and the vendors whose genuinely good operating characteristics go unrewarded.

## Impact If Fixed
Every property the composition depends on is unpublished and most vendors can state them, which makes asking the fix. Contracting for latency distribution rather than only availability binds the property the architecture actually rests on.
