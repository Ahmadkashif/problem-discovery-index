# Tour Costing Across Currencies

**Industry:** [[tour-operators|Tour Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A tour is priced in dollars a year or more before departure from a cost sheet paid in four or five other currencies on different dates. Treasury tools can hedge the exposure, but none can read the cost sheet that creates it.
**Tags:** #monte-carlo-methods #time-series-forecasting #probability-distributions #optimization-fundamentals #data-integration #revenue-impact #automation

## The Problem
A product manager costs a ten-day European itinerary line by line, usually in a workbook that has grown over many seasons. Each line has its own currency and payment date:
- hotel nights in euros and Swiss francs, at a rate valid only for one season;
- coach days priced per vehicle;
- guide days, entrance fees and included meals;
- a deposit due on signature and a balance due 30 to 60 days before arrival.

The total is divided by an assumed group size, marked up to a target margin, converted at an assumed exchange rate and published, often 12-18 months before the first departure (estimate). Bookings then arrive over the following year. Supplier payments go out in tranches up to arrival.

When the dollar weakens between pricing and payment, the margin goes with it. A 10% move against the main cost currency can take several points off the margin on every departure (estimate). Operators respond in one of three ways. They hedge a guessed share of the season's exposure through a bank or FX specialist; they add a currency surcharge that advisors and travellers resent; or they absorb the loss. Most cannot say, departure by departure, how much currency they are actually short, because the exposure only exists inside the cost workbook and the booking forecast.

## What Already Exists
Treasury and FX-risk platforms (Kantox, Convera, Corpay, Ebury and the banks' own portals) hedge forecast cash flows and offer layered hedging programmes and pricing at forward rates. Tour-operations systems such as Tourplan and Tourwriter cost itineraries with multi-currency supplier rates. Spreadsheets do both, badly. Lindblad's 10-K describes the large-operator version: forward contracts and options covering a portion of currency risk on charter and tour contracts, with the unhedged remainder exposed.

## The Customisation Gap
The FX platform expects a cash-flow forecast; the tour operator has a cost sheet and a booking curve. The industry-specific layer would:
- read each itinerary's cost lines by currency and payment date;
- scale them by the forecast number of departures and travellers, since rooms and guides are bought per departure and coaches per vehicle, so cost does not scale with travellers;
- account for cancellations and supplier refunds that unwind exposure;
- produce a dated exposure by currency that updates as bookings arrive.

It would then simulate margin by departure under currency scenarios, show the price at which each itinerary still meets its target, and flag when a surcharge clause, a price change or an extra hedge is warranted. Hedges and published prices would be tied to the same record. None of this is FX science. It is tour costing logic the treasury vendors do not have and the tour software vendors do not model.

## Impact If Solved
An operator with ~$20-50M of non-dollar costs a year (estimate) would know its true exposure by currency and month, hedge against bookings rather than a guess, and stop discovering currency losses at season end. In a year with a ~10% adverse currency move, that plausibly protects ~1-2 points of gross margin (estimate), roughly ~$0.3-1M a year at that scale (estimate). It would also get a defensible basis for when to reprice.
