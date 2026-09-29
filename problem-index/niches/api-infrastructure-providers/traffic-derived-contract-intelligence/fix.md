# The Documented Field Nobody Sends

**Niche:** [[niches/api-infrastructure-providers/traffic-derived-contract-intelligence/profile|Traffic-Derived Contract Intelligence]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** An API's documentation describes forty request fields, consumers use eleven, and the other twenty-nine are maintained, tested, explained in support tickets and read by every new integrator.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #k-means-clustering #quick-win #automation #data-integration
**Contested on:** Every serious competitor that gets here is fighting to turn observed traffic into the API's real contract — what is actually used, actually returned and actually relied upon — and whoever does that holds the accurate specification while everyone else holds the intended one.

## The Problem
The create-order endpoint documents forty request fields. Analysis of a week's traffic shows eleven are ever sent, four more appear from a single consumer, and twenty-five have never been used by anybody. Those twenty-five are nonetheless implemented, validated, tested, documented, described to every new integrator who must decide whether they need them, and maintained through every refactor. Nobody has looked, so they will still be there in five years, and the documentation will still be forty fields long for a developer trying to work out which eleven matter.

## Why It's Still Broken
Field-level usage is not something gateway analytics compute, because the operational questions are endpoint-level and payload inspection was ruled out early. Removing a documented field is a breaking change in principle, which triggers the same paralysis the deprecation niche describes. And nobody has framed documentation length as a cost, although it is one of the largest contributors to how long a new consumer takes to reach a first successful call.

## What a Fix Looks Like
Count the fields and act on the count. Report per-field usage from sampled traffic — sent by how many consumers, how often, over what period — which is the enabling measurement and is a sampling change rather than a new system. Mark never-used fields for removal and single-consumer fields for a conversation, which is a far smaller and more tractable decision than a general deprecation. Reorder the documentation by actual usage, so the eleven fields everyone sends appear first and the rare ones are behind a disclosure — which requires no removal at all and is the single largest improvement available to onboarding time. Do the same for response fields, where the question is which are read rather than which are sent, and which the breaking-change niche needs anyway. Report undocumented parameters that consumers send successfully, since those are either features to document or accidents to close. And repeat it per release, because unused fields accumulate faster than anyone expects.

## Who Feels the Pain
New integrators reading forty fields to find eleven; engineering teams maintaining and testing parameters nobody has ever sent; and support teams explaining fields whose purpose nobody in the company remembers.

## Impact If Fixed
Field-level usage counting is a sampling change and immediately reveals how much of the surface is dead. Reordering documentation by usage requires removing nothing, avoids the deprecation paralysis entirely, and directly improves the metric the external programme niche cares most about.
