# Real User Monitoring, Joined to Configuration

**Niche:** [[niches/edge-cdn-providers/edge-delivery-platforms/profile|Edge Delivery Platforms]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Real user monitoring is mature and available from every provider, and it is sold as a dashboard rather than joined to the configuration decisions that determine what it measures.
**Tags:** #descriptive-statistics #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #data-integration #automation
**Contested on:** Every serious competitor here is fighting to be the network a customer's traffic flows through — and that contest is fought on cost per byte in one market and on latency for uncacheable content in another, which is why this niche is not terminal and is decomposed below.

## The Problem
Real user monitoring collects how long real pages took for real users on real networks, with detailed timing breakdowns, and is available from every provider in the category and from several independent vendors. It produces dashboards. The configuration decisions that determine those timings — caching rules, routing, protocol settings, compression, edge logic — are made in a different interface, and no product connects a change in one to an outcome in the other.

## What Already Exists
Real user monitoring with standard browser timing interfaces; synthetic monitoring from many vantage points; web performance metrics with established definitions; causal inference methods for before-and-after comparison; and the experimentation infrastructure that consumer software uses routinely. All mature.

## The Customization Gap
The adaptation is to configuration changes evaluated on real traffic. It requires: (1) a change log joined to the measurement stream, so every configuration change is a marked event against which the outcome can be evaluated — which is the missing join and is trivial to create and currently created by nobody; (2) segment-aware evaluation, because a change improves one region and degrades another more often than it moves a global number, and the aggregate comparison will find nothing; (3) proper handling of confounding, since traffic mix, device composition and network conditions shift continuously and a naive before-and-after comparison mostly measures those; (4) the ability to apply a change to a fraction of traffic, which converts an observational comparison into an experiment and is technically straightforward at the edge and offered by almost nobody; and (5) an outcome measure that includes the business metric where available, since a latency improvement that does not change abandonment is worth knowing about.

## Target Customer
Edge and CDN providers, real user monitoring vendors, and the platform teams making configuration decisions with no feedback.

## Impact If Solved
The measurement exists, the configuration exists, and nothing joins them, which is why nobody in this category can say whether a change helped. Fractional application at the edge turns the comparison into an experiment and is the capability that would settle the question properly.
