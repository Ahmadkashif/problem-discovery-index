# The Contingency That Was a Round Number

**Niche:** [[niches/game-porting-studios/effort-model-and-pricing/profile|Effort Model & Bid Pricing]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Every bid carries the same contingency percentage regardless of the project, because somebody chose it years ago.
**Tags:** #quick-win #descriptive-statistics #confidence-intervals #revenue-impact #evaluation-metrics #probability-distributions #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to turn measured codebase properties and a history of past projects into a price with stated risk — and whoever prices it correctly takes the account.

## The Problem
Most porting studios apply a flat contingency to every bid. It is the same for a straightforward port of a well-structured codebase on a familiar engine and for a heavily modified engine targeting the hardest platform. The number came from somewhere years ago. It is simultaneously too high for the easy projects, which the studio then loses on price, and far too low for the hard ones, which it wins and loses money on.

## Why It's Still Broken
The contingency is a habit rather than a calculation — a single percentage applied to every project cannot be right for any of them, and nobody has computed what the variance actually was. Per-project risk assessment takes time in a bid process that is always rushed. Nobody tracks which bids were won and lost on price. And the losses look like execution problems.

## What a Fix Looks Like
Compute the variance you have already lived through and vary the number. Calculate the actual overrun distribution across past projects, which is the fix and immediately shows the flat number is wrong in both directions. Segment it by engine, platform and client type, since the differences are usually large enough to act on without any modelling. Set contingency bands by project profile rather than one figure, which is a lookup table and not a model. Identify the profiles where the studio consistently loses money and either price them properly or decline them, which is the commercial decision the data enables. Identify the profiles where it consistently wins, as those are being overpriced and lost on bid. Track won and lost bids against price, which nobody records and which is half the picture. Separate estimation overrun from scope change in the history, because they require different remedies. Review the bands annually rather than inheriting them. State the contingency internally as a risk position rather than hiding it in the rate. And start with three bands rather than a model, which is achievable this quarter.

## Who Feels the Pain
Studios losing easy work on price and money on hard work; commercial leads with no basis for varying a number; engineers delivering projects that were never priced to succeed; and the margin, in both directions.

## Impact If Fixed
A single percentage applied to every project cannot be right for any of them, and nobody has computed what the variance actually was. Three contingency bands from the studio's own overrun history is a lookup table that fixes both failure modes.
