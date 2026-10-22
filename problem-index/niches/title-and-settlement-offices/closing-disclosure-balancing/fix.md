# The Title Premium That Never Matches

**Niche:** [[niches/title-and-settlement-offices/closing-disclosure-balancing/profile|Closing Disclosure Balancing & Settlement Statements]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Fix (Pain Point)
**One-liner:** TRID's disclosure rule for simultaneous-issue title premiums makes the CD's title figures differ from the agent's invoice, and lenders and agents recompute it differently on every purchase.
**Tags:** #compliance #evaluation-metrics #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to make the lender's Closing Disclosure and the settlement agent's statement agree to the cent in one round inside TRID's three-business-day window, and whoever eliminates the redisclosure round gets onto the lender's preferred settlement-agent list.

## The Problem
Where an owner's and a lender's policy are issued together at a discount, TRID requires the lender's policy to be disclosed at its full rate and the owner's policy as the remainder of the combined premium. The agent's invoice shows the actual split. Lenders' systems and agents' calculators often disagree on rate tiers, endorsements and state rules, and the title lines become the last items to balance.

## Why It's Still Broken
Each lender implements the calculation in its own system from a rate table it maintains, and the agent's rate manual is the source of truth nobody shares.

## What a Fix Looks Like
A shared calculation service driven by the underwriter's filed rate manual, returning both the actual and the TRID-disclosed figures for any policy combination, consumed by both the lender's and the agent's systems.

## Who Feels the Pain
Escrow officers and lender closers on every financed purchase.

## Impact If Fixed
A recurring source of last-minute CD differences disappears.
