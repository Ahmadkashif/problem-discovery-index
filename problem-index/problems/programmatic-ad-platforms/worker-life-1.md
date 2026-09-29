# The Trader Who Babysits Pacing

**Industry:** [[programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Worker Life Changing
**One-liner:** Media traders spend their days dragging budget sliders between line items to hit a delivery number, and the work they were hired for — deciding what the campaign should actually do — happens in whatever time is left.
**Tags:** #time-series-forecasting #exponential-smoothing #markov-decision-processes #gradient-boosting #convex-optimization #evaluation-metrics #worker-facing #automation

## The Problem
A media trader at an agency or a DSP's managed service desk runs somewhere between fifteen and sixty live campaigns. Each has a budget, a flight window, a delivery obligation and a performance goal, and each is split across line items by channel, geography, audience and format. The daily job is to keep every one of them pacing: check which are under-delivering and which are burning too fast, shift budget between line items, adjust bids, pause what is not working, unpause what might.

It is done in a UI, by hand, against a dashboard that updates hourly. Monday mornings are spent recovering from the weekend, when nobody was watching and a line item either spent its week's budget in a day or spent nothing. Month-end is worse, because under-delivery means a make-good and over-delivery means an unbillable overspend, and both land on the trader. Quarterly, a large brand's campaign will have a flight that starts on a holiday or a creative that arrives late, and someone reforecasts the whole thing manually in a spreadsheet.

## Why It Matters to the Worker
None of this is the job the role describes. Traders are hired to understand a client's business and translate it into a media strategy — which audiences are worth reaching, what a frequency cap should be, when to move budget out of a channel that has stopped working. That thinking is what distinguishes a good trader from a bad one and what a client is actually paying for, and it is what gets squeezed, because pacing is urgent and strategy is not.

The failure mode is personal and visible. An under-delivered campaign is a conversation with the client at month-end, and the trader is the person in that conversation regardless of whether the shortfall was caused by a creative that arrived nine days late or a supply source that went dark. Traders carry too many accounts to catch everything, so the ones that get caught are the ones that were looked at, which makes the whole thing feel arbitrary. Turnover in trading desks is high and concentrated in the first two years — long enough to learn the tooling, not long enough to become good at the part that is interesting.

## What a Solution Looks Like
Pacing forecast rather than pacing dashboard. Delivery is a forecastable series with known structure — day-of-week, holidays, supply seasonality, creative rotation, competitive pressure in the auction — and a model that projects each line item to end-of-flight with an interval turns the daily scan into an exception list. A trader should open the morning to *these four campaigns will miss, here is why, here is the reallocation that fixes it*, not to sixty rows to read.

Budget reallocation proposed, not executed silently. The allocation across line items under a delivery constraint and a performance goal is a constrained optimisation the machine should solve and the human should approve, because the constraints that matter most are the ones not in the system: a client who will not accept spend in a channel, a brand moment, a promise made on a call.

And the reforecast has to be automatic. When a creative lands late or a flight is cut short, the plan should reshape itself and show what it did, rather than being rebuilt in a spreadsheet by whoever has capacity.

## Impact If Solved
Pacing consumes the majority of a trader's day and produces nothing a client values. Moving it to exception handling gives the desk's most expensive judgment back to the accounts that need it, and reduces the make-goods and unbillable overspend that come from campaigns nobody had time to open. It also changes what the job is in year two, which is the difference between a trading desk that retains people and one that trains them for someone else.
