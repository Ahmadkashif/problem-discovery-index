# Experience Quality Measurement From Streaming Video

**Niche:** [[niches/game-hosting-providers/match-outcome-measurement/profile|Match Outcome Measurement]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Streaming video established what a rebuffer costs in abandonment and built its whole delivery stack around that number, and multiplayer has no equivalent.
**Tags:** #causal-inference #survival-analysis #confidence-intervals #evaluation-metrics #hypothesis-testing #logistic-regression #descriptive-statistics #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to put a number on what a mismatched match, a long queue and excess latency each cost in whether the player queues again — and whoever produces that number takes the account.

## The Problem
Streaming video faced the same question and answered it. The industry established, with real measurement, what a startup delay costs in abandonment, what a rebuffer costs in viewing time, and what a bitrate drop costs in engagement — and then designed the entire adaptive delivery stack around those numbers. The quality-of-experience literature is public, the metrics are standardised, and every major delivery decision is justified against them. Multiplayer gaming has richer data and no equivalent.

## What Already Exists
Quality-of-experience metric frameworks; measured relationships between technical quality and abandonment; engagement impact estimation; adaptive delivery optimisation against those measures; and industry-standard definitions.

## The Customization Gap
The adaptation is to an experience whose quality depends on other people. It requires: (1) quality determined partly by who else was matched, so the experience is social rather than purely technical — video has no equivalent of a one-sided match, and this is the substantive difference; (2) three interacting factors rather than a delivery quality ladder; (3) an outcome measured in returning to queue rather than in session duration, since a bad match can be completed and still cost the player; (4) asymmetric experience within one session, where the winner and loser of the same match are affected differently; and (5) no industry-standard definitions at all, so the metric framework must be established before it can be applied.

## Target Customer
Studios operating multiplayer titles, hosting and platform vendors, analytics firms, and quality-of-experience measurement vendors.

## Impact If Solved
Streaming established what a rebuffer costs and rebuilt its delivery stack around it. Quality that depends on who else was matched, and an outcome measured in returning to queue, are what make this a new framework rather than a port.
