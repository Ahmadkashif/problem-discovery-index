# The Same Advertisement Eleven Times

**Niche:** [[niches/streaming-video-platforms/ad-supported-tier-operations/profile|Ad-Supported Tier Operations]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The frequency cap is set to three and the viewer saw it eleven times in one evening.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #graph-theory #automation #confidence-intervals #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to forecast, fill and frequency-cap inventory across a supply chain that makes capping structurally difficult — and whoever solves the repetition viewers notice keeps the tier that is supposed to be the growth engine.

## The Problem
The cap is configured and the experience contradicts it. Nobody at the platform is looking at what an individual viewer actually saw over an evening, because the reporting aggregates impressions by campaign and by identifier rather than reconstructing a viewer's session. The complaint is widespread, well known, and unquantified — which means it is never prioritised against revenue features that have numbers attached.

## Why It's Still Broken
Reporting is built around the campaign because that is what is sold, so nobody produces the viewer-session view — a reporting model organised by the buyer's unit cannot describe the viewer's experience. The identifier fragmentation makes the true count hard to compute. The complaint is qualitative. And fixing it reduces fill or revenue in the short term.

## What a Fix Looks Like
Measure the session as the viewer experienced it. Reconstruct per-viewer ad exposure over a session and a day, which is the fix and is computable from delivery logs today. Report the distribution of repeat exposures, since the average will look fine and the tail is the problem. Resolve obviously identical creative across identifiers by fingerprint, as that alone will collapse much of the fragmentation without solving the full identity problem. Cap on the resolved creative as an interim measure, which is a partial fix available immediately. Report the worst-affected sessions, because a concrete example of eleven exposures in one evening moves a prioritisation conversation that a percentage does not. Handle the unsold break with house content or a shorter break rather than repeating, since filling with repetition is the worst available option. Correlate repetition with session abandonment, which quantifies the cost and is directly observable. Tell advertisers their true delivered frequency, as they are paying for wasted impressions and would object. Set an experience threshold that the fill logic must respect. And review the metric weekly, since it will regress as demand mix changes.

## Who Feels the Pain
Viewers who cancel the ad tier over the experience; advertisers paying for exposures that annoy their audience; ad operations teams configuring caps that do not bind; and a growth tier undermined by its own delivery.

## Impact If Fixed
A reporting model organised by the buyer's unit cannot describe the viewer's experience, so nobody sees the session. Reconstructing per-viewer exposure from delivery logs quantifies a well-known complaint and makes it prioritisable.
