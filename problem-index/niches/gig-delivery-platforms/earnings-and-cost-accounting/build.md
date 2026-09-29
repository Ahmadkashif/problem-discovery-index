# Build: A Defensible Net Earnings Ledger

**Niche:** [[niches/gig-delivery-platforms/earnings-and-cost-accounting/profile|Earnings, Pay & Cost Accounting]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Build the per-courier ledger that joins earnings, engaged time, online time and dispatched mileage, so net earnings per hour is a computed figure rather than a contested estimate.
**Tags:** #descriptive-statistics #confidence-intervals #evaluation-metrics #compliance #data-integration #hypothesis-testing #revenue-impact #worker-facing
**Contested on:** Whether the platform will build the ledger that makes its own earnings claims checkable.

## The Problem

Nobody can say what gig couriers earn. Studies produce figures that differ by more than a factor of two, platforms quote gross per-hour numbers with unstated denominators, worker organisations quote net figures with different assumptions, and the argument runs for years without converging because the underlying quantities are never assembled in one place.

Inside the platform they exist as separate records: payments by delivery, engaged intervals from the dispatch system, online intervals from the app session log, and route distances from the routing service. Nothing joins them into a per-courier, per-period ledger with a stated methodology, so even the platform's own answer to "what do our couriers earn per hour" depends on which team you ask.

## Why Nobody Has Built This

A defensible ledger is a checkable claim, and checkable claims constrain marketing. Recruitment materials quoting an hourly figure benefit from an unstated denominator.

The definitional question is genuinely contested and has been used to defer the work. Engaged time — accepted to delivered — excludes the waiting between offers, which is real working time for someone who is logged in and available. Online time includes it but also includes a courier who is parked and unavailable. Both are defensible, they differ substantially, and there is no neutral answer. The correct response is to compute both and state which is which, and the availability of the argument has instead functioned as a reason to compute neither publicly.

Mileage is the third gap: platforms dispatch routes and have the distance, but attributing deadhead miles requires deciding whether the drive between deliveries belongs to the platform that dispatched the next one, which in a multi-app world is genuinely ambiguous.

## What to Build

A per-courier ledger with an explicit, published methodology.

**Join the records.** Per courier, per period: gross earnings decomposed by component, engaged time from acceptance to completion, online-and-available time, dispatched route distance including the leg to each merchant, and deliveries completed. All four are instrumented; the work is the join and the definitional discipline.

**Compute both rates and say so.** Earnings per engaged hour and per online hour, reported side by side with definitions. A single number with an unstated denominator is the source of the entire public confusion, and publishing both ends it at negligible cost.

**Handle mileage properly.** Report total dispatched distance and, separately, the deadhead legs. Where a courier is multi-apping, the platform can only claim the miles it dispatched, and saying so is more honest than the alternatives. A deduction-ready log falls out of this directly.

**Attach costs as a stated assumption, not as a fact.** Publish net figures at a standard per-mile rate with the rate stated, and let the courier substitute their own. The objection that costs vary is correct and is handled by transparency about the assumption, not by silence.

**Report the distribution, not the mean.** Median, quartiles and the bottom decile of earnings per engaged hour, by market and daypart. The mean is the least informative statistic here and the one most often quoted. The bottom decile is what minimum earnings standards are actually about.

**Make it the compliance spine.** Where a jurisdiction sets a floor, this ledger is the reconciliation record: what was earned, over what engaged time, whether the floor was met, what top-up was paid. Platforms currently build this per jurisdiction as a bolt-on. Building it once, properly, turns a compliance cost into a capability.

## Target Customer

Platform finance and compliance leadership, most urgently in jurisdictions with minimum earnings standards where the reconciliation is already mandatory and currently implemented as a fork per market. The strategic argument is that a platform which publishes a methodology-stated distribution sets the terms of the public argument instead of receiving them.

## Impact If Built

The most persistent factual dispute about this industry becomes answerable from records. Compliance reconciliation runs off one ledger instead of a fork per jurisdiction. Couriers get a deduction-ready mileage log and a net figure with a stated basis. And the platform can answer, precisely, a question it is asked constantly and currently deflects.
