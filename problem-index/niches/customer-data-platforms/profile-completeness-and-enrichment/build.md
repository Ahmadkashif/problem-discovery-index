# Buying What You Could Infer

**Niche:** [[niches/customer-data-platforms/profile-completeness-and-enrichment/profile|Profile Completeness & Enrichment]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Organisations buy third-party attributes of unknown accuracy to fill gaps their own behavioural data would predict better, and measure completeness against a schema nobody asked for.
**Tags:** #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #compliance #k-nearest-neighbors #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to say what is missing from a profile and what can be inferred rather than bought — and whoever does that replaces a third-party data purchase with the organisation's own observations.

## The Problem
A profile is missing a life-stage attribute, a category affinity and a channel preference. The organisation buys these from a data provider at meaningful cost, with accuracy nobody has verified, under privacy terms that are becoming harder to sustain. Meanwhile the same organisation has observed this customer's purchases, browsing, timing, device use and response history for three years — from which the same attributes are frequently predictable with better accuracy than the purchased ones, at no marginal cost, entirely within their own first-party data and consent boundary.

## Why Nobody Has Built This
Enrichment was established as a purchasing relationship, and buying is procurement while inferring is a project — the organisational path of least resistance runs through a vendor. Purchased attributes arrive as facts and inferred ones as probabilities, which feels weaker despite frequently being better. Nobody has validated either against ground truth. And data providers sell completeness as a metric that their own product improves.

## What to Build
Infer from what is already observed. Predict the missing attributes from first-party behaviour with calibrated confidence, which is the core and is a well-posed supervised problem wherever a subset of customers have the attribute known. Validate inferences against the known subset, which gives a genuine accuracy figure and is the comparison that makes the case against purchasing. Validate purchased attributes the same way, since almost nobody does and the results are frequently unflattering to the purchase. Measure completeness against what is actually used rather than against a schema, because an unfilled field nothing consumes is not a gap and the standard completeness percentage is mostly noise. Prioritise the gaps that affect outcomes, so effort goes where it produces something. Model staleness explicitly, as an attribute captured three years ago may be worse than an inference from last month's behaviour. Use progressive profiling intelligently, asking the customer only for what cannot be inferred and matters, which respects their time and improves response. Keep inferences flagged as inferences with their confidence, so downstream consumers can decide and a probabilistic attribute is never mistaken for a stated one. Handle the privacy position, since inference from first-party data sits differently from a third-party append and that difference is increasingly the deciding factor. And report the cost of purchased data against its measured incremental accuracy, because that comparison decides the budget and nobody currently runs it.

## Target Customer
Data and marketing leadership buying third-party enrichment, customer data platform vendors, and the organisations whose own behavioural data is better than what they purchase.

## Impact If Built
Buying is procurement and inferring is a project, so the organisational path of least resistance runs through a vendor. Validating both inferred and purchased attributes against a known subset produces the accuracy comparison that decides the budget and that nobody currently runs.
