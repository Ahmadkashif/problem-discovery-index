# The Load Test That Did Not Look Like the Launch

**Niche:** [[niches/game-hosting-providers/launch-day-operations/profile|Launch Day Operations]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The load test passed at twice expected concurrency and the launch failed at half of it, because the test ramped over an hour and the launch did not ramp at all.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #confidence-intervals #automation #workflow-orchestration #time-series-forecasting #compliance
**Contested on:** Every serious competitor in this niche is fighting to make a one-time event at a fixed hour, in front of everyone, run by a small team on somebody else's estimate, into something rehearsed rather than improvised — and whoever does it takes the account.

## The Problem
Load tests routinely pass and launches routinely fail, and the reason is usually shape rather than volume. The test ramps gradually to a target; the launch arrives as a vertical wall at the unlock second. The test spreads load evenly; the launch concentrates it in two regions. The test exercises one subsystem at a time; the launch saturates authentication, matchmaking and allocation together. The test measured the wrong thing and everyone drew confidence from it.

## Why It's Still Broken
The test models volume rather than shape — a system validated against a gradual ramp has been told nothing about how it behaves against a vertical one, and the passing result actively creates false confidence. Load tools default to ramping. Nobody compares the test profile against past launch curves. And the test's success is reported as readiness.

## What a Fix Looks Like
Test the shape you will actually get. Rebuild the load profile from an actual past launch curve rather than from a ramp, which is the fix and needs only a chart the provider already has. Concentrate the synthetic load regionally to match the expected distribution, since even global totals hide the regional failure. Saturate all subsystems simultaneously rather than testing each in isolation, as the interaction is where launches break. Include the retry storm that follows the first failure, because that is the amplification that turns a stumble into an outage. Test the cold-start path, since the first minutes run against empty caches and unwarmed pools. Compare the test profile against past launch curves explicitly, which makes the mismatch obvious before anyone relies on the result. Report the shape the test used alongside the result, so confidence is calibrated. Test the degradation path rather than only the success path. Run the test at the actual unlock hour where possible, which surfaces scheduling and dependency issues. And require a shape justification before a test result is accepted as readiness evidence.

## Who Feels the Pain
Infrastructure teams who tested and still failed; studios whose launch was judged in the first ten minutes; players in a queue that never moved; and the account relationship afterwards.

## Impact If Fixed
A system validated against a gradual ramp has been told nothing about how it behaves against a vertical one, and the passing result actively creates false confidence. Rebuilding the profile from a real launch curve costs nothing and changes what the test means.
