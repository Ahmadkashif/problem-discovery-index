# An Airspace P&L by Customer and Material

**Niche:** [[niches/landfill-operators/airspace-disposal-revenue/profile|Airspace Sales & Disposal Revenue]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A landfill knows what each customer pays per ton but not what each customer's waste costs it in cubic yards, so it cannot see which contracts are spending its scarcest asset cheaply.
**Tags:** #bayesian-linear-regression #feature-engineering #data-integration #revenue-impact #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is "Every serious competitor in this niche is fighting to earn the most revenue from each cubic yard of permitted airspace," but revenue per cubic yard multiplies two contests with different winners: the price a landfill realises per ton against rival disposal sites, and the tons it packs into each cubic yard. Decomposed into contested sub-niches below.

## The Problem
Airspace is sold by weight and consumed by volume. A ton of wet municipal waste, a ton of contaminated soil, a ton of shredded tyres and a ton of bulky furniture occupy very different volumes after compaction, and some materials are used as cover rather than consuming airspace at all. Landfill managers know this in general and price some materials with surcharges, but the airspace report arrives once or twice a year for the whole site, so no one can say which customers, materials or contracts earn the most per cubic yard.

## Why Nobody Has Built This
The two halves live with different people and systems: tickets in scale software owned by finance, volumes in survey files owned by engineering. Allocating a survey's volume change back to tickets is a statistical problem, not a report, and the consolidators who could build it treat airspace models as internal accounting.

## What to Build
A model that allocates each survey period's consumed airspace to the material and customer mix tipped in that period, using drone volume differences, ticket data by area and time, daily cover hauls and material density priors, with uncertainty. The output is revenue per cubic yard by customer, contract and material, refreshed with every survey, and a price floor per material that covers its airspace at the site's replacement cost of capacity.

## Target Customer
VPs of disposal and pricing at consolidators and regional landfill owners; solid waste directors at large public landfills setting gate rates.

## Impact If Built
If 10% of a 500,000-ton-a-year landfill's tons are under-priced by ~$10 per ton-equivalent of airspace (estimate), repricing them recovers ~$500K a year or keeps the airspace for better-paying waste.
