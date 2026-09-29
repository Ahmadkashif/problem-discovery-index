# Two-Sided Market and Matching Theory

**Niche:** [[niches/online-marketplaces/liquidity-engineering/profile|Liquidity Engineering]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Market design is an established field with real results on matching, thickness and congestion, and marketplace operators run growth campaigns.
**Tags:** #convex-optimization #graph-theory #evaluation-metrics #probability-distributions #revenue-impact #confidence-intervals #optimization-fundamentals #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to raise the probability that a one-of-a-kind listing finds its buyer — and whoever does that takes the market, because both sides stay or leave on that number and it is worst exactly where marketplaces are most valuable.

## The Problem
How to make a market work — get enough participants on both sides, help them find each other, stop the market unravelling into early bilateral deals, and avoid congestion where everyone chases the same few options — is the subject matter of market design, with a substantial literature, real-world deployments in labour and organ exchange, and well-understood failure modes. Marketplace operators mostly reason about liquidity through growth spend and conversion rates, and rediscover thickness and congestion problems empirically.

## What Already Exists
Matching market theory with results on stability and efficiency; market thickness and congestion analysis; two-sided platform economics with pricing structure results; auction and mechanism design; and the empirical market design tradition of diagnosing why a specific market fails.

## The Customization Gap
The adaptation is to a market where the goods are heterogeneous and the preferences are not stated. It requires: (1) preferences inferred from behaviour rather than submitted, since matching theory assumes participants rank options and marketplace buyers browse — inference over a behavioural trace is the substitution and is the whole adaptation; (2) heterogeneous indivisible goods with no substitutes, which is the hard case in matching theory and is exactly the inventory in question; (3) congestion analysed at the attention level, since the failure mode here is that a few listings absorb all the views while most get none, which is a congestion result the field has language for and operators treat as a ranking outcome; (4) thickness measured per micro-market rather than platform-wide, because a marketplace is hundreds of small markets and platform liquidity is an average that hides starvation; and (5) interventions that are product changes rather than mechanism changes, since an operator cannot impose a clearing procedure on browsing consumers and must work through ranking, pricing guidance and supply acquisition.

## Target Customer
Marketplace operators, their economics and data science functions, and the market design community for whom heterogeneous consumer marketplaces are an under-served application.

## Impact If Solved
Market design has results on exactly the failures operators rediscover empirically. Thickness measured per micro-market exposes starvation that a platform average hides, and attention-level congestion analysis names a failure operators currently read as a ranking outcome.
