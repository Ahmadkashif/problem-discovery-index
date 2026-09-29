# Slower and Less Certain Than a Phone Call

**Niche:** [[niches/b2b-commerce-platforms/reorder-and-account-purchasing/profile|Reorder & Account Purchasing]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A buyer reordering eleven familiar items can do it in ninety seconds by phoning a rep who knows their account, and the storefront takes longer and leaves them less certain it is right.
**Tags:** #time-series-forecasting #gradient-boosting #workflow-orchestration #evaluation-metrics #worker-facing #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to make a repeat order faster and more certain than phoning the rep — and whoever does that takes the volume, because the buyer knows what they want and is choosing between channels rather than between products.

## The Problem
A maintenance buyer needs their monthly order. On the phone, the rep pulls up the account, reads back the usual list, notes that one item is now superseded and offers the replacement, confirms stock and a delivery date, and it is done. On the storefront the buyer scrolls order history, adds items individually, discovers one is unavailable with no alternative offered, cannot see a delivery date until checkout, and triggers an approval that sends an email to a manager who will action it tomorrow. The storefront is worse at the thing this buyer needs on every dimension, and the supplier funds both channels.

## Why Nobody Has Built This
The reorder experience is a list of past orders with an add button, which is what a consumer platform provides and which nobody redesigned for a buyer whose entire relationship is repetition. The rep's advantages — knowing the account, spotting supersessions, confirming availability, handling the exception — are knowledge and judgement that the platform has the data to replicate and has not. Approval workflow was added as a feature rather than designed as the normal path. And the order arrives through the rep either way, so the failure does not appear in revenue.

## What to Build
Beat the phone call on the dimensions the buyer cares about. Predict the reorder rather than waiting for it: from the buyer's own purchase history, propose the list with quantities before they ask, which is a well-posed prediction on highly regular data and is the single change that makes the storefront faster than the rep. Confirm availability and a delivery date on the proposal, since certainty is what the phone call provides and its absence is why buyers call. Surface supersessions, discontinuations and alternatives proactively, which the rep does from memory and the platform can do from data. Make approval a first-class flow with the approver notified in a channel they use and able to approve without logging in, since approval friction is the most common reason an order leaves the storefront. Support the buyer's own part numbers, cost centres and requisition references throughout. Allow bulk entry — paste, upload, grid — because these buyers work in lists and the platform makes them work in pages. Schedule recurring orders where the pattern is stable, which removes the transaction entirely and is the strongest form of the win. And measure channel share for reorder volume, since that number tells the supplier whether their storefront is earning its keep and is rarely reported.

## Target Customer
Distributors and manufacturers, their account buyers, and the reps whose time is spent on orders a good storefront would take.

## Impact If Built
The rep wins on speed and certainty and the platform has the data to beat both. A predicted reorder list with confirmed availability and dates is the change that makes the storefront faster than the phone call, and approval friction is the most common reason the order leaves anyway.
