# No-Show Revenue Recovery

**Niche:** [[niches/independent-restaurants/reservation-heavy-upscale/profile|Reservation-Heavy Upscale Independents]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Fix (Pain Point)
**One-liner:** No-shows cost upscale independents 8-15% of potential revenue, but the tools to predict, prevent, and recover from them are either nonexistent or socially unacceptable to deploy.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact

## The Problem
Upscale independents experience 8-15% no-show rates on any given night, with each no-show costing $100-$400 in lost revenue plus wasted prep. The restaurant cannot overbook like a hotel because walking a guest destroys the brand. Credit card holds deter some no-shows but also deter bookings — a 50-seat restaurant that adds a $50 cancellation fee sees a 10-15% drop in reservation volume, trading one problem for another.

## Why It's Still Broken
No-show prevention is a behavioral problem, not just a technology problem. Confirmation texts reduce no-shows by 20-30% but do not eliminate them. The remaining no-shows are "intention no-shows" — people who booked multiple restaurants and decided at the last minute, or who simply forgot despite reminders. Predicting which specific reservations are likely to no-show (based on booking channel, lead time, party size, guest history, weather, and day-of-week) would allow the restaurant to selectively overbook high-risk slots without walking committed guests.

## What a Fix Looks Like
A no-show prediction model that scores each reservation's no-show probability, enabling selective overbooking: on a night where 4 reservations have >60% no-show probability, the system recommends accepting 1-2 additional reservations for those time slots. Combined with tiered confirmation urgency (high-risk reservations get a personal call, not just an SMS), this recovers 50-70% of no-show revenue without walking guests.

## Who Feels the Pain
The chef who prepped for 120 covers and served 105, wasting $500-$1,000 in food, and the owner who watches $1,500 in revenue evaporate on a Saturday night with no recourse.

## Impact If Fixed
Recovering 50% of no-show revenue saves $30K-$80K annually for a typical upscale independent — a direct bottom-line improvement in a segment where net margins are 3-7%.
