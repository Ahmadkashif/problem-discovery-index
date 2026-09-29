# Fix: The Approval Rate Is Permanent and the Rejection Is Not Explained

**Niche:** [[niches/crowdsourcing-platforms/error-cost-allocation/profile|Error Cost Allocation]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** One requester's batch rejection permanently lowers an approval rate that gates access to better-paid work, and no reason was ever given.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #worker-facing #quick-win #compliance
**Contested on:** Whether a single requester's decision will be allowed to permanently gate someone's earnings.

## The Problem

Approval rate is the qualification that matters. Better-paying requesters gate on it — 95%, 98%, 99% — so a worker's access to the viable end of the market depends on it.

It is computed as a lifetime ratio, it does not age, and a single requester rejecting a batch of a hundred submissions can move it below a threshold that closes off a large share of available work. The rejection may have been for a broken task, an ambiguous item, or nothing at all, and the worker was given no reason.

Recovery is slow and mathematically brutal: a worker at 97% who is rejected on a hundred tasks needs thousands of approvals to climb back, during which the better-paid work they need to do that is closed to them.

## Why It's Still Broken

The metric is simple and requesters rely on it, so changing it means changing something requesters use to filter. The lifetime ratio is the crudest possible construction and it has persisted because nobody had to defend it.

Requesters also benefit from the crudeness: a high threshold on a noisy lifetime metric excludes a lot of people, which for a requester worried about quality feels safe.

And no reason is required for a rejection, so there is nothing to appeal even when an appeal exists.

## What a Fix Looks Like

Change the arithmetic and require a reason. Both are rule changes with no technical content.

Age the metric. Approval rate over the last few thousand tasks, or the last six months, rather than lifetime. Recent behaviour is what a requester is trying to predict and a lifetime ratio is a worse predictor of it, so this is better for requesters too.

Cap any single requester's contribution. No one requester should be able to move a worker's rate by more than a bounded amount, which prevents a single batch rejection from being career-altering while preserving the signal from a pattern across many requesters.

Require a reason from a fixed list on every rejection, attached to items. This costs a requester seconds and it is the precondition for any appeal existing.

Exclude overturned rejections and rejections from requesters under investigation. Where a requester's rejection rate is a large multiple of the population median, their rejections should be suspended from affecting approval rates pending review — a percentile lookup and a rule.

Report the rate with its uncertainty. A worker with 300 tasks and one with 30,000 have very different estimates behind the same percentage, and requesters filtering on a threshold are treating them identically.

And show the worker their own history: which requesters rejected, when, with what reason, and what it did to their rate. Currently a worker watches a number fall and has to reconstruct why from their own records.

## Who Feels the Pain

Workers whose access to viable work is closed by a single requester's unexplained decision, with a recovery path that requires the work they can no longer get. New workers, whose thin denominators make every rejection enormous. And requesters, filtering on a metric so noisy that it excludes many capable workers and admits others on a technicality.

## Impact If Fixed

A single rejection stops being able to end someone's access to the market. The metric ages, which makes it a better predictor and a fairer one. Rejections carry reasons, which makes appeals possible at all. And requesters whose rejection behaviour is far outside the norm stop being able to damage people while nobody is looking.
