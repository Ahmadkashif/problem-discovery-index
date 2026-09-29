# A Recommender That Is Also an Allocator

**Niche:** [[niches/digital-audio-platforms/recommendation-and-discovery/profile|Recommendation & Discovery]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The recommender decides what is streamed, streams decide who is paid, and the objective it optimises is engagement.
**Tags:** #matrix-decompositions #contrastive-learning #markov-decision-processes #evaluation-metrics #confidence-intervals #causal-inference #revenue-impact #transformers
**Contested on:** Every serious competitor in this niche is fighting to surface the right track from a catalogue receiving a hundred thousand arrivals a day, against an objective that reliably favours what is already familiar.

## The Problem
In a pro-rata system, exposure is income. The recommender allocates exposure, which means it allocates money, and it does so by optimising listening engagement — an objective that favours the familiar, the already-popular and the safely similar. A hundred thousand new tracks arrive every day into a system structurally biased against them. No platform treats its recommender as an economic mechanism, reports the concentration of exposure it produces, or measures what a new release's realistic chance of being heard actually is.

## Why Nobody Has Built This
Recommenders are evaluated on listening outcomes, so the economic consequence sits outside the team's objective function entirely — a system optimised for one metric has no representation of what that optimisation does to third parties. Cold start is genuinely hard at this catalogue size. Exposure concentration is uncomfortable to publish. And the artists affected have no visibility and no standing.

## What to Build
Treat exposure as the allocation it is. Report exposure concentration across the catalogue, which is the core and is the number that makes the recommender's economic role visible. Solve cold start deliberately with structured exploration, since a new release's entire commercial life depends on early exposure and the current system gives it almost none. Optimise for listener satisfaction over a longer horizon rather than immediate engagement, because familiarity wins the short horizon and discovery wins the long one. Model the recommender's causal effect on a track's performance, which is also what content valuation elsewhere needs and is entirely unmeasured. Give new and niche material a guaranteed exploration allocation, as the cost is small and the alternative is a self-fulfilling concentration. Measure what a new release's realistic exposure distribution looks like and publish it, since artists are making investment decisions in ignorance of it. Balance personalisation against breadth, because a listener served only what they already like is a retention risk as well as an artistic one. Separate editorial placement from algorithmic exposure in reporting, as they behave differently and are conflated. Evaluate against long-horizon retention rather than session engagement. And report exposure by artist tier, which will be uncomfortable and is the honest description of what the system does.

## Target Customer
Product and data leadership, artists and labels dependent on exposure, regulators examining platform allocation, and recommendation vendors.

## Impact If Built
A system optimised for one metric has no representation of what that optimisation does to third parties, and here those third parties are paid by it. Reporting exposure concentration and guaranteeing exploration for new releases makes the recommender's economic role explicit.
