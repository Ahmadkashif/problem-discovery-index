# The Linear Projection That Was Never Linear

**Niche:** [[niches/game-liveops-services/economy-simulation/profile|Economy Simulation]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Fix (Pain Point)
**One-liner:** The designer projected the new reward forward in a spreadsheet, assumed behaviour would not change, and it did.
**Tags:** #quick-win #descriptive-statistics #confidence-intervals #evaluation-metrics #time-series-forecasting #causal-inference #monte-carlo-methods #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to tell a designer what the economy will look like in three months if they ship a proposed change — and whoever makes that forecast trustworthy takes the account.

## The Problem
The standard tool for evaluating an economy change is a spreadsheet row: current earning rate, plus the new reward, times the number of players, extended forward. It assumes the population does not respond — that nobody plays the new event more because it pays better, that nobody stops buying because the currency became easier to earn, that the distribution stays where it was. Every one of those assumptions fails, and the projection is wrong in the direction that matters within weeks.

## Why It's Still Broken
Nobody wrote down the assumptions — a projection whose assumptions are implicit cannot be challenged, so it is presented as arithmetic rather than as a claim about behaviour. The behavioural response is real but not measured. The sheet is fast and a model is not. And the error is discovered too late to attribute.

## What a Fix Looks Like
Make the assumptions explicit and bound them before building anything. State the behavioural assumptions on the face of the projection, which is the fix and is what makes it arguable. Bound the projection with an optimistic and pessimistic behavioural response rather than presenting a single line, since the range is the honest output. Use the game's own history of similar changes to estimate the response, because the team has run these before and never tabulated the outcomes. Project the distribution rather than the total, as the mean moves least and matters least. Check the projection against what happened after previous changes, which usually reveals a consistent directional bias. Separate the mechanical effect from the behavioural one explicitly. Project over months rather than weeks, since the compounding is the whole risk. Note which players are most exposed to the change, because the damage concentrates. Record the projection so it can be compared to reality later, which nobody currently does. And treat a spreadsheet with stated assumptions as the minimum standard rather than the maximum.

## Who Feels the Pain
Designers whose change went wrong in a way the sheet did not show; live teams firefighting a predictable outcome; players in an economy that shifted under them; and the analyst asked afterwards what happened.

## Impact If Fixed
A projection whose assumptions are implicit cannot be challenged, so it is presented as arithmetic rather than as a claim about behaviour. Stating them and bounding the response turns the spreadsheet into something that can be argued with before it ships.
