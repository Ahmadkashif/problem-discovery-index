# Fix: The Unpaid Time Is Nobody's Number

**Niche:** [[niches/crowdsourcing-platforms/the-crowdworker/profile|The Crowdworker]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every platform reports what a worker earned and none reports how long they were logged in to earn it.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #data-integration #worker-facing #quick-win #compliance
**Contested on:** Whether the platform will report session time alongside earnings.

## The Problem

A worker's dashboard shows earnings by day, week and month. It does not show time. So the number every worker most needs — earnings divided by hours — cannot be computed from anything the platform provides, even approximately.

The platform has it. Session start and end, task accept and submit timestamps, page views, idle detection. A session-level time figure is available at essentially zero cost and would let any worker compute a rate within a rounding error of the truth.

The absence has a consequence beyond the individual: the public argument about what this market pays is conducted with academic estimates from instrumented studies of small samples, because the only party with the complete data does not publish it.

## Why It's Still Broken

Reporting time makes the rate computable, and the computed rate is a number nobody at the platform wants attached to their service. Earnings alone read as income; earnings over time read as a wage.

There is a technical quibble that gets used: session time overstates work time because a worker may be logged in and doing something else. That is true, it is handleable with idle detection, and a figure with a stated definition is far better than no figure.

And the party who wants it has no leverage.

## What a Fix Looks Like

Report the time. It is a timestamp subtraction.

Show session duration alongside earnings on the worker's dashboard, with a stated definition — active session time with idle periods excluded above a threshold. Daily, weekly, monthly, matching the earnings view.

Compute the rate and display it. Earnings divided by active time, per period. The worker will compute it anyway the moment the time is available; showing it is honest and saves them the arithmetic.

Break it down by requester and task type. Which requesters and which task types produced the best real rate for this worker. This is a group-by over the same data and it is the most immediately actionable output.

Separate paid from unpaid time where the platform can. Time inside a task versus time browsing, searching or reading instructions. The split is the finding and the platform can see both.

Report the aggregate publicly. Median realised hourly rate on the platform, by task type and worker region, updated periodically. A platform that publishes this before someone publishes it about them is in a materially better position, and the academic segment has already demonstrated that being able to point at a decent number is commercially useful.

And give it to requesters too, since the same measurement drives the pricing fix — one computation serving both sides.

## Who Feels the Pain

Workers, unable to compute their own wage from anything their platform provides, and allocating their evenings on guesswork. Researchers, reconstructing from instrumented studies what the platform could report exactly. Ethics boards and requesters trying to comply with pay standards they cannot verify. And the platform, whose public characterisation rests on external estimates it declines to correct with its own data.

## Impact If Fixed

The number this market is argued about becomes computable by the people earning it, from a timestamp subtraction. Workers can direct their time at what actually pays. And the platform gains the ability to state what it pays, which is a claim worth having in a market where the academic segment has already shown that better treatment is a competitive position.
