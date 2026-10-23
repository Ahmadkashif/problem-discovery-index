# Experience Marketplace Channel Operations

**Parent Industry:** [[industries/tour-operators|Tour Operators]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to keep one live inventory of seats, prices and cancellation terms across the booking system and every marketplace, and whoever sells the last seat without an overbooking, a stale price or a mismatched refund takes the account.

## Profile
**Market Size:** ~$300M of reservation and channel-connectivity software and staff time spent operating marketplace distribution (estimate); commissions paid to the marketplaces are several times larger
**Share of Parent Industry:** ~3% of the ~$9.0B employer receipts (estimate)
**Digital Adoption:** High. The whole flow is API-driven, and the failures are in mapping and reconciliation
**Target Buyer:** Head of distribution at a multi-product operator, or the owner of a day-tour and short-break operator
**Automation Potential:** Very high

## What Makes This a Distinct Niche
Tours and activities now sell heavily through experience marketplaces. Tripadvisor's Viator reported ~$4.7B of gross bookings in 2025, and GetYourGuide, Klook, Expedia and Airbnb sell the same products. Each marketplace has its own product model, its own option and pricing structure, its own cancellation-policy format and its own payout timing. The operator's reservation system (FareHarbor, Peek, Rezdy, Checkfront, Bókun, Ventrata, Xola) must keep availability and prices in step everywhere. Every booking, amendment and refund must come back cleanly. The vendors compete on connectivity: how many channels, how live, how few mapping errors. Arival estimated in 2023 that such reservation providers serve under 5% of the global market, so most operators still run some channels by hand. Marketplace commission and ranking economics are a different question. They are set out in [[problems/tour-operators/low-impact-2|Selling Through the Experience Marketplaces]] and are not this niche's contest.

## Current Tools & Gaps
Reservation systems with marketplace connections; channel managers and connectivity hubs; marketplace supplier portals. Gaps: product and option mapping errors that sell the wrong time or price; cancellation terms that differ by channel; refunds processed on one side only; and payouts that cannot be matched to bookings without spreadsheet work.

## Problems
- [[niches/tour-operators/marketplace-channel-operations/build|🔨 Build: A Channel Mapping Checker That Runs Before Every Change]]
- [[niches/tour-operators/marketplace-channel-operations/buy|🛒 Buy: Marketplace Seller Reconciliation, Built for Departures]]
- [[niches/tour-operators/marketplace-channel-operations/fix|🔧 Fix: The Refund Issued on One Side Only]]
