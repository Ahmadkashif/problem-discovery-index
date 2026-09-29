# The Mechanism: Economic Dispatch and Unit Commitment

**Origin:** [[origins/electric-utilities/profile|Electric Utilities]]
**Tags:** #optimization-fundamentals #convex-optimization #lagrange-multipliers #dynamic-programming #time-series-forecasting #data-integration #automation #compliance #revenue-impact

> This is the file an FDE should read to see what a constrained optimisation problem looks like when it has run in production, unglamorously, since before most software existed.

## Two Problems, One Stacked on the Other

**Economic Dispatch (ED)** answers: given the generators already running, how much should each produce, this instant, to meet demand at minimum cost without violating a transmission limit anywhere on the network?

**Unit Commitment (UC)** answers a slower question underneath it: over the next hours to days, which generators should be started or stopped at all, given that starting one has a cost and takes time, and that once running it cannot be cheaply cycled off and back on?

ED runs continuously, on a timescale of minutes. UC runs on a rolling horizon, re-solved as forecasts update. **UC is a mixed-integer optimisation problem** — a binary "is this unit on" decision per generator per time step, layered under the continuous dispatch problem — and it is one of the oldest continuously-solved large optimisation problems running in any industry.

## The Decomposition

**1. Forecast load** for the next dispatch interval and the whole commitment horizon, from historical curves adjusted for weather, day type and season. Get this wrong and everything downstream solves the wrong problem precisely.

**2. Commit units ahead of need.** Decide which generators must be running, respecting each unit's **minimum up/down time** and **start-up cost**, which can be substantial for large thermal plants. This is the genuinely hard combinatorial part — a search over which subset of generators to have ready.

**3. Dispatch economically among whatever is running,** minimising total cost subject to: generation equals demand (equality), and no line, transformer or bus exceeds its physical limit (inequality). Classically solved via marginal-cost equalisation across generators — the discrete-time descendant of the same logic that prices anything scarce under a hard limit.

**4. Hold reserves.** Commit and dispatch to a margin, not to the forecast exactly, so the loss of any single major element does not itself cause further failures — **N-1 contingency planning**, a deliberate, permanent sacrifice of pure cost-minimisation for reliability.

**5. Re-solve continuously.** Automatic Generation Control makes second-by-second corrections between full re-optimisations. The system is a control loop, the same shape as [[origins/airlines/the-mechanism|DINAMO's revenue-management loop]], solving a different variable under a different constraint.

## What It Gave Up

**Exactness was traded for tractability.** Full AC power-flow physics is nonlinear and expensive at grid scale on every cycle; utilities have long used linearised (DC) approximations in the loop — usually good enough, occasionally not, and knowing which is an operating skill in itself.

**Cost minimisation was subordinated to reliability, by rule.** N-1 margins mean the system routinely runs less cheaply than the unconstrained optimum, because the optimum has no slack when something breaks — the opposite trade to yield management's fences: airlines sacrifice fairness to protect revenue; utilities sacrifice cost to protect continuity of supply.

**Situational awareness was assumed, not verified.** The dispatch mathematics has no term for "does the operator have an accurate picture of the network." [[origins/electric-utilities/the-fight|The 2003 blackout]] is what happens when that assumption silently fails while the optimisation itself keeps running correctly on stale information.

## The Transferable Pattern

> **When the product cannot be stored and the network has hard physical limits, optimisation becomes optimisation-plus-a-safety-margin, and the size of that margin is a policy choice, not a technical one. What fails is rarely the maths. It is whatever tells the operator the maths is still solving the real problem.**

**Sources:** IEEE Annals of the History of Computing, *Transitions from Analog to Digital Computing in Electric Power Systems* (2015); electricenergyonline.com, *A Brief History of Electric Utility Automation Systems*; standard power-systems literature on economic dispatch, unit commitment and N-1 contingency criteria (NERC reliability standards).
