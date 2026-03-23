# Guest Lifetime Value Intelligence

**Niche:** [[niches/independent-restaurants/reservation-heavy-upscale/profile|Reservation-Heavy Upscale Independents]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** CRM tools like SevenRooms and OpenTable's GuestCenter track visit history but do not predict which guests will become high-LTV regulars or which are at risk of churning.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #recommendation #revenue-impact

## The Problem
Upscale restaurants have 20-35% repeat guest rates, and the top 10% of guests generate 40-50% of annual revenue. But the GM treats all reservation requests equally because no tool distinguishes a first-time visitor who will become a $10K/year regular from a tourist who will never return. High-LTV guests who have a single bad experience and stop visiting are not flagged until the GM notices months later — by then, recovery is impossible.

## What Already Exists
SevenRooms, OpenTable GuestCenter, and Resy OS offer guest profile management with visit history, spending, and notes. They show "this guest has visited 12 times and spent $4,500" — backward-looking data. They do not predict future value, churn risk, or optimal re-engagement timing.

## The Customization Gap
The tool must predict guest lifetime value from early signals (first-visit spending, booking lead time, party composition, ordering pattern), identify churn risk (a regular who has not booked in 45 days when their pattern was monthly), and recommend personalized re-engagement actions (a specific comp or invitation tailored to the guest's preferences). This requires restaurant-specific LTV models trained on reservation and POS data, not generic CRM scoring.

## Target Customer
GMs and owners of upscale independents with 200+ unique guests per month who want to convert one-time visitors into regulars and prevent high-value guest churn.

## Impact If Solved
Converting 5% more first-time visitors into regulars and retaining 10% more at-risk regulars adds $50K-$150K in annual revenue for a typical upscale independent.
