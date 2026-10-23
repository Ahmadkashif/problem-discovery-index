# Port Call Optimisation Adapted to Fixed-Day Island Services

**Niche:** [[niches/ocean-shipping-carriers/jones-act-noncontiguous-trades/profile|Jones Act Noncontiguous Liner Trades]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Port-call and speed-optimisation tools save fuel on international loops; an island service must protect a fixed arrival day before it saves fuel.
**Tags:** #optimization-fundamentals #time-series-forecasting #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver an island's weekly freight on the day the island plans around, and whoever lands the most containers on the scheduled arrival day takes the account.

## The Problem
Carriers want to slow-steam to save fuel without missing the island's arrival day, and to recover schedule after mainland delays without burning excess fuel.

## What Already Exists
Port-call optimisation and just-in-time arrival tools (Portchain, Wärtsilä voyage tools, weather routers) balance speed, fuel and berth windows.

## The Customization Gap
The objective is reversed: arrival day is a hard constraint, fuel the variable. The tools must encode customers' receiving windows, island terminal labour shifts and storm-season contingency plans, and treat a missed day as a service failure rather than a cost.

## Target Customer
Fleet operations managers at noncontiguous carriers.

## Impact If Solved
Slowing by 0.5 knot when the arrival day is safe cuts fuel on that leg by roughly 8–10% (estimate, from the cube-law rule of thumb), with fewer emergency speed-ups after mainland delays.
