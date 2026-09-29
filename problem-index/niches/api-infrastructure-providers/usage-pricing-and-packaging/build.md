# Metering Is Solved and the Commercial Question Is Guessed

**Niche:** [[niches/api-infrastructure-providers/usage-pricing-and-packaging/profile|Usage Pricing & Packaging]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Metering and usage billing are available from several vendors, and choosing what to charge for, at what tier, with what overage behaviour, is a commercial decision every API business makes by guessing.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor here is fighting to tell an API business what to charge for, at what tier, with what overage behaviour — and whoever answers that takes the commercial side of the category, because metering is solved and the pricing decision is guessed at by everybody.

## The Problem
A company prices its API per call, with tiers at ten thousand, a hundred thousand and a million calls a month, and hard cut-off at the limit. The unit was chosen because a competitor uses it, even though cost to serve is driven by response size rather than call count, so the heaviest consumers are the least profitable and nobody has noticed. A large cluster of consumers sits just under the middle tier boundary and will never cross it. The hard cut-off has produced three churn events after surprise service interruptions. Every one of these facts is computable from data the company already has, and none of them has been computed.

## Why Nobody Has Built This
Pricing is owned by commercial functions and the data sits with engineering, and the two rarely meet over a query. Changing pricing on existing consumers is genuinely disruptive, which makes revisiting it feel expensive and produces a bias toward leaving it alone — the decision is taken once and defended thereafter. Cost to serve per consumer requires attributing infrastructure cost to usage, which nobody has plumbed. And there is no practice of evaluating a pricing decision after the fact, so no learning accumulates.

## What to Build
Pricing analysis from the data the provider already holds. Plot the usage distribution against the current boundaries, which immediately reveals bunching below a tier and consumers paying for capacity they cannot use. Compute cost to serve per consumer by attributing infrastructure cost to their usage pattern, which establishes margin by customer and frequently inverts the assumed ranking of good customers. Test candidate metering units against cost: which unit — calls, payload volume, compute, records, outcomes — best tracks what serving actually costs, since a unit uncorrelated with cost guarantees a margin problem somewhere in the book. Model tier placement against the observed distribution, choosing boundaries that sit where consumers naturally cluster rather than at round numbers. Estimate the churn consequence of overage behaviour from the provider's own history, since hard cut-offs, soft overage and throttling produce measurably different retention and nobody compares them. Simulate a proposed change against the existing book before committing, which is arithmetic and is almost never done. And evaluate afterwards, so the next decision is informed rather than guessed.

## Target Customer
API businesses and the product and commercial leaders who own their pricing, and the metering and billing vendors for whom this is the obvious layer above solved plumbing.

## Impact If Built
Metering is commodity and the decision it exists to serve is unsupported, which is where the commercial value in this niche now sits. The usage-against-boundaries plot and cost-to-serve attribution are both straightforward and typically produce immediate, surprising findings.
