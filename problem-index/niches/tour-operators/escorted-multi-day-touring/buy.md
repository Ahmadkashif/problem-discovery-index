# Airline and Cruise Revenue Management, Cut Down to Departures

**Niche:** [[niches/tour-operators/escorted-multi-day-touring/profile|Escorted Multi-Day Touring]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines and cruise lines have forecast bookings by departure and priced against capacity for decades; escorted touring has the same structure with far less data per departure.
**Tags:** #time-series-forecasting #bayesian-inference #dynamic-programming #optimization-fundamentals #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to guarantee departures early enough for advisors to sell them without running them half empty, and whoever guarantees the most departures while holding load above break-even takes the account.

## The Problem
Each departure has fixed capacity, a booking window of many months and a hard date. That is the classic revenue-management setting. Escorted operators mostly use only its pricing half, through early-booking discounts and promotions. They rarely forecast at departure level or connect forecasts to inventory decisions.

## What Already Exists
Airline and cruise revenue-management systems, from vendors such as PROS and the cruise lines' in-house systems, forecast demand by departure and fare class, set inventory controls and model cancellations and overbooking. Hotel revenue-management systems do the same for room nights.

## The Customization Gap
The adaptation needs:
- forecasts that work with 30-40 seats per departure and a few seasons of history, pooling across itineraries, rather than hundreds of seats and decades;
- inventory decisions spread across several supplier allotments per departure, each with its own release date, not one cabin inventory;
- the guarantee decision, a binary commitment with no airline equivalent;
- consolidation, which moves booked travellers between dates;
- single-supplement and room-type mix, which change cost per traveller.

Pricing belongs in the same system but matters less than the run-or-cancel call.

## Target Customer
Revenue and operations leaders at escorted brands that already run dynamic pricing and want inventory decisions on the same footing.

## Impact If Solved
A proven method family, adapted to small departures and multi-supplier inventory, gives the departure call a forecast and an expected value instead of a spreadsheet.
