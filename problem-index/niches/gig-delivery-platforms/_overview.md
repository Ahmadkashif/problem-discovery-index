# Niche Analysis — Gig Delivery Platforms

**Parent Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]

## Niche Selection

These platforms run world-class real-time allocation and point almost none of it at the courier's own economics. The eight niches follow that asymmetry: the offer a courier accepts or declines, the dispatch that produced it, the two places where unpaid time and unpriced judgement accumulate, the two people the system governs, and the mechanical layers.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Offer Construction & the Accept Decision | 🔵 High Market Share | ~$27B | High and deliberately opaque | Platform marketplace leadership |
| 2 | Dispatch, Routing & Batching | 🔵 High Market Share | ~$18B | Very high — the platforms' core competence | Platform dispatch engineering |
| 3 | Merchant Wait & Handoff | 🟠 Low Digitized | ~$10.8B | Low — a courier standing in a lobby | Merchant operations, couriers |
| 4 | Substitution & Order Accuracy | 🟠 Low Digitized | ~$9B | Low — ninety seconds and a guess | Platform grocery operations |
| 5 | The Courier | 🟣 Underserved Audience | ~$10.8B | Low — an app that issues instructions | Couriers, worker organisations |
| 6 | The Deactivation Review Agent | 🟣 Underserved Audience | ~$5.4B | Low — a policy, a queue and minutes | Platform trust & safety |
| 7 | Earnings, Pay & Cost Accounting | ⚡ Highly Automatable | ~$5.4B | Moderate — gross is shown, net is not | Platform finance, couriers, regulators |
| 8 | Onboarding, Background Checks & Identity | ⚡ Highly Automatable | ~$3.6B | High — automated and consequential | Platform trust & safety, supply growth |

## Why These Niches

The offer is where the whole system meets the worker: a number, a time estimate, and a few seconds to decide. Dispatch produces it. Merchant wait and substitution are where the estimate fails and the courier absorbs it. The two underserved people are the courier, governed by systems that never explain themselves, and the review agent deciding in minutes whether someone keeps their income. Earnings accounting and onboarding are mechanical, and both are where regulation is arriving first.

## Niches

- [[niches/gig-delivery-platforms/offer-construction/profile|🔵 Offer Construction & the Accept Decision]]
  - [[niches/gig-delivery-platforms/offer-outcome-prediction/profile|🎯 Offer Outcome Prediction]]
  - [[niches/gig-delivery-platforms/pay-composition-disclosure/profile|🎯 Pay Composition Disclosure]]
- [[niches/gig-delivery-platforms/dispatch-and-batching/profile|🔵 Dispatch, Routing & Batching]]
- [[niches/gig-delivery-platforms/merchant-wait-and-handoff/profile|🟠 Merchant Wait & Handoff]]
- [[niches/gig-delivery-platforms/substitution-and-accuracy/profile|🟠 Substitution & Order Accuracy]]
- [[niches/gig-delivery-platforms/the-courier/profile|🟣 The Courier]]
- [[niches/gig-delivery-platforms/the-deactivation-agent/profile|🟣 The Deactivation Review Agent]]
- [[niches/gig-delivery-platforms/earnings-and-cost-accounting/profile|⚡ Earnings, Pay & Cost Accounting]]
- [[niches/gig-delivery-platforms/onboarding-and-background-checks/profile|⚡ Onboarding, Background Checks & Identity]]

## Filter Notes

Seven of the eight are terminal — each names a single contest and further division would produce features rather than markets.

**Offer construction** is not, and its two halves separate on an unusually clean line: what the number will turn out to be, versus what the number is made of. Offer outcome prediction is an estimation problem — expected merchant wait by hour, realised trip duration including the parts the estimate omits, net earnings after vehicle cost, and the probability the offer turns out materially worse than promised. It is computable from the platform's own telemetry, it is testable against what actually happened, and the platform has its own reason to want it because bad offers produce declines, abandonments and churn. Pay composition disclosure is not an estimation problem at all. The number's components are known exactly at the moment it is generated — base, distance, effort, promotion, and in contested historical configurations the customer's tip — and disclosing them requires no computation whatsoever. It delivers nothing to the platform, removes the discretion that opacity provides, and is arriving by statute in jurisdiction after jurisdiction rather than by product decision. A platform builds the prediction half for its own metrics and defers the disclosure half until legislation forces it, which is precisely the observed history of this industry.

Two adjacent candidates were rejected as belonging elsewhere: **passenger transport with its own fleet, vehicle and driver economics** is the subject of [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]], and **contracted parcel and route-based last-mile delivery** belongs to [[industries/last-mile-delivery|Last Mile Delivery]].
