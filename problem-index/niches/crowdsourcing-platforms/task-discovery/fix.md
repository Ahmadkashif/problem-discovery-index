# Fix: The Qualification Test Nobody Pays For

**Niche:** [[niches/crowdsourcing-platforms/task-discovery/profile|Task Discovery & Unpaid Search Time]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A twenty-minute qualification test, unpaid, for access to a batch that may already be gone by the time it is graded.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #worker-facing #quick-win #automation
**Contested on:** Whether time spent proving you can do the work is part of the work.

## The Problem

Qualification tests gate access to better-paid batches. They take minutes to an hour, they are unpaid, and passing one does not guarantee any work at all — the batch may be exhausted by the time the test is graded, the requester may never post again, or the qualification may be for a one-off study.

Workers therefore invest unpaid time on a speculative basis, repeatedly. The ones who invest most are the ones with the least slack, and a worker who takes four qualification tests in an evening and gets no work from any of them has spent a shift earning nothing.

Requesters frequently do not intend this. A researcher building a qualification for a study genuinely does not realise that a hundred people will spend twenty minutes each to access forty slots.

## Why It's Still Broken

Qualifications are a requester tool and the time cost falls on the other side, so it appears in nobody's accounting. A requester sees a qualified pool; they do not see the hours spent assembling it.

The platforms treat qualification as infrastructure rather than as work, which was a defensible position when tests were two questions and is not when they are twenty minutes.

And no mechanism exists to pay for it. Qualification sits outside the task-payment flow entirely, so even a requester who wanted to compensate it has no way to.

## What a Fix Looks Like

Pay for it, size it, and make it reusable.

Pay for qualification tests above a duration threshold, at the same implied rate as the task. The mechanism is the same as a task payment and the cost is small relative to a batch. A requester told that their twenty-minute qualification will cost $3 per applicant will either shorten it or accept the cost, and both outcomes are better than the current one.

Report the time cost to the requester. Applicants, median completion time, total unpaid hours consumed, and how many of the qualified actually received work. Most requesters have never considered this and the ratio is frequently startling.

Make qualifications reusable. A worker who qualifies for a task type should carry that qualification across requesters with similar requirements, rather than retaking an equivalent test for each. Platform-level qualifications by skill or task type — properly designed, periodically revalidated — would eliminate most of the repetition.

Show the odds before the test. How many qualified workers already exist, how many slots remain, and how much work this requester has posted historically. A worker deciding whether to spend twenty minutes should know they are the two hundredth applicant for forty slots.

Cap the duration for unpaid tests. An unpaid qualification above a few minutes is not a screening device, it is unpaid work, and a platform limit resolves it without requiring anyone's goodwill.

And expire qualifications tied to batches that never materialised, so the record of a worker's investment is not simply lost.

## Who Feels the Pain

Workers, spending unpaid hours on speculative access, and disproportionately newer ones who have not learned which qualifications are worth taking. Requesters, who did not know what their screening cost and would frequently shorten it. And the platform, whose worker supply is spending a meaningful share of its time on unpaid prerequisites.

## Impact If Fixed

Qualification time gets paid or gets short, and either is better than the current arrangement. Requesters see what their screening costs the people taking it. Platform-level qualifications remove the repetition. And a worker can tell, before starting, whether the twenty minutes has any chance of leading to work.
