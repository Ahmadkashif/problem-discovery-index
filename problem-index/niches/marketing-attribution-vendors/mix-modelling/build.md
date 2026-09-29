# The Answer Lives in the Specification

**Niche:** [[niches/marketing-attribution-vendors/mix-modelling/profile|Mix Modelling]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The technique is open source and the whole answer lives in specification choices — adstock, saturation, priors, controls — which are made by an analyst's judgement and reported as if the data produced them.
**Tags:** #bayesian-inference #causal-inference #time-series-forecasting #confidence-intervals #monte-carlo-methods #hypothesis-testing #evaluation-metrics #regularization
**Contested on:** Every serious competitor in this niche is fighting to separate channels whose spends move together, from a series that is too short to do it — and whoever handles that identification problem honestly replaces answers that are mostly priors.

## The Problem
Two channels were increased together every quarter for three years because that is how the budget was planned. The model is asked to say what each contributed. There is no variation in the data that separates them, so the separation comes from the adstock assumption, the saturation curve shape, the control variables chosen and the prior placed on each channel's effect. Change any of those within a defensible range and the contributions move substantially. The client receives one set of numbers with a confident interval, and the interval reflects sampling uncertainty within a chosen specification rather than uncertainty about the specification, which is where nearly all the real uncertainty lives.

## Why Nobody Has Built This
The technique became accessible through open-source implementations, which democratised the modelling and not the judgement — the hard part was always specification and the tooling made everything except that easy. Reporting specification uncertainty makes the answer look far less precise. A wide range is hard to act on and clients want a number. And analysts making these choices are often not the ones who will be held to the result.

## What to Build
Make the specification the object of analysis. Report results across the full space of defensible specifications rather than from one chosen model, which is the fix and turns a hidden judgement into a visible range — the honest output of an underdetermined problem is a range, and presenting one is the differentiator. Quantify how much of each contribution comes from the data and how much from the prior, which is directly computable and is the disclosure that would change how these models are read. Diagnose identification explicitly, flagging channel pairs that the data cannot separate, since telling a client which questions their data cannot answer is more valuable than a confident answer to all of them. Use experiments to pin the parameters the data cannot identify, which is the correct use of a scarce experimental budget and connects to the validation work. Deliberately vary spend to create identification, which is a planning recommendation rather than a modelling one and is the only durable solution to collinear channels. Bring cross-client priors in where they are defensible, connecting to the priors niche, since a prior estimated from many businesses is better than one an analyst chose. Validate on contribution rather than on outcome fit, because a model can fit a revenue series perfectly with wrong contributions and usually does. Version the specification with its rationale, so the choices are auditable. Automate the sensitivity sweep so it is routine rather than a special exercise. And publish the method, since specification transparency is the one thing an open-source technique cannot commoditise.

## Target Customer
Measurement vendors, client measurement and finance functions, and the marketing science community adopting open-source implementations without the judgement they require.

## Impact If Built
The tooling democratised everything except the judgement, and the judgement is where the answer comes from. Reporting across defensible specifications and quantifying prior-versus-data contribution turns a hidden choice into a visible range and tells clients which questions their data cannot answer.
