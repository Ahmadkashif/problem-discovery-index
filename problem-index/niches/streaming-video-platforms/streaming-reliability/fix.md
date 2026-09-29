# It Worked in the Load Test

**Niche:** [[niches/streaming-video-platforms/streaming-reliability/profile|Streaming Reliability]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The test simulated twice normal load and the launch delivered eleven times it, in a shape nothing had rehearsed.
**Tags:** #quick-win #time-series-forecasting #evaluation-metrics #descriptive-statistics #confidence-intervals #automation #change-point-detection #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to survive the moment when a hundred million dollars of marketing delivers every subscriber to the same play button at the same second — and whoever predicts and absorbs that concentration keeps the launch that pays for the year.

## The Problem
The load test passed. It ran at a multiple of average traffic, in a smooth ramp, against a subset of the system, on a weekday afternoon. The actual launch produced a near-vertical spike at midnight, concentrated on one title, across every client type at once, with everyone hitting the same few code paths simultaneously. The test bore no resemblance to the event, and the test passing is what created the confidence.

## Why It's Still Broken
Load testing practice defaults to a ramp against a target multiple, so the test's shape is a convention rather than a model of the event — a test designed to be runnable is not a test designed to be realistic. Testing the true shape is expensive and disruptive. The forecast the multiple is based on is itself an average-derived guess. And a passing test ends the conversation.

## What a Fix Looks Like
Test the shape, not the multiple. Model the launch's expected arrival shape from previous launches and test against that, which is the fix and is the difference between a realistic test and a reassuring one. Test the concentration on a single title, since real launches concentrate on one piece of content and tests distribute load evenly. Include every client type, because client-specific failures are common and are usually untested. Test at the real hour with the real cold-start conditions, as a warm system at two in the afternoon is not the system at midnight. Test the failure modes deliberately rather than only the success path, since what happens when a component saturates is the thing that determines the outcome. Review previous launch telemetry to derive the shape, which exists and is not being used to design the tests. Record what the test did and did not cover, so the confidence it produces is proportionate. Rehearse the incident response alongside the load, because the response is as untested as the system. Test the degradation path specifically, as it is the mitigation and is the least exercised code in the system. And compare every launch to the forecast afterwards, which is how the next test gets designed properly.

## Who Feels the Pain
Engineers on call for a launch their tests did not represent; viewers who cannot watch what they were marketed; content and marketing teams whose investment fails publicly; and reliability teams whose passing test produced false confidence.

## Impact If Fixed
A test designed to be runnable is not a test designed to be realistic, and its shape is a convention rather than a model. Deriving the arrival shape from previous launches and testing that is the difference between confidence and readiness.
