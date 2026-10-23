# A Load Probability on Every Booking

**Niche:** [[niches/ocean-shipping-carriers/liner-pricing-and-allocation/profile|Container Liner Pricing & Allocation]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Trade desks overbook every sailing on instinct because no system tells them which individual bookings will actually load.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to fill each sailing with the highest-paying cargo that actually turns up, and whoever earns the highest net revenue per available slot across a season of sailings takes the account.

## The Problem
Three weeks before a sailing, the desk holds bookings well above the ship's allocation and must decide how many more to accept, which to protect and which to roll. Each booking carries a different chance of loading: a long-standing retailer's contract booking is nearly certain, a spot booking taken at a rate far below this week's market is fragile, and a forwarder's block booking will shrink. Experienced trade managers carry these odds in their heads. The booking system sees every booking as equally real until it gates in or is cancelled.

## Why Nobody Has Built This
Booking and load data sit inside each carrier and never leave, so vendors cannot train on it. Revenue-management projects in liner shipping have historically been central optimisers that regional desks overrode (recalled), which left a reputation for tools that ignore commercial reality. And the market is small: ten carriers hold most capacity and the largest build in-house.

## What to Build
A model per trade that scores each booking's probability of loading on its sailing and the expected shrinkage from booked to loaded TEU. Features: customer history, lead time, rate against the week's index, amendments, competitor blank sailings and holiday calendars. A sailing-level view adds up the probabilities into an overbooking recommendation with the customers driving the uncertainty, and a decision ledger records what the desk chose and why. Grade both weekly against what loaded.

## Target Customer
Heads of trade and revenue-management leads at mid-sized and regional carriers without large in-house data teams, and embedded builds at the top lines.

## Impact If Built
A 1% lift in net revenue per slot on a carrier with ~$10B of annual freight revenue is ~$100M a year (estimate). It comes from fewer slots sailing empty after no-shows and fewer high-paying boxes rolled for low-paying ones, which is the number the commercial director is judged on.
