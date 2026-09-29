# History: Warehouse & 3PL

**Industry:** [[industries/warehouse-3pl|Warehouse & 3PL]]
**Primary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Secondary Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**Origin Parent:** [[origins/package-carriers/profile|Package Carriers]] · [[origins/railroads/profile|Railroads]]
**Episode Tier:** 1
**Transferable Pattern:** When two organisations each run a system that claims to be the truth about the same physical object, the integration between them is not a project you finish — it is a permanent tax, paid every time the two disagree.

## Before

A warehouse before the 1980s ran on a location ledger and a filing cabinet. Bin cards — one per SKU, hand-updated with every put-away and pick — told a stock clerk roughly where something was and roughly how much existed. "Roughly" is the operative word: the card was only as current as the last clerk who bothered to write on it, readable by one person, in one building, at one moment.

Two industries had already solved a piece of this problem, for different objects and different reasons — and this industry inherited both solutions rather than inventing its own. **Package carriers** solved *identity at the handoff*: scan the item every time it changes hands, write the scan to one authoritative system. **Railroads** solved *queryability at distance*: make a physical asset's location answerable across a network, not just legible to whoever is standing next to it. Southern Pacific and IBM ran the feasibility study for TOPS in June 1960; British Railways adopted the resulting discipline from August 1973. Warehousing needed both halves — scan-at-every-touch *and* location-queryable-from-anywhere — and got them from two different parents, decades apart, on falling hardware costs.

## The Origin Event

There isn't a single one — there are two, on different clocks, and neither is a computer.

**Legally and physically**, the modern 3PL industry has a starting gun: the **Motor Carrier Act, signed July 1 1980**, deregulating interstate trucking. Warehousing and third-party logistics grew as an adjacent capacity market once carriers could enter routes and set rates freely — someone had to hold the inventory between a now-more-flexible truck network and the customer.

