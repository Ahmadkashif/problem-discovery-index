# Every Millisecond Paid by Every Call

**Niche:** [[niches/api-infrastructure-providers/internal-platform-api-traffic/profile|Internal Platform API Traffic]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform layer in front of every internal service is paid for by every call in the company, and no vendor reports what their layer actually costs in latency, compute and engineer time.
**Tags:** #time-series-forecasting #descriptive-statistics #change-point-detection #optimization-fundamentals #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to carry service-to-service traffic with negligible latency cost and negligible friction for the teams deploying behind it — and whoever does that takes the platform account, because the alternative is that teams route around the layer entirely.

## The Problem
An organisation adopts a service mesh for the resilience and observability. Eighteen months later the sidecars consume a noticeable share of the cluster's compute, the added latency per hop is small and is multiplied by a call graph that is eleven hops deep for a user-facing request, three engineers work full time on the mesh, and several teams have quietly exempted their latency-sensitive services. Nobody computed any of this in advance because no vendor reports it and no customer asked for the numbers in a form that would have been comparable.

## Why Nobody Has Built This
Vendors benchmark throughput in isolation, which is the flattering measurement and bears little relation to the cost in a real call graph. The cost is also structurally hidden: latency is per hop and the pain is per request path, compute is spread across every workload, and engineer time is a headcount line rather than a product cost. Customers cannot compare because nobody publishes in comparable terms. And the exemptions that accumulate — services that opted out — are the clearest evidence of the problem and are not tracked anywhere.

## What to Build
Make the total cost visible and then reduce it. Measure the layer's cost as deployed: added latency per hop and per user-facing request path, compute and memory overhead as a share of the workload, and the engineering effort to operate it — reported to the customer about their own estate rather than as a vendor benchmark. Expose the multiplication explicitly, since the interesting number is the added latency on the ninety-ninth percentile of a deep request path and not the per-hop median. Track exemptions, because a service that has opted out is both a coverage gap and a complaint, and neither is recorded today. Then attack the cost where the data shows it: selective policy application so that simple internal calls do not pay for features they do not use, and configuration defaults derived from what the traffic actually needs rather than from a maximal template. Report the friction side too — time from a new service existing to being correctly onboarded, and how many steps it takes — since that determines whether teams adopt or route around. And give platform teams the comparison they cannot currently make, because a decision of this magnitude is made on vendor benchmarks and a proof of concept.

## Target Customer
Platform engineering teams operating or evaluating a service layer, and the mesh and gateway vendors willing to compete on total cost rather than on throughput.

## Impact If Built
The cost of the layer is real, multiplied by every call, and is not reported by anyone in comparable terms. Exemption tracking is the clearest available signal of where the layer is too expensive, and it is currently invisible.
