# Deciding From a Filename

**Niche:** [[niches/music-distribution-platforms/the-content-reviewer/profile|The Content Reviewer]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The uploader has had four releases rejected for impersonation this month and the reviewer looking at the fifth cannot see that.
**Tags:** #quick-win #worker-facing #graph-theory #automation #evaluation-metrics #descriptive-statistics #confidence-intervals #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to let a reviewer decide in seconds whether a release is legitimate, at a volume that only grows — and whoever gives them evidence instead of a filename changes both the accuracy and the survivability of the role.

## The Problem
Each release is reviewed as an isolated item. The account behind it may have a history of rejections, may have been created last week, may be uploading in batches at three in the morning, may share a payment method with a previously banned account. All of that is recorded and none of it is shown. The reviewer makes an independent judgement about a single release while the pattern that would settle it sits one query away.

## Why It's Still Broken
The queue was built around the release because the release is the unit of work, so the account context was never joined — a workflow organised by item cannot see a pattern across items belonging to the same actor. Account data sits in a different system. Reviewers are measured on throughput. And the pattern is obvious only in aggregate, which nobody presents.

## What a Fix Looks Like
Show the account, not just the release. Display uploader history, account age, prior decisions and release cadence on every review, which is the fix and is a join between two existing systems. Group an account's releases into one review where they arrive together, since batch uploads are reviewed item by item and the batch is the signal. Flag accounts sharing payment methods or other identifiers with previously actioned ones, as that link is the strongest available and is currently unused. Show near-matches to established artist names automatically, because impersonation is the highest-consequence case and name similarity is computable. Surface prior appeals and their outcomes, which prevents relitigating and helps the legitimate artist who was wrongly blocked before. Rank the queue by account risk rather than by arrival time. Let a reviewer action an account rather than only a release, since the release-level remedy is why the same uploader returns. Record the decision reason in a fixed vocabulary, which is what makes the pattern analysis possible at all. Report decisions by reason and by account, so the abuse shapes become visible. And escalate the repeat account rather than re-reviewing it, because the fifth release from a known bad actor should not consume a judgement.

## Who Feels the Pain
Reviewers making isolated judgements about coordinated behaviour; legitimate artists caught alongside; streaming services receiving what slipped through; and distributors penalised for abuse they could have seen.

## Impact If Fixed
A workflow organised by item cannot see a pattern across items belonging to the same actor, so the account context was never joined. Showing uploader history and identifier links on every review is a join between existing systems and settles most of the ambiguous cases.
