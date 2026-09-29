# Knowing What Was Acted On

**Niche:** [[niches/player-research-firms/implementation-tracking/profile|Implementation Tracking]]
**Industry:** [[industries/player-research-firms|Player Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm does not know which of its recommendations were taken, and nobody has ever asked.
**Tags:** #workflow-orchestration #data-integration #evaluation-metrics #descriptive-statistics #automation #confidence-intervals #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to find out which of its recommendations the development team actually acted on — and whoever establishes that takes the account.

## The Problem
A study produces recommendations, they are presented, and the engagement ends. Some are implemented immediately, some are deferred, some are rejected for reasons the researcher never hears — the change was too expensive, it conflicted with a design intent, the team disagreed with the interpretation, or nobody had time. All of that is knowable by asking, and it would tell the firm which of its findings survive contact with a real development schedule.

## Why Nobody Has Built This
The engagement ends at the readout and the follow-up is unpaid. Researchers worry the question reads as chasing. The recommendations are prose in a deck rather than trackable items. And nobody has framed the implementation rate as a metric worth having.

## What to Build
Make the recommendation a trackable object and ask about it on a schedule. Record each recommendation as a discrete item with an identifier, a priority and an owner, which is the core and is what converts a deck into something that can be followed. Capture the client's response at the readout — accepted, deferred, rejected — which is free and happens in the room. Follow up at defined intervals with a light request rather than an audit, since most clients will answer a single short question. Record rejection reasons in a consistent vocabulary, as the pattern across rejections is the most useful thing in the whole exercise. Report the firm's implementation rate by client, study type and recommendation type, which nobody currently knows. Identify the recommendation characteristics that predict implementation — specificity, cost, priority, framing — because that is directly actionable in how findings are written. Feed it back into report writing, which is where the firm can change its own outcomes immediately. Show clients their own implementation rate, which they also do not know and frequently find uncomfortable and useful. Handle multi-study programmes as a cumulative record. And keep the follow-up light enough that it happens, since an elaborate process will not.

## Target Customer
Games user research firms and platforms, in-house research functions, publishers, and research operations vendors.

## Impact If Built
The pattern across rejections is the most useful thing the firm could learn and nobody records it. Trackable recommendations with a light follow-up gives a firm its implementation rate and tells it how to write findings that get used.
