# Competitor Position Blind Spot

**Niche:** [[niches/food-trucks/location-revenue-intelligence/profile|Location Revenue Intelligence]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Fix (Pain Point)
**One-liner:** Operators arrive at a spot to find two competitors already parked there — splitting revenue three ways on a day they expected to be solo, because there is no real-time competitor visibility.
**Tags:** #data-integration #automation #revenue-impact

## The Problem
Food truck revenue at a location drops 30-50% for each additional truck of similar cuisine type parked nearby. Operators check competitor positions by scanning social media posts, texting other operators, or simply driving by — all unreliable and time-consuming. By the time an operator discovers a competitor at their planned location, they have already prepped, driven, and paid parking fees. Relocating mid-day is possible but costly (lost setup time, new permit zone needed, customer confusion). The blind spot is worst for operators who park in common high-traffic areas where multiple trucks converge.

## Why It's Still Broken
No centralized food truck location feed exists. Roaming Hunger and StreetFoodFinder list some truck locations, but participation is voluntary and incomplete. Social media posts about truck locations are delayed (posted hours after arrival) and scattered across platforms. Real-time GPS tracking would solve this, but operators resist sharing their exact position with competitors. The incentive structure is adversarial: sharing your location helps competitors avoid you, but also helps customers find you.

## What a Fix Looks Like
An opt-in location sharing network where operators share their current position in exchange for seeing other trucks' positions — creating a mutually beneficial early warning system. The key design is showing cuisine type and general area (not exact GPS) to reduce adversarial concerns while still preventing same-cuisine clustering. Operators who share see others; operators who do not share see nothing. Integration with the location scoring engine adjusts revenue predictions downward when competitors are detected nearby.

## Who Feels the Pain
Operators in competitive metro markets (50+ trucks in the metro area) who lose 10-20 revenue days per year to unexpected competitor clustering, costing $2K-$8K in split revenue.

## Impact If Fixed
Avoiding 10-15 competitor-clustered days per year by choosing alternative locations preserves $3K-$6K in revenue. The network effect grows as more operators participate, creating a natural moat for the platform.
