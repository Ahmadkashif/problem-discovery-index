# The Only Cross-Brand Reliability Record in Existence, Spent on Approving One Repair at a Time

**Niche:** [[niches/auto-repair-shops/fleet-maintenance-analytics/profile|Fleet Maintenance Management Analytics]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Line-item repair history on millions of vehicles across every manufacturer, from delivery to disposal, joined to mileage and duty cycle — a component reliability dataset no manufacturer holds and no regulator sees, used to authorise individual work orders.
**Tags:** #survival-analysis #causal-inference #change-point-detection #gradient-boosting #confidence-intervals

## The Problem
Fleet management companies manage maintenance for millions of leased and fleet vehicles. Their maintenance staff authorise essentially every repair before a shop performs it: the shop calls, describes the work, and an authoriser approves the labour hours and the parts at negotiated rates. Every one of those authorisations is captured as a structured line item — vehicle, mileage, date, component, labour operation, parts, cost.

Accumulated over decades across millions of vehicles, that is the most complete record of mechanical reliability that exists anywhere.

It is worth being precise about why nothing else compares. A manufacturer sees its own vehicles, and mostly only during the warranty period, and only when an owner brings the car to a franchised dealer. Insurers see collisions. Telematics vendors see sensor data with no repair outcome attached. Recall data records failures serious enough to be regulated. None of them observe the full service life of a vehicle, across every brand, at component level, with mileage attached, all the way to disposal. The fleet managers do, and they do it for a population large enough to compare a Transit against a Savana against a ProMaster on identical routes.

They use it for three things: authorise the repair in front of them, publish cost-per-mile benchmarks back to clients, and recommend when to replace a unit.

Those are useful and they are a fraction of what the corpus supports.

## Why Nobody Has Built This
The invoice is a per-vehicle management fee. Analytics ride along inside it as a retention feature — the quarterly benchmark report that makes the client feel well served. Nothing in the revenue model pays for a component reliability study, so nothing funds one.

The client relationship also caps the ambition. A fleet client wants to know its own cost per mile against a peer benchmark. It has not asked whether a particular engine family fails at 140,000 miles, so the question is not on anyone's list.

There is a real commercial nervousness too. A fleet manager negotiates purchase terms with manufacturers on behalf of clients. Publishing a finding that one manufacturer's transmissions fail early would complicate a relationship that is worth more than the finding — a constraint that is understandable and that leaves the analysis undone.

And the data is genuinely messy in a way that has deterred people. Labour operation codes vary by shop and by system, component descriptions are free text, the same repair is coded three ways. Cleaning it is a real project, and it has never had a sponsor.

## What to Build
**Component survival curves, by platform and duty cycle.** Time and mileage to first failure for each major component, with censoring handled properly, segmented by how the vehicle was actually used. This is the foundational artefact and it does not exist publicly for any vehicle.

**Test whether preventive maintenance does anything.** Fleets run different service intervals, and the same manager authorises both the scheduled work and the failures that follow. That is an unusually good natural experiment on a question the entire industry answers by convention — whether an interval prevents a failure, and by how much, for which component. The confounding is real and addressable; the data is not.

**Detect emerging defect patterns early.** A component failing above its historical rate on a specific platform is a change point in a time series the fleet manager watches continuously. They would see it well before a recall, on a cross-brand population, and they are not looking.

**Optimise replacement against evidence, not policy.** Replacement timing is set by lease term and rules of thumb. The corpus supports an actual expected-cost curve per platform and duty cycle, including the rising hazard that makes a late-life vehicle expensive.

**Price the authorisation.** Whether a specific quoted repair is reasonable for this vehicle at this mileage in this market is a prediction problem with millions of labelled examples, and it is currently a judgment call made on a phone.

**Sell reliability, not cost per mile.** The benchmark report says what a client spent. What a client wants to know is which vehicle to buy next, and that answer is in the same dataset and has never been packaged.

## Target Customer
VP of Fleet Analytics or Chief Data Officer at a fleet management company. The strategic argument is that the management fee is under permanent price pressure from clients who see the service as commoditised, and the reliability corpus is the one asset in the business that a competitor cannot replicate or a client insource.

## Impact If Built
Fleet purchasing decisions move billions of dollars and are made on price, residual value assumptions and brand relationships. The empirical record of how these vehicles actually hold up exists, in one place, across every manufacturer — and is used to say yes to a brake job.
