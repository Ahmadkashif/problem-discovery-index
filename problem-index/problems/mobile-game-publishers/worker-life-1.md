# The Developer Whose Game Is Killed Every Three Weeks

**Industry:** [[mobile-game-publishers|Mobile Game Publishers]]
**Type:** Worker Life Changing
**One-liner:** A prototype team builds a concept, watches a retention number fall below a threshold, and starts again — dozens of times a year, with no way to know whether any of it was good.
**Tags:** #bayesian-inference #confidence-intervals #gradient-boosting #survival-analysis #evaluation-metrics #worker-facing #tacit-knowledge-ml #hypothesis-testing

## The Problem
Prototype teams at a hypercasual or hybridcasual publisher work on a cycle of weeks. Build a concept to testable state, ship it into a small paid campaign, wait for the numbers, and almost always kill it. The kill rate is by design and everyone knows the odds going in.

What makes it hard is not the failure rate but the absence of information in the failure. The number came from a few thousand installs with substantial sampling error; it was compared against a threshold nobody on the team derived; and the result is delivered as a binary. The developer does not learn what was wrong — whether the core mechanic failed, whether the first thirty seconds lost people, whether the acquisition source brought the wrong players, or whether the concept was simply below a line by an amount smaller than the measurement error.

So the learning loop, which should be the entire point of a high-volume prototype funnel, does not close. Teams accumulate intuitions from a long series of binary outcomes with unknown noise, which is close to the worst possible conditions for developing craft judgement.

And the work has no artefact. Nothing shipped, nobody played it, there is no portfolio piece, and a year of genuine effort leaves no trace except in an internal spreadsheet of killed concepts.

## Why It Matters to the Worker
This is a job structured as repeated rejection with no diagnosis. People can sustain a high failure rate when they learn from it; sustaining one where the feedback is a number without an explanation is much harder, and burnout in prototype teams is a known and discussed feature of this part of the industry.

The attribution problem is corrosive. A developer cannot tell whether they are improving. Two concepts that both died tell them nothing about their relative quality, and a concept that survived may have done so for reasons unrelated to the design. Over a career that produces either false confidence or none.

And the incentives push toward imitation. When the feedback is an opaque threshold, the safest strategy is to build something close to whatever passed recently, which is both professionally unsatisfying and — for a business whose returns come from outliers — commercially counterproductive.

## What a Solution Looks Like
Return a diagnosis, not a verdict. Telemetry from a prototype test shows where players stopped, which tutorial beat lost them, whether the core loop was reached, and how the retention curve is shaped rather than only where it landed. Reporting that with the kill decision turns a rejection into a finding.

State the uncertainty. A prototype that missed a threshold by less than the sampling error should be described that way, and the developer should know the difference between a clear failure and a coin flip. That single change alters what a team concludes about their own work.

Separate the game from the test conditions. Acquisition source, creative used, and the geography of the test all affect the retention number, and adjusting for them tells a developer whether the concept failed or the test did.

Aggregate across the funnel. What the publisher's whole history of prototypes says about which mechanics, first-session structures and difficulty curves survive is the craft knowledge this funnel should be producing, and it currently exists only as individual intuition in the people who have been there longest.

## Impact If Solved
A prototype funnel is a learning machine that has been wired to produce only a pass or fail. Returning diagnosis, uncertainty and test-condition adjustment converts the highest-volume experimentation programme in consumer product design into something the people running it actually learn from — which improves the concepts, and makes the job survivable for longer than the two years it currently tends to last.
