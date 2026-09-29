# One Objective Instead of Two Teams

**Niche:** [[niches/mobile-game-publishers/hybrid-monetisation-balance/profile|Hybrid Monetisation Balance]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Advertising and purchases compete for the same player attention and are tuned by tests that measure one of them at a time.
**Tags:** #causal-inference #optimization-fundamentals #confidence-intervals #hypothesis-testing #evaluation-metrics #gradient-boosting #revenue-impact #markov-decision-processes
**Contested on:** Every serious competitor in this niche is fighting to set the balance between advertising and in-app purchase when the two compete for the same player's attention and every test measures only one of them — and whoever measures both together takes the account.

## The Problem
A rewarded video that grants a resource is also a purchase the player did not need to make. An interstitial that earns a fraction of a cent also interrupts a session and shortens it. The publisher runs an ad monetisation test, sees ad revenue per player rise, and ships it — while purchase revenue and retention move in the other direction on a slower timescale that the test window never covered. Two teams, two targets, one player, and no one measuring the sum.

## Why Nobody Has Built This
The organisational structure encodes the split: ad monetisation and IAP are different teams with different targets, often different reporting lines. Mediation platforms optimise ad yield alone because that is what they sell. The substitution effect is slow and confounded. And a joint objective means one team's number goes down, which nobody volunteers for.

## What to Build
Optimise the player's total contribution, not either channel. Define a single joint objective — revenue per player across both streams plus the retention effect — which is the core and is where every current test fails. Measure substitution explicitly: how much purchase revenue is displaced per unit of ad revenue gained, by segment, since the average hides that the effect reverses across the spending distribution. Run tests long enough to capture retention effects, as the interruption cost accrues over weeks and every short test is biased toward advertising. Personalise the balance by player propensity rather than applying a global configuration, which is where the largest gain sits — a likely purchaser and a never-purchaser should not see the same ad load. Model session-level attention as the constrained resource, which is the honest framing of the trade. Attribute both revenue streams to the same player identity, which is a data plumbing problem more than a modelling one. Evaluate placements by their total effect rather than their ad yield. Give both teams the same dashboard, since the shared number changes the argument. Detect configurations that win in the short term and lose over the cohort's life, as those are what ship today. And make the trade-off explicit to leadership rather than resolving it silently in favour of whoever tested last.

## Target Customer
Mobile publishers, hybridcasual studios, mediation and monetisation platform vendors, and games analytics providers.

## Impact If Built
An ad shown is sometimes a purchase not made, and no current test can see that because each measures one stream. A joint objective with substitution measured per segment is what makes the trade decidable.
