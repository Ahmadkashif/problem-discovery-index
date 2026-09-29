# Award Optimisation the Operations Research Field Solved

**Niche:** [[niches/procurement-spend-platforms/sourcing-category-management/profile|Sourcing & Category Management]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Awarding a multi-lot sourcing event across suppliers under capacity, diversity and risk constraints is a well-studied optimisation problem with commercial solvers, and most awards are decided by sorting a spreadsheet by total price.
**Tags:** #optimization-fundamentals #convex-optimization #combinatorics-and-counting #dynamic-programming #evaluation-metrics #confidence-intervals #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in sourcing software is fighting to remove the assembly work from a sourcing event so the category manager spends the time on negotiation — and whoever cuts specification and bid normalisation effort most takes the account.

## The Problem
An event covers forty lots across three regions with eight bidding suppliers, several of whom have offered volume discounts, bundle pricing and capacity limits. The optimal award — which combination of suppliers across which lots minimises total cost subject to capacity, a minimum number of suppliers for resilience, incumbent transition costs and any diversity requirement — is a combinatorial problem with a well-established solution method. It is decided by awarding each lot to its lowest bidder and then adjusting by judgement, which leaves value on the table in a way that is measurable and is not measured.

## What Already Exists
Combinatorial auction and award optimisation is a developed field with a substantial academic literature, and expressive bidding and optimisation-based sourcing have been offered commercially for two decades. Mixed integer programming solvers handle problems of this size routinely and are available free. The methodology for expressive bidding — allowing suppliers to bid on bundles and express conditions — is documented and proven in large industrial sourcing. The capability exists and has never reached the mid-market or the ordinary event.

## The Customization Gap
The adaptation is to a category manager rather than an operations researcher. It requires: (1) constraint elicitation in procurement language — minimum two suppliers per region, no more than 40% with any one supplier, incumbent retained for the transition period — translated into the model rather than exposed as one; (2) scenario comparison as the primary interface, since the decision is made in a room and a single optimal answer will be rejected while five annotated scenarios with their trade-offs will be discussed; (3) transition and switching costs modelled explicitly, because the theoretical optimum frequently ignores the cost of moving and the category manager's judgement is correcting for exactly that; (4) expressive bidding introduced gently, since suppliers must understand how to bid on bundles and a mechanism nobody understands produces worse outcomes than a simple one; and (5) the value of optimisation measured against the naive award, which is what justifies the effort and is currently never computed.

## Target Customer
Sourcing platform vendors, category management functions running multi-lot events, and the sourcing consultancies who have used these methods on large engagements and could deliver them routinely.

## Impact If Solved
Optimisation-based award has demonstrated substantial value in large industrial sourcing for two decades and has never been packaged for the ordinary event. The scenario framing is the adaptation that determines whether it is used, and measuring the improvement against the naive award is what makes the case each time rather than requiring the category manager to take it on faith.
