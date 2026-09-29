# Waiting on the Build

**Industry:** [[ci-cd-platforms|CI/CD Platforms]]
**Type:** Worker Life Changing
**One-liner:** Developers stop losing fragments of every day to a pipeline they cannot speed up, and stop discovering at minute forty that the failure was in the first test that ran.
**Tags:** #gradient-boosting #k-nearest-neighbors #time-series-forecasting #graph-theory #evaluation-metrics #automation #workflow-orchestration #worker-facing

## The Problem
A developer pushes a change and waits. Depending on the organisation this is a few minutes or the better part of an hour.

The wait is not idle in a useful way. It is too long to sit through and too short to start something substantial, so it produces a context switch — read messages, look at another task — and returning costs the reload of everything that was in working memory. Repeated several times a day, the cost is large and entirely invisible.

Then the pipeline fails at minute thirty-eight on a test that ran early in a stage that reports at the end. The developer fixes it and waits again. Two or three cycles of this consume an afternoon.

Some of the failures are flaky, so the response is a re-run and another wait, this time with no expectation of learning anything.

Queueing adds unpredictability. At busy times the build waits for a runner before it starts, so the same change takes fifteen minutes in the morning and forty at four in the afternoon, which makes planning around it impossible.

## Why It Matters to the Worker
The cost is attention rather than time, and attention is the scarce input to software engineering. A day fragmented by six pipeline waits produces less than one with two long uninterrupted stretches, and every developer knows this while no measurement captures it.

The powerlessness is its own frustration. The pipeline belongs to a shared configuration, its duration is the accumulated result of decisions by many teams, and an individual developer cannot make it faster. They can only wait, or batch changes into larger ones — which makes review harder and failures more ambiguous, so the pipeline's slowness degrades engineering practice upstream of itself.

And the late failure is the specific irritation: information that existed at minute three is delivered at minute thirty-eight because nothing ordered the work by likelihood of failure.

## What a Solution Looks Like
Fail fast by ordering. Run the checks most likely to fail for this specific change first — learned from which tests have historically failed for changes touching these files — so the developer learns in the first two minutes rather than the last. This requires no risk and no skipping, and it is the single largest improvement available to the experience.

Honest duration prediction. A developer told this will take twenty-six minutes can decide what to do with the interval; one watching an indeterminate progress bar cannot. Queue depth makes this predictable and it is not predicted anywhere.

Test selection with a stated miss rate, for teams willing to accept a measured risk in exchange for a much shorter loop.

Incremental result reporting, so a failure is surfaced when it happens rather than when its stage completes — which is a presentation change with a disproportionate effect on how the wait feels.

And flakiness handled before the developer sees it: a known-flaky failure should be identified as such rather than presented as a result to be interpreted.

## Impact If Solved
Pipeline wait time is one of the largest uncounted costs in software engineering, paid in fragmented attention. Ordering by failure likelihood and predicting duration honestly cost nothing and change the experience immediately, and they also stop the slow pipeline from degrading how engineers batch and review their work.
