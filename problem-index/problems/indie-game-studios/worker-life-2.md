# The Schedule That Was Always Going to Slip

**Industry:** [[indie-game-studios|Indie Game Studios]]
**Type:** Worker Life Changing
**One-liner:** Small teams plan eighteen months, take three years, fund the difference out of savings, and the overrun kills more studios than bad games do.
**Tags:** #time-series-forecasting #survival-analysis #gradient-boosting #confidence-intervals #bayesian-inference #evaluation-metrics #worker-facing #tacit-knowledge-ml

## The Problem
Game development estimation is famously poor and indie estimation is worse, because the projects are exploratory by design — the thing being built is partly discovered during building, and the scope that emerges is larger than the scope that was planned. Overruns of two or three times the original schedule are ordinary rather than exceptional.

The financial structure makes the overrun existential. A studio funds development from savings, a modest advance, or a grant, sized against the original plan. When the schedule doubles, the money runs out before the game ships, and the responses are all bad: cut content that the game needs, ship early into a launch that will not recover, take contract work that halts the project, or continue unpaid.

Crunch follows from the same arithmetic. The deadline is now financial rather than chosen, and the only remaining variable is hours. In small teams there is no HR function, no one to escalate to, and the person imposing the crunch is usually also the person subject to it, which makes it harder to stop rather than easier.

Nobody forecasts from their own data. Task-level velocity, the rate at which new work is discovered, and how much of the remaining plan is exploratory versus known are all observable in a team's own tracker, and essentially no small studio uses them to project a completion date.

## Why It Matters to the Worker
The overrun converts a creative project into a financial emergency, and it does so slowly enough that each individual month feels survivable. People spend savings, take on debt, and work unpaid on something they still believe in, and the industry's culture treats this as ordinary rather than as a structural failure of planning.

Crunch in small teams is under-examined precisely because it is self-imposed. There is no employer to hold responsible, which is frequently taken to mean there is no problem, and the health consequences are the same regardless of who set the deadline.

And the failure is misattributed afterwards. A studio that ran out of money and shipped an unfinished game concludes the game was not good enough, when the identifiable failure was a schedule that was wrong at the start and never re-forecast. That misattribution means the next project repeats it.

## What a Solution Looks Like
Forecast from observed velocity, not from the plan. Completion date as a distribution, derived from the team's own task completion rate and — critically — from the rate at which new tasks are being discovered, is computable from any ordinary issue tracker. The discovery rate is the variable that actually determines overrun and nobody tracks it.

Re-forecast continuously and make the money visible alongside it. The decision that matters is not when the game will be done but whether the runway reaches it, and seeing those two curves together, monthly, turns a slow-motion emergency into a decision taken while options still exist.

Separate the exploratory from the known. Early-project uncertainty is genuine and a forecast should say so; late-project work is much more estimable. A forecast that reports a wide interval in year one and a narrow one in year two is honest, and is more useful than a plan that was precise and wrong.

Make scope decisions with evidence. When the forecast says the runway does not reach completion, the question is what to cut, and playtest telemetry showing which content players actually engage with is the only defensible basis for that decision.

## Impact If Solved
Schedule overrun is the leading identifiable cause of independent studio failure and is treated as an inevitability rather than a forecastable quantity. Velocity-based forecasting with a discovery rate, presented against the runway, gives a small team the one thing it never has — enough warning to make a decision about scope, funding or delay while those are still choices rather than consequences.
