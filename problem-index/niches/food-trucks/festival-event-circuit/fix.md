# Post-Event P&L and Fee Negotiation Data

**Niche:** [[niches/food-trucks/festival-event-circuit/profile|Festival & Event Circuit Trucks]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Fix (Pain Point)
**One-liner:** Circuit operators have no per-event profit data — they pay vendor fees blind, negotiate without leverage, and cannot tell which events actually make money.
**Tags:** #data-integration #automation #revenue-impact #tabular-ml

## The Problem
After a festival weekend, most operators know their gross sales (from Square) but cannot tell you their net profit for that specific event. Calculating per-event P&L requires subtracting vendor fee, travel costs (gas, tolls, hotel), ingredient costs for that event's prep, staff wages, and equipment wear — all tracked in different places or not at all. Without event-level P&L, operators cannot identify which events are net-negative, negotiate vendor fees with data, or make informed decisions about returning next year.

## Why It's Still Broken
POS systems track sales, not costs. Travel costs are buried in personal credit card statements. Ingredient costs are approximated, not allocated to specific events. The result is that the most important financial question in a circuit operation — "Did I make money at that event?" — is unanswerable without 30 minutes of manual reconciliation per event, which most solo operators never do.

## What a Fix Looks Like
An automated post-event P&L builder that pulls POS revenue per shift (geotagged to the event), auto-captures travel costs (mileage tracking or gas receipts via photo), allocates ingredient costs from prep orders, and subtracts the vendor fee to produce a per-event profit statement within 24 hours. Over time, the system builds a per-event history that operators use to negotiate fees ("I grossed $4K at your event but netted $800 after your $2,500 fee — I need $1,500 or I'm not returning").

## Who Feels the Pain
Solo circuit operators who attend 80-120 events/year and currently cannot identify which 20-30% of their events are net-negative drags on annual profitability.

## Impact If Fixed
Operators who can identify and eliminate their bottom 20% of events (net-negative) and negotiate fees down 15-20% on marginal events add $8K-$15K in annual profit without working a single additional day.
