# The Accrual That Ignores Week Three's Scale

**Niche:** [[niches/movie-theaters/exhibitor-film-rent-and-settlement/profile|Exhibitor Film Rent & Settlement]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Fix (Pain Point)
**One-liner:** Month-end accruals use one blended percentage per film, so profit swings when settlements land weeks later and nobody can tell a good month from a timing difference.
**Tags:** #linear-regression #evaluation-metrics #feature-engineering #quick-win #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to hold an engagement-level record of the terms the theatre actually agreed, so that accruals are right every week and each distributor's invoice is checked before it is paid, and whoever catches the most overcharges and knows each sales office's settlement habits takes the account.

## The Problem
To close the month, the film accountant applies an estimated percentage to each film's gross. Under a sliding scale the true percentage falls as the run ages, and settlements often move again after the run. The result is accruals that overstate cost on long-running films and understate it on short ones, with true-ups landing in later months.

## Why It's Still Broken
The scale for each engagement sits in an email, so a blended estimate is the only practical shortcut, and the true-up is buried in the next month's numbers.

## What a Fix Looks Like
Apply the week-of-run scale per engagement from a simple terms table, and adjust it with each distributor's historical settlement drift (how far settled rates land from scale), estimated from past settlements. Report the true-up separately each month.

## Who Feels the Pain
Controllers presenting monthly results to owners and lenders; district managers judged on theatre profit that moves for accounting reasons.

## Impact If Fixed
Monthly theatre profit becomes trustworthy within a quarter, with no new system beyond a terms table and a settlement history.
