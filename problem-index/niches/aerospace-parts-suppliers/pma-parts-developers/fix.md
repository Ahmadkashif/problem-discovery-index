# Picking the Next PMA From a Spreadsheet

**Niche:** [[niches/aerospace-parts-suppliers/pma-parts-developers/profile|PMA Parts Developers & Reverse-Engineering Teams]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** Which part to reverse engineer next is the biggest decision a PMA team makes, and it is made from a spreadsheet of customer requests and remembered OEM prices.
**Tags:** #gradient-boosting #feature-engineering #descriptive-statistics #revenue-impact #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get a high-demand part through FAA Parts Manufacturer Approval before the OEM's aftermarket price moves, and whoever turns a teardown into an accepted test-and-computation package in the fewest months takes the account.

## The Problem
A PMA programme costs engineering months and test money. The payoff depends on fleet size, replacement rate, OEM list price and its trend, competing PMAs and customer willingness to install. Teams rank candidates from airline requests and sales intuition, with demand and price data scattered across quotes, catalogues and the sales team's memory.

## Why It's Still Broken
The data sits in different places (fleet data, quotes, catalogues, sales notes), and the decision is made once a quarter by people with no time to assemble it.

## What a Fix Looks Like
A single ranked list of candidates scored on fleet exposure, observed demand from quotes and requests, OEM price history, existing PMA competition and estimated development cost, refreshed monthly and reviewed at the quarterly portfolio meeting.

## Who Feels the Pain
Engineering leaders who spend a year on the wrong part; sales teams who cannot answer customers' requests; finance, which funds the programme.

## Impact If Fixed
Choosing one better part a year out of ~10–20 programmes (estimate) can shift several million dollars of lifetime revenue toward parts that pay back.
