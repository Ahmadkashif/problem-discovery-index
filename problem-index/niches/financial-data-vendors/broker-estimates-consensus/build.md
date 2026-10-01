# Event-Aware Consensus Hygiene

**Niche:** [[niches/financial-data-vendors/broker-estimates-consensus/profile|Broker Estimates & Consensus]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Specialists decide estimate by estimate what belongs in consensus, and years of those decisions — with the actuals that followed — have never trained a model.
**Tags:** #gradient-boosting #change-point-detection #bayesian-inference #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to hold the broadest set of contributed broker estimates at line-item detail and to clean them into a consensus clients trust — and whoever gets both the contributions and the hygiene right owns the number earnings surprises are measured against.

## The Problem
After a company changes guidance, some brokers revise within hours and others not for weeks. A consensus that averages both is wrong in a predictable direction, and earnings surprise — the number markets react to — is measured against it. Specialists catch the obvious cases; at peak volume they cannot catch all of them.

## Why Nobody Has Built This
Hygiene is treated as editorial work. The labels exist (inclusion and exclusion history) but the reasons are codes, and the objective — consensus closer to the actual on the same basis — requires an alignment the vendor rarely builds.

## What to Build
Define staleness relative to events (guidance, peer revisions, results) using change-point detection on the estimate cloud. Classify each contribution as include, stale, basis-mismatched or likely error, trained on specialist decisions and validated against consensus error versus same-basis actuals. Surface the recommendation and its reason to the specialist rather than auto-excluding, and report dispersion impact so legitimate contrarian estimates are not cleaned away.

## Target Customer
Heads of estimates content at consensus providers.

## Impact If Built
Consensus quality is the product's reputation. Event-aware hygiene makes it measurably better on the nights it matters most.
