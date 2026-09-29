# Every Search and Every Lock Recorded, and No Model of What Wins

**Niche:** [[niches/mortgage-brokers/product-pricing-engines/profile|Product & Pricing Engines]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The engine sees the whole panel's pricing and every lock that follows, and returns a sorted list.
**Tags:** #gradient-boosting #logistic-regression #ml-time-series #evaluation-metrics #revenue-impact

## The Problem
A broker enters a borrower scenario and the engine returns the lenders who will lend and what each charges. The broker picks one. Pass 1 says the decision intelligence around lender selection and rate timing is almost entirely absent at the broker level, and it is right — the engine hands over a sorted list and the reasoning stops there.

The engine, meanwhile, records everything that follows. Which lender was chosen. Whether the loan locked. Whether the lock was extended, renegotiated, or fell out. How long it took to close. Whether the lender's stated turn times held. Multiply that across a very large share of originations and the result is a measurement of lender behaviour that no individual broker, and no individual lender, can assemble.

None of it comes back as a product. A lender whose price is best and whose underwriting takes three weeks longer than advertised looks identical in the results to one that closes on time — which is a real cost to the borrower and the broker, and a competitive fact the market cannot see.

## Why Nobody Has Built This
The business model points the other way. Lenders pay for placement and participation, and a product that publicly ranks lenders on execution rather than price puts revenue relationships at risk. That tension is real and it is also the reason the most valuable thing in the dataset stays unbuilt.

The engine's identity is also as infrastructure — accurate, fast, comprehensive pricing. Being right about eligibility and price is the job, and everything after the search is somebody else's system.

And attribution looks hard: a loan that fell out may have failed for reasons unrelated to the lender. That is a modelling problem, not an obstacle, and the volume is more than sufficient.

## What to Build
Model execution, not just price.

**Pull-through and cycle time by lender, adjusted for the loan.** Which lenders actually close the scenarios they price, controlling for borrower profile, product, and market conditions. This is the number brokers most need and cannot compute.

**Price-to-close, not price-at-search.** Renegotiations, extensions, and repricing at lock are where advertised pricing diverges from realized cost. The engine sees both ends.

**Lock timing.** Every search and lock is timestamped against the rate market, and the corpus supports honest guidance on how lock decisions have actually played out for comparable scenarios — a question every broker faces daily and answers by instinct.

**Scenario coaching.** Small structural changes — a different product, an adjusted down payment, a fee restructure — often move a borrower into a materially better tier. The eligibility and adjustment grids make that computable, and today the broker finds it by re-running searches by hand.

**Pipeline risk.** Given a broker's live pipeline and current rates, which loans are at risk of fallout. Pass 1 names pipeline risk explicitly as a gap, and the engine holds the inputs.

## Target Customer
Chief Data Officer or VP of Product at a product and pricing engine provider. The commercial argument is that the pricing engine category is converging on feature parity, execution data is the one asset a competitor cannot replicate, and the lender-relationship objection is manageable by selling execution analytics to lenders as much as to brokers.

## Impact If Built
Borrowers pay for lender execution failures they never see, and brokers choose lenders on advertised price because nothing else is measurable. Making execution visible reprices the market on what actually happens — and the data has been accumulating in these systems for years with nobody asking it anything.
