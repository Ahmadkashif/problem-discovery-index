# A Delivery-Risk Score on Every Listing

**Niche:** [[niches/ticketing-agencies/secondary-resale-marketplaces/profile|Secondary Resale Marketplaces]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A marketplace learns that a seat will not be delivered when the buyer is standing at the gate, though the seller's history and the venue's transfer rules predicted it days earlier.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to guarantee that every listed seat is real, deliverable and lawfully priced in the venue's state, and whoever settles the fewest failed orders, speculative-listing complaints and chargebacks per thousand tickets takes the account.

## The Problem
A failed order costs the marketplace a replacement seat bought at the current market price, a refund, a support contact, often a chargeback, and a buyer who does not come back. The failures are concentrated: certain sellers, certain venues with late transfer windows, sold-out shows where sellers listed seats they hoped to buy. Marketplaces handle them reactively, with penalty schedules applied after the fact.

## Why Nobody Has Built This
Seller scorecards exist but are coarse, based on aggregate fill rates. The signals that matter, such as whether the seller holds the seat in a transferable account, the venue's transfer release date and the seller's behaviour in tight markets, are spread across systems, and marketplaces compete for the same large sellers, so none wants to be the strict one alone.

## What to Build
A per-listing model, scored at listing and refreshed daily, estimating the probability of non-delivery or late delivery from seller history, proof of possession, venue transfer rules, event demand and days to show. It drives listing rank, payout timing, collateral holds and proactive replacement before the buyer notices.

## Target Customer
Heads of trust and safety and of fulfilment operations at resale marketplaces.

## Impact If Built
Fewer failed orders and gate-side disputes, lower replacement costs, and buyers who trust the guarantee enough to return.
