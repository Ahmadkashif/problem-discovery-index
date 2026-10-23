# Scaling Recommendations Graded Against Resale

**Niche:** [[niches/ticketing-agencies/concert-tour-onsales/profile|Concert Tour Onsales & Allocation]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A tour is scaled city by city on a ticketing director's memory, and the resale market grades each call within hours without anyone writing the grade down.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #bayesian-inference #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to put a tour's tickets into fans' hands at the price the artist chose, against bots and broker account farms, and whoever lets the smallest share of the house reach resale in the first 48 hours takes the account.

## The Problem
For a 40-date arena tour, the promoter's ticketing lead scales each building: price levels by section, holds by purpose, the presale sequence and what to keep back for the general onsale. The calls come from memory of past tours in each market. After the onsale, resale listings show which sections were underpriced and how many seats brokers got, but the scaling decision is not recorded in a form that can be compared with that outcome, so the next tour repeats the same misses.

## Why Nobody Has Built This
Primary ticketers hold the sales data but sell as agent and have their own resale businesses, so a tool that measures leakage to resale is awkward for them. Promoters have the decision but rarely the data team. The label is messy: resale prices move with fee rules and state caps.

## What to Build
A per-tour decision ledger that captures each city's scaling and hold plan from the setup files. It grades each city against section-level sell-through and the share and price of seats relisted in the first 48 hours, and fits time-to-sale and resale-premium models that propose next tour's scaling within the artist's price ceiling. The first product is the leakage report; the recommendations come later.

## Target Customer
Heads of ticketing at promoters (Live Nation, AEG Presents and independents) and the managers of touring artists who own the price decision.

## Impact If Built
A tour can show its artist how many tickets reached fans at face, and each successive tour can be scaled on graded evidence rather than memory.