**Commercially**, the first purpose-built warehouse management software has a real founding date. **Manhattan Associates was founded in 1990 in Atlanta, Georgia, by Alan J. Dabbiere**, building a product called **PkMS** — described in the company's own 1998 SEC filing as software to manage "the receipt, storage, assembly and distribution of inventory and the management of equipment and personnel within a distribution center." Manhattan converted from an LLC to a C-corporation and IPO'd on Nasdaq as **MANH on April 23 1998** *(verified against Manhattan Associates' 1998 fiscal-year 10-K)*.

Neither event is a eureka moment. A statute made the industry's shape possible; a company two years old at the time of R/3's release started selling the software to run it. This is the same pattern freight brokerage shows for the same decade: **deregulation created the market, and off-the-shelf software followed it in, on a normal product-company timeline.**

## What Became Cheap

**Knowing what you have, without walking to go look.** Before barcode scanning and networked location data, "is it in stock, and where" required a person to physically check, or to trust a bin card that might be a shift out of date. After, both questions became a query.

What did **not** become cheap, and is the spine of everything that follows: **agreement between two parties' systems about the same fact.** A 3PL and its client each run software that believes it knows how many units of a SKU exist and where. Scanning made each system's *own* belief cheap to update. It did nothing to make the two systems' beliefs the same thing.

## How It Was Actually Solved — three EDI transaction sets, and what each one admits

The mechanism is not glamorous, and that is the point: it is a message format, not an algorithm.

**EDI 940 — Warehouse Shipping Order.** A seller (the 3PL's client) transmits this to the warehouse to request, confirm, modify or cancel a shipment. It is an instruction travelling *from the client's system into the 3PL's system* — the client telling the warehouse what it believes needs to happen.

**EDI 945 — Warehouse Shipping Advice.** The warehouse's answer: what was actually picked, packed and shipped, reconciling requested quantity against fulfilled quantity. This travels *back*, from the 3PL's WMS into the client's world.

**EDI 856 — Advance Ship Notice.** Sent onward to the receiving party (a retailer, a distribution centre, an end customer) ahead of physical arrival, describing shipment contents and packaging in enough detail that receiving can scan a container ID and know what's inside without opening it. X12's 856 has existed since the standard's Version 2 release window (**1987–1989**); ASC X12 itself was chartered by ANSI in **1979**, growing out of the earlier **Transportation Data Coordinating Committee** — this industry's messaging plumbing has transportation-sector DNA in its literal committee lineage, not just in spirit.

**EDI 846 — Inventory Inquiry/Advice** is the quietest and most consequential of the four. It is how a 3PL tells a client's ERP what's on the shelf — and it is very often sent on a schedule, not continuously: a vendor might transmit it "twice daily" to indicate the state of an entire catalogue. That cadence is the whole argument in one fact. **The client's ERP is never looking at the warehouse. It is looking at the warehouse's last report.**

None of these four transaction sets required a shared database. Each is a periodic, asynchronous reconciliation between two independently authoritative systems — which is exactly why the question below has never closed.

## Who Owns the Record — the 3PL's WMS or the Client's ERP

This is the closest thing this industry has to "the contest," and it is not a fight anyone won. It's a standing disagreement, re-litigated in every new contract.

The 3PL's WMS is closer to the physical truth: it knows what a barcode scanner actually saw, in real time, on the floor. The client's ERP is closer to the business truth: it is the system the client uses to promise availability to *its* customers, plan replenishment, and close the books. Both have a legitimate claim to being "the" record, and the two disagree by construction, because the 846 that reconciles them runs on a batch schedule, not a transaction log.

The vault's own hub note for this industry records the downstream cost directly: **inventory accuracy is what loses a 3PL its client contracts**, and physical counts to fix the discrepancy are expensive and disruptive precisely *because* they are the only way to force the two records back into agreement. This is Wave 4's integration tax in its purest form here — not a one-time systems project, but a permanent, recurring reconciliation cost that never gets paid off, only serviced.

## What Became Automatable, and What Remains a Genuinely Open Problem

**Slotting** — deciding which SKU goes in which storage location to minimise picker travel — and **pick-path optimisation** — routing a picker efficiently through the locations on their pick list — are the two places this industry's own labour cost (50–70% of a 3PL's operating cost, per the vault's hub note) meets real computer science, and it is important not to overclaim what that computer science has actually delivered.

The foundational result is **H. Donald Ratliff and Arnon S. Rosenthal, "Order-Picking in a Rectangular Warehouse: A Solvable Case of the Traveling Salesman Problem," *Operations Research*, 1983** *(bibliographic details confirmed via Crossref)*. The finding, precisely stated, is narrower than it sounds: for a **single-block rectangular warehouse** with a specific aisle structure, the picker-routing problem — a structured special case of the general Travelling Salesman Problem — is solvable **in polynomial time**, not merely heuristically approximated. That is a genuine, durable result, forty years old and still cited as the base case every subsequent routing paper extends.

What it does **not** mean: that pick-path optimisation is solved in general. Multi-block layouts, mixed storage strategies, dynamic slotting, multiple simultaneous pickers and robot-assisted picking each reintroduce complexity the 1983 special case doesn't cover, and the literature since has been a steady stream of extensions and heuristics rather than a single closed solution — the same shape the vault records in its own pick-path problem note: *WMS-generated pick lists aren't optimised for a picker's current aisle position.* Slotting has the same character: not unmodelled, but continuously re-solved as demand patterns shift, which is why the vault finds that this knowledge "takes years to build for a specific facility/SKU mix."

This is the same lesson railroads already taught, on a different asset. TOPS made a boxcar's location *queryable* in the 1960s; making the **network's routing decisions actually better** was a separate, later, contested project (Precision Scheduled Railroading — an operating discipline, not a new algorithm). Warehousing has repeated the split: barcode-and-WMS visibility (know where the pallet is) arrived first and is largely solved. Slotting and pick-path *optimisation* (decide where the pallet should be, and how to walk to it fastest) is the harder, still-partial second project — and conflating "we can see the warehouse" with "we have optimised the warehouse" is the single most common overclaim in this space.

## The Trade-Off

**Real-time physical accuracy was traded for negotiated, batch-cadence agreement — and the 3PL is the one who eats the cost when the batch is wrong.**

A WMS can know, to the second, what a scanner just saw. But the contractual relationship between a 3PL and its client runs on periodic EDI exchange, not a shared ledger — no client will hand its system of record to a vendor it could switch away from next year, and no 3PL will expose its live operational database to every client's ERP. Both sides protect their own record, reasonably, and the result is a permanent, mutually-agreed information lag. When a physical count finds the discrepancy the batch report missed, it is overwhelmingly the 3PL's operational and reputational cost, not the client's, even though the disagreement was built into the integration from day one.

## What's Still Open

- [[problems/warehouse-3pl/high-impact|🔴 Dynamic SKU slotting optimisation]] — the SKU-placement problem that resists staying solved
- [[problems/warehouse-3pl/worker-life-1|🟢 Pick-path optimisation for batch and zone picking]] — the Ratliff–Rosenthal special case, still being extended forty years later
- [[problems/warehouse-3pl/low-impact-1|🟡 Inventory discrepancy detection and cycle-count targeting]] — finding which locations are most likely wrong, because the 846 cadence guarantees some will be
- [[niches/warehouse-3pl/wms-supply-chain-software-analytics/profile|WMS & Supply Chain Software Analytics]]
- [[niches/warehouse-3pl/warehouse-automation-analytics/profile|Warehouse Automation Analytics]]
- [[niches/warehouse-3pl/receiving-put-away-automation/profile|Receiving & Put-Away Automation]]
- [[niches/warehouse-3pl/billing-reconciliation-3pl/profile|Billing Reconciliation]] — the same two-systems-disagreeing shape, applied to invoices instead of inventory
- [[niches/warehouse-3pl/threepl-rollup-analytics/profile|3PL Roll-Up Analytics]]

## The Transferable Pattern

> **Before proposing an integration, ask which side's system is "closer to the truth" and which side's system is "the one the business runs on." If they are different systems, you have not found a bug to fix — you have found a permanent condition to manage, and the honest deliverable is a reconciliation cadence with a known, bounded lag, not a promise of one shared truth.**

For an FDE, this industry is a clean teaching case because the mechanism is small enough to hold in your head entirely: four EDI transaction sets, a batch schedule, and a labour cost that is the actual business problem underneath the data problem. The temptation, faced with a client complaining about inventory discrepancies, is to propose replacing the reconciliation with a single shared database. That proposal fails for the same reason it always fails in Wave 4 territory: neither party will give up owning their own record, and the resistance is not a technology limitation — it is each party correctly protecting its own leverage. The deliverable that actually ships is the one that shortens the batch window and makes the disagreement visible faster, not the one that promises to make the disagreement impossible.

**Sources:** Manhattan Associates Inc., Form 10-K405 for fiscal year 1998, filed March 31 1999, SEC EDGAR (CIK 0001056696) — founding year 1990, founder Alan J. Dabbiere, product PkMS, IPO April 23 1998; Wikipedia, *ANSI ASC X12* (chartered by ANSI 1979; predecessor Transportation Data Coordinating Committee); Wikipedia, *Advance ship notice* (EDI 856 / EDIFACT DESADV correspondence, receiving-cost reduction claim, EDI 997 acknowledgement); Stedi EDI transaction-set reference pages for X12 856, 940, 945 and 846 (transaction flow, sender/receiver roles, X12 856 versioning from 1987–1989); Crossref bibliographic record for H. Donald Ratliff and Arnon S. Rosenthal, "Order-Picking in a Rectangular Warehouse: A Solvable Case of the Traveling Salesman Problem," *Operations Research*, 1983; ShipBob company "About" page (founded 2014, Chicago, Dhruv Saxena and Divey Gulati); this vault's `industries/warehouse-3pl.md` and `problems/warehouse-3pl/*.md`; this vault's `origins/package-carriers/legacy.md` and `origins/railroads/legacy.md` (TOPS feasibility study June 1960, British Railways adoption August 1973; PSR vs TOPS distinction). *(Locus Robotics' precise founding date could not be confirmed in this session — flagged as unverified rather than asserted. The specific first-mandate date for EDI 940/945/846 adoption in warehousing could also not be pinned to a single year; treat the adoption curve as gradual through the 1980s–90s rather than a discrete event.)*
