# Walkthrough-to-Workload Forecast

**Niche:** [[niches/auctioneers/whole-house-estate-contents/profile|Whole-House Estate Contents]]
**Industry:** [[industries/auctioneers|Auctioneers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Estate firms quote and schedule a house on a guess of how many lots and crew-days it holds, and the guess decides whether they make money on it.
**Tags:** #cnns #object-detection #gradient-boosting #linear-regression #evaluation-metrics #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to clear a whole house by the executor's closing date while netting more than an estate-sale company or a cleanout would, and whoever can lot, photograph and close a full house in the fewest crew-days without leaving value in the box lots takes the account.

## The Problem
Two houses of the same size can differ threefold in work: one tidy, one with a full basement, attic and garage. The auctioneer estimates lots and crew-days from the walkthrough, commits to a sale date ahead of the closing, and finds out halfway through set-up whether the house will fit. Overruns mean overtime, a rushed catalogue, or a missed closing.

## Why Nobody Has Built This
Firms rarely record crew-hours per house against what the house contained, so there is nothing to learn from, and walkthrough video is not captured systematically.

## What to Build
From a walkthrough video and the firm's history of houses, estimate the lot count, the share of box lots, photography hours, crew-days and expected gross, with ranges. Feed the estimate into scheduling and the proposal, then record actuals after each sale to retrain.

## Target Customer
Estate auction firms running several houses at once in peak season.

## Impact If Built
Quotes that cover cost, sale dates that hold, and fewer rushed catalogues, worth crew-days per house in avoided overruns (estimate).
