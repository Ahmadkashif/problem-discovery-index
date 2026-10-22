# The Package Priced as a Lump Sum

**Niche:** [[niches/film-distributors/library-licence-pricing/profile|Library Licence Pricing]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** Library packages are sold for one total fee, so the seller never learns which titles the buyer was really paying for, and producers' shares are allocated by formula rather than value.
**Tags:** #feature-engineering #linear-regression #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to price a library title or package for a specific buyer, territory and window close to what that buyer will actually pay, and whoever knows the clearing price best closes the deal without leaving money on the table.

## The Problem
A buyer pays one fee for twenty titles. Internally the distributor splits it equally or by a rule of thumb to compute each producer's share, which invites disputes and hides which titles drove the deal.

## Why It's Still Broken
Allocation is done at quarter end in a spreadsheet, and no per-title value estimate exists to allocate against.

## What a Fix Looks Like
Allocate each package fee across titles using per-title demand signals and the firm's past single-title prices. Keep the allocation basis on file for producers and auditors, and feed the implied per-title values back into future pricing.

## Who Feels the Pain
Royalty accountants defending allocations; producers of strong titles diluted by weak ones; salespeople pricing the next package blind.

## Impact If Fixed
Defensible allocations, fewer producer disputes, and a growing record of what individual titles are worth inside packages.
