# Retention Spend Nobody Can Measure

**Niche:** [[niches/wired-broadband-providers/residential-retention-and-migration/profile|Residential Retention & Migration]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Operators count saves, not the customers who would have stayed anyway, so nobody knows how much retention spending actually retains.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to keep a household's broadband revenue when its current connection stops being its best option, but for cable operators that is a pricing contest at promo roll-off against fixed wireless and fibre, and for telcos it is an operational contest to move households off copper before the wire center is retired. Decomposed into contested sub-niches below.

## The Problem
A save desk reports a save rate of, say, ~60% (an illustrative figure, not a measured benchmark). Some of those households were bluffing, some would have stayed at the full price, and some left three months later anyway. The same blind spot applies to migration incentives: credits offered to move copper customers to fibre are counted as conversions whether or not they changed anything.

## Why It's Still Broken
Running a holdout means deliberately not offering a discount to some customers, which save-desk managers resist because it lowers their reported save rate. Nobody owns incrementality as a metric.

## What a Fix Looks Like
A small, standing randomised holdout for each offer type and each migration incentive, with results reported as incremental retained revenue per dollar spent, at 90 and 180 days. Agents' scorecards move from saves to incremental saves.

## Who Feels the Pain
CFOs approving retention budgets; retention leaders defending them; customers who never got an offer because the budget went to people who didn't need one.

## Impact If Fixed
A low-cost change in measurement exposes which offers work, which is worth more than any model built on the current, biased save data.
