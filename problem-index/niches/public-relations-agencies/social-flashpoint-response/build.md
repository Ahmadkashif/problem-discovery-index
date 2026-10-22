# Escalation Forecasts From Amplifier Mix, Not Volume

**Niche:** [[niches/public-relations-agencies/social-flashpoint-response/profile|Social Media Flashpoint Response]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Experienced crisis counsellors judge a flare-up by who is sharing it, not how much, and no tool encodes that read.
**Tags:** #tacit-knowledge-ml #survival-analysis #graph-neural-networks #gradient-boosting #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to call, within the first hours, whether an online flare-up will reach mainstream media and whether responding will feed it or kill it, and whoever calls escalation right most often keeps the client's crisis retainer.

## The Problem
Two complaints about a product each reach 5,000 posts in three hours. One is driven by a few large accounts recycling the same video; the other is spreading through journalists, a consumer advocacy group and a state legislator. The senior counsellor knows the second is the story. The dashboard shows two identical volume spikes.

## Why Nobody Has Built This
Listening vendors sell detection to many buyers and optimise for alert recall. The outcome label (did it reach tier-one media, did it last, did it cost sales or trigger regulators) sits in agencies' and clients' memories, not in the vendor's data.

## What to Build
A forecaster that represents each emerging issue by its amplification network (account types, journalist and activist involvement, cross-platform jumps, outlet pickup sequence) and estimates the hazard of tier-one pickup at 6, 24 and 72 hours, trained on a labelled archive of past flare-ups with outcomes. Capture the senior counsellor's call on each live issue as an extra label and report the model against it.

## Target Customer
Crisis and social practices at agencies serving consumer brands; in-house brand reputation teams.

## Impact If Built
Fewer unnecessary responses that create stories, earlier action on the issues that matter, and a counsellor's pattern recognition available to the overnight watcher.
