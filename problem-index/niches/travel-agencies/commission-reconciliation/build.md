# An Expected-Commission Ledger That Knows Who Won't Pay

**Niche:** [[niches/travel-agencies/commission-reconciliation/profile|Supplier Commission Reconciliation]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Back offices chase unpaid commissions on a fixed age rule, when supplier payment behaviour is predictable enough to chase the right claims weeks earlier.
**Tags:** #survival-analysis #gradient-boosting #k-nearest-neighbors #large-language-models #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to match every expected commission to a payment and chase the rest before the supplier stops answering, and whoever recovers the highest share of earned commission takes the account.

## The Problem
A host's commission team works its open items by age: everything unpaid at ~60 or ~90 days (estimate) gets a claim. Some chains reliably pay through the clearing house within weeks; some independent properties never pay without a call; some underpay by excluding resort fees. Treating them alike wastes time on claims that would have paid and starts too late on those that won't.

## Why Nobody Has Built This
Back-office systems record expected and received amounts but do not model time to payment, and the history needed — years of payments by supplier — is fragmented across hosts.

## What to Build
A ledger that computes expected commission per booking from booking and change history and supplier terms, matches incoming payments with learned similarity on names, dates and amounts, and runs survival models of time to payment by supplier, chain, channel and amount. Claims are generated when a booking's probability of payment drops below a threshold, through the route most likely to work for that supplier.

## Target Customer
Commission and finance teams at host agencies and consortia; multi-advisor agencies with material hotel volume.

## Impact If Built
More commission recovered per chase hour, earlier action on the suppliers that won't pay, and less sent to contingency firms at a 50% fee.
