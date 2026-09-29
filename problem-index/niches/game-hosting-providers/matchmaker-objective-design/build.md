# Policy Instead of Weights

**Niche:** [[niches/game-hosting-providers/matchmaker-objective-design/profile|Matchmaker Objective Design]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The matchmaker decides greedily, one match at a time, against a scoring function rather than a policy.
**Tags:** #optimization-fundamentals #markov-decision-processes #dynamic-programming #convex-optimization #evaluation-metrics #confidence-intervals #hypothesis-testing #numerical-methods
**Contested on:** Every serious competitor in this niche is fighting to turn measured experience costs into a matchmaking policy that runs in milliseconds against a live queue — and whoever builds that policy engine takes the account.

## The Problem
Most matchmakers work greedily: take the players currently waiting, score candidate groupings against a weighted function, form the best available match, repeat. This is locally sensible and globally poor — holding one player for twenty more seconds can improve three subsequent matches, and the greedy algorithm cannot see that. Search bands expand on a timer rather than on a model of who is likely to arrive. The whole layer runs on heuristics that were never posed as an optimisation problem.

## Why Nobody Has Built This
The real-time constraint is genuinely tight and rules out most textbook approaches. Any change risks a visible regression in queue times. Nobody has the measured costs to optimise against, which is the sibling niche's output. And the current system works acceptably, which is the strongest defence there is.

## What to Build
Optimise over the queue, not over the next match. Formulate the decision as a sequential policy over the whole queue rather than a greedy per-match choice, which is the core and is where the available improvement sits. Model arrivals so the wait-versus-start decision accounts for who is likely to join, since expanding bands on a timer ignores the information the queue itself carries. Adapt the policy to population density, as the correct behaviour in a thick peak queue and a thin overnight one are genuinely different problems. Set per-mode policies rather than one global configuration, because latency tolerance and quality sensitivity vary sharply by mode. Respect a hard millisecond budget with heuristics that carry proven bounds, which is the engineering constraint that shapes everything. Handle party and group constraints as first-class, since they are the commonest source of degenerate behaviour. Run continuous holdouts so the policy is validated as the population changes rather than once at launch. Degrade predictably in thin populations instead of producing arbitrary matches. Expose the policy's reasoning for debugging, as an opaque matchmaker is untunable and blamed for everything. And make the objective a configurable input so a studio can supply its own measured costs.

## Target Customer
Multiplayer platform vendors, studios with in-house matchmaking, matchmaking service providers, and optimisation consultancies.

## Impact If Built
Holding one player for twenty more seconds can improve three subsequent matches, and a greedy algorithm cannot see that. A sequential policy over the queue with an arrival model is the formulation the layer has never had.
