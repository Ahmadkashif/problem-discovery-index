# Optimising Against a Number Nobody Validated

**Niche:** [[niches/app-marketing-firms/incrementality-verification/profile|Incrementality Verification]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The discipline optimises hard against a reported return that nobody has tested, in a channel where the attribution behind that number is weaker than it has ever been.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #revenue-impact #bayesian-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to establish how much of a reported return survives an experiment — and whoever does that in a channel where attribution is aggregated supplies the only number anyone can actually trust.

## The Problem
A campaign reports a strong return. That number was produced by attribution rules — which network claimed the install, under which window, with what view-through policy — layered on top of a coarse aggregated signal and a predictive model. Whether the spend caused any of those installs is a different question that the number does not address, and a substantial share of app install advertising targets people who would have installed anyway, particularly on branded and retargeting activity. The team optimises hard against the reported figure. Almost nobody has run the test that would say how much of it is real.

## Why Nobody Has Built This
Experiments cost suppressed spend and take weeks, and in a channel with aggregated attribution the design is harder than elsewhere, so the practice never established itself — the constraint that made attribution worse also made the remedy harder, which is why this gap is specific to this channel. The networks offer lift studies, which absorbs the demand without meeting it. The reported number is favourable and everyone in the chain benefits. And nobody has been asked to prove it.

## What to Build
Make incrementality testing routine here. Design geographic holdouts adapted to app store geography and platform constraints, which is the core and is more constrained than in web advertising — the design work is the product and is why teams do not attempt it. Automate the design, execution and analysis, so a test is a workflow rather than a project, which is the change that converts occasional to routine. Calculate power honestly and refuse designs that cannot detect the effect at stake, since an underpowered null in this channel is regularly read as proof a channel does not work. Test by campaign type rather than in aggregate, because branded search, retargeting and prospecting have wildly different incrementality and the blended answer is useless for allocation. Run always-on holdouts at a small allocation, which converts a project into a stream and is affordable at the spend levels in this category. Compare the experimental result against the reported return and publish the ratio, which is the single most useful number a team can have and reframes every subsequent allocation. Accumulate results across campaigns, apps and networks into priors, so a team without the volume to test can still reason from evidence. Feed the findings into bidding and budget rather than into a report. Handle the aggregated signal's limitations in the analysis, since the outcome measurement is itself constrained. And validate the prediction models against experimental results, connecting to the prediction niche, because that is the strongest available check on the whole stack.

## Target Customer
User acquisition and finance leadership, agencies accountable for client returns, and measurement vendors whose products stop at attribution.

## Impact If Built
The constraint that made attribution worse also made the remedy harder, which is why this channel tests least and needs it most. Automating design and execution converts a project into a stream, and the ratio of experimental to reported return reframes every allocation decision.
