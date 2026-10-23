# Batch Feasibility for a Lot Full of Keyless VINs

**Niche:** [[niches/locksmiths/dealer-auction-repo-keys/profile|Dealer, Auction & Repossession Key Work]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An auction emails a list of 80 keyless VINs due on the lane next week, and the locksmith prices the batch by guesswork, because nobody knows which of the 80 are a ten-minute add-key and which need a module out on the bench.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #optimization-fundamentals #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put a working key in every keyless unit on a dealer lot, auction lane or repossession yard before it sells, and whoever turns around the most VINs per visit at a fixed per-unit price takes the account.

## The Problem
Batch work is priced per unit, but difficulty varies enormously. An older transponder key takes minutes; an all-keys-lost smart key on a recent European car may take hours or need a dealer. A flat price loses money on the hard units, and pricing each by hand delays the quote past the sale date.

## Why Nobody Has Built This
Feasibility knowledge is scattered across tool vendors and individual locksmiths. Dealers and auctions see keys as a reconditioning line item, not a dataset, and no locksmith has had the volume to model it.

## What to Build
A batch planner that takes a VIN list and returns, per unit, the decoded vehicle, key part, likely procedure, expected minutes, probability of on-site success and parts cost. It then produces a tiered per-unit price, an optimised visit plan (order of units, parts to bring, units to send to the dealer) and a completion forecast against the sale date. It runs on the same outcome logs as the retail feasibility service in [[niches/locksmiths/automotive-key-programming/build|Feasibility and Price Before the Van Leaves]], weighted to batch conditions.

## Target Customer
Automotive locksmiths with dealer, auction and repossession contracts, including work for [[industries/repossession-services|repossession agencies]]; reconditioning managers who want a firm quote and date.

## Impact If Built
Quotes in hours instead of days, prices that cover the hard units, and more vehicles crossing the block with working keys.
