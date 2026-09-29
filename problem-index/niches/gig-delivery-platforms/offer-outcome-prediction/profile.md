# Offer Outcome Prediction

**Parent Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether what an offer will actually turn out to be worth — in time, in cost and in risk of going badly — can be predicted at the moment it is sent.

## Profile
**Market Size:** ~$16.2B — 60% of the offer construction niche
**Share of Parent Industry:** ~18% of US gross order value
**Digital Adoption:** Moderate — the components are predicted internally for dispatch and not assembled for the courier
**Target Buyer:** Platform marketplace and dispatch engineering; courier-side tooling vendors
**Automation Potential:** Very high — every input is already instrumented

## What Makes This a Distinct Niche

This is the estimation half of the offer. What will the total engaged time be, including the merchant wait the estimate omits? What will the route actually cost in vehicle terms? What is the probability that this delivery goes materially worse than described — the order not ready, the address wrong, the apartment complex with no parking, the customer unreachable?

Every one of these is a prediction problem with abundant labels, because the outcome arrives within the hour and the platform records it. Merchant wait distributions, realised trip durations, route distances, failure and redelivery rates by address, and the historical divergence between estimate and actual are all in the telemetry.

It is a distinct market from disclosure because it is work — modelling, validation, calibration, serving at offer latency — and because the platform has its own reasons to want it. Better outcome prediction improves dispatch, reduces abandoned deliveries, reduces the support volume from failed handoffs, and improves courier retention. It is the half a platform builds for itself.

## Current Tools & Gaps

The platforms are excellent at the pieces they need for dispatch: ETA prediction, merchant readiness forecasting, route optimisation and demand prediction are all sophisticated and continuously improved. Courier-side third-party tools attempt a weak version of the assembled answer by screen-scraping offers and crowdsourcing outcomes, which is evidence of the demand and a poor substitute for the data.

The gap is assembly and direction. The components are computed for the platform's own allocation decisions and never combined into the single quantity that governs the courier's decision, nor calibrated against the courier's experience of them. No platform publishes how often its own estimates are materially wrong.

## Problems
- [[niches/gig-delivery-platforms/offer-outcome-prediction/build|🔨 Build: Realised-Outcome Prediction at Offer Time]]
- [[niches/gig-delivery-platforms/offer-outcome-prediction/buy|🛒 Buy: ETA and Forecasting Stacks Repointed at the Courier's Question]]
- [[niches/gig-delivery-platforms/offer-outcome-prediction/fix|🔧 Fix: Nobody Measures How Wrong the Estimates Are]]
