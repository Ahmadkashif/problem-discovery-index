# The Shipping Lead Reading Twelve Routing Guides

**Industry:** [[consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Worker Life Changing
**One-liner:** The warehouse shipping lead gets a check that catches a fine before the truck leaves, instead of a list of deductions months later blamed on her floor.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #worker-facing #compliance #quick-win

## The Problem
A shipping lead at a wholesaler's distribution centre builds each retailer's shipments to that retailer's routing guide. She has to get GS1-128 carton labels in the right place, pallet heights and configurations, mixed-SKU rules, the ship notice (EDI 856) sent and matched to the cartons before arrival, an appointment booked, the right carrier on collect freight, and a must-arrive-by date that may be days after the order dropped. Each big retailer's guide runs to dozens or hundreds of pages and changes during the year. A wholesaler with twelve retailer accounts has twelve rulebooks, and the lead keeps most of them in her head. Walmart charges 3% of the cost of goods on cases that miss its on-time or in-full targets (search summary). The fines arrive months later as deductions, coded in ways the warehouse cannot trace to a particular load.

## Why It Matters to the Worker
She is blamed for the fines and rarely shown what caused them. The rules change without warning, peak season doubles the loads, and the one person who knew a retailer's label quirk may be on vacation when that retailer's order ships. The job rewards memory and punishes the one mistake in a hundred, and the stress lands on her personally.

## What a Solution Looks Like
A pre-ship check on the handheld or the dock screen. For each load it pulls the retailer's current rules and the order and ship-notice data, checks labels, pallet build, notice timing and appointment against them, and scores the risk of a fine from the history of past loads and the deductions they drew. It gives a short checklist of what to fix before the trailer door closes. Afterwards it ties each fine back to the load that drew it, so she can see the cause. The maker-side version of this contest is profiled at [[niches/consumer-products-makers/otif-routing-edi-compliance/profile|OTIF, Routing-Guide & EDI Compliance]].

## Impact If Solved
Halving compliance fines at a wholesaler paying ~$400K a year in them (estimate) saves ~$200K, and the lead stops spending ~4 hours a week reconstructing loads for the AR team's disputes (estimate).
