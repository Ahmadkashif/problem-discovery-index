# Build: A Prioritised Daily Work Queue Across Four Systems

**Niche:** [[niches/rideshare-fleet-operators/the-fleet-manager/profile|The Fleet Manager]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Join telematics, payments, maintenance and contracts into one driver-centric view, and rank what needs attention today by what it costs to leave it.
**Tags:** #gradient-boosting #descriptive-statistics #confidence-intervals #evaluation-metrics #workflow-orchestration #data-integration #worker-facing #automation
**Contested on:** Whether the day's priorities can be ranked by expected cost rather than by whatever rang last.

## The Problem

A fleet manager's morning has forty things in it: six drivers behind on payments, four vehicles due service, two cars sitting idle awaiting renters, a driver reporting a noise, a registration expiring, a repossession agent to brief, three prospective renters to screen, and an owner asking why utilisation is down.

The information needed to rank them lives in four systems that do not talk. Which of the six arrears is likely to cure. Which of the two idle cars has a renter approved and waiting. Which service is urgent and which can wait a fortnight. Which prospective renter should be prioritised because a vehicle is coming back Thursday. The manager holds a rough version of this in their head, under interruption, and gets it approximately right on good days.

The consequence is not just inefficiency. It is that the highest-cost items are frequently not the loudest ones, and the loudest ones get handled.

## Why Nobody Has Built This

The category's software is organised by object — vehicles in the telematics product, contracts in the fleet system, invoices in the accounting package — because that is how the vendors' markets were defined. Nobody sells a product organised around the fleet manager's day, because the fleet manager is not the buyer and the operator buys systems of record.

The integration is also genuinely fiddly: several APIs of varying quality, a payment processor, a maintenance record that may be paper, and a contract system that may be a folder. For a small operator that is a real project with no obvious owner.

And the prioritisation needs a cost model — what does it cost to leave this until tomorrow — which requires the carrying-cost and arrears-cure work that nobody has done either.

## What to Build

A driver-and-vehicle operations layer over the existing systems, with a ranked queue as its main screen.

**Consolidate into a driver view.** One page per driver: their vehicle, telematics summary and trend, contract and rate, payment status and history, maintenance state, communication log, and documents. Most of a manager's questions are answered by this page existing, and today they require four logins.

**Rank the day by expected cost of delay.** An idle vehicle costs its carrying cost per day. An arrears case costs the expected unrecovered balance, weighted by how the cure probability decays with time. A due service costs the difference between doing it in a scheduled gap and doing it after a roadside failure. A renter in the pipeline unscreened costs the idle days their vehicle will wait. These are all computable once the cost model exists, and ranking by them reorders the day substantially — typically pushing pipeline and idle-vehicle work above collections, which is the opposite of what happens now.

**Automate the routine contact.** Payment reminders, document expiry notices, service booking, inspection scheduling — templated, logged, and handled without the manager. A large share of the phone calls are informational and do not need a person.

**Log every interaction.** Calls, texts, agreements, promises, concessions. This is the institutional memory the operation currently keeps in one person's head, and it is the difference between a fleet that can add a second manager and one that cannot.

**Surface the leading indicators in the same place.** Drivers whose hours are falling, vehicles approaching a duty-cycle threshold, contracts predicted to end soon, market-level payment trend. These are the items that never make it onto a reactive day and are where the avoidable cost lives.

## Target Customer

Fleet operators between roughly thirty and three hundred vehicles — large enough that one person cannot hold it and small enough that they have not built anything. Also the fleet management software vendors, for whom a driver-centric operations layer with a prioritised queue is the obvious product on top of the data they already hold.

## Impact If Built

The manager's day gets ranked by what it costs rather than by what rang, which reorders it toward the work that prevents next week's problems. Routine contact stops consuming a person. The fleet's institutional knowledge becomes a record. And the operation can grow past the point where one person can remember it, which is where these businesses currently stop.
