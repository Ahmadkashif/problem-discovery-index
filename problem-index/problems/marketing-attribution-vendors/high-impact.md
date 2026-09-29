# Selling a Causal Answer With No Way to Check It

**Industry:** [[marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** High Impact
**One-liner:** The product is a number that reallocates a marketing budget, derived from observational data, and essentially nobody in the category backtests it against an experiment that could show it was wrong.
**Tags:** #causal-inference #bayesian-inference #hypothesis-testing #confidence-intervals #cross-validation #monte-carlo-methods #evaluation-metrics #revenue-impact

## The Problem
An attribution vendor delivers channel contributions: this much revenue came from paid search, this much from social, this much from the baseline. A client moves millions of dollars on that output. The number is produced from observational data — spend, impressions, conversions, seasonality, competitive and macro covariates — by a model that must assume something to identify a causal effect from correlation.

There is no accepted validation. Model fit is reported as in-sample or holdout fit on the historical series, which measures whether the model explains past revenue, not whether its causal decomposition is correct. Two specifications can fit almost identically and attribute a channel's contribution differently by a factor of two, because the data is close to uninformative about the split and the difference comes from priors, adstock assumptions or saturation curves. Fit does not discriminate between them; only an experiment does.

So the category ships uncheckable numbers with confident interfaces. Clients notice when two vendors disagree, and are told to triangulate — an appealing word for averaging estimates whose biases are unknown and quite possibly correlated. Meanwhile the experiments that would adjudicate are run occasionally, on one channel, and their results are used to argue about the model rather than to systematically correct it.

The pattern that should worry the category is the recurring one where a business runs a genuine geo holdout on a channel its model credited heavily and finds a small fraction of the modelled effect. That result is common enough to be folklore in the industry and rare enough in published form that nobody has to account for it.

## Why It's Unsolved
Validation exposes error, and error is the product's weakness. A vendor that publishes how often its predictions were contradicted by subsequent experiments is competing against vendors that do not, in a sales process where the buyer is a marketing leader who wants a defensible number for a board deck. The market currently rewards confidence over calibration.

There are honest difficulties too. Experiments are expensive in withheld spend, slow, and underpowered at most advertisers' scale — a mid-sized business testing a mid-sized channel often cannot detect anything short of a very large effect. Running enough experiments to validate a model across channels, seasons and spend levels is beyond any single advertiser's budget. That argues for pooling across clients, which requires a vendor willing to build a shared evidence base rather than a per-client model.

And the underlying identification problem is real. Marketing spends move together because budgets are planned together; separating collinear channels from observational data is close to impossible without either experimental variation or strong assumptions that are doing the identification themselves. Practitioners know this. The interfaces do not say it.

Lastly, the incentive at the client is not neutral either. A model that credits a channel generously validates the decisions of the person who bought it, and an attribution finding that reallocates budget away from someone's channel is a political event before it is an analytical one.

## What a Solution Looks Like
Invert the hierarchy. Treat randomised experiments as the ground truth and every model as an interpolator between the experiments that exist, explicitly scored on how well it predicted the last one it did not see. That single reframing — model validated against experiment, continuously, with the record visible — is the product the category lacks and the one a serious buyer would prefer.

Make experiments continuous rather than occasional. Rotating geo holdouts, staggered launches, matched-market spend variation and deliberate budget perturbation produce a stream of causal estimates at modest cost when designed as a permanent programme rather than as a project. Each one both answers its own question and becomes a validation point for the model.

Pool across clients to get power. A vendor with two hundred advertisers can accumulate experimental estimates across channels, verticals, spend levels and seasons, and fit a hierarchical model whose priors are empirical rather than assumed. That is how a small advertiser gets a defensible answer despite having no power of their own, and it is the one thing a vendor can build that a client cannot.

Report identifiability honestly. Where two channels moved together and the data cannot separate them, say so, show the range of contributions consistent with the data, and recommend the experiment that would resolve it. A measurement product whose output includes "we cannot currently distinguish these two, here is what would" is more useful than one that silently lets a prior decide.

## Impact If Solved
This category's output reallocates a very large share of US marketing spend, on numbers whose error rate nobody measures. A continuously validated, experiment-anchored measurement layer changes the allocation and, more importantly, changes what advertisers can demand — a vendor with a published track record against experimental ground truth resets the basis of competition from interface confidence to demonstrated accuracy. For the vendor willing to go first, it is the only durable moat available in a field where the core technique is now open source.
