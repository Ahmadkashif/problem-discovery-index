# Measured From Places With Good Connectivity

**Niche:** [[niches/edge-cdn-providers/constrained-network-delivery/profile|Constrained Network Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Synthetic monitoring runs from well-connected data centres and reports excellent performance, which describes the experience of nobody the measurement was supposed to represent.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #quick-win #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to deliver acceptably to users on expensive, slow and intermittent connections — and whoever does that takes the markets where growth actually is, because the category's defaults assume conditions those users do not have.

## The Problem
Synthetic monitoring reports page load times from a set of vantage points, all of which are servers in data centres with excellent connectivity, several of them in the same facilities as the delivery nodes being measured. The numbers are excellent. They describe a path no user takes: no user is a server in a data centre next door to a cache. The organisation reviews these numbers monthly and concludes performance is good, while its users on mobile networks two thousand miles away have an experience nobody is measuring.

## Why It's Still Broken
Synthetic vantage points are placed where infrastructure is cheap and reliable, which is exactly where connectivity is good, and the bias is structural rather than chosen. Measuring from genuinely representative locations means devices on real mobile networks, which is operationally harder and more expensive. Real user monitoring covers the successful population and, as the build note describes, structurally omits the failures. And the good numbers are comfortable, so nobody has pressed the question.

## What a Fix Looks Like
Measure where the users are, on what the users have. Place vantage points on real consumer networks in the markets that matter rather than in data centres, which is available from several measurement providers and is the direct fix. Measure on representative devices, since a recent flagship and a four-year-old mid-range device differ enormously in parse and render time and the latter is what a large share of the audience holds. Emulate the network conditions of the target population explicitly — bandwidth, latency and packet loss profiles matched to real observations rather than to a generic slow-connection preset. Weight the reported aggregate by the actual audience distribution rather than averaging vantage points equally, since equal weighting over-represents wherever the provider happened to place servers. Report by segment rather than in aggregate, because the whole point is that the segments differ. And reconcile synthetic against real user measurement, since a large divergence between them is itself the finding and is currently unexamined.

## Who Feels the Pain
Users in markets whose experience nobody measures; product teams concluding a market does not convert; and organisations whose performance reporting describes a path no user takes.

## Impact If Fixed
Vantage points on real consumer networks and representative devices are available and are a procurement choice rather than a technical problem. Audience-weighted aggregation alone changes the reported number substantially and makes the underserved segments visible.
