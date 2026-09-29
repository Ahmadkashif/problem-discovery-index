# The Offer Chosen for the Player and the Moment

**Niche:** [[niches/mobile-game-publishers/offer-and-bundle-configuration/profile|Offer & Bundle Configuration]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Offers are configured by hand from a handful of segments, thousands of times a day, against players whose state is fully known.
**Tags:** #gradient-boosting #optimization-fundamentals #k-nearest-neighbors #confidence-intervals #evaluation-metrics #revenue-impact #markov-decision-processes #automation
**Contested on:** Every serious competitor in this niche is fighting to choose which offer to put in front of which player at which moment, a decision made thousands of times a day by hand-written rules — and whoever automates it well takes the account.

## The Problem
A live product manager configures a bundle: these contents, this price, this segment, this window. The game knows each player's exact progression state, inventory, spending history, current blocker and session pattern — and the offer is selected from four segments and a price ladder someone set last year. The gap between what the system knows about the player and what the offer decision uses is enormous, and closing it is a well-posed and entirely tractable problem.

## Why Nobody Has Built This
Live ops tooling was built for configuration rather than for decisioning. Personalised pricing raises fairness questions the industry has avoided rather than resolved. The manual process works and produces revenue. And the team that would build it is occupied with the monetisation tests.

## What to Build
Decide the offer from player state rather than from a segment. Select contents, price point and timing per player from their progression state, inventory and history, which is the core — the game already knows exactly what the player is short of and the offer ignores it. Compose bundle contents around the player's actual blocker instead of a fixed template, since relevance rather than discount is what converts here. Time the offer to the moment of need rather than to a calendar slot, which is the single largest available gain. Personalise value rather than headline price, because personalised pricing is a reputational problem and personalised contents is not — this distinction is what makes the system deployable. Learn from declines as well as conversions, as the declined offers are most of the data and are currently discarded. Respect a welfare guardrail so the system cannot escalate pressure on flagged accounts. Cap frequency per player, since the aggregate optimum will otherwise over-serve the responsive. Hold out a control population permanently, which is how the whole system stays honest. Explain each decision to the product manager, as an unexplainable offer engine will be overridden. And let the manager set the boundaries rather than the individual offers, which is the right division of labour.

## Target Customer
Mobile publishers, live product teams, live ops platform vendors, and games monetisation tooling providers.

## Impact If Built
The game already knows exactly what the player is short of and the offer ignores it. Composing contents around the actual blocker, timed to the moment of need, is relevance rather than discount.
