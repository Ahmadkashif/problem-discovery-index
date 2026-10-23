# The Wire Order Released on a Six-Week-Old Quote

**Niche:** [[niches/electrical-distributors/wire-cable-copper-pricing/profile|Wire & Cable Pricing Against COMEX Copper]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** A contractor releases the job's feeder cable against a quote from before copper jumped, and the branch ships it at a loss because nobody checked.
**Tags:** #time-series-forecasting #feature-engineering #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to price every wire and cable quote and order to the day's copper with hold terms the contractor accepts, and whoever keeps wire margin flat through a copper swing without losing the bid takes the account.

## The Problem
Project wire is quoted once and released in pieces over months. Releases are entered against the original quote price, and the margin is only seen at month end.

## Why It's Still Broken
Quote prices carry no expiry in many ERPs, and the people entering releases don't own wire pricing.

## What a Fix Looks Like
Every wire release checked against current replacement cost and the quote's hold term at order entry, with an automatic reprice or a manager approval when margin falls below floor, and a note to the contractor citing the agreed terms.

## Who Feels the Pain
Branch managers, wire product managers and controllers explaining margin variances.

## Impact If Fixed
Losses on stale wire quotes are stopped at the order screen. If ~5–10% of project wire releases ship on stale prices in a rising copper month (estimate), the check saves several margin points on those lines.
