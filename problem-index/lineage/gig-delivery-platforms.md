# Lineage: Gig Delivery Platforms

**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** PaloAltoDelivery.com — a website showing local Palo Alto restaurants' menus, launched January 12 2013, whose orders were carried by couriers the site itself supplied; the seed of the DoorDash Dasher offer
**Builder:** Palo Alto Delivery
**Builder in vault:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Verification:** partial — see Sources

## The Problem That Came First

A restaurant that wants to deliver has to employ a driver for its busiest hour and pay for the other seven.

That is why, outside a few dense cities, most restaurants did not deliver at all. Demand for delivery is spiky — dinner rush, rain, a Friday — and a single restaurant's volume is too small to keep one courier busy. Pizza chains made it work by building the whole business around delivery. A Thai place in a suburban strip mall could not. The cost of delivery was not the trip; it was the idle driver between trips.

## What Got Built

A website with menus on it, and a promise that someone would bring the food.

DoorDash's 2020 prospectus dates it precisely: on January 12 2013 the founders "launched a website displaying menus from local restaurants in Palo Alto, California." Within hours the first customer ordered prawn pad thai and spring rolls from a nearby Thai restaurant, and dinner was delivered to his door.

The site did not need the restaurants to change anything. It listed menus the restaurants already had and supplied the courier from outside. That is the whole mechanism in miniature: pool delivery demand across *many* restaurants so that one courier's idle time between one restaurant's orders is filled by another's. Everything later — the Dasher app, batching, the offer screen with a number on it — is the industrial version of the Palo Alto page.

## Who Built It, And Why Them

Tony Xu, Stanley Tang, Andy Fang and Evan Moore, Stanford students at the time. The company was incorporated in 2013 as Palo Alto Delivery Inc., took Y Combinator seed money that summer, and renamed itself DoorDash, Inc. in 2015.

**Why them:** they went looking for a merchant problem rather than a consumer one. In the prospectus's founders' letter they describe canvassing Bay Area businesses on what they needed to grow, and being surprised by the answer: "Delivery was not a new idea, yet outside of New York City in the United States, very few businesses offered it." A restaurant could not solve delivery alone because its own demand was too thin; only a party sitting *across* many restaurants could make one courier's hour pay. Students with a website and no restaurant were exactly that party — and the suburban, car-dependent setting, not a dense downtown, is what made pooling the whole value.

The prospectus also records that the couriers are "independent contractors" — the Dashers. That choice is where the model's economics and its later fights both live.

## What It Cost

Pooling moved the idle-time cost from the restaurant to the courier.

A restaurant's employed driver is paid for the slow hours. A contractor offered one job at a time is paid for the job, and the wait between offers is theirs. The platform's pay model was the visible edge of that: until DoorDash changed it after 2019 press coverage, a customer's tip went first to covering the company's guaranteed minimum per order rather than on top of it. And classification of the courier became a standing legal question the prospectus lists among its principal risks.

## What You Still Touch

The offer that appears on a courier's phone — one number, accept or decline — is the Palo Alto page's pooling logic handed to the worker to judge in seconds.

- [[problems/gig-delivery-platforms/high-impact|🔴 The Offer Shows a Number and Not What It Is Made Of]] — the price of one job in a pooled market
- [[problems/gig-delivery-platforms/worker-life-1|🟢 The Courier Waiting Unpaid]] — the idle time pooling relocated
- [[problems/gig-delivery-platforms/low-impact-1|🟡 Batching, Routing and Wait Time]]
- [[niches/gig-delivery-platforms/offer-construction/profile|Offer Construction & the Accept Decision]]
- [[niches/gig-delivery-platforms/merchant-wait-and-handoff/profile|Merchant Wait & Handoff]]

**Sources:** DoorDash, Inc., Form S-1, SEC EDGAR, filed 13 November 2020 (CIK 1792789, accession 0001193125-20-292381) — mission statement (12 January 2013 launch, first order), founders' letter (Stanford canvassing; the New York City quotation), "Corporate Information" (incorporated 2013 as Palo Alto Delivery Inc.; renamed DoorDash, Inc. in 2015), Dashers as independent contractors, worker-classification risk factors; Wikipedia, *DoorDash* (four founders including Evan Moore; PaloAltoDelivery.com; Y Combinator seed; 2019 tipping model); this vault's `history/gig-delivery-platforms.md` (vault material, not independent corroboration). WebSearch was unavailable this session (session cap reached). ⚠️ **Conflict:** Wikipedia says the company was "incorporated as DoorDash in June 2013"; the S-1 says incorporated as Palo Alto Delivery Inc. with the name change in 2015. The S-1 is used and governs the build-time key. **Not established:** that the founders personally made the early deliveries, and the widely repeated detail that the first site carried PDF menus and a phone number — both plausible, neither in a fetched source, so neither is asserted.
