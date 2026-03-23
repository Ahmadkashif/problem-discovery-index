# Last-Mile Grocery & Meal Kit Delivery

**Parent Industry:** [[industries/cold-chain-logistics|Cold Chain Logistics]]
**Category:** Low Digitized

## Profile
**Market Size:** $8-12B
**Share of Parent Industry:** ~8-10%
**Digital Adoption:** Low-Medium — delivery routing is app-based but temperature management relies on passive coolers with no monitoring or documentation
**Target Buyer:** Delivery operations manager at grocery delivery companies, meal kit providers, or dark store operators
**Automation Potential:** Medium — route optimization is partially automated but cold chain integrity during last-mile delivery is unmonitored and unmanaged

## What Makes This a Distinct Niche
Last-mile grocery and meal kit delivery operates an entirely different cold chain model than line-haul refrigerated transport. Delivery vehicles are vans or cars using passive insulated containers (cooler bags, EPS boxes with gel packs), not active refrigeration. Temperature maintenance depends on gel pack pre-conditioning, container insulation quality, ambient temperature, and time-to-delivery — none of which is monitored in real time. There is no reefer unit to control; the cold chain is a race against thermal decay. FSMA technically applies to these deliveries but enforcement is nascent, and most operators have no temperature documentation for individual deliveries. As grocery delivery scales (Instacart, Amazon Fresh, regional dark stores), the gap between line-haul cold chain standards and last-mile temperature chaos becomes a food safety and regulatory liability.

## Current Tools & Gaps
Routing platforms (Onfleet, Routific, Bringg) optimize delivery sequences for time and distance. No platform models temperature decay in passive containers as a routing constraint, predicts which deliveries will arrive above safe temperature based on ambient conditions and route timing, or provides per-delivery temperature documentation.

## Problems
- [[niches/cold-chain-logistics/last-mile-grocery-delivery/build|🔨 Build: Passive Cold Chain Temperature Decay Predictor]]
- [[niches/cold-chain-logistics/last-mile-grocery-delivery/buy|🛒 Buy: Temperature-Aware Last-Mile Route Optimization]]
- [[niches/cold-chain-logistics/last-mile-grocery-delivery/fix|🔧 Fix: Zero Temperature Visibility on Passive Cold Chain Deliveries]]
