# History: Gig Delivery Platforms

**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Primary Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** *(none)* — see below
**Episode Tier:** 1
**Transferable Pattern:** When a market's labour law has not caught up with its dispatch technology, the fight over classification is decided at the ballot box and in appellate courts, not in an engineering roadmap — and the number a worker is paid for is always smaller than the number the platform can compute.

> **Origin Parent — omitted.** No industry in `origins/` bequeathed this one anything mechanical. The nearest analogue, package carriers' COSMOS/ORION lineage, solved *where is the parcel*; this industry's founding problem is *where is the worker, and will they accept this offer* — a labour-dispatch problem, not a freight-tracking one. It was built inside the span this vault already covers, on smartphones that did not exist until 2007.

## Before

Restaurant delivery existed before this industry and was mostly done by the restaurant: a pizza chain or a Chinese takeaway employed its own driver, paid an hourly wage plus tips, and covered a radius it could reliably reach in thirty minutes. Grocery delivery was a service department of the supermarket itself, or it did not exist. A courier company that delivered for hire — a bike messenger firm, a local same-day service — ran on phone dispatch and a small roster of drivers who worked regular hours and knew their patch.

What did not exist was a continuous, app-mediated marketplace matching a large, elastic pool of intermittent drivers to a large, elastic pool of small orders, priced and dispatched per delivery with no minimum commitment on either side.

## The Origin Event

**Uber was founded in March 2009**, by Garrett Camp and Travis Kalanick, as **UberCab** — a black-car hailing service, renamed Uber in 2011 after complaints from San Francisco taxi regulators about the "cab" in its name. It is usually told as a consumer convenience story. Mechanically it is [[series/eras/wave-08-mobile-gps|a dispatch story]]: a phone that reports its own GPS position continuously, matched against another phone doing the same, turns allocation from a phone call into a computation performed thousands of times a second.

Delivery followed the same mechanism onto a different payload. **Instacart was founded 1 July 2012** by Apoorva Mehta, Max Mullen and Brandon Leonardo — personal shoppers dispatched to a grocery store rather than a rider dispatched to a curb. **DoorDash was founded January 2013** in Palo Alto, as PaloAltoDelivery.com, by four Stanford students — Tony Xu, Stanley Tang, Andy Fang and Evan Moore — incorporating under its current name that June. Uber itself entered food with UberEats later in the decade. By December 2018 DoorDash had passed Uber Eats into second place in US food-delivery sales; by March 2019 it had passed Grubhub into first.

**None of this required a new invention.** The GPS chip, the data connection and the payment rail all existed by 2009 courtesy of the smartphone. What these companies built was the dispatch logic and the labour model sitting on top of it — and the labour model is where the history actually lives.

## What Became Cheap

Hiring a person for a single delivery, for however long it takes, with no schedule, no interview, no minimum shift and no employment relationship — priced per task and matched by an algorithm running continuously against a mapped, moving pool of contractors. That is the whole mechanical innovation. Everything contested about this industry follows from what that mechanism does *not* price: the wait, the deadhead mile back to a dense zone, and the moment a customer's tip is added after the fact.

## The Trade-Off

DoorDash's early pay model is the cleanest documented instance of a trade made deliberately rather than discovered by accident. Through the mid-2010s into 2019, when a customer added a tip, it did not add to the courier's guaranteed base pay — it substituted for a portion of it, so a generous customer subsidised DoorDash's own guarantee rather than topping up the driver's earnings. **Reporting in July 2019 made this public; by January 2020, coverage citing driver-reported data put realised net pay as low as $1.45 an hour after expenses in some cases; a class action followed the "materially false and misleading" framing of the tipping policy, and DoorDash settled it for a reported $17 million in 2025.** Instacart absorbed a smaller, earlier version of the same dispute: a **$4.6 million settlement in 2015** over shopper misclassification and improper tip pooling.

The trade was not a bug. Structuring pay so a tip could offset a guarantee lowers the platform's own labour cost while keeping the number a courier sees on the offer screen unchanged — the courier cannot tell, from the offer alone, whether a large tip is being paid twice or once. DoorDash changed the model publicly after the 2019 reporting. The fact that it had to be reported before it changed is the finding worth keeping.

