# Benchmarks Run on Contended Hardware

**Niche:** [[niches/ai-inference-providers/the-performance-engineer/profile|The Performance Engineer]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Performance measurements are taken on accelerators shared with production traffic, where run-to-run variance routinely exceeds the regression being investigated.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #monte-carlo-methods #probability-distributions #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to attribute a latency regression to the layer that caused it without a person bisecting five independently-moving components — and whoever does that takes the account, because that bisect is most of a performance engineer's week.

## The Problem
An engineer measures a configuration and gets 42 milliseconds. They change one variable and get 45. They change it back and get 44. The accelerator is shared with production traffic whose composition varies minute to minute, the thermal state differs between runs, and the fleet is mixed so the node may not even be the same hardware generation. Days are spent chasing differences that are entirely measurement noise, and real regressions are dismissed as noise because everything looks like noise. The team's confidence in its own numbers is low and correctly so.

## Why It's Still Broken
Reserving accelerators for benchmarking removes them from revenue service, which loses every budget argument against a cost that is measured in engineer-days nobody counts. Benchmarking practice in this industry is inherited from kernel microbenchmarks where variance is small, so the statistical discipline was never developed. The mixed fleet is a procurement reality. And an engineer who reports a range rather than a number is perceived as less decisive than one who reports 42.

## What a Fix Looks Like
Control the measurement, then treat it statistically. Reserve a small pool of uncontended, homogeneous accelerators for benchmarking, which is a handful of devices against days of repeated engineer time and wins the argument once anyone counts the other side — this is the fix and the rest is method. Pin everything controllable: clocks where possible, thermal state through warm-up, hardware generation, and the full software manifest. Repeat every measurement and report an interval, making a single-run number an unacceptable result, which removes most of the false chases immediately. Establish the noise floor per benchmark and hardware type, so everyone knows what magnitude of difference is meaningful before they start — this single measurement changes how every subsequent investigation is run. Use paired comparison on the same hardware in the same session, which cancels most of the variance and is far more sensitive than comparing two independent measurements. Reject investigations of differences inside the noise floor as a matter of policy. And report production measurements separately from benchmark measurements, since they answer different questions and mixing them is a recurring source of confusion.

## Who Feels the Pain
Performance engineers chasing noise and dismissing signal; teams whose optimisation decisions rest on unreliable comparisons; and providers shipping regressions because everything looked like variance.

## Impact If Fixed
A handful of reserved accelerators costs less than the repeated engineer-days nobody counts. Establishing the noise floor per benchmark tells everyone what magnitude is meaningful before they start, and paired comparison in a single session cancels most of the variance outright.
