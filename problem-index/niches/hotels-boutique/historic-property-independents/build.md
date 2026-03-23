# Unique Room Revenue Optimization

**Niche:** [[niches/hotels-boutique/historic-property-independents/profile|Historic Property Independents]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No revenue management tool prices individual rooms — they price room types, but in a historic inn where every room is different, each room IS its own type and should be priced individually based on its unique attributes and demand patterns.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #tacit-knowledge-ml

## The Problem
A 25-room historic inn has 25 unique rooms: the corner suite with the fireplace, the attic room with the skylight, the garden-view room with the clawfoot tub, the small room by the stairs that books last. Standard PMS systems force these into 3-5 "room types" (Standard, Deluxe, Suite) and price by type. But a guest who specifically wants the fireplace room will pay $50 more than the guest who wants any "Deluxe" — and the GM knows this intuitively but has no system to capture individual room demand curves.

## Why Nobody Has Built This
Revenue management systems are designed for 200+ room hotels with 5-10 standardized room types and sufficient booking volume per type to train pricing models. A 25-room property with 25 unique rooms has ~365 room-nights per room per year — too little data for per-room pricing models using traditional approaches. The model must learn from room attribute features (size, view, floor, amenities, noise level) rather than per-room history alone.

## What to Build
A room-level pricing engine that learns guest willingness-to-pay for individual room attributes (view premium, fireplace premium, size premium, noise discount, floor premium) from historical booking data and guest behavior (which rooms are requested by name, which are upgraded to, which generate the highest review scores). Output: per-room nightly pricing that captures attribute-specific demand signals, not just room-type averages.

## Target Customer
Owners of 10-40 room historic properties where every room is architecturally unique and current PMS pricing cannot differentiate between rooms within the same "type."

## Impact If Built
Attribute-based room pricing captures $10-$40 per room-night in premiums that are currently averaged away — $50K-$200K annually for a 25-room property with 65% occupancy.
