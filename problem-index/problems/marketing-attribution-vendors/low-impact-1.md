# Mix Model Specification and Identifiability

**Industry:** [[marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The technique is open source and the whole answer lives in specification choices — adstock, saturation, priors, controls — which are made by an analyst's judgement and reported as if the data produced them.
**Tags:** #bayesian-inference #variational-inference #mcmc-sampling #confidence-intervals #hypothesis-testing #cross-validation #regularization #evaluation-metrics

## The Problem
A marketing mix model requires a series of choices before it can be fit. How long does a channel's effect persist and with what decay. What shape is the saturation curve. Which competitive, macro and seasonal covariates enter. What priors constrain the coefficients. Whether to model at national or regional level. How to treat promotions, price and distribution.

Each choice changes the answer, sometimes dramatically, and the data is frequently too weak to prefer one over another. Channel spends are planned together and therefore move together; with two years of weekly data and eight collinear channels, the likelihood surface is close to flat across a wide region and the posterior is substantially the prior. That is not a failure of the analyst — it is the identification problem — but the output arrives as a contribution chart with no indication that a different defensible specification would have produced a different chart.

The practical result is that mix modelling results are sensitive to the modeller, and organisations that have switched vendors or analysts have seen contributions shift without the business changing.

## What Already Exists
The core technique has been commoditised by open source: Meta's Robyn, Google's Meridian and PyMC-Marketing all implement Bayesian mix models with adstock, saturation and hierarchical structure, and they are good. Commercial vendors — Recast, Prescient, the established econometrics houses — layer data engineering, workflow and consulting on top. Most tools offer some form of hyperparameter search over adstock and saturation, and Bayesian implementations report posterior intervals.

## The Customisation Gap
The tooling optimises within a specification; the uncertainty that matters is across specifications, and nothing reports it. A practitioner who fit two hundred defensible specifications and showed the distribution of contributions across them would be telling the client something true and useful — this channel's contribution is somewhere between these bounds under any reasonable model, this other one is entirely specification-dependent — and no product does this.

Identifiability diagnostics are the second gap. Which parameters the data actually informs is answerable: prior-versus-posterior contraction, collinearity structure among the spend series, and simulation-based checks that ask whether a known effect could be recovered from this data at all. Running those and reporting them prominently would prevent the most common failure in the field, which is treating a prior-driven estimate as evidence.

The genuinely per-client part is the business structure the model must encode: what a client's purchase cycle is, whether distribution or price changed, what the competitive set did, what internal events — a site migration, a stockout, a rebrand — contaminate the series. That knowledge sits with the client's team, is gathered in interviews, and is lost when the engagement ends.

And the priors should come from somewhere. A vendor with many clients can derive empirical priors by vertical and spend level from its own experimental results, which is both more defensible than an analyst's judgement and the natural use of a portfolio.

## Impact If Solved
Specification uncertainty is the dominant source of error in mix modelling and the least reported. Showing the range of answers consistent with the data, flagging where the prior is doing the work, and deriving priors empirically from pooled experiments turns a technique that varies with the modeller into one whose limits are visible. Given the core method is now free, this honesty layer is the remaining place a vendor can create value.
