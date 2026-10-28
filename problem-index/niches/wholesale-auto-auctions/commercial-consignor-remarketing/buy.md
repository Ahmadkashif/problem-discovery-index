# Hotel Revenue Management Adapted to Remarketing Floors

**Niche:** [[niches/wholesale-auto-auctions/commercial-consignor-remarketing/profile|Commercial Consignor Remarketing]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hotels and airlines solved perishable-inventory pricing decades ago; a wholesale car loses value daily and is priced with a floor copied from a guide.
**Tags:** #time-series-forecasting #bayesian-inference #gradient-boosting #optimization-fundamentals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to sell a commercial consignor's off-lease, rental, fleet and repossessed units for the most money after fees and transport, and whoever returns the highest net proceeds as a share of MMR takes the account.

## The Problem
A commercial unit is perishable inventory: it depreciates every day it sits, costs storage and loses its next run slot if it no-sells. Floors are set as a percentage of MMR, often by rule, and revised when a car fails to sell, not before.

## What Already Exists
Revenue management systems from hotel and airline pricing (IDeaS, PROS, Duetto, named from recall) forecast demand by date and segment, set dynamic floors and learn price elasticity from bookings. Retail markdown optimisation does the same for perishable goods.

## The Customization Gap
The adaptation needs:
- a demand curve per unit rather than per room type, built from condition grade, mileage, trim and region against live bidder counts;
- depreciation as the perishability clock, using the Manheim index trend and segment indices such as EV and non-EV;
- channel-specific fees, transport and rerun costs inside the objective, maximising net-to-MMR rather than revenue;
- consignor rules such as minimum floors, grounding windows and repossession notice periods;
- outputs that land in the auction's private-label and lane systems.

## Target Customer
Commercial account and pricing teams at the auctions, and remarketing directors at consignors large enough to set their own floors.

## Impact If Solved
Dynamic floors that cut no-sales on commercial units by a fifth save a rerun fee, a slot and a week of depreciation each. That is ~$150–300 a unit avoided on the share that would have no-sold (estimate).
