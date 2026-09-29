# Explaining the Change Before It Lands

**Niche:** [[niches/game-liveops-services/the-designer-facing-the-community/profile|The Designer Facing the Community]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A correct change arrives as a number in a patch note and the reaction is set before any explanation exists.
**Tags:** #worker-facing #large-language-models #workflow-orchestration #evaluation-metrics #descriptive-statistics #automation #confidence-intervals #data-integration
**Contested on:** Every serious competitor in this niche is fighting to let a designer make a change the data clearly supports without spending the following fortnight being told publicly that they have ruined the game — and whoever solves that takes the account.

## The Problem
Balance changes land as bare numbers. Players experience them as arbitrary, infer bad intent, and respond at volume within hours. The designer holds evidence that the change was necessary — usage distributions, win rates, economy data — and it is either never published or published days later, after the narrative has formed. The consequence is not only an unpleasant fortnight for one person; it is that teams learn to avoid necessary changes.

## Why Nobody Has Built This
Patch notes are a communication artefact nobody owns analytically. Publishing the evidence feels like inviting argument. Community managers are not equipped to explain statistical reasoning and designers are not equipped to write for a hostile audience. And nobody has treated the designer's exposure as a problem to solve.

## What to Build
Publish the reasoning with the change, and put a team between the person and the feed. Generate a plain-language rationale from the data behind each balance change and ship it with the patch note, which is the core — the evidence exists and its absence is what makes the change look arbitrary. Publish the underlying distributions where they are not exploitable, since players argue far less with a chart than with a number. Signal intent before the change rather than announcing it after, as a pre-announced change is discussed and an announced one is resented. Attribute changes to the team rather than to an individual, which is the single most effective protection available. Triage community response into substantive and abusive, so the designer reads the first and never the second. Extract the genuine signal from the feedback volume, because there usually is some and it is buried. Prepare the follow-up communication in advance for changes expected to be unpopular. Track sentiment against the change so the team knows whether the explanation worked. Give community managers the evidence pack rather than the number, which is what lets them defend it. And make reading the raw feed nobody's job by default, which it currently is by omission.

## Target Customer
Live game operators, design and community teams, live ops platform vendors, and community management tooling providers.

## Impact If Built
The evidence exists and its absence is what makes a correct change look arbitrary. Shipping a generated rationale with the patch note, and attributing changes to the team, is what lets designers keep proposing correct changes.
