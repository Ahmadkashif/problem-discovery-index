# The Debit Memo Dispute Nobody Has Time to File

**Niche:** [[niches/travel-agencies/ticketing-exchanges-settlement/profile|Air Ticketing, Exchanges & ARC Settlement]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Agencies pay many debit memos they could win because assembling the evidence takes longer than the memo seems worth.
**Tags:** #large-language-models #bert #evaluation-metrics #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to process exchanges, refunds and voids without manual rework, and whoever generates the fewest agency debit memos per thousand tickets takes the account.

## The Problem
A memo arrives citing a fare-rule violation on an exchange made weeks earlier. Disputing it means pulling the ticket history, fare rules in force at the time, any waiver code the airline issued during a disruption, and the agent's notes, then writing the dispute inside the airline's window. Memos of ~$25-75 in fees plus fare difference (estimate) are often just paid.

## Why It's Still Broken
The evidence is scattered across the GDS, the airline's waiver notices and email, and nobody tracks which airlines' memos are most often reversed on dispute.

## What a Fix Looks Like
For every incoming memo, automatically assemble the ticket history, archived fare rules and applicable waivers, classify whether a dispute is likely to succeed, draft it, and file within the window; report reversal rates by airline and reason so the agency knows where disputes pay.

## Who Feels the Pain
Ticketing managers and accounting staff; agents whose names are on memos for exchanges done under a waiver.

## Impact If Fixed
Winnable memos are disputed as a matter of routine, and the agency recovers money it now writes off.
