# One Production Ledger for Every Floating Spread

**Niche:** [[niches/heavy-civil-contractors/marine-waterway-construction/profile|Marine, Port & Waterway Construction]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Marine contractors price every bid off production rates for dredges, crane barges and pile spreads that they never compare with what those spreads actually achieved on the last job in the same water.
**Tags:** #tacit-knowledge-ml #gradient-boosting #bayesian-inference #feature-engineering #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to deliver work in and over water inside the owner's navigation and environmental windows," but that fight splits three ways. Dredging is won by having a certified dredge near the work and pricing under the Corps' 125%-of-estimate ceiling. Port and marine structures are won by crane-barge and pile-driving spreads that keep berths working. Locks, dams and levees are won by pricing in-the-wet cofferdam and river-stage risk on federal megaprojects. Decomposed into contested sub-niches below.

## The Problem
A marine contractor's estimate assumes a production rate per spread: cubic yards per hour for a 24-inch cutter dredge (illustrative), tons of stone per shift for a crane barge, piles per day for a driving crew. The spread's real performance sits in DQM logs, survey volumes and cost-code time cards on the jobs it has done. Nobody puts the two side by side.

## Why Nobody Has Built This
Estimating vendors stop at the estimate, field apps at the time card, and dredge monitoring at the Corps' compliance feed. Each system belongs to a different department. Weather, tide and river-stage effects have to be cleaned out before rates compare.

## What to Build
A ledger keyed by spread, material class and site conditions that joins each bid item's assumed rate to achieved production from DQM data, surveys and cost codes, with weather and owner delays separated. On top of it sits a rate model with intervals that the chief estimator queries while bidding. A two-week demo can run on one firm's last ten jobs and NOAA tide and wave records.

## Target Customer
Chief estimators and operations VPs at marine and dredging contractors with ~$50M–$1B of revenue (estimate).

## Impact If Built
If rate error on the dominant bid item falls by a third (estimate), a contractor bidding ~$300M a year (illustrative) avoids most money-losing awards and stops leaving several points of margin on jobs it priced too safely.
