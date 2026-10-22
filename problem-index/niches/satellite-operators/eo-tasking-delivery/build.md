# Pricing a Tasking Order on Its Odds of Success

**Niche:** [[niches/satellite-operators/eo-tasking-delivery/profile|Earth-Observation Tasking & Delivery]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An earth-observation operator quotes a tasking order at a list price by priority tier, without estimating the probability it will actually deliver a usable image in the window.
**Tags:** #gradient-boosting #bayesian-inference #monte-carlo-methods #convex-optimization #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver a usable, cloud-free image of the customer's target inside the promised window, and whoever turns tasking orders into successful collections at the highest rate takes the tasking contract.

## The Problem
Whether an optical collection succeeds depends on the cloud forecast for the target during each feasible pass, the viewing angles available, the satellite's other commitments and the downlink path. Priority tiers buy a place in the queue, not an outcome. Customers learn the odds from experience and over-order to compensate.

## Why Nobody Has Built This
Collection planners optimise the satellite schedule, sales owns pricing, and historical outcome data — which collections succeeded and why — is scattered across planning, processing and QA systems.

## What to Build
A model that estimates, for each order and window, the probability of delivering an image meeting the customer's cloud, angle and resolution criteria, from cloud-forecast ensembles, pass geometry, queue contention and past outcomes. Quotes are priced on that probability, the scheduler uses it to allocate passes, and customers see a success estimate before they buy.

## Target Customer
Heads of collection planning and commercial operations at optical earth-observation operators.

## Impact If Built
Higher collection success per pass, fewer duplicate orders, and pricing that matches what the customer actually receives.
