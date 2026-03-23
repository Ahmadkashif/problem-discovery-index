# Selling Out Too Early on High-Demand Nights

**Niche:** [[niches/hotels-boutique/dynamic-rate-optimization/profile|Dynamic Rate Optimization]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Fix (Pain Point)
**One-liner:** A boutique hotel that sells out at $189 three days before a demand spike discovers competitors are selling at $289 — $100 per room left on the table because rates were not raised fast enough.
**Tags:** #time-series-forecasting #regression #tabular-ml #revenue-impact

## The Problem
Selling out is not a success — it means the hotel priced too low. A 40-room boutique that sells out Wednesday for Saturday night at $189 ADR while the market clears at $249 left $2,400 on the table in one night. This happens 20-40 times per year on high-demand nights (weekends, events, holidays), representing $50K-$100K in annual foregone revenue. The GM sets rates on Monday, does not check again until Thursday, and by then the hotel is sold out at too-low prices.

## Why It's Still Broken
The GM's rate-setting cadence (2-3 times per week) is too slow for demand-driven markets. Booking pace accelerates on high-demand dates, but the GM does not see it until the next time they check rates — by which point the hotel is already sold out or nearly so. There is no alert system that says "your booking pace for Saturday is 3x the 30-day average — consider raising rates immediately."

## What a Fix Looks Like
A booking-pace alert system that monitors PMS booking flow and triggers notifications when pace exceeds historical norms for a given lead-time window: "Saturday night is 85% booked 4 days out — you are typically 60% booked at this lead time. Suggested rate increase: $189 -> $235." The alert includes one-click rate adjustment through the PMS. For GMs who want full automation, the system can auto-increase rates when pace exceeds thresholds.

## Who Feels the Pain
The GM who sees "SOLD OUT" on the PMS and realizes 15 minutes of research would have shown the market was $60-$100 higher — and the owner who watches $50K-$100K in annual revenue evaporate through pricing inattention.

## Impact If Fixed
Capturing $40-$80 more per room-night on the 30-50 high-demand nights the hotel currently underprices adds $50K-$150K in annual revenue — pure profit with zero incremental cost.
