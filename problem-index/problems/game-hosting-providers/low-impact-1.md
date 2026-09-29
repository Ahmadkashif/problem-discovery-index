# The Matchmaking Trade Nobody Has Measured

**Industry:** [[game-hosting-providers|Game Hosting Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every matchmaker trades match quality against wait time against latency, the weights are set by hand, and almost nobody has measured what any of the three actually costs in whether the player queues again.
**Tags:** #bayesian-inference #markov-decision-processes #causal-inference #gradient-boosting #confidence-intervals #convex-optimization #evaluation-metrics #hypothesis-testing

## The Problem
Matchmaking is a constrained assignment problem with three objectives that conflict. A closer skill match usually means waiting longer or accepting a more distant server. A shorter queue means a looser match or a worse route. A lower-latency server means a smaller candidate pool.

The weights between these are set by hand, adjusted when something looks wrong, and defended by intuition. The reason is that queue length is immediately visible and complained about, while the cost of a poor match — a one-sided game, an early quit, a player who does not queue again that evening — is delayed and diffuse. So matchmakers drift toward shorter queues, and the resulting experience degradation is invisible in the metrics anyone watches.

Skill rating systems underneath add their own uncertainty. Ratings are estimates with variance, larger for new and returning players, and matchmakers frequently treat them as points — which produces matches that look balanced on paper and are not, particularly for the newest players whose experience matters most.

## What Already Exists
Skill rating is a mature area with well-established Bayesian systems descended from Elo, widely implemented. Platform matchmaking services from GameLift, PlayFab and Unity handle assignment with configurable rules. Latency-aware matchmaking and regional pooling are standard. Larger studios run matchmaking experiments and publish occasional analyses. Backfill, party handling and role constraints are solved engineering problems in most implementations.

## The Customisation Gap
The objective is the gap. Nearly every implementation optimises a hand-weighted combination of quality, wait and latency, and the currency that should determine those weights — the effect on whether the player has a good session and returns — is measurable from the data these systems already hold. Estimating the retention and session-quality cost of an additional thirty seconds of queue, of a skill mismatch of a given size, and of twenty milliseconds of additional latency converts the weights from opinion into exchange rates.

The per-title customisation is large and underappreciated. The tolerance for a skill mismatch differs enormously between a competitive shooter and a cooperative game; latency sensitivity differs by title genre and even by mode within a title; and queue patience differs by audience and time of day. A single set of weights across modes is wrong in most of them.

Rating uncertainty should enter the matching rather than being discarded. Matching on the distribution rather than the point, and being more conservative where the estimate is uncertain, directly improves the experience of new players — the population most likely to leave after a bad first session and the one current systems serve worst.

And the population thinning problem needs handling explicitly. At low population hours or in small regions the trade becomes severe, and the correct behaviour — wait, widen, or route further — should follow from the measured exchange rates rather than from a static rule that was tuned at peak hours.

## Impact If Solved
Matchmaking determines the quality of every session a multiplayer game delivers, and its central trade is governed by weights nobody has validated against player outcomes. Measured exchange rates between wait, quality and latency — fitted per title and per mode — would let a studio make that trade deliberately, and the new-player case alone is worth it, since the first sessions of the least-established players are where the current bias toward short queues does the most damage.
