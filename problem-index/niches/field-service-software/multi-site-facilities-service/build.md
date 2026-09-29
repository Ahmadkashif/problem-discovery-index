# Verified Service Delivery Without a Supervisor Present

**Niche:** [[niches/field-service-software/multi-site-facilities-service/profile|Multi-Site Facilities Service]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A facilities contractor's entire product is work performed where nobody is watching, and its evidence that the work happened is a crew member ticking boxes on their own phone.
**Tags:** #cnns #object-detection #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #compliance #worker-facing
**Contested on:** Every serious competitor in multi-site facilities software is fighting to prove that service actually happened, to the standard promised, at a site nobody supervises — and whoever makes verification credible to the client takes the contract.

## The Problem
A cleaning specification lists forty tasks per floor per night. The crew completes most of them most nights. The record is a checklist the crew fills in themselves, which is both unverifiable and, for the crew, a tedious ritual that means nothing. The client's facilities manager forms an opinion from what they notice walking in, which is dominated by a small number of visible things — the entrance, the washrooms, the meeting room used that morning. Contracts are lost on that opinion. The contractor's defence is a checklist nobody believes and a supervisor's inspection from three weeks ago.

## Why Nobody Has Built This
Verification in this setting has an ugly history: the available technology has mostly been surveillance-shaped — badge readers, GPS tracking, phone monitoring — which workers experience as distrust and which unions and workers have resisted for good reasons. Products that went down that path damaged the working relationship without producing evidence a client found convincing, since knowing a worker was in the building is not evidence that the work was done. Building verification that is about the work rather than about the worker is a harder design problem and has not been attempted seriously.

## What to Build
Verification anchored to the outcome rather than to the person. Task completion evidenced by a photograph of the completed state at defined points, captured as part of the work rather than as a separate reporting act, with time and location attached — which verifies the condition of the space, not the movements of an individual. Image comparison against the site's own baseline flags conditions that do not match a completed standard, which is what turns a photo archive into a signal. Client-visible evidence is the product: a facilities manager who can see last night's state of the areas they care about stops forming an opinion from a single glance at the entrance. Design discipline matters here more than technology — the system must measure spaces and not people, must be explained to the crew in exactly those terms, and must not become a productivity monitor, because that is the version that will be resisted and deserves to be.

## Target Customer
Multi-site janitorial and facilities contractors competing on quality against price-driven bidders, and the clients whose contract decisions currently rest on impressions.

## Impact If Built
Evidence changes the commercial conversation from assertion to record, which is what lets a good contractor defend a price against a cheaper bidder — the segment's central competitive problem. It also gives crews something the current arrangement denies them: a record that the work they did was done, which is a defence as much as a measurement.
