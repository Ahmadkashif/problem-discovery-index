# Fulfilment Planner on the Monthly Wave

**Industry:** [[subscription-commerce|Subscription Commerce]]
**Type:** Worker Life Changing
**One-liner:** Subscription fulfilment arrives as a wave — everything ships in the same few days — and the planner absorbs a peak they could have smoothed if anyone had let them.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #confidence-intervals #evaluation-metrics #convex-optimization #workflow-orchestration #worker-facing

## The Problem
Subscription billing and shipping cluster. Most subscribers are charged and shipped on the same few days each month, which produces a fulfilment peak several times higher than the average day.

The planner sizes labour, warehouse capacity and carrier pickups for the peak. Temporary staff are hired and trained for a few days a month. Third-party logistics providers price the peak accordingly. Errors rise during it because the operation is running at capacity with less experienced staff.

Forecasting the wave is harder than it should be. Active subscriber count is known, but skips are not confirmed until close to the ship date, swaps change what needs picking, new sign-ups arrive continuously, and cancellations reduce the number after the plan is made. The planner works with a number that firms up days before the peak.

Then the variable content problem compounds it. In a curated subscription, what goes in each box is decided per subscriber, so the pick list is not one item times fifty thousand but a different combination per customer, which is a substantially harder warehouse operation.

## Why It Matters to the Worker
The rhythm is punishing and entirely artificial. The peak exists because billing dates cluster, and billing dates cluster because that is how the system was set up, not because customers need it. The planner absorbs an operational problem created by a product decision nobody revisits.

The uncertainty is the daily frustration. Planning for a number that is not final until days before means either over-staffing, which is visible waste, or under-staffing, which means late shipments and a support spike. The planner is criticised for both.

The peak also concentrates errors, and errors in a subscription are worse than in ordinary commerce because the customer is evaluating whether to continue. A mis-picked box in cycle two contributes to a cancellation in cycle three, and the planner sees the error rate without seeing that consequence.

Temporary staff management is a recurring burden — hire, train and lose the same roles every month, with quality that never improves because nobody stays.

## What a Solution Looks Like
Smoothing the wave, which is a product change with an operational payoff. Distributing billing and ship dates across the month reduces the peak dramatically, and the objection — that customers expect a fixed date — is testable and probably overstated for most categories.

Accurate demand forecasting for the wave that remains. Skip probability per subscriber is predictable from their own history, and a forecast that accounts for it is far better than the active subscriber count minus a historical skip rate.

Pick optimisation for variable contents. Once contents are decided, batching and routing the pick is a real optimisation problem, and warehouse systems designed for uniform orders handle it badly.

Content decisions made earlier. Much of the planning difficulty comes from box contents being finalised close to the ship date, and deciding earlier — with a mechanism for late changes — would give the operation a week it does not currently have.

Error consequence measurement, so that a mis-picked box is understood as a retention event rather than as a warehouse statistic.

## Impact If Solved
The monthly peak is an artefact of billing design that costs a permanent capacity premium, degrades quality at the worst moment, and makes the planning role reactive. Smoothing it and forecasting the remainder properly is one of the rare operational changes that improves cost, quality and the working experience simultaneously.
