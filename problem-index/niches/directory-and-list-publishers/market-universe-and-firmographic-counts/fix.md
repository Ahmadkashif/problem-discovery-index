# Size Bands That Move Accounts Between Territories

**Niche:** [[niches/directory-and-list-publishers/market-universe-and-firmographic-counts/profile|Market Universe & Firmographic Counts]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** A compiler re-models employee counts, thousands of accounts change band overnight, and a customer's territories and quotas shift with no change in the real world.
**Tags:** #gradient-boosting #confidence-intervals #evaluation-metrics #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to give a revenue team the complete, de-duplicated and correctly sized universe of accounts in its market, and whoever's count survives the customer's own match test — no dead, duplicate or mis-banded firms — becomes the system of record for targeting and territories.

## The Problem
Territories are often cut by employee band — reps own "50–199 employees" in a region. When the compiler retrains its size model or swaps a source, accounts move across bands in the next enrichment run. Reps lose accounts they were working, quota maths breaks mid-year, and the revenue operations team spends weeks unpicking it.

## Why It's Still Broken
Modelled sizes are delivered as point values without intervals or version tags, so the customer cannot tell a real change from a model change.

## What a Fix Looks Like
Version every modelled field, ship a band probability alongside the band, flag records whose band changed because of a model update rather than new evidence, and let customers freeze bands for the planning year.

## Who Feels the Pain
Revenue operations leaders, sales managers re-cutting territories, and reps who lose accounts mid-cycle.

## Impact If Fixed
Territories stop moving under reps' feet, and model improvements stop costing renewals.
