# The Escalator Applied From the Wrong Date

**Niche:** [[niches/land-developers/lot-takedown-contract-administration/profile|Lot Takedown & Option Contract Administration]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Fix (Pain Point)
**One-liner:** A quarterly lot-price escalator starts from the phase delivery date in one contract and the contract date in another, and the spreadsheet uses the same start for both.
**Tags:** #large-language-models #evaluation-metrics #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to close every scheduled takedown on its date with the right lots, escalated price and deposit credit, and whoever posts the fewest takedown closings needing correction takes the account.

## The Problem
Escalators compound per period from a defined start, and contracts define the start differently. Applying the wrong one misprices every takedown on that contract, in either direction.

## Why It's Still Broken
The escalator clause is read once at signing and turned into a spreadsheet formula by whoever builds the tracker. Nobody re-reads it at each closing.

## What a Fix Looks Like
Extract the escalator's start, rate and compounding from the clause, store them with the contract, and compute each takedown's price from them with the clause quoted on the closing statement.

## Who Feels the Pain
Developer and land-banker finance teams, and the builders who dispute the invoice.

## Impact If Fixed
Pricing every takedown from the clause itself ends a recurring source of disputes and silent margin leakage. One quarter's misapplication of a 1% quarterly escalator misprices each lot by ~$1,100 at $108,400, ~$110K across a 100-lot phase (estimate).
