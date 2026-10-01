# Which Interactions Moved the Vote

**Niche:** [[niches/sell-side-equity-research/broker-vote-attribution/profile|Broker Vote Attribution]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Analysts allocate effort across notes, calls, meetings and events with no estimate of which of them clients actually vote for.
**Tags:** #causal-inference #gradient-boosting #linear-regression #confidence-intervals #evaluation-metrics #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to show, client by client, which research interactions earned the vote — and whoever measures that best directs analyst effort and defends commission share where research is still paid through execution.

## The Problem
Vote results per client per period are known; the interactions that preceded them are partly known; the link is guessed. Analysts default to volume.

## Why Nobody Has Built This
Two votes a year per client gives a short panel; analysts call clients who already rate them, so naive correlations overstate the effect of calls; and CRM logging is incomplete.

## What to Build
A client–analyst panel of interactions and vote points, models of vote change with adjustment for prior relationship and client size, effects reported with intervals by interaction type, and per-analyst guidance delivered privately before each vote period.

## Target Customer
Heads of research sales and directors of research at brokers paid mainly through commissions, especially in the US.

## Impact If Built
Effort shifts toward the interactions voters reward, and the department sees vote risk before the spreadsheet arrives.
