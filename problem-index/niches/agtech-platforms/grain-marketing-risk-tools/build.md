# The Grower's Whole Position in One Place

**Niche:** [[niches/agtech-platforms/grain-marketing-risk-tools/profile|Grain Marketing & Risk Tools]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A grower's marketing position is spread across three elevators, several contract types and a futures account, and the only place it exists as a whole is in their head.
**Tags:** #monte-carlo-methods #time-series-forecasting #confidence-intervals #evaluation-metrics #probability-distributions #data-integration #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in grower-side grain marketing is fighting to show a grower their own position — bushels priced, basis exposure, storage and interest cost, against production risk — in one place, and whoever makes the grower's position legible takes the account.

## The Problem
In August a grower has forward contracted a portion of expected corn production at one elevator, entered hedge-to-arrive contracts at another leaving basis open, holds a small futures position, and expects to sell the remainder at harvest. Asked what percentage of their crop is priced and what their remaining exposure is, they estimate. Then a dry September cuts yield by a fifth and the contracted bushels become an obligation against production they do not have, which is the specific scenario that has ruined operations and which was fully computable in August.

## Why Nobody Has Built This
Position aggregation requires ingesting contracts from multiple elevators, each with its own portal or paper, plus broker statements — a data acquisition problem across counterparties who have no reason to help, which is the same structural obstacle that appears in dock scheduling and in agency remarketing. Elevator portals show that elevator's contracts because that is what serves the elevator. And the grower-facing tools that exist have mostly been advisory services selling opinions about price direction, which is a different and easier product than an accounting of the grower's own position.

## What to Build
A position aggregator and risk view on the grower's side. Contracts are ingested from wherever they live — elevator portals, emailed confirmations, paper scanned, broker statements — and normalised into an exposure model: bushels committed, price fixed or open, basis fixed or open, delivery period, and the obligations each carries. Expected production is modelled as a distribution rather than a number, from the operation's own yield history and the current season's conditions, which is what makes the risk view meaningful. The output is the two figures a grower cannot currently state — percentage priced and remaining exposure — plus the scenario that matters: what happens to obligations and income under a yield shortfall, with the probability attached. No price forecasting is involved, deliberately; the product's value is in making the grower's own position legible rather than in opinions about the market, and being explicit about that distinction is what should make it trustworthy.

## Target Customer
Growers marketing their own production at any scale, farm management platform vendors, and the lenders financing these operations, whose own credit assessment depends on exactly this exposure.

## Impact If Built
Knowing what proportion of production is priced and what a yield shortfall does to obligations is the minimum basis for any marketing decision, and most growers operate without it. The over-contracting scenario in a short year is a well-known route to serious financial trouble and is entirely foreseeable from information the grower already has, scattered.
