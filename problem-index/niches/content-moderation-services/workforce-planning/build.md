# Build: Planning Against Surges, Skills and a Hazard Budget

**Niche:** Workforce Planning & Scheduling
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A planning system that forecasts event-driven surges from external signals, routes across many skill dimensions, and treats each reviewer's remaining exposure budget as a hard scheduling constraint.
**Tags:** #time-series-forecasting #change-point-detection #gradient-boosting #convex-optimization #markov-decision-processes #evaluation-metrics #confidence-intervals #workflow-orchestration
**Contested on:** Whether staffing is planned against a forecast that anticipates event-driven surges and the constraints of exposure and language, or against a smoothed volume curve.

## The Problem

A moderation operation is planned with tools that assume the work arrives the way phone calls do: smoothly, predictably, independently, with stable daily and weekly shape. It does not. Volume in this industry is driven by events — a breaking incident, a coordinated campaign, a platform change, a single item spreading — that produce sudden correlated surges concentrated in particular languages and categories, arriving in minutes.

The forecast misses these by construction. What follows is familiar: overtime, backlog, reviewers pulled from the queues they are qualified for onto the one that is burning, and severe material routed to whoever is available rather than to whoever should receive it. Decision quality falls and reviewer exposure spikes at precisely the same moment, which is also the moment when the platform's actual risk is highest.

Two further constraints make the standard tooling inadequate even between surges. The skill space is large — language, dialect, policy specialism, market context, severity clearance — and coarse routing leaves items waiting while a qualified reviewer sits idle on another queue. And the resource is not fungible in the way a scheduler assumes: a reviewer who is free is not necessarily assignable, because assignment should depend on what they have already absorbed today. No installed system represents that at all, which is why every exposure programme in the industry fights its own scheduler.

## Why Nobody Has Built This

**The incumbents have no reason to.** The contact-centre platforms are already sold into these accounts and the vertical is a small share of their revenue. Rebuilding forecasting around correlated event-driven arrivals for one vertical is a poor return for them.

**Surge forecasting needs external signals nobody has wired up.** Anticipating volume requires news, platform event calendars, campaign detection, and upstream reporting rates as leading indicators — data that exists but sits outside the workforce system and, in several cases, outside the vendor's access entirely.

**Exposure budgets have no accepted definition.** A scheduler cannot enforce a constraint that has not been defined, and defining it is the work described in [[niches/content-moderation-services/presentation-controls/profile|🎯 Presentation & Dosimetry]]. The planning system depends on a quantity that does not yet exist.

**The optimisation gets harder with every constraint.** High-dimensional skills, exposure budgets, fairness constraints, labour rules across many jurisdictions and multi-client allocation is a genuinely difficult scheduling problem, and the easy version — occupancy against a service level — is what the installed tools already do.

**The objective would have to change.** Adding exposure and slack to the objective means sometimes declining to assign available work to an available person, which reads as inefficiency in every report the operation currently produces.

**Nobody owns the joined problem.** Forecasting sits with planning, routing with operations, exposure with wellness or legal. The value is in solving them together and no single function is accountable for that.

## What to Build

**Forecast surges as a regime, not as outliers.** A two-component model: a baseline with the usual seasonality, plus an explicit surge component driven by external leading indicators — news signals, platform release calendars, upstream report rate acceleration, early virality signals on queued items. Report the probability and expected magnitude of a surge per language and category, with honest uncertainty, rather than a single smoothed number that will be wrong.

**Plan capacity the way cloud operations plans load.** A committed baseline, a trained and retained surge bench, and defined spillover paths — cross-trained reviewers, other clients' capacity, partner vendors. Capacity as tiers with different costs and activation times is a far better fit than a weekly roster, and the framing is borrowed rather than invented.

**Route across the full skill space.** Language, dialect, policy specialism, market context and clearance as real dimensions, with a matching engine that finds the best available qualified reviewer rather than the first person on a coarse queue. This alone recovers meaningful capacity that is currently idle behind routing granularity.

**Make the exposure budget a hard constraint.** Each reviewer's remaining severe-exposure budget enters the assignment decision as a constraint, not a preference. When the budget is exhausted the scheduler routes them to lower-intensity work. This is the change that makes exposure management operationally real rather than a policy nobody can enforce.

**Optimise for slack, not occupancy.** The objective should include the cost of being unable to absorb a surge and the cost of exposure, alongside throughput. High occupancy is what makes surges catastrophic and what maximises harm, and it is what the current objective maximises.

**Link hiring to forecast uncertainty.** With two- to three-month lead times and forecasts unreliable beyond weeks, hiring should be planned against scenarios with explicit probabilities rather than a point estimate, and the surge bench sized to the uncertainty rather than to the mean.

## Target Customer

Vendor workforce planning and operations leadership, where the whole system is internal, the data is already held, and the payback is visible in overtime, backlog and attrition within a quarter.

A specialist entrant is more likely than an incumbent here, because the required rebuild is deep and the vertical is too small to interest the contact-centre platforms — and the same system serves emergency dispatch and other event-driven, skill-constrained, hazard-exposed operations.

## Impact If Built

Surges stop being absorbed by the people. Today the entire cost of a missed forecast is paid in overtime, backlog and reviewers handling material they should not be handling, all at the moment when the platform most needs good decisions.

Full-dimension routing recovers capacity that already exists and is stranded behind coarse queues, which is free throughput.

And making the exposure budget a scheduling constraint is what turns every protective policy in this industry from a document into something that actually happens, because the scheduler is where all of them currently die.
