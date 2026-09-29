# The Other Half of the Event Ledger

**Niche:** [[niches/game-liveops-services/event-evaluation/profile|Event Evaluation]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An event's revenue is counted in the week it runs and its cost is never counted at all.
**Tags:** #causal-inference #survival-analysis #confidence-intervals #time-series-forecasting #evaluation-metrics #hypothesis-testing #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to measure what an event cost over the following months rather than what it earned in the week it ran — and whoever measures the cost takes the account.

## The Problem
Event evaluation in live games is structurally one-sided. Revenue is immediate, attributable and reported. The cost is delayed, diffuse and never measured: players who found an event exhausting or coercive do not complain, they reduce their play slightly and churn some months later for reasons they would describe as losing interest. Every incentive in the reporting structure therefore points toward the more aggressive event, and the accumulated damage looks like a game naturally ageing.

## Why Nobody Has Built This
The measurement horizon required is months and the reporting cycle is weekly. Attributing later churn to an earlier event requires causal work that nobody has been asked for. The team that ran the event is measured on its revenue. And the alternative explanation — the game is getting old — is always available and never falsified.

## What to Build
Extend the horizon and put a cost on the other side. Measure each event's effect on engagement and retention over the following months, not the following week, which is the core and is the entire missing half of the evaluation. Use exposure variation and holdouts to establish causation rather than correlation, since players who engage heavily with events differ from those who do not and the naive comparison gets the sign wrong. Report a net event value combining immediate revenue and long-horizon retention effect, which is the number that should govern the calendar. Identify which event designs carry the largest hidden cost — time pressure, fear of missing out, escalating commitment — as the pattern is consistent and currently unnamed. Detect the quiet disengagement that precedes churn rather than waiting for the churn itself, which is where the early signal lives. Measure the effect separately by cohort, because the aggressive event is usually paid for by the mid-tier players rather than the top ones. Keep a long-horizon record per event design so the calendar can be planned on evidence. Report the accumulated fatigue across a season rather than event by event, since the effect compounds. Show the counterfactual calendar — what a lighter schedule would have earned — as that is the decision leadership is actually making. And put the net value next to the gross on the same report, which is the change that makes the rest stick.

## Target Customer
Live game operators, live ops platform vendors, product leadership, and games analytics providers.

## Impact If Built
Every incentive in the reporting structure favours the more aggressive event because only its revenue is counted. A causally measured long-horizon retention effect puts a number on the other side of the ledger.
