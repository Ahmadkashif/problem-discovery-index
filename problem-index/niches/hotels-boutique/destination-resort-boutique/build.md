# Unified Guest Revenue Optimization Across Room + Ancillary

**Niche:** [[niches/hotels-boutique/destination-resort-boutique/profile|Destination Resort Boutiques]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product optimizes total guest spend (room + spa + F&B + experiences) as a unified revenue target — resort boutiques optimize each silo independently and miss cross-sell opportunities worth $50-$150 per stay.
**Tags:** #gradient-boosting #recommendation #regression #tabular-ml #revenue-impact

## The Problem
A resort boutique guest books a $300/night room for 3 nights ($900). But the total revenue opportunity is $1,400: $250 in spa treatments, $150 in restaurant dining, $100 in guided experiences. Currently, the room is priced by the GM, the spa markets separately, the restaurant runs its own promotions, and the experience desk hopes guests ask. No system calculates the total guest revenue potential, recommends pre-arrival upsells, or optimizes pricing across the full guest journey.

## Why Nobody Has Built This
Room revenue, spa revenue, F&B revenue, and experience revenue live in four different systems (PMS, Booker/Mindbody, restaurant POS, activity booking platform) with no shared guest ID. Merging these data streams requires cross-system integration that is technically feasible but has not been productized for single-property independents. Chain resorts solve this with enterprise CRM (Salesforce, Oracle Hospitality) — products that cost $50K+ and require dedicated IT.

## What to Build
A unified guest revenue platform that creates a single guest profile linking PMS reservation, spa booking, F&B POS, and activity booking data. Pre-arrival, the system recommends personalized upsells based on guest profile, booking history, and segment behavior patterns. Post-checkout, it calculates total guest yield and identifies revenue gaps (guests who booked rooms but never visited the spa — what was the conversion barrier?). Package optimization: pricing room + spa + dining bundles to maximize total yield rather than each component independently.

## Target Customer
Owners of resort boutique hotels where ancillary revenue (spa, F&B, experiences) represents 25-50% of total revenue and is currently managed independently from room revenue.

## Impact If Built
Increasing ancillary capture rate by 15-20% adds $30-$60 per occupied room-night — $150K-$350K annually for a 40-room resort at 65% average occupancy.
