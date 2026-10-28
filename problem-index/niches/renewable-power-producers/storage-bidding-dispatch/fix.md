# Optimiser Claims Nobody Can Audit

**Niche:** [[niches/renewable-power-producers/storage-bidding-dispatch/profile|Battery Storage Bidding & Dispatch]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Fix (Pain Point)
**One-liner:** Every optimiser reports a capture rate against its own benchmark, so an owner choosing or renewing one cannot tell skill from a favourable comparison.
**Tags:** #dynamic-programming #evaluation-metrics #descriptive-statistics #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to capture the most of a battery's theoretical market revenue, and whoever has the highest capture rate against a perfect-foresight benchmark takes the account.

## The Problem
Perfect-foresight revenue depends on assumptions: which markets, which state-of-charge limits, which cycle cap, which interval. Optimisers choose them, and the owner signs multi-year revenue-share contracts on the result.

## Why It's Still Broken
Owners rarely have a quant team, the optimiser holds the bid history, and public benchmarks cover market averages rather than one asset.

## What a Fix Looks Like
An independent monthly calculation from the asset's own telemetry, bids and ISO settlement data: a perfect-foresight and a rolling-intrinsic benchmark on the owner's stated constraints, realised revenue against both, and a breakdown of the gap by market and by day type.

## Who Feels the Pain
Storage asset managers renewing optimiser contracts, lenders sizing debt on revenue claims, and owners comparing two optimisers across a portfolio.

## Impact If Fixed
Exposing a 5-point capture-rate gap between two optimisers (estimate) on a 200 MW battery earning ~$8M a year is worth ~$500K a year at the next contract choice.
