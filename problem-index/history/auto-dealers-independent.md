# History: Independent Auto Dealers

**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Primary Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**Secondary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Origin Parent:** [[origins/auto-oems/profile|Auto OEMs]]
**Episode Tier:** 1
**Transferable Pattern:** A financing structure sets the clock a business must run on. Software that helps you run faster against that clock is real and valuable — but it is not the same thing as software that changes the clock, and only a regulator or a lender can do the second.

## Before

A used-car lot before computerisation ran on exactly one instrument: the dealer principal's judgement, built up over years at the auction lane. Which cars were worth bidding on, at what price, given what they would fetch on the retail lot weeks later, was tacit knowledge, not a spreadsheet. Financing a purchase meant walking it to a local bank or a small finance company; verifying a car's history meant looking at the odometer and trusting the seller.

## The Origin Event — inherited thin, from someone else's factory floor

This industry's origin parent is [[origins/auto-oems/profile|Auto OEMs]], and the inheritance is explicitly a thin one. [[origins/auto-oems/legacy|The legacy file]] already states it: independent dealers received *"a thin, consumer-grade descendant: budget dealer-management systems handle basic vehicle inventory but... offer no analytics, no lead scoring — the computerised-inventory idea survived; the optimisation layer that made MRP worth building did not travel with it downstream."*

That inheritance has a specific, dated source. **ADP** entered dealership software in 1973 by acquiring two companies — National Inventory Control System (Portland, Oregon) and Computer System Inc. (Cincinnati, Ohio) — forming ADP Dealer Services, which computerised accounting, financial reporting and parts inventory for dealerships. That business grew for 41 years and more than 30 acquisitions before ADP spun it off in October 2014 as **CDK Global**. It was built overwhelmingly for franchised new-car dealers, whose volumes justified the cost. Independents — the roughly 38,000 non-franchise used-car dealers this vault studies — got budget descendants years later: **Frazer** and **DealerCenter**, which the vault's own hub note already describes accurately as offering "no analytics, no lead scoring, and minimal integration with auction platforms."

**A second, separate thread runs alongside the DMS thread and matters more to this specific industry: the wholesale supply channel.** Manheim, the dominant vehicle auction operator, was acquired by Cox in 1968 and expanded internationally through the 1980s. It is where the great majority of used vehicles this industry retails actually originate — off-lease returns, fleet de-fleeting, and franchised dealers' own trade-ins that they choose to wholesale rather than retail themselves. *(Manheim's own founding date, commonly cited as 1945, is recalled and not independently re-verified this session — treat as approximate.)*

## What Became Cheap

**Two different kinds of information, on two different timelines.**

**A vehicle's history.** CARFAX, founded 1984 in Columbia, Missouri, began by distributing fax-based vehicle history reports to dealers through the Missouri Automobile Dealers Association, working from a database of 10,000 records. It did not go direct-to-consumer until its website launched in December 1996. What it solved is the textbook lemons problem: a used-car buyer cannot verify a car's condition and history, so the market price adjusts downward for everyone, including honest sellers. By 2006, an estimated 34% of American used-vehicle buyers were purchasing a vehicle history report before buying.

**A vehicle's market value, continuously.** Where CARFAX priced risk, a second wave of tooling priced the market itself — real-time, VIN-configuration-level pricing built from live listing inventory and observed time-to-sell, rather than a periodic guide-book figure. This is a genuine algorithmic contest, and it is worth naming as one below.

## The Contest — gut feel versus the algorithm, at the auction lane

**vAuto**, built around a "days-supply" pricing discipline that replaced experience-based acquisition bidding with a computed figure for how fast a given vehicle configuration was actually turning in the local market, was brought fully under Cox Automotive in 2014 (having taken outside investment from Cox earlier). Cox's own consolidation of Manheim, Kelley Blue Book, Autotrader and vAuto under one roof by 2014 put the auction, the valuation guide, the listing marketplace and the pricing algorithm inside a single company — a vertical integration of exactly the four functions a buyer used to perform with judgement alone.

**This is a real contest and it has a real winner: data-driven acquisition pricing displaced pure gut feel at the margin**, the same way category management displaced pure merchandising instinct in [[origins/supermarket-chains/the-fight|supermarket retail]]. It did not eliminate judgement — condition assessment at the auction lane is still substantially a human skill — but it changed what "a good buyer" means, from someone with the best memory to someone who can read a days-supply number and knows when to override it.

## The Binding Constraint — the clock is set by the lender, not the lot

**Franchise law is not this industry's own constraint, and the file should not pretend otherwise.** All fifty states restrict manufacturers from selling new vehicles directly to consumers, but that law binds the relationship between an OEM and its *franchised* dealers. Independent, non-franchise used-car dealers are not party to it. Its relevance here is upstream and indirect: franchise law is part of why used-vehicle supply flows through wholesale auctions in the first place, rather than OEMs disposing of returned and traded vehicles directly — but stating it as *the* constraint on independents would overclaim what the law actually does.

