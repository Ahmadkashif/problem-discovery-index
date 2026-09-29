# What Moving a Player Actually Costs

**Niche:** [[niches/game-user-acquisition-firms/cross-promotion-allocation/profile|Cross-Promotion & Portfolio Allocation]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The cheapest acquisition channel a publisher has is allocated by negotiation and priced at zero.
**Tags:** #causal-inference #optimization-fundamentals #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #gradient-boosting #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to decide which of its own games should send players to which others, when the cost of moving a player between titles has never been measured — and whoever measures it takes the account.

## The Problem
Cross-promotion moves players between a publisher's own titles at almost no media cost, which makes it look free. It is not. The player leaving a game they were engaged with may have continued to spend there; the destination may suit them poorly; and a badly targeted transfer can lose the player entirely. The allocation is decided by which team needs installs, and the real economics of each transfer have never been estimated.

## Why Nobody Has Built This
Internal inventory has no price, so nobody computes its value. The counterfactual — what the player would have done had they stayed — is unobserved. Game teams have conflicting interests and no shared measurement. And the channel appears to work because the installs are free.

## What to Build
Estimate the counterfactual and price the internal inventory. Estimate what a transferred player would have been worth had they stayed, using matched players who were not shown the promotion, which is the core and is what turns a free channel into a decision. Measure destination fit rather than assuming a player is worth the same everywhere, since matching player to title is where the available gain concentrates. Model the portfolio-level outcome rather than each game's installs, which is the only frame in which the question has a right answer. Price internal inventory so allocation is an economic decision rather than a negotiation. Run holdouts on cross-promotion placements routinely, as they are cheap here and settle the cannibalisation question directly. Identify players who are poorly served by their current title, which is where a transfer genuinely creates value. Avoid promoting to players in a high-value state in the source game, which is the clearest mistake and is currently made constantly. Report each transfer's net portfolio effect rather than the destination's install count. Handle the timing of the promotion within a player's lifecycle, which changes the counterfactual substantially. And give the two game teams a shared number, since the argument is otherwise unresolvable.

## Target Customer
Publishers with portfolios, portfolio and cross-promotion managers, UA leadership, and portfolio analytics vendors.

## Impact If Built
The cheapest channel a publisher has is priced at zero, so nobody computes what a transfer costs. Estimating the counterfactual with matched holdouts turns a negotiation into an economic decision.
