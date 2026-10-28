# One Settlement Record Per Sale

**Niche:** [[niches/wholesale-auto-auctions/title-and-payment-settlement/profile|Title & Payment Settlement]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Title status, buyer payment and seller payout sit in three systems, so nobody sees in one place which sold cars are still exposed.
**Tags:** #workflow-orchestration #data-integration #survival-analysis #gradient-boosting #automation #compliance
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to close each sale into a negotiable title and cleared funds. But titles are won by whoever controls the paper chain through sellers, lienholders and state title offices, against the auction's title window. Funds are won by whoever carries the buyer's credit, against the floorplan lender's payoff terms. Different players win on different clocks, so the niche is decomposed into contested sub-niches below.

## The Problem
For every sale the auction must know three things: has the title arrived and is it negotiable, has the buyer's payment cleared or the floorplan funded, and has the seller been paid. Each lives in a different module, often with a different team. Exceptions such as title absent, payment returned or payout made early surface only when someone runs a report or a buyer complains.

## Why Nobody Has Built This
Auction systems grew by bolting modules on, and floorplan lenders run their own platforms. The two sub-contests have different owners: titles sit with the title department, funds with the cashier and the lender relationship.

## What to Build
A settlement ledger keyed by sale. It pulls title events, payment and floorplan events and payout events into one record. Each sale gets a state (clean, title-exposed, funds-exposed, both) and an age. The gate pass and the seller payout are held automatically when exposure crosses a threshold the controller sets. Survival models on title and funds events rank the open items. The sub-niches own the detail: [[niches/wholesale-auto-auctions/title-absent-sales/profile|Title-Absent & Title-Defect Sales]] and [[niches/wholesale-auto-auctions/floorplan-funds-settlement/profile|Floorplan & Funds Settlement]].

## Target Customer
Controllers and operations VPs at auction chains and large independents.

## Impact If Built
Seeing every exposed sale in one queue could cut settlement losses (write-offs plus title unwinds) by a quarter. At an auction losing ~0.05% of gross sales value, ~$250,000 a year on $500M of sales, that saves ~$60,000 a year, before staff time (estimates).
