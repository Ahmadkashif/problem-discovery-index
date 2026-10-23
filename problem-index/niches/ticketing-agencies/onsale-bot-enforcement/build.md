# An Account-Cluster Graph From Purchase to Resale

**Niche:** [[niches/ticketing-agencies/onsale-bot-enforcement/profile|Onsale Bot & Purchase-Limit Enforcement]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The proof that many buyer accounts are one broker appears days after the onsale, when their tickets show up on resale under one seller, and nothing joins the two.
**Tags:** #graph-neural-networks #dbscan #graph-theory #gradient-boosting #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to stop one buyer from holding many accounts at an onsale without blocking real fans, and whoever catches the most limit-breaking account clusters at a false-block rate the artist will tolerate takes the account.

## The Problem
At the onsale, a farm of accounts each buys within the limit. Bot management sees ordinary browsers. Days later, hundreds of those tickets are transferred to a few accounts and listed on resale marketplaces. The ticketer's trust team may notice and cancel some orders, but by then the fans who lost out have gone.

## Why Nobody Has Built This
Onsale telemetry sits with the primary ticketer, transfers in its ticket system, and listings on marketplaces it competes with. Bot vendors see traffic, not tickets. And until the 2025 enforcement wave, a ticketer that also earns resale fees had mixed incentives.

## What to Build
A graph of accounts, devices, payment tokens, addresses, phones, transfer recipients and resale seller identities, updated through each onsale and the days after it. Community detection finds clusters; a classifier trained on review outcomes scores each as one controller or independent fans. Each flagged cluster gets an evidence file showing tickets bought, transferred and listed, ready for order cancellation and, when needed, a regulator.

## Target Customer
Fan-protection and trust-and-safety heads at primary ticketers, and promoters who want an independent measure for their tours.

## Impact If Built
Limits enforced on people rather than accounts, and enforcement records that stand up to the FTC and state attorneys general.
