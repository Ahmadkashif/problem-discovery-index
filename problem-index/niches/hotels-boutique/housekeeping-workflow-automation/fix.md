# Linen and Supply Par Level Accuracy

**Niche:** [[niches/hotels-boutique/housekeeping-workflow-automation/profile|Housekeeping Workflow Automation]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Fix (Pain Point)
**One-liner:** Boutique hotels over-order linens and supplies by 20-30% because par levels are set by gut feel and never adjusted for actual occupancy patterns — tying up $10K-$30K in unnecessary inventory.
**Tags:** #time-series-forecasting #regression #tabular-ml #automation #revenue-impact

## The Problem
The housekeeping supervisor orders linens (sheets, towels, bathrobes) and supplies (toiletries, cleaning products) based on par levels set when the hotel opened — a fixed count per room regardless of occupancy. A 40-room hotel maintaining par for 100% occupancy year-round holds $20K-$40K in linen inventory, but average occupancy is 65%. Over-ordering creates storage problems (limited space in boutique properties), cash flow waste, and quality degradation (linens sitting unused for months lose freshness). Under-ordering on high-occupancy weekends forces emergency laundry runs.

## Why It's Still Broken
Par levels require matching supply to predicted occupancy by day — but the supervisor sets pars annually (if ever) and does not adjust for seasonal demand patterns, day-of-week variations, or average stay length (which affects linen change frequency). Occupancy-driven par adjustment is simple math, but no one is doing the math because there is no tool that connects occupancy forecasts to supply ordering.

## What a Fix Looks Like
An automated par-level system that uses the PMS occupancy forecast to calculate linen and supply needs per day, generates weekly ordering recommendations adjusted for actual occupancy patterns, and tracks linen lifecycle (usage count, condition) to optimize replacement schedules. The supervisor sees: "This week: 28 rooms occupied average. Recommend 42 sheet sets on hand (28 x 1.5 safety factor). Current stock: 60. Skip linen order this week."

## Who Feels the Pain
The housekeeping supervisor who runs out of bath towels on a sold-out Saturday because the delivery is not until Monday, and the owner who has $15K in linens sitting in a closet unused for months during low season.

## Impact If Fixed
Reducing linen over-ordering by 25% frees $5K-$10K in working capital. Eliminating emergency supply runs saves $2K-$5K annually in rush-delivery premiums. Extending linen life through usage-based rotation reduces replacement costs by 10-15%.
