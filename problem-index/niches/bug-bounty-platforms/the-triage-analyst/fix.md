# Fix: Measured on Speed, Judged on the One They Missed

**Niche:** The Triage Analyst
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The analyst's objectives are throughput and time to triage, and the only mistake anyone will ever remember is the real vulnerability they closed.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #compliance #revenue-impact
**Contested on:** Whether the person reading the queue is supported as a specialist making consequential judgements, or measured as a throughput worker.

## The Problem

An analyst is measured on submissions handled and time to first response. Those are the numbers in the operational report and the ones discussed in a performance conversation.

The judgement they are actually employed to make is invisible in both. Whether the finding was real, whether the severity was right, whether the closure was correct — none of it is measured, because measuring it requires re-examination nobody funds.

The incentives this creates are sharp. Reading a submission carefully costs time against a target. Escalating a borderline case costs more. Closing it is fast and its cost — a vulnerability left in production — is invisible, deferred, and will never be traced back. An analyst behaving rationally under these objectives handles more submissions and looks at each one less.

And then, occasionally, a breach occurs and someone finds the submission that described it, closed as informative eight months earlier by a named person. That person was working to the objectives they were given, and the consequence lands on them entirely.

It is a working pattern designed to produce exactly the error it will later punish.

## Why It's Still Broken

**Speed is measurable and quality is not.** Time to triage is a number that exists. Correctness requires a second qualified analyst to re-examine a sample, which costs scarce capacity and produces an uncomfortable statistic.

**Programmes contract on response time.** Service levels specify triage speed because it is what a client can verify. The contract therefore encodes the wrong objective, and the operation optimises what the contract measures.

**The expensive error has no owner until it explodes.** Nobody is accountable for the wrongly-closed rate because nobody computes it, and then a single instance becomes very personally owned.

**Analysts have no calibration reference.** Without knowing how others assess comparable submissions, an analyst cannot tell whether they dismiss too readily. Nobody in this industry gives them that information.

**Career paths lead out of triage.** Progression means leaving the queue, so accumulated triage expertise leaves with the person, and the role is continually restaffed with people early in their calibration.

**Researcher disputes land personally.** The analyst absorbs the argument for a decision made under a throughput target, and public escalation is directed at them individually rather than at the operation.

## What a Fix Looks Like

**Measure quality and report it alongside speed.** Sampled blind re-examination of closed submissions, producing a per-analyst and operation-wide accuracy figure. This is the change that makes everything else possible — an objective nobody measures is an objective nobody has.

**Remove the throughput penalty for depth.** Time targets computed excluding escalated and deliberately deep-examined submissions, so careful work does not damage the analyst's numbers. Until this is true, no amount of encouragement to be thorough will work.

**Make escalation free and expected.** A defined path for uncertainty with no cost, and a stated expectation that a healthy escalation rate is normal. An operation where nobody escalates is not an operation with no hard cases.

**Give analysts calibration feedback privately.** Their assessments against adjudicated references and peer distributions, confidentially, framed as development and kept out of performance management — because a calibration tool used for performance will be gamed within a month.

**Negotiate service levels on quality, not only speed.** Programme contracts should specify accuracy measurement alongside response time. Clients want correct triage more than fast triage and have never been offered the choice.

**Build a career path through triage.** Senior triage as a destination — specialism, adjudication, calibration ownership — rather than a stage to leave. The expertise is real and the industry currently discards it on a cycle.

**Take the disputes off the individual.** Researcher escalations addressed by the operation rather than by the named analyst, so a decision made under organisational constraints is defended organisationally.

## Who Feels the Pain

The analyst, working to objectives that reward exactly the behaviour that produces the error they will be blamed for.

The researcher, whose valid finding was closed by someone with three minutes and no reference.

The organisation, which had the vulnerability described to it and declined it, and will not connect the two events if it is later exploited.

And the platform, whose core quality claim rests on judgements it does not measure, made by people it measures on something else.

## Impact If Fixed

Measuring accuracy and reporting it next to speed reframes the role from throughput work to quality control, which is what it actually is. The measurement is the fix.

Removing the throughput penalty for depth costs some apparent efficiency and buys back the careful reading that the whole operation depends on.

And a real career path through triage would let the industry retain calibrated judgement instead of rebuilding it every eighteen months, which is the compounding cost nobody counts.
