# Advice on the Whole Position

**Niche:** [[niches/robo-advisors/held-away-assets/profile|Held-Away Assets]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform optimises twenty percent of the client's wealth as though it were all of it.
**Tags:** #optimization-fundamentals #data-integration #evaluation-metrics #gradient-boosting #confidence-intervals #automation #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to advise on the client's whole financial position when most of it is custodied somewhere else — and whoever makes the complete picture usable turns advice from account management into planning.

## The Problem
A client has a 401(k) holding a target date fund, an old rollover IRA in three funds chosen years ago, a spouse's plan, and the platform's account. The platform builds a carefully diversified allocation for its own slice. Across the whole position the client may be heavily overweight domestic equity, duplicating exposures, or holding the platform's bond allocation alongside a workplace plan that is already conservative. The advice is locally optimal and globally arbitrary, and the platform has the aggregation feed to know it.

## Why Nobody Has Built This
Aggregation was adopted as an engagement feature, so it was built to display balances rather than to feed the optimiser — and once it lived in the net worth screen nobody moved it. Classifying external holdings into asset classes is unglamorous data work. Advising on assets the platform does not custody raises a fiduciary question. And the business is measured on assets under management, where held-away assets count only as a pipeline.

## What to Build
Make the aggregated position an input to advice. Classify every aggregated holding into asset classes and exposures, which is the core and is the unglamorous work that unlocks everything downstream. Compute the client's true allocation across all accounts, since that number is the one that matters and no client has ever been shown it. Adjust the platform's own allocation to complete the whole position rather than to be internally balanced, which is the actual advice and is what a human planner would do first. Model the workplace plan's available options, because recommending within a constrained menu is where most of the client's money actually is. Locate assets across account types for tax efficiency, as asset location is a large, mechanical and entirely unexploited gain. Identify duplicated and conflicting exposures, since they are common and obvious once the position is assembled. Handle stale and partial data honestly, because aggregation is imperfect and advice built on a broken feed is worse than none. Resolve the fiduciary scope deliberately — the platform can inform without directing, which is most of the value. Show the client the whole picture with the platform's role in it, since that is the retention argument as well as the advice one. And measure advice quality against the whole position, which is the only meaningful standard.

## Target Customer
Product and advice leadership, clients receiving locally optimal advice, workplace plan providers adjacent to the same client, and aggregation vendors whose feeds end at display.

## Impact If Built
Aggregation was built to display balances and nobody ever moved it into the optimiser. Classifying held-away holdings and completing the allocation across the whole position is what turns account management into planning.
