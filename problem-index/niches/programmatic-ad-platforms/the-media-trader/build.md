# Dragging Sliders in an Automated Market

**Niche:** [[niches/programmatic-ad-platforms/the-media-trader/profile|The Media Trader]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Media traders spend their days dragging budget sliders between line items to hit a delivery number, and the work they were hired for happens in whatever time is left.
**Tags:** #worker-facing #convex-optimization #time-series-forecasting #automation #workflow-orchestration #evaluation-metrics #revenue-impact #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to take the slider-dragging off the trader so they can do the judgement work they were hired for — and whoever does that changes what a trading desk is worth.

## The Problem
The trader opens eleven campaigns across three platforms. Four are underpacing, two are overpacing, one has a line item that has stopped delivering entirely. They shift budget from the overpacers to the underpacers, adjust a bid modifier, note the one that needs investigating, and move to the next account. Tomorrow they will do it again, because the shifts they made yesterday moved the system into a state that now needs correcting. This consumes most of a skilled person's day, in a market where machines make millions of decisions a second, and the decisions that actually need a human — what this campaign should be trying to achieve and whether it is working — get the remainder.

## Why Nobody Has Built This
Platforms built for a trader who wanted control and never revisited that assumption as the work became routine. Cross-platform automation would require a layer above the platforms, which none of them wants to exist. Agencies bill for hours, so the hours are not obviously a cost to the party who could remove them. And underdelivery is a visible contractual failure while wasted expertise is not.

## What to Build
Automate the loop and give the trader the decisions. Handle pacing and reallocation automatically against a stated objective, across platforms, continuously — which removes most of the day's work and is straightforward optimisation that nobody has packaged because it spans vendors. Forecast delivery ahead rather than reporting it behind, since the trader intervenes because they cannot see a shortfall forming and a forecast converts a daily scramble into a weekly check. Present the decisions that genuinely need judgement — a campaign whose objective is wrong, an audience that has saturated, a creative that has decayed, a constraint that cannot be met — which is the actual product and is what the trader was hired for. Explain every automated action, because a trader who does not understand a reallocation will turn the automation off and that is how these systems die. Keep a full audit trail with the ability to revert, which is what allows a trader to trust it in the first week. Operate across platforms as a single portfolio, since the trader's mandate is the client's budget and the platforms' boundaries are irrelevant to it. Flag conflicts between campaigns competing for the same inventory, which is invisible within any one platform and is a genuine source of waste. Measure the trader's interventions against the automated baseline honestly, which is uncomfortable and is the only way to know what human judgement is adding. Prioritise the accounts that need attention today, since a trader with forty campaigns cannot look at all of them. And report the time recovered, because that is the case for the product and the case for the desk.

## Target Customer
Agency trading desks and in-house programmatic teams, the traders themselves, and the demand-side platforms whose interfaces create the work.

## Impact If Built
A skilled person performs a mechanical optimisation loop all day in the most automated market in commerce. Cross-platform pacing against a stated objective is straightforward optimisation that nobody packaged because it spans vendors, and it returns the day to the judgement work.
