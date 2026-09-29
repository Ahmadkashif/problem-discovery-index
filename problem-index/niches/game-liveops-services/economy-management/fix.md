# Nobody Can Say How Much Currency Exists

**Niche:** [[niches/game-liveops-services/economy-management/profile|Economy Management]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Fix (Pain Point)
**One-liner:** Ask a live team the total currency held by its players and the honest answer is that nobody has ever computed it.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #time-series-forecasting #confidence-intervals #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep a currency economy with millions of participants in balance when it is tuned by hand and the drift that ruins it compounds invisibly for a quarter — and whoever makes the economy legible takes the account.

## The Problem
The most basic economic figure — how much currency is held across the player base, and whether it is rising — is not on any dashboard in most live games. Neither is the inflow and outflow per system, nor the distribution across players. The data is in the inventory tables. Nobody queries it as a standing report, so the first evidence of inflation is a designer noticing that rewards feel meaningless.

## Why It's Still Broken
The dashboards were built to report revenue and engagement — a reporting stack assembled to answer commercial questions will never accidentally answer economic ones, and nobody noticed the omission because the omission is invisible. Currency lives in operational tables rather than in the analytics warehouse. No role owns economic health. And there is no incident until there is a crisis.

## What a Fix Looks Like
Compute the aggregates and put them on the wall. Report total and per-capita currency stock daily, which is the fix and is a query against tables the game already writes. Report inflow and outflow by source and sink, since knowing which faucet is oversized is most of the diagnosis. Show the distribution across the population, as a hoarding tail and an empty majority both hide inside the mean. Track the same figures for premium currency and major items, which are separate economies inside the same game. Chart it over months rather than days, because the pattern only appears at that scale. Set an expected corridor and alert on departure from it rather than on a fixed level. Break it out by cohort age, since veterans and new players experience different economies. Join parameter change dates onto the chart, which makes the cause obvious in most cases. Give the economy designer access directly rather than through an analyst request. And review it on a fixed cadence, so the drift is caught in weeks rather than in quarters.

## Who Feels the Pain
Designers whose rewards stopped meaning anything; teams discovering an inflated economy a quarter late; players whose progression flattened; and the revenue that erodes as purchases lose value.

## Impact If Fixed
A reporting stack assembled to answer commercial questions will never accidentally answer economic ones, and nobody noticed the omission because the omission is invisible. A daily currency stock query against existing tables is the whole first step.
