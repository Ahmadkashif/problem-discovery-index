# Drift Detection Across Every Programme's Bordereaux

**Niche:** [[niches/reinsurers/programme-quota-share-oversight/profile|MGA & Programme Quota Share Oversight]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reinsurer behind thirty programmes receives thirty monthly bordereaux and learns that one of them has drifted when its loss ratio jumps a year later.
**Tags:** #change-point-detection #gradient-boosting #k-means-clustering #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to see a delegated-authority programme's underwriting drift in its monthly bordereaux before the loss ratio shows it, and whoever detects drift early enough to reprice or exit at the next renewal takes the account.

## The Problem
An MGA under growth pressure shifts toward classes or states outside its original appetite, lets rate slip, or slows claim reporting. Each change shows faintly in the bordereaux months before it shows in losses, but nobody compares month against month across programmes.

## Why Nobody Has Built This
Bordereaux are not standardised, each programme is managed by a different underwriter, and audit is treated as an annual event rather than a continuous measurement.

## What to Build
A normalised bordereaux store with per-programme baselines for class and state mix, average rate per exposure unit, limit profile and claim reporting lag. Change-point detection runs on each, and similar programmes are clustered so one programme's drift can be read against its peers. Alerts carry the evidence the underwriter needs for a renewal conversation.

## Target Customer
Heads of programme business and delegated authority managers at reinsurers with ten or more MGA and fronted programmes.

## Impact If Built
Programmes repriced or exited a renewal earlier than the loss ratio would force, which is where programme reinsurance profit is won or lost.
