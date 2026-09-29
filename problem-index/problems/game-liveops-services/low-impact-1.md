# Event Calendar and Content Cadence

**Industry:** [[game-liveops-services|Game LiveOps Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Seasons escalate because each must beat the last, the calendar fills until neither players nor the team can sustain it, and nobody models fatigue.
**Tags:** #survival-analysis #time-series-forecasting #causal-inference #gradient-boosting #confidence-intervals #hidden-markov-models #evaluation-metrics #revenue-impact

## The Problem
A live game runs a calendar: seasons, limited-time events, collaborations, sales and content drops. Each is planned to hit revenue and engagement targets, and each target is set against the previous period, so the cadence ratchets. More events, larger rewards, more simultaneous mechanics, shorter gaps.

Players experience this as pressure. A game with several overlapping limited-time systems asks for daily engagement to avoid missing rewards, which converts a hobby into an obligation. The behavioural signature is well documented by players themselves: people describe playing to keep up rather than to enjoy, and then stopping abruptly. Abrupt permanent departure after sustained high engagement is a common pattern in long-running live games and it is not what a churn model trained on declining engagement is looking for.

The team experiences the same ratchet as a production treadmill, and the cadence is frequently set without anyone having established what this game's audience can actually absorb.

## What Already Exists
Live operations platforms provide event scheduling, segmentation and configuration. Publishers maintain calendars and post-event reports. A/B testing infrastructure allows event variants. Community feedback is collected by community managers reading Discord and Reddit. Some larger operators run engagement forecasting at the calendar level. Seasonal pass structures are standardised across the industry and their pacing is broadly copied rather than derived.

## The Customisation Gap
Fatigue is not modelled anywhere, and it is the variable the calendar is implicitly trading against. A model in which engagement capacity is a depleting resource — consumed by required daily activity and obligation pressure, restored by gaps — turns cadence into an optimisation rather than an escalation. The data to fit it exists: sessions, completion behaviour under time pressure, and the abrupt-departure pattern that follows sustained obligation.

The per-game customisation is large. A game played in short daily sessions by a broad audience and one played in long sessions by a committed one have entirely different absorption capacities, and the industry's tendency to copy pass structures across genres means most games are running a cadence derived from a different audience.

Event effect estimation is the second gap. Events overlap, so attributing engagement or revenue to any single one requires either staggered exposure or a model that handles the overlap — and post-event reports typically attribute the whole period to the event that was running.

And the departure pattern needs its own detection. Players who leave after sustained high engagement do not look like ordinary churn risk in the weeks before, which means the standard model misses precisely the most valuable departures. Identifying the obligation signature specifically is a different and more useful problem.

## Impact If Solved
Calendar cadence determines both the sustainability of a live game's audience and the sustainability of its team, and it is set by a ratchet nobody chose. Modelling absorption capacity per game, estimating event effects despite overlap, and detecting the obligation-driven departure pattern give a live team the evidence to argue for a calendar that is smaller — which is currently an argument with no numbers on its side.
