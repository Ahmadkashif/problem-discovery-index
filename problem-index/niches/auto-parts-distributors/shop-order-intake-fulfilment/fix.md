# Shop Orders Arrive on Four Channels and Leave No Trace

**Niche:** [[niches/auto-parts-distributors/shop-order-intake-fulfilment/profile|Shop Order Intake & Hot-Shot Fulfilment]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Fix (Pain Point)
**One-liner:** A shop orders by phone at 8:05, texts a correction at 8:07 and adds a part in the e-catalog at 8:10, and the store treats them as three unrelated tickets.
**Tags:** #large-language-models #transformers #feature-engineering #workflow-orchestration #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn a shop's call, text or e-catalog order into the right part at the shop's bay, but that hides two contests with different winners: matching the request to the one part that fits that VIN, won by catalog depth and matching models and measured by fitment returns, and running the delivery, won by route density and dispatch and measured by shop orders cancelled because the part arrived after the shop's window. Decomposed into contested sub-niches below.

## The Problem
Shops use whatever channel is closest: a call, a text to the counter's mobile, an e-catalog order, a note left with the driver. Corrections and additions arrive on a different channel from the original, so the store ships the uncorrected order, sends two runs, or misses an item.

## Why It's Still Broken
Phones, messaging tools, e-catalog networks and business systems don't share a queue, and counter staff are the only integration.

## What a Fix Looks Like
One queue per shop that pulls in calls (transcribed), texts and e-catalog orders, groups messages about the same vehicle or repair order within a time window, applies corrections to the open order, and shows the counter a single ticket. The shop gets one confirmation listing what will arrive.

## Who Feels the Pain
Counter staff juggling channels; drivers sent twice; service writers whose corrections were missed.

## Impact If Fixed
If merged tickets prevented ~3 duplicate or uncorrected orders a day per store (estimate), at ~$20 per wasted run and return (estimate) that is ~$18K a year per store.
