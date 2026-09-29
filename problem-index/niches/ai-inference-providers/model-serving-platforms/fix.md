# Benchmarks Published at Concurrency One

**Niche:** [[niches/ai-inference-providers/model-serving-platforms/profile|Model Serving Platforms]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Published throughput and latency figures are measured on an idle machine serving one request, and every customer runs on a shared fleet under concurrent load where the numbers are unrecognisable.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #probability-distributions #markov-chains #quick-win #monte-carlo-methods
**Contested on:** Not terminal — the contest differs by whether latency is constrained, and the decomposition is recorded in the profile.

## The Problem
A provider advertises tokens per second and time-to-first-token for a given model. The figures are measured with one request on a dedicated accelerator. In production the request joins a continuous batch with thirty others of varying prompt lengths, on hardware shared with other tenants, and the experienced numbers are different — sometimes by a factor. The benchmark is not dishonest, it is a measurement of a condition no paying customer is ever in, and every provider publishes the same way, which makes comparison a comparison of nothing.

## Why It's Still Broken
Single-request numbers are reproducible and comparable, which is what a published benchmark wants to be. Under-load figures depend on the mix, which is customer-specific and makes a headline number harder to state. No provider will publish worse-looking numbers unilaterally. And customers evaluate on the published figures because constructing a realistic load test across several providers is a project they do not have time for.

## What a Fix Looks Like
Publish the curve instead of the point. Report latency against concurrency as a curve rather than a single figure, since that is the shape a customer actually operates on and it costs nothing extra to measure — this is the change, and everything else follows from it. Report the tail rather than the mean, because the tail is what breaks a product and the mean is what flatters a provider. Publish under a realistic prompt and output length mix rather than a uniform one, since batch composition dominates the result and uniform mixes are the most favourable case. State the tenancy conditions of the measurement plainly — dedicated or shared — because that difference alone explains much of the gap customers experience. Offer a load-test harness a customer can run against their own traffic shape, which is the fully honest answer and is cheap to provide. Report achieved service levels from production rather than from a lab, since providers have that data and publishing it would be far more credible than any benchmark. And report variance, since these systems are noisy and a single run comparison between close competitors is frequently meaningless.

## Who Feels the Pain
Customers who chose on published numbers and built a product against latency they do not get; providers whose genuinely better behaviour under load is unrewarded; and engineers whose capacity plans were built on a measurement from an idle machine.

## Impact If Fixed
The published figure measures a condition no paying customer is ever in. A latency-against-concurrency curve costs nothing extra to measure and is the shape customers actually operate on; production service levels would be more credible than any benchmark.
