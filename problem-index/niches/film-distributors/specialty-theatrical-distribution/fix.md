# The P&L Model That Is Overwritten at Signature

**Niche:** [[niches/film-distributors/specialty-theatrical-distribution/profile|Specialty Theatrical Distribution]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** The acquisitions P&L is revised a dozen times during a bidding war, and the version that justified the final number is the one nobody saves.
**Tags:** #large-language-models #evaluation-metrics #feature-engineering #workflow-orchestration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a festival film against what its platform release, awards run and later windows will actually earn, and whoever prices closest to the outcome wins the films that pay back and avoids the ones that sink the slate.

## The Problem
During an auction the acquisitions team updates one spreadsheet as the price climbs: P&A raised, international assumptions stretched, the streamer licence nudged up until the bid clears. After signature the same file becomes the release budget. Two years later, when the film underperforms, nobody can see which assumption was stretched to win it.

## Why It's Still Broken
The model lives in a shared drive, versions are overwritten in a hurry, and the bid's reasoning is in phone calls and texts. Nothing in the workflow prompts anyone to freeze the version that set the price.

## What a Fix Looks Like
Snapshot every version of the acquisition model automatically, with the time and the bid it supported. Flag the final pre-signature version and diff it against the first. Draft a one-paragraph note of which assumptions moved and why, from the team's emails, for the buyer to confirm. Store it with the contract.

## Who Feels the Pain
CFOs explaining write-downs to boards and lenders; heads of acquisitions defending past bids; new buyers trying to learn the firm's pricing habits.

## Impact If Fixed
At almost no cost in time, every acquisition gets a record of the assumptions that bought it. That is the raw material for grading bids, and it ends the post-mortem argument about what anyone thought at the time.
