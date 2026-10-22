# One Lien Ledger From Payoff Request to Recorded Release

**Niche:** [[niches/title-and-settlement-offices/payoffs-releases-trailing-docs/profile|Payoffs, Lien Releases & Trailing Documents]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The payoff and the release of the same mortgage are tracked by different people in different places, months apart, so nobody sees the lien's whole life.
**Tags:** #survival-analysis #large-language-models #feature-engineering #workflow-orchestration #automation #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to make sure every existing lien is paid and then released of record — but before closing the contest is getting an accurate, good-through payoff statement from the lienholder in time to balance the Closing Disclosure, and after closing it is proving months later that the release was recorded and the final policy issued. Different counterparties, clocks and vendors win each half. Decomposed into contested sub-niches below.

## The Problem
The escrow team requests the payoff and wires the funds; the post-closer chases the release weeks or months later. The link between them — which wire paid which loan, which servicer now holds it, what the statute requires — is reconstructed each time from the file.

## Why Nobody Has Built This
Production systems are organised by file, not by lien, and the two halves fall to different staff with different tools. The two halves really are different contests, which is why this niche is decomposed below; the ledger is the shared spine both need.

## What to Build
A lien-level record created when the search finds the instrument: lienholder and servicer history, payoff requests and statements, the disbursement that paid it, the release due date under the state statute, county recording checks, and closure when the satisfaction is indexed. Servicer-level cycle-time baselines drive escalation in both halves.

## Target Customer
Agencies with separate escrow and post-closing teams and recurring audit findings on open releases.

## Impact If Built
Every paid lien has a visible path to release, and both teams work from the same record.
