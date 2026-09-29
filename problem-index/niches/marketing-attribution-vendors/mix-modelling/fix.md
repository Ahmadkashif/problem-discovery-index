# The Prior That Produced the Result

**Niche:** [[niches/marketing-attribution-vendors/mix-modelling/profile|Mix Modelling]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The model's channel contribution is close to the prior it was given, the data barely moved it, and the output is presented as a finding.
**Tags:** #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #monte-carlo-methods #quick-win #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to separate channels whose spends move together, from a series that is too short to do it — and whoever handles that identification problem honestly replaces answers that are mostly priors.

## The Problem
A Bayesian mix model is given priors on each channel's effectiveness, drawn from the analyst's experience or from a benchmark. For channels with strong variation in the data, the posterior moves well away from the prior and the model has learned something. For channels whose spend barely varied, the posterior sits almost exactly on the prior — the data contributed nothing and the output is the assumption restated with a credible interval around it. Both appear identically in the report. A client reading the contributions cannot tell which numbers their own data produced and which were supplied by the modeller.

## Why It's Still Broken
Posterior output looks the same regardless of how much the data informed it, which means the distinction is invisible unless it is deliberately computed — and nobody computes it. Bayesian methods are presented as principled, which they are, and the presentation obscures that a weakly identified parameter returns its prior. Disclosing which results are prior-driven weakens the deliverable. And clients do not know to ask.

## What a Fix Looks Like
Show how much the data moved each estimate. Report prior-to-posterior movement per parameter, which is the fix, is a one-line computation from output every Bayesian model already produces, and immediately separates what was learned from what was assumed. Flag parameters whose posterior is effectively the prior, since those contributions are assumptions and should be labelled as such in the report. Disclose the priors and their source, because a prior from a published benchmark and one from an analyst's intuition are different and clients are told neither. Run the model under alternative reasonable priors and report the spread, which is the sensitivity analysis that should accompany every Bayesian result and rarely does. Use cross-client empirical priors where available, connecting to the priors niche, since an estimated prior is defensible where a chosen one is a judgement. Explain in plain terms which channels the client's own data can speak to, which is genuinely useful and reframes the engagement honestly. Recommend the spend variation that would identify the weak parameters, turning a limitation into a plan. Keep the prior specification under version control with its rationale. Teach clients to ask how much the data moved this, since a single question changes what vendors must be prepared to answer. And report the share of total contribution that is prior-driven, because a model whose answer is mostly assumption should say so.

## Who Feels the Pain
Clients acting on assumptions presented as findings; analysts who know which numbers are prior-driven and have nowhere to say it; and the category, whose most respected method is opaque about where its answers come from.

## Impact If Fixed
A posterior looks the same whether the data informed it or not, so a weakly identified parameter returns its prior invisibly. Prior-to-posterior movement is a one-line computation from output every model already produces and separates what was learned from what was assumed.
