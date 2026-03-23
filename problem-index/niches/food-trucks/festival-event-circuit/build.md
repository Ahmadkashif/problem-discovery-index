# Event ROI Prediction and Circuit Planning

**Niche:** [[niches/food-trucks/festival-event-circuit/profile|Festival & Event Circuit Trucks]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product helps a food truck operator predict which festivals and events will be profitable before committing a $500-$5,000 vendor fee and a weekend of inventory — turning event selection from a gamble into a data-driven decision.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A circuit operator receives 200+ event invitations per year and must select 80-120 to attend. Each requires a vendor fee ($500-$5,000), travel (gas, tolls, sometimes hotel), and 2-5x normal inventory investment. An experienced operator "knows" that a 50,000-person beer festival with $1,500 vendor fee is worth it while a 20,000-person arts fair with $2,000 fee is not — but this intuition takes 3-5 seasons of expensive trial-and-error to develop. New operators lose $10K-$20K in their first year on bad event choices.

## Why Nobody Has Built This
Event ROI prediction requires a training dataset that does not exist in any single place: operator revenue per event (private data), event attendance (claimed vs. actual — organizers inflate), weather on event day, competing truck count, event demographics, and vendor fee. Building this model requires a cooperative data network where multiple operators share anonymized per-event revenue data — a chicken-and-egg problem (operators will not share data until the model provides value, and the model cannot provide value without data).

## What to Build
An event intelligence platform where circuit operators log per-event revenue (auto-ingested from Square POS via geotagged shift data), and the system builds an event quality database: predicted revenue by truck type (taco truck vs. BBQ vs. dessert), event attendance estimates, weather impact, competitor density, and net ROI after fees and travel. Operators see event recommendations ranked by predicted ROI for their cuisine type. The model improves as the network grows.

## Target Customer
Festival circuit operators attending 60+ events/year who currently select events based on personal experience and word-of-mouth, with no systematic data on event quality.

## Impact If Built
Replacing the bottom 20% of event selections (net-negative events) with better choices shifts $10K-$25K in annual revenue from losses to profits — often the difference between a sustainable circuit operation and one that quits after 2 seasons.
