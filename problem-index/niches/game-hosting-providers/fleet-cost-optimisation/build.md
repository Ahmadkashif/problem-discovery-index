# The Same Capacity for Less

**Niche:** [[niches/game-hosting-providers/fleet-cost-optimisation/profile|Fleet Cost Optimisation]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The fleet's cost is set by decisions made once at setup and never revisited, on margins that cannot absorb it.
**Tags:** #optimization-fundamentals #revenue-impact #evaluation-metrics #confidence-intervals #gradient-boosting #automation #time-series-forecasting #convex-optimization
**Contested on:** Every serious competitor in this niche is fighting to serve the same concurrency for less money across regions, instance types and pricing models, on margins thin enough that the difference decides who wins the contract — and whoever optimises it takes the account.

## The Problem
Delivering a given concurrency can cost very different amounts depending on how many sessions share a machine, which instance family is used, which region serves which players, and what mix of on-demand, committed and interruptible capacity backs it. These are optimisation decisions with clear objectives and measurable constraints. In practice they are made once, conservatively, by an engineer at setup, and left for years while hardware, pricing and the game itself all change.

## Why Nobody Has Built This
Session density is constrained by player experience, which nobody has measured, so everyone defaults to conservative. Interruptible capacity looks incompatible with live sessions, so it is dismissed rather than engineered around. Cost tooling is generic and does not understand session workloads. And the person who could optimise it is building features.

## What to Build
Measure the real density limit, then optimise placement and pricing against it. Establish how many sessions a machine can host before player experience degrades, measured rather than assumed, which is the core — the conservative default is the single largest cost item and nobody has tested it. Evaluate instance families continuously against the game's actual performance profile rather than at setup, since the price-performance landscape moves constantly. Build an interruptible capacity strategy compatible with sessions — short-lived match types on preemptible instances with drain-on-notice — which is the largest unclaimed saving and is genuinely engineerable. Optimise the region-to-player mapping against both latency and price, as those trade against each other and nobody models the trade. Size committed capacity against the forecast distribution rather than against peak, which is where over-commitment hides. Pack sessions with headroom sized from measured variance rather than a fixed margin. Attribute cost per title, mode and region so the expensive parts are visible. Model the cost of each matchmaking policy option, since match placement and cost are coupled and treated separately. Re-evaluate on a schedule rather than on an incident. And report savings against a measured baseline, which is what keeps the work funded.

## Target Customer
Game hosting providers, studios operating their own fleets, cloud cost management vendors, and infrastructure consultancies.

## Impact If Built
The conservative session density default is the single largest cost item and nobody has tested it. Measuring the real limit, then optimising instance family, region and pricing mix against it, moves a large share of a thin margin.
