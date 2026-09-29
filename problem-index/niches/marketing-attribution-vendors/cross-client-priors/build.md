# A Hundred Models and No Accumulated Knowledge

**Niche:** [[niches/marketing-attribution-vendors/cross-client-priors/profile|Cross-Client Priors]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A vendor has fitted a hundred models and run dozens of experiments, and the next client's priors come from whatever the assigned analyst remembers.
**Tags:** #bayesian-inference #monte-carlo-methods #confidence-intervals #hypothesis-testing #evaluation-metrics #causal-inference #regularization #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn a portfolio of clients into estimated priors that replace an analyst's judgement — and whoever does that makes every new engagement start from evidence instead of from an assumption.

## The Problem
The vendor has run measurement for a hundred businesses. Each engagement produced fitted parameters — channel effectiveness, adstock decay, saturation points — and some produced experimental results. Those hundred sets of estimates are a sample from a population of businesses, and that population is exactly what a prior for the hundred and first should be estimated from. Instead the analyst assigned to the new client picks priors from experience, which is an informal and unexamined version of the same inference, performed by one person from a subset they happen to remember, with no uncertainty attached.

## Why Nobody Has Built This
Client confidentiality is invoked as a blanket prohibition on anything cross-client, which is correct about raw data and wrong about abstracted parameters — the conflation is what has prevented this and it is resolvable by design. Engagements are organised as separate projects with no shared parameter store. Nobody is accountable for the firm's accumulated knowledge. And the informal version works well enough that its absence is not felt.

## What to Build
Estimate the priors from the portfolio. Retain fitted parameters from every engagement in a structured, abstracted form — vertical, business model, spend scale, channel, parameter, uncertainty — which is the foundation and is the step that converts a hundred projects into a dataset. Fit a hierarchical model across clients, which is the correct statistical treatment and yields both a population distribution and a shrinkage estimate for each new client. Abstract sufficiently that no client is identifiable, which resolves the confidentiality objection properly rather than using it as a reason to keep nothing. Use experimental results as the strongest input, since they identify what observational fits cannot and are the scarcest and most valuable element of the portfolio. Provide priors with their own uncertainty, so a new model knows how much to trust them and the prior does not silently dominate. Report where the portfolio has evidence and where it does not, since a prior for a well-represented vertical and one for a novel business are different things and should not look alike. Shorten new engagements, because a defensible starting point removes months of the calibration period and is the commercial argument. Update continuously as engagements complete, so the asset compounds. Publish population-level findings, which is a marketing asset and a contribution to a field that has almost no empirical base. And validate the priors against subsequent outcomes, since an unchecked prior is an analyst's recollection with a standard deviation.

## Target Customer
Measurement vendors with client portfolios, large advertisers with many business units, and the marketing science community operating without an empirical base.

## Impact If Built
An analyst picking priors from memory is an informal version of the inference the portfolio could do formally, with no uncertainty attached. Abstracted hierarchical estimation resolves the confidentiality objection and turns a hundred separate projects into evidence for the hundred and first.
