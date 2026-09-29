# Buyer Open-to-Buy Spreadsheet

**Industry:** [[retail-pos-platforms|Retail POS Platforms]]
**Type:** Worker Life Changing
**One-liner:** The buyer stops rebuilding the same fragile spreadsheet every season to work out what they can afford to order, because the platform holds every number in it and can maintain it continuously.
**Tags:** #time-series-forecasting #gradient-boosting #linear-regression #optimization-fundamentals #confidence-intervals #evaluation-metrics #worker-facing #revenue-impact

## The Problem
Open-to-buy is the discipline of planning purchases against a budget: given planned sales, planned markdowns, existing inventory and target closing stock, how much can be spent on new goods in each category in each month. It is the central planning tool of retail merchandising and it has been for a century.

At an independent retailer it is a spreadsheet. Usually built by the owner or a single buyer, usually inherited from a previous version, usually containing errors nobody has found. It is rebuilt or patched each season, populated by exporting numbers from the POS and typing them in, and it goes stale within weeks of the season starting because nobody wants to redo the export.

The consequence is that buying decisions — placed months ahead, at trade shows, under vendor pressure, with minimum order quantities and early-order discounts — are made against a plan that was approximately right in August and is unrecognisable by October. Retailers over-buy into slow categories and run out of the ones that are working, and discover both too late to do anything.

## Why It Matters to the Worker
The buyer at an independent retailer is usually also the owner, the manager, or the only merchandiser, and the open-to-buy work happens on top of running the store. It is done in evenings, in spreadsheets, with real anxiety attached, because the numbers determine whether the business has cash in six months.

The spreadsheet is also a private, fragile artefact. If the person who built it leaves, nobody else can operate it. If it contains an error, it may go undetected for a season. Buyers know this and it contributes to a persistent low-level worry about a plan they cannot fully verify.

And the work is not judgement. The judgement is choosing the goods, which is the part buyers enjoy and are good at. The arithmetic around it — projecting sales, reconciling receipts, tracking commitments against budget — is bookkeeping performed by someone whose skill is taste.

## What a Solution Looks Like
Open-to-buy maintained as a live view rather than rebuilt as a document. Every input is already in the platform: sales by category, current inventory at cost, on-order commitments, receipts, markdowns taken. The plan should update itself daily and show remaining budget by category and month without anyone exporting anything.

Planned sales should come from a forecast rather than from last year plus a percentage, and should carry a range so the buyer can see how much room the plan actually has.

Commitments matter as much as spend. Orders placed months ahead against future months' budgets are the thing buyers most often lose track of, and tracking them against the plan is the single most useful function such a tool performs.

And it should warn: this category is tracking behind and you have three deliveries still to come.

## Impact If Solved
Buying decisions commit an independent retailer's working capital months ahead, and they are made against a plan that is stale by construction. Making open-to-buy live turns the sector's core planning discipline from an evening spreadsheet exercise into a continuous view, and returns the buyer's attention to choosing the goods.
