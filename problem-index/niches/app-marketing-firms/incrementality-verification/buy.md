# Geo Experimentation Practice

**Niche:** [[niches/app-marketing-firms/incrementality-verification/profile|Incrementality Verification]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Geographic experimentation with synthetic controls is well developed in web advertising and economics, and app marketing treats each test as a bespoke project.
**Tags:** #causal-inference #hypothesis-testing #monte-carlo-methods #confidence-intervals #evaluation-metrics #time-series-forecasting #bayesian-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to establish how much of a reported return survives an experiment — and whoever does that in a channel where attribution is aggregated supplies the only number anyone can actually trust.

## The Problem
Geographic experimentation is a developed practice. Matched market design, synthetic control construction, difference-in-differences estimation and the open-source tooling around them are used routinely in web advertising measurement and in policy evaluation. The methods handle small numbers of units, pre-period matching and inference with few clusters. App marketing needs exactly this and mostly builds each test from first principles, which is why so few get run.

## What Already Exists
Matched market and geo holdout design; synthetic control methods with open implementations; difference-in-differences with clustered inference; pre-period matching and placebo testing; and power analysis for small-unit designs.

## The Customization Gap
The adaptation is to geography defined by app store regions and to an outcome measured through the attribution constraint. It requires: (1) geographic granularity limited by what the ad platforms and the store expose, which is coarser than web advertising's and reduces the number of available units — fewer units is the binding statistical constraint and shapes every design decision; (2) outcome measurement through the store and the aggregated signal rather than through the advertiser's own site analytics, which adds noise and lag to the dependent variable; (3) spillover between regions through organic discovery and store ranking, which violates the independence assumption more strongly than in web advertising; (4) store ranking effects that make suppression in one region affect organic performance, so the treatment has an indirect channel; and (5) short campaign lifecycles, which limits the pre-period available for matching.

## Target Customer
User acquisition teams and agencies, measurement vendors, and experimentation practitioners for whom the app channel is an unserved application.

## Impact If Solved
The methods are developed and the tooling is open, and app marketing rebuilds each test from scratch. Fewer available geographic units is the binding statistical constraint, and store ranking spillover gives the treatment an indirect channel the web designs do not contend with.
