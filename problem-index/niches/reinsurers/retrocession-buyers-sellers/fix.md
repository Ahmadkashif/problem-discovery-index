# Retro Bought on Last Year's Portfolio

**Niche:** [[niches/reinsurers/retrocession-buyers-sellers/profile|Retrocession Buyers & Sellers]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Fix (Pain Point)
**One-liner:** Retro cover for 1 January is bound before the inwards renewals finish, so the protection is sized on a portfolio that no longer exists.
**Tags:** #monte-carlo-methods #time-series-forecasting #evaluation-metrics #workflow-orchestration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to present a reinsurer's whole treaty portfolio as one loss distribution that a retrocession writer can price without seeing the underlying cedents, and whoever's roll-up the retro panel accepts with the fewest data requests takes the account.

## The Problem
The buyer projects its 1 January book from the expiring portfolio and the renewal plan, binds retro, then writes a portfolio that differs: lines won, lost or resized, new cedents added. The mismatch is discovered when the capital team re-runs the book in January.

## Why It's Still Broken
Inwards and outwards teams work to the same date with different information, and no tool updates the projected portfolio as firm orders arrive.

## What a Fix Looks Like
A live projection of the inwards portfolio that updates with each firm order, recomputes the retro need and flags when the bound protection falls short of the plan.

## Who Feels the Pain
Retro buyers; chief risk officers whose tail exposure exceeds appetite in January; capital teams re-running models over the holidays.

## Impact If Fixed
Retro sized to the book actually written, with gaps found while capacity is still available.
