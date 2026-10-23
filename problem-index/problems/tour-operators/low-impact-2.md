# Selling Through the Experience Marketplaces

**Industry:** [[tour-operators|Tour Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Channel managers keep seats and prices in sync between the reservation system and Viator, GetYourGuide and Klook. None tells the operator what each channel's bookings actually earn after commission, cancellations and the marketplace's ranking rules.
**Tags:** #gradient-boosting #causal-inference #evaluation-metrics #feature-engineering #data-integration #revenue-impact #automation

## The Problem
A day-tour or short-break operator sells the same departure through its own website, walk-ups, hotel concierges, resellers and three or four experience marketplaces. The reservation system pushes availability and prices to each marketplace and takes bookings back. Each marketplace takes a commission. A supplier quoted Viator's basic rate at 27%, and GetYourGuide moved some suppliers from 20% to 30% in July 2025 with little notice. Each also applies its own cancellation-policy format, price-parity expectations, instant-confirmation rules and payout timing.

Each marketplace ranks products on signals it does not fully disclose, including review score and volume, conversion, cancellation rate and price. Ranking decides how many bookings arrive. Operators manage this by feel. They discount on one marketplace to climb its rankings and widen a cancellation window because a rep suggested it. They accept a commission increase because the alternative is disappearing from search. They seldom know whether a marketplace booking displaced a direct booking that would have come anyway, or what a channel's bookings earn once refunds, payout lags and the commission on cancelled-then-rebooked travellers are counted.

## What Already Exists
Reservation systems built for tours and activities (FareHarbor, Peek, Rezdy, Checkfront, Bókun, Ventrata, Xola) connect to the marketplaces and report bookings by channel. The marketplaces' supplier portals show performance and ranking tips. Generic channel managers and revenue-management tools in hotels (rate shopping, parity monitoring) do the equivalent job for rooms.

## The Customisation Gap
The tours version needs four things hotel tools and booking-system reports do not supply:
- **Contribution by channel and departure.** Each departure has a fixed cost (the guide, the vehicle, the boat) and a capacity, so a booking's value depends on whether that seat would otherwise have sold. A marketplace booking on a departure that was going to run half empty is worth more than one on a sold-out date.
- **Commission accounting that matches how marketplaces charge.** That includes rates per product, promotional programmes, and commission handling on cancellations and amendments.
- **Ranking and policy tests.** Did the price cut or the looser cancellation window actually move rank and bookings, or did seasonality? That calls for operator-level experiments and difference-in-differences, not a dashboard.
- **Payout reconciliation.** Each marketplace payout has to be matched to the bookings and refunds it covers.

## Impact If Solved
An operator selling ~30% of seats through marketplaces (estimate) could choose where to cap marketplace inventory, which products to push and which commission terms to accept, with evidence instead of instinct. Shifting even a tenth of marketplace bookings on already-full departures to direct sale, and recovering unchecked payout differences, plausibly adds ~1-2 points of net margin (estimate).
