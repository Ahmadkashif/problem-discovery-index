# Seconds, With Evidence

**Niche:** [[niches/music-distribution-platforms/the-content-reviewer/profile|The Content Reviewer]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The reviewer decides whether a stranger's release is legitimate from a filename and thirty seconds of audio.
**Tags:** #contrastive-learning #graph-theory #gradient-boosting #worker-facing #evaluation-metrics #confidence-intervals #automation #transformers
**Contested on:** Every serious competitor in this niche is fighting to let a reviewer decide in seconds whether a release is legitimate, at a volume that only grows — and whoever gives them evidence instead of a filename changes both the accuracy and the survivability of the role.

## The Problem
The queue contains impersonations of established artists, uploads of other people's recordings, releases designed to capture search traffic for a well-known name, and a large majority of legitimate music from people nobody has heard of. Distinguishing them requires knowing whether this uploader has done this before, whether the recording matches something already released, whether the artist name is close to a known one, and whether the account's behaviour resembles known abuse. None of that is in front of the reviewer.

## Why Nobody Has Built This
Review was staffed to absorb a growing queue, so the investment went to headcount rather than to evidence — a function that scales by hiring does not develop tooling until hiring stops working. Fingerprinting was deployed for known-recording detection and stops there. Outcomes are rarely known, so reviewer accuracy is unmeasured and therefore unmanaged. And the failures are visible only when they reach a platform.

## What to Build
Assemble the case before the reviewer sees it. Surface the uploader's history, account behaviour and prior decisions alongside every release, which is the core and is the context that turns a guess into a judgement. Detect name similarity to established artists, since impersonation is the highest-consequence category and is largely a string and entity problem. Match audio against existing catalogue beyond exact fingerprints, as re-uploads are frequently altered enough to defeat exact matching. Model the abuse patterns — batch uploads, account age, payment signals, metadata templates — because abusive releases arrive in recognisable shapes and individual review sees them one at a time. Auto-clear the unambiguous, so the reviewer's seconds go to the cases that need them. Rank the queue by risk rather than by arrival, which is where the accuracy improvement comes from. Return outcomes to reviewers where they become known, as the role currently learns nothing. Measure consistency with duplicated cases, since it is the only available quality signal. Give the rejected artist a specific reason and an appeal, because a legitimate release blocked without explanation is a serious harm and is currently common. And track the cases that reached a platform and were caught there, which is the honest measure of what the function misses.

## Target Customer
Trust and safety leadership, reviewers, artists wrongly blocked, streaming services receiving the output, and content protection vendors.

## Impact If Built
A function that scales by hiring does not develop tooling until hiring stops working, so the queue grew and the evidence did not. Uploader history and name-similarity detection are the context that make a seconds-long decision defensible.
