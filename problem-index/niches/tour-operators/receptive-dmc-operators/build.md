# A Request Turned Into a Costed Draft in Minutes

**Niche:** [[niches/tour-operators/receptive-dmc-operators/profile|Receptive Operators & Destination Management Companies]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A receptive's quoting team reads every emailed request, rebuilds an itinerary from memory and costs it line by line, while the competing receptive does the same race.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #gradient-boosting #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn an overseas operator's or agency's request into an accurate, costed proposal within hours, and whoever quotes fastest without missing a cost line takes the account.

## The Problem
Requests arrive as free text: dates, group size, a route, a budget, a few must-sees. A product specialist interprets them, picks hotels and routing from experience, checks availability and rates, adds coach, guide, entrances and meals, and prices the result. A complex request can take a day. The receptive answers dozens a week in season, and wins a minority.

## Why Nobody Has Built This
Tour-operations software holds rates and builds quotes once someone has designed the itinerary. The design step, turning a request into a sensible draft, depends on the specialist's knowledge of what works: driving times, which hotels suit which buyer markets, seasonal closures. It was not automatable before language models. The receptive's past quotes and won trips are the training data, and they sit in files.

## What to Build
An assistant that reads a request and retrieves similar past quotes and won itineraries. It drafts a day-by-day itinerary within driving-hour and seasonal constraints, and prices it from the receptive's contracted rates with every conditional cost applied. The specialist edits rather than builds. A win-probability model on past quotes shows which price and content choices tend to win with each buyer.

## Target Customer
Owners and heads of product at receptive operators and DMCs handling hundreds to thousands of requests a year (estimate).

## Impact If Built
Quotes in hours instead of days, more requests answered per specialist, and higher win rates from being first with an accurate price (estimate).
