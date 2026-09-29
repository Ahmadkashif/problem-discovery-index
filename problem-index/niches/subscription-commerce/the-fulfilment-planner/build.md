# Absorbing a Peak Somebody Else Created

**Niche:** [[niches/subscription-commerce/the-fulfilment-planner/profile|The Fulfilment Planner]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Subscription fulfilment arrives as a wave — everything ships in the same few days — and the planner absorbs a peak they could have smoothed if anyone had let them.
**Tags:** #convex-optimization #time-series-forecasting #evaluation-metrics #revenue-impact #worker-facing #confidence-intervals #optimization-fundamentals #automation
**Contested on:** Every serious competitor in this niche is fighting to smooth a demand wave that the business itself created — and whoever does that takes the cost out, because the peak is self-inflicted and the planner absorbing it has no authority over the thing causing it.

## The Problem
Eighty percent of the month's volume ships in five days because most subscribers were signed up on a billing cycle that renews at the start of the month. The warehouse staffs to that peak and idles for three weeks. The logistics provider charges peak rates and imposes a cut-off. Overtime is routine, errors rise under time pressure, and a missed window pushes deliveries into the following week where they become support contacts. Spreading the same volume across twenty days would cost materially less and improve quality, and the only change required is which day each subscriber is billed — a field nobody considers an operational decision.

## Why Nobody Has Built This
Billing dates were set by the sign-up flow, which anchors on the join date or on the first of the month, and nobody connected that to warehouse cost because the two functions never met. Changing an existing subscriber's billing date sounds like touching revenue timing, which finance resists. The peak cost is booked to fulfilment and the cause sits in product. And the planner, who understands it perfectly, has no forum in which to raise it.

## What to Build
Smooth the wave and attribute its cost. Assign billing and ship dates to level the daily load, for new subscribers at sign-up and progressively for existing ones, which is a scheduling optimisation with a large and immediate payoff and is the whole build — the constraint is organisational rather than technical. Model fulfilment capacity and cost as a function of the daily profile, so the saving from smoothing is quantified and the conversation with product and finance has a number in it. Offer subscribers a choice of delivery day, which is a genuine product improvement and is also the smoothing mechanism, which is the rare case where the operational fix is also a customer benefit. Migrate existing subscribers gradually with a small incentive or simply by asking, since most will not mind and the ones who do can keep their date. Attribute peak cost to the billing design in reporting, so the cause is visible where the decision is made. Forecast fulfilment load from the subscriber base and the date distribution, which gives the planner a horizon they currently lack. Include the shortfall and substitution decisions in the plan rather than leaving them to peak-day improvisation. And give the planner a seat in the sign-up and billing design, since they are the only person who understands what those choices cost.

## Target Customer
Operations and fulfilment leadership, the planners, and the product and finance functions whose decisions create the cost.

## Impact If Built
The peak is created by a billing date field nobody considers operational, and levelling it is a scheduling optimisation with an immediate payoff. Offering subscribers a delivery day of their choice is simultaneously the smoothing mechanism and a genuine product improvement.
