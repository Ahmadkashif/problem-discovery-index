# Fix: All of It Arrives Three Weeks Before the Audit

**Niche:** The Engineer Supplying Evidence
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Evidence collection is continuous in principle and in practice arrives as a surge of requests immediately before the audit, into sprints that were already committed.
**Tags:** #evaluation-metrics #time-series-forecasting #workflow-orchestration #worker-facing #compliance #confidence-intervals
**Contested on:** Whether the residual evidence work reaches engineers as a specific, contextualised, one-off task or as recurring interruption.

## The Problem

The platform collects evidence continuously. The residue that needs a human does not, because nobody chases it until there is a deadline.

So three weeks before the audit the compliance manager works through the outstanding items and raises forty tickets across six teams, all urgent, all due before the auditor arrives. Teams that committed to a sprint two weeks earlier absorb it, or do not, and the compliance manager spends the intervening period escalating.

The surge is entirely avoidable. Most of the requests were knowable months in advance — the same items were outstanding in month three as in month eleven. Nobody raised them then, because there was no forcing function, and compliance managers are short-staffed enough that work without a deadline does not happen.

The cost is not only the hours. It is that compliance arrives in engineers' lives exclusively as an emergency, always disruptive, always at the worst moment, always from outside. That shapes the relationship permanently, and it is why a function that depends on engineering cooperation has so little of it.

## Why It's Still Broken

**Nothing forces the work before the deadline exists.** An outstanding evidence item with no due date is not urgent for anyone until the audit gives it one.

**Compliance teams are too small to chase continuously.** One or two people covering several frameworks handle what is urgent, and nothing else, which is a capacity constraint rather than a choice.

**Engineering has no visibility of what is outstanding.** The list lives in the compliance platform, which engineers do not have access to. They cannot work ahead on something they cannot see.

**Audit dates are known and not planned against.** Everyone knows when the audit is. Nobody builds a collection schedule backward from it, so it is handled as an event rather than as a project.

**The surge is normalised.** It happens every cycle, everyone expects it, and its predictability has made it feel inevitable rather than fixable.

**Nobody owns engineering's compliance capacity.** No one is accountable for how much engineering time compliance consumes or when, so there is no party whose job it is to smooth it.

## What a Fix Looks Like

**Make outstanding items visible to the owning team, continuously.** A view per team showing what evidence is outstanding for their services, with target dates spread across the period. Visibility alone converts an invisible obligation into something a team can schedule.

**Schedule backward from the audit date.** A collection plan with monthly targets, built when the audit is booked. This is basic project management applied to something currently treated as an event, and it costs an afternoon.

**Put evidence items into the engineering backlog.** Not as an urgent external ticket but as a normal item with a sensible due date, entering the planning process like any other work. Teams accommodate planned work and resist interruption, and this is the difference between the two.

**Distribute across the year deliberately.** Quarterly evidence cycles per team rather than one annual surge, so each team's exposure is a few hours four times a year rather than a crisis once.

**Measure and report the engineering hours consumed.** Somebody should be able to state what compliance costs engineering annually. Without the number there is no case for automating the recurring items, and the number is likely large enough to fund substantial automation.

**Automate whatever recurred last cycle.** Any evidence item supplied manually in two consecutive cycles is an automation candidate. Working through that list once would permanently shrink the surge.

**Give compliance a named engineering partner.** One person in engineering who owns the relationship and can plan the work into team capacity, which is the organisational fix that makes the scheduling one possible.

## Who Feels the Pain

The engineer, whose committed sprint is disrupted by urgent requests about work they consider unrelated to their job, every cycle, predictably.

The compliance manager, escalating for three weeks, having chased nothing for the previous eleven months because they had no capacity to.

Engineering managers, absorbing an unplanned load that was entirely forecastable and that nobody forecast.

And the compliance function's standing, which is set by this experience and is why the next request gets a worse reception than the last.

## Impact If Fixed

Backward scheduling from a known audit date is free, takes an afternoon, and converts a recurring emergency into planned work — which is most of the fix.

Making outstanding items visible to the owning team lets engineering work ahead on something they currently cannot see, which is the cheapest possible way to smooth the load.

And counting the hours would establish, for the first time, what this actually costs — which is the number that would justify automating the recurring items and end the surge permanently rather than merely rescheduling it.
