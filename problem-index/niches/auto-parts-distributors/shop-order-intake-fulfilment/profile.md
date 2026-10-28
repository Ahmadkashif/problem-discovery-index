# Shop Order Intake & Hot-Shot Fulfilment

**Parent Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Category:** Highly Automatable
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn a shop's call, text or e-catalog order into the right part at the shop's bay, but that hides two contests with different winners: matching the request to the one part that fits that VIN, won by catalog depth and matching models and measured by fitment returns, and running the delivery, won by route density and dispatch and measured by shop orders cancelled because the part arrived after the shop's window. Decomposed into contested sub-niches below.

## Profile
**Market Size:** ~$5–7B a year of counter and driver labour spent taking, matching and delivering shop orders across U.S. parts stores and distributors (estimate: ~$3B of counter time on commercial orders, from ~273,300 parts salespersons, BLS, search summary, plus ~$3–4B of commercial delivery)
**Share of Parent Industry:** ~1.6% of the three codes' receipts (estimate)
**Digital Adoption:** Medium — e-catalog orders are digital, but phone and text orders are keyed by hand and runs are dispatched by shouting across the counter
**Target Buyer:** VP of store operations or commercial operations; owner at an independent
**Automation Potential:** Very High for matching and dispatch; the hand-off at the bay stays physical

## What Makes This a Distinct Niche
This is the industry's order-to-bay loop: a shop asks for parts by phone, text or e-catalog, the counter decodes the vehicle and matches the parts, someone picks them, and a driver runs them to the bay inside the promised window. The AI order-intake vendors selling to distributors generally (the Avent, Mercura and Comena field) are profiled once, at [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]]; this niche keeps to what differs in auto parts: requests keyed by VIN or year-make-model-engine rather than SKU or customer stock code, voice and text rather than emailed purchase orders, and a hot-shot delivery that follows within the hour. Of the AI vendors hiring near this desk, only Partly (Austin) is auto-specific; Endeavor builds custom AI for manufacturers and distributors with no auto customer named, SalesPatriot is an adjacent aerospace and defence quoting platform, and Paragon is hiring a founding engineer only. Writing one contest for the loop fails: the matching step and the delivery step are bought from different vendors, judged on different numbers, and won by different strengths.

## Current Tools & Gaps
E-catalog networks and the chains' shop sites take digital orders; business systems from Epicor, MAM and Autologue hold the catalog and stock; parts-identification models such as Partly's are reaching repairers; routing apps exist for last-mile delivery. Nothing joins a request to its match, its run and its outcome.

## Problems
- [[niches/auto-parts-distributors/shop-order-intake-fulfilment/build|🔨 Build: One Record From the Shop's Request to the Part at the Bay]]
- [[niches/auto-parts-distributors/shop-order-intake-fulfilment/buy|🛒 Buy: Distributor Order-Intake Agents Adapted to Shop Calls and Texts]]
- [[niches/auto-parts-distributors/shop-order-intake-fulfilment/fix|🔧 Fix: Shop Orders Arrive on Four Channels and Leave No Trace]]
