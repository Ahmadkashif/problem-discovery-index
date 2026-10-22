# Loss Runs Sent to Reinsurers With No Allegation Coding

**Niche:** [[niches/self-insured-benefit-pools/public-entity-liability-pools/profile|Public Entity Liability Pools]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Fix (Pain Point)
**One-liner:** At every renewal the reinsurer asks what is driving police losses, and the pool answers with a PDF loss run coded only "law enforcement liability".
**Tags:** #large-language-models #transformers #feature-engineering #data-integration #quick-win #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep a public entity's liability programme affordable through the police-verdict cycle, but that is two contests with different winners: closing police and civil rights claims at the lowest ultimate cost, which claims managers and defence panels win, and pricing each member close enough to its own risk that low-loss members stay, which underwriters and actuaries win. Decomposed into contested sub-niches below.

## The Problem
Reinsurers price a pool's liability excess from its loss history. The loss run lists claimant, date, line, paid and reserved, with no field for excessive force versus false arrest versus jail death versus employment. Underwriters then assume the worst and price accordingly.

## Why It's Still Broken
Claim systems were configured by line of coverage years ago, and recoding history means reading thousands of files. Nobody inside a small pool has the time, and the broker sees only what the pool sends.

## What a Fix Looks Like
Recode open and closed liability claims from their notes and complaints into a short allegation and evidence taxonomy with LLM extraction and adjuster confirmation, then add the fields to the pool's system so new claims are coded at intake. Produce the renewal loss summary by allegation type, with trends.

## Who Feels the Pain
Pool underwriting and finance directors at renewal; members paying reinsurance loads built on worst-case assumptions; brokers trying to argue for better terms with nothing to show.

## Impact If Fixed
A coded loss history is a negotiating asset at the next renewal and the foundation for every model the pool wants later.
