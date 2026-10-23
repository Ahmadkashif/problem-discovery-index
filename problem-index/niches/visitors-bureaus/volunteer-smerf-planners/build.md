# Block Sizing for Groups That Have Never Met Before

**Niche:** [[niches/visitors-bureaus/volunteer-smerf-planners/profile|Volunteer & SMERF Group Planners]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A volunteer planning a reunion guesses how many rooms to block, and the bureau has years of similar groups' outcomes it never uses.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a volunteer planner's loose inquiry for a reunion, church convention or fraternal meeting into a hotel block the group can actually fill, and whoever sizes those blocks so the groups avoid attrition penalties and come back takes the account.

## The Problem
A reunion organiser expects 150 attendees and asks for 60 rooms over two nights. Forty are picked up; the hotel invoices attrition; the organiser pays out of pocket or the group never returns. Bureau staff have seen hundreds of such groups and know the pattern, but tell each organiser informally, if at all.

## Why Nobody Has Built This
SMERF is a low-revenue segment for hotels and bureaus, and outcomes are scattered across hotels' group records.

## What to Build
A block-sizing assistant in the bureau's planning service: the organiser enters group type, mailing list size, distance members travel, past attendance and dates; a model trained on the bureau's and hotels' past SMERF pickups recommends a block and a sensible attrition allowance, with a range. The recommendation goes into the lead sent to hotels.

## Target Customer
SMERF sales managers at bureaus in drive-market and reunion destinations.

## Impact If Built
Fewer groups penalised, more repeat bookings, and hotels getting blocks they can count on.
