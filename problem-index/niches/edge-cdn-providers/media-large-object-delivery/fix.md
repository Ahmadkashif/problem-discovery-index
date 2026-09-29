# Quality Measured by One Vendor, Delivery Configured by Another

**Niche:** [[niches/edge-cdn-providers/media-large-object-delivery/profile|Media & Large Object Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Playback quality is measured by a specialist vendor and delivery is configured with a provider, and nothing connects a buffering event to the delivery decision that caused it.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #change-point-detection #quick-win #data-integration #automation
**Contested on:** Every serious competitor here is fighting to deliver a byte more cheaply while holding playback quality — and whoever does that takes the media account, because egress is a dominant cost line and quality of experience is the product.

## The Problem
The quality of experience dashboard shows a rise in rebuffering in one region on Tuesday evening. The delivery provider's dashboard shows normal cache hit rates and availability. The two datasets have no shared identifier, no aligned time granularity and no common dimension beyond geography, so establishing whether the rebuffering was caused by a delivery problem, an origin problem, a network problem or a player release takes a week of correspondence between three parties. It happens regularly, and it is usually resolved by the problem going away.

## Why It's Still Broken
Quality of experience monitoring grew as a specialist category serving the media buyer, and delivery telemetry belongs to the provider, and no commercial relationship connects them. Session identifiers exist on both sides and are not shared. Time granularity differs — one aggregates by minute, the other by five — and dimension definitions differ enough that even matched geography is not quite matched. And each vendor's incentive is to show that their part was healthy.

## What a Fix Looks Like
Make the two datasets joinable. Propagate a session or request identifier from the player through to the delivery logs, which is a header the player can set and the provider can log, and is the single change that makes every subsequent analysis possible. Align time granularity and dimension definitions, which is unglamorous schema work and removes a large share of the ambiguity. Attribute each rebuffering event to a stage — origin fetch, edge delivery, last mile, player decision — using the timings both sides already record, which is the question every one of these investigations is trying to answer. Report the joined view to the customer rather than two separate dashboards, since they are the party who cares about the whole path. Correlate against configuration and player release events, so a degradation that followed a change is attributable immediately. And publish the joined metric as the one both vendors are judged on, because two separately healthy dashboards and an unhappy viewer is the situation the current arrangement produces.

## Who Feels the Pain
Media operations teams investigating across three vendors; viewers experiencing rebuffering nobody can attribute; and organisations whose quality and delivery vendors each report success.

## Impact If Fixed
A propagated session identifier is a one-line change that makes the join possible, and stage attribution answers the question every one of these investigations exists to ask. Reporting the joined metric is what stops two healthy dashboards coexisting with a bad experience.
