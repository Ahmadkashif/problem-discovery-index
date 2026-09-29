# The Bitrate Ladder Nobody Prices

**Niche:** [[niches/edge-cdn-providers/media-large-object-delivery/profile|Media & Large Object Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An encoding team chooses the bitrate ladder on quality grounds and a delivery team pays the egress bill it produces, and no analysis connects the two.
**Tags:** #optimization-fundamentals #convex-optimization #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to deliver a byte more cheaply while holding playback quality — and whoever does that takes the media account, because egress is a dominant cost line and quality of experience is the product.

## The Problem
The encoding team defines a bitrate ladder with eight rungs, chosen for coverage and quality. In practice the top rung is delivered to a small fraction of sessions and accounts for a disproportionate share of egress; two middle rungs are close enough that the player rarely distinguishes them; and one rung is never selected at all by any common device. The delivery cost of this ladder is substantial and is paid by a different team, who have no visibility into the ladder and no mechanism to influence it. The data that would settle it — which rungs are actually delivered, to which devices, on which networks, with what playback outcome — exists in the delivery logs and the player telemetry and is never joined.

## Why Nobody Has Built This
Encoding and delivery are separate functions with separate tooling and separate budgets, and the ladder is designed before delivery data exists for that content. Quality of experience telemetry comes from the player and delivery data from the network, and joining them requires an integration that neither vendor has built. The ladder is also treated as a quality decision, where introducing cost feels like compromising the product — which is a real tension and is better resolved with numbers than by keeping the two teams apart.

## What to Build
Join playback outcomes to delivery cost and optimise the ladder against both. Measure which rungs are actually delivered, to which device classes, on which networks, and what the playback outcome was — the join between player telemetry and delivery logs, which is the enabling step. Price each rung's contribution to egress, per title and per region, which converts a quality decision into a quality-and-cost decision. Identify rungs that are never selected or are indistinguishable in outcome from their neighbours, which is usually one or two and is free to remove. Model the ladder as an optimisation over quality of experience and cost jointly, with the trade-off stated, rather than choosing on one axis. Adapt per title and per audience, since a title watched mostly on mobile in one region needs a different ladder from one watched on large screens, and a single ladder for a whole library is a compromise nobody chose. Feed delivery cost back to the encoding team continuously, which is the organisational change the analysis enables. And report cost per hour watched by title, which is the unit media operations should be managing and frequently cannot compute.

## Target Customer
Streaming and media operations teams, delivery providers competing for media volume, and the encoding and packaging vendors whose decisions determine the bill.

## Impact If Built
The ladder determines the egress bill and is designed without reference to it, by a team that does not pay it. Joining player telemetry to delivery logs is the enabling step and regularly identifies rungs that cost substantially and serve nobody.