## The Binding Constraint

**California's Dynamex ruling, 30 April 2018,** replaced a multi-factor test for who counts as an employee with a strict **ABC test**: a hiring entity must prove a worker is free from its control, does work outside its usual business, and independently runs a trade of the same kind — failing any one prong means employee status. **Assembly Bill 5 codified this into statute, passed the legislature 10–11 September 2019, was signed 18 September 2019, and took effect 1 January 2020.**

Gig platforms could not plausibly clear prong (B) — delivery *is* DoorDash's usual business — so AB5 threatened to reclassify their entire courier workforce as employees. Uber, Lyft, DoorDash, Instacart and Postmates responded by funding **Proposition 22**, a ballot initiative exempting app-based drivers from AB5. Contributions exceeded **$205 million**, making it the most expensive ballot measure in California history against roughly $19 million raised in opposition, mostly from labour groups. **It passed 3 November 2020 with 58.63% of the vote.**

Prop 22 did not leave drivers with nothing — it guaranteed **120% of the local minimum wage for "engaged time"** (driving to a pickup or with a customer) plus **$0.30 per mile** for engaged-time expenses, a healthcare stipend for those averaging 15+ hours a week, and occupational accident coverage. **The engaged-time definition is the tell: it explicitly excludes time spent waiting**, which is exactly the uncompensated category this vault's own worker-life note for the industry names as the core economic complaint. The statute that resolved the classification fight preserved the exact gap the fight was nominally about.

Litigation followed immediately. SEIU sued in January 2021; **Alameda County Superior Court Judge Frank Roesch ruled Prop 22 unconstitutional on 20 August 2021**, on single-subject and legislative-power grounds. **The California Courts of Appeal reversed most of that ruling on 13 March 2023**, severing only a narrow collective-bargaining provision. **The California Supreme Court unanimously upheld Prop 22 on 25 July 2024**, in *Castellanos v. State of California*, finding nothing in the state constitution bars voters from legislating on workers' compensation by initiative.

**This is a policy outcome, not a technology outcome, and the file should say so plainly.** The platforms had, and still have, the data to compute a courier's true realised hourly rate including wait time — the industry hub note observes exactly this. What changed between 2018 and 2024 was not what could be measured. It was who had the legal standing to decide what must be paid for.

## What's Still Open

- [[problems/gig-delivery-platforms/high-impact|🔴 The Offer Shows a Number and Not What It Is Made Of]]
- [[problems/gig-delivery-platforms/worker-life-1|🟢 The Courier Waiting Unpaid]]
- [[problems/gig-delivery-platforms/worker-life-2|🟢 The Agent Reviewing a Deactivation Appeal]]
- [[niches/gig-delivery-platforms/pay-composition-disclosure/profile|Pay Composition Disclosure]]
- [[niches/gig-delivery-platforms/earnings-and-cost-accounting/profile|Earnings & Cost Accounting]]
- [[niches/gig-delivery-platforms/offer-construction/profile|Offer Construction]]
- [[niches/gig-delivery-platforms/the-deactivation-agent/profile|The Deactivation Agent]]

## The Transferable Pattern

> **A worker's realised pay is always the platform's headline rate minus every category of time the contract defines as "not working." Find that definition before asking whether a pay model is fair, because the definition, not the rate, is where the money actually moves.**

For an FDE the operational lesson is that "the platform could compute this and doesn't" is frequently true here and is not, by itself, a product opportunity — it collided with a $205 million ballot campaign and four years of litigation before it was resolved as law, and it was resolved in the platforms' favour. [[history/crowdsourcing-platforms|Crowdsourcing Platforms]] documents the same asymmetry with no employment law anywhere near it; this industry documents what happens when the law does show up, and it is not a clean win for transparency.

**Sources:** Wikipedia, *Uber*, *DoorDash*, *Instacart*, *Dynamex Operations West, Inc. v. Superior Court*, *2020 California Proposition 22*, *California Assembly Bill 5 (2019)*; this vault's `series/eras/wave-08-mobile-gps.md` and `industries/gig-delivery-platforms.md`.
