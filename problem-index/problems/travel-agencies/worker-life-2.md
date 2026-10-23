# The Overnight Disruption Desk

**Industry:** [[travel-agencies|Travel Agencies]]
**Type:** Worker Life Changing
**One-liner:** When a storm cancels a hub's departures, a TMC's after-hours agent faces a queue of stranded, angry business travellers and rebooks them one at a time in cryptic GDS commands, through the night.
**Tags:** #large-language-models #gradient-boosting #optimization-fundamentals #monte-carlo-methods #worker-facing #automation #workflow-orchestration

## The Problem
A travel management company runs a 24/7 service desk for its corporate clients. On a normal night it handles lost bookings, late check-ins and the occasional missed connection. When a winter storm or thunderstorm line shuts down a hub, thousands of flights can cancel in a day (estimate), and the desk receives several times its normal volume at once (estimate). Each caller needs a seat on a flight that still exists, under their company's travel policy, often with a hotel for tonight and a car tomorrow, while the airline's own rebooking may already have moved them to a flight that doesn't work.

The agent works in a GDS terminal, often in cryptic commands, checking availability across carriers, fare rules for the exchange, policy limits and whether a seat will hold long enough to ticket. Options that look valid on screen fail: the connection is too tight to make in practice, the alternate airport has no rental cars left, the "protected" seat was released. NDC bookings complicate it further, because a ticket bought through an airline's NDC channel may not be changeable from the same screen as everything else.

## Why It Matters to the Worker
These agents work nights, weekends and holidays, and the worst nights arrive without warning. Every caller is stressed, many are rude, and the agent absorbs it for hours while knowing the queue behind them is growing. Mistakes — a reissue that breaks a fare rule, a hotel booked in the wrong city — come back weeks later as a debit memo or a complaint with the agent's name on it.

The skill that makes a good disruption agent is hard-won: knowing which reroutes actually work, which airlines will protect a passenger on a partner, which airport hotels still have rooms at midnight. It is learned on the worst nights, which is also when newer agents burn out and leave.

## What a Solution Looks Like
Before the agent picks up, an assistant has already read the traveller's itinerary, policy and the airline's current rebooking, generated ranked alternatives with the realistic chance each connection is made, checked seat availability and fare-rule consequences, and held a hotel near the new departure point. The agent reviews, adjusts and confirms in a few keystrokes; the traveller receives the new itinerary by message; the exchange is pre-checked for fare-rule errors before ticketing. Proactive outreach to travellers whose flights are likely to cancel takes calls off the queue before they arrive.

## Impact If Solved
Cutting handling time per disrupted traveller from ~15-20 minutes to ~5 (estimate) shortens the worst nights by hours, reduces the debit memos that land on individual agents, and makes the after-hours desk a job people can stay in.
