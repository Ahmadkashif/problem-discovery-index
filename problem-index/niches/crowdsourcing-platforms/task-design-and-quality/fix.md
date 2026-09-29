# Fix: The Attention Check That Is Itself Ambiguous

**Niche:** [[niches/crowdsourcing-platforms/task-design-and-quality/profile|Task Design & Quality Enforcement]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A worker fails an attention check that was badly worded, loses payment for the whole batch, and has no way to point out that the check was wrong.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Whether the attention checks that gate payment will themselves be checked.

## The Problem

Attention checks are the standard quality device: an item with an obvious correct answer, inserted to catch workers clicking through without reading. Failing one frequently voids the entire submission and the payment for it.

Many are badly written. The "obvious" answer is obvious to the requester and not to a worker in a different country reading in a second language. The instruction says select the third option and the options are unnumbered. The check contradicts the main instructions. The check tests reading speed rather than attention. And the requester who wrote it will never know, because the people who fail it have no way to tell them and every incentive not to try.

The failure rate on a defective check is measurable and sits in the platform's data: an attention check failed by twenty percent of a population that passes everything else is not catching inattention.

## Why It's Still Broken

The check is the requester's to write and the platform does not review it. Requesters post thousands of batches and nobody could review them all by hand — which is true and is an argument for checking them statistically rather than not at all.

The consequence also falls entirely on the worker, so the requester receives no signal. A defective check quietly voids a share of submissions, the requester sees a lower cost per usable response, and nothing prompts a review.

And workers who complain about a check are, from the requester's perspective, workers complaining about being caught.

## What a Fix Looks Like

Check the checks, statistically, before they cost anyone their pay.

Compute the failure rate on every attention check, per batch, and compare it to the population's failure rate on other checks. A check failed by a large share of workers who pass everything else is defective, and this comparison is a query the platform can run in real time.

Hold payment decisions on a suspect check. When a check's failure rate crosses a threshold within the first fifty submissions, stop it voiding payments, flag it to the requester, and pay the affected workers. This is a rule, not a model, and it prevents nearly all of the harm.

Require more than one check to void a batch. A single failed item voiding an hour of work is disproportionate on any reading, and requiring two or three independent failures is both fairer and a better detector of actual inattention.

Give the worker a route to flag a defective item. One click, aggregated, with the flag count visible to the platform alongside the failure rate. Where both signals agree, the check is bad.

Screen checks before launch. Common defects — ambiguous wording, contradiction with the main instructions, unnumbered options referenced by number, cultural or language assumptions — are detectable by a language model reading the check against the instructions, and flagging them at posting time costs nothing.

And report failure rates back to requesters as a design metric. A requester whose checks fail at four times the platform median has a problem they would want to fix and cannot currently see.

## Who Feels the Pain

Workers who lose a batch's pay to a badly-worded item, disproportionately those working in a second language, and who have no appeal. Requesters, who discard valid responses from careful workers and never learn their check is broken. And the platform, whose central quality device is unvalidated at the point where it destroys someone's earnings.

## Impact If Fixed

Defective attention checks get caught by their own statistics within the first fifty submissions, before they void anyone's batch. A single failure stops being enough to withhold an hour's pay. And requesters find out that their check is broken, which is the only way it ever gets fixed.