**The real, binding constraint is floor-plan financing**, and it is a financial rather than a legal one. A franchised dealer typically floors inventory through a manufacturer-captive lender at preferential terms. An independent, non-franchise dealer overwhelmingly cannot access that captive financing and instead floors inventory through non-captive lenders — Cox Automotive's own NextGear Capital is the largest — at higher rates, with **curtailment**: a schedule of forced partial principal repayment at fixed intervals (commonly 30, 60 and 90 days) regardless of whether the vehicle has sold. This vault's own hub note states the resulting daily cost directly: **$30–50 in floorplan interest, depreciation and lot rent for every day a vehicle sits unsold.**

**No software changes the interest rate or the curtailment schedule.** What software can do — and what vAuto's days-supply logic and this vault's own high-impact problem note both aim at — is shrink the number of days a given vehicle sits against that clock. That is a real, valuable, buildable thing. It is not the same as fixing the clock, and an FDE should be precise with a dealer about which one is being sold.

## Why There Is No Graveyard Inside This Segment — and one adjacent to it, worth knowing

**No venture-scale digital-disruption graveyard exists among truly independent, non-franchise used-car dealers**, because venture capital never targeted that segment the way it targeted freight brokerage. The capital instead targeted an *adjacent and different* business model: vertically integrated used-car e-commerce retail, competing with independents rather than serving them. **Vroom is the clean example.** It announced on January 22 2024 that it was discontinuing its e-commerce operations and winding down its used-vehicle dealership business entirely, citing an inability to raise capital in the market conditions of the time, laying off roughly 800 employees; it filed for Chapter 11 in November 2024. Vroom kept two subsidiaries running — United Auto Credit Corporation, a finance company, and CarStory, an AI-powered analytics platform sold into auto retail.

**Do not conflate this with the independent dealer's own story, the way an episode about freight must not conflate Convoy's collapse with digital brokerage failing generally.** Vroom's thesis was to *replace* the independent lot with a national online one. Its collapse says something about that specific bet under 2020s capital conditions. It says nothing about whether an ordinary independent lot, financed the ordinary way and buying at Manheim the ordinary way, is in any distress at all.

## What's Still Open

- [[problems/auto-dealers-independent/high-impact|🔴 Vehicle Acquisition Pricing and Turn Rate Optimization]] — the days-supply problem, and the clock behind it
- [[problems/auto-dealers-independent/low-impact-2|🟡 Title and Registration Processing Automation]]
- [[problems/auto-dealers-independent/worker-life-2|🟢 Finance Manager Lender Submission Tedium]]
- [[niches/auto-dealers-independent/marketplace-pricing-analytics/profile|Listing Marketplace Pricing Analytics]] — vAuto's descendants
- [[niches/auto-dealers-independent/vehicle-history-report-providers/profile|Vehicle History Report Providers]] — CARFAX's category
- [[niches/auto-dealers-independent/wholesale-auction-flippers/profile|Wholesale Auction Flippers]]
- [[niches/auto-dealers-independent/buy-here-pay-here/profile|Buy-Here-Pay-Here]] · [[niches/auto-dealers-independent/bhph-portfolio-analytics/profile|BHPH Portfolio Analytics]] — where floor-plan financing's cousin, in-house consumer financing, lives

## The Transferable Pattern

> **When a dealer's or a business owner's stated problem is "I need better data," check first whether the actual constraint is a financing term nobody is going to renegotiate. If it is, the honest product speeds up the business's clock. It does not stop it.**

This industry sits between [[origins/auto-oems/profile|its origin parent's]] push-versus-pull manufacturing argument and [[history/dental-practices|dental practice's]] un-indexed annual maximum, and it is worth teaching as the case where **both a real algorithmic contest (vAuto) and a real binding financial constraint (floor-plan curtailment) coexist in the same shop, and a good FDE sells against the first without pretending to have solved the second.**

**Sources:** Wikipedia, *CDK Global* (ADP's 1973 acquisitions of NICS and CSI; Oct 1 2014 spin-off); this vault's `origins/auto-oems/legacy.md` (the "thin, consumer-grade descendant" finding, already citing this vault's own `industries/auto-dealers-independent.md`); Wikipedia, *Carfax (company)* (1984 founding, Missouri Automobile Dealers Association distribution, Dec 1996 website launch); Wikipedia, *Car dealerships in the United States* (state franchise laws, floor-plan/curtailment terminology, dealer holdbacks); Wikipedia and Cox Automotive corporate materials on Manheim (1968 Cox acquisition) and vAuto (2014 full integration under Cox Automotive) — vAuto's founding date and "Velocity Method" branding are recalled from industry trade press, not independently re-verified this session; Wikipedia, *Vroom (company)* (Jan 22 2024 wind-down announcement, Nov 2024 Chapter 11); this vault's `industries/auto-dealers-independent.md`.
